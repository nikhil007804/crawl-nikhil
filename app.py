import streamlit as st
import os
from dotenv import load_dotenv
from firecrawl import FirecrawlApp
import time

# Load environment variables
load_dotenv()

# Initialize Firecrawl
@st.cache_resource
def init_firecrawl():
    # Try to get API key from Streamlit secrets first (for cloud deployment)
    api_key = None
    try:
        api_key = st.secrets["FIRECRAWL_API_KEY"]
    except:
        # Fallback to environment variable (for local development)
        api_key = os.getenv("FIRECRAWL_API_KEY")
    
    if not api_key:
        st.error("Please set FIRECRAWL_API_KEY in Streamlit secrets or .env file")
        st.info("For Streamlit Cloud: Add your API key in the app settings under 'Secrets'")
        return None
    return FirecrawlApp(api_key=api_key)

def main():
    st.set_page_config(
        page_title="Web Crawler",
        page_icon="🕷️",
        layout="wide"
    )
    
    st.title("🕷️ Web Crawler with Firecrawl")
    st.markdown("Enter a URL to crawl and extract content")
    
    # Initialize Firecrawl
    app = init_firecrawl()
    if not app:
        return
    
    # URL input
    url = st.text_input("Enter URL to crawl:", placeholder="https://example.com")
    
    # Crawl options
    col1, col2 = st.columns(2)
    with col1:
        include_tags = st.multiselect(
            "Include specific tags (optional):",
            ["h1", "h2", "h3", "p", "a", "img", "div", "span"],
            default=["h1", "h2", "h3", "p"]
        )
    
    with col2:
        exclude_tags = st.multiselect(
            "Exclude tags (optional):",
            ["script", "style", "nav", "footer", "header"],
            default=["script", "style"]
        )
    
    # Crawl button
    if st.button("🚀 Start Crawling", type="primary"):
        if not url:
            st.error("Please enter a URL")
            return
        
        # Show loading spinner
        with st.spinner("Crawling website... This may take a few minutes."):
            try:
                # Perform the crawl
                start_time = time.time()
                result = app.scrape(
                    url=url,
                    formats=['markdown', 'html'],
                    only_main_content=True,
                    include_tags=include_tags if include_tags else None,
                    exclude_tags=exclude_tags if exclude_tags else None
                )
                end_time = time.time()
                
                # Display results
                st.success(f"✅ Crawling completed in {end_time - start_time:.2f} seconds!")
                
                # Create tabs for different views
                tab1, tab2, tab3 = st.tabs(["📄 Markdown Content", "🔧 HTML Content", "📊 Metadata"])
                
                with tab1:
                    st.subheader("Extracted Markdown Content")
                    if hasattr(result, 'markdown') and result.markdown:
                        st.markdown("```markdown\n" + result.markdown + "\n```")
                        
                        # Download button for markdown
                        st.download_button(
                            label="📥 Download Markdown",
                            data=result.markdown,
                            file_name=f"crawled_content_{int(time.time())}.md",
                            mime="text/markdown"
                        )
                    else:
                        st.warning("No markdown content extracted")
                
                with tab2:
                    st.subheader("HTML Content")
                    if hasattr(result, 'html') and result.html:
                        st.code(result.html, language='html')
                        
                        # Download button for HTML
                        st.download_button(
                            label="📥 Download HTML",
                            data=result.html,
                            file_name=f"crawled_content_{int(time.time())}.html",
                            mime="text/html"
                        )
                    else:
                        st.warning("No HTML content extracted")
                
                with tab3:
                    st.subheader("Page Metadata")
                    metadata = {
                        "Title": getattr(result.metadata, 'title', 'N/A') if hasattr(result, 'metadata') else 'N/A',
                        "Description": getattr(result.metadata, 'description', 'N/A') if hasattr(result, 'metadata') else 'N/A',
                        "URL": getattr(result.metadata, 'sourceURL', url) if hasattr(result, 'metadata') else url,
                        "Status Code": getattr(result.metadata, 'statusCode', 'N/A') if hasattr(result, 'metadata') else 'N/A',
                        "Language": getattr(result.metadata, 'language', 'N/A') if hasattr(result, 'metadata') else 'N/A'
                    }
                    
                    for key, value in metadata.items():
                        st.write(f"**{key}:** {value}")
                
            except Exception as e:
                st.error(f"❌ Error during crawling: {str(e)}")
                st.info("Please check your API key and URL, then try again.")

if __name__ == "__main__":
    main()
