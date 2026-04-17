import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from components import render_navigation

st.set_page_config(
    page_title="About | Dave Campo",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Render custom navbar and sidebar
render_navigation("about")

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

/* About card */
.about-card {
    background: var(--card-bg);
    border-radius: var(--radius-lg);
    border: 1px solid var(--border-subtle);
    padding: 1.8rem 1.6rem 1.6rem 1.6rem;
    box-shadow: var(--shadow-soft);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
}

.about-title {
    font-size: 2.2rem;
    font-weight: 800;
    margin: 0 0 0.4rem 0;
}

.about-subtitle {
    font-size: 0.92rem;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    color: var(--primary);
    margin-bottom: 1.2rem;
}

.about-text {
    font-size: 0.96rem;
    color: var(--text-muted);
    line-height: 1.6;
    margin-bottom: 1.4rem;
}

/* Goals list */
.goals-title {
    font-size: 0.95rem;
    margin-bottom: 0.4rem;
}

.goals-list {
    list-style: none;
    padding-left: 0;
    margin: 0;
}

.goals-list li {
    position: relative;
    padding-left: 1.4rem;
    margin-bottom: 0.35rem;
    font-size: 0.9rem;
    color: var(--text-main);
}

.goals-list li::before {
    content: "•";
    position: absolute;
    left: 0.25rem;
    top: -0.05rem;
    font-size: 1.1rem;
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

/* Timeline */
.timeline {
    position: relative;
    margin-left: 0.4rem;
    padding-left: 1.6rem;
}

.timeline::before {
    content: "";
    position: absolute;
    left: 0.45rem;
    top: 0.15rem;
    bottom: 0.15rem;
    width: 2px;
    background: linear-gradient(to bottom, var(--primary), rgba(148, 163, 184, 0.4));
}

.timeline-item {
    position: relative;
    margin-bottom: 1.2rem;
    padding-left: 0.4rem;
}

.timeline-dot {
    position: absolute;
    left: -1.08rem;
    top: 0.1rem;
    width: 10px;
    height: 10px;
    border-radius: 999px;
    background: radial-gradient(circle at center, var(--primary), #0ea5e9);
    box-shadow: 0 0 0 4px rgba(56, 189, 248, 0.18);
}

.timeline-year {
    font-size: 0.85rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--primary);
    margin-bottom: 0.08rem;
}

.timeline-text {
    font-size: 0.94rem;
    color: var(--text-main);
}

/* Responsive */
@media (max-width: 768px) {
    .about-title {
        font-size: 1.9rem;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------- LAYOUT ----------
with st.container():
    # ABOUT CARD
    st.markdown(
        """
        <div class="about-card">
            <p class="about-subtitle">A little bit about me</p>
            <h1 class="about-title">👤 About Me</h1>
            <p class="about-text">
                I am a passionate developer who loves creating systems that solve real-world problems.
                I enjoy working across the stack, from designing clean APIs to crafting smooth user
                experiences, and I'm especially interested in how AI can automate and augment meaningful work.
            </p>
            <h3 class="goals-title">🎯 My Goals</h3>
            <ul class="goals-list">
                <li>Build scalable, resilient applications</li>
                <li>Deepen my understanding of advanced AI systems</li>
                <li>Create digital products that have real impact</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # TIMELINE
    st.markdown('<h3 class="section-heading">📅 My Journey</h3>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-year">2023</div>
                <div class="timeline-text">Started coding</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-year">2024</div>
                <div class="timeline-text">Built my first web projects</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-year">2025</div>
                <div class="timeline-text">Leveled up into full‑stack development</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-year">2026</div>
                <div class="timeline-text">Exploring AI, automation, and systems design</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )