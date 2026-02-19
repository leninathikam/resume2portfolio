# Deployment Guide

This project can be deployed for free using GitHub Pages (frontend) and free cloud services for the backend.

## Option A: Complete Cloud Deployment (Recommended)

### Frontend: Deploy to GitHub Pages

GitHub Pages will serve your test.html and React build automatically.

#### Step 1: Enable GitHub Pages in Repository Settings
1. Go to https://github.com/leninathikam/resume2portfolio/settings
2. Scroll down to **Pages** section
3. Select **Deploy from a branch**
4. Choose branch: **main**
5. Select folder: **/ (root)** or **/docs**
6. Click Save

Your site will be available at: `https://leninathikam.github.io/resume2portfolio/`

#### Step 2: Access the App
- **Test Page**: `https://leninathikam.github.io/resume2portfolio/test.html`
- If deploying React build: `https://leninathikam.github.io/resume2portfolio/`

### Backend: Deploy to Render (Free)

Render offers free hosting for web services with automatic deploys from GitHub.

#### Step 1: Create Render Account
1. Go to https://render.com and sign up (free)
2. Connect your GitHub account

#### Step 2: Deploy Flask Backend
1. Click **New +** → **Web Service**
2. Select repository: `resume2portfolio`
3. Configure:
   - **Name**: `resume2portfolio-api`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `cd backend && python run.py`
   - **Plan**: Free

4. Set Environment Variables:
   ```
   FLASK_ENV=production
   FLASK_DEBUG=False
   FRONTEND_URL=https://leninathikam.github.io
   ```

5. Deploy

Your backend will be at: `https://resume2portfolio-api.onrender.com`

#### Step 3: Update Frontend API URL
After getting your backend URL, update `test.html` and React components to use the new API endpoint.

In `test.html`, change:
```javascript
const response = await fetch('http://localhost:5000/api/upload', {
```

To:
```javascript
const response = await fetch('https://resume2portfolio-api.onrender.com/api/upload', {
```

Then commit and push:
```bash
git add test.html
git commit -m "Update API URL for production"
git push origin main
```

---

## Option B: Backend on Railway.app (Alternative)

Railway is another free option with better free tier.

1. Go to https://railway.app
2. Create account → Connect GitHub
3. Click **New Project** → **Deploy from GitHub repo**
4. Select `resume2portfolio`
5. Add variables:
   - `FLASK_ENV`: `production`
   - `PORT`: `5000`
6. Deploy

Your backend URL will be provided by Railway.

---

## Option C: Heroku Alternative (Now Paid, Not Recommended)

Heroku removed free tier in November 2022. Use Render or Railway instead.

---

## Local Testing Before Deployment

### Test Locally First
1. Make sure backend is running:
   ```bash
   cd backend
   .\venv\Scripts\python.exe run.py
   ```

2. Open test.html in browser:
   ```
   file:///c:/Users/lenin/Downloads/resume2portfolio/test.html
   ```

3. Upload a resume and verify everything works

### Build React (Optional)
If you want to deploy the React app instead of test.html:
```bash
cd frontend
npm run build
```

This creates a `build/` folder that GitHub Pages can serve.

---

## Step-by-Step Deployment Checklist

### For GitHub Pages
- [ ] Go to repo settings
- [ ] Enable GitHub Pages from main branch
- [ ] Wait 2-3 minutes for deployment
- [ ] Test at `https://leninathikam.github.io/resume2portfolio/test.html`

### For Render Backend
- [ ] Create Render account
- [ ] Click "New Web Service"
- [ ] Connect GitHub repo
- [ ] Set Python 3 environment
- [ ] Add build command: `pip install -r backend/requirements.txt`
- [ ] Add start command: `cd backend && python run.py`
- [ ] Add environment variables
- [ ] Deploy
- [ ] Copy backend URL from Render
- [ ] Update API URL in test.html
- [ ] Push changes to GitHub
- [ ] Verify deployment

### For Railway Backend
- [ ] Create Railway account
- [ ] Connect GitHub
- [ ] Deploy from repo
- [ ] Add environment variables
- [ ] Copy backend URL
- [ ] Update API URL in test.html
- [ ] Push to GitHub

---

## Testing Your Deployed App

1. Open: `https://leninathikam.github.io/resume2portfolio/test.html`
2. Drag and drop a resume file
3. Click "Generate Portfolio"
4. Should generate portfolio from your backend API

---

## Troubleshooting

### GitHub Pages Not Working
- Wait 2-3 minutes after enabling
- Clear cache (Ctrl+Shift+Delete)
- Check repo settings → Pages

### API Connection Issues
- Verify backend is running on Render/Railway
- Check CORS is enabled in Flask
- Verify API URL in test.html matches Render/Railway URL

### Build Errors on Render
- Check logs in Render dashboard
- Ensure requirements.txt has all dependencies
- Verify environment variables are set

---

## Summary

| Component | Service | Cost | URL |
|-----------|---------|------|-----|
| Frontend (HTML/JS) | GitHub Pages | Free | `github.io` |
| Backend (Flask API) | Render or Railway | Free tier | `onrender.com` or `railway.app` |
| Database | None (file-based) | Free | Local |

**Total Cost**: $0 for both services on free tier!

---

## Next Steps

1. Commit test.html changes (if updating API URL)
2. Push to GitHub
3. Wait for GitHub Pages to deploy (2-3 min)
4. Set up Render or Railway backend
5. Test the complete workflow

Good luck! 🚀
