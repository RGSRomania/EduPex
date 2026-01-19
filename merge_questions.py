#!/usr/bin/env python3
"""
Merge Questions with Lesson Structure
This script takes the lesson structure and adds generated/extracted questions
"""

import json
import os

def load_lesson_structure():
    """Load the Matematica Clasa 5 lesson structure"""
    with open("Matematica_Clasa_5_Complete.json", "r", encoding="utf-8") as f:
        return json.load(f)

def merge_questions_with_lessons(lessons_data, questions_data):
    """Merge questions into the lesson structure"""

    # This is a mapping of lesson names to questions
    lessons_data["questions_status"] = {
        "total_lessons": 55,
        "lessons_with_questions": 0,
        "questions_total": 0
    }

    return lessons_data

# Load the base lesson structure
print("📚 Loading Matematica Clasa 5 lesson structure...")
lessons = load_lesson_structure()

print(f"✅ Loaded {lessons['unitati'].__len__()} unitati")
print(f"✅ Total lessons ready for questions\n")

# Count lessons
total_lessons = 0
for unitate in lessons['unitati']:
    for capitol in unitate['capitole']:
        total_lessons += len(capitol['lectii'])

print(f"📊 Total Lessons: {total_lessons}")
print("🎯 Status: Ready for question import\n")

# Save merged structure
output_path = "Matematica_Clasa_5_With_Questions_Ready.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)

print(f"✅ Lesson structure saved: {output_path}")
print("\n📋 Next Steps:")
print("1. Extract questions from Manual.pdf")
print("2. Map questions to lessons")
print("3. Import to database with questions")
print("4. Build frontend UI")
print("5. Deploy to mobile APK\n")

