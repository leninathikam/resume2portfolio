# Resume to Portfolio Website Generator

Transform your resume into a stunning, professional portfolio website using Claude AI.

## 🚀 Live Demo

- **Frontend**: https://leninathikam.github.io/resume2portfolio/
- **Docs**: [QUICK_DEPLOY.md](QUICK_DEPLOY.md) - Deploy in 5 minutes!
- **Full Guide**: [DEPLOYMENT.md](DEPLOYMENT.md) - Complete deployment instructions

## Project Overview

This application takes your resume as input and generates beautiful, responsive HTML portfolio code. The generated portfolio is immediately viewable and downloadable. Works offline (no API key required) or with Claude AI.
    
### Features
- 📄 **Resume Upload**: Support for PDF, DOCX, DOC, and TXT files
- 🤖 **AI-Powered Generation**: Uses AI to generate custom portfolios (optional)
- 🎨 **Professional Design**: Modern, responsive HTML/CSS portfolio templates
- 👀 **Live Preview**: View your portfolio in real-time
- ⬇️ **Download**: Download the generated HTML file
- 📱 **Responsive**: Mobile-friendly portfolio design
- ✅ **Offline Mode**: Works without any API key or backend
- 🆓 **Free Hosting**: Deploy on GitHub Pages + Render/Railway for free

## Tech Stack

### Backend
- **Framework**: Flask (Python)
- **LLM**: Anthropic Claude API
- **File Handling**: Werkzeug
- **API**: RESTful with CORS support

### Frontend
- **Framework**: React 18
- **Language**: TypeScript
- **HTTP Client**: Axios
- **Styling**: CSS3 with responsive design

## Project Structure

```
resume2portfolio/
├── backend/                    # Flask backend
│   ├── app/                   # Application package
│   │   ├── __init__.py        # App factory
│   │   ├── routes/            # API routes
│   │   │   ├── upload.py      # Resume upload endpoint
│   │   │   └── __init__.py
│   │   ├── services/          # Business logic
│   │   │   ├── llm_service.py # Claude integration
│   │   │   └── __init__.py
│   │   └── models/            # Data models (if needed)
│   ├── uploads/               # Temporary file storage
│   ├── run.py                 # Application entry point
│   ├── config.py              # Configuration
│   ├── requirements.txt        # Python dependencies
│   └── .env.example           # Environment variables template
│
├── frontend/                   # React frontend
│   ├── src/
│   │   ├── components/        # React components
│   │   │   ├── ResumeUpload.tsx
│   │   │   └── PortfolioPreview.tsx
│   │   ├── pages/             # Page components (for future expansion)
│   │   ├── App.tsx            # Main app component
│   │   ├── App.css            # Global styles
│   │   └── index.tsx          # Entry point
│   ├── public/
│   │   └── index.html         # HTML template
│   ├── package.json           # Node dependencies
│   └── tsconfig.json          # TypeScript config
│
├── .github/
│   └── copilot-instructions.md
├── README.md                   # This file
└── .gitignore                  # Git ignore rules
```

## Setup Instructions

### Prerequisites
- Python 3.9+
- Node.js 16+
- npm or yarn
- Claude API key from Anthropic

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file from `.env.example`:
```bash
cp .env.example .env
```

5. Edit `.env` and add your Claude API key:
```
CLAUDE_API_KEY=your_api_key_here
FLASK_ENV=development
FLASK_DEBUG=True
FRONTEND_URL=http://localhost:3000
```

6. Run the Flask server:
```bash
python run.py
```

The backend will start on `http://localhost:5000`

### Frontend Setup

1. In a new terminal, navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
# or
yarn install
```

3. Start the development server:
```bash
npm start
# or
yarn start
```

The frontend will open at `http://localhost:3000`

## Deployment

### Quick Deploy (5 minutes)
See **[QUICK_DEPLOY.md](QUICK_DEPLOY.md)** for rapid deployment steps:
- Frontend → GitHub Pages (automatic)
- Backend → Render or Railway (free tier)

### Full Deployment Guide
See **[DEPLOYMENT.md](DEPLOYMENT.md)** for complete instructions with:
- Step-by-step GitHub Pages setup
- Render deployment with free tier
- Railway.app alternative
- Testing & troubleshooting

## Usage

1. **Upload Resume**: Choose or drag a resume file (PDF, DOCX, DOC, TXT)
2. **Generate**: Click "Generate Portfolio" button
3. **Preview**: View your AI-generated portfolio in real-time
4. **Download**: Download the HTML file to use or customize further

## API Endpoints

### POST `/api/upload`
Upload a resume and generate portfolio HTML

**Request:**
```
Content-Type: multipart/form-data
Field: resume (file)
```

**Response:**
```json
{
  "success": true,
  "portfolio": "<html>...</html>",
  "message": "Portfolio generated successfully"
}
```

## Environment Variables

Create a `.env` file in the `backend` directory with the following variables:

```env
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True

# Claude API Configuration
CLAUDE_API_KEY=your_claude_api_key_here
CLAUDE_MODEL=claude-3-5-sonnet-20241022

# Server Configuration
FLASK_HOST=0.0.0.0
FLASK_PORT=5000

# CORS Configuration
FRONTEND_URL=http://localhost:3000
```

## File Upload Support

The application currently supports:
- **PDF** (.pdf)
- **DOCX** (.docx)
- **DOC** (.doc)
- **TXT** (.txt)

*Note: For PDF and DOCX support, install optional dependencies:*
```bash
pip install PyPDF2 python-docx
```

## Features Overview

### Resume Analysis
- Extracts key information from resumes
- Identifies skills, experience, education
- Understands career progression

### Portfolio Generation
- Creates professional HTML/CSS
- Responsive design (mobile-friendly)
- Modern aesthetics
- Smooth animations and transitions

### User Experience
- Drag-and-drop file upload
- Real-time preview in iframe
- Download generated portfolio
- Responsive UI for all devices

## Future Enhancements

- [ ] Generate React component versions
- [ ] Multiple portfolio templates/themes
- [ ] Portfolio customization editor
- [ ] Dark mode support
- [ ] Email portfolio to user
- [ ] Save portfolio history
- [ ] Social media integration
- [ ] SEO optimization options

## Troubleshooting

### Claude API Key Error
- Verify the API key is correct in `.env`
- Ensure the key has appropriate permissions
- Check if the key has sufficient credits

### File Upload Fails
- Ensure file size is under 16MB
- Verify file format is supported
- Check backend upload folder permissions

### Frontend Can't Connect to Backend
- Verify backend is running on port 5000
- Check CORS configuration in Flask
- Ensure frontend is trying to connect to correct URL

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please open an issue on the GitHub repository.

---

**Built with ❤️ using Flask, React, and Claude AI**
