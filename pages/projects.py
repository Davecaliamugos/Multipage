import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from components import render_navigation

st.set_page_config(
    page_title="Projects | Dave Campo",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Render custom navbar and sidebar
render_navigation("projects")

# ---------- PAGE-LEVEL STYLES ----------
st.markdown("""
<style>
:root {
    --primary: #00d4ff;
    --accent: #ff6bcb;
    --bg: #050816;
    --card-bg: rgba(15, 23, 42, 0.96);
    --border-subtle: rgba(148, 163, 184, 0.35);
    --text-main: #e5e7eb;
    --text-muted: #9ca3af;
    --radius-lg: 18px;
    --shadow-soft: 0 24px 60px rgba(0, 0, 0, 0.85);
}

.stApp {
    background: radial-gradient(circle at 0% 0%, #1f2937 0, #020617 40%, #000 100%);
    color: var(--text-main);
}

.block-container {
    max-width: 900px;
    padding-top: 2.5rem !important;
    padding-bottom: 3rem !important;
}

/* Main projects card */
.project-card {
    background: var(--card-bg);
    border-radius: var(--radius-lg);
    border: 1px solid var(--border-subtle);
    padding: 1.8rem 1.6rem 1.6rem 1.6rem;
    box-shadow: var(--shadow-soft);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
}

.page-subtitle {
    font-size: 0.92rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    color: var(--primary);
    margin-bottom: 1.2rem;
}

.page-title {
    font-size: 2.2rem;
    font-weight: 800;
    margin: 0 0 0.6rem 0;
}

.page-text {
    font-size: 0.96rem;
    color: var(--text-muted);
    line-height: 1.6;
    margin-bottom: 1.4rem;
}

/* Section heading inside the card */
.section-heading {
    margin-top: 1.6rem;
    margin-bottom: 0.7rem;
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 0.18em;
    color: var(--text-muted);
}

/* Project description */
.project-description {
    font-size: 0.95rem;
    color: var(--text-main);
    margin-top: 0.4rem;
    margin-bottom: 0.9rem;
}

/* Selectbox styling */
.stSelectbox > label {
    font-size: 0.86rem;
    color: var(--text-muted);
    margin-bottom: 0.25rem;
}

/* Responsive Design */
@media (max-width: 1024px) {
    .block-container {
        max-width: 90% !important;
    }
    
    .project-card {
        padding: 1.6rem 1.4rem 1.4rem 1.4rem;
    }
    
    .page-title {
        font-size: 1.9rem;
    }
}

@media (max-width: 768px) {
    .block-container {
        max-width: 95% !important;
        padding-top: 1.8rem !important;
        padding-bottom: 2rem !important;
    }
    
    .project-card {
        padding: 1.4rem 1.2rem 1.2rem 1.2rem;
    }
    
    .page-title {
        font-size: 1.6rem;
    }
    
    .page-subtitle {
        font-size: 0.85rem;
    }
    
    .page-text {
        font-size: 0.9rem;
    }
    
    .section-heading {
        font-size: 0.85rem;
        margin-top: 1.2rem;
    }
    
    .project-description {
        font-size: 0.9rem;
    }
}

@media (max-width: 480px) {
    .block-container {
        max-width: 100% !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        padding-top: 1.5rem !important;
    }
    
    .project-card {
        padding: 1.2rem 1rem 1rem 1rem;
    }
    
    .page-title {
        font-size: 1.3rem;
    }
    
    .page-subtitle {
        font-size: 0.8rem;
        margin-bottom: 1rem;
    }
    
    .page-text {
        font-size: 0.85rem;
        margin-bottom: 1rem;
    }
    
    .section-heading {
        font-size: 0.75rem;
        margin-top: 1rem;
        margin-bottom: 0.6rem;
    }
    
    .project-description {
        font-size: 0.8rem;
    }
}

.stSelectbox [data-baseweb="select"] {
    background: rgba(15, 23, 42, 0.96);
    border-radius: 999px;
    border: 1px solid var(--border-subtle);
    color: var(--text-main);
}

/* Slider styling */
.stSlider > label {
    font-size: 0.86rem;
    color: var(--text-muted);
    margin-bottom: 0.25rem;
}

/* Responsive */
@media (max-width: 768px) {
    .page-title {
        font-size: 1.9rem;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------- DATA ----------
project_descriptions = {
    "Portfolio Website": "A personal portfolio built with modern UI/UX.",
    "Face Recognition System": "AI-based attendance system with security features.",
    "Grocery Web App": "E-commerce grocery system with cart & checkout.",
}

# ---------- LAYOUT ----------
with st.container():
    # Open main card
    st.markdown(
        """
        <div class="project-card">
            <p class="page-subtitle">Selected work</p>
            <h1 class="page-title">💼 Projects</h1>
            <p class="page-text">
                A glimpse into some of the projects I've worked on, from personal experiments
                to practical applications that solve real problems.
            </p>
        """,
        unsafe_allow_html=True,
    )

    # Project selection
    st.markdown('<div class="section-heading">Explore a project</div>', unsafe_allow_html=True)
    project = st.selectbox(
        "Select a project:",
        ["Portfolio Website", "Face Recognition System", "Grocery Web App"],
        index=0,
    )

    desc = project_descriptions.get(project, "")
    st.markdown(f"<p class='project-description'>{desc}</p>", unsafe_allow_html=True)

    # Rating section
    st.markdown('<div class="section-heading">Rate my projects</div>', unsafe_allow_html=True)
    rating = st.slider("Rate from 1 to 10:", 1, 10)

    if rating:
        st.success(f"Thanks for rating: {rating}/10 🎉")

    # Close main card
    st.markdown("</div>", unsafe_allow_html=True)