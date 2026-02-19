import React from 'react';
import './PortfolioPreview.css';

interface PortfolioPreviewProps {
  portfolio: {
    html: string;
    error?: string;
  };
}

const PortfolioPreview: React.FC<PortfolioPreviewProps> = ({ portfolio }) => {
  if (portfolio.error) {
    return (
      <div className="portfolio-preview">
        <h2>Portfolio Preview</h2>
        <div className="error-message">
          <p>{portfolio.error}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="portfolio-preview">
      <div className="preview-header">
        <h2>Portfolio Preview</h2>
        <a
          href={`data:text/html;charset=utf-8,${encodeURIComponent(portfolio.html)}`}
          download="portfolio.html"
          className="download-btn"
        >
          ⬇ Download HTML
        </a>
      </div>
      
      <div className="preview-container">
        <iframe
          title="Portfolio Preview"
          srcDoc={portfolio.html}
          className="preview-iframe"
        />
      </div>
    </div>
  );
};

export default PortfolioPreview;
