import React, { useState } from 'react';
import './App.css';
import ResumeUpload from './components/ResumeUpload';
import PortfolioPreview from './components/PortfolioPreview';

interface PortfolioData {
  html: string;
  error?: string;
}

function App() {
  const [portfolio, setPortfolio] = useState<PortfolioData | null>(null);
  const [loading, setLoading] = useState(false);

  const handlePortfolioGenerated = (htmlContent: string) => {
    setPortfolio({ html: htmlContent });
  };

  const handleError = (error: string) => {
    setPortfolio({ html: '', error });
  };

  return (
    <div className="app">
      <header className="app-header">
        <div className="container">
          <h1>Resume to Portfolio Generator</h1>
          <p>Transform your resume into a stunning portfolio website</p>
        </div>
      </header>

      <main className="app-main">
        <div className="container">
          <div className="grid">
            <div className="upload-section">
              <ResumeUpload 
                onPortfolioGenerated={handlePortfolioGenerated}
                onError={handleError}
                onLoading={setLoading}
              />
            </div>

            {portfolio && (
              <div className="preview-section">
                <PortfolioPreview portfolio={portfolio} />
              </div>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
