import os
from typing import Optional


def generate_portfolio(resume_text: str, model: Optional[str] = None, api_key: Optional[str] = None) -> str:
    """
    Generate portfolio HTML from resume text using configured LLM
    
    Supports: Claude, Gemini, GPT, Llama, Qwen, Groq, and more!
    
    Args:
        resume_text: Extracted text from resume
        model: Optional model override
        api_key: Optional API key (overrides environment variable)
    
    Returns:
        HTML string for portfolio website
    """
    
    # Get model configuration
    configured_model = model or os.getenv('LLM_MODEL', 'offline')
    
    # Determine if we should use API (if model is not offline or api_key is provided)
    if api_key or (configured_model != 'offline' and os.getenv('USE_LLM_API', 'false').lower() == 'true'):
        try:
            html = call_llm_api(resume_text, configured_model, api_key)
            if html:
                return html
        except Exception as e:
            print(f"LLM API error: {e}. Using offline template.")
    
    # Otherwise use template mode
    return generate_portfolio_template(resume_text)


def call_llm_api(resume_text: str, model: str, api_key: Optional[str] = None) -> Optional[str]:
    """
    Call various LLM APIs based on model selection
    
    Supported providers:
    - Euron.ai: euron:gpt-4.1-nano, euron:gpt-4.1-mini (FREE - 10k tokens/day!)
    - Google: gemini-2.5-flash, gemini-2.5-pro, gemini-2.0-flash
    - OpenAI: gpt-5-mini, gpt-5-nano, gpt-4.1-mini
    - Meta: llama-3.3-70b, llama-4-scout, llama-4-maverick  
    - Groq: groq/compound, groq/compound-mini
    - Alibaba: qwen/qwen3-32b
    """
    
    if model.startswith('euron'):
        return call_euron_ai(resume_text, model, api_key)
    elif model.startswith('gemini'):
        return call_google_gemini(resume_text, model, api_key)
    elif model.startswith('gpt'):
        return call_openai(resume_text, model, api_key)
    elif model.startswith('llama') or 'llama' in model:
        return call_llama_model(resume_text, model, api_key)
    elif model.startswith('qwen'):
        return call_alibaba(resume_text, model, api_key)
    elif model.startswith('groq'):
        return call_groq(resume_text, model, api_key)
    
    return None


