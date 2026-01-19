#!/usr/bin/env python3
"""
Extract questions from Matematica Manual PDF and create a structured JSON
"""

import os
import sys

pdf_path = "/Users/mdica/PycharmProjects/EduPex/Planificari + Manual + Culegeri/Clasa a V a/Matematica/Manual.pdf"

# Check if file exists
if not os.path.exists(pdf_path):
    print(f"❌ PDF not found at: {pdf_path}")
    sys.exit(1)

print(f"✅ PDF found: {pdf_path}")
print(f"File size: {os.path.getsize(pdf_path) / 1024 / 1024:.2f} MB")

try:
    import pdfplumber
    print("\n📖 Opening PDF with pdfplumber...")

    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        print(f"✅ PDF has {total_pages} pages\n")

        # Extract all text
        all_text = ""
        for i, page in enumerate(pdf.pages):
            try:
                text = page.extract_text()
                all_text += f"\n--- PAGE {i+1} ---\n{text}\n"
            except Exception as e:
                print(f"⚠️  Error extracting page {i+1}: {e}")

        # Save to file
        output_path = "/Users/mdica/PycharmProjects/EduPex/Manual_Matematica_5_EXTRACTED.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(all_text)

        print(f"✅ Extracted {len(all_text)} characters")
        print(f"✅ Saved to: {output_path}\n")

        # Show preview
        preview = all_text[:3000]
        print("=== PREVIEW (first 3000 chars) ===\n")
        print(preview)
        print("\n" + "="*50)

except ImportError:
    print("❌ pdfplumber not installed")
    print("Installing: pip3 install pdfplumber pypdf")
    os.system("pip3 install pdfplumber pypdf -q")
    print("Please run this script again")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

