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

# ═══════════════════════════════════════════════════════
#   PAGE STYLES
# ═══════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background: radial-gradient(circle at 0% 0%, #1f2937 0, #020617 40%, #000 100%) !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}
.block-container {
    max-width: 1100px !important;
    padding-top: 1.5rem !important;
    padding-bottom: 3rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
}
iframe { display: block; border: none !important; }
.stApp, .stApp * { color: #e5e7eb; }

.stTextInput > label,
.stTextArea > label,
.stSelectbox > label {
    color: #9ca3af !important;
    font-size: 0.86rem !important;
    font-weight: 500 !important;
}
div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
    background: rgba(15,23,42,0.98) !important;
    border: 1px solid rgba(148,163,184,0.35) !important;
    border-radius: 12px !important;
    color: #e5e7eb !important;
    font-size: 0.92rem !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
}
div[data-baseweb="input"] input:focus,
div[data-baseweb="textarea"] textarea:focus {
    border-color: #00d4ff !important;
    box-shadow: 0 0 0 3px rgba(0,212,255,0.18) !important;
}
div[data-baseweb="select"] > div {
    background: rgba(15,23,42,0.98) !important;
    border: 1px solid rgba(148,163,184,0.35) !important;
    border-radius: 12px !important;
    color: #e5e7eb !important;
}
div.stFormSubmitButton > button:first-child {
    background: linear-gradient(135deg, #00d4ff, #ff6bcb) !important;
    color: #020617 !important;
    border-radius: 999px !important;
    border: none !important;
    padding: 0.65rem 2rem !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    box-shadow: 0 12px 35px rgba(0,212,255,0.28) !important;
    transition: all 0.22s ease !important;
    width: 100% !important;
}
div.stFormSubmitButton > button:first-child:hover {
    transform: translateY(-2px) scale(1.02) !important;
    box-shadow: 0 20px 50px rgba(0,212,255,0.45) !important;
}
div[data-testid="stMetric"] {
    background: rgba(15,23,42,0.96);
    border: 1px solid rgba(148,163,184,0.25);
    border-radius: 14px;
    padding: 1rem 1.2rem;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
div[data-testid="stMetric"]:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.5);
}
div[data-testid="stMetric"] label {
    color: #9ca3af !important;
    font-size: 0.78rem !important;
}
div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
    color: #00d4ff !important;
    font-size: 1.3rem !important;
    font-weight: 700 !important;
}
div[data-testid="stAlert"] { border-radius: 12px !important; }
div[data-testid="stCheckbox"] label p { color: #9ca3af !important; font-size: 0.85rem !important; }

@media (max-width: 768px) {
    .block-container {
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
        padding-top: 1rem !important;
    }
}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
#   FULL HEADER + SIDE INFO — single HTML block
# ═══════════════════════════════════════════════════════
components.html("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: transparent;
    color: #e5e7eb;
    -webkit-font-smoothing: antialiased;
  }

  /* ── Animations ── */
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(24px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  @keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
  }
  @keyframes pulse {
    0%,100% { opacity:1; transform:scale(1); }
    50%      { opacity:0.5; transform:scale(1.4); }
  }
  @keyframes glowPulse {
    0%,100% { box-shadow: 0 0 25px rgba(0,212,255,0.12); }
    50%      { box-shadow: 0 0 45px rgba(0,212,255,0.3); }
  }
  @keyframes shimmer {
    0%   { background-position: -200% center; }
    100% { background-position:  200% center; }
  }
  @keyframes slideRight {
    from { transform: translateX(-8px); opacity: 0; }
    to   { transform: translateX(0);    opacity: 1; }
  }

  /* ── Hero Card ── */
  .hero {
    background: rgba(15,23,42,0.97);
    border-radius: 20px;
    border: 1px solid rgba(148,163,184,0.3);
    padding: 2.2rem 2.4rem 2rem;
    margin-bottom: 1rem;
    animation: fadeUp 0.6s ease both, glowPulse 4s ease-in-out infinite;
    position: relative;
    overflow: hidden;
  }
  .hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg,
      rgba(0,212,255,0.04) 0%,
      transparent 50%,
      rgba(255,107,203,0.04) 100%);
    pointer-events: none;
  }
  .eyebrow {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.22em;
    color: #00d4ff;
    margin-bottom: 0.75rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    animation: fadeIn 0.5s 0.2s ease both;
  }
  .eyebrow-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #00d4ff;
    animation: pulse 2s ease-in-out infinite;
  }
  .hero-title {
    font-size: clamp(1.9rem, 5vw, 2.7rem);
    font-weight: 800;
    color: #e5e7eb;
    line-height: 1.15;
    margin-bottom: 0.7rem;
    display: flex;
    align-items: center;
    gap: 0.6rem;
    animation: fadeUp 0.5s 0.15s ease both;
  }
  .hero-desc {
    font-size: clamp(0.88rem, 2vw, 1rem);
    color: #9ca3af;
    line-height: 1.7;
    max-width: 560px;
    animation: fadeUp 0.5s 0.25s ease both;
  }
  .status-row {
    display: flex;
    gap: 0.7rem;
    flex-wrap: wrap;
    margin-top: 1.3rem;
    animation: fadeUp 0.5s 0.35s ease both;
  }
  .badge {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.35rem 0.9rem;
    border-radius: 999px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.03em;
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
  .dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    background: currentColor;
    animation: pulse 1.8s infinite;
  }

  /* ── Responsive ── */
  @media (max-width: 640px) {
    .hero { padding: 1.4rem 1.2rem 1.4rem; }
    .status-row { gap: 0.5rem; }
    .badge { font-size: 0.72rem; padding: 0.28rem 0.7rem; }
  }
</style>
</head>
<body>

<div class="hero">
  <div class="eyebrow">
    <div class="eyebrow-dot"></div>
    Let's talk
  </div>

  <h1 class="hero-title">
    <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36"
         viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2"
         stroke-linecap="round" stroke-linejoin="round">
      <path d="M22 16.92v3a2 2 0 0 1-2.18 2
               19.79 19.79 0 0 1-8.63-3.07
               19.5 19.5 0 0 1-6-6
               19.79 19.79 0 0 1-3.07-8.67
               A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72
               12.84 12.84 0 0 0 .7 2.81
               2 2 0 0 1-.45 2.11L8.09 9.91
               a16 16 0 0 0 6 6l1.27-1.27
               a2 2 0 0 1 2.11-.45
               12.84 12.84 0 0 0 2.81.7
               A2 2 0 0 1 22 16.92z"/>
    </svg>
    Contact Me
  </h1>

  <p class="hero-desc">
    Have an idea, a project, or just want to say hi? Drop me a message
    and I'll get back to you as soon as I can.
  </p>

  <div class="status-row">
    <span class="badge badge-green">
      <span class="dot"></span>
      Available for Work
    </span>
    <span class="badge badge-blue">
      <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12"
           viewBox="0 0 24 24" fill="none" stroke="currentColor"
           stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
      </svg>
      Usually replies in &lt;24h
    </span>
  </div>
</div>

