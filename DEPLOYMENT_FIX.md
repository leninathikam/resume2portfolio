# Deployment Fix: GitHub Pages + Render Integration

## Problem
Getting "404 Not Found" error when trying to use the deployed frontend with the Render backend.

## Root Causes
1. **Frontend API URL pointing to localhost** - `docs/app.html` was configured for local development
2. **CORS configuration too restrictive** - Backend only allowed requests from single origin
3. **Backend environment variables not updated** - Render backend needs to know about GitHub Pages URL

## Solutions Applied

### ✅ 1. Updated Frontend API URL
**File:** `docs/app.html` (line 242)
```javascript
// Before
const API_BASE_URL = 'http://localhost:5000';

// After
const API_BASE_URL = 'https://resume2portfolio-api.onrender.com';
```
👉 **Update `resume2portfolio-api` with your actual Render URL**

### ✅ 2. Fixed Backend CORS Configuration
**File:** `backend/app/__init__.py`

Now accepts multiple origins:
- `http://localhost:3000` - Local React dev
- `http://localhost:5000` - Local Flask
- `https://leninathikam.github.io` - GitHub Pages (your deployed frontend)
- Environment variable `FRONTEND_URL` (if set)

## Next Steps

### Step 1: Update Render Environment Variables

The Render backend needs to know to accept requests from GitHub Pages:

1. Go to [Render Dashboard](https://render.com/dashboard)
2. Select your `resume2portfolio-api` web service
3. Click **Environment** tab
4. Update or add these variables:
   ```
   FRONTEND_URL=https://leninathikam.github.io
   FLASK_ENV=production
   FLASK_DEBUG=False
   ```
5. Click **Save**
6. Service will auto-redeploy (~2-5 minutes)

### Step 2: Update Frontend URL

If your Render backend URL is different from `resume2portfolio-api.onrender.com`:

1. Go to [GitHub Pages deployed site](https://leninathikam.github.io/resume2portfolio/)
2. Open Browser DevTools (F12)
3. Check Console for API errors
4. Note the actual Render URL from error messages
5. Edit `docs/app.html` line 242 and replace with your actual URL:
   ```javascript
   const API_BASE_URL = 'https://YOUR-ACTUAL-RENDER-URL.onrender.com';
   ```
6. Commit and push changes
7. GitHub Pages will auto-deploy within ~1 minute

### Step 3: Push Backend Code Changes

Deploy the CORS fix to Render:

```bash
cd resume2portfolio
git add backend/app/__init__.py docs/app.html
git commit -m "Fix: Update CORS and API URL for GitHub Pages + Render deployment"
git push origin main
```

Render will auto-deploy the changes (~2-5 minutes).

### Step 4: Test the Connection

1. Go to https://leninathikam.github.io/resume2portfolio/
2. Upload a resume file
3. If still getting 404:
   - Check Browser Console (F12) for exact URL being called
   - Check Render logs: Dashboard → Web Service → Logs tab
   - Verify API_BASE_URL in docs/app.html matches your Render URL

## Troubleshooting Checklist

### Still getting 404?

- [ ] **Render URL correct?**
  - Actual format: `https://<service-name>.onrender.com`
  - Check Render dashboard for exact URL
  - Verify in `docs/app.html` line 242

- [ ] **Render backend running?**
  - Check Render dashboard → Logs tab
  - Should show "Running on..." message
  - No "Application failed to start" errors

- [ ] **Environment variables set?**
  - Go to Render dashboard → Environment
  - Verify `FRONTEND_URL` is set (optional, but helpful)
  - Verify `FLASK_ENV=production`

- [ ] **CORS headers correct?**
  - Open Browser DevTools (F12) → Network tab
  - Click upload
  - Look for `POST` request to `/api/upload`
  - Check Response Headers for `Access-Control-Allow-Origin`
  - Should include your GitHub Pages URL

- [ ] **API route exists?**
  - Try: `https://<your-render-url>/api/upload` in browser
  - Should show error about GET not allowed (that's normal)
  - If shows 404, backend routing is broken

### Getting CORS error instead of 404?

This is actually progress! Means backend is responding. 

- Check browser console shows actual error
- Update `backend/app/__init__.py` to add your exact frontend URL
- Push changes to GitHub
- Render will auto-deploy

## Quick Command Reference

```bash
# View current branch
git status

# Stage all changes
git add .

# Commit with message
git commit -m "Fix: Deployment configuration"

# Push to GitHub (triggers Render auto-deploy)
git push origin main

# Check Python syntax
python -m py_compile backend/app/__init__.py

# Test locally before pushing
cd backend
python run.py
# Visit http://localhost:5000 in browser
```

## Environment Variable Reference

For **Render Backend** (set in Render Dashboard):
```
FLASK_ENV=production
FLASK_DEBUG=False
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
FRONTEND_URL=https://leninathikam.github.io
USE_LLM_API=false
LLM_MODEL=offline
```

For **Local Development** (in `backend/.env`):
```
FLASK_ENV=development
FLASK_DEBUG=True
FRONTEND_URL=http://localhost:3000
```

## Testing with cURL (from command line)

```bash
# Test if backend is responding
curl -X OPTIONS https://resume2portfolio-api.onrender.com/api/upload -v

# Should see:
# < HTTP/1.1 200 OK
# < Access-Control-Allow-Origin: ...
# < Access-Control-Allow-Methods: ...
```

## Expected Flow After Fix

1. User uploads resume at GitHub Pages frontend
2. Frontend sends POST to `https://resume2portfolio-api.onrender.com/api/upload`
3. Backend receives request, checks CORS (✅ GitHub Pages URL allowed)
4. Backend processes file, generates portfolio
5. Backend returns HTML to frontend
6. Frontend displays in preview

---

**Last Updated:** February 19, 2026  
**Status:** Deployment infrastructure fixed, ready for testing
