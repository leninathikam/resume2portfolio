## Resume to Portfolio Website Generator

This project converts resumes into personalized portfolio websites using Claude LLM.

### Project Stack
- **Backend**: Flask (Python)
- **Frontend**: React (TypeScript/JavaScript)
- **LLM**: Claude API
- **Output**: HTML/CSS portfolio website

### Development Guidelines
- Use Claude API for resume analysis and code generation
- Implement secure file upload handling
- Generate responsive portfolio websites
- Follow best practices for both Python and React development
- Resume files supported: PDF, DOCX, DOC, TXT
- Optional: Install PyPDF2 and python-docx for better extraction

### Project Structure
```
backend/           - Flask REST API
├── app/
│   ├── routes/   - API endpoints
│   ├── services/ - LLM integration
│   └── models/   - Data models
├── uploads/      - Temporary file storage
├── config.py     - Configuration
└── run.py        - Entry point

frontend/          - React SPA
├── src/
│   ├── components/ - React components
│   ├── pages/      - Page components  
│   └── App.tsx    - Main component
└── public/        - Static assets
```

### Quick Start
1. **Backend Setup**:
   - Virtual environment created: `backend/venv`
   - Dependencies installed from `requirements.txt`
   - Copy `.env.example` to `.env` and add your Claude API key
   - Run: `python run.py`

2. **Frontend Setup**:
   - Install Node.js (required, not yet installed on this system)
   - Run: `npm install` then `npm start`

3. **Environment Variables** (.env):
   ```
   CLAUDE_API_KEY=your_key_here
   CLAUDE_MODEL=claude-3-5-sonnet-20241022
   FLASK_ENV=development
   FRONTEND_URL=http://localhost:3000
   ```

### Available Tasks
Use VS Code Tasks (Ctrl+Shift+D) to run:
- "Backend: Run Flask Server" - Starts Flask on port 5000
- "Frontend: Start Dev Server" - Starts React on port 3000  
- "Backend: Install Dependencies" - Install Python packages
- "Frontend: Install Dependencies" - Install npm packages
- "Setup: Backend .env File" - Create .env from template

### API Endpoints
- `POST /api/upload` - Upload resume and generate portfolio

### Key Features Implemented
- ✅ Resume file upload (drag-drop & click)
- ✅ Claude API integration for portfolio generation
- ✅ Real-time preview iframe
- ✅ HTML download functionality
- ✅ Responsive design
- ✅ CORS enabled for local development
- ✅ TypeScript React frontend
- ✅ Python Flask backend with proper config management
