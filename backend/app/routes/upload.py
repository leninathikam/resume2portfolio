from flask import request, jsonify, current_app
from app.routes import upload_bp
from app.services.llm_service import generate_portfolio
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc', 'txt'}

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_bp.route('/upload', methods=['POST'])
def upload_resume():
    """
    Upload resume and generate portfolio HTML
    Expected: multipart/form-data with 'resume' file field
    """
    try:
        # Check if file is present
        if 'resume' not in request.files:
            return jsonify({'error': 'No resume file provided'}), 400
        
        file = request.files['resume']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'File type not allowed. Use PDF, DOC, DOCX, or TXT'}), 400
        
        # Save uploaded file
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Extract text from resume (placeholder - implement based on file type)
        resume_text = extract_resume_text(filepath)
        
        # Generate portfolio using Claude
        portfolio_html = generate_portfolio(resume_text)
        
        # Clean up uploaded file
        os.remove(filepath)
        
        return jsonify({
            'success': True,
            'portfolio': portfolio_html,
            'message': 'Portfolio generated successfully'
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def extract_resume_text(filepath):
    """Extract text from resume file"""
    ext = os.path.splitext(filepath)[1].lower()
    
    if ext == '.txt':
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    
    elif ext == '.pdf':
        try:
            import PyPDF2
            with open(filepath, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text = ''
                for page in reader.pages:
                    text += page.extract_text()
                return text
        except ImportError:
            return "PDF extraction requires PyPDF2. Install with: pip install PyPDF2"
    
    elif ext in ['.docx', '.doc']:
        try:
            from docx import Document
            doc = Document(filepath)
            text = ''
            for para in doc.paragraphs:
                text += para.text + '\n'
            return text
        except ImportError:
            return "DOCX extraction requires python-docx. Install with: pip install python-docx"
    
    return ""
