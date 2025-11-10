# Web Crawler with Firecrawl

A simple Streamlit application for web crawling using Firecrawl API.

## Setup

1. **Install dependencies:**
   ```bash
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure API Key:**
   - Update the `FIRECRAWL_API_KEY` in the `.env` file with your actual Firecrawl API key

3. **Run the application:**
   ```bash
   .venv\Scripts\activate
   streamlit run app.py
   ```

## Features

- 🕷️ Web crawling with Firecrawl API
- 📄 Extract content in Markdown and HTML formats
- 🎯 Customizable tag inclusion/exclusion
- ⏱️ Loading spinner for better UX
- 📥 Download extracted content
- 📊 View page metadata

## Usage

1. Enter a URL to crawl
2. Select tags to include/exclude (optional)
3. Click "Start Crawling"
4. View results in different tabs
5. Download content if needed

The application includes a loading spinner as crawling can take a few minutes depending on the website size.
