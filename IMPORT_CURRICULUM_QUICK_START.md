# 🚀 QUICK START: IMPORT CURRICULUM TO BACKEND

## What This Does

This script reads all 8 `*_CORRECT.json` curriculum files and imports them into your MongoDB database, creating:
- ✅ 2 Subjects (Matematica, Limba Română)
- ✅ 8 Grades (V, VI, VII, VIII)
- ✅ 48 Units
- ✅ 463 Lessons
- ✅ 463 Questions (4 options each)

---

## Prerequisites

Before running the import script, ensure:

### 1. **MongoDB is running**
```bash
# Check if MongoDB is running
mongosh

# If not running, start it (on macOS with Homebrew):
brew services start mongodb-community
```

### 2. **Backend is set up**
```bash
cd backend
npm install  # if not already done
```

### 3. **Environment variables are configured**

Check `backend/.env` has:
```
MONGODB_URI=mongodb://localhost:27017/edupex
```

Or if using MongoDB Atlas:
```
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/edupex
```

---

## Run the Import

### Step 1: Copy JSON files to root directory

The import script looks for `*_CORRECT.json` files in the root of the project:
```bash
# Make sure these files exist in /Users/mdica/PycharmProjects/EduPex/
ls Matematica_Clasa_V_CORRECT.json
ls LimbaRomana_Clasa_V_CORRECT.json
```

### Step 2: Run the import script

```bash
# From the root directory (EduPex folder)
node backend/scripts/importCurriculum.js
```

### Expected Output

```
================================================================================
🚀 STARTING CURRICULUM IMPORT
================================================================================

📚 Step 1: Creating Materii (Subjects)...
   ✅ Created: Matematica
   ✅ Created: Limba și literatura română

📖 Step 2: Importing Curriculum Files...

   📄 Processing: Matematica_Clasa_V_CORRECT.json
      ✅ Created Clasa: V
      ✅ Matematica Clasa V imported successfully
      
   📄 Processing: Matematica_Clasa_VI_CORRECT.json
      ✅ Created Clasa: VI
      ✅ Matematica Clasa VI imported successfully
      
   ... (continues for all 8 files)

================================================================================
📊 IMPORT SUMMARY
================================================================================

Materii created:     2
Clase created:       8
Unitati imported:    48
Capitole created:    48
Lectii imported:     463
Questions created:   463

✅ NO ERRORS - Import completed successfully!

================================================================================
🎉 CURRICULUM IMPORT COMPLETE
================================================================================
```

---

## Verify the Import

### Option 1: Using MongoDB Compass (GUI)

1. Open MongoDB Compass
2. Connect to `mongodb://localhost:27017`
3. Find database `edupex`
4. Check collections:
   - `materies` - Should have 2 documents
   - `clasas` - Should have 8 documents
   - `unitatedeinavtares` - Should have 48 documents
   - `lecties` - Should have 463 documents
   - `lectiequestions` - Should have 463 documents

### Option 2: Using MongoDB Shell

```bash
mongosh

# Connect to database
use edupex

# Count documents in each collection
db.materies.countDocuments()        # Should be 2
db.clasas.countDocuments()          # Should be 8
db.unitatedeinavtares.countDocuments()  # Should be 48
db.lecties.countDocuments()         # Should be 463
db.lectiequestions.countDocuments() # Should be 463

# View a lesson example
db.lecties.findOne()

# View a question example
db.lectiequestions.findOne()

# Exit
exit
```

---

## Troubleshooting

### Error: "Cannot find module 'mongoose'"

**Solution:**
```bash
cd backend
npm install
```

### Error: "MONGODB_URI not set"

**Solution:**
Add to `backend/.env`:
```
MONGODB_URI=mongodb://localhost:27017/edupex
```

### Error: "connect ECONNREFUSED 127.0.0.1:27017"

**Solution:**
MongoDB is not running. Start it:
```bash
brew services start mongodb-community
```

### Error: "File not found: .../Matematica_Clasa_V_CORRECT.json"

**Solution:**
The JSON files must be in the root directory:
```
/Users/mdica/PycharmProjects/EduPex/Matematica_Clasa_V_CORRECT.json
/Users/mdica/PycharmProjects/EduPex/Matematica_Clasa_VI_CORRECT.json
... etc
```

Make sure files are named exactly `*_CORRECT.json`

---

## Re-importing (If You Need To)

### To clear and re-import:

```bash
# Drop the database
mongosh
> use edupex
> db.dropDatabase()
> exit

# Run import again
node backend/scripts/importCurriculum.js
```

---

## Next Steps

Once import is complete:

1. ✅ Database is populated with curriculum
2. ✅ Backend API can serve lessons (already implemented)
3. **⏳ Next**: Build frontend components to display lessons
4. **⏳ Next**: Implement progress tracking in frontend
5. **⏳ Next**: Add Duolingo-style UI (XP, streak, hearts)

---

## Testing the Backend API

Once import is done, test the API:

```bash
# Start backend server
cd backend
npm start

# In another terminal, test API endpoints:
curl http://localhost:5000/api/lessons/materii
# Should return 2 subjects

curl http://localhost:5000/api/lessons/materii/[MATERIA_ID]/clase
# Should return grades for that subject
```

---

## Summary

| Component | Status |
|-----------|--------|
| JSON files created | ✅ |
| Import script created | ✅ |
| Database models ready | ✅ |
| API routes ready | ✅ |
| **Import to DB** | 🚀 **DO THIS NOW** |
| Frontend components | ⏳ TODO |
| UI/UX | ⏳ TODO |
| Duolingo-style features | ⏳ TODO |

---

**Ready? Run the import!**
```bash
node backend/scripts/importCurriculum.js
```

Let me know when it's done! 🎉

