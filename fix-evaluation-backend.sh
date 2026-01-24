#!/bin/bash

# Copy curriculum file to backend
echo "Copying curriculum_structure.json to backend..."
cp curriculum_structure.json backend/curriculum_structure.json

# Commit and push
echo "Adding to git..."
git add backend/curriculum_structure.json

echo "Committing..."
git commit -m "Add curriculum_structure.json to backend for Render deployment - Fix evaluation form questions not displaying"

echo "Pushing to GitHub..."
git push

echo "Done! Render will redeploy automatically. Check https://dashboard.render.com"