</body>
</html>
""", height=255, scrolling=False)

# ═══════════════════════════════════════════════════════
#   METRICS ROW
# ═══════════════════════════════════════════════════════
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric("Response Time", "< 24 hrs")
with m2:
    st.metric("Projects Done", "20+")
with m3:
    st.metric("Timezone", "UTC +8")
with m4:
    st.metric("Availability", "Immediate")

st.markdown("<br>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
#   MAIN LAYOUT — Form (left) + Info (right)
# ═══════════════════════════════════════════════════════
col_form, col_side = st.columns([3, 2], gap="large")

# ── LEFT: CONTACT FORM ─────────────────────────────────
with col_form:

    # Form header
    components.html("""
    <div style="
        font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
        display:flex; align-items:center; gap:0.6rem;
        margin-bottom:0.5rem;
        animation: fadeUp 0.5s 0.1s ease both;
    ">
      <svg xmlns='http://www.w3.org/2000/svg' width='20' height='20'
           viewBox='0 0 24 24' fill='none' stroke='#00d4ff' stroke-width='2'
           stroke-linecap='round' stroke-linejoin='round'>
        <path d='M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14
                 a2 2 0 0 1 2 2z'/>
      </svg>
      <span style="font-size:1.05rem;font-weight:700;color:#e5e7eb;">Send a Message</span>
    </div>
    <style>
      @keyframes fadeUp {
        from { opacity:0; transform:translateY(16px); }
        to   { opacity:1; transform:translateY(0); }
      }
    </style>
    """, height=42)

    with st.form("contact_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            name  = st.text_input("Your Name",  placeholder="Dave Campo")
        with c2:
            email = st.text_input("Your Email", placeholder="dave@example.com")

        subject_options = [
            "Job Opportunity",
            "Collaboration",
            "Bug Report",
            "Project Idea",
            "Just Saying Hi",
            "Other",
        ]
        subject = st.selectbox("Subject", subject_options)

        priority = st.select_slider(
            "Message Priority",
            options=["Low", "Normal", "High", "Urgent"],
            value="Normal",
        )

        message = st.text_area(
            "Your Message",
            placeholder="Tell me about your project, idea, or question...",
            height=160,
        )

        agree = st.checkbox(
            "I agree to be contacted via email regarding this message."
        )

        submitted = st.form_submit_button(
            "Send Message", use_container_width=True
        )

        if submitted:
            if not name or not email or not message:
                st.error("Please fill in all required fields.")
            elif not agree:
                st.warning("Please agree to be contacted before sending.")
            elif "@" not in email:
                st.error("Please enter a valid email address.")
            else:
                st.success(
                    f"Thanks **{name}**! Your message has been sent. "
                    "I'll reply soon!"
                )
                st.balloons()

    # ── MAP ──────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)

    components.html("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <style>
      *, *::before, *::after { box-sizing:border-box; margin:0; padding:0; }
      body {
        font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
        background:transparent;
      }
      @keyframes fadeUp {
        from { opacity:0; transform:translateY(20px); }
        to   { opacity:1; transform:translateY(0); }
      }
      .section-heading {
        display:flex; align-items:center; gap:0.55rem;
        font-size:1.02rem; font-weight:700; color:#e5e7eb;
        margin-bottom:0.7rem;
        animation: fadeUp 0.5s ease both;
      }
      .map-card {
        background:rgba(15,23,42,0.96);
        border:1px solid rgba(148,163,184,0.3);
        border-radius:16px;
        overflow:hidden;
        box-shadow:0 8px 32px rgba(0,0,0,0.6);
        animation: fadeUp 0.55s 0.1s ease both;
        transition: transform 0.25s ease, box-shadow 0.25s ease;
      }
      .map-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 18px 45px rgba(0,0,0,0.7);
      }
      .map-frame {
        width:100%; height:210px;
        border:none; display:block;
      }
      .map-footer {
        padding:0.9rem 1.2rem;
        display:flex; align-items:center;
        justify-content:space-between; flex-wrap:wrap; gap:0.5rem;
        border-top:1px solid rgba(148,163,184,0.15);
      }
      .map-loc {
        display:flex; align-items:center; gap:0.5rem;
      }
      .map-loc svg { flex-shrink:0; }
      .map-loc-text { color:#e5e7eb; font-size:0.9rem; font-weight:600; }
      .map-sub { font-size:0.75rem; color:#9ca3af; margin-top:0.1rem; }
      .map-badge {
        background:rgba(0,212,255,0.1);
        border:1px solid rgba(0,212,255,0.3);
        color:#00d4ff;
        border-radius:999px;
        padding:0.25rem 0.8rem;
        font-size:0.72rem; font-weight:600;
        display:flex; align-items:center; gap:0.35rem;
      }
    </style>
    </head>
    <body>

    <div class="section-heading">
      <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18"
           viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2"
           stroke-linecap="round" stroke-linejoin="round">
        <path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/>
        <circle cx="12" cy="10" r="3"/>
      </svg>
      My Location
    </div>

    <div class="map-card">
      <iframe class="map-frame"
        src="https://www.openstreetmap.org/export/embed.html?bbox=123.2300,12.1600,123.3300,12.2600&layer=mapnik&marker=12.2155,123.2847"
        allowfullscreen loading="lazy">
      </iframe>
      <div class="map-footer">
        <div class="map-loc">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
               viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2"
               stroke-linecap="round" stroke-linejoin="round">
            <path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/>
            <circle cx="12" cy="10" r="3"/>
          </svg>
          <div>
            <div class="map-loc-text">Cabitan, Mandaon</div>
            <div class="map-sub">Masbate · Philippines</div>
          </div>
        </div>
        <span class="map-badge">
          <svg xmlns="http://www.w3.org/2000/svg" width="11" height="11"
               viewBox="0 0 24 24" fill="none" stroke="currentColor"
               stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"/>
            <polyline points="12 6 12 12 16 14"/>
          </svg>
          UTC +8 · PHT
        </span>
      </div>
    </div>
    </body>
    </html>
    """, height=320, scrolling=False)

