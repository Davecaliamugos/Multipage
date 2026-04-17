import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from components import render_navigation

st.set_page_config(
    page_title="Contact | Dave Campo",
    page_icon="📬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Render custom navbar and sidebar
render_navigation("contact")

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

/* Main contact card */
.contact-card {
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

/* Form labels */
.stTextInput > label,
.stTextArea > label {
    font-size: 0.86rem;
    color: var(--text-muted);
    margin-bottom: 0.25rem;
}

/* Inputs & textarea */
input[type="text"],
textarea {
    border-radius: 14px;
    border: 1px solid var(--border-subtle);
    background: rgba(15, 23, 42, 0.96);
    color: var(--text-main);
    font-size: 0.9rem;
    padding: 0.5rem 0.75rem;
}

textarea {
    min-height: 140px;
    resize: vertical;
}

input[type="text"]::placeholder,
textarea::placeholder {
    color: rgba(148, 163, 184, 0.7);
}

input[type="text"]:focus,
textarea:focus {
    outline: none !important;
    border-color: var(--primary);
    box-shadow: 0 0 0 1px rgba(56, 189, 248, 0.6);
}

/* Submit button */
div.stFormSubmitButton > button:first-child {
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

div.stFormSubmitButton > button:first-child:hover {
    transform: translateY(-2px) scale(1.02);
    box-shadow: 0 24px 55px rgba(0, 212, 255, 0.5);
}

/* Social block */
.social-text {
    font-size: 0.9rem;
    color: var(--text-muted);
    margin-bottom: 0.8rem;
}

.social-list {
    list-style: none;
    padding-left: 0;
    margin: 0;
}

.social-list li {
    margin-bottom: 0.4rem;
    font-size: 0.9rem;
}

.social-list a {
    color: var(--primary);
    text-decoration: none;
}

.social-list a:hover {
    text-decoration: underline;
}

/* Responsive */
@media (max-width: 768px) {
    .page-title {
        font-size: 1.9rem;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------- LAYOUT ----------
with st.container():
    st.markdown(
        """
        <div class="contact-card">
            <p class="page-subtitle">Let's talk</p>
            <h1 class="page-title">📬 Contact Me</h1>
            <p class="page-text">
                Have an idea, a project, or just want to say hi? Drop me a message and I'll get
                back to you as soon as I can.
            </p>
        """,
        unsafe_allow_html=True,
    )

    col_form, col_side = st.columns([2, 1])

    # CONTACT FORM
    with col_form:
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message")

            submitted = st.form_submit_button("Send Message")

            if submitted:
                if name and email and message:
                    st.success("Message sent successfully! 🚀")
                else:
                    st.error("Please fill all fields!")

    # SOCIAL / QUICK CONTACT
    with col_side:
        st.markdown('<div class="section-heading">Connect</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <p class="social-text">
                Prefer to connect directly? You can also reach me on:
            </p>
            <ul class="social-list">
                <li><strong>GitHub</strong><br>
                    <a href="https://github.com/yourusername" target="_blank">
                        github.com/yourusername
                    </a>
                </li>
                <li><strong>LinkedIn</strong><br>
                    <a href="https://linkedin.com/in/yourprofile" target="_blank">
                        linkedin.com/in/yourprofile
                    </a>
                </li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)  # close contact-card