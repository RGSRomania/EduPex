# 🎯 QUICK REFERENCE - EduPex Lesson Format (v1.0)

**Status:** ✅ PRODUCTION READY | **Date:** January 20, 2026

---

## 📚 Lesson Structure (Template)

```
Lesson:
├─ Title: "LX - Lecția X"
├─ Summary: "Brief lesson topic description"
├─ Content:
│  ├─ Theory: "200-600 characters explaining concept"
│  ├─ Examples: [
│  │    "Example 1",
│  │    "Example 2",
│  │    "Example 3"
│  │  ]
│  └─ Tips: [
│       "Tip 1",
│       "Tip 2",
│       "Tip 3"
│     ]
└─ Question:
   ├─ question: "Clear, specific question about lesson"
   └─ options: [
        { text: "Correct answer", isCorrect: true, explanation: "..." },
        { text: "Wrong answer 1", isCorrect: false, explanation: "..." },
        { text: "Wrong answer 2", isCorrect: false, explanation: "..." },
        { text: "Wrong answer 3", isCorrect: false, explanation: "..." }
      ]
```

---

## ✅ Content Requirements

| Component | Min | Max | Required |
|-----------|-----|-----|----------|
| **Theory** | 200 ch | 600 ch | ✅ Yes |
| **Examples** | 1 | 4 | ✅ Yes |
| **Tips** | 2 | 4 | ✅ Yes |
| **Options** | 4 | 4 | ✅ Yes |
| **Correct Answers** | 1 | 1 | ✅ Yes |

---

## ❌ What NOT to Do

- ❌ Generic questions ("Întrebare de bază pentru L4")
- ❌ Questions unrelated to lesson
- ❌ More than 4 options
- ❌ Multiple correct answers
- ❌ Missing explanations
- ❌ Out-of-date content
- ❌ Breaking the structure
- ❌ Inconsistent formatting

---

## ✅ What TO Do

- ✅ Create lesson-SPECIFIC questions
- ✅ Match question to lesson topic
- ✅ Always 4 options, 1 correct
- ✅ Include explanations
- ✅ Use proper Romanian
- ✅ Follow the template exactly
- ✅ Test before deploying
- ✅ Update backup file

---

## 📊 Current Statistics

```
Total Lessons: 108
├─ Matematica: 51 lessons
│  ├─ Theory: 51/51 ✅
│  ├─ Examples: 51/51 ✅
│  ├─ Tips: 51/51 ✅
│  └─ Questions: 51/51 ✅
│
└─ Limba Română: 57 lessons
   ├─ Theory: 57/57 ✅
   ├─ Examples: 57/57 ✅
   ├─ Tips: 57/57 ✅
   └─ Questions: 57/57 ✅
```

---

## 🔗 Key Files

| File | Purpose | Location |
|------|---------|----------|
| `LESSON_FORMAT_SPECIFICATION.md` | Technical specification | Root |
| `CURRENT_FORMAT_SAVED.md` | Usage & maintenance guide | Root |
| `FORMAT_SAVED_SUMMARY.txt` | Quick summary | Root |
| `LESSONS_BACKUP_2026-01-20.json` | Data backup (257 KB) | backend/ |

---

## 🚀 Common Tasks

### Add New Lesson
```
1. Create Lectie document (with theory, examples, tips)
2. Create LectieQuestion (with 4 options)
3. Link question to lesson (lectieId)
4. Test thoroughly
5. Deploy
6. Run: node backend/export_current_lessons.js (backup)
```

### Fix Existing Lesson
```
1. Update content in Lectie
2. Check if question still matches
3. Update question if needed
4. Verify quality standards
5. Test changes
6. Deploy
7. Create new backup
```

### Backup Lessons
```
cd backend
node export_current_lessons.js
# Creates: LESSONS_BACKUP_YYYY-MM-DD.json
```

### Check Format
```
Review LESSON_FORMAT_SPECIFICATION.md
OR
Check LESSONS_BACKUP_2026-01-20.json for examples
```

---

## 📋 Quality Checklist (Before Deployment)

- [ ] Title follows "LX - Lecția X" format
- [ ] Summary describes lesson topic clearly
- [ ] Theory: 200-600 characters, clear explanation
- [ ] Examples: 1-4 practical, progressively complex
- [ ] Tips: 2-4 practical, encouraging tone
- [ ] Question: Lesson-SPECIFIC (not generic)
- [ ] Options: Exactly 4, 1 correct, 3 realistic incorrect
- [ ] Explanations: Clear for all options
- [ ] Language: Proper Romanian, age-appropriate
- [ ] Content Match: All parts relate to lesson
- [ ] No typos: Grammar and spelling correct
- [ ] Tested: Works in frontend

---

## 🎓 Example Format

### Matematica Example
```
Title: L2 - Lecția 2
Summary: Adunarea și scăderea numerelor naturale

Theory: (200-600 chars)
Adunarea numerelor naturale:
- Operația inversă scăderii
- Termeni: numerele care se adună
- Sumă: rezultatul adunării
Proprietatea comutativă: a + b = b + a
Exemplu: 3 + 5 = 5 + 3 = 8

Examples: [
  "3 + 5 = 8 (termenii: 3 și 5; suma: 8)",
  "5 + 3 = 8 (comutativă)",
  "(2 + 3) + 4 = 5 + 4 = 9"
]

Tips: [
  "Folosește proprietatea comutativă",
  "Grupează numerele care se adună ușor",
  "Verifică prin efectuarea în cealaltă ordine"
]

Question: "Dacă aduni 15 + 27, care este rezultatul?"
✅ 42 - Corect! 15 + 27 = 42
❌ 40 - Incorect. Calculeaza din nou.
❌ 45 - Incorect. Calculeaza din nou.
❌ 35 - Incorect. Calculeaza din nou.
```

### Limba Română Example
```
Title: L1 - Lecția 1
Summary: Comunicare și limba - procesul comunicării

Theory: (200-600 chars)
Comunicarea este schimbul de mesaje între persoane.

ELEMENTELE PROCESULUI DE COMUNICARE:
1. Emițător (vorbitor/autor)
2. Receptor (ascultător/cititor)
3. Mesaj (informația transmisă)
4. Canal (calea de transmitere)
5. Context (situația comunicării)

Examples: [
  "Comunicare verbală: conversație între prieteni",
  "Comunicare non-verbală: gesturi",
  "Comunicare scrisă: e-mail",
  "Comunicare digitală: mesaj pe rețea"
]

Tips: [
  "Ascultă cu atenție",
  "Exprimă-te clar",
  "Respectă opinia celui cu care comunici"
]

Question: "Care sunt elementele esențiale ale procesului de comunicare?"
✅ Emițător, receptor, mesaj, canal și context - Corect!
❌ Doar emițător și receptor - Incorect
❌ Doar mesajul - Incorect
❌ Doar contextul - Incorect
```

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| Question doesn't match lesson | Review question content, update to match lesson topic |
| Missing explanations | Add explanation field for each option |
| Too few/many examples | Adjust to 1-4 range |
| Generic question | Replace with lesson-specific question |
| Content too long | Trim theory to 200-600 characters |
| Quality issues | Review checklist above |

---

## 📞 Getting Help

1. **Format questions:** Check `LESSON_FORMAT_SPECIFICATION.md`
2. **Usage questions:** Check `CURRENT_FORMAT_SAVED.md`
3. **Quick reference:** Check `FORMAT_SAVED_SUMMARY.txt`
4. **Data examples:** Check `LESSONS_BACKUP_2026-01-20.json`
5. **Maintenance:** Review each file's maintenance section

---

## 🔒 Format Lock

This format is **LOCKED v1.0** as of January 20, 2026.

All new lessons must follow this specification exactly.
Updates to this format require version bump and documentation.

**Next Review:** After 50 new lessons or 6 months

---

**Status:** ✅ PRODUCTION READY
**Total Lessons:** 108
**Success Rate:** 100%

