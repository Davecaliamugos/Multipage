import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from components import render_navigation

st.set_page_config(
    page_title="Certifications | Dave Campo",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Render custom navbar and sidebar
render_navigation("certificates")

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

/* Generic content card (matches About page styling) */
.cert-card {
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

/* Certifications list */
.cert-list {
    list-style: none;
    padding-left: 0;
    margin: 0.3rem 0 1.2rem 0;
}

.cert-list li {
    position: relative;
    padding-left: 1.6rem;
    margin-bottom: 0.5rem;
    font-size: 0.92rem;
    color: var(--text-main);
}

.cert-list li::before {
    content: "✔";
    position: absolute;
    left: 0.1rem;
    top: -0.1rem;
    font-size: 0.95rem;
    background: linear-gradient(135deg, var(--primary), var(--accent));
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}

/* Section heading */
.section-heading {
    margin-top: 2.2rem;
    margin-bottom: 1.1rem;
    font-size: 1.1rem;
    text-transform: uppercase;
    letter-spacing: 0.18em;
    color: var(--text-muted);
}

/* Download button styling */
div.stDownloadButton > button:first-child {
    background: linear-gradient(135deg, var(--primary), var(--accent));
    color: #020617;
    border-radius: 999px;
    border: none;
    padding: 0.55rem 1.7rem;
    font-weight: 600;
    font-size: 0.9rem;
    box-shadow: 0 18px 40px rgba(0, 212, 255, 0.3);
    transition: all 0.22s ease;
}

div.stDownloadButton > button:first-child:hover {
    transform: translateY(-2px) scale(1.02);
    box-shadow: 0 24px 55px rgba(0, 212, 255, 0.5);
}

/* Carousel */
.carousel-card {
    margin-top: 0.4rem;
    padding: 0.9rem;
    border-radius: var(--radius-lg);
    background: var(--card-bg);
    border: 1px solid var(--border-subtle);
    box-shadow: var(--shadow-soft);
}

.carousel-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.6rem;
}

.carousel-title {
    font-size: 0.98rem;
    font-weight: 600;
    opacity: 0.9;
}

.carousel-counter {
    font-size: 0.85rem;
    opacity: 0.7;
}

.carousel-dots {
    text-align: center;
    margin-top: 0.4rem;
}

.carousel-dot {
    display: inline-block;
    width: 7px;
    height: 7px;
    margin: 0 3px;
    border-radius: 999px;
    background: rgba(148, 163, 184, 0.4);
}

.carousel-dot.active {
    width: 18px;
    background: linear-gradient(135deg, var(--primary), var(--accent));
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
certs = [
    "Python Programming Certificate",
    "Web Development Bootcamp",
    "UI/UX Design Fundamentals"
]

carousel_images = [
    "https://picsum.photos/seed/cert1/900/500",
    "https://picsum.photos/seed/cert2/900/500",
    "https://picsum.photos/seed/cert3/900/500",
    "https://picsum.photos/seed/cert4/900/500",
    "https://picsum.photos/seed/cert5/900/500",
]

if "cert_carousel_index" not in st.session_state:
    st.session_state.cert_carousel_index = 0

idx = st.session_state.cert_carousel_index
total = len(carousel_images)

# ---------- LAYOUT ----------
with st.container():
    # MAIN CERTIFICATIONS CARD
    st.markdown(
        """
        <div class="cert-card">
            <p class="page-subtitle">Verified skills & learning</p>
            <h1 class="page-title">📜 Certifications</h1>
            <p class="page-text">
                A snapshot of some of the formal learning and training I've completed along the way.
                These certifications back up my hands-on experience with solid foundations in
                software development and design.
            </p>
        """,
        unsafe_allow_html=True,
    )

    # Certifications list
    cert_list_html = "<ul class='cert-list'>"
    for cert in certs:
        cert_list_html += f"<li>{cert}</li>"
    cert_list_html += "</ul>"

    st.markdown(cert_list_html, unsafe_allow_html=True)

    # Download resume (inside the same card)
    st.markdown("**📄 Download Resume**", unsafe_allow_html=True)
    st.download_button(
        "Download Resume",
        data="Sample Resume Content",
        file_name="resume.txt",
        key="resume_download",
    )

    st.markdown("</div>", unsafe_allow_html=True)  # close cert-card

    # ---------- CAROUSEL SECTION ----------
    st.markdown('<h3 class="section-heading">📸 Certification Gallery</h3>', unsafe_allow_html=True)

    st.markdown('<div class="carousel-card">', unsafe_allow_html=True)

    # Header
    st.markdown(
        f"""
        <div class="carousel-header">
            <div class="carousel-title">Highlights from my certification journey</div>
            <div class="carousel-counter">{idx + 1} / {total}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    prev_col, img_col, next_col = st.columns([1, 6, 1])

    with prev_col:
        if st.button("◀", key="cert_prev"):
            st.session_state.cert_carousel_index = (idx - 1) % total
            idx = st.session_state.cert_carousel_index

    with img_col:
        st.image(
            carousel_images[idx],
            use_container_width=True,
            caption=f"Sample certification image {idx + 1}",
        )

    with next_col:
        if st.button("▶", key="cert_next"):
            st.session_state.cert_carousel_index = (idx + 1) % total
            idx = st.session_state.cert_carousel_index

    # Dots
    dots_html = ""
    for i in range(total):
        active_class = "active" if i == idx else ""
        dots_html += f'<span class="carousel-dot {active_class}"></span>'

    st.markdown(f'<div class="carousel-dots">{dots_html}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)  # close carousel-card