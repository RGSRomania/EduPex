#!/usr/bin/env python3
import os
import json
import re
try:
    import PyPDF2
except ImportError:
    os.system("pip install PyPDF2")
    import PyPDF2
def extract_cuprins_from_pdf(pdf_path):
    """Extract table of contents from PDF"""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            # Find the Cuprins page
            for page_num, page in enumerate(pdf_reader.pages[:20]):
                text = page.extract_text()
                if 'CUPRINS' in text.upper():
                    # Found cuprins, continue extracting until next major section
                    full_text = text
                    # Get next few pages to capture all content
                    for i in range(page_num + 1, min(page_num + 10, len(pdf_reader.pages))):
                        next_text = pdf_reader.pages[i].extract_text()
                        # Stop if we hit a new major section
                        if any(keyword in next_text.upper() for keyword in ['LECȚIA', 'LECTIA', 'SITUAȚIE']):
                            break
                        full_text += "\n" + next_text
                    return full_text
            return ""
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return ""
def parse_cuprins_text(text):
    """Parse extracted text to find unitati and lectii with their exact names"""
    unitati = []
    current_unitate = None
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        i += 1
        if not line:
            continue
        # Match U# format for Unitati  (e.g., "U1 Operații cu numere naturale")
        unitate_match = re.match(r'^U(\d+)\s+(.+)$', line)
        if unitate_match:
            unit_num = unitate_match.group(1)
            unit_name = unitate_match.group(2).strip()
            current_unitate = {
                'number': unit_num,
                'name': unit_name,
                'lectii': []
            }
            unitati.append(current_unitate)
            continue
        # Match Lecția # format (e.g., "Lecția 1 10 Scrierea și citirea numerelor naturale")
        lectie_match = re.match(r'^Lecția\s+(\d+)\s+(\d+)\s+(.+)$', line)
        if lectie_match and current_unitate:
            lectie_num = lectie_match.group(1)
            # page_num = lectie_match.group(2)  # We can ignore page numbers
            lectie_name = lectie_match.group(3).strip()
            current_unitate['lectii'].append({
                'number': lectie_num,
                'name': lectie_name
            })
            continue
        # Handle multi-line lectii (some have page breaks)
        lectie_match2 = re.match(r'^Lecția\s+(\d+)\s+(\d+)\s*(.*)$', line)
        if lectie_match2 and current_unitate:
            lectie_num = lectie_match2.group(1)
            lectie_name = lectie_match2.group(3).strip()
            # If name is incomplete, check next line
            if lectie_name and not lectie_name.endswith(('ordinare', 'natural', 'naturale', 'măsură', 'dreptunghi')):
                if i < len(lines):
                    next_line = lines[i].strip()
                    if not next_line[0].isdigit() and 'Lecția' not in next_line:
                        lectie_name += " " + next_line
                        i += 1
            if lectie_name:  # Only add if we have a name
                current_unitate['lectii'].append({
                    'number': lectie_num,
                    'name': lectie_name
                })
    return unitati
def main():
    base_path = "/Users/mdica/PycharmProjects/EduPex/Planificari + Manual + Culegeri"
    # Get actual folder names
    classes = []
    for item in os.listdir(base_path):
        if os.path.isdir(os.path.join(base_path, item)) and item.startswith("Clasa"):
            classes.append(item)
    curriculum = {}
    for class_name in sorted(classes):
        print(f"\n{class_name}:")
        class_path = os.path.join(base_path, class_name)
        curriculum[class_name] = {}
        # Get actual subject folder names
        for subject_folder in sorted(os.listdir(class_path)):
            subject_path = os.path.join(class_path, subject_folder)
            if not os.path.isdir(subject_path):
                continue
            pdf_path = os.path.join(subject_path, "Manual.pdf")
            if not os.path.exists(pdf_path):
                print(f"  ✗ {subject_folder} - Manual.pdf not found")
                continue
            print(f"  Extracting: {subject_folder}...")
            text = extract_cuprins_from_pdf(pdf_path)
            if not text:
                print(f"    ✗ Could not extract Cuprins")
                continue
            unitati = parse_cuprins_text(text)
            if unitati:
                curriculum[class_name][subject_folder] = unitati
                total_lectii = sum(len(u['lectii']) for u in unitati)
                print(f"    ✓ Found {len(unitati)} unitati with {total_lectii} lectii")
                for u in unitati[:2]:  # Show first 2
                    print(f"      - UNITATEA {u['number']}: {u['name'][:50]}... ({len(u['lectii'])} lectii)")
                if len(unitati) > 2:
                    print(f"      ... and {len(unitati)-2} more unitati")
            else:
                print(f"    ✗ Could not parse unitati")
    output_path = "/Users/mdica/PycharmProjects/EduPex/curriculum_structure.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(curriculum, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Curriculum structure saved to: {output_path}")
    print(f"Total classes extracted: {len(curriculum)}")
    # Summary
    total_unitati = sum(len(subjects) for subjects in curriculum.values() for subjects in subjects.values() if isinstance(subjects, list))
    print(f"Total unitati: {total_unitati}")
if __name__ == "__main__":
    main()
