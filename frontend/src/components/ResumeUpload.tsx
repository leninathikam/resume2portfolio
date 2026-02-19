import React, { useState } from 'react';
import axios from 'axios';
import './ResumeUpload.css';

interface ResumeUploadProps {
  onPortfolioGenerated: (html: string) => void;
  onError: (error: string) => void;
  onLoading: (loading: boolean) => void;
}

const LLM_MODELS = [
  { label: 'Offline Mode (No API needed)', value: 'offline' },
  { label: 'Euron.ai GPT-4.1 Nano (Free!)', value: 'euron:gpt-4.1-nano' },
  { label: 'Euron.ai GPT-4.1 Mini (Free!)', value: 'euron:gpt-4.1-mini' },
  { label: 'Google Gemini 2.5 Flash', value: 'gemini-2.5-flash' },
  { label: 'Google Gemini 2.5 Pro', value: 'gemini-2.5-pro' },
  { label: 'OpenAI GPT-4.1 Mini', value: 'gpt-4.1-mini' },
  { label: 'OpenAI GPT-5 Mini', value: 'gpt-5-mini' },
  { label: 'Meta Llama 3.3 70B', value: 'llama-3.3-70b' },
  { label: 'Groq Compound', value: 'groq/compound' },
  { label: 'Alibaba Qwen 3 32B', value: 'qwen/qwen3-32b' },
];

const ResumeUpload: React.FC<ResumeUploadProps> = ({
  onPortfolioGenerated,
  onError,
  onLoading
}) => {
  const [file, setFile] = useState<File | null>(null);
  const [isDragging, setIsDragging] = useState(false);
  const [message, setMessage] = useState('');
  const [selectedModel, setSelectedModel] = useState(LLM_MODELS[0].value);
  const [apiKey, setApiKey] = useState('');

  const handleDragOver = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => {
    setIsDragging(false);
  };

  const handleDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    setIsDragging(false);
    const files = e.dataTransfer.files;
    if (files.length > 0) {
      setFile(files[0]);
      setMessage('');
    }
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0]);
      setMessage('');
    }
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!file) {
      setMessage('Please select a resume file');
      return;
    }

    if (selectedModel !== 'offline' && !apiKey.trim()) {
      setMessage('Please enter an API key for the selected model');
      return;
    }

    const formData = new FormData();
    formData.append('resume', file);
    formData.append('model', selectedModel);
    if (apiKey.trim()) {
      formData.append('api_key', apiKey);
    }

    try {
      onLoading(true);
      setMessage('Generating your portfolio...');

      const response = await axios.post('/api/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });

      if (response.data.success) {
        setMessage('Portfolio generated successfully!');
        onPortfolioGenerated(response.data.portfolio);
        setFile(null);
      } else {
        onError(response.data.error || 'Failed to generate portfolio');
        setMessage('Error: ' + (response.data.error || 'Failed to generate portfolio'));
      }
    } catch (error: any) {
      const errorMsg = error.response?.data?.error || error.message || 'An error occurred';
      onError(errorMsg);
      setMessage('Error: ' + errorMsg);
    } finally {
      onLoading(false);
    }
  };

  return (
    <div className="resume-upload">
      <h2>Upload Your Resume</h2>
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="model-select">Select LLM Provider:</label>
          <select 
            id="model-select"
            value={selectedModel}
            onChange={(e) => setSelectedModel(e.target.value)}
            className="model-select"
          >
            {LLM_MODELS.map(model => (
              <option key={model.value} value={model.value}>
                {model.label}
              </option>
            ))}
          </select>
          <p className="model-hint">
            {selectedModel === 'offline' 
              ? 'No API key needed - uses template-based generation'
              : 'You must provide your API key for this provider'}
          </p>
        </div>

        {selectedModel !== 'offline' && (
          <div className="form-group">
            <label htmlFor="api-key">API Key:</label>
            <input
              id="api-key"
              type="password"
              value={apiKey}
              onChange={(e) => setApiKey(e.target.value)}
              placeholder="Enter your API key for the selected provider"
              className="api-key-input"
            />
            <p className="api-hint">Your API key is sent only to generate your portfolio and is not stored.</p>
          </div>
        )}

        <div
          className={`drop-zone ${isDragging ? 'dragging' : ''}`}
          onDragOver={handleDragOver}
          onDragLeave={handleDragLeave}
          onDrop={handleDrop}
        >
          <svg className="upload-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
          </svg>
          <p>Drag and drop your resume here or click to select</p>
          <p className="file-types">Supported: PDF, DOCX, DOC, TXT</p>
          <input
            type="file"
            onChange={handleFileChange}
            accept=".pdf,.docx,.doc,.txt"
            className="file-input"
          />
        </div>

        {file && (
          <div className="file-info">
            <p className="file-name">{file.name}</p>
            <p className="file-size">({(file.size / 1024).toFixed(2)} KB)</p>
          </div>
        )}

        <button
          type="submit"
          className="submit-btn"
          disabled={!file || (selectedModel !== 'offline' && !apiKey.trim())}
        >
          Generate Portfolio
        </button>
      </form>

      {message && (
        <div className={`message ${message.startsWith('Error') ? 'error' : 'success'}`}>
          {message}
        </div>
      )}
    </div>
  );
};

export default ResumeUpload;
