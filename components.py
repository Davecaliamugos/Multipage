import streamlit as st

def render_navigation(active_page: str = "home"):
    """
    Render a clean navbar using Streamlit's native page_link.
    """
    pages = [
        ("home", "home.py", "Home"),
        ("about", "pages/about.py", "About"),
        ("projects", "pages/projects.py", "Projects"),
        ("skills", "pages/skills.py", "Skills"),
        ("certificates", "pages/certificates.py", "Certificates"),
        ("contact", "pages/contact.py", "Contact"),
    ]
    
    # CSS for styling - clean navbar
    st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at 0% 0%, #1f2937 0, #020617 40%, #000 100%);
    }
    
    header[data-testid="stHeader"] {
        display: none !important;
    }
    
    .block-container {
        padding-top: 0 !important;
        max-width: 1100px !important;
    }
    
    section[data-testid="stSidebar"] { 
        display: none !important; 
    }
    
    /* Navbar row styling */
    [data-testid="stVerticalBlock"] > div > [data-testid="stHorizontalBlock"] {
        background: rgba(15, 23, 42, 0.95) !important;
        border-bottom: 1px solid rgba(148, 163, 184, 0.2) !important;
        padding: 0.5rem 0 !important;
        margin: 0 0 1rem 0 !important;
        border-radius: 0 !important;
    }
    
    /* Navbar link styling */
    .stPageLink {
        text-align: center !important;
    }
    .stPageLink a {
        color: #9ca3af !important;
        text-decoration: none !important;
        padding: 0.35rem 0.7rem !important;
        border-radius: 999px !important;
        font-size: 0.85rem !important;
        transition: all 0.2s ease !important;
        display: inline-block !important;
    }
    .stPageLink a:hover {
        color: #00d4ff !important;
        background: rgba(0, 212, 255, 0.1) !important;
    }
    .stPageLink a[aria-current="page"] {
        color: #00d4ff !important;
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.15), rgba(255, 107, 203, 0.1)) !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
    }
    
    /* Mobile responsive - maintain same design */
    @media (max-width: 768px) {
        [data-testid="stVerticalBlock"] > div > [data-testid="stHorizontalBlock"] {
            flex-wrap: wrap !important;
            gap: 0.3rem !important;
            padding: 0.5rem 0 !important;
        }
        
        [data-testid="stHorizontalBlock"] > div {
            min-width: 0 !important;
            flex: 1 1 auto !important;
        }
        
        .stPageLink a {
            font-size: 0.7rem !important;
            padding: 0.3rem 0.5rem !important;
            white-space: normal !important;
        }
        
        [data-testid="stMarkdownContainer"] span {
            font-size: 1rem !important;
        }
    }
    
    /* Tablet breakpoint */
    @media (max-width: 1024px) {
        .block-container {
            max-width: 95% !important;
        }
    }
    
    /* Extra small phones */
    @media (max-width: 480px) {
        [data-testid="stVerticalBlock"] > div > [data-testid="stHorizontalBlock"] {
            padding: 0.4rem 0 !important;
        }
        
        .stPageLink a {
            font-size: 0.65rem !important;
            padding: 0.2rem 0.4rem !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Navbar container - full width
    cols = st.columns([2, 1, 1, 1, 1, 1, 1], gap="small")
    
    # Logo
    with cols[0]:
        st.markdown("""
        <span style="font-size: 1.3rem; font-weight: 700; 
        background: linear-gradient(120deg, #00d4ff, #ff6bcb);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            Dave.dev
        </span>
        """, unsafe_allow_html=True)
    
    # Navigation links
    for i, (key, page_path, label) in enumerate(pages):
        with cols[i+1]:
            st.page_link(page_path, label=label)
