import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from components import render_navigation

st.set_page_config(
    page_title="Skills | Dave Campo",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Render custom navbar and sidebar
render_navigation("skills")

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

/* Main skills card */
.skills-card {
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

/* Skills list */
.skill-list {
    display: flex;
    flex-direction: column;
    gap: 0.85rem;
    margin-top: 0.4rem;
}

.skill-row {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
}

.skill-label {
    display: flex;
    justify-content: space-between;
    font-size: 0.9rem;
    color: var(--text-main);
}

.skill-label span.skill-name {
    font-weight: 500;
}

.skill-label span.skill-value {
    font-size: 0.86rem;
    color: var(--text-muted);
}

/* Custom progress bar */
.skill-bar-outer {
    position: relative;
    width: 100%;
    height: 9px;
    border-radius: 999px;
    background: rgba(15, 23, 42, 0.98);
    border: 1px solid rgba(148, 163, 184, 0.45);
    overflow: hidden;
}

.skill-bar-inner {
    height: 100%;
    border-radius: inherit;
    background: linear-gradient(135deg, var(--primary), var(--accent));
    box-shadow: 0 0 18px rgba(0, 212, 255, 0.45);
}

/* Section heading inside the card */
.section-heading {
    margin-top: 1.8rem;
    margin-bottom: 0.7rem;
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 0.18em;
    color: var(--text-muted);
}

/* Radio styling */
.stRadio > label {
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
skills = {
    "Frontend": 80,
    "Backend": 75,
    "Python": 85,
    "UI/UX Design": 70
}

# ---------- LAYOUT ----------
with st.container():
    st.markdown(
        """
        <div class="skills-card">
            <p class="page-subtitle">What I work with</p>
            <h1 class="page-title">🧠 Skills</h1>
            <p class="page-text">
                A blend of frontend, backend, and design skills that let me take ideas from prototype
                to production, with a strong focus on Python and modern web technologies.
            </p>
        """,
        unsafe_allow_html=True,
    )

    # Skills section (custom bars)
    skill_html = '<div class="skill-list">'
    for skill, level in skills.items():
        skill_html += f"""
        <div class="skill-row">
            <div class="skill-label">
                <span class="skill-name">{skill}</span>
                <span class="skill-value">{level}%</span>
            </div>
            <div class="skill-bar-outer">
                <div class="skill-bar-inner" style="width: {level}%;"></div>
            </div>
        </div>
        """
    skill_html += "</div>"

    st.markdown(skill_html, unsafe_allow_html=True)

    # Interactive filter
    st.markdown('<div class="section-heading">Skill interest</div>', unsafe_allow_html=True)
    choice = st.radio(
        "Which area interests you most?",
        ["Frontend", "Backend", "AI"],
        index=0,
    )

    st.info(f"You selected: {choice}")

    st.markdown("</div>", unsafe_allow_html=True)  # close skills-card