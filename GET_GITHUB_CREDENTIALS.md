# 🔐 HOW TO GET GITHUB CREDENTIALS

## Problem
GitHub no longer supports password authentication for Git operations over HTTPS. You need a **Personal Access Token (PAT)**.

---

## Solution: Create a Personal Access Token on GitHub

### Step 1: Go to GitHub Settings
1. Go to: https://github.com/settings/tokens
2. Or manually: GitHub.com → Settings → Developer settings → Personal access tokens

### Step 2: Generate New Token
1. Click **"Generate new token"** → **"Generate new token (classic)"**
2. Name it: `EduPex-Push` or similar
3. Set Expiration: 90 days (or longer if you prefer)

### Step 3: Select Scopes (Permissions)
Check these boxes:
- ✅ `repo` (full control of private repositories)
- ✅ `workflow` (update GitHub Action workflows)

### Step 4: Generate
1. Click **"Generate token"**
2. **COPY THE TOKEN IMMEDIATELY** (you won't see it again!)

### Step 5: Use Token with Git

**When Git asks for password, paste the token instead:**

```
Username for 'https://github.com': RGSRomania
Password for 'https://RGSRomania@github.com': [PASTE YOUR TOKEN HERE]
```

---

## Better: Cache Credentials So You Don't Need to Enter Every Time

### Option A: Store in Keychain (Recommended for Mac)

```bash
git config --global credential.helper osxkeychain
git push origin main
# First time: enter your PAT when prompted
# Future: it remembers automatically
```

### Option B: Store in ~/.git-credentials File

```bash
git config --global credential.helper store
git push origin main
# Enter credentials when prompted, they're saved
```

### Option C: Use SSH Instead (Most Secure)

If you prefer not to use tokens, set up SSH:

1. Generate SSH key: `ssh-keygen -t ed25519 -C "mdica@bitdefender.com"`
2. Add to GitHub: https://github.com/settings/ssh/new
3. Change remote: `git remote set-url origin git@github.com:RGSRomania/EduPex.git`
4. Push: `git push origin main`

---

## Try Pushing Now

### Option 1: Use Token Directly (One Time)

```bash
cd /Users/mdica/PycharmProjects/EduPex
git push origin main
# When prompted for password, paste your PAT
```

### Option 2: Cache with Keychain (Recommended)

```bash
git config --global credential.helper osxkeychain
cd /Users/mdica/PycharmProjects/EduPex
git push origin main
# Enter PAT when prompted, then it's cached
```

---

## What Happens After Push

Once you push:
1. ✅ Your code is on GitHub
2. ✅ Render auto-deploys the backend
3. ✅ Your frontend fixes go live
4. ✅ 401 error is fixed on Render

---

## Next Steps

1. Create GitHub Personal Access Token: https://github.com/settings/tokens
2. Cache credentials (optional but recommended)
3. Push your changes
4. Check Render deployment in your dashboard

**You're almost there!** Just need the token to finish deploying! 🚀


