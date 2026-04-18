import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import streamlit.components.v1 as components
from components import apply_global_effects

st.set_page_config(
    page_title="Skills | Dave Campo",
    page_icon="🧠",
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
#   GLOBAL STYLES
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

div[data-testid="stRadio"] label p { color: #e5e7eb !important; font-size: 0.95rem !important; }
div[data-testid="stRadio"] > div { gap: 0.6rem; flex-wrap: wrap; }
div[data-testid="stRadio"] > div > label {
    background: rgba(15,23,42,0.6) !important;
    border: 1px solid rgba(148,163,184,0.25) !important;
    border-radius: 8px !important;
    padding: 0.4rem 1rem !important;
    transition: all 0.2s ease !important;
}
div[data-testid="stRadio"] > div > label:hover { border-color: #00d4ff !important; }
h1, h2, h3, h4 { color: #e5e7eb !important; }
hr { border-color: rgba(148,163,184,0.2) !important; margin: 1.5rem 0 !important; }

@media (max-width: 768px) {
    .block-container {
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
    }
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#   SKILL CATEGORIES DATA
# ─────────────────────────────────────────────
SKILL_CATEGORIES = [
    {
        "label": "Languages",
        "icon": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"
                   fill="none" stroke="currentColor" stroke-width="2"
                   stroke-linecap="round" stroke-linejoin="round">
                   <polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>
                   </svg>""",
        "color": "#fca5a5",
        "border": "rgba(239,68,68,0.35)",
        "bg": "rgba(239,68,68,0.08)",
        "skills": [
            ("C",          15),
            ("C++",        18),
            ("Python",     30),
            ("JavaScript", 18),
        ],
    },
    {
        "label": "Frontend",
        "icon": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"
                   fill="none" stroke="currentColor" stroke-width="2"
                   stroke-linecap="round" stroke-linejoin="round">
                   <circle cx="12" cy="12" r="10"/>
                   <path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/>
                   <path d="M2 12h20"/>
                   </svg>""",
        "color": "#7dd3fc",
        "border": "rgba(56,189,248,0.35)",
        "bg": "rgba(56,189,248,0.08)",
        "skills": [
            ("HTML",    85),
            ("CSS",     52),
            ("React",   30),
            ("Spline",  60),
            ("Canva",   72),
        ],
    },
    {
        "label": "Backend & Django",
        "icon": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"
                   fill="none" stroke="currentColor" stroke-width="2"
                   stroke-linecap="round" stroke-linejoin="round">
                   <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
                   </svg>""",
        "color": "#86efac",
        "border": "rgba(22,163,74,0.35)",
        "bg": "rgba(22,163,74,0.08)",
        "skills": [
            ("Django",                50),
            ("Django REST Framework", 45),
            ("Django Channels",       35),
            ("Django Allauth",        60),
        ],
    },
    {
        "label": "Databases",
        "icon": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"
                   fill="none" stroke="currentColor" stroke-width="2"
                   stroke-linecap="round" stroke-linejoin="round">
                   <ellipse cx="12" cy="5" rx="9" ry="3"/>
                   <path d="M3 5V19A9 3 0 0 0 21 19V5"/>
                   <path d="M3 12A9 3 0 0 0 21 12"/>
                   </svg>""",
        "color": "#fde68a",
        "border": "rgba(234,179,8,0.35)",
        "bg": "rgba(234,179,8,0.08)",
        "skills": [
            ("MySQL",     60),
            ("MS Access", 65),
            ("SQLite",    80),
        ],
    },
    {
        "label": "Python Libraries",
        "icon": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"
                   fill="none" stroke="currentColor" stroke-width="2"
                   stroke-linecap="round" stroke-linejoin="round">
                   <path d="M8 3H7a2 2 0 0 0-2 2v5a2 2 0 0 1-2 2 2 2 0 0 1 2 2v5c0 1.1.9 2 2 2h1"/>
                   <path d="M16 3h1a2 2 0 0 1 2 2v5a2 2 0 0 0 2 2 2 2 0 0 0-2 2v5a2 2 0 0 1-2 2h-1"/>
                   </svg>""",
        "color": "#93c5fd",
        "border": "rgba(59,130,246,0.35)",
        "bg": "rgba(59,130,246,0.08)",
        "skills": [
            ("Streamlit", 50),
            ("OpenCV",    50),
            ("Pandas",    30),
            ("NumPy",     28),
            ("Requests",  32),
            ("DeepFace",  12),
        ],
    },
    {
        "label": "Tools & Design",
        "icon": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"
                   fill="none" stroke="currentColor" stroke-width="2"
                   stroke-linecap="round" stroke-linejoin="round">
                   <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77
                            a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91
                            a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>
                   </svg>""",
        "color": "#c4b5fd",
        "border": "rgba(167,139,250,0.35)",
        "bg": "rgba(167,139,250,0.08)",
        "skills": [
            ("GitHub",    78),
            ("VS Code",   85),
            ("Canva",     72),
            ("Spline 3D", 60),
            ("ChatGPT",   90),
        ],
    },
]

# ─────────────────────────────────────────────
#   BADGE DATA
# ─────────────────────────────────────────────
ALL_BADGES = [
    ("C",                 "#fca5a5","rgba(239,68,68,0.1)","rgba(239,68,68,0.35)"),
    ("C++",               "#fca5a5","rgba(239,68,68,0.1)","rgba(239,68,68,0.35)"),
    ("Python",            "#93c5fd","rgba(59,130,246,0.1)","rgba(59,130,246,0.35)"),
    ("JavaScript",        "#fde047","rgba(253,224,71,0.08)","rgba(253,224,71,0.3)"),
    ("HTML",              "#fdba74","rgba(251,146,60,0.1)","rgba(251,146,60,0.35)"),
    ("CSS",               "#7dd3fc","rgba(56,189,248,0.1)","rgba(56,189,248,0.3)"),
    ("React",             "#7dd3fc","rgba(56,189,248,0.1)","rgba(56,189,248,0.3)"),
    ("Django",            "#86efac","rgba(22,163,74,0.1)","rgba(22,163,74,0.35)"),
    ("Django REST",       "#86efac","rgba(22,163,74,0.1)","rgba(22,163,74,0.35)"),
    ("Django Channels",   "#86efac","rgba(22,163,74,0.1)","rgba(22,163,74,0.35)"),
    ("Django Allauth",    "#86efac","rgba(22,163,74,0.1)","rgba(22,163,74,0.35)"),
    ("Django ORM",        "#86efac","rgba(22,163,74,0.1)","rgba(22,163,74,0.35)"),
    ("MySQL",             "#fde68a","rgba(234,179,8,0.08)","rgba(234,179,8,0.3)"),
    ("MS Access",         "#fde68a","rgba(234,179,8,0.08)","rgba(234,179,8,0.3)"),
    ("SQLite",            "#fde68a","rgba(234,179,8,0.08)","rgba(234,179,8,0.3)"),
    ("Streamlit",         "#00d4ff","rgba(0,212,255,0.08)","rgba(0,212,255,0.3)"),
    ("OpenCV",            "#93c5fd","rgba(59,130,246,0.1)","rgba(59,130,246,0.3)"),
    ("Pandas",            "#93c5fd","rgba(59,130,246,0.1)","rgba(59,130,246,0.3)"),
    ("NumPy",             "#93c5fd","rgba(59,130,246,0.1)","rgba(59,130,246,0.3)"),
    ("Spline 3D",         "#c4b5fd","rgba(167,139,250,0.1)","rgba(167,139,250,0.3)"),
    ("Canva",             "#ff6bcb","rgba(255,107,203,0.1)","rgba(255,107,203,0.3)"),
    ("Git & GitHub",      "#fdba74","rgba(251,146,60,0.1)","rgba(251,146,60,0.3)"),
    ("VS Code",           "#9ca3af","rgba(148,163,184,0.08)","rgba(148,163,184,0.25)"),
    ("ChatGPT",           "#86efac","rgba(22,163,74,0.08)","rgba(22,163,74,0.25)"),
]

# ═══════════════════════════════════════════════════════
#   FULL PAGE HTML — single components.html call
# ═══════════════════════════════════════════════════════

# Build skill cards HTML
skill_cards_html = ""
for i, cat in enumerate(SKILL_CATEGORIES):
    bars_html = ""
    for skill_name, pct in cat["skills"]:
        bars_html += f"""
        <div class="bar-row" style="--delay:{i*0.08 + 0.1}s">
          <div class="bar-meta">
            <span class="bar-label">{skill_name}</span>
            <span class="bar-pct" style="color:{cat['color']}">{pct}%</span>
          </div>
          <div class="bar-track">
            <div class="bar-fill"
                 style="--pct:{pct}%;
                        background:linear-gradient(135deg,{cat['color']},rgba(255,255,255,0.2));
                        box-shadow:0 0 12px {cat['bg']};">
            </div>
          </div>
        </div>
        """

    skill_cards_html += f"""
    <div class="skill-card" style="border-color:{cat['border']};
         animation-delay:{i*0.1}s">
      <div class="card-header">
        <div class="card-icon" style="color:{cat['color']};
             background:{cat['bg']};border-color:{cat['border']};">
          {cat['icon']}
        </div>
        <div>
          <div class="card-label" style="color:{cat['color']}">{cat['label']}</div>
          <div class="card-count">{len(cat['skills'])} technologies</div>
        </div>
      </div>
      {bars_html}
    </div>
    """

# Build badges HTML
badges_html = "".join([
    f'<span class="badge" style="color:{color};background:{bg};border-color:{border};">{label}</span>'
    for label, color, bg, border in ALL_BADGES
])

# Interest map data
interest_map = {
    "Frontend":    ("React, HTML, CSS, JavaScript, Spline & Canva for UI/UX design.", "#7dd3fc", "rgba(56,189,248,0.08)", "rgba(56,189,248,0.3)"),
    "Backend":     ("Django, DRF, Django Channels, Celery, MySQL & REST API development.", "#86efac", "rgba(22,163,74,0.08)", "rgba(22,163,74,0.3)"),
    "AI / Python": ("OpenCV, DeepFace, Pandas, NumPy, Streamlit & Python scripting.", "#93c5fd", "rgba(59,130,246,0.08)", "rgba(59,130,246,0.3)"),
    "Django":      ("Full Django ecosystem — ORM, REST, Channels, Celery, Allauth & more.", "#86efac", "rgba(22,163,74,0.08)", "rgba(22,163,74,0.3)"),
}

components.html(f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

  body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: transparent;
    color: #e5e7eb;
    -webkit-font-smoothing: antialiased;
  }}

  /* ── Keyframes ─────────────────────────────── */
  @keyframes fadeUp {{
    from {{ opacity: 0; transform: translateY(28px); }}
    to   {{ opacity: 1; transform: translateY(0);    }}
  }}
  @keyframes fillBar {{
    from {{ width: 0; }}
    to   {{ width: var(--pct); }}
  }}
  @keyframes shimmer {{
    0%   {{ background-position: -200% center; }}
    100% {{ background-position:  200% center; }}
  }}
  @keyframes pulse {{
    0%, 100% {{ opacity: 1; }}
    50%       {{ opacity: 0.6; }}
  }}
  @keyframes badgePop {{
    from {{ opacity: 0; transform: scale(0.8); }}
    to   {{ opacity: 1; transform: scale(1);   }}
  }}
  @keyframes glowPulse {{
    0%,100% {{ box-shadow: 0 0 20px rgba(0,212,255,0.15); }}
    50%      {{ box-shadow: 0 0 40px rgba(0,212,255,0.35); }}
  }}

  /* ── Hero ──────────────────────────────────── */
  .hero {{
    background: rgba(15,23,42,0.97);
    border: 1px solid rgba(148,163,184,0.3);
    border-radius: 20px;
    padding: 2.2rem 2.4rem 2rem;
    margin-bottom: 1.8rem;
    animation: fadeUp 0.6s ease both, glowPulse 4s ease-in-out infinite;
    position: relative;
    overflow: hidden;
  }}
  .hero::before {{
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg,
      rgba(0,212,255,0.04) 0%,
      transparent 50%,
      rgba(255,107,203,0.04) 100%);
    pointer-events: none;
  }}
  .hero-eyebrow {{
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.22em;
    color: #00d4ff;
    margin-bottom: 0.7rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }}
  .hero-eyebrow-dot {{
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #00d4ff;
    animation: pulse 2s ease-in-out infinite;
  }}
  .hero-title {{
    font-size: clamp(2rem, 5vw, 2.8rem);
    font-weight: 800;
    color: #e5e7eb;
    line-height: 1.15;
    margin-bottom: 0.7rem;
    display: flex;
    align-items: center;
    gap: 0.6rem;
  }}
  .hero-title svg {{ flex-shrink: 0; }}
  .hero-desc {{
    font-size: clamp(0.88rem, 2vw, 1rem);
    color: #9ca3af;
    line-height: 1.7;
    max-width: 560px;
  }}
  .hero-stats {{
    display: flex;
    gap: 1.5rem;
    margin-top: 1.4rem;
    flex-wrap: wrap;
  }}
  .hero-stat {{
    display: flex;
    flex-direction: column;
    gap: 0.15rem;
  }}
  .hero-stat-num {{
    font-size: 1.6rem;
    font-weight: 800;
    background: linear-gradient(135deg, #00d4ff, #ff6bcb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }}
  .hero-stat-lbl {{
    font-size: 0.75rem;
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: 0.1em;
  }}

  /* ── Grid ──────────────────────────────────── */
  .grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1rem;
    margin-bottom: 1.2rem;
  }}

  /* ── Skill Card ────────────────────────────── */
  .skill-card {{
    background: rgba(15,23,42,0.96);
    border: 1px solid;
    border-radius: 16px;
    padding: 1.4rem 1.5rem;
    animation: fadeUp 0.55s ease both;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    position: relative;
    overflow: hidden;
  }}
  .skill-card::after {{
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg,
      rgba(255,255,255,0.02) 0%,
      transparent 60%);
    pointer-events: none;
  }}
  .skill-card:hover {{
    transform: translateY(-4px);
    box-shadow: 0 20px 50px rgba(0,0,0,0.6);
  }}
  .card-header {{
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 1.2rem;
  }}
  .card-icon {{
    width: 40px; height: 40px;
    border-radius: 10px;
    border: 1px solid;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    transition: transform 0.3s ease;
  }}
  .skill-card:hover .card-icon {{ transform: rotate(8deg) scale(1.1); }}
  .card-label {{
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    font-weight: 700;
    margin-bottom: 0.15rem;
  }}
  .card-count {{
    font-size: 0.76rem;
    color: #6b7280;
  }}

  /* ── Bars ──────────────────────────────────── */
  .bar-row {{
    margin-bottom: 0.9rem;
    animation: fadeUp 0.4s ease both;
    animation-delay: var(--delay, 0.1s);
  }}
  .bar-meta {{
    display: flex;
    justify-content: space-between;
    margin-bottom: 0.32rem;
  }}
  .bar-label {{
    color: #e5e7eb;
    font-size: 0.88rem;
    font-weight: 500;
  }}
  .bar-pct {{
    font-size: 0.8rem;
    font-weight: 700;
  }}
  .bar-track {{
    width: 100%;
    height: 7px;
    border-radius: 999px;
    background: rgba(148,163,184,0.1);
    border: 1px solid rgba(148,163,184,0.12);
    overflow: hidden;
  }}
  .bar-fill {{
    height: 100%;
    border-radius: 999px;
    width: 0;
    animation: fillBar 1s cubic-bezier(0.4,0,0.2,1) forwards;
    animation-delay: 0.3s;
  }}

  /* ── Badge Cloud ───────────────────────────── */
  .badge-section {{
    background: rgba(15,23,42,0.96);
    border: 1px solid rgba(148,163,184,0.2);
    border-radius: 16px;
    padding: 1.5rem 1.6rem;
    margin-bottom: 1.4rem;
    animation: fadeUp 0.6s 0.4s ease both;
  }}
  .badge-title {{
    font-size: 1rem;
    font-weight: 700;
    color: #e5e7eb;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }}
  .badge-eyebrow {{
    font-size: 0.68rem;
    text-transform: uppercase;
    letter-spacing: 0.16em;
    color: #00d4ff;
    margin-bottom: 0.4rem;
  }}
  .badge-cloud {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
  }}
  .badge {{
    border: 1px solid;
    border-radius: 999px;
    padding: 0.3rem 0.9rem;
    font-size: 0.8rem;
    font-weight: 600;
    white-space: nowrap;
    cursor: default;
    animation: badgePop 0.4s ease both;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }}
  .badge:hover {{
    transform: scale(1.08) translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.4);
  }}

  /* ── Interest Selector ─────────────────────── */
  .interest-section {{
    margin-bottom: 1rem;
    animation: fadeUp 0.6s 0.5s ease both;
  }}
  .interest-label {{
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: #6b7280;
    margin-bottom: 0.8rem;
  }}
  .interest-tabs {{
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
    margin-bottom: 0.9rem;
  }}
  .tab-btn {{
    background: rgba(15,23,42,0.7);
    border: 1px solid rgba(148,163,184,0.2);
    border-radius: 8px;
    padding: 0.45rem 1.1rem;
    font-size: 0.88rem;
    color: #9ca3af;
    cursor: pointer;
    transition: all 0.2s ease;
    font-family: inherit;
    font-weight: 500;
  }}
  .tab-btn:hover {{ border-color: #00d4ff; color: #e5e7eb; }}
  .tab-btn.active {{
    background: rgba(0,212,255,0.12);
    border-color: rgba(0,212,255,0.5);
    color: #00d4ff;
    font-weight: 700;
  }}
  .interest-desc {{
    border: 1px solid;
    border-radius: 10px;
    padding: 0.85rem 1.1rem;
    font-size: 0.93rem;
    color: #e5e7eb;
    line-height: 1.6;
    transition: all 0.3s ease;
    display: flex;
    align-items: flex-start;
    gap: 0.5rem;
  }}
  .interest-desc svg {{ flex-shrink: 0; margin-top: 2px; }}

  /* ── Section Divider ───────────────────────── */
  .divider {{
    height: 1px;
    background: rgba(148,163,184,0.15);
    margin: 1.6rem 0;
  }}

  /* ── Footer ────────────────────────────────── */
  .footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 0.5rem;
    padding-top: 1rem;
    border-top: 1px solid rgba(148,163,184,0.15);
  }}
  .footer-left {{ color: #6b7280; font-size: 0.82rem; }}
  .footer-left strong {{ color: #9ca3af; }}

  /* ── Responsive ────────────────────────────── */
  @media (max-width: 640px) {{
    .hero {{ padding: 1.4rem 1.2rem 1.4rem; }}
    .hero-stats {{ gap: 1rem; }}
    .grid {{ grid-template-columns: 1fr; }}
    .interest-tabs {{ gap: 0.4rem; }}
    .tab-btn {{ font-size: 0.82rem; padding: 0.4rem 0.8rem; }}
    .badge-section {{ padding: 1.1rem 1rem; }}
    .badge {{ font-size: 0.75rem; padding: 0.25rem 0.7rem; }}
  }}
</style>
</head>
<body>

<!-- ═══ HERO ═════════════════════════════════════════ -->
<div class="hero">
  <div class="hero-eyebrow">
    <div class="hero-eyebrow-dot"></div>
    What I work with
  </div>
  <h1 class="hero-title">
    <svg xmlns="http://www.w3.org/2000/svg" width="34" height="34"
         viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2"
         stroke-linecap="round" stroke-linejoin="round">
      <path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44
               2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58
               2.5 2.5 0 0 1 1.32-4.24l.67-.23A2.5 2.5 0 0 0 7.05 2.5"/>
      <path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44
               2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58
               2.5 2.5 0 0 0-1.32-4.24l-.67-.23A2.5 2.5 0 0 1 16.95 2.5"/>
    </svg>
    Skills
  </h1>
  <p class="hero-desc">
    A snapshot of my full-stack toolkit — languages, frameworks, databases,
    and every tool I reach for when building something real.
  </p>
  <div class="hero-stats">
    <div class="hero-stat">
      <span class="hero-stat-num">6+</span>
      <span class="hero-stat-lbl">Categories</span>
    </div>
    <div class="hero-stat">
      <span class="hero-stat-num">24+</span>
      <span class="hero-stat-lbl">Technologies</span>
    </div>
    <div class="hero-stat">
      <span class="hero-stat-num">3+</span>
      <span class="hero-stat-lbl">Years Learning</span>
    </div>
  </div>
</div>

<!-- ═══ SKILL CARDS GRID ═══════════════════════════════ -->
<div class="grid">
  {skill_cards_html}
</div>

<div class="divider"></div>

<!-- ═══ BADGE CLOUD ════════════════════════════════════ -->
<div class="badge-section">
  <div class="badge-eyebrow">Full Tech Stack</div>
  <div class="badge-title">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"
         viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2"
         stroke-linecap="round" stroke-linejoin="round">
      <path d="M12 2H2v10l9.29 9.29c.94.94 2.48.94 3.42 0l6.58-6.58
               c.94-.94.94-2.48 0-3.42L12 2Z"/>
      <path d="M7 7h.01"/>
    </svg>
    All Technologies at a Glance
  </div>
  <div class="badge-cloud">
    {badges_html}
  </div>
</div>

<div class="divider"></div>

<!-- ═══ INTEREST SELECTOR ══════════════════════════════ -->
<div class="interest-section">
  <div class="interest-label">Which area interests you most?</div>
  <div class="interest-tabs">
    <button class="tab-btn active" onclick="selectTab(this,'Frontend')">Frontend</button>
    <button class="tab-btn" onclick="selectTab(this,'Backend')">Backend</button>
    <button class="tab-btn" onclick="selectTab(this,'AI / Python')">AI / Python</button>
    <button class="tab-btn" onclick="selectTab(this,'Django')">Django</button>
  </div>

  <div id="interest-Frontend" class="interest-desc"
       style="background:rgba(56,189,248,0.08);border-color:rgba(56,189,248,0.3);">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
         viewBox="0 0 24 24" fill="none" stroke="#7dd3fc" stroke-width="2"
         stroke-linecap="round" stroke-linejoin="round" style="margin-top:2px">
      <path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912
               a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1
               1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/>
    </svg>
    <div>
      <strong style="color:#7dd3fc">Frontend:</strong>
      React, HTML, CSS, JavaScript, Spline &amp; Canva for UI/UX design.
    </div>
  </div>

  <div id="interest-Backend" class="interest-desc" style="display:none;
       background:rgba(22,163,74,0.08);border-color:rgba(22,163,74,0.3);">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
         viewBox="0 0 24 24" fill="none" stroke="#86efac" stroke-width="2"
         stroke-linecap="round" stroke-linejoin="round" style="margin-top:2px">
      <path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912
               a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1
               1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/>
    </svg>
    <div>
      <strong style="color:#86efac">Backend:</strong>
      Django, DRF, Django Channels, Celery, MySQL &amp; REST API development.
    </div>
  </div>

  <div id="interest-AI / Python" class="interest-desc" style="display:none;
       background:rgba(59,130,246,0.08);border-color:rgba(59,130,246,0.3);">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
         viewBox="0 0 24 24" fill="none" stroke="#93c5fd" stroke-width="2"
         stroke-linecap="round" stroke-linejoin="round" style="margin-top:2px">
      <path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912
               a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1
               1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/>
    </svg>
    <div>
      <strong style="color:#93c5fd">AI / Python:</strong>
      OpenCV, DeepFace, Pandas, NumPy, Streamlit &amp; Python scripting.
    </div>
  </div>

  <div id="interest-Django" class="interest-desc" style="display:none;
       background:rgba(22,163,74,0.08);border-color:rgba(22,163,74,0.3);">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
         viewBox="0 0 24 24" fill="none" stroke="#86efac" stroke-width="2"
         stroke-linecap="round" stroke-linejoin="round" style="margin-top:2px">
      <path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912
               a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1
               1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/>
    </svg>
    <div>
      <strong style="color:#86efac">Django:</strong>
      Full Django ecosystem — ORM, REST, Channels, Celery, Allauth &amp; more.
    </div>
  </div>
</div>

<div class="divider"></div>

<!-- ═══ FOOTER ═════════════════════════════════════════ -->
<div class="footer">
  <div class="footer-left">
    © 2026 <strong>Dave Campo</strong> · Built with Python &amp; Streamlit
  </div>
  <div style="display:flex;align-items:center;gap:0.4rem;color:#6b7280;font-size:0.8rem;">
    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14"
         viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2"
         stroke-linecap="round" stroke-linejoin="round">
      <polyline points="16 18 22 12 16 6"/>
      <polyline points="8 6 2 12 8 18"/>
    </svg>
    Skills Page
  </div>
</div>

<script>
  /* ── Tab Switcher ─────────────────────────── */
  function selectTab(btn, key) {{
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('.interest-desc').forEach(el => {{
      el.style.display = 'none';
    }});
    var target = document.getElementById('interest-' + key);
    if (target) {{
      target.style.display = 'flex';
      target.style.animation = 'fadeUp 0.3s ease';
    }}
  }}

  /* ── Stagger badge animations ─────────────── */
  document.querySelectorAll('.badge').forEach(function(b, i) {{
    b.style.animationDelay = (0.05 * i + 0.2) + 's';
    b.style.opacity = '0';
    b.addEventListener('animationend', function() {{
      b.style.opacity = '1';
    }});
  }});

  /* ── Intersection Observer for bars ──────── */
  var observer = new IntersectionObserver(function(entries) {{
    entries.forEach(function(entry) {{
      if (entry.isIntersecting) {{
        var fill = entry.target.querySelector('.bar-fill');
        if (fill) {{
          fill.style.animationPlayState = 'running';
        }}
      }}
    }});
  }}, {{ threshold: 0.1 }});

  document.querySelectorAll('.bar-row').forEach(function(row) {{
    var fill = row.querySelector('.bar-fill');
    if (fill) fill.style.animationPlayState = 'paused';
    observer.observe(row);
  }});

  /* ── Card hover glow ──────────────────────── */
  document.querySelectorAll('.skill-card').forEach(function(card) {{
    card.addEventListener('mouseenter', function() {{
      this.style.transition = 'transform 0.25s ease, box-shadow 0.25s ease';
    }});
  }});
</script>

</body>
</html>
""", height=3200, scrolling=False)