# Setup Guide

## Prerequisites
- Python 3.9 or higher
- Node.js 16+ and npm (needs to be installed)
- Anthropic Claude API key

## Backend Setup (Python)

### 1. Create Virtual Environment
```bash
cd backend
python -m venv venv
```

### 2. Activate Virtual Environment
**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

Edit `.env` and add your Claude API key:
```
CLAUDE_API_KEY=sk-ant-your-actual-key-here
CLAUDE_MODEL=claude-3-5-sonnet-20241022
FLASK_ENV=development
FLASK_DEBUG=True
FRONTEND_URL=http://localhost:3000
```

### 5. Run Backend Server
```bash
python run.py
```

The Flask server will start on `http://localhost:5000`

## Frontend Setup (React + TypeScript)

### 1. Install Node.js
First, you need to install Node.js 16 or higher from https://nodejs.org/

Verify installation:
```bash
node --version
npm --version
```

### 2. Install Dependencies
```bash
cd frontend
npm install
```

### 3. Start Development Server
```bash
npm start
```

The React app will open at `http://localhost:3000`

## Running the Full Application

### Terminal 1: Backend
```bash
cd backend
.\venv\Scripts\activate  # On Windows
python run.py
```

### Terminal 2: Frontend
```bash
cd frontend
npm start
```

Then open your browser to `http://localhost:3000`

## Optional: Resume File Format Support

To enable PDF and DOCX parsing in the backend:

```bash
cd backend
# Activate venv first
pip install PyPDF2 python-docx
```

## Troubleshooting

### Flask server won't start
- Make sure virtual environment is activated
- Check if port 5000 is available
- Verify .env file exists with correct API key

### React app won't start
- Make sure Node.js is installed
- Try deleting `node_modules` and running `npm install` again
- Check if port 3000 is available

### Claude API errors
- Verify API key is correct in .env
- Check API key has appropriate permissions
- Ensure account has sufficient credits

## Using VS Code Tasks

Press `Ctrl+Shift+D` or use Command Palette (`Ctrl+Shift+P` > "Tasks: Run Task") to run predefined tasks:

- "Backend: Install Dependencies" - Install Python packages
- "Backend: Run Flask Server" - Start Flask server
- "Frontend: Install Dependencies" - Install npm packages
- "Frontend: Start Dev Server" - Start React dev server
- "Setup: Backend .env File" - Create .env from template
