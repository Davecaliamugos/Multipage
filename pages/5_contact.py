import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import streamlit.components.v1 as components
from components import apply_global_effects

st.set_page_config(
    page_title="Contact | Dave Campo",
    page_icon="📬",
    layout="wide"
)

apply_global_effects()

# ═══════════════════════════════════════════════════════
#                    SIDEBAR
# ═══════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div style="text-align:center;margin-bottom:1rem;">
        <h2 style="color:#00d4ff;font-size:1.5rem;font-weight:800;margin:0;">Dave.dev</h2>
        <p style="color:#9ca3af;font-size:0.8rem;margin:0.3rem 0 0;">Portfolio</p>
    </div>
    """, unsafe_allow_html=True)
    st.divider()

# ---------- PAGE-LEVEL STYLES ----------
st.markdown("""
<style>
:root {
    --primary: #00d4ff;
    --accent: #ff6bcb;
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
    max-width: 1200px;
    padding-top: 1.5rem !important;
    padding-bottom: 2rem !important;
}

/* ── Inputs ── */
.stTextInput > label,
.stTextArea > label,
.stSelectbox > label {
    color: #9ca3af !important;
    font-size: 0.86rem !important;
}

div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
    background: rgba(15, 23, 42, 0.98) !important;
    border: 1px solid rgba(148, 163, 184, 0.35) !important;
    border-radius: 12px !important;
    color: #e5e7eb !important;
    font-size: 0.92rem !important;
}

div[data-baseweb="input"] input:focus,
div[data-baseweb="textarea"] textarea:focus {
    border-color: #00d4ff !important;
    box-shadow: 0 0 0 2px rgba(0, 212, 255, 0.2) !important;
}

/* ── Submit button ── */
div.stFormSubmitButton > button:first-child {
    background: linear-gradient(135deg, #00d4ff, #ff6bcb) !important;
    color: #020617 !important;
    border-radius: 999px !important;
    border: none !important;
    padding: 0.6rem 2rem !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    box-shadow: 0 18px 40px rgba(0, 212, 255, 0.3) !important;
    transition: all 0.22s ease !important;
    width: 100% !important;
}

div.stFormSubmitButton > button:first-child:hover {
    transform: translateY(-2px) scale(1.02) !important;
    box-shadow: 0 24px 55px rgba(0, 212, 255, 0.5) !important;
}

/* ── Selectbox ── */
div[data-baseweb="select"] > div {
    background: rgba(15, 23, 42, 0.98) !important;
    border: 1px solid rgba(148, 163, 184, 0.35) !important;
    border-radius: 12px !important;
    color: #e5e7eb !important;
}

/* ── Slider ── */
div[data-testid="stSlider"] label {
    color: #9ca3af !important;
    font-size: 0.86rem !important;
}

/* ── Radio ── */
div[data-testid="stRadio"] label {
    color: #e5e7eb !important;
}

/* ── Success / Error ── */
div[data-testid="stAlert"] {
    border-radius: 12px !important;
}

/* ── Metric cards ── */
div[data-testid="stMetric"] {
    background: rgba(15, 23, 42, 0.96);
    border: 1px solid rgba(148, 163, 184, 0.35);
    border-radius: 14px;
    padding: 1rem 1.2rem;
}

div[data-testid="stMetric"] label {
    color: #9ca3af !important;
    font-size: 0.8rem !important;
}

div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
    color: #00d4ff !important;
    font-size: 1.4rem !important;
    font-weight: 700 !important;
}