def call_euron_ai(resume_text: str, model: str, api_key: Optional[str] = None) -> Optional[str]:
    """Call Euron.ai API (OpenAI-compatible, FREE 10k tokens/day)"""
    try:
        import requests
        
        api_key = api_key or os.getenv('EURON_API_KEY')
        if not api_key:
            print("EURON_API_KEY not set")
            return None
        
        # Extract model name (format: euron:gpt-4.1-nano)
        model_name = model.split(':')[1] if ':' in model else model
        
        prompt = f"""You are an expert web designer. Create ADVANCED RESPONSIVE HTML5 portfolio that is UNIQUE with enriched modern features.

Extract: Name, title, email, phone, location, summary, ALL work experience (3-5 achievements), ALL education, technical skills grouped by category, soft skills, certifications.

Design: Animated hero with gradient background, sticky mobile navigation, experience timeline or cards with badges, skill progress bars grouped by category, education cards, professional about section, contact with social links. Add subtle animations, hover effects, CSS gradients, responsive grid layouts. Fully responsive on mobile/tablet/desktop.

Color scheme: Professional 2-3 colors with good contrast. Typography: 2-3 font families using system fonts or Google Fonts @import. Include boxes shadows, smooth transitions, custom scrollbar.

Create DIFFERENT design each time - vary layout, colors, and style (modern minimalist, dark professional, colorful creative, card-based, timeline, parallax).

ONLY complete HTML5 with embedded CSS. NO external dependencies, NO images. Starting <!DOCTYPE html>, NO markdown.

Resume: {resume_text}"""
        
        response = requests.post(
            'https://api.euron.one/api/v1/euri/chat/completions',
            headers={
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            },
            json={
                'messages': [{'role': 'user', 'content': prompt}],
                'model': model_name,
                'temperature': 0.8,
                'max_tokens': 4096
            },
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['message']['content']
        else:
            print(f"Euron.ai error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Euron.ai error: {e}")
        return None


def call_google_gemini(resume_text: str, model: str, api_key: Optional[str] = None) -> Optional[str]:
    """Call Google Gemini API"""
    try:
        import google.generativeai as genai
        
        api_key = api_key or os.getenv('GOOGLE_API_KEY')
        if not api_key:
            print("GOOGLE_API_KEY not set")
            return None
        
        genai.configure(api_key=api_key)
        client = genai.GenerativeModel(model)
        
        prompt = f"""You are an expert web designer and developer. Generate an ADVANCED, RESPONSIVE, PROFESSIONAL HTML5 portfolio website that is UNIQUE and ENRICHED with modern features.

=== DATA EXTRACTION ===
Carefully extract from resume: Full name, professional title, email, phone, location, professional summary, ALL work experience, ALL education, ALL technical skills grouped by category, certifications, awards.

=== DESIGN FEATURES (ADVANCED) ===
1. HEADER/HERO: Animated gradient, clear name/title, smooth scroll indicator, mobile navigation
2. NAVIGATION: Sticky header, hamburger menu for mobile, active section highlighting
3. EXPERIENCE: Timeline or cards with company badges, job title, dates, 3-5 achievements, hover effects
4. SKILLS: Progress bars with visual indicators, grouped by category, color-coded, responsive grid
5. EDUCATION: Clean cards, degree, institution, graduation date, GPA, relevant coursework
6. ABOUT: Professional bio (100-200 words), key highlights, photo placeholder
7. CONTACT: Email, phone, social links, contact form, download resume button

=== RESPONSIVE DESIGN ===
- Mobile-first approach (perfect on phones)
- Tablet optimizations
- Desktop enhancements
- CSS Grid/Flexbox layouts
- Responsive fonts (rem/em units)
- Touch-friendly buttons (44px min height)
- No horizontal scrolling

=== ADVANCED CSS FEATURES ===
- Subtle animations (fade-in, slide effects)
- Hover effects (cards lift, color changes)
- Smooth transitions
- Box shadows for depth
- CSS gradients
- Custom scrollbar styling

=== COLOR & STYLING ===
- Professional 2-3 color scheme
- High contrast for readability
- 2-3 font families
- White space for breathing room
- Icon usage for hierarchy

=== UNIQUE DESIGN VARIATION ===
Create DIFFERENT design each time: Modern minimalist, Colorful creative, Dark professional, Card-based, Timeline, Parallax

=== OUTPUT ===
- Complete valid HTML5
- ALL CSS embedded in <style>
- NO external dependencies
- System fonts or Google Fonts @import
- Inline SVG for icons
- Starting with <!DOCTYPE html>
- ONLY HTML, NO markdown

Resume:
{resume_text}"""
        
        response = client.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Google Gemini error: {e}")
        return None


def call_openai(resume_text: str, model: str, api_key: Optional[str] = None) -> Optional[str]:
    """Call OpenAI API"""
    try:
        from openai import OpenAI
        
        api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not api_key:
            print("OPENAI_API_KEY not set")
            return None
        
        client = OpenAI(api_key=api_key)
        
        prompt = f"""You are an expert web designer and developer. Generate an ADVANCED, RESPONSIVE, PROFESSIONAL HTML5 portfolio website that is UNIQUE and ENRICHED with modern features.

=== DATA EXTRACTION ===
Carefully extract from resume:
- Full name, professional title, email, phone, location
- Professional summary/objective
- ALL work experience (company, title, duration, 3+ achievements per job)
- ALL education (degree, institution, graduation date, GPA if present)
- ALL technical skills (group by category: languages, frameworks, tools, etc.)
- Soft skills (communication, leadership, teamwork, etc.)
- Certifications, awards, projects, publications

=== DESIGN FEATURES (ADVANCED) ===

1. HEADER/HERO SECTION:
   - Full-screen or large call-to-action area
   - Animated gradient background OR subtle pattern
   - Clear name, title, and tagline
   - Smooth scroll indicator
   - Mobile-optimized navigation

2. NAVIGATION:
   - Sticky header with smooth scrolling
   - Hamburger menu for mobile
   - Active section highlighting

3. EXPERIENCE SECTION:
   - Timeline layout or card-based design
   - Company logo placeholder or colored company badges
   - Job title as heading
   - Date range with duration calculation
   - 3-5 bullet points per job
   - Hover effects on cards (desktop)

4. SKILLS SECTION:
   - Skill progress bars/visual indicators (0-100%)
   - Skills grouped by category (Technical, Languages, Tools, Soft Skills)
   - Color-coded skill categories
   - Responsive grid layout
   - Optional: Skill proficiency levels

5. EDUCATION SECTION:
   - Clean card layout
   - Institution name, degree, field
   - Graduation date
   - GPA if present
   - Relevant coursework or achievements

6. ABOUT SECTION:
   - Professional biography (100-200 words)
   - Key highlights or achievements
   - Professional photo placeholder
   - Call-to-action button

7. CONTACT SECTION:
   - Email, phone, LinkedIn, GitHub (if available)
   - Simple contact form HTML (action can be placeholder)
   - Social media icons with hover effects
   - Download resume button (href=#)

=== RESPONSIVE DESIGN REQUIREMENTS ===
- Mobile-first approach (works perfectly on phones)
- Tablet optimizations (medium screens)
- Desktop enhancements (large screens)
- Flexible layouts using CSS Grid/Flexbox
- Responsive font sizes (using rem/em units)
- Touch-friendly buttons (min 44px height)
- No horizontal scrolling on any device
- Proper spacing and padding for all screen sizes

=== ADVANCED CSS FEATURES ===
- Subtle animations (fade-in, slide effects on scroll)
- Hover effects (cards lift, text changes color)
- Smooth transitions between colors/states
- Box shadows for depth
- CSS gradients for visual appeal
- Custom scrollbar styling
- Loading animations

=== COLOR & STYLING ===
- Professional color scheme (2-3 main colors + accent)
- High contrast for readability
- Consistent typography (2-3 font families)
- White space for visual breathing room
- Icon usage for visual hierarchy

=== UNIQUE DESIGN VARIATION ===
- Create a DIFFERENT design style each time
- Options: Modern minimalist, Colorful creative, Dark mode professional, Card-based, Timeline, Parallax effects
- Use different layouts, color schemes, and typography for variety

=== OUTPUT REQUIREMENTS ===
- Complete, valid HTML5 document
- ALL CSS embedded in <style> tag
- NO external dependencies, NO images, NO external fonts
- Use system fonts or Google Fonts @import
- Inline SVG for icons if needed
- Self-contained and deployable
- Starting with <!DOCTYPE html>
- NO markdown, NO explanations, ONLY HTML

Resume:
{resume_text}"""
        
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4096,
            temperature=0.9
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI error: {e}")
        return None


def call_groq(resume_text: str, model: str, api_key: Optional[str] = None) -> Optional[str]:
    """Call Groq API (fast inference)"""
    try:
        from groq import Groq
        
        api_key = api_key or os.getenv('GROQ_API_KEY')
        if not api_key:
            print("GROQ_API_KEY not set")
            return None
        
        client = Groq(api_key=api_key)
        
        prompt = f"""You are an expert web designer. Generate ADVANCED RESPONSIVE HTML5 portfolio with enriched features.

Extract from resume: Name, title, email, phone, summary, ALL experience (3-5 achievements each), ALL education, technical skills (grouped), soft skills, certifications.

Design with: Animated hero section, sticky nav, experience timeline/cards, skill progress bars, education cards, about section, contact section. Include subtle animations, hover effects, gradients, 2-3 color scheme. Make fully responsive (mobile, tablet, desktop). NO external files. ONLY HTML starting <!DOCTYPE html>.

Resume: {resume_text}"""
        
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4096
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Groq error: {e}")
        return None


def call_llama_model(resume_text: str, model: str, api_key: Optional[str] = None) -> Optional[str]:
    """Call Llama models via Together AI or Groq"""
    try:
        # Try Together AI first
        if 'togethercomputer' in model or 'together' in model.lower():
            return call_together_api(resume_text, model, api_key)
        # Otherwise try Groq
        else:
            return call_groq(resume_text, model, api_key)
    except Exception as e:
        print(f"Llama model error: {e}")
        return None


def call_together_api(resume_text: str, model: str, api_key: Optional[str] = None) -> Optional[str]:
    """Call Together AI API for Llama and other models"""
    try:
        import requests
        
        api_key = api_key or os.getenv('TOGETHER_API_KEY')
        if not api_key:
            print("TOGETHER_API_KEY not set")
            return None
        
        prompt = f"""Design ADVANCED RESPONSIVE HTML5 portfolio with enriched features. Extract: Name, title, email, phone, summary, ALL experience (3-5 achievements), ALL education, skills grouped, certifications. Design: Animated hero, sticky nav, experience timeline/cards, skill bars, education cards. Responsive mobile/tablet/desktop. Subtle animations, hover effects, gradients, 2-3 color scheme. ONLY HTML starting <!DOCTYPE html>. NO external files.

Resume: {resume_text}"""
        
        response = requests.post(
            "https://api.together.xyz/inference",
            headers={"Authorization": f"Bearer {api_key}"},
            json={
                "model": model,
                "prompt": prompt,
                "max_tokens": 4096,
                "temperature": 0.8,
            },
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            if 'output' in data:
                return data['output']['choices'][0]['text']
        return None
    except Exception as e:
        print(f"Together AI error: {e}")
        return None


def call_alibaba(resume_text: str, model: str, api_key: Optional[str] = None) -> Optional[str]:
    """Call Alibaba Qwen API"""
    try:
        import requests
        
        api_key = api_key or os.getenv('ALIBABA_API_KEY')
        if not api_key:
            print("ALIBABA_API_KEY not set")
            return None
        
        prompt = f"""Design ADVANCED RESPONSIVE HTML5 portfolio. Extract: Name, title, email, phone, summary, ALL experience, ALL education, skills grouped, certifications. Create: Hero section with animation, sticky nav, experience timeline/cards, skill progress bars, education cards, about, contact. Responsive mobile/tablet/desktop. Animations, hover effects, gradients, 2-3 colors. ONLY HTML <!DOCTYPE html>. NO external files.

Resume: {resume_text}"""
        
        response = requests.post(
            "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation",
            headers={"Authorization": f"Bearer {api_key}"},
            json={
                "model": model,
                "input": {"messages": [{"role": "user", "content": prompt}]},
                "parameters": {"max_tokens": 4096}
            },
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            if 'output' in data:
                return data['output']['text']
        return None
    except Exception as e:
        print(f"Alibaba error: {e}")
        return None


def generate_portfolio_template(resume_text):
    """
    Generate a professional portfolio template using the resume text
    Version 2.1 - Fixed skills generation
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
    
    # Generate skills HTML
    skills_list = [s.strip() for s in skills.split(',')[:8]]
    skills_html = '\n'.join([f'<span class="skill-tag">{skill}</span>' for skill in skills_list])
    
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
                {skills_html}
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
