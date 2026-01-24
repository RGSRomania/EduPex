#!/usr/bin/env python3
import subprocess
import os

os.chdir('/Users/mdica/PycharmProjects/EduPex')

# Stage all changes
result = subprocess.run(['git', 'add', '-A'], capture_output=True, text=True)
print("Git add output:", result.stdout, result.stderr)

# Check status
result = subprocess.run(['git', 'status', '--short'], capture_output=True, text=True)
print("Git status:", result.stdout)

# Commit
result = subprocess.run([
    'git', 'commit', '-m',
    'Fix: Add curriculum_structure.json to backend directory and improve file path resolution for evaluation questions'
], capture_output=True, text=True)
print("Git commit output:", result.stdout, result.stderr)

# Push
result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)
print("Git push output:", result.stdout, result.stderr)

