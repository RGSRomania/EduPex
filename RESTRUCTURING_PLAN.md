# RESTRUCTURING PLAN - CORRECT CURRICULUM ARCHITECTURE

## WHAT WAS WRONG:
- Previous files had 1 UNIT with 13 lessons (INCORRECT)
- Should have 6 UNITS (for Clasa V Math) with multiple lessons each
- Each UNIT is called "UNITATEA" with its own lessons

## WHAT'S NEEDED NOW:

### For EACH subject/grade combination, I need to:
1. Extract the EXACT chapter names (UNITATEA 1, 2, 3...)
2. Extract the EXACT lesson names (L1, L2, L3...) for each unit
3. Build JSON with correct hierarchy

### Clasa V - Matematica (from Cuprins):
- UNITATEA 1: 13 lessons (L1-L13)
- UNITATEA 2: 5 lessons (L1-L5)
- UNITATEA 3: 3 lessons (L1-L3)
- UNITATEA 4: 10 lessons (L1-L10)
- UNITATEA 5: 9 lessons (L1-L9)
- UNITATEA 6: 11 lessons (L1-L11)
**TOTAL: 51 lessons** (NOT 13!)

### Clasa V - Limba și literatura română:
- Needs to be extracted from that PDF's Cuprins
- Will have different number of units and lessons

### Clasa VI, VII, VIII - Same approach for both subjects

## ACTION ITEMS:
1. Get exact structure from each PDF Cuprins
2. Rebuild all 8 JSON files with CORRECT multi-unit structure
3. Populate with actual content from the PDFs

## NEXT STEPS:
- I will create one CORRECT template for each class/subject
- Then populate with content from extracted PDFs