@media (max-width: 768px) {
    .block-container {
        padding-top: 1rem !important;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER CARD (components.html — bypass sanitizer) ----------
components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
  * { margin:0; padding:0; box-sizing:border-box; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background: transparent;
    padding: 0.2rem 0;
  }
  .contact-card {
    background: rgba(15,23,42,0.96);
    border-radius: 18px;
    border: 1px solid rgba(148,163,184,0.35);
    padding: 2rem 2rem 1.6rem;
    box-shadow: 0 24px 60px rgba(0,0,0,0.85);
    backdrop-filter: blur(18px);
  }
  .page-subtitle {
    font-size: 0.82rem;
    text-transform: uppercase;
    letter-spacing: 0.22em;
    color: #00d4ff;
    margin-bottom: 0.8rem;
  }
  .page-title {
    font-size: 2.6rem;
    font-weight: 800;
    color: #e5e7eb;
    margin-bottom: 0.6rem;
  }
  .page-text {
    font-size: 1rem;
    color: #9ca3af;
    line-height: 1.65;
    margin-bottom: 0;
  }

  /* ── Status badges ── */
  .status-row {
    display: flex;
    gap: 0.75rem;
    flex-wrap: wrap;
    margin-top: 1.2rem;
  }
  .badge {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.35rem 0.9rem;
    border-radius: 999px;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.04em;
  }
  .badge-green {
    background: rgba(16,185,129,0.15);
    border: 1px solid rgba(16,185,129,0.4);
    color: #34d399;
  }
  .badge-blue {
    background: rgba(0,212,255,0.12);
    border: 1px solid rgba(0,212,255,0.35);
    color: #00d4ff;
  }
  .badge-pink {
    background: rgba(255,107,203,0.12);
    border: 1px solid rgba(255,107,203,0.35);
    color: #ff6bcb;
  }
  .dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    background: currentColor;
    animation: pulse 1.8s infinite;
  }
  @keyframes pulse {
    0%,100% { opacity:1; transform:scale(1); }
    50%      { opacity:0.5; transform:scale(1.35); }
  }

  /* ── Info pills ── */
  .info-row {
    display: flex;
    gap: 1.2rem;
    flex-wrap: wrap;
    margin-top: 1.1rem;
    padding-top: 1.1rem;
    border-top: 1px solid rgba(148,163,184,0.2);
  }
  .info-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.85rem;
    color: #9ca3af;
  }
  .info-icon { font-size: 1rem; }
  .info-label { color: #e5e7eb; font-weight: 500; }
</style>
</head>
<body>
<div class="contact-card">
  <p class="page-subtitle">Let's talk</p>
  <h1 class="page-title">📬 Contact Me</h1>
  <p class="page-text">
    Have an idea, a project, or just want to say hi? Drop me a message
    and I'll get back to you as soon as I can.
  </p>

  <!-- Live status badges -->
  <div class="status-row">
    <span class="badge badge-green"><span class="dot"></span>Available for Work</span>
    <span class="badge badge-blue">⚡ Usually replies in &lt;24h</span>
  </div>

</div>
</body>
</html>
""", height=280, scrolling=False)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- METRICS ROW ----------
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric("⏱ Response Time", "< 24 hrs")
with m2:
    st.metric("✅ Projects Done", "20+")
with m3:
    st.metric("🌐 Timezone", "UTC +8")
with m4:
    st.metric("📅 Availability", "Immediate")

st.markdown("<br>", unsafe_allow_html=True)

# ---------- MAIN COLUMNS ----------
col_form, col_side = st.columns([3, 2], gap="large")

# ── LEFT: CONTACT FORM ──────────────────────────────────────────────
with col_form:
    st.markdown("##### 📝 Send a Message")

    with st.form("contact_form", clear_on_submit=True):

        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Your Name", placeholder="Dave Campo")
        with c2:
            email = st.text_input("Your Email", placeholder="dave@example.com")

        subject_options = [
            "💼 Job Opportunity",
            "🤝 Collaboration",
            "🐛 Bug Report",
            "💡 Project Idea",
            "👋 Just Saying Hi",
            "Other",
        ]
        subject = st.selectbox("Subject", subject_options)

        priority = st.select_slider(
            "Message Priority",
            options=["🟢 Low", "🔵 Normal", "🟡 High", "🔴 Urgent"],
            value="🔵 Normal",
        )

        message = st.text_area(
            "Your Message",
            placeholder="Tell me about your project, idea, or question...",
            height=160,
        )

        agree = st.checkbox("I agree to be contacted via email regarding this message.")

        submitted = st.form_submit_button("🚀 Send Message", use_container_width=True)

        if submitted:
            if not name or not email or not message:
                st.error("⚠️ Please fill in all required fields.")
            elif not agree:
                st.warning("☑️ Please agree to be contacted before sending.")
            elif "@" not in email:
                st.error("📧 Please enter a valid email address.")
            else:
                st.success(f"✅ Thanks **{name}**! Your message has been sent. I'll reply soon!")
                st.balloons()

    # ── LOCATION / MAP ────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("##### 📍 My Location")

    components.html("""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      * { margin:0; padding:0; box-sizing:border-box; }
      body { font-family: -apple-system, sans-serif; background:transparent; }
      .map-card {
        background: rgba(15,23,42,0.96);
        border: 1px solid rgba(148,163,184,0.35);
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(0,0,0,0.6);
      }
      .map-frame {
        width: 100%;
        height: 220px;
        border: none;
        display: block;
      }
      .map-footer {
        padding: 0.85rem 1.2rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 0.5rem;
      }
      .map-location {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        color: #e5e7eb;
        font-size: 0.9rem;
        font-weight: 600;
      }
      .map-sub {
        font-size: 0.78rem;
        color: #9ca3af;
        margin-top: 0.1rem;
      }
      .map-badge {
        background: rgba(0,212,255,0.12);
        border: 1px solid rgba(0,212,255,0.35);
        color: #00d4ff;
        border-radius: 999px;
        padding: 0.25rem 0.8rem;
        font-size: 0.75rem;
        font-weight: 600;
      }
    </style>
    </head>
    <body>
    <div class="map-card">
      <iframe
        class="map-frame"
        src="https://www.openstreetmap.org/export/embed.html?bbox=123.2300,12.1600,123.3300,12.2600&layer=mapnik&marker=12.2155,123.2847"
        allowfullscreen>
      </iframe>
      <div class="map-footer">
        <div>
          <div class="map-location">📍 Cabitan, Mandaon</div>
          <div class="map-sub">Debesmscat · Cabitan</div>
        </div>
        <span class="map-badge">UTC +8 · PHT</span>
      </div>
    </div>
    </body>
    </html>
    """, height=310, scrolling=False)

# ── RIGHT: SIDEBAR INFO ──────────────────────────────────────────────
with col_side:

    # Social Links Card
    components.html("""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      * { margin:0; padding:0; box-sizing:border-box; }
      body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        background: transparent;
      }
      .side-card {
        background: rgba(15,23,42,0.96);
        border: 1px solid rgba(148,163,184,0.35);
        border-radius: 16px;
        padding: 1.4rem 1.4rem 1.2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.6);
        margin-bottom: 1rem;
      }
      .side-heading {
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: 0.2em;
        color: #9ca3af;
        margin-bottom: 1rem;
      }
      .social-item {
        display: flex;
        align-items: center;
        gap: 0.85rem;
        padding: 0.75rem 0.9rem;
        border-radius: 12px;
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(148,163,184,0.15);
        margin-bottom: 0.6rem;
        text-decoration: none;
        transition: all 0.2s ease;
      }
      .social-item:hover {
        background: rgba(0,212,255,0.08);
        border-color: rgba(0,212,255,0.3);
        transform: translateX(4px);
      }
      .social-icon {
        font-size: 1.3rem;
        width: 36px;
        height: 36px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 10px;
        background: rgba(0,212,255,0.1);
        flex-shrink: 0;
      }
      .social-info { flex: 1; }
      .social-name {
        font-size: 0.88rem;
        font-weight: 600;
        color: #e5e7eb;
      }
      .social-handle {
        font-size: 0.75rem;
        color: #9ca3af;
        margin-top: 0.1rem;
      }
      .social-arrow {
        color: #00d4ff;
        font-size: 0.9rem;
      }

      /* Availability card */
      .avail-card {
        background: rgba(16,185,129,0.08);
        border: 1px solid rgba(16,185,129,0.3);
        border-radius: 16px;
        padding: 1.2rem 1.4rem;
        margin-bottom: 1rem;
      }
      .avail-header {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 0.6rem;
      }
      .avail-dot {
        width: 9px; height: 9px;
        border-radius: 50%;
        background: #34d399;
        animation: pulse 1.8s infinite;
      }
      @keyframes pulse {
        0%,100% { opacity:1; transform:scale(1); }
        50%      { opacity:0.5; transform:scale(1.4); }
      }
      .avail-title {
        font-size: 0.88rem;
        font-weight: 700;
        color: #34d399;
      }
      .avail-text {
        font-size: 0.8rem;
        color: #9ca3af;
        line-height: 1.5;
      }

      /* Working hours */
      .hours-card {
        background: rgba(15,23,42,0.96);
        border: 1px solid rgba(148,163,184,0.35);
        border-radius: 16px;
        padding: 1.2rem 1.4rem;
      }
      .hours-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.35rem 0;
        border-bottom: 1px solid rgba(148,163,184,0.1);
        font-size: 0.82rem;
      }
      .hours-row:last-child { border-bottom: none; }
      .hours-day { color: #9ca3af; }
      .hours-time { color: #e5e7eb; font-weight: 500; }
      .hours-closed { color: #6b7280; }
      .hours-title {
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: 0.18em;
        color: #9ca3af;
        margin-bottom: 0.8rem;
      }
    </style>
    </head>
    <body>

    <!-- Availability -->
    <div class="avail-card">
      <div class="avail-header">
        <div class="avail-dot"></div>
        <span class="avail-title">Available for New Projects</span>
      </div>
      <p class="avail-text">
        Currently accepting freelance work and full-time opportunities.
        I typically respond within 24 hours.
      </p>
    </div>

    <!-- Social Links -->
    <div class="side-card">
      <p class="side-heading">Connect with me</p>

      <a class="social-item" href="https://github.com/yourusername" target="_blank">
        <div class="social-icon">🐙</div>
        <div class="social-info">
          <div class="social-name">GitHub</div>
          <div class="social-handle">github.com/yourusername</div>
        </div>
        <span class="social-arrow">→</span>
      </a>

      <a class="social-item" href="https://linkedin.com/in/yourprofile" target="_blank">
        <div class="social-icon">💼</div>
        <div class="social-info">
          <div class="social-name">LinkedIn</div>
          <div class="social-handle">linkedin.com/in/yourprofile</div>
        </div>
        <span class="social-arrow">→</span>
      </a>

      <a class="social-item" href="https://twitter.com/yourhandle" target="_blank">
        <div class="social-icon">🐦</div>
        <div class="social-info">
          <div class="social-name">Twitter / X</div>
          <div class="social-handle">@yourhandle</div>
        </div>
        <span class="social-arrow">→</span>
      </a>

      <a class="social-item" href="mailto:dave@example.com">
        <div class="social-icon">📧</div>
        <div class="social-info">
          <div class="social-name">Email</div>
          <div class="social-handle">dave@example.com</div>
        </div>
        <span class="social-arrow">→</span>
      </a>
    </div>

    <!-- Working Hours -->
    <div class="hours-card">
      <p class="hours-title">🕐 Working Hours (PHT)</p>
      <div class="hours-row">
        <span class="hours-day">Monday – Friday</span>
        <span class="hours-time">9:00 AM – 6:00 PM</span>
      </div>
      <div class="hours-row">
        <span class="hours-day">Saturday</span>
        <span class="hours-time">10:00 AM – 2:00 PM</span>
      </div>
      <div class="hours-row">
        <span class="hours-day">Sunday</span>
        <span class="hours-closed">Unavailable</span>
      </div>
    </div>

    </body>
    </html>
    """, height=680, scrolling=False)

    # ═══════════════════════════════════════════════════════
#                      FOOTER
# ═══════════════════════════════════════════════════════
st.markdown("---")

components.html("""
<div style="
    font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
    display:flex;justify-content:space-between;align-items:center;
    flex-wrap:wrap;gap:0.5rem;padding:0.4rem 0;
">
  <div style="color:#6b7280;font-size:0.82rem;">
    © 2025 <strong style="color:#9ca3af;">Dave Campo</strong>
    · Built with Python &amp; Streamlit
  </div>
</div>
""", height=50)