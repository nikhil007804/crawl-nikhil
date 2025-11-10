# Deploying to Streamlit Cloud

## Prerequisites
1. Push your code to a GitHub repository
2. Have a Firecrawl API key

## Steps to Deploy

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit: Web crawler app"
git branch -M main
git remote add origin https://github.com/yourusername/your-repo-name.git
git push -u origin main
```

### 2. Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Set main file path: `app.py`
6. Click "Deploy"

### 3. Add API Key to Secrets
1. In your deployed app, click the settings gear icon
2. Go to "Secrets"
3. Add your API key:
```toml
FIRECRAWL_API_KEY = "your_actual_api_key_here"
```
4. Click "Save"

### 4. Your app is live!
Your app will be available at: `https://your-app-name.streamlit.app`

## Files needed for deployment:
- ✅ `app.py` - Main application
- ✅ `requirements.txt` - Dependencies
- ❌ `.env` - Not needed (use Streamlit secrets instead)
- ❌ `.streamlit/secrets.toml` - Only for local development

## Troubleshooting
- If deployment fails, check the logs in Streamlit Cloud
- Make sure all dependencies are in `requirements.txt`
- Verify your API key is correctly set in secrets
