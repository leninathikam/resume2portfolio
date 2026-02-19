# Feature Summary: Dynamic LLM & API Key Input

## Overview
The application now accepts **LLM provider**, **API key**, and **resume file** as user inputs instead of relying on environment variables.

## Changes Made

### Frontend (`frontend/src/components/ResumeUpload.tsx`)

**New Features:**
- LLM Provider dropdown with 8 options:
  - Offline Mode (no API needed)
  - Google Gemini 2.5 Flash
  - Google Gemini 2.5 Pro
  - OpenAI GPT-4.1 Mini
  - OpenAI GPT-5 Mini
  - Meta Llama 3.3 70B
  - Groq Compound
  - Alibaba Qwen 3 32B

- API Key input field (hidden for Offline mode)
  - Password field for security
  - Shows helpful hints about API key usage
  - Explains privacy (not stored)

- Form validation:
  - Requires API key if non-offline mode is selected
  - Requires resume file
  - Button disabled until both are provided (if needed)

**State Management:**
- `selectedModel`: Tracks chosen LLM provider
- `apiKey`: Stores user's API key temporarily
- Form submission includes: `model`, `api_key`, and `resume` file

### Frontend Styling (`frontend/src/components/ResumeUpload.css`)

**New CSS Classes:**
- `.form-group`: Container for input groups
- `.model-select`: LLM provider dropdown styling
- `.api-key-input`: Text input for API key
- `.model-hint` / `.api-hint`: Helper text styling

**Features:**
- Focus states with border and shadow effects
- Responsive design maintained
- Professional color scheme consistent with existing design

### Backend API (`backend/app/routes/upload.py`)

**Updated Endpoint:**
- `POST /api/upload` now accepts:
  - `resume` (file, required)
  - `model` (form field, optional, defaults to 'offline')
  - `api_key` (form field, optional)

**Processing:**
- Extracts model and API key from form data
- Passes both to `generate_portfolio()`
- Server never stores API keys (only used for current request)

### Backend Service (`backend/app/services/llm_service.py`)

**Updated Functions:**

1. **`generate_portfolio()`**
   - New parameter: `api_key: Optional[str]`
   - Uses provided API key to trigger LLM calls
   - Falls back to offline mode if API call fails

2. **`call_llm_api()`**
   - New parameter: `api_key: Optional[str]`
   - Routes API key to appropriate provider function

3. **Provider Functions** (updated signatures):
   - `call_google_gemini()` - Google Gemini API
   - `call_openai()` - OpenAI GPT
   - `call_groq()` - Groq inference
   - `call_llama_model()` - Meta Llama via Together AI
   - `call_together_api()` - Together AI API
   - `call_alibaba()` - Alibaba Qwen

**Key Logic:**
```python
api_key = api_key or os.getenv('PROVIDER_API_KEY')
```
- Uses provided API key first
- Falls back to environment variable if not provided
- Allows both runtime and environment-based configuration

## User Flow

1. User selects LLM provider from dropdown
2. If not "Offline Mode", user enters API key
3. User uploads resume file (drag-drop or click)
4. User clicks "Generate Portfolio"
5. Frontend sends: form data with model, API key, and file
6. Backend processes and generates portfolio using specified LLM
7. Portfolio displays in preview

## Supported Models

| Provider | Models | API Env Variable |
|----------|--------|------------------|
| Offline | (template-based) | N/A |
| Google | gemini-2.5-flash, gemini-2.5-pro | GOOGLE_API_KEY |
| OpenAI | gpt-5-mini, gpt-5-nano, gpt-4.1-mini | OPENAI_API_KEY |
| Meta/Together | llama-3.3-70b, llama-4-scout | TOGETHER_API_KEY |
| Groq | groq/compound, groq/compound-mini | GROQ_API_KEY |
| Alibaba | qwen/qwen3-32b | ALIBABA_API_KEY |

## Security Considerations

- ✅ API keys are password-masked in UI (type="password")
- ✅ API keys are not stored on server
- ✅ API keys are only used for current request
- ✅ Backend validates API key presence before making API calls
- ✅ Graceful fallback to offline mode if API fails

## Testing Recommendations

1. **Test Offline Mode:**
   - Select "Offline Mode"
   - No API key input shown
   - Upload resume and generate portfolio
   - Should use template-based generation

2. **Test API Modes:**
   - Select any LLM provider
   - API key input appears
   - Enter valid API key
   - Upload resume and generate portfolio
   - Should use LLM for generation

3. **Test Error Handling:**
   - Try invalid API key
   - Should show error message
   - Should optionally fall back to offline mode

4. **Test Form Validation:**
   - Select non-offline mode without API key
   - Submit button should be disabled
   - Error message should show when attempting submission

## Environment Variables (.env)

The application still supports environment variables for backward compatibility:

```env
USE_LLM_API=false
LLM_MODEL=offline
GOOGLE_API_KEY=
OPENAI_API_KEY=
GROQ_API_KEY=
TOGETHER_API_KEY=
ALIBABA_API_KEY=
```

Users can:
- Use environment variables for production deployments
- Use UI inputs for one-off/testing scenarios
- UI inputs override environment variables