# ── RIGHT: INFO CARDS ───────────────────────────────────
with col_side:
    components.html("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <style>
      *, *::before, *::after { box-sizing:border-box; margin:0; padding:0; }
      body {
        font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
        background:transparent;
        color:#e5e7eb;
        -webkit-font-smoothing:antialiased;
      }

      /* ── Animations ── */
      @keyframes fadeUp {
        from { opacity:0; transform:translateY(22px); }
        to   { opacity:1; transform:translateY(0); }
      }
      @keyframes pulse {
        0%,100% { opacity:1; transform:scale(1); }
        50%      { opacity:0.45; transform:scale(1.45); }
      }
      @keyframes slideRight {
        from { opacity:0; transform:translateX(-10px); }
        to   { opacity:1; transform:translateX(0); }
      }

      /* ── Availability ── */
      .avail-card {
        background:rgba(16,185,129,0.08);
        border:1px solid rgba(16,185,129,0.3);
        border-radius:16px;
        padding:1.2rem 1.4rem;
        margin-bottom:0.9rem;
        animation: fadeUp 0.5s 0.05s ease both;
        transition: transform 0.22s ease, box-shadow 0.22s ease;
      }
      .avail-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 14px 35px rgba(16,185,129,0.15);
      }
      .avail-header {
        display:flex; align-items:center; gap:0.5rem;
        margin-bottom:0.55rem;
      }
      .avail-dot {
        width:9px; height:9px;
        border-radius:50%;
        background:#34d399;
        animation: pulse 1.8s ease-in-out infinite;
        flex-shrink:0;
      }
      .avail-title {
        font-size:0.9rem; font-weight:700; color:#34d399;
      }
      .avail-text {
        font-size:0.8rem; color:#9ca3af; line-height:1.55;
      }

      /* ── Social Card ── */
      .side-card {
        background:rgba(15,23,42,0.96);
        border:1px solid rgba(148,163,184,0.25);
        border-radius:16px;
        padding:1.3rem 1.4rem 1rem;
        margin-bottom:0.9rem;
        box-shadow:0 8px 30px rgba(0,0,0,0.5);
        animation: fadeUp 0.5s 0.12s ease both;
      }
      .side-heading {
        font-size:0.7rem;
        text-transform:uppercase;
        letter-spacing:0.2em;
        color:#6b7280;
        margin-bottom:0.9rem;
        display:flex; align-items:center; gap:0.4rem;
      }
      .social-item {
        display:flex; align-items:center; gap:0.8rem;
        padding:0.72rem 0.9rem;
        border-radius:12px;
        background:rgba(255,255,255,0.02);
        border:1px solid rgba(148,163,184,0.12);
        margin-bottom:0.5rem;
        text-decoration:none;
        transition:all 0.22s ease;
        animation: slideRight 0.4s ease both;
      }
      .social-item:nth-child(1) { animation-delay:0.15s; }
      .social-item:nth-child(2) { animation-delay:0.22s; }
      .social-item:nth-child(3) { animation-delay:0.29s; }
      .social-item:nth-child(4) { animation-delay:0.36s; }
      .social-item:last-child   { margin-bottom:0; }
      .social-item:hover {
        background:rgba(0,212,255,0.07);
        border-color:rgba(0,212,255,0.3);
        transform:translateX(5px);
        box-shadow:0 6px 20px rgba(0,0,0,0.35);
      }
      .social-icon {
        width:36px; height:36px;
        border-radius:10px;
        display:flex; align-items:center; justify-content:center;
        flex-shrink:0;
        transition:transform 0.2s ease;
      }
      .social-item:hover .social-icon { transform:scale(1.1) rotate(5deg); }
      .social-info { flex:1; min-width:0; }
      .social-name {
        font-size:0.87rem; font-weight:600; color:#e5e7eb;
        white-space:nowrap; overflow:hidden; text-overflow:ellipsis;
      }
      .social-handle {
        font-size:0.73rem; color:#9ca3af; margin-top:0.1rem;
        white-space:nowrap; overflow:hidden; text-overflow:ellipsis;
      }
      .social-arrow {
        color:#00d4ff; flex-shrink:0;
        transition:transform 0.2s ease;
      }
      .social-item:hover .social-arrow { transform:translateX(3px); }

      /* ── Hours Card ── */
      .hours-card {
        background:rgba(15,23,42,0.96);
        border:1px solid rgba(148,163,184,0.25);
        border-radius:16px;
        padding:1.2rem 1.4rem;
        box-shadow:0 8px 30px rgba(0,0,0,0.5);
        animation: fadeUp 0.5s 0.2s ease both;
      }
      .hours-title {
        font-size:0.7rem;
        text-transform:uppercase;
        letter-spacing:0.18em;
        color:#6b7280;
        margin-bottom:0.85rem;
        display:flex; align-items:center; gap:0.4rem;
      }
      .hours-row {
        display:flex;
        justify-content:space-between;
        align-items:center;
        padding:0.4rem 0;
        border-bottom:1px solid rgba(148,163,184,0.08);
        font-size:0.82rem;
      }
      .hours-row:last-child { border-bottom:none; padding-bottom:0; }
      .hours-day { color:#9ca3af; }
      .hours-time { color:#e5e7eb; font-weight:500; }
      .hours-closed { color:#4b5563; }
      .now-badge {
        background:rgba(0,212,255,0.1);
        border:1px solid rgba(0,212,255,0.25);
        color:#00d4ff;
        border-radius:999px;
        padding:0.12rem 0.55rem;
        font-size:0.65rem;
        font-weight:700;
        margin-left:0.4rem;
        letter-spacing:0.05em;
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
        I typically respond within 24 hours on weekdays.
      </p>
    </div>

    <!-- Social Links -->
    <div class="side-card">
      <div class="side-heading">
        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12"
             viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8
                   a2 2 0 0 1 2-2h6"/>
          <polyline points="15 3 21 3 21 9"/>
          <line x1="10" y1="14" x2="21" y2="3"/>
        </svg>
        Connect with me
      </div>

      <!-- GitHub -->
      <a class="social-item"
         href="https://github.com/yourusername" target="_blank">
        <div class="social-icon"
             style="background:rgba(148,163,184,0.08);
                    border:1px solid rgba(148,163,184,0.2);">
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18"
               viewBox="0 0 24 24" fill="none" stroke="#e5e7eb"
               stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <path d="M15 22v-4a4.8 4.8 0 0 0-1-3.2c3 0 6-2 6-5.5
                     .08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5
                     0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2
                     c-.3 1.15-.3 2.35 0 3.5A5.4 5.4 0 0 0 4 9c0 3.5
                     3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65S9 17.44 9 18v4"/>
            <path d="M9 18c-4.51 2-5-2-7-2"/>
          </svg>
        </div>
        <div class="social-info">
          <div class="social-name">GitHub</div>
          <div class="social-handle">github.com/yourusername</div>
        </div>
        <span class="social-arrow">
          <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14"
               viewBox="0 0 24 24" fill="none" stroke="currentColor"
               stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="m9 18 6-6-6-6"/>
          </svg>
        </span>
      </a>

      <!-- LinkedIn -->
      <a class="social-item"
         href="https://linkedin.com/in/yourprofile" target="_blank">
        <div class="social-icon"
             style="background:rgba(10,102,194,0.12);
                    border:1px solid rgba(10,102,194,0.3);">
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18"
               viewBox="0 0 24 24" fill="none" stroke="#7dd3fc"
               stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2
                     2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/>
            <rect width="4" height="12" x="2" y="9"/>
            <circle cx="4" cy="4" r="2"/>
          </svg>
        </div>
        <div class="social-info">
          <div class="social-name">LinkedIn</div>
          <div class="social-handle">linkedin.com/in/yourprofile</div>
        </div>
        <span class="social-arrow">
          <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14"
               viewBox="0 0 24 24" fill="none" stroke="currentColor"
               stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="m9 18 6-6-6-6"/>
          </svg>
        </span>
      </a>

      <!-- Twitter / X -->
      <a class="social-item"
         href="https://twitter.com/yourhandle" target="_blank">
        <div class="social-icon"
             style="background:rgba(29,161,242,0.1);
                    border:1px solid rgba(29,161,242,0.25);">
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18"
               viewBox="0 0 24 24" fill="none" stroke="#7dd3fc"
               stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6
                     2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1
                     9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z"/>
          </svg>
        </div>
        <div class="social-info">
          <div class="social-name">Twitter / X</div>
          <div class="social-handle">@yourhandle</div>
        </div>
        <span class="social-arrow">
          <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14"
               viewBox="0 0 24 24" fill="none" stroke="currentColor"
               stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="m9 18 6-6-6-6"/>
          </svg>
        </span>
      </a>

      <!-- Email -->
      <a class="social-item" href="mailto:dave@example.com">
        <div class="social-icon"
             style="background:rgba(255,107,203,0.1);
                    border:1px solid rgba(255,107,203,0.25);">
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18"
               viewBox="0 0 24 24" fill="none" stroke="#ff6bcb"
               stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <rect width="20" height="16" x="2" y="4" rx="2"/>
            <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
          </svg>
        </div>
        <div class="social-info">
          <div class="social-name">Email</div>
          <div class="social-handle">dave@example.com</div>
        </div>
        <span class="social-arrow">
          <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14"
               viewBox="0 0 24 24" fill="none" stroke="currentColor"
               stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="m9 18 6-6-6-6"/>
          </svg>
        </span>
      </a>
    </div>

    <!-- Working Hours -->
    <div class="hours-card">
      <div class="hours-title">
        <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13"
             viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"/>
          <polyline points="12 6 12 12 16 14"/>
        </svg>
        Working Hours (PHT)
      </div>
      <div class="hours-row">
        <span class="hours-day">Monday – Friday</span>
        <span class="hours-time">
          9:00 AM – 6:00 PM
          <span class="now-badge">NOW</span>
        </span>
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
#   FOOTER
# ═══════════════════════════════════════════════════════
st.markdown("---")

components.html("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  *, *::before, *::after { box-sizing:border-box; margin:0; padding:0; }
  body {
    font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
    background:transparent;
  }
  @keyframes fadeIn {
    from { opacity:0; } to { opacity:1; }
  }
  .footer {
    display:flex;
    justify-content:space-between;
    align-items:center;
    flex-wrap:wrap;
    gap:0.5rem;
    padding:0.4rem 0;
    animation: fadeIn 0.6s ease both;
  }
  .footer-left {
    color:#6b7280; font-size:0.82rem;
    display:flex; align-items:center; gap:0.4rem;
  }
  .footer-left strong { color:#9ca3af; }
  .footer-right {
    display:flex; align-items:center; gap:0.4rem;
    color:#6b7280; font-size:0.8rem;
  }
</style>
</head>
<body>
<div class="footer">
  <div class="footer-left">
    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14"
         viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2"
         stroke-linecap="round" stroke-linejoin="round">
      <path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/>
      <circle cx="12" cy="10" r="3"/>
    </svg>
    © 2026 <strong>Dave Campo</strong> · Built with Python &amp; Streamlit
  </div>
  <div class="footer-right">
    <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13"
         viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2"
         stroke-linecap="round" stroke-linejoin="round">
      <path d="M22 16.92v3a2 2 0 0 1-2.18 2
               19.79 19.79 0 0 1-8.63-3.07
               19.5 19.5 0 0 1-6-6
               19.79 19.79 0 0 1-3.07-8.67
               A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72
               12.84 12.84 0 0 0 .7 2.81
               2 2 0 0 1-.45 2.11L8.09 9.91
               a16 16 0 0 0 6 6l1.27-1.27
               a2 2 0 0 1 2.11-.45
               12.84 12.84 0 0 0 2.81.7
               A2 2 0 0 1 22 16.92z"/>
    </svg>
    Contact Page
  </div>
</div>
</body>
</html>
""", height=46)