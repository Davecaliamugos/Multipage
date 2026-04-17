import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
import base64
from components import render_navigation

# 1. PAGE CONFIG
st.set_page_config(
    page_title="Dave Campo | Portfolio",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Render custom navbar and sidebar
render_navigation("home")

# 2. ENHANCED GLOBAL STYLES
st.markdown("""
<style>
:root {
    --primary: #00d4ff;
    --primary-soft: rgba(0, 212, 255, 0.14);
    --accent: #ff6bcb;
    --bg: #050816;
    --bg-alt: #0b1020;
    --card-bg: rgba(15, 23, 42, 0.92);
    --border-subtle: rgba(148, 163, 184, 0.35);
    --text-main: #e5e7eb;
    --text-muted: #9ca3af;
    --radius-lg: 18px;
    --radius-xl: 26px;
    --shadow-soft: 0 24px 60px rgba(0, 0, 0, 0.8);
}

/* App background */
.stApp {
    background: radial-gradient(circle at 0% 0%, #1f2937 0, #020617 40%, #000 100%);
    color: var(--text-main);
}

/* Main content container */
.block-container {
    max-width: 1100px;
    padding-top: 2.5rem !important;
    padding-bottom: 3rem !important;
}

/* Remove default Streamlit white background where it appears */
.main {
    background-color: transparent;
}

/* ---------- HERO SECTION ---------- */

.hero-image-card {
    position: relative;
    width: 260px;
    max-width: 100%;
    aspect-ratio: 1;
    border-radius: var(--radius-xl);
    padding: 6px;
    background:
        radial-gradient(circle at top, rgba(56, 189, 248, 0.35), transparent 55%),
        linear-gradient(145deg, #020617, #020617);
    box-shadow: var(--shadow-soft);
    overflow: hidden;
    animation: floatUp 0.85s ease-out both;
}

.hero-image-card::after {
    content: "";
    position: absolute;
    inset: -1px;
    border-radius: inherit;
    border: 1px solid rgba(148, 163, 184, 0.4);
    mix-blend-mode: screen;
    pointer-events: none;
}

.hero-image-card img.profile-img,
.hero-image-card [data-testid="stImage"] img {
    width: 100%;
    height: 100%;
    border-radius: inherit;
    object-fit: cover;
    filter: saturate(1.1);
    transform: translateY(2px);
    transition: transform 0.25s ease, filter 0.25s ease;
}

.hero-image-card:hover img.profile-img,
.hero-image-card:hover [data-testid="stImage"] img {
    transform: translateY(-4px) scale(1.02);
    filter: saturate(1.3);
}

.hero-text {
    padding-top: 0.3rem;
    animation: floatUp 0.9s ease-out both;
    animation-delay: 0.05s;
}

.hero-eyebrow {
    text-transform: uppercase;
    letter-spacing: 0.18em;
    font-size: 0.78rem;
    color: var(--primary);
    font-weight: 600;
    margin-bottom: 0.8rem;
    opacity: 0.9;
}

.hero-text h1 {
    font-size: 2.8rem;
    line-height: 1.08;
    font-weight: 800;
    margin: 0 0 0.7rem 0;
}

.hero-text h1 span {
    background: linear-gradient(120deg, var(--primary), var(--accent));
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}

.hero-subtitle {
    font-size: 0.98rem;
    max-width: 34rem;
    color: var(--text-muted);
    margin-bottom: 1.4rem;
}

.hero-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin-bottom: 1.6rem;
}

.hero-tag {
    font-size: 0.78rem;
    padding: 0.18rem 0.7rem;
    border-radius: 999px;
    border: 1px solid rgba(148, 163, 184, 0.4);
    background: radial-gradient(circle at top, rgba(15, 23, 42, 0.9), rgba(15, 23, 42, 0.75));
    color: var(--text-muted);
}

/* ---------- BUTTONS (GitHub / LinkedIn / Say Hello) ---------- */

a[data-testid="stLinkButton"] {
    border-radius: 999px;
    padding: 0.45rem 1.4rem;
    border: 1px solid rgba(148, 163, 184, 0.5);
    background: rgba(15, 23, 42, 0.92);
    color: var(--text-main);
    font-size: 0.86rem;
    font-weight: 500;
    box-shadow: 0 14px 35px rgba(15, 23, 42, 0.8);
    transition: all 0.22s ease;
    text-decoration: none !important;
}

a[data-testid="stLinkButton"]:hover {
    border-color: var(--primary);
    background: linear-gradient(135deg, var(--primary), var(--accent));
    color: #020617 !important;
    transform: translateY(-2px);
    box-shadow: 0 20px 45px rgba(0, 212, 255, 0.35);
}

/* Primary buttons (e.g. "Say Hello") */
div.stButton > button:first-child {
    background: linear-gradient(135deg, var(--primary), var(--accent));
    color: #020617;
    border-radius: 999px;
    border: none;
    padding: 0.5rem 1.6rem;
    font-weight: 600;
    font-size: 0.9rem;
    box-shadow: 0 18px 40px rgba(0, 212, 255, 0.3);
    transition: all 0.22s ease;
}

div.stButton > button:first-child:hover {
    transform: translateY(-2px) scale(1.02);
    box-shadow: 0 24px 55px rgba(0, 212, 255, 0.5);
}

/* ---------- SECTION DIVIDERS & TITLES ---------- */

.section-divider {
    border: none;
    border-top: 1px solid rgba(148, 163, 184, 0.35);
    margin: 2.2rem 0 1.9rem;
}

.section-title {
    font-size: 1.05rem;
    text-transform: uppercase;
    letter-spacing: 0.16em;
    color: var(--text-muted);
    margin-bottom: 0.9rem;
}

/* ---------- METRICS / STATS CARDS ---------- */

.stats-row {
    margin-bottom: 2.2rem;
}

.stat-card {
    position: relative;
    background: var(--card-bg);
    border-radius: var(--radius-lg);
    padding: 1.05rem 1.1rem;
    border: 1px solid var(--border-subtle);
    box-shadow: 0 20px 50px rgba(15, 23, 42, 0.95);
    overflow: hidden;
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
}

.stat-card::before {
    content: "";
    position: absolute;
    inset: -1px;
    border-radius: inherit;
    background: radial-gradient(circle at top, rgba(56, 189, 248, 0.22), transparent 58%);
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.22s ease;
}

.stat-card:hover {
    transform: translateY(-5px) scale(1.01);
    border-color: rgba(56, 189, 248, 0.7);
    box-shadow: 0 26px 60px rgba(0, 0, 0, 0.95);
}

.stat-card:hover::before {
    opacity: 1;
}

.stat-label {
    text-transform: uppercase;
    font-size: 0.74rem;
    letter-spacing: 0.18em;
    color: var(--text-muted);
    margin-bottom: 0.12rem;
}

.stat-value {
    font-size: 1.6rem;
    font-weight: 700;
}

/* ---------- TECH STACK PILLS ---------- */

.tech-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-top: 0.4rem;
}

.tech-pill {
    font-size: 0.78rem;
    padding: 0.18rem 0.7rem;
    border-radius: 999px;
    border: 1px solid rgba(148, 163, 184, 0.35);
    background: rgba(15, 23, 42, 0.9);
    color: var(--text-muted);
}

/* ---------- EXPANDER / CONTACT CARD ---------- */

[data-testid="stExpander"] {
    border-radius: var(--radius-xl) !important;
    border: 1px solid var(--border-subtle) !important;
    background:
        radial-gradient(circle at 0% 0%, rgba(56, 189, 248, 0.14), transparent 60%),
        radial-gradient(circle at 100% 0%, rgba(244, 114, 182, 0.1), transparent 55%),
        rgba(15, 23, 42, 0.98) !important;
    box-shadow: var(--shadow-soft);
    overflow: hidden;
}

[data-testid="stExpander"] > div {
    background: transparent !important;
    border: none !important;
}

/* Input styling */
input[type="text"] {
    border-radius: 999px;
    border: 1px solid var(--border-subtle);
    background: rgba(15, 23, 42, 0.96);
    color: var(--text-main);
    font-size: 0.9rem;
    padding: 0.45rem 0.85rem;
}

input[type="text"]::placeholder {
    color: rgba(148, 163, 184, 0.7);
}

/* ---------- FOOTER ---------- */

.footer-divider {
    margin-top: 2.5rem;
    border-top: 1px solid rgba(148, 163, 184, 0.3);
}

.footer-note {
    text-align: right;
    opacity: 0.7;
    font-size: 0.82rem;
}

/* ---------- ANIMATIONS ---------- */

@keyframes floatUp {
    from {
        opacity: 0;
        transform: translateY(8px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Responsive tweaks */
@media (max-width: 1024px) {
    .block-container {
        max-width: 90% !important;
    }
    
    .hero-text h1 {
        font-size: 2.4rem;
    }
    
    .stat-card {
        padding: 0.9rem 1rem !important;
    }
}

@media (max-width: 768px) {
    .block-container {
        max-width: 95% !important;
        padding-top: 1.8rem !important;
    }
    
    .hero-image-card {
        width: 200px;
        margin: 0 auto 1.5rem auto;
    }
    
    .hero-text h1 {
        font-size: 1.8rem;
        line-height: 1.1;
    }
    
    .hero-eyebrow {
        font-size: 0.7rem;
    }
    
    .hero-subtitle {
        font-size: 0.85rem;
        max-width: 100%;
    }
    
    .hero-tag {
        font-size: 0.7rem;
        padding: 0.12rem 0.6rem;
    }
    
    a[data-testid="stLinkButton"] {
        font-size: 0.75rem;
        padding: 0.35rem 1rem;
    }
    
    .stat-card {
        padding: 0.8rem 0.9rem !important;
    }
    
    .stat-label {
        font-size: 0.65rem;
    }
    
    .stat-value {
        font-size: 1.3rem;
    }
    
    .section-title {
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
    
    .hero-image-card {
        width: 160px;
        margin: 0 auto 1.2rem auto;
    }
    
    .hero-text h1 {
        font-size: 1.5rem;
    }
    
    .hero-subtitle {
        font-size: 0.8rem;
    }
    
    .hero-tag {
        font-size: 0.65rem;
        padding: 0.1rem 0.5rem;
    }
    
    a[data-testid="stLinkButton"] {
        font-size: 0.7rem;
        padding: 0.3rem 0.9rem;
    }
    
    .stat-card {
        padding: 0.7rem 0.8rem !important;
    }
    
    .stat-label {
        font-size: 0.6rem;
    }
    
    .stat-value {
        font-size: 1.1rem;
    }
    
    input[type="text"] {
        font-size: 0.85rem;
        padding: 0.4rem 0.75rem;
    }
}
</style>
""", unsafe_allow_html=True)

# 3. HERO SECTION
with st.container():
    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        # Read and encode profile image to base64 for HTML embedding
        with open("assets/profile/profile.png", "rb") as img_file:
            profile_b64 = base64.b64encode(img_file.read()).decode()
        
        st.markdown(
            f"""
            <div class="hero-image-card">
                <img src="data:image/png;base64,{profile_b64}" class="profile-img" alt="Profile picture of Dave Campo" />
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="hero-text">
                <p class="hero-eyebrow">Full-Stack Developer · AI Enthusiast</p>
                <h1>👋 Hi, I'm <span>Dave</span></h1>
                <p class="hero-subtitle">
                    I bridge the gap between complex backend logic and intuitive user experiences.
                    Currently specializing in high-performance web applications and automated AI workflows.
                </p>
                <div class="hero-tags">
                    <span class="hero-tag">Python</span>
                    <span class="hero-tag">FastAPI</span>
                    <span class="hero-tag">React</span>
                    <span class="hero-tag">Streamlit</span>
                    <span class="hero-tag">LLM Apps</span>
                    <span class="hero-tag">MLOps</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        c1, c2, _ = st.columns([1, 1, 3])
        with c1:
            st.link_button("GitHub", "https://github.com/")
        with c2:
            st.link_button("LinkedIn", "https://linkedin.com/")

# 4. EXPERIENCE & TECH STACK
st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>By the numbers</div>", unsafe_allow_html=True)

metrics = [
    ("Projects", "15+"),
    ("Experience", "3 Years"),
    ("Uptime", "99.9%"),
    ("Coffee / Day", "4 Cups"),
]

cols = st.columns(4)
for i, (label, value) in enumerate(metrics):
    with cols[i]:
        st.markdown(
            f"""
            <div class="stat-card">
                <p class="stat-label">{label}</p>
                <p class="stat-value">{value}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# Add CSS to make stats responsive
st.markdown("""
<style>
@media (max-width: 1024px) {
    /* On tablet, show 2 columns for stats */
    [data-testid="stColumn"]:nth-child(n+3) {
        margin-top: -30px;
    }
}

@media (max-width: 768px) {
    /* On mobile, show 2 columns by adjusting layout */
}
</style>
""", unsafe_allow_html=True)



# 5. INTERACTIVE SECTION
st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)
st.markdown("<h3 class='section-title'>Let's connect</h3>", unsafe_allow_html=True)

with st.expander("Quick Greeting", expanded=True):
    name = st.text_input("What's your name?", placeholder="Type here...")
    if st.button("Say Hello"):
        if name:
            st.success(f"Great to meet you, {name}! Thanks for stopping by my digital space.")
        else:
            st.info("I'd love to know who's visiting!")

# 6. FOOTER
st.markdown("<div class='footer-divider'></div>", unsafe_allow_html=True)
footer_col1, footer_col2 = st.columns(2)
with footer_col1:
    st.caption("© 2026 Dave Campo. Built with Python & Streamlit.")
with footer_col2:
    st.markdown(
        "<p class='footer-note'>Available for freelance opportunities</p>",
        unsafe_allow_html=True
    )