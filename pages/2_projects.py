import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import streamlit.components.v1 as components
import random
from components import apply_global_effects

st.set_page_config(
    page_title="Projects | Dave Campo",
    page_icon="💼",
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

# ---------- GLOBAL STYLES ----------
st.markdown("""
<style>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css');
.stApp {
    background: radial-gradient(circle at 0% 0%, #1f2937 0, #020617 40%, #000 100%) !important;
}
.block-container {
    max-width: 1200px;
    padding-top: 1.5rem !important;
    padding-bottom: 2rem !important;
}
.stApp, .stApp * { color: #e5e7eb; }
div[data-testid="stSelectbox"] > div > div {
    background-color: #0f172a !important;
    border: 1px solid rgba(148,163,184,0.35) !important;
    border-radius: 12px !important;
    color: #e5e7eb !important;
}
div[data-testid="stSelectbox"] span,
div[data-testid="stSelectbox"] p,
div[data-testid="stSelectbox"] div { color: #e5e7eb !important; }
div[data-testid="stSelectbox"] svg { fill: #e5e7eb !important; }
ul[data-testid="stSelectboxVirtualDropdown"] {
    background-color: #0f172a !important;
    border: 1px solid rgba(148,163,184,0.35) !important;
    border-radius: 10px !important;
}
ul[data-testid="stSelectboxVirtualDropdown"] li {
    color: #e5e7eb !important;
    background-color: #0f172a !important;
}
ul[data-testid="stSelectboxVirtualDropdown"] li:hover {
    background-color: rgba(0,212,255,0.12) !important;
}
div[data-testid="stSlider"] label p { color: #9ca3af !important; }
div[data-testid="stButton"] button {
    background: linear-gradient(135deg, #00d4ff, #ff6bcb) !important;
    color: #000 !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.55rem 1.8rem !important;
    font-size: 0.97rem !important;
}
div[data-testid="stButton"] button p { color: #000 !important; }
div[data-testid="stAlert"] {
    border-radius: 10px !important;
    background: rgba(15,23,42,0.8) !important;
}
div[data-testid="stAlert"] p { color: #e5e7eb !important; }
hr { border-color: rgba(148,163,184,0.2) !important; margin: 1.5rem 0 !important; }
iframe { display: block; border: none !important; }
</style>
""", unsafe_allow_html=True)

# ---------- DATA ----------
PROJECTS = {
    "globe Portfolio Website": {
        "description": "A personal portfolio built with Streamlit featuring smooth navigation, dark theme UI, animations, and interactive components.",
        "tech": ["Python", "Streamlit", "CSS", "HTML"],
        "status": "Live",
        "year": "2024",
        "icon": "fa-globe",
        "color": "#00d4ff",
        "features": ["Responsive design", "Dark theme", "Smooth animations", "Custom navigation"],
        "difficulty": "Intermediate",
    },
    "robot Face Recognition System": {
        "description": "AI-powered attendance system using facial recognition with real-time detection, logging, and an admin dashboard.",
        "tech": ["Python", "OpenCV", "DeepFace", "SQLite"],
        "status": "Completed",
        "year": "2024",
        "icon": "fa-robot",
        "color": "#ff6bcb",
        "features": ["Real-time detection", "Auto attendance logging", "Admin dashboard", "98% accuracy"],
        "difficulty": "Advanced",
    },
    "cart Grocery Web App": {
        "description": "Full-stack e-commerce grocery platform with product listings, cart management, checkout flow, and order tracking.",
        "tech": ["React", "Node.js", "MongoDB", "Stripe"],
        "status": "In Progress",
        "year": "2024",
        "icon": "fa-cart-shopping",
        "color": "#a78bfa",
        "features": ["Cart & checkout", "Payment integration", "Order tracking", "Admin panel"],
        "difficulty": "Advanced",
    },
    "chart Data Dashboard": {
        "description": "Interactive analytics dashboard with live charts, CSV upload support, and exportable reports.",
        "tech": ["Python", "Plotly", "Pandas", "Streamlit"],
        "status": "Completed",
        "year": "2023",
        "icon": "fa-chart-line",
        "color": "#34d399",
        "features": ["Live charts", "CSV upload", "Export reports", "Filters & drill-down"],
        "difficulty": "Intermediate",
    },
}

STATUS_COLORS = {
    "Live":        ("rgba(16,185,129,0.15)", "rgba(16,185,129,0.5)", "#6ee7b7"),
    "Completed":   ("rgba(0,212,255,0.12)",  "rgba(0,212,255,0.4)",  "#00d4ff"),
    "In Progress": ("rgba(251,191,36,0.12)", "rgba(251,191,36,0.4)", "#fde68a"),
}
DIFFICULTY_COLORS = {
    "Intermediate": "#00d4ff",
    "Advanced":     "#ff6bcb",
    "Beginner":     "#34d399",
}

if "ratings"        not in st.session_state: st.session_state.ratings        = {}
if "rated_projects" not in st.session_state: st.session_state.rated_projects = set()
if "liked_projects" not in st.session_state: st.session_state.liked_projects = set()

# ── Hero ─────────────────────────────────────────────────────
components.html("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
<div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
background:rgba(15,23,42,0.96);border-radius:18px;border:1px solid rgba(148,163,184,0.35);
padding:2.2rem 2.2rem 1.8rem;box-shadow:0 24px 60px rgba(0,0,0,0.85);backdrop-filter:blur(18px);margin-bottom:0.5rem;">
  <p style="font-size:0.82rem;text-transform:uppercase;letter-spacing:0.22em;color:#00d4ff;margin:0 0 0.8rem;">Selected work</p>
  <h1 style="font-size:2.6rem;font-weight:800;color:#e5e7eb;margin:0 0 0.6rem;">
    <i class="fa-solid fa-briefcase" style="color:#00d4ff;margin-right:0.5rem;"></i>Projects
  </h1>
  <p style="font-size:1rem;color:#9ca3af;line-height:1.65;margin:0;">
    A glimpse into some of the projects I've built.
  </p>
</div>
""", height=210)

# ── Project selector ─────────────────────────────────────────
st.markdown("""
<div style="color:#9ca3af;font-size:0.82rem;text-transform:uppercase;
letter-spacing:0.15em;margin-bottom:0.3rem;margin-top:0.8rem;">Choose a project to explore</div>
""", unsafe_allow_html=True)

project_name = st.selectbox("Project", list(PROJECTS.keys()), label_visibility="collapsed")
proj = PROJECTS[project_name]
status_bg, status_border, status_text = STATUS_COLORS.get(proj["status"],
    ("rgba(148,163,184,0.1)", "rgba(148,163,184,0.3)", "#9ca3af"))
diff_color  = DIFFICULTY_COLORS.get(proj["difficulty"], "#9ca3af")
liked       = project_name in st.session_state.liked_projects
avg_rating  = (round(sum(st.session_state.ratings.get(project_name, [])) /
               len(st.session_state.ratings.get(project_name, [1])), 1)
               if st.session_state.ratings.get(project_name) else "—")

tech_badges   = "".join([
    f'<span style="background:rgba(0,212,255,0.1);border:1px solid rgba(0,212,255,0.3);'
    f'border-radius:999px;padding:0.2rem 0.75rem;font-size:0.78rem;color:#00d4ff;'
    f'font-weight:600;margin-right:0.4rem;margin-bottom:0.4rem;display:inline-block;">{t}</span>'
    for t in proj["tech"]
])

feature_items = "".join([
    f'<div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.4rem;">'
    f'<i class="fa-solid fa-circle-check" style="color:#00d4ff;font-size:0.75rem;flex-shrink:0;"></i>'
    f'<span style="color:#9ca3af;font-size:0.9rem;">{f}</span></div>'
    for f in proj["features"]
])

# Status icon mapping
STATUS_ICONS = {
    "Live":        "fa-circle-dot",
    "Completed":   "fa-circle-check",
    "In Progress": "fa-spinner",
}
status_icon = STATUS_ICONS.get(proj["status"], "fa-circle")

components.html(f"""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
<div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
background:rgba(15,23,42,0.96);border-radius:18px;border:1px solid rgba(148,163,184,0.35);
padding:1.8rem 2rem;box-shadow:0 24px 60px rgba(0,0,0,0.85);backdrop-filter:blur(18px);margin-top:0.5rem;">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.8rem;">
    <div style="flex:1;min-width:200px;">
      <div style="
        width:52px;height:52px;border-radius:14px;
        background:linear-gradient(135deg,rgba(0,212,255,0.15),rgba(255,107,203,0.15));
        border:1px solid rgba(0,212,255,0.3);
        display:flex;align-items:center;justify-content:center;
        margin-bottom:0.6rem;">
        <i class="fa-solid {proj['icon']}" style="font-size:1.5rem;color:{proj['color']};"></i>
      </div>
      <h2 style="color:#e5e7eb;font-size:1.55rem;font-weight:800;margin:0 0 0.3rem;">
        {" ".join(project_name.split()[1:])}
      </h2>
      <div style="display:flex;gap:0.5rem;flex-wrap:wrap;margin-bottom:0.8rem;">
        <span style="background:{status_bg};border:1px solid {status_border};border-radius:999px;
          padding:0.2rem 0.8rem;font-size:0.75rem;color:{status_text};font-weight:600;">
          <i class="fa-solid {status_icon}" style="margin-right:4px;"></i>{proj['status']}
        </span>
        <span style="background:rgba(148,163,184,0.08);border:1px solid rgba(148,163,184,0.25);
          border-radius:999px;padding:0.2rem 0.8rem;font-size:0.75rem;color:{diff_color};font-weight:600;">
          <i class="fa-solid fa-signal" style="margin-right:4px;"></i>{proj['difficulty']}
        </span>
        <span style="background:rgba(148,163,184,0.08);border:1px solid rgba(148,163,184,0.2);
          border-radius:999px;padding:0.2rem 0.8rem;font-size:0.75rem;color:#9ca3af;">
          <i class="fa-solid fa-calendar" style="margin-right:4px;"></i>{proj['year']}
        </span>
      </div>
    </div>
    <div style="background:linear-gradient(135deg,rgba(0,212,255,0.08),rgba(255,107,203,0.08));
      border:1px solid rgba(0,212,255,0.2);border-radius:14px;padding:1rem 1.4rem;
      text-align:center;min-width:110px;">
      <div style="font-size:2rem;font-weight:900;background:linear-gradient(135deg,#00d4ff,#ff6bcb);
        -webkit-background-clip:text;-webkit-text-fill-color:transparent;">{avg_rating}</div>
      <div style="color:#9ca3af;font-size:0.75rem;margin-top:0.2rem;">
        <i class="fa-solid fa-star" style="color:#fde68a;margin-right:3px;"></i>avg rating
      </div>
    </div>
  </div>
  <p style="color:#9ca3af;font-size:0.97rem;line-height:1.65;margin:0 0 1.2rem;">{proj['description']}</p>
  <div style="margin-bottom:1.2rem;">
    <div style="font-size:0.72rem;text-transform:uppercase;letter-spacing:0.18em;color:#9ca3af;margin-bottom:0.5rem;">
      <i class="fa-solid fa-layer-group" style="margin-right:5px;color:#00d4ff;"></i>Tech Stack
    </div>
    <div>{tech_badges}</div>
  </div>
  <div>
    <div style="font-size:0.72rem;text-transform:uppercase;letter-spacing:0.18em;color:#9ca3af;margin-bottom:0.6rem;">
      <i class="fa-solid fa-list-check" style="margin-right:5px;color:#00d4ff;"></i>Key Features
    </div>
    {feature_items}
  </div>
</div>
""", height=520)

# ── Like + Rating ────────────────────────────────────────────
components.html("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
<div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;margin:0.8rem 0 0.3rem;">
  <span style="font-size:0.78rem;text-transform:uppercase;letter-spacing:0.18em;color:#00d4ff;">
    <i class="fa-solid fa-star" style="margin-right:4px;"></i>Rate &amp; Interact
  </span>
  <h3 style="color:#e5e7eb;font-size:1.3rem;font-weight:700;margin:0.3rem 0 0;">
    <i class="fa-solid fa-star" style="color:#fde68a;margin-right:6px;"></i>Rate this Project
  </h3>
</div>
""", height=70)

col_like, _ = st.columns([1, 4])
with col_like:
    heart_icon = "fa-heart" if liked else "fa-heart"
    heart_color = "#ff6bcb" if liked else "#9ca3af"
    heart_label = "Liked" if liked else "Like"
    if st.button(f"{'❤ ' if liked else '♡ '}{heart_label}", key="like_btn"):
        if project_name in st.session_state.liked_projects:
            st.session_state.liked_projects.discard(project_name)
        else:
            st.session_state.liked_projects.add(project_name)
        st.rerun()

total_likes = len(st.session_state.liked_projects)
liked_msg   = "You liked this project!" if liked else ""
components.html(f"""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
<div style="font-family:sans-serif;color:#9ca3af;font-size:0.88rem;margin-top:0.3rem;display:flex;align-items:center;gap:0.4rem;">
  <i class="fa-solid fa-heart" style="color:{'#ff6bcb' if liked else 'rgba(148,163,184,0.4)'};font-size:0.9rem;"></i>
  <span>{'<span style="color:#ff6bcb;">You liked this project!</span>' if liked else ''}</span>
  <span style="color:rgba(148,163,184,0.4);">·</span>
  <span>{total_likes} total like{'s' if total_likes!=1 else ''}</span>
</div>
""", height=35)

st.markdown('<div style="color:#9ca3af;font-size:0.85rem;margin-top:0.8rem;margin-bottom:0.3rem;">Drag to rate (1–10):</div>', unsafe_allow_html=True)
rating = st.slider("Rating", 1, 10, 5, label_visibility="collapsed")

# Build star icons
full_stars = rating // 2
half_star  = rating % 2
empty      = 5 - full_stars - half_star

stars_html = (
    '<i class="fa-solid fa-star" style="color:#fde68a;font-size:1.2rem;"></i>' * full_stars +
    ('<i class="fa-solid fa-star-half-stroke" style="color:#fde68a;font-size:1.2rem;"></i>' if half_star else '') +
    '<i class="fa-regular fa-star" style="color:rgba(253,230,138,0.3);font-size:1.2rem;"></i>' * empty
)

components.html(f"""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
<div style="font-family:sans-serif;display:flex;align-items:center;gap:0.8rem;margin-top:0.2rem;">
  <span style="display:flex;gap:3px;">{stars_html}</span>
  <span style="font-size:1.1rem;font-weight:700;background:linear-gradient(135deg,#00d4ff,#ff6bcb);
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;">{rating}/10</span>
</div>
""", height=45)

already_rated = project_name in st.session_state.rated_projects
if not already_rated:
    if st.button("Submit Rating", key="rate_btn"):
        if project_name not in st.session_state.ratings:
            st.session_state.ratings[project_name] = []
        st.session_state.ratings[project_name].append(rating)
        st.session_state.rated_projects.add(project_name)
        st.rerun()
else:
    components.html(f"""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
    <div style="font-family:sans-serif;background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.4);
    border-radius:12px;padding:1rem 1.2rem;margin-top:0.5rem;">
      <div style="color:#6ee7b7;font-weight:700;font-size:1rem;">
        <i class="fa-solid fa-circle-check" style="margin-right:6px;"></i>
        Thank you for rating <strong>{project_name.split(' ', 1)[1] if ' ' in project_name else project_name}</strong>!
      </div>
      <div style="color:#9ca3af;font-size:0.87rem;margin-top:0.3rem;">
        You gave it
        <strong style="color:#00d4ff;">{rating}/10</strong>
        <i class="fa-solid fa-star" style="color:#fde68a;margin-left:3px;"></i>
      </div>
    </div>
    """, height=100)
    if st.button("Change Rating", key="change_rate_btn"):
        st.session_state.rated_projects.discard(project_name)
        st.rerun()

if st.session_state.ratings:
    st.markdown("---")
    rating_rows = "".join([f"""
    <div style="margin-bottom:0.7rem;">
      <div style="display:flex;justify-content:space-between;margin-bottom:0.3rem;">
        <span style="color:#e5e7eb;font-size:0.88rem;">
          <i class="fa-solid fa-diagram-project" style="color:#00d4ff;margin-right:5px;font-size:0.75rem;"></i>{p}
        </span>
        <span style="color:#00d4ff;font-size:0.88rem;font-weight:700;">
          <i class="fa-solid fa-star" style="color:#fde68a;margin-right:3px;font-size:0.75rem;"></i>
          {round(sum(r)/len(r),1)}/10
        </span>
      </div>
      <div style="width:100%;height:7px;border-radius:999px;background:rgba(148,163,184,0.12);overflow:hidden;">
        <div style="width:{int(round(sum(r)/len(r),1)*10)}%;height:100%;border-radius:999px;
          background:linear-gradient(135deg,#00d4ff,#ff6bcb);"></div>
      </div>
    </div>
    """ for p, r in st.session_state.ratings.items()])

    components.html(f"""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
    <div style="font-family:sans-serif;background:rgba(15,23,42,0.96);border:1px solid rgba(148,163,184,0.2);
    border-radius:14px;padding:1.2rem 1.4rem;">{rating_rows}</div>
    """, height=len(st.session_state.ratings) * 75 + 30)

# ═══════════════════════════════════════════════════════════════
#                    SNAKE GAME
# ═══════════════════════════════════════════════════════════════
st.markdown("---")

components.html("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
<div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;margin-bottom:0.6rem;">
  <span style="font-size:0.78rem;text-transform:uppercase;letter-spacing:0.2em;color:#ff6bcb;">
    <i class="fa-solid fa-gamepad" style="margin-right:4px;"></i>Mini Game
  </span>
  <h2 style="font-size:1.85rem;font-weight:800;color:#e5e7eb;margin:0.3rem 0 0.4rem;">
    <i class="fa-solid fa-worm" style="color:#34d399;margin-right:8px;"></i>Snake Game
  </h2>
  <p style="color:#9ca3af;font-size:0.95rem;margin:0;">
    <strong style="color:#00d4ff;">
      <i class="fa-solid fa-keyboard" style="margin-right:4px;"></i>Keyboard:
    </strong> Arrow Keys / WASD
  </p>
</div>
""", height=120)

components.html("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no"/>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
<style>
  * { margin:0; padding:0; box-sizing:border-box; -webkit-tap-highlight-color:transparent; }

  body {
    background: transparent;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0 4px;
    overscroll-behavior: none;
  }

  .game-wrapper { width: 100%; max-width: 620px; }

  /* ── Scoreboard ── */
  .scoreboard {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 6px;
    margin-bottom: 8px;
  }

  .score-card {
    background: rgba(15,23,42,0.96);
    border: 1px solid rgba(148,163,184,0.2);
    border-radius: 10px;
    padding: 8px 6px;
    text-align: center;
  }

  .score-value {
    font-size: 1.5rem;
    font-weight: 900;
    background: linear-gradient(135deg, #00d4ff, #ff6bcb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1;
  }

  .score-label {
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #9ca3af;
    margin-top: 3px;
  }

  .score-label i { margin-right: 3px; }

  /* ── Canvas container ── */
  .canvas-wrap {
    position: relative;
    border-radius: 14px;
    overflow: hidden;
    border: 2px solid rgba(0,212,255,0.35);
    box-shadow: 0 0 30px rgba(0,212,255,0.12), 0 20px 50px rgba(0,0,0,0.8);
    touch-action: none;
    cursor: pointer;
  }

  canvas {
    display: block;
    width: 100%;
    height: auto;
  }

  /* ── Overlays ── */
  .overlay {
    position: absolute; inset: 0;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    background: rgba(2,6,23,0.90);
    backdrop-filter: blur(8px);
    border-radius: 12px;
    text-align: center;
    padding: 1.5rem;
  }
  .overlay.hidden { display: none; }

  .ov-icon {
    font-size: 3rem;
    margin-bottom: 10px;
  }
  .ov-title {
    font-size: 1.8rem; font-weight: 900;
    background: linear-gradient(135deg,#00d4ff,#ff6bcb);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin-bottom: 6px;
  }
  .ov-sub {
    color: #9ca3af; font-size: 0.9rem;
    line-height: 1.55; margin-bottom: 1.2rem;
  }
  .ov-sub i { margin-right: 4px; }

  .play-btn {
    background: linear-gradient(135deg,#00d4ff,#ff6bcb);
    color: #000; font-weight: 800; font-size: 1rem;
    border: none; border-radius: 999px;
    padding: 0.65rem 2rem;
    cursor: pointer;
    transition: transform 0.15s, opacity 0.15s;
    display: flex; align-items: center; gap: 0.5rem;
  }
  .play-btn:hover  { opacity: 0.88; }
  .play-btn:active { transform: scale(0.95); }

  /* ── Speed row ── */
  .speed-row {
    display: flex; align-items: center;
    gap: 8px; margin-top: 8px;
    justify-content: center; flex-wrap: wrap;
  }
  .speed-label {
    color:#9ca3af; font-size:0.78rem;
    text-transform:uppercase; letter-spacing:0.1em;
  }
  .speed-btn {
    background: rgba(15,23,42,0.9);
    border: 1px solid rgba(148,163,184,0.25);
    border-radius: 8px; color: #e5e7eb;
    font-size: 0.82rem; padding: 5px 14px;
    cursor: pointer; transition: border-color 0.15s;
    display: flex; align-items: center; gap: 5px;
  }
  .speed-btn.active { border-color:#00d4ff; color:#00d4ff; font-weight:700; }

  /* ── D-pad ── */
  .dpad-wrap {
    margin-top: 14px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .dpad-label {
    color: #9ca3af;
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    margin-bottom: 8px;
  }
  .dpad-label i { margin-right: 5px; }

  .dpad {
    display: grid;
    grid-template-columns: repeat(3, 68px);
    grid-template-rows:    repeat(3, 68px);
    gap: 5px;
  }

  .dpad-btn {
    background: rgba(15,23,42,0.95);
    border: 2px solid rgba(0,212,255,0.35);
    border-radius: 14px;
    color: #00d4ff;
    font-size: 1.4rem;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;
    transition: background 0.1s, transform 0.08s, border-color 0.1s;
    box-shadow: 0 4px 15px rgba(0,0,0,0.4);
  }

  .dpad-btn:active,
  .dpad-btn.pressed {
    background: rgba(0,212,255,0.22);
    border-color: #00d4ff;
    transform: scale(0.90);
    box-shadow: 0 0 18px rgba(0,212,255,0.4);
  }

  .btn-up     { grid-column:2; grid-row:1; }
  .btn-left   { grid-column:1; grid-row:2; }
  .btn-center {
    grid-column:2; grid-row:2;
    background: rgba(255,107,203,0.08);
    border-color: rgba(255,107,203,0.3);
    color: #ff6bcb; font-size: 1rem;
    cursor: default;
  }
  .btn-right  { grid-column:3; grid-row:2; }
  .btn-down   { grid-column:2; grid-row:3; }

  .swipe-hint {
    margin-top: 10px;
    color: rgba(148,163,184,0.5);
    font-size: 0.75rem;
    text-align: center;
    letter-spacing: 0.05em;
  }
  .swipe-hint i { margin-right: 4px; }
</style>
</head>
<body>
<div class="game-wrapper">

  <!-- Scoreboard -->
  <div class="scoreboard">
    <div class="score-card">
      <div class="score-value" id="scoreDisp">0</div>
      <div class="score-label"><i class="fa-solid fa-trophy" style="color:#fde68a;"></i>Score</div>
    </div>
    <div class="score-card">
      <div class="score-value" id="bestDisp">0</div>
      <div class="score-label"><i class="fa-solid fa-medal" style="color:#ff6bcb;"></i>Best</div>
    </div>
    <div class="score-card">
      <div class="score-value" id="lvlDisp">1</div>
      <div class="score-label"><i class="fa-solid fa-layer-group" style="color:#00d4ff;"></i>Level</div>
    </div>
    <div class="score-card">
      <div class="score-value" id="lenDisp">1</div>
      <div class="score-label"><i class="fa-solid fa-ruler" style="color:#34d399;"></i>Length</div>
    </div>
  </div>

  <!-- Canvas -->
  <div class="canvas-wrap" id="canvasWrap">
    <canvas id="gc" width="600" height="500"></canvas>

    <!-- Start Overlay -->
    <div class="overlay" id="startOv">
      <div class="ov-icon">
        <i class="fa-solid fa-worm" style="color:#34d399;"></i>
      </div>
      <div class="ov-title">Snake Game</div>
      <div class="ov-sub">
        <i class="fa-solid fa-keyboard" style="color:#00d4ff;"></i>
        <strong style="color:#00d4ff;">Keyboard:</strong> Arrow / WASD<br/>
        <i class="fa-solid fa-mobile-screen" style="color:#ff6bcb;"></i>
        <strong style="color:#ff6bcb;">Mobile:</strong> Swipe or use D-pad<br/>
        <i class="fa-solid fa-apple-whole" style="color:#ff6bcb;margin-top:4px;display:inline-block;"></i>
        Eat food to grow &nbsp;·&nbsp;
        <i class="fa-solid fa-star" style="color:#fde68a;"></i>
        bonus = 5× points!
      </div>
      <button class="play-btn" id="startBtn">
        <i class="fa-solid fa-play"></i> Play Now
      </button>
    </div>

    <!-- Game Over Overlay -->
    <div class="overlay hidden" id="overOv">
      <div class="ov-icon">
        <i class="fa-solid fa-skull" style="color:#ff6bcb;"></i>
      </div>
      <div class="ov-title">Game Over!</div>
      <div class="ov-sub" id="overMsg"></div>
      <button class="play-btn" id="restartBtn">
        <i class="fa-solid fa-rotate-right"></i> Play Again
      </button>
    </div>
  </div>

  <!-- Speed -->
  <div class="speed-row">
    <span class="speed-label"><i class="fa-solid fa-gauge"></i> Speed:</span>
    <button class="speed-btn active" id="spSlow"   onclick="setSpeed('slow')">
      <i class="fa-solid fa-gauge-simple-low"></i> Slow
    </button>
    <button class="speed-btn"        id="spNormal" onclick="setSpeed('normal')">
      <i class="fa-solid fa-gauge-simple"></i> Normal
    </button>
    <button class="speed-btn"        id="spFast"   onclick="setSpeed('fast')">
      <i class="fa-solid fa-gauge-simple-high"></i> Fast
    </button>
  </div>

  <!-- D-pad -->
  <div class="dpad-wrap">
    <div class="dpad-label">
      <i class="fa-solid fa-mobile-screen-button"></i> Touch Controls
    </div>
    <div class="dpad">
      <button class="dpad-btn btn-up"    id="dUp"    aria-label="Up">
        <i class="fa-solid fa-chevron-up"></i>
      </button>
      <button class="dpad-btn btn-left"  id="dLeft"  aria-label="Left">
        <i class="fa-solid fa-chevron-left"></i>
      </button>
      <div    class="dpad-btn btn-center" aria-hidden="true">
        <i class="fa-solid fa-worm"></i>
      </div>
      <button class="dpad-btn btn-right" id="dRight" aria-label="Right">
        <i class="fa-solid fa-chevron-right"></i>
      </button>
      <button class="dpad-btn btn-down"  id="dDown"  aria-label="Down">
        <i class="fa-solid fa-chevron-down"></i>
      </button>
    </div>
    <div class="swipe-hint">
      <i class="fa-solid fa-hand-pointer"></i>
      Swipe anywhere on the canvas to change direction
    </div>
  </div>

</div>

<script>
// ── Config ────────────────────────────────────────────────────
const COLS = 24, ROWS = 20, CELL = 25;
const SPEEDS = { slow:180, normal:120, fast:65 };

let speed = 'slow', tickMs = SPEEDS.slow;
let snake, dir, nextDir, food, bonus, bonusTick;
let score = 0, highScore = 0, level = 1;
let loop, running = false;
let foodCount = 0;

const canvas = document.getElementById('gc');
const ctx    = canvas.getContext('2d');

// ── Colours ───────────────────────────────────────────────────
const C = {
  bg:     '#020617',
  grid:   'rgba(148,163,184,0.04)',
  head:   '#00d4ff',
  body:   '#0ea5e9',
  food:   '#ff6bcb',
  bonus:  '#fde68a',
  gHead:  'rgba(0,212,255,0.55)',
  gFood:  'rgba(255,107,203,0.4)',
  gBonus: 'rgba(253,230,138,0.45)',
};

// ── Helpers ───────────────────────────────────────────────────
const rnd = n => Math.floor(Math.random() * n);

function freeCell(exclude) {
  let p;
  do { p = { x: rnd(COLS), y: rnd(ROWS) }; }
  while (exclude.some(e => e.x === p.x && e.y === p.y));
  return p;
}

// ── Start / Restart ───────────────────────────────────────────
function startGame() {
  document.getElementById('startOv').classList.add('hidden');
  document.getElementById('overOv').classList.add('hidden');

  snake     = [{x:12,y:10},{x:11,y:10},{x:10,y:10}];
  dir       = {x:1, y:0};
  nextDir   = {x:1, y:0};
  food      = freeCell(snake);
  bonus     = null; bonusTick = 0; foodCount = 0;
  score     = 0; level = 1;
  running   = true;

  updateHUD();
  clearInterval(loop);
  loop = setInterval(tick, tickMs);
}

document.getElementById('startBtn').addEventListener('click', startGame);
document.getElementById('restartBtn').addEventListener('click', startGame);

// ── Speed ─────────────────────────────────────────────────────
function setSpeed(s) {
  speed = s; tickMs = SPEEDS[s];
  ['slow','normal','fast'].forEach(k => {
    const id = 'sp' + k[0].toUpperCase() + k.slice(1);
    document.getElementById(id).classList.toggle('active', k === s);
  });
  if (running) { clearInterval(loop); loop = setInterval(tick, tickMs); }
}

// ── Direction helpers ─────────────────────────────────────────
function go(dx, dy) {
  if (dx !== 0 && dir.x !== 0) return;
  if (dy !== 0 && dir.y !== 0) return;
  nextDir = { x: dx, y: dy };
}

// ── Keyboard ──────────────────────────────────────────────────
document.addEventListener('keydown', e => {
  const m = {
    ArrowUp:[0,-1], ArrowDown:[0,1], ArrowLeft:[-1,0], ArrowRight:[1,0],
    w:[0,-1], s:[0,1], a:[-1,0], d:[1,0],
    W:[0,-1], S:[0,1], A:[-1,0], D:[1,0],
  };
  if (m[e.key]) { e.preventDefault(); go(...m[e.key]); }
});

// ── D-pad ─────────────────────────────────────────────────────
function addDpad(id, dx, dy) {
  const btn = document.getElementById(id);
  btn.addEventListener('touchstart', e => {
    e.preventDefault(); btn.classList.add('pressed'); go(dx, dy);
  }, { passive: false });
  btn.addEventListener('touchend', e => {
    e.preventDefault(); btn.classList.remove('pressed');
  }, { passive: false });
  btn.addEventListener('mousedown', e => {
    e.preventDefault(); btn.classList.add('pressed'); go(dx, dy);
  });
  btn.addEventListener('mouseup',    () => btn.classList.remove('pressed'));
  btn.addEventListener('mouseleave', () => btn.classList.remove('pressed'));
}

addDpad('dUp',    0, -1);
addDpad('dDown',  0,  1);
addDpad('dLeft', -1,  0);
addDpad('dRight', 1,  0);

// ── Swipe on canvas ───────────────────────────────────────────
let swX = null, swY = null;
const wrap = document.getElementById('canvasWrap');

wrap.addEventListener('touchstart', e => {
  const t = e.changedTouches[0];
  swX = t.clientX; swY = t.clientY;
}, { passive: false });

wrap.addEventListener('touchmove', e => {
  e.preventDefault();
}, { passive: false });

wrap.addEventListener('touchend', e => {
  if (swX === null) return;
  const t = e.changedTouches[0];
  const dx = t.clientX - swX;
  const dy = t.clientY - swY;
  if (Math.abs(dx) < 10 && Math.abs(dy) < 10) { swX = swY = null; return; }
  Math.abs(dx) > Math.abs(dy) ? go(dx > 0 ? 1 : -1, 0) : go(0, dy > 0 ? 1 : -1);
  swX = swY = null;
}, { passive: false });

// ── Tick ──────────────────────────────────────────────────────
function tick() {
  dir = { ...nextDir };
  const h = snake[0];
  const n = { x: h.x + dir.x, y: h.y + dir.y };

  if (n.x < 0 || n.x >= COLS || n.y < 0 || n.y >= ROWS) return endGame();
  if (snake.some(s => s.x === n.x && s.y === n.y))       return endGame();

  snake.unshift(n);
  let ate = false;

  if (n.x === food.x && n.y === food.y) {
    score += 10 * level; ate = true; foodCount++;
    food = freeCell(snake);
    if (!bonus && foodCount % 3 === 0) { bonus = freeCell(snake); bonusTick = 25; }
    const nl = Math.floor(score / 60) + 1;
    if (nl > level) {
      level = nl;
      clearInterval(loop);
      loop = setInterval(tick, Math.max(45, tickMs - (level-1)*10));
    }
  }

  if (bonus && n.x === bonus.x && n.y === bonus.y) {
    score += 50 * level; ate = true; bonus = null;
  }

  if (!ate) snake.pop();
  if (bonus) { bonusTick--; if (bonusTick <= 0) bonus = null; }
  if (score > highScore) highScore = score;

  updateHUD();
  draw();
}

// ── End ───────────────────────────────────────────────────────
function endGame() {
  running = false;
  clearInterval(loop);

  const medal =
    score >= 300 ? '<i class="fa-solid fa-trophy" style="color:#fde68a;"></i> Incredible!'    :
    score >= 150 ? '<i class="fa-solid fa-medal"  style="color:#ff6bcb;"></i> Amazing!'        :
    score >= 80  ? '<i class="fa-solid fa-thumbs-up" style="color:#00d4ff;"></i> Good job!'   :
                   '<i class="fa-solid fa-dumbbell" style="color:#9ca3af;"></i> Keep going!';

  const isNew = score > 0 && score >= highScore;

  document.getElementById('overMsg').innerHTML = `
    <strong style="color:#00d4ff;font-size:1.15rem;">
      <i class="fa-solid fa-hashtag" style="font-size:0.9rem;margin-right:3px;"></i>${score} points
    </strong><br/>
    <i class="fa-solid fa-ruler" style="color:#34d399;margin-right:3px;"></i>Length: <strong>${snake.length}</strong>
    &nbsp;·&nbsp;
    <i class="fa-solid fa-layer-group" style="color:#00d4ff;margin-right:3px;"></i>Level: <strong>${level}</strong><br/>
    <span style="margin-top:6px;display:block;">${medal}</span>
    ${isNew ? '<span style="color:#ff6bcb;font-size:0.88rem;margin-top:4px;display:block;"><i class="fa-solid fa-crown" style="margin-right:4px;"></i>New High Score!</span>' : ''}
  `;
  document.getElementById('overOv').classList.remove('hidden');
  draw();
}

// ── HUD ───────────────────────────────────────────────────────
function updateHUD() {
  document.getElementById('scoreDisp').textContent = score;
  document.getElementById('bestDisp').textContent  = highScore;
  document.getElementById('lvlDisp').textContent   = level;
  document.getElementById('lenDisp').textContent   = snake ? snake.length : 1;
}

// ── Draw ──────────────────────────────────────────────────────
function drawRoundRect(x, y, w, h, r, color) {
  ctx.fillStyle = color;
  ctx.beginPath();
  ctx.roundRect(x, y, w, h, r);
  ctx.fill();
}

function draw() {
  ctx.fillStyle = C.bg;
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.strokeStyle = C.grid;
  ctx.lineWidth   = 0.5;
  for (let c = 0; c <= COLS; c++) {
    ctx.beginPath(); ctx.moveTo(c*CELL, 0); ctx.lineTo(c*CELL, canvas.height); ctx.stroke();
  }
  for (let r = 0; r <= ROWS; r++) {
    ctx.beginPath(); ctx.moveTo(0, r*CELL); ctx.lineTo(canvas.width, r*CELL); ctx.stroke();
  }

  if (!snake) return;

  // Food — drawn as a coloured circle with "F" label (canvas can't render FA icons)
  ctx.shadowColor = C.gFood; ctx.shadowBlur = 20;
  ctx.fillStyle = C.food;
  ctx.beginPath();
  ctx.arc(food.x*CELL + CELL/2, food.y*CELL + CELL/2, CELL/2 - 2, 0, Math.PI*2);
  ctx.fill();
  ctx.shadowBlur = 0;
  ctx.fillStyle = '#fff';
  ctx.font = `bold ${CELL - 8}px sans-serif`;
  ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
  ctx.fillText('F', food.x*CELL + CELL/2, food.y*CELL + CELL/2);

  // Bonus
  if (bonus) {
    const pulse = 0.5 + 0.5 * Math.sin(Date.now() / 150);
    ctx.shadowColor = C.gBonus; ctx.shadowBlur = 18 + pulse * 10;
    ctx.fillStyle = C.bonus;
    ctx.beginPath();
    ctx.arc(bonus.x*CELL + CELL/2, bonus.y*CELL + CELL/2, CELL/2 - 2, 0, Math.PI*2);
    ctx.fill();
    ctx.shadowBlur = 0;
    ctx.fillStyle = '#000';
    ctx.font = `bold ${CELL - 8}px sans-serif`;
    ctx.fillText('B', bonus.x*CELL + CELL/2, bonus.y*CELL + CELL/2);

    // Countdown arc
    const pct = bonusTick / 25;
    ctx.strokeStyle = `rgba(253,230,138,${0.3 + pulse * 0.4})`;
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    ctx.arc(bonus.x*CELL + CELL/2, bonus.y*CELL + CELL/2, CELL/2 + 3,
            -Math.PI/2, -Math.PI/2 + pct * Math.PI * 2);
    ctx.stroke();
  }

  // Snake body
  snake.forEach((seg, i) => {
    if (i === 0) return;
    const alpha = Math.max(0.35, 1 - i / snake.length * 0.65);
    ctx.globalAlpha = alpha;
    const green = Math.floor(165 - i / snake.length * 80);
    drawRoundRect(seg.x*CELL+1, seg.y*CELL+1, CELL-2, CELL-2, 4, `rgb(14,${green},233)`);
  });
  ctx.globalAlpha = 1;

  // Head glow
  ctx.shadowColor = C.gHead; ctx.shadowBlur = 22;
  drawRoundRect(snake[0].x*CELL+1, snake[0].y*CELL+1, CELL-2, CELL-2, 6, C.head);
  ctx.shadowBlur = 0;

  drawEyes(snake[0], dir);
}

function drawEyes(h, d) {
  const cx = h.x*CELL + CELL/2;
  const cy = h.y*CELL + CELL/2;
  let e1, e2;
  if      (d.x ===  1) { e1=[cx+5,cy-4]; e2=[cx+5,cy+4]; }
  else if (d.x === -1) { e1=[cx-5,cy-4]; e2=[cx-5,cy+4]; }
  else if (d.y === -1) { e1=[cx-4,cy-5]; e2=[cx+4,cy-5]; }
  else                 { e1=[cx-4,cy+5]; e2=[cx+4,cy+5]; }

  [e1, e2].forEach(([ex, ey]) => {
    ctx.fillStyle = '#fff';
    ctx.beginPath(); ctx.arc(ex, ey, 3, 0, Math.PI*2); ctx.fill();
    ctx.fillStyle = '#000';
    ctx.beginPath(); ctx.arc(ex+d.x, ey+d.y, 1.5, 0, Math.PI*2); ctx.fill();
  });
}

draw(); // initial static frame
</script>
</body>
</html>
""", height=900, scrolling=False)

# ═══════════════════════════════════════════════════════
#                      FOOTER
# ═══════════════════════════════════════════════════════
st.markdown("---")

components.html("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
<div style="
    font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
    display:flex;justify-content:space-between;align-items:center;
    flex-wrap:wrap;gap:0.5rem;padding:0.4rem 0;
">
  <div style="color:#6b7280;font-size:0.82rem;">
    <i class="fa-solid fa-copyright" style="margin-right:4px;"></i>
    2025 <strong style="color:#9ca3af;">Dave Campo</strong>
    <i class="fa-solid fa-circle" style="font-size:0.3rem;margin:0 6px;vertical-align:middle;"></i>
    Built with
    <i class="fa-brands fa-python" style="color:#00d4ff;margin:0 3px;"></i>Python &amp;
    <i class="fa-solid fa-stream" style="color:#ff6bcb;margin:0 3px;"></i>Streamlit
  </div>
</div>
""", height=50)