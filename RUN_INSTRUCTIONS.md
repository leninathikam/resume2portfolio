# Resume to Portfolio Generator - Complete Setup & Running Guide

A powerful AI-powered application that transforms resumes into beautiful, responsive portfolio websites using Claude, OpenAI, Google Gemini, and other LLM providers.

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Quick Start (5 Minutes)](#quick-start-5-minutes)
3. [Full Installation](#full-installation)
4. [Running the Application](#running-the-application)
5. [How to Use](#how-to-use)
6. [Available Models](#available-models)
7. [Project Structure](#project-structure)
8. [Troubleshooting](#troubleshooting)
9. [Features](#features)

---

## 📋 Prerequisites

Before you start, ensure you have:

- **Python 3.8 or higher** - [Download](https://www.python.org/downloads/)
- **Node.js 14+ and npm** - [Download](https://nodejs.org/)
- **OpenAI API Key** (recommended) - Get from [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- **Git** (optional, for version control)

### Verify Installation

```bash
# Check Python version
python --version

# Check Node.js version
node --version

# Check npm version
npm --version
```

---

## 🚀 Quick Start (5 Minutes)

### For Windows Users

#### Step 1: Open PowerShell and navigate to project
```powershell
cd c:\Users\lenin\Downloads\resume2portfolio
```

#### Step 2: Get your OpenAI API Key
1. Visit [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Click "Create new secret key"
3. Copy the key (starts with `sk-proj-`)
4. **Keep it safe!** Don't share it in chat or version control

#### Step 3: Update backend configuration
Edit `backend/.env`:
```
OPENAI_API_KEY=sk-proj-your-actual-key-here
```

#### Step 4: Start Backend Server (Terminal 1)
```powershell
cd backend
.\venv\Scripts\python.exe run.py
```

You should see:
```
 * Running on http://0.0.0.0:5000
 * Debug mode: on
```

#### Step 5: Start Frontend Server (Terminal 2)
```powershell
cd frontend\build
python -m http.server 3000
```

You should see:
```
Serving HTTP on 0.0.0.0 port 3000 (http://0.0.0.0:3000/)
```

#### Step 6: Open Application
Click this link: [http://localhost:3000](http://localhost:3000)

✅ **You're ready to go!** Upload a resume and generate your first portfolio.

---

## 📦 Full Installation

Use these steps if it's your first time or if you need to set everything up from scratch.

### Step 1: Backend Setup

```powershell
# Navigate to project root
cd c:\Users\lenin\Downloads\resume2portfolio

# Go to backend directory
cd backend

# Create Python virtual environment (if it doesn't exist)
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Install additional libraries for PDF/DOCX support
pip install PyPDF2 python-docx
```

**Expected output after `pip install`:**
```
Successfully installed Flask==3.0.0 Flask-CORS==4.0.0 ... (multiple packages)
```

### Step 2: Frontend Setup

```powershell
# Go back to project root
cd ..

# Navigate to frontend
cd frontend

# Install npm dependencies
npm install

# Build for production
npm run build
```

**Expected output after `npm run build`:**
```
The project was built successfully
File sizes after gzip:
  62.34 kB  build\static\js\main.xxxxx.js
  1.25 kB   build\static\css\main.xxxxx.css
```

### Step 3: Configure API Key

Edit file: `backend/.env`

**Current content:**
```
OPENAI_API_KEY=sk-proj-lqj_3BPU5Era...
```

**Replace with your new key:**
```dotenv
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True

# LLM Configuration
USE_LLM_API=true
LLM_MODEL=gpt-4o-mini

# API Keys
OPENAI_API_KEY=sk-proj-your-new-key-here

# Server Configuration
FLASK_HOST=0.0.0.0
FLASK_PORT=5000

# CORS Configuration
FRONTEND_URL=http://localhost:3000
```

✅ **Installation complete!**

---

## 🎯 Running the Application

You need **at least 2 terminal windows** open.

### Terminal 1: Start Backend Server

```powershell
# Navigate to backend
cd c:\Users\lenin\Downloads\resume2portfolio\backend

# Activate virtual environment
.\venv\Scripts\activate

# Start Flask server
python run.py
```

**Success indicators:**
- `Running on http://0.0.0.0:5000`
- `Debugger PIN: xxxxx`
- No error messages

✅ **Backend is running!**

### Terminal 2: Start Frontend Server

```powershell
# Navigate to frontend build
cd c:\Users\lenin\Downloads\resume2portfolio\frontend\build

# Start HTTP server
python -m http.server 3000
```

**Success indicators:**
- `Serving HTTP on 0.0.0.0 port 3000`
- No error messages

✅ **Frontend is running!**

### Step 3: Open Browser

Click here: [http://localhost:3000](http://localhost:3000)

Or open your browser and type: `http://localhost:3000`

---

## 💻 How to Use the Application

### Step-by-Step Guide

1. **Open Application**
   - Go to [http://localhost:3000](http://localhost:3000)
   - You should see "Resume to Portfolio Generator"

2. **Upload Resume**
   - Click the upload area or drag & drop a file
   - Supported formats:
     - PDF (.pdf)
     - Word (.docx, .doc)
     - Text (.txt)
   - File size: Max 16MB

3. **Select Model** (optional)
   - Default: "Offline Mode (No API needed)"
   - Recommended: "OpenAI GPT-4o Mini"
   - Other options available (Google Gemini, Groq, etc.)

4. **Add API Key** (optional)
   - Leave blank if you added key to `backend/.env`
   - Or paste your key here for that session only

5. **Click "Generate Portfolio"**
   - Wait 30-60 seconds for processing
   - First generation may take longer

6. **View Your Portfolio**
   - Portfolio appears on right side
   - Scroll through to see all sections
   - Button to download as HTML included

7. **Generate Again**
   - Upload same or different resume
   - Get a completely different design!
   - Each generation creates unique portfolio

### Tips

- 💡 Use "Offline Mode" if you don't have an API key (basic template)
- 🎨 Upload multiple times to see different design variations
- 📱 Generated portfolios are fully responsive (mobile-friendly)
- ⚡ GPT-4o-mini is fastest and cheapest option
- 🔒 API keys are secure (only sent to OpenAI, not stored locally)

---

## 🤖 Available Models

### OpenAI (Recommended)
- **gpt-4o** - Most advanced, highest quality
- **gpt-4o-mini** - Fast, cheaper, recommended ⭐
- **gpt-4-turbo** - Good balance
- **gpt-3.5-turbo** - Fastest, cheapest

Setup: Get key from [platform.openai.com](https://platform.openai.com/api-keys)

### Google Gemini
- **gemini-2.5-flash** - Very fast
- **gemini-2.5-pro** - Most advanced

Setup: Get key from [Google AI Studio](https://aistudio.google.com/)

### Meta Llama (via Groq)
- **llama-3.3-70b** - High quality, fast
- **groq/compound** - Groq's native model

Setup: Get key from [console.groq.com](https://console.groq.com/)

### Other Options
- **qwen/qwen3-32b** (Alibaba)
- **offline** - No API key needed (basic template)

---

## 📁 Project Structure

```
resume2portfolio/
│
├── backend/                    # Flask Python API
│   ├── app/
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   └── upload.py      # Resume upload endpoint
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── llm_service.py # LLM integration (Claude, OpenAI, etc.)
│   │   ├── models/
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   └── __pycache__/
│   ├── uploads/               # Temporary file storage
│   ├── venv/                  # Python virtual environment
│   ├── .env                   # API keys (NEVER COMMIT!)
│   ├── config.py              # Flask configuration
│   ├── run.py                 # Entry point
│   ├── requirements.txt        # Python dependencies
│   └── __pycache__/
│
├── frontend/                   # React TypeScript App
│   ├── src/
│   │   ├── components/
│   │   │   ├── ResumeUpload.tsx
│   │   │   ├── ResumeUpload.css
│   │   │   ├── PortfolioPreview.tsx
│   │   │   └── PortfolioPreview.css
│   │   ├── App.tsx
│   │   ├── App.css
│   │   ├── index.tsx
│   │   └── index.css
│   ├── public/
│   │   ├── index.html
│   │   └── favicon.ico
│   ├── build/                 # Production build (run this)
│   ├── node_modules/          # npm dependencies
│   ├── package.json           # npm config
│   ├── tsconfig.json          # TypeScript config
│   └── README.md
│
├── RUN_INSTRUCTIONS.md        # This file
├── README.md
└── LICENSE
```

---

## ⚠️ Troubleshooting

### Problem: Backend won't start

**Error:** `ModuleNotFoundError: No module named 'flask'`

**Solution:**
```powershell
cd backend
pip install -r requirements.txt
python run.py
```

---

### Problem: Frontend shows blank page

**Error:** Nothing loads at localhost:3000

**Solution:**
```powershell
cd frontend
npm run build
cd build
python -m http.server 3000
```

---

### Problem: API Key Error

**Error:** `OPENAI_API_KEY not set` or `Invalid API Key`

**Solution:**
1. Go to [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Check if key is still valid (hasn't been deleted)
3. If exposed in chat, revoke it and create a new one
4. Update `backend/.env` with new key
5. Restart backend

---

### Problem: Port 5000 or 3000 already in use

**Error:** `Address already in use`

**Solution 1 - Change port:**

Edit `backend/.env`:
```
FLASK_PORT=5001
```

Change frontend:
```powershell
python -m http.server 3001
```

**Solution 2 - Kill existing process:**
```powershell
# Find what's using port 5000
netstat -ano | findstr :5000

# Kill process (replace PID with actual number)
taskkill /PID 1234 /F

# Try again
python run.py
```

---

### Problem: PDF/DOCX upload doesn't work

**Error:** `PDF extraction requires PyPDF2`

**Solution:**
```powershell
cd backend
pip install PyPDF2 python-docx
python run.py
```

---

### Problem: Slow portfolio generation

**Possible causes:**
- Using slow model (GPT-4 instead of GPT-4-mini)
- Network connection slow
- OpenAI API overloaded

**Solution:**
- Use `gpt-4o-mini` instead of `gpt-4o`
- Use `groq/compound` (faster)
- Wait and try again

---

### Problem: Generated portfolio looks generic

**Cause:** Using offline mode or fallback template

**Solution:**
- Add OpenAI API key to `backend/.env` or form
- Select a model from dropdown (not "Offline Mode")
- System will use advanced LLM prompts for better results

---

## 🎨 Features

### ✅ Core Features

- **📄 Multiple Resume Formats**
  - PDF support (PyPDF2)
  - DOCX/DOC support (python-docx)
  - Plain text (TXT)

- **🤖 Multiple AI Providers**
  - OpenAI (GPT-3.5, GPT-4, GPT-4o)
  - Google Gemini
  - Meta Llama (via Groq)
  - Alibaba Qwen
  - Euron.ai
  - Offline mode (no API)

- **🎯 Smart Data Extraction**
  - Full name & contact info
  - Professional summary
  - Work experience with achievements
  - Education & certifications
  - Technical & soft skills

### ✨ Portfolio Features

- **🎨 Advanced Design**
  - Animated hero sections
  - Gradient backgrounds
  - Skill progress bars
  - Experience timelines
  - Education cards
  - Professional contact forms

- **📱 Fully Responsive**
  - Mobile optimized
  - Tablet friendly
  - Desktop enhanced
  - Touch-friendly buttons
  - No horizontal scrolling

- **🎭 Unique Variations**
  - Different design each generation
  - Modern minimalist style
  - Colorful creative designs
  - Dark professional mode
  - Card-based layouts
  - Timeline variations

- **⚡ Advanced CSS Effects**
  - Hover animations
  - Smooth transitions
  - Box shadows & depth
  - Custom scrollbars
  - Subtle fade-in effects

### 🔧 Technical Features

- **Self-Contained**
  - All CSS embedded
  - No external dependencies
  - Works offline after generation
  - Single HTML file deployable

- **Secure**
  - API keys never logged
  - Files deleted after processing
  - CORS enabled for localhost

- **Performant**
  - Fast generation (30-60 seconds)
  - Optimized frontend
  - Efficient backend

---

## 📚 API Reference

### Health Check
```
GET http://localhost:5000/
```
Returns: `{ "status": "ok", "service": "resume-to-portfolio-api" }`

### Generate Portfolio
```
POST http://localhost:5000/api/upload
```

**Request (multipart/form-data):**
- `resume` (file) - Resume file (PDF, DOCX, TXT)
- `model` (string) - Model name (e.g., "gpt-4o-mini")
- `api_key` (string) - API key (optional, uses .env if empty)

**Response:**
```json
{
  "success": true,
  "portfolio": "<html>...</html>",
  "message": "Portfolio generated successfully"
}
```

---

## 🚀 Deployment

### For Production Use

1. **Change environment:**
   ```
   FLASK_ENV=production
   FLASK_DEBUG=False
   ```

2. **Use production server:**
   ```powershell
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

3. **Deploy frontend:**
   - Copy `frontend/build/` to web server
   - Or use services like Vercel, Netlify, GitHub Pages

4. **Secure API keys:**
   - Use environment variables
   - Never commit `.env` file
   - Use `.env.example` as template

---

## 📞 Support

### Common Questions

**Q: Do I need an API key?**
A: No, you can use offline mode. But API keys give much better results.

**Q: Which model is best?**
A: `gpt-4o-mini` - fast, cheap, and high quality.

**Q: Can I modify the generated portfolio?**
A: Yes! Download as HTML and edit in any text editor.

**Q: How much does it cost?**
A: OpenAI GPT-4o-mini: ~$0.01-0.05 per portfolio

**Q: Can I host this online?**
A: Yes! Deploy backend to Heroku/Railway and frontend to Vercel/Netlify

**Q: Is my resume data private?**
A: Yes, files are deleted after processing and never stored.

---

## 📝 License

[See LICENSE file](LICENSE)

---

## 🎉 Getting Started Now

```powershell
# Quick start
cd c:\Users\lenin\Downloads\resume2portfolio

# Terminal 1
cd backend
.\venv\Scripts\python.exe run.py

# Terminal 2
cd frontend\build
python -m http.server 3000

# Browser
# Open http://localhost:3000
```

**Enjoy creating amazing portfolios!** 🚀

