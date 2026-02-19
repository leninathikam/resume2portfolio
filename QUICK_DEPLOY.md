# 🚀 Quick Deployment (5 minutes)

## Frontend - GitHub Pages (Already Done!)

Your site is ready at: `https://leninathikam.github.io/resume2portfolio/`

## Backend - Deploy to Render (Free)

### 1. Create Render Account
- Go to https://render.com
- Sign up with GitHub

### 2. Create New Web Service
```
1. Click "New +" → "Web Service"
2. Connect your GitHub repo
3. Select: resume2portfolio
4. Configure:
   - Name: resume2portfolio-api
   - Runtime: Python 3.9
   - Build Cmd: pip install -r backend/requirements.txt
   - Start Cmd: cd backend && python run.py
   - Plan: Free
5. Click "Create Web Service"
```

### 3. Wait for Deployment
- Takes 2-5 minutes
- You'll get a URL like: `https://resume2portfolio-api.onrender.com`

### 4. Update Frontend URL
Edit `docs/app.html` line 191:
```javascript
const API_BASE_URL = 'https://resume2portfolio-api.onrender.com';
```

### 5. Push Update
```bash
git add docs/app.html
git commit -m "Update API URL for Render deployment"
git push origin main
```

### 6. Test
- Go to: `https://leninathikam.github.io/resume2portfolio/docs/app.html`
- Upload a resume
- Generate portfolio!

---

## Alternative: Railway.app

If Render doesn't work:

1. Go to https://railway.app
2. New Project → Deploy from GitHub
3. Select repo, add environment vars, deploy
4. Update API URL in docs/app.html
5. Push changes

---

## Verify Deployment

```bash
# Frontend health check
curl https://leninathikam.github.io/resume2portfolio/

# Backend health check (after deploying)
curl https://resume2portfolio-api.onrender.com/health
```

---

**That's it! Your app is live!** 🎉
