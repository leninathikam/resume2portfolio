import os
import re

def generate_portfolio(resume_text):
    """
    Generate portfolio HTML from resume text
    Works offline without Claude API
    
    Args:
        resume_text: Extracted text from resume
    
    Returns:
        HTML string for portfolio website
    """
    
    # Try to use Claude API if available
    use_api = os.getenv('USE_CLAUDE_API', 'false').lower() == 'true'
    api_key = os.getenv('CLAUDE_API_KEY')
    
    if use_api and api_key:
        try:
            import anthropic
            client = anthropic.Anthropic(api_key=api_key)
            
            prompt = f"""You are a professional web designer. Generate a beautiful, responsive HTML5 portfolio website from this resume. Include: header, about, skills, experience, education, and footer. Use modern CSS, responsive design, and professional colors. Return only the HTML with embedded CSS starting with <!DOCTYPE html>

Resume: {resume_text}"""
            
            message = client.messages.create(
                model=os.getenv('CLAUDE_MODEL', 'claude-3-5-sonnet-20241022'),
                max_tokens=4096,
                messages=[{"role": "user", "content": prompt}]
            )
            return message.content[0].text
        except Exception as e:
            print(f"Claude API error: {e}. Using template mode.")
    
    # Generate default portfolio from resume text
    return generate_portfolio_template(resume_text)


def generate_portfolio_template(resume_text):
    """
    Generate a professional portfolio template using the resume text
    """
    
    # Extract information from resume (basic regex patterns)
    lines = resume_text.split('\n')
    
    # Try to extract name (usually first line or a line starting with capital letters)
    name = "Your Name"
    email = "your.email@example.com"
    phone = "(123) 456-7890"
    
    for line in lines[:10]:
        if '@' in line:
            email = line.strip()
        if any(char.isdigit() for char in line) and '(' in line:
            phone = line.strip()
    
    # Extract sections
    skills = extract_section(resume_text, ['skills', 'technical', 'proficiency'])
    experience = extract_section(resume_text, ['experience', 'work', 'employment'])
    education = extract_section(resume_text, ['education', 'academic'])
    
    if not skills:
        skills = "Python, JavaScript, React, Flask, HTML/CSS, REST APIs, Database Design"
    if not experience:
        experience = "Senior Developer at Tech Company\nBuilt web applications using modern frameworks"
    if not education:
        education = "Bachelor of Science in Computer Science"
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Professional Portfolio</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f4f4f4;
        }}
        
        header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 60px 20px;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 700;
        }}
        
        header p {{
            font-size: 1.1em;
            opacity: 0.9;
            margin-bottom: 20px;
        }}
        
        .contact-info {{
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-top: 20px;
            flex-wrap: wrap;
        }}
        
        .contact-info span {{
            font-size: 0.95em;
            opacity: 0.9;
        }}
        
        .container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 0 20px;
        }}
        
        section {{
            background: white;
            margin: 40px auto;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        section h2 {{
            color: #667eea;
            font-size: 1.8em;
            margin-bottom: 30px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
        }}
        
        .skill-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 10px;
        }}
        
        .skill-tag {{
            background: #667eea;
            color: white;
            padding: 8px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            transition: all 0.3s ease;
        }}
        
        .skill-tag:hover {{
            background: #764ba2;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }}
        
        .experience-item {{
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 1px solid #e0e0e0;
        }}
        
        .experience-item:last-child {{
            border-bottom: none;
        }}
        
        .experience-item h3 {{
            color: #333;
            margin-bottom: 5px;
            font-size: 1.1em;
        }}
        
        .experience-item .date {{
            color: #666;
            font-size: 0.9em;
            font-style: italic;
            margin-bottom: 10px;
        }}
        
        .about-text {{
            color: #555;
            line-height: 1.8;
            margin-bottom: 20px;
        }}
        
        footer {{
            background: #333;
            color: white;
            text-align: center;
            padding: 30px 20px;
            margin-top: 60px;
        }}
        
        footer p {{
            margin: 10px 0;
        }}
        
        @media (max-width: 768px) {{
            header h1 {{
                font-size: 1.8em;
            }}
            
            section {{
                padding: 30px 20px;
                margin: 30px auto;
            }}
            
            .contact-info {{
                flex-direction: column;
                gap: 15px;
            }}
            
            .skill-tags {{
                gap: 8px;
            }}
            
            .skill-tag {{
                padding: 6px 12px;
                font-size: 0.85em;
            }}
        }}
    </style>
</head>
<body>
    <header>
        <h1>Professional Portfolio</h1>
        <p>Building beautiful digital experiences</p>
        <div class="contact-info">
            <span>📧 {email}</span>
            <span>📱 {phone}</span>
        </div>
    </header>
    
    <div class="container">
        <section id="about">
            <h2>About Me</h2>
            <p class="about-text">
                I'm a passionate developer dedicated to creating innovative solutions and delivering high-quality software. 
                With a strong foundation in full-stack development and a commitment to continuous learning, 
                I strive to make a meaningful impact through technology.
            </p>
        </section>
        
        <section id="skills">
            <h2>Skills & Expertise</h2>
            <div class="skill-tags">
                {self._generate_skills_html(skills)}
            </div>
        </section>
        
        <section id="experience">
            <h2>Experience</h2>
            <div class="experience-item">
                <h3>Professional Experience</h3>
                <p class="about-text">{experience}</p>
            </div>
        </section>
        
        <section id="education">
            <h2>Education</h2>
            <div class="experience-item">
                <h3>Academic Background</h3>
                <p class="about-text">{education}</p>
            </div>
        </section>
    </div>
    
    <footer>
        <p>&copy; 2026 Professional Portfolio. All rights reserved.</p>
        <p>Built with HTML & CSS</p>
    </footer>
</body>
</html>"""
    
    return html


def _generate_skills_html(skills_text):
    """Convert skills text to HTML tags"""
    if not skills_text:
        default = ["Python", "JavaScript", "React", "Flask", "HTML/CSS", "REST APIs"]
    else:
        # Try to extract comma-separated skills
        default = [s.strip() for s in skills_text.split(',')[:8]]
    
    return '\n'.join([f'<span class="skill-tag">{skill}</span>' for skill in default])


def extract_section(text, keywords):
    """
    Extract a section from resume text based on keywords
    """
    lines = text.split('\n')
    section_content = []
    capture = False
    
    for line in lines:
        lower_line = line.lower()
        
        # Check if this line starts the section
        if any(kw in lower_line for kw in keywords):
            capture = True
            continue
        
        # Check if this line starts a new section (different keyword)
        if capture and any(kw in lower_line for kw in 
                          ['experience', 'education', 'skills', 'contact', 
                           'projects', 'summary', 'objective', 'references']):
            break
        
        # Capture content
        if capture and line.strip():
            section_content.append(line.strip())
    
    return ' '.join(section_content[:3]) if section_content else ""


def generate_react_portfolio(resume_text):
    """
    Generate React component code for portfolio (placeholder)
    """
    return """import React from 'react';
import './Portfolio.css';

export default function Portfolio() {
  return (
    <div className="portfolio">
      <header>
        <h1>Your Portfolio</h1>
        <p>Powered by Resume to Portfolio Generator</p>
      </header>
      
      <main>
        <section>
          <h2>About</h2>
          <p>Your professional summary here</p>
        </section>
        
        <section>
          <h2>Skills</h2>
          <div className="skills">
            <span>Skill 1</span>
            <span>Skill 2</span>
          </div>
        </section>
      </main>
    </div>
  );
}"""
