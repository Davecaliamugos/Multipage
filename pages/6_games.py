import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import streamlit.components.v1 as components
import random
from components import apply_global_effects

st.set_page_config(
    page_title="Games | Dave Campo",
    page_icon="🎮",
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
#                    GLOBAL STYLES
# ═══════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

.stApp {
    background: radial-gradient(ellipse at 0% 0%, #1a2744 0, #020617 45%, #000 100%) !important;
}

/* Hide Streamlit default elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.stDeployButton {display:none;}

/* Button overrides */
.stButton > button {
    background: linear-gradient(135deg, rgba(0,212,255,0.12), rgba(255,107,203,0.12)) !important;
    border: 1px solid rgba(0,212,255,0.4) !important;
    color: #e5e7eb !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    transition: all 0.25s ease !important;
    font-family: 'Inter', sans-serif !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, rgba(0,212,255,0.22), rgba(255,107,203,0.22)) !important;
    border-color: #00d4ff !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 24px rgba(0,212,255,0.2) !important;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #00d4ff, #ff6bcb) !important;
    border: none !important;
    color: #000 !important;
    font-weight: 700 !important;
}
.stButton > button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 28px rgba(0,212,255,0.35) !important;
}

/* Radio buttons */
.stRadio > div {
    background: rgba(15,23,42,0.6) !important;
    border-radius: 12px !important;
    padding: 0.5rem !important;
}
.stRadio label {
    color: #e5e7eb !important;
    font-family: 'Inter', sans-serif !important;
}

/* Divider */
hr {
    border-color: rgba(148,163,184,0.15) !important;
}

/* Game grid cards */
.game-grid-card {
    background: rgba(15,23,42,0.96);
    border: 1px solid rgba(148,163,184,0.2);
    border-radius: 20px;
    padding: 1.8rem 1.4rem;
    text-align: center;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    height: 100%;
    position: relative;
    overflow: hidden;
}
.game-grid-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--accent, #00d4ff), transparent);
    opacity: 0;
    transition: opacity 0.3s ease;
}
.game-grid-card:hover::before { opacity: 1; }
.game-grid-card:hover {
    border-color: var(--accent, #00d4ff);
    box-shadow: 0 0 40px rgba(0,212,255,0.1), 0 20px 60px rgba(0,0,0,0.6);
    transform: translateY(-6px);
}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
#                    SESSION STATE INIT
# ═══════════════════════════════════════════════════════
if "selected_game" not in st.session_state:
    st.session_state.selected_game = None
if "quiz_initialized" not in st.session_state:
    st.session_state.quiz_initialized = False

# ═══════════════════════════════════════════════════════
#                    HERO SECTION
# ═══════════════════════════════════════════════════════
components.html("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
  .hero-wrap {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background: rgba(15,23,42,0.97);
    border-radius: 22px;
    border: 1px solid rgba(148,163,184,0.2);
    padding: 2.4rem 2.4rem 2rem;
    box-shadow: 0 32px 80px rgba(0,0,0,0.9), 0 0 0 1px rgba(0,212,255,0.05);
    backdrop-filter: blur(20px);
    position: relative;
    overflow: hidden;
  }
  .hero-wrap::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(0,212,255,0.08) 0%, transparent 70%);
    pointer-events: none;
  }
  .hero-wrap::after {
    content: '';
    position: absolute;
    bottom: -40px; left: -40px;
    width: 160px; height: 160px;
    background: radial-gradient(circle, rgba(255,107,203,0.06) 0%, transparent 70%);
    pointer-events: none;
  }
  .hero-tag {
    display: inline-flex; align-items: center; gap: 6px;
    font-size: 0.76rem; text-transform: uppercase;
    letter-spacing: 0.22em; color: #00d4ff;
    background: rgba(0,212,255,0.08);
    border: 1px solid rgba(0,212,255,0.2);
    border-radius: 999px; padding: 0.3rem 0.9rem;
    margin-bottom: 1rem;
  }
  .hero-title {
    font-size: 2.8rem; font-weight: 900;
    color: #e5e7eb; margin: 0 0 0.7rem;
    line-height: 1.1;
    display: flex; align-items: center; gap: 12px;
  }
  .hero-icon-wrap {
    width: 52px; height: 52px;
    background: linear-gradient(135deg, rgba(0,212,255,0.15), rgba(255,107,203,0.15));
    border: 1px solid rgba(0,212,255,0.3);
    border-radius: 14px;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
  }
  .hero-sub {
    font-size: 1rem; color: #9ca3af;
    line-height: 1.7; margin: 0;
    max-width: 560px;
  }
  .hero-stats {
    display: flex; gap: 2rem; margin-top: 1.6rem;
    flex-wrap: wrap;
  }
  .hero-stat {
    display: flex; align-items: center; gap: 8px;
  }
  .hero-stat-icon {
    width: 32px; height: 32px;
    background: rgba(0,212,255,0.08);
    border: 1px solid rgba(0,212,255,0.15);
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
  }
  .hero-stat-text { font-size: 0.82rem; color: #9ca3af; }
  .hero-stat-val { font-size: 0.92rem; font-weight: 700; color: #e5e7eb; }
</style>
<div class="hero-wrap">
  <div class="hero-tag">
    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
      <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
    </svg>
    Fun &amp; Interactive
  </div>
  <h1 class="hero-title">
    <div class="hero-icon-wrap">
      <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <line x1="6" y1="12" x2="10" y2="12"/><line x1="8" y1="10" x2="8" y2="14"/>
        <line x1="15" y1="13" x2="15.01" y2="13"/><line x1="18" y1="11" x2="18.01" y2="11"/>
        <rect x="2" y="6" width="20" height="12" rx="2"/>
      </svg>
    </div>
    Mini Games
  </h1>
  <p class="hero-sub">
    Take a break and play! Seven hand-crafted mini-games await — all with full keyboard &amp; mobile touch controls.
  </p>
  
</div>
""", height=290)

st.markdown("<br>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
#                  GAME DEFINITIONS
# ═══════════════════════════════════════════════════════
GAMES = [
    {
        "id": "snake",
        "title": "Snake",
        "tag": "Arcade",
        "desc": "Classic snake! Eat food, grow longer, dodge your own tail.",
        "accent": "#00d4ff",
        "icon": """<svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/>
          <path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/>
          <path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/>
          <path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/>
        </svg>""",
        "controls": "Arrow / WASD / Swipe / D-pad",
        "badge": "Classic",
    },
    {
        "id": "tetris",
        "title": "Tetris",
        "tag": "Puzzle",
        "desc": "Stack tetrominoes, clear lines, and beat your high score!",
        "accent": "#a78bfa",
        "icon": """<svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#a78bfa" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <rect x="2" y="14" width="5" height="5" rx="1"/><rect x="7" y="14" width="5" height="5" rx="1"/>
          <rect x="12" y="14" width="5" height="5" rx="1"/><rect x="7" y="9" width="5" height="5" rx="1"/>
        </svg>""",
        "controls": "Arrow Keys / A·D·S / Swipe / D-pad",
        "badge": "Strategy",
    },
    {
        "id": "breakout",
        "title": "Breakout",
        "tag": "Arcade",
        "desc": "Break all the bricks with your ball and paddle. Don't let it fall!",
        "accent": "#fb923c",
        "icon": """<svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#fb923c" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <rect x="2" y="4" width="20" height="4" rx="1"/>
          <rect x="6" y="10" width="12" height="4" rx="1"/>
          <rect x="9" y="19" width="6" height="2" rx="1"/>
          <circle cx="12" cy="16" r="1.5"/>
        </svg>""",
        "controls": "Mouse / Touch drag / Arrow Keys",
        "badge": "Reflex",
    },
    {
        "id": "memory",
        "title": "Memory Match",
        "tag": "Brain",
        "desc": "Flip cards to find matching pairs. Test your memory!",
        "accent": "#34d399",
        "icon": """<svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#34d399" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <rect x="2" y="3" width="9" height="9" rx="2"/><rect x="13" y="3" width="9" height="9" rx="2"/>
          <rect x="2" y="13" width="9" height="9" rx="2"/><rect x="13" y="13" width="9" height="9" rx="2"/>
        </svg>""",
        "controls": "Click / Tap cards",
        "badge": "Memory",
    },
    {
        "id": "flappy",
        "title": "Flappy Bird",
        "tag": "Endless",
        "desc": "Tap to flap! Navigate through pipes as long as you can.",
        "accent": "#fbbf24",
        "icon": """<svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#fbbf24" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <path d="M17 4c0 1.5-1.5 3-3.5 3C11.5 7 10 5.5 10 4s1.5-3 3.5-3S17 2.5 17 4z"/>
          <path d="M10 7c-2 0-4 1-5 3l-2 4h5l1 4h3l1-4h2l2-4c-1-2-3-3-5-3"/>
          <path d="M8 10l-1 4"/>
        </svg>""",
        "controls": "Space / Click / Tap",
        "badge": "Endless",
    },
    {
        "id": "whack",
        "title": "Whack-a-Mole",
        "tag": "Reflex",
        "desc": "Whack the moles as fast as you can before they hide!",
        "accent": "#f472b6",
        "icon": """<svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#f472b6" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="8" r="5"/>
          <path d="M3 21a9 9 0 0 1 18 0"/>
          <line x1="12" y1="13" x2="12" y2="16"/>
          <circle cx="9" cy="7" r="1" fill="#f472b6"/><circle cx="15" cy="7" r="1" fill="#f472b6"/>
        </svg>""",
        "controls": "Click / Tap moles",
        "badge": "Reaction",
    },
    {
        "id": "quiz",
        "title": "Dev Quiz",
        "tag": "Trivia",
        "desc": "5 random programming questions. Test your dev knowledge!",
        "accent": "#fde047",
        "icon": """<svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#fde047" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/>
          <path d="M9 18h6"/><path d="M10 22h4"/>
        </svg>""",
        "controls": "Click / Tap answers",
        "badge": "Knowledge",
    },
]

# ═══════════════════════════════════════════════════════
#                    GAME SELECTION GRID
# ═══════════════════════════════════════════════════════
if st.session_state.selected_game is None:
    components.html("""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@600;700;800&display=swap');
      .sec-head {
        font-family: 'Inter', sans-serif;
        display: flex; align-items: center; gap: 10px;
        margin-bottom: 0.4rem;
      }
      .sec-head h2 { font-size: 1.35rem; font-weight: 800; color: #e5e7eb; margin: 0; }
      .sec-head p { font-size: 0.85rem; color: #9ca3af; margin: 0; }
    </style>
    <div class="sec-head">
      <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <line x1="6" y1="12" x2="10" y2="12"/><line x1="8" y1="10" x2="8" y2="14"/>
        <line x1="15" y1="13" x2="15.01" y2="13"/><line x1="18" y1="11" x2="18.01" y2="11"/>
        <rect x="2" y="6" width="20" height="12" rx="2"/>
      </svg>
      <div>
        <h2>Choose Your Game</h2>
        <p>Click any card to launch — all games support keyboard &amp; touch</p>
      </div>
    </div>
    """, height=65)

    # Build game cards in rows of 3 + 1 last row
    rows = [GAMES[:3], GAMES[3:6], GAMES[6:]]
    
    for row in rows:
        if not row:
            continue
        cols = st.columns(len(row))
        for col, game in zip(cols, row):
            with col:
                components.html(f"""
                <style>
                  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
                  .gc {{
                    font-family: 'Inter', -apple-system, sans-serif;
                    background: rgba(15,23,42,0.97);
                    border: 1px solid rgba(148,163,184,0.18);
                    border-radius: 20px;
                    padding: 1.6rem 1.2rem 1.4rem;
                    text-align: center;
                    position: relative;
                    overflow: hidden;
                    min-height: 210px;
                  }}
                  .gc-glow {{
                    position: absolute; top: -1px; left: 0; right: 0; height: 2px;
                    background: linear-gradient(90deg, transparent, {game['accent']}, transparent);
                  }}
                  .gc-bg {{
                    position: absolute; top: -30px; right: -30px;
                    width: 100px; height: 100px;
                    background: radial-gradient(circle, {game['accent']}18 0%, transparent 70%);
                    pointer-events: none;
                  }}
                  .gc-badge {{
                    display: inline-flex; align-items: center;
                    background: {game['accent']}18;
                    border: 1px solid {game['accent']}40;
                    border-radius: 999px;
                    padding: 0.2rem 0.7rem;
                    font-size: 0.68rem; font-weight: 700;
                    color: {game['accent']};
                    text-transform: uppercase; letter-spacing: 0.1em;
                    margin-bottom: 0.9rem;
                  }}
                  .gc-icon {{
                    width: 64px; height: 64px;
                    background: {game['accent']}12;
                    border: 1px solid {game['accent']}25;
                    border-radius: 18px;
                    display: flex; align-items: center; justify-content: center;
                    margin: 0 auto 0.9rem;
                  }}
                  .gc-title {{
                    font-size: 1.2rem; font-weight: 800;
                    color: #e5e7eb; margin-bottom: 0.4rem;
                  }}
                  .gc-desc {{
                    font-size: 0.82rem; color: #9ca3af;
                    line-height: 1.55; margin-bottom: 0.9rem;
                  }}
                  .gc-ctrl {{
                    display: inline-flex; align-items: center; gap: 5px;
                    font-size: 0.72rem; color: #6b7280;
                  }}
                </style>
                <div class="gc">
                  <div class="gc-glow"></div>
                  <div class="gc-bg"></div>
                  <div class="gc-badge">{game['badge']}</div>
                  <div class="gc-icon">{game['icon']}</div>
                  <div class="gc-title">{game['title']}</div>
                  <div class="gc-desc">{game['desc']}</div>
                  <div class="gc-ctrl">
                    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <line x1="6" y1="12" x2="10" y2="12"/><line x1="8" y1="10" x2="8" y2="14"/>
                      <line x1="15" y1="13" x2="15.01" y2="13"/><line x1="18" y1="11" x2="18.01" y2="11"/>
                      <rect x="2" y="6" width="20" height="12" rx="2"/>
                    </svg>
                    {game['controls']}
                  </div>
                </div>
                """, height=240)
                
                if st.button(f"▶  Play {game['title']}", key=f"play_{game['id']}", use_container_width=True):
                    st.session_state.selected_game = game['id']
                    st.session_state.quiz_initialized = False
                    st.rerun()

# ═══════════════════════════════════════════════════════
#                    BACK BUTTON
# ═══════════════════════════════════════════════════════
if st.session_state.selected_game:
    col_back, col_title = st.columns([1, 4])
    with col_back:
        if st.button("← Back to Games", key="back_btn"):
            st.session_state.selected_game = None
            for k in ["quiz_finished","quiz_index","quiz_score","quiz_answers","quiz_submitted","quiz_initialized"]:
                if k in st.session_state:
                    del st.session_state[k]
            st.rerun()
    st.markdown("---")

# ═══════════════════════════════════════════════════════
#                    SNAKE GAME
# ═══════════════════════════════════════════════════════
if st.session_state.selected_game == "snake":
    components.html("""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
      .gh { font-family: 'Inter', sans-serif; }
      .gh-tag { font-size:0.76rem; text-transform:uppercase; letter-spacing:0.2em; color:#ff6bcb; }
      .gh-title { font-size:1.9rem; font-weight:900; color:#e5e7eb; margin:0.3rem 0 0.4rem; display:flex; align-items:center; gap:10px; }
      .gh-icon { width:42px; height:42px; background:rgba(0,212,255,0.12); border:1px solid rgba(0,212,255,0.25); border-radius:12px; display:flex; align-items:center; justify-content:center; }
      .gh-sub { color:#9ca3af; font-size:0.92rem; margin:0; }
      .ctrl-chip { display:inline-flex; align-items:center; gap:5px; background:rgba(0,212,255,0.08); border:1px solid rgba(0,212,255,0.2); border-radius:999px; padding:0.25rem 0.75rem; font-size:0.75rem; color:#00d4ff; margin-right:6px; }
    </style>
    <div class="gh">
      <div class="gh-tag">Arcade · Classic</div>
      <div class="gh-title">
        <div class="gh-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/>
            <path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/>
          </svg>
        </div>
        Snake
      </div>
      <p class="gh-sub">
        <span class="ctrl-chip">
          <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
          </svg>
          Keyboard: Arrow / WASD
        </span>
        <span class="ctrl-chip">
          <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/>
          </svg>
          Mobile: Swipe / D-pad
        </span>
      </p>
    </div>
    """, height=120)

    components.html("""
    <!DOCTYPE html><html lang="en"><head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=no"/>
    <style>
      *{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent;}
      body{background:transparent;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
           display:flex;flex-direction:column;align-items:center;padding:0 4px;overscroll-behavior:none;}
      .gw{width:100%;max-width:640px;}
      .scoreboard{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:10px;}
      .sc{background:rgba(15,23,42,0.97);border:1px solid rgba(148,163,184,0.18);border-radius:12px;padding:10px 6px;text-align:center;}
      .sv{font-size:1.6rem;font-weight:900;background:linear-gradient(135deg,#00d4ff,#ff6bcb);-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1;}
      .sl{font-size:0.63rem;text-transform:uppercase;letter-spacing:0.12em;color:#9ca3af;margin-top:3px;}
      .cwrap{position:relative;border-radius:16px;overflow:hidden;border:2px solid rgba(0,212,255,0.3);
             box-shadow:0 0 40px rgba(0,212,255,0.1),0 24px 60px rgba(0,0,0,0.9);touch-action:none;}
      canvas{display:block;width:100%;height:auto;}
      .ov{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;
          background:rgba(2,6,23,0.93);backdrop-filter:blur(10px);border-radius:14px;text-align:center;padding:1.5rem;}
      .ov-icon{width:72px;height:72px;background:rgba(0,212,255,0.1);border:1px solid rgba(0,212,255,0.25);
               border-radius:20px;display:flex;align-items:center;justify-content:center;margin:0 auto 1rem;}
      .ov-title{font-size:1.7rem;font-weight:900;color:#e5e7eb;margin-bottom:0.5rem;}
      .ov-sub{font-size:0.88rem;color:#9ca3af;line-height:1.6;max-width:300px;}
      .pbtn{margin-top:1.2rem;padding:0.75rem 2rem;font-size:1rem;font-weight:700;color:#000;
            background:linear-gradient(135deg,#00d4ff,#ff6bcb);border:none;border-radius:999px;
            cursor:pointer;box-shadow:0 8px 24px rgba(0,212,255,0.3);transition:transform 0.15s,box-shadow 0.15s;
            display:flex;align-items:center;gap:8px;}
      .pbtn:hover{transform:scale(1.05);box-shadow:0 12px 32px rgba(0,212,255,0.4);}
      .hidden{display:none!important;}
      .speed-row{display:flex;align-items:center;justify-content:center;gap:8px;margin-top:12px;flex-wrap:wrap;}
      .slbl{font-size:0.73rem;color:#9ca3af;text-transform:uppercase;letter-spacing:0.1em;}
      .sbtn{padding:0.4rem 1rem;font-size:0.78rem;font-weight:600;background:rgba(15,23,42,0.8);
            border:1px solid rgba(148,163,184,0.25);border-radius:999px;color:#9ca3af;cursor:pointer;
            transition:all 0.15s;display:inline-flex;align-items:center;gap:5px;}
      .sbtn.active{border-color:#00d4ff;color:#00d4ff;background:rgba(0,212,255,0.1);}
      /* D-PAD */
      .dpad-section{margin-top:14px;text-align:center;}
      .dpad-lbl{font-size:0.7rem;color:#9ca3af;margin-bottom:8px;text-transform:uppercase;
                letter-spacing:0.1em;display:flex;align-items:center;justify-content:center;gap:6px;}
      .dpad{display:inline-grid;grid-template-columns:52px 52px 52px;grid-template-rows:52px 52px;gap:6px;}
      .db{width:52px;height:52px;border-radius:14px;border:1px solid rgba(148,163,184,0.25);
          background:rgba(15,23,42,0.9);color:#e5e7eb;font-size:1.2rem;
          display:flex;align-items:center;justify-content:center;cursor:pointer;
          box-shadow:0 4px 12px rgba(0,0,0,0.4);transition:all 0.1s;user-select:none;}
      .db:active,.db.pressed{transform:scale(0.93);background:rgba(0,212,255,0.15);border-color:#00d4ff;box-shadow:0 0 12px rgba(0,212,255,0.25);}
      .db-up{grid-column:2;grid-row:1;}
      .db-left{grid-column:1;grid-row:2;}
      .db-center{grid-column:2;grid-row:2;opacity:0.35;}
      .db-right{grid-column:3;grid-row:2;}
      /* Row 3 for down */
      .dpad{grid-template-rows:52px 52px 52px;}
      .db-down{grid-column:2;grid-row:3;}
      .swipe-hint{font-size:0.68rem;color:#4b5563;margin-top:8px;}
    </style>
    </head><body>
    <div class="gw">
      <div class="scoreboard">
        <div class="sc"><div class="sv" id="scoreD">0</div><div class="sl">Score</div></div>
        <div class="sc"><div class="sv" id="bestD" style="-webkit-text-fill-color:#34d399;color:#34d399">0</div><div class="sl">Best</div></div>
        <div class="sc"><div class="sv" id="lvlD" style="font-size:1.3rem;">1</div><div class="sl">Level</div></div>
        <div class="sc"><div class="sv" id="lenD" style="font-size:1.3rem;">1</div><div class="sl">Length</div></div>
      </div>
      <div class="cwrap" id="cwrap">
        <canvas id="gc" width="600" height="480"></canvas>
        <div class="ov" id="startOv">
          <div class="ov-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
              <path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/>
              <path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/>
            </svg>
          </div>
          <div class="ov-title">Snake</div>
          <div class="ov-sub">Eat food to grow · Avoid walls &amp; yourself<br/>Bonus stars give 5× points!</div>
          <button class="pbtn" id="startBtn">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>
            Play Now
          </button>
        </div>
        <div class="ov hidden" id="overOv">
          <div class="ov-icon" style="background:rgba(255,107,203,0.1);border-color:rgba(255,107,203,0.3);">
            <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#ff6bcb" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"/>
              <path d="M16 16s-1.5-2-4-2-4 2-4 2"/>
              <line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/>
            </svg>
          </div>
          <div class="ov-title">Game Over</div>
          <div class="ov-sub" id="overMsg"></div>
          <button class="pbtn" id="restartBtn">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 12a9 9 0 0 0-9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/>
              <path d="M3 12a9 9 0 0 0 9 9 9.75 9.75 0 0 0 6.74-2.74L21 16"/><path d="M16 21h5v-5"/>
            </svg>
            Play Again
          </button>
        </div>
      </div>
      <div class="speed-row">
        <span class="slbl">Speed:</span>
        <button class="sbtn active" id="spSlow" onclick="setSpeed('slow')">
          <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>Slow
        </button>
        <button class="sbtn" id="spNormal" onclick="setSpeed('normal')">
          <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/>
            <path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/>
          </svg>Normal
        </button>
        <button class="sbtn" id="spFast" onclick="setSpeed('fast')">
          <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>Fast
        </button>
      </div>
      <div class="dpad-section">
        <div class="dpad-lbl">
          <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#9ca3af" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="5" y="2" width="14" height="20" rx="2"/><line x1="12" y1="18" x2="12.01" y2="18"/>
          </svg>
          Touch Controls
        </div>
        <div class="dpad">
          <button class="db db-up" id="dUp" aria-label="Up">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"/></svg>
          </button>
          <button class="db db-left" id="dLeft" aria-label="Left">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
          </button>
          <div class="db db-center" aria-hidden="true">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="6" y1="12" x2="10" y2="12"/><line x1="8" y1="10" x2="8" y2="14"/>
              <line x1="15" y1="13" x2="15.01" y2="13"/><line x1="18" y1="11" x2="18.01" y2="11"/>
              <rect x="2" y="6" width="20" height="12" rx="2"/>
            </svg>
          </div>
          <button class="db db-right" id="dRight" aria-label="Right">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>
          </button>
          <button class="db db-down" id="dDown" aria-label="Down">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
        </div>
        <div class="swipe-hint">Swipe on canvas · Arrow keys · WASD</div>
      </div>
    </div>
    <script>
    const COLS=24,ROWS=20,CELL=25;
    const SPEEDS={slow:180,normal:120,fast:65};
    let sp='slow',tickMs=SPEEDS.slow,snake,dir,nextDir,food,bonus,bonusTick,score=0,hi=0,lv=1,loop,running=false;
    const cv=document.getElementById('gc'),ctx=cv.getContext('2d');
    function setSpeed(s){sp=s;tickMs=SPEEDS[s];document.querySelectorAll('.sbtn').forEach(b=>b.classList.remove('active'));document.getElementById('sp'+s[0].toUpperCase()+s.slice(1)).classList.add('active');if(running){clearInterval(loop);loop=setInterval(tick,tickMs);}}
    function rand(n){return Math.floor(Math.random()*n);}
    function hit(p){return snake.some(s=>s.x===p.x&&s.y===p.y);}
    function placeFood(){do{food={x:rand(COLS),y:rand(ROWS)};}while(hit(food));bonus=null;bonusTick=0;}
    function reset(){snake=[{x:4,y:10},{x:3,y:10},{x:2,y:10}];dir={x:1,y:0};nextDir={x:1,y:0};score=0;lv=1;tickMs=SPEEDS[sp];placeFood();hud();}
    function hud(){document.getElementById('scoreD').textContent=score;document.getElementById('bestD').textContent=hi;document.getElementById('lvlD').textContent=lv;document.getElementById('lenD').textContent=snake?snake.length:1;}
    function start(){if(running)return;reset();running=true;document.getElementById('startOv').classList.add('hidden');document.getElementById('overOv').classList.add('hidden');loop=setInterval(tick,tickMs);}
    function tick(){
      dir=nextDir;
      const h={x:snake[0].x+dir.x,y:snake[0].y+dir.y};
      if(h.x<0||h.x>=COLS||h.y<0||h.y>=ROWS||snake.some(s=>s.x===h.x&&s.y===h.y)){end();return;}
      snake.unshift(h);
      let ate=false;
      if(h.x===food.x&&h.y===food.y){score+=10;ate=true;placeFood();if(snake.length%5===0)lvUp();}
      else if(bonus&&h.x===bonus.x&&h.y===bonus.y){score+=50;ate=true;bonus=null;bonusTick=0;}
      if(!ate)snake.pop();
      if(!bonus&&++bonusTick>30&&Math.random()<0.3){bonus={x:rand(COLS),y:rand(ROWS),life:20};}
      if(bonus){if(--bonus.life<=0)bonus=null;if(bonus&&hit(bonus))bonus=null;}
      if(score>hi)hi=score;
      hud();draw();
    }
    function lvUp(){lv++;tickMs=Math.max(45,tickMs-8);clearInterval(loop);loop=setInterval(tick,tickMs);}
    function end(){
      running=false;clearInterval(loop);
      const r=score>=300?'Incredible! Top tier!':score>=150?'Amazing work!':score>=80?'Good job!':'Keep grinding!';
      document.getElementById('overMsg').innerHTML=`<strong style="color:#00d4ff;font-size:1.2rem;">${score} pts</strong><br>Length <strong>${snake.length}</strong> · Level <strong>${lv}</strong><br><span style="color:#fde68a;margin-top:6px;display:block;">${r}</span>`;
      document.getElementById('overOv').classList.remove('hidden');draw();
    }
    function draw(){
      ctx.fillStyle='#020617';ctx.fillRect(0,0,cv.width,cv.height);
      ctx.strokeStyle='rgba(148,163,184,0.04)';ctx.lineWidth=0.5;
      for(let c=0;c<=COLS;c++){ctx.beginPath();ctx.moveTo(c*CELL,0);ctx.lineTo(c*CELL,cv.height);ctx.stroke();}
      for(let r=0;r<=ROWS;r++){ctx.beginPath();ctx.moveTo(0,r*CELL);ctx.lineTo(cv.width,r*CELL);ctx.stroke();}
      // glow head
      const g=ctx.createRadialGradient(snake[0].x*CELL+CELL/2,snake[0].y*CELL+CELL/2,0,snake[0].x*CELL+CELL/2,snake[0].y*CELL+CELL/2,CELL*1.2);
      g.addColorStop(0,'rgba(0,212,255,0.4)');g.addColorStop(1,'transparent');
      ctx.fillStyle=g;ctx.beginPath();ctx.arc(snake[0].x*CELL+CELL/2,snake[0].y*CELL+CELL/2,CELL*1.2,0,Math.PI*2);ctx.fill();
      // head
      ctx.fillStyle='#00d4ff';ctx.beginPath();ctx.roundRect(snake[0].x*CELL+1,snake[0].y*CELL+1,CELL-2,CELL-2,6);ctx.fill();
      // body gradient
      for(let i=1;i<snake.length;i++){
        const t=1-i/snake.length;
        ctx.fillStyle=`rgba(14,165,233,${0.3+t*0.7})`;
        ctx.beginPath();ctx.roundRect(snake[i].x*CELL+1,snake[i].y*CELL+1,CELL-2,CELL-2,5);ctx.fill();
      }
      // food glow
      const fg=ctx.createRadialGradient(food.x*CELL+CELL/2,food.y*CELL+CELL/2,0,food.x*CELL+CELL/2,food.y*CELL+CELL/2,CELL);
      fg.addColorStop(0,'rgba(255,107,203,0.5)');fg.addColorStop(1,'transparent');
      ctx.fillStyle=fg;ctx.beginPath();ctx.arc(food.x*CELL+CELL/2,food.y*CELL+CELL/2,CELL,0,Math.PI*2);ctx.fill();
      ctx.fillStyle='#ff6bcb';ctx.beginPath();ctx.arc(food.x*CELL+CELL/2,food.y*CELL+CELL/2,CELL*0.38,0,Math.PI*2);ctx.fill();
      if(bonus){
        const bg2=ctx.createRadialGradient(bonus.x*CELL+CELL/2,bonus.y*CELL+CELL/2,0,bonus.x*CELL+CELL/2,bonus.y*CELL+CELL/2,CELL);
        bg2.addColorStop(0,'rgba(253,230,138,0.5)');bg2.addColorStop(1,'transparent');
        ctx.fillStyle=bg2;ctx.beginPath();ctx.arc(bonus.x*CELL+CELL/2,bonus.y*CELL+CELL/2,CELL,0,Math.PI*2);ctx.fill();
        ctx.fillStyle='#fde047';ctx.beginPath();ctx.arc(bonus.x*CELL+CELL/2,bonus.y*CELL+CELL/2,CELL*0.42,0,Math.PI*2);ctx.fill();
        ctx.fillStyle='#000';ctx.font='bold 13px sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';
        ctx.fillText('★',bonus.x*CELL+CELL/2,bonus.y*CELL+CELL/2+1);
      }
    }
    document.addEventListener('keydown',e=>{
      if(['ArrowUp','w','W'].includes(e.key)){e.preventDefault();if(dir.y===0)nextDir={x:0,y:-1};}
      else if(['ArrowDown','s','S'].includes(e.key)){e.preventDefault();if(dir.y===0)nextDir={x:0,y:1};}
      else if(['ArrowLeft','a','A'].includes(e.key)){e.preventDefault();if(dir.x===0)nextDir={x:-1,y:0};}
      else if(['ArrowRight','d','D'].includes(e.key)){e.preventDefault();if(dir.x===0)nextDir={x:1,y:0};}
    });
    const dmap={Up:{x:0,y:-1},Down:{x:0,y:1},Left:{x:-1,y:0},Right:{x:1,y:0}};
    ['Up','Down','Left','Right'].forEach(k=>{
      const btn=document.getElementById('d'+k);
      ['touchstart','mousedown'].forEach(ev=>btn.addEventListener(ev,e=>{
        e.preventDefault();const nd=dmap[k];
        if(nd.x!==-dir.x||nd.y!==-dir.y)nextDir=nd;
        btn.classList.add('pressed');setTimeout(()=>btn.classList.remove('pressed'),150);
      },{passive:false}));
    });
    let sx=0,sy=0;
    const cw=document.getElementById('cwrap');
    cw.addEventListener('touchstart',e=>{sx=e.touches[0].clientX;sy=e.touches[0].clientY;},{passive:true});
    cw.addEventListener('touchend',e=>{
      const dx=e.changedTouches[0].clientX-sx,dy=e.changedTouches[0].clientY-sy;
      if(Math.abs(dx)>25||Math.abs(dy)>25){
        if(Math.abs(dx)>Math.abs(dy)){const nd={x:dx>0?1:-1,y:0};if(nd.x!==-dir.x)nextDir=nd;}
        else{const nd={x:0,y:dy>0?1:-1};if(nd.y!==-dir.y)nextDir=nd;}
      }
    },{passive:true});
    document.getElementById('startBtn').addEventListener('click',start);
    document.getElementById('restartBtn').addEventListener('click',start);
    reset();draw();
    </script>
    </body></html>
    """, height=640)

# ═══════════════════════════════════════════════════════
#                    TETRIS GAME
# ═══════════════════════════════════════════════════════
if st.session_state.selected_game == "tetris":
    components.html("""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
      .gh{font-family:'Inter',sans-serif;}
      .gh-tag{font-size:0.76rem;text-transform:uppercase;letter-spacing:0.2em;color:#a78bfa;}
      .gh-title{font-size:1.9rem;font-weight:900;color:#e5e7eb;margin:0.3rem 0 0.4rem;display:flex;align-items:center;gap:10px;}
      .gh-icon{width:42px;height:42px;background:rgba(167,139,250,0.12);border:1px solid rgba(167,139,250,0.25);border-radius:12px;display:flex;align-items:center;justify-content:center;}
      .ctrl-chip{display:inline-flex;align-items:center;gap:5px;background:rgba(167,139,250,0.08);border:1px solid rgba(167,139,250,0.2);border-radius:999px;padding:0.25rem 0.75rem;font-size:0.75rem;color:#a78bfa;margin-right:6px;}
    </style>
    <div class="gh">
      <div class="gh-tag">Puzzle · Strategy</div>
      <div class="gh-title">
        <div class="gh-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#a78bfa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="14" width="5" height="5" rx="1"/><rect x="7" y="14" width="5" height="5" rx="1"/>
            <rect x="12" y="14" width="5" height="5" rx="1"/><rect x="7" y="9" width="5" height="5" rx="1"/>
          </svg>
        </div>
        Tetris
      </div>
      <p style="color:#9ca3af;font-size:0.92rem;margin:0;">
        <span class="ctrl-chip">
          <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
          ← → Move · ↑ Rotate · ↓ Soft Drop · Space Hard Drop
        </span>
        <span class="ctrl-chip">
          <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2"/></svg>
          D-pad + Rotate button
        </span>
      </p>
    </div>
    """, height=120)

    components.html("""
    <!DOCTYPE html><html lang="en"><head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=no"/>
    <style>
      *{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent;}
      body{background:transparent;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
           display:flex;flex-direction:column;align-items:center;padding:0 4px;overscroll-behavior:none;}
      .gw{width:100%;max-width:640px;}
      .layout{display:flex;gap:12px;align-items:flex-start;}
      .left-panel{flex:none;}
      .right-panel{flex:1;min-width:0;}
      .scoreboard{display:flex;flex-direction:column;gap:8px;width:120px;}
      .sc{background:rgba(15,23,42,0.97);border:1px solid rgba(148,163,184,0.18);border-radius:12px;padding:10px 8px;text-align:center;}
      .sv{font-size:1.4rem;font-weight:900;background:linear-gradient(135deg,#a78bfa,#00d4ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1;}
      .sl{font-size:0.6rem;text-transform:uppercase;letter-spacing:0.1em;color:#9ca3af;margin-top:3px;}
      .next-label{font-size:0.65rem;text-transform:uppercase;letter-spacing:0.1em;color:#9ca3af;margin-bottom:6px;text-align:center;}
      .next-cv{background:rgba(15,23,42,0.97);border:1px solid rgba(148,163,184,0.18);border-radius:10px;display:block;margin:0 auto;}
      .cwrap{position:relative;border-radius:14px;overflow:hidden;border:2px solid rgba(167,139,250,0.35);
             box-shadow:0 0 40px rgba(167,139,250,0.1),0 24px 60px rgba(0,0,0,0.9);}
      canvas#tc{display:block;width:100%;height:auto;}
      .ov{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;
          background:rgba(2,6,23,0.93);backdrop-filter:blur(10px);border-radius:12px;text-align:center;padding:1.5rem;}
      .ov-icon{width:68px;height:68px;background:rgba(167,139,250,0.1);border:1px solid rgba(167,139,250,0.3);
               border-radius:18px;display:flex;align-items:center;justify-content:center;margin:0 auto 1rem;}
      .ov-title{font-size:1.7rem;font-weight:900;color:#e5e7eb;margin-bottom:0.5rem;}
      .ov-sub{font-size:0.88rem;color:#9ca3af;line-height:1.6;max-width:280px;}
      .pbtn{margin-top:1.2rem;padding:0.75rem 2rem;font-size:1rem;font-weight:700;color:#000;
            background:linear-gradient(135deg,#a78bfa,#00d4ff);border:none;border-radius:999px;
            cursor:pointer;box-shadow:0 8px 24px rgba(167,139,250,0.3);transition:transform 0.15s;
            display:flex;align-items:center;gap:8px;}
      .pbtn:hover{transform:scale(1.05);}
      .hidden{display:none!important;}
      /* D-PAD for Tetris */
      .dpad-section{margin-top:14px;text-align:center;}
      .dpad-lbl{font-size:0.68rem;color:#9ca3af;margin-bottom:8px;text-transform:uppercase;
                letter-spacing:0.1em;display:flex;align-items:center;justify-content:center;gap:6px;}
      .tdpad{display:inline-grid;grid-template-columns:52px 52px 52px 52px;grid-template-rows:52px 52px;gap:6px;}
      .db{width:52px;height:52px;border-radius:14px;border:1px solid rgba(148,163,184,0.22);
          background:rgba(15,23,42,0.9);color:#e5e7eb;
          display:flex;align-items:center;justify-content:center;cursor:pointer;
          box-shadow:0 4px 12px rgba(0,0,0,0.4);transition:all 0.1s;user-select:none;font-size:1.2rem;}
      .db:active,.db.pressed{transform:scale(0.93);background:rgba(167,139,250,0.15);border-color:#a78bfa;}
      .db-rotate{background:rgba(167,139,250,0.08);border-color:rgba(167,139,250,0.35);color:#a78bfa;}
      .db-hard{background:rgba(0,212,255,0.08);border-color:rgba(0,212,255,0.35);color:#00d4ff;font-size:0.7rem;font-weight:700;}
    </style>
    </head><body>
    <div class="gw">
      <div class="layout">
        <div class="left-panel">
          <div class="scoreboard">
            <div class="sc"><div class="sv" id="tScore">0</div><div class="sl">Score</div></div>
            <div class="sc"><div class="sv" id="tLines" style="font-size:1.2rem;">0</div><div class="sl">Lines</div></div>
            <div class="sc"><div class="sv" id="tLevel" style="font-size:1.2rem;">1</div><div class="sl">Level</div></div>
            <div style="margin-top:4px;">
              <div class="next-label">Next</div>
              <canvas id="nc" class="next-cv" width="80" height="80"></canvas>
            </div>
          </div>
        </div>
        <div class="right-panel">
          <div class="cwrap">
            <canvas id="tc" width="200" height="400"></canvas>
            <div class="ov" id="tStart">
              <div class="ov-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#a78bfa" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="2" y="14" width="5" height="5" rx="1"/><rect x="7" y="14" width="5" height="5" rx="1"/>
                  <rect x="12" y="14" width="5" height="5" rx="1"/><rect x="7" y="9" width="5" height="5" rx="1"/>
                </svg>
              </div>
              <div class="ov-title">Tetris</div>
              <div class="ov-sub">Stack tetrominoes · Clear lines · Beat your score!</div>
              <button class="pbtn" id="tStartBtn">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>
                Play Now
              </button>
            </div>
            <div class="ov hidden" id="tOver">
              <div class="ov-icon" style="background:rgba(255,107,203,0.1);border-color:rgba(255,107,203,0.3);">
                <svg xmlns="http://www.w3.org/2000/svg" width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#ff6bcb" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"/>
                  <path d="M16 16s-1.5-2-4-2-4 2-4 2"/>
                  <line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/>
                </svg>
              </div>
              <div class="ov-title">Game Over</div>
              <div class="ov-sub" id="tMsg"></div>
              <button class="pbtn" id="tRestart">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M21 12a9 9 0 0 0-9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/>
                  <path d="M3 12a9 9 0 0 0 9 9 9.75 9.75 0 0 0 6.74-2.74L21 16"/><path d="M16 21h5v-5"/>
                </svg>
                Play Again
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="dpad-section">
        <div class="dpad-lbl">
          <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#9ca3af" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="5" y="2" width="14" height="20" rx="2"/><line x1="12" y1="18" x2="12.01" y2="18"/>
          </svg>
          Touch Controls
        </div>
        <div class="tdpad">
          <button class="db db-rotate" id="tRotate" title="Rotate">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 12a9 9 0 0 0-9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/>
            </svg>
          </button>
          <button class="db" id="tLeft" aria-label="Left">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
          </button>
          <button class="db" id="tRight" aria-label="Right">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>
          </button>
          <button class="db db-hard" id="tHard" title="Hard Drop">DROP</button>
          <div></div>
          <button class="db" id="tDown" aria-label="Soft Drop">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div></div><div></div>
        </div>
        <div style="font-size:0.68rem;color:#4b5563;margin-top:8px;">Arrow keys · Space=Hard drop · ↑=Rotate</div>
      </div>
    </div>
    <script>
    const COLS=10,ROWS=20,CS=20;
    const PIECES=[
      {s:[[1,1,1,1]],c:'#00d4ff'},
      {s:[[1,0],[1,0],[1,1]],c:'#fb923c'},
      {s:[[0,1],[0,1],[1,1]],c:'#a78bfa'},
      {s:[[1,1],[1,1]],c:'#fde047'},
      {s:[[0,1,1],[1,1,0]],c:'#34d399'},
      {s:[[1,1,0],[0,1,1]],c:'#f472b6'},
      {s:[[1,1,1],[0,1,0]],c:'#60a5fa'},
    ];
    const cv=document.getElementById('tc'),ctx=cv.getContext('2d');
    const nc=document.getElementById('nc'),nctx=nc.getContext('2d');
    let board,cur,curX,curY,next,score,lines,level,speed,loop,running=false;
    function newBoard(){board=Array.from({length:ROWS},()=>Array(COLS).fill(0));}
    function randPiece(){return JSON.parse(JSON.stringify(PIECES[Math.floor(Math.random()*PIECES.length)]));}
    function reset(){
      newBoard();score=0;lines=0;level=1;speed=800;
      cur=randPiece();next=randPiece();
      curX=Math.floor(COLS/2)-Math.floor(cur.s[0].length/2);curY=0;
      hud();
    }
    function hud(){document.getElementById('tScore').textContent=score;document.getElementById('tLines').textContent=lines;document.getElementById('tLevel').textContent=level;}
    function fits(p,ox,oy){return p.s.every((r,ri)=>r.every((v,ci)=>!v||((oy+ri>=0)&&oy+ri<ROWS&&ox+ci>=0&&ox+ci<COLS&&!board[oy+ri][ox+ci])));}
    function place(){cur.s.forEach((r,ri)=>r.forEach((v,ci)=>{if(v)board[curY+ri][curX+ci]=cur.c;}));}
    function clearLines(){
      let c=0;
      for(let r=ROWS-1;r>=0;){
        if(board[r].every(v=>v)){board.splice(r,1);board.unshift(Array(COLS).fill(0));c++;}
        else r--;
      }
      if(c){lines+=c;score+=[0,100,300,500,800][c]*level;if(lines%10===0){level++;speed=Math.max(100,speed-80);clearInterval(loop);loop=setInterval(drop,speed);}}
    }
    function rotate(p){const r={s:p.s[0].map((_,i)=>p.s.map(r=>r[i]).reverse()),c:p.c};return r;}
    function drop(){
      if(fits(cur,curX,curY+1)){curY++;}
      else{
        place();clearLines();
        cur=next;next=randPiece();
        curX=Math.floor(COLS/2)-Math.floor(cur.s[0].length/2);curY=0;
        if(!fits(cur,curX,curY)){endGame();return;}
      }
      hud();draw();
    }
    function hardDrop(){while(fits(cur,curX,curY+1))curY++;drop();}
    function endGame(){running=false;clearInterval(loop);document.getElementById('tMsg').innerHTML=`<strong style="color:#a78bfa;font-size:1.1rem;">${score} pts</strong><br>Lines: <strong>${lines}</strong> · Level: <strong>${level}</strong>`;document.getElementById('tOver').classList.remove('hidden');}
    function ghostY(){let gy=curY;while(fits(cur,curX,gy+1))gy++;return gy;}
    function draw(){
      ctx.fillStyle='#020617';ctx.fillRect(0,0,cv.width,cv.height);
      // grid
      ctx.strokeStyle='rgba(148,163,184,0.05)';ctx.lineWidth=0.5;
      for(let c=0;c<=COLS;c++){ctx.beginPath();ctx.moveTo(c*CS,0);ctx.lineTo(c*CS,cv.height);ctx.stroke();}
      for(let r=0;r<=ROWS;r++){ctx.beginPath();ctx.moveTo(0,r*CS);ctx.lineTo(cv.width,r*CS);ctx.stroke();}
      // board
      board.forEach((row,ri)=>row.forEach((v,ci)=>{if(v){ctx.fillStyle=v;ctx.beginPath();ctx.roundRect(ci*CS+1,ri*CS+1,CS-2,CS-2,3);ctx.fill();ctx.fillStyle='rgba(255,255,255,0.15)';ctx.beginPath();ctx.roundRect(ci*CS+1,ri*CS+1,CS-2,4,3);ctx.fill();}}));
      // ghost
      const gy=ghostY();
      cur.s.forEach((r,ri)=>r.forEach((v,ci)=>{if(v){ctx.fillStyle='rgba(255,255,255,0.08)';ctx.beginPath();ctx.roundRect((curX+ci)*CS+1,(gy+ri)*CS+1,CS-2,CS-2,3);ctx.fill();}}));
      // current
      cur.s.forEach((r,ri)=>r.forEach((v,ci)=>{if(v){ctx.fillStyle=cur.c;ctx.beginPath();ctx.roundRect((curX+ci)*CS+1,(curY+ri)*CS+1,CS-2,CS-2,3);ctx.fill();ctx.fillStyle='rgba(255,255,255,0.2)';ctx.beginPath();ctx.roundRect((curX+ci)*CS+1,(curY+ri)*CS+1,CS-2,4,3);ctx.fill();}}));
      // next preview
      nctx.fillStyle='rgba(15,23,42,0.97)';nctx.fillRect(0,0,nc.width,nc.height);
      const ps=4,ox=Math.floor((nc.width/ps-next.s[0].length)/2)*ps,oy=Math.floor((nc.height/ps-next.s.length)/2)*ps;
      next.s.forEach((r,ri)=>r.forEach((v,ci)=>{if(v){nctx.fillStyle=next.c;nctx.beginPath();nctx.roundRect(ox+ci*ps+0.5,oy+ri*ps+0.5,ps-1,ps-1,1);nctx.fill();}}));
    }
    function start(){if(running)return;reset();running=true;document.getElementById('tStart').classList.add('hidden');document.getElementById('tOver').classList.add('hidden');loop=setInterval(drop,speed);}
    document.addEventListener('keydown',e=>{
      if(!running)return;
      if(e.key==='ArrowLeft'){if(fits(cur,curX-1,curY))curX--;}
      else if(e.key==='ArrowRight'){if(fits(cur,curX+1,curY))curX++;}
      else if(e.key==='ArrowDown'){drop();}
      else if(e.key==='ArrowUp'||e.key==='w'||e.key==='W'){const r=rotate(cur);if(fits(r,curX,curY))cur=r;}
      else if(e.key===' '){e.preventDefault();hardDrop();return;}
      else return;
      e.preventDefault();draw();
    });
    function dbtn(id,fn){const b=document.getElementById(id);['touchstart','mousedown'].forEach(ev=>b.addEventListener(ev,e=>{e.preventDefault();if(running)fn();b.classList.add('pressed');setTimeout(()=>b.classList.remove('pressed'),150);},{passive:false}));}
    dbtn('tLeft',()=>{if(fits(cur,curX-1,curY)){curX--;draw();}});
    dbtn('tRight',()=>{if(fits(cur,curX+1,curY)){curX++;draw();}});
    dbtn('tDown',()=>drop());
    dbtn('tRotate',()=>{const r=rotate(cur);if(fits(r,curX,curY)){cur=r;draw();}});
    dbtn('tHard',()=>hardDrop());
    let tsx=0,tsy=0;
    cv.addEventListener('touchstart',e=>{tsx=e.touches[0].clientX;tsy=e.touches[0].clientY;},{passive:true});
    cv.addEventListener('touchend',e=>{
      const dx=e.changedTouches[0].clientX-tsx,dy=e.changedTouches[0].clientY-tsy;
      if(!running)return;
      if(Math.abs(dx)<10&&Math.abs(dy)<10){const r=rotate(cur);if(fits(r,curX,curY)){cur=r;draw();}}
      else if(Math.abs(dx)>Math.abs(dy)){if(fits(cur,curX+(dx>0?1:-1),curY)){curX+=(dx>0?1:-1);draw();}}
      else if(dy>0)drop();
      else{const r=rotate(cur);if(fits(r,curX,curY)){cur=r;draw();}}
    },{passive:true});
    document.getElementById('tStartBtn').addEventListener('click',start);
    document.getElementById('tRestart').addEventListener('click',start);
    reset();draw();
    </script>
    </body></html>
    """, height=640)

# ═══════════════════════════════════════════════════════
#                    BREAKOUT GAME
# ═══════════════════════════════════════════════════════
if st.session_state.selected_game == "breakout":
    components.html("""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
      .gh{font-family:'Inter',sans-serif;}
      .gh-tag{font-size:0.76rem;text-transform:uppercase;letter-spacing:0.2em;color:#fb923c;}
      .gh-title{font-size:1.9rem;font-weight:900;color:#e5e7eb;margin:0.3rem 0 0.4rem;display:flex;align-items:center;gap:10px;}
      .gh-icon{width:42px;height:42px;background:rgba(251,146,60,0.12);border:1px solid rgba(251,146,60,0.25);border-radius:12px;display:flex;align-items:center;justify-content:center;}
      .ctrl-chip{display:inline-flex;align-items:center;gap:5px;background:rgba(251,146,60,0.08);border:1px solid rgba(251,146,60,0.2);border-radius:999px;padding:0.25rem 0.75rem;font-size:0.75rem;color:#fb923c;margin-right:6px;}
    </style>
    <div class="gh">
      <div class="gh-tag">Arcade · Reflex</div>
      <div class="gh-title">
        <div class="gh-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#fb923c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="4" width="20" height="4" rx="1"/><rect x="6" y="10" width="12" height="3" rx="1"/>
            <rect x="9" y="20" width="6" height="2" rx="1"/><circle cx="12" cy="17" r="1.5"/>
          </svg>
        </div>
        Breakout
      </div>
      <p style="color:#9ca3af;font-size:0.92rem;margin:0;">
        <span class="ctrl-chip">
          <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
          Mouse / Arrow Keys
        </span>
        <span class="ctrl-chip">
          <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2"/></svg>
          Drag / ← → buttons
        </span>
      </p>
    </div>
    """, height=120)

    components.html("""
    <!DOCTYPE html><html lang="en"><head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=no"/>
    <style>
      *{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent;}
      body{background:transparent;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
           display:flex;flex-direction:column;align-items:center;padding:0 4px;overscroll-behavior:none;}
      .gw{width:100%;max-width:640px;}
      .scoreboard{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:10px;}
      .sc{background:rgba(15,23,42,0.97);border:1px solid rgba(148,163,184,0.18);border-radius:12px;padding:10px 6px;text-align:center;}
      .sv{font-size:1.5rem;font-weight:900;background:linear-gradient(135deg,#fb923c,#fde047);-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1;}
      .sl{font-size:0.62rem;text-transform:uppercase;letter-spacing:0.1em;color:#9ca3af;margin-top:3px;}
      .cwrap{position:relative;border-radius:16px;overflow:hidden;border:2px solid rgba(251,146,60,0.35);
             box-shadow:0 0 40px rgba(251,146,60,0.1),0 24px 60px rgba(0,0,0,0.9);touch-action:none;cursor:none;}
      canvas{display:block;width:100%;height:auto;}
      .ov{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;
          background:rgba(2,6,23,0.93);backdrop-filter:blur(10px);border-radius:14px;text-align:center;padding:1.5rem;}
      .ov-icon{width:68px;height:68px;background:rgba(251,146,60,0.1);border:1px solid rgba(251,146,60,0.3);
               border-radius:18px;display:flex;align-items:center;justify-content:center;margin:0 auto 1rem;}
      .ov-title{font-size:1.7rem;font-weight:900;color:#e5e7eb;margin-bottom:0.5rem;}
      .ov-sub{font-size:0.88rem;color:#9ca3af;line-height:1.6;max-width:280px;}
      .pbtn{margin-top:1.2rem;padding:0.75rem 2rem;font-size:1rem;font-weight:700;color:#000;
            background:linear-gradient(135deg,#fb923c,#fde047);border:none;border-radius:999px;
            cursor:pointer;box-shadow:0 8px 24px rgba(251,146,60,0.35);transition:transform 0.15s;
            display:flex;align-items:center;gap:8px;}
      .pbtn:hover{transform:scale(1.05);}
      .hidden{display:none!important;}
      .ctrl-row{display:flex;align-items:center;justify-content:center;gap:10px;margin-top:12px;}
      .cb{width:72px;height:56px;border-radius:14px;border:1px solid rgba(251,146,60,0.3);
          background:rgba(15,23,42,0.9);color:#fb923c;display:flex;align-items:center;justify-content:center;
          cursor:pointer;box-shadow:0 4px 12px rgba(0,0,0,0.4);transition:all 0.1s;user-select:none;font-size:1.3rem;}
      .cb:active,.cb.pressed{transform:scale(0.93);background:rgba(251,146,60,0.15);}
    </style>
    </head><body>
    <div class="gw">
      <div class="scoreboard">
        <div class="sc"><div class="sv" id="bScore">0</div><div class="sl">Score</div></div>
        <div class="sc"><div class="sv" id="bLives" style="-webkit-text-fill-color:#f472b6;color:#f472b6;">3</div><div class="sl">Lives</div></div>
        <div class="sc"><div class="sv" id="bLevel" style="font-size:1.2rem;">1</div><div class="sl">Level</div></div>
      </div>
      <div class="cwrap" id="bcwrap">
        <canvas id="bc" width="480" height="420"></canvas>
        <div class="ov" id="bStart">
          <div class="ov-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#fb923c" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
              <rect x="2" y="4" width="20" height="4" rx="1"/><rect x="6" y="10" width="12" height="3" rx="1"/>
              <rect x="9" y="20" width="6" height="2" rx="1"/><circle cx="12" cy="17" r="1.5"/>
            </svg>
          </div>
          <div class="ov-title">Breakout</div>
          <div class="ov-sub">Move the paddle to bounce the ball and break all bricks!</div>
          <button class="pbtn" id="bStartBtn">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>
            Play Now
          </button>
        </div>
        <div class="ov hidden" id="bOver">
          <div class="ov-icon" style="background:rgba(255,107,203,0.1);border-color:rgba(255,107,203,0.3);">
            <svg xmlns="http://www.w3.org/2000/svg" width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#ff6bcb" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"/>
              <path d="M16 16s-1.5-2-4-2-4 2-4 2"/>
              <line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/>
            </svg>
          </div>
          <div class="ov-title" id="bOverTitle">Game Over</div>
          <div class="ov-sub" id="bMsg"></div>
          <button class="pbtn" id="bRestart" style="background:linear-gradient(135deg,#fb923c,#fde047);">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 12a9 9 0 0 0-9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/>
              <path d="M3 12a9 9 0 0 0 9 9 9.75 9.75 0 0 0 6.74-2.74L21 16"/><path d="M16 21h5v-5"/>
            </svg>
            Play Again
          </button>
        </div>
        <div class="ov hidden" id="bWin">
          <div class="ov-icon" style="background:rgba(52,211,153,0.1);border-color:rgba(52,211,153,0.3);">
            <svg xmlns="http://www.w3.org/2000/svg" width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#34d399" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
              <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/>
              <path d="M4 22h16"/><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"/>
              <path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"/>
              <path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"/>
            </svg>
          </div>
          <div class="ov-title">You Win!</div>
          <div class="ov-sub" id="bWinMsg"></div>
          <button class="pbtn" id="bNextLevel" style="background:linear-gradient(135deg,#34d399,#00d4ff);">
            Next Level
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>
          </button>
        </div>
      </div>
      <div class="ctrl-row">
        <button class="cb" id="bLeft" aria-label="Move Left">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
        </button>
        <div style="font-size:0.7rem;color:#6b7280;text-align:center;">Move<br>Paddle</div>
        <button class="cb" id="bRight" aria-label="Move Right">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>
        </button>
      </div>
    </div>
    <script>
    const cv=document.getElementById('bc'),ctx=cv.getContext('2d');
    const W=cv.width,H=cv.height;
    const ROWS_B=5,COLS_B=10,BPAD=4;
    const BCOLORS=['#ff6bcb','#fb923c','#fde047','#34d399','#00d4ff','#a78bfa'];
    let paddle,ball,bricks,score,lives,level,running=false,raf=null;
    let keys={left:false,right:false};
    let mouseX=-1,touchX=-1;
    function makeBricks(){
      bricks=[];
      for(let r=0;r<ROWS_B;r++)for(let c=0;c<COLS_B;c++){
        const bw=(W-BPAD*(COLS_B+1))/COLS_B;
        bricks.push({x:BPAD+c*(bw+BPAD),y:40+r*(18+BPAD),w:bw,h:18,color:BCOLORS[r%BCOLORS.length],hp:2,alive:true});
      }
    }
    function reset(keepLevel=false){
      if(!keepLevel){score=0;lives=3;level=1;}
      const bw=90,ph=12,spd=3.5+level*0.4;
      paddle={x:W/2-bw/2,y:H-30,w:bw,h:ph,speed:7};
      ball={x:W/2,y:H-50,r:7,vx:spd*(Math.random()>0.5?1:-1),vy:-spd};
      makeBricks();hud();
    }
    function hud(){document.getElementById('bScore').textContent=score;document.getElementById('bLives').textContent=lives;document.getElementById('bLevel').textContent=level;}
    function start(keepLevel=false){
      if(running)return;reset(keepLevel);running=true;
      ['bStart','bOver','bWin'].forEach(id=>document.getElementById(id).classList.add('hidden'));
      if(raf)cancelAnimationFrame(raf);gameLoop();
    }
    function gameLoop(){
      if(!running)return;
      update();draw();raf=requestAnimationFrame(gameLoop);
    }
    function update(){
      // paddle movement
      if(keys.left)paddle.x-=paddle.speed;
      if(keys.right)paddle.x+=paddle.speed;
      if(mouseX>0)paddle.x=mouseX-paddle.w/2;
      if(touchX>0)paddle.x=touchX-paddle.w/2;
      paddle.x=Math.max(0,Math.min(W-paddle.w,paddle.x));
      // ball
      ball.x+=ball.vx;ball.y+=ball.vy;
      if(ball.x-ball.r<0){ball.x=ball.r;ball.vx*=-1;}
      if(ball.x+ball.r>W){ball.x=W-ball.r;ball.vx*=-1;}
      if(ball.y-ball.r<0){ball.y=ball.r;ball.vy*=-1;}
      if(ball.y+ball.r>H){lives--;hud();if(lives<=0){endGame();}else{ball.x=W/2;ball.y=H-50;ball.vx=(3.5+level*0.4)*(Math.random()>0.5?1:-1);ball.vy=-(3.5+level*0.4);}return;}
      // paddle
      if(ball.y+ball.r>=paddle.y&&ball.y+ball.r<=paddle.y+paddle.h&&ball.x>=paddle.x&&ball.x<=paddle.x+paddle.w){
        ball.vy=Math.abs(ball.vy)*-1;
        const hit=(ball.x-(paddle.x+paddle.w/2))/(paddle.w/2);
        ball.vx=(4+level*0.4)*hit;
        ball.y=paddle.y-ball.r;
      }
      // bricks
      let alive=0;
      bricks.forEach(b=>{
        if(!b.alive)return;alive++;
        if(ball.x+ball.r>b.x&&ball.x-ball.r<b.x+b.w&&ball.y+ball.r>b.y&&ball.y-ball.r<b.y+b.h){
          b.hp--;if(b.hp<=0){b.alive=false;score+=10*level;}
          else score+=5*level;
          const ox=Math.min(ball.x+ball.r-b.x,b.x+b.w-(ball.x-ball.r));
          const oy=Math.min(ball.y+ball.r-b.y,b.y+b.h-(ball.y-ball.r));
          if(ox<oy)ball.vx*=-1;else ball.vy*=-1;
          hud();
        }
      });
      if(alive===0)winLevel();
    }
    function endGame(){running=false;cancelAnimationFrame(raf);document.getElementById('bMsg').innerHTML=`<strong style="color:#fb923c;font-size:1.1rem;">${score} pts</strong><br>Level <strong>${level}</strong>`;document.getElementById('bOver').classList.remove('hidden');}
    function winLevel(){running=false;cancelAnimationFrame(raf);level++;document.getElementById('bWinMsg').innerHTML=`<strong style="color:#34d399;font-size:1.1rem;">${score} pts</strong><br>Moving to Level <strong>${level}</strong>!`;document.getElementById('bWin').classList.remove('hidden');}
    function draw(){
      ctx.fillStyle='#020617';ctx.fillRect(0,0,W,H);
      ctx.strokeStyle='rgba(148,163,184,0.04)';ctx.lineWidth=0.5;
      for(let c=0;c<10;c++){ctx.beginPath();ctx.moveTo(c*W/10,0);ctx.lineTo(c*W/10,H);ctx.stroke();}
      // bricks
      bricks.forEach(b=>{
        if(!b.alive)return;
        const alpha=b.hp===2?1:0.5;
        ctx.globalAlpha=alpha;
        ctx.fillStyle=b.color;ctx.beginPath();ctx.roundRect(b.x,b.y,b.w,b.h,4);ctx.fill();
        ctx.fillStyle='rgba(255,255,255,0.2)';ctx.beginPath();ctx.roundRect(b.x,b.y,b.w,4,4);ctx.fill();
        ctx.globalAlpha=1;
      });
      // paddle glow
      const pg=ctx.createLinearGradient(paddle.x,0,paddle.x+paddle.w,0);
      pg.addColorStop(0,'#fb923c');pg.addColorStop(1,'#fde047');
      ctx.shadowColor='#fb923c';ctx.shadowBlur=15;
      ctx.fillStyle=pg;ctx.beginPath();ctx.roundRect(paddle.x,paddle.y,paddle.w,paddle.h,paddle.h/2);ctx.fill();
      ctx.shadowBlur=0;
      // ball glow
      const bg=ctx.createRadialGradient(ball.x,ball.y,0,ball.x,ball.y,ball.r*2);
      bg.addColorStop(0,'rgba(251,146,60,0.6)');bg.addColorStop(1,'transparent');
      ctx.fillStyle=bg;ctx.beginPath();ctx.arc(ball.x,ball.y,ball.r*2,0,Math.PI*2);ctx.fill();
      ctx.shadowColor='#fb923c';ctx.shadowBlur=12;
      ctx.fillStyle='#fde047';ctx.beginPath();ctx.arc(ball.x,ball.y,ball.r,0,Math.PI*2);ctx.fill();
      ctx.shadowBlur=0;
    }
    document.addEventListener('keydown',e=>{if(e.key==='ArrowLeft')keys.left=true;if(e.key==='ArrowRight')keys.right=true;e.preventDefault();});
    document.addEventListener('keyup',e=>{if(e.key==='ArrowLeft')keys.left=false;if(e.key==='ArrowRight')keys.right=false;});
    const cw=document.getElementById('bcwrap');
    cw.addEventListener('mousemove',e=>{const r=cv.getBoundingClientRect();mouseX=(e.clientX-r.left)*(W/r.width);},{passive:true});
    cw.addEventListener('mouseleave',()=>mouseX=-1);
    cw.addEventListener('touchmove',e=>{e.preventDefault();const r=cv.getBoundingClientRect();touchX=(e.touches[0].clientX-r.left)*(W/r.width);},{passive:false});
    cw.addEventListener('touchend',()=>touchX=-1,{passive:true});
    function dbtn(id,down,up){
      const b=document.getElementById(id);
      b.addEventListener('mousedown',()=>down());b.addEventListener('mouseup',()=>up&&up());b.addEventListener('mouseleave',()=>up&&up());
      b.addEventListener('touchstart',e=>{e.preventDefault();down();b.classList.add('pressed');},{passive:false});
      b.addEventListener('touchend',()=>{up&&up();b.classList.remove('pressed');},{passive:true});
    }
    dbtn('bLeft',()=>keys.left=true,()=>keys.left=false);
    dbtn('bRight',()=>keys.right=true,()=>keys.right=false);
    document.getElementById('bStartBtn').addEventListener('click',()=>start());
    document.getElementById('bRestart').addEventListener('click',()=>start());
    document.getElementById('bNextLevel').addEventListener('click',()=>start(true));
    hud();draw();
    </script>
    </body></html>
    """, height=600)

# ═══════════════════════════════════════════════════════
#                    MEMORY MATCH GAME
# ═══════════════════════════════════════════════════════
if st.session_state.selected_game == "memory":
    components.html("""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
      .gh{font-family:'Inter',sans-serif;}
      .gh-tag{font-size:0.76rem;text-transform:uppercase;letter-spacing:0.2em;color:#34d399;}
      .gh-title{font-size:1.9rem;font-weight:900;color:#e5e7eb;margin:0.3rem 0 0.4rem;display:flex;align-items:center;gap:10px;}
      .gh-icon{width:42px;height:42px;background:rgba(52,211,153,0.12);border:1px solid rgba(52,211,153,0.25);border-radius:12px;display:flex;align-items:center;justify-content:center;}
      .ctrl-chip{display:inline-flex;align-items:center;gap:5px;background:rgba(52,211,153,0.08);border:1px solid rgba(52,211,153,0.2);border-radius:999px;padding:0.25rem 0.75rem;font-size:0.75rem;color:#34d399;margin-right:6px;}
    </style>
    <div class="gh">
      <div class="gh-tag">Brain · Memory</div>
      <div class="gh-title">
        <div class="gh-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#34d399" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="3" width="9" height="9" rx="2"/><rect x="13" y="3" width="9" height="9" rx="2"/>
            <rect x="2" y="13" width="9" height="9" rx="2"/><rect x="13" y="13" width="9" height="9" rx="2"/>
          </svg>
        </div>
        Memory Match
      </div>
      <p style="color:#9ca3af;font-size:0.92rem;margin:0;">
        <span class="ctrl-chip">
          <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
          Click / Tap cards to flip
        </span>
      </p>
    </div>
    """, height=120)

    components.html("""
    <!DOCTYPE html><html lang="en"><head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=no"/>
    <style>
      *{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent;}
      body{background:transparent;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
           display:flex;flex-direction:column;align-items:center;padding:0 4px;}
      .gw{width:100%;max-width:540px;}
      .scoreboard{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:12px;}
      .sc{background:rgba(15,23,42,0.97);border:1px solid rgba(148,163,184,0.18);border-radius:12px;padding:10px 6px;text-align:center;}
      .sv{font-size:1.5rem;font-weight:900;background:linear-gradient(135deg,#34d399,#00d4ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1;}
      .sl{font-size:0.62rem;text-transform:uppercase;letter-spacing:0.1em;color:#9ca3af;margin-top:3px;}
      .grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;}
      .card{aspect-ratio:1;border-radius:12px;cursor:pointer;perspective:800px;transition:transform 0.1s;}
      .card:active{transform:scale(0.95);}
      .card-inner{width:100%;height:100%;position:relative;transform-style:preserve-3d;transition:transform 0.4s cubic-bezier(0.4,0,0.2,1);}
      .card.flipped .card-inner{transform:rotateY(180deg);}
      .card-front,.card-back{position:absolute;inset:0;border-radius:12px;display:flex;align-items:center;justify-content:center;backface-visibility:hidden;}
      .card-front{background:linear-gradient(135deg,rgba(15,23,42,0.97),rgba(30,41,59,0.97));border:1px solid rgba(148,163,184,0.2);font-size:1.8rem;}
      .card-back{background:linear-gradient(135deg,rgba(52,211,153,0.1),rgba(0,212,255,0.1));border:1px solid rgba(52,211,153,0.3);transform:rotateY(180deg);font-size:2rem;}
      .card.matched .card-back{background:linear-gradient(135deg,rgba(52,211,153,0.2),rgba(0,212,255,0.2));border-color:rgba(52,211,153,0.5);box-shadow:0 0 20px rgba(52,211,153,0.2);}
      .card-front svg{opacity:0.3;}
      .win-banner{background:linear-gradient(135deg,rgba(52,211,153,0.12),rgba(0,212,255,0.12));
                  border:1px solid rgba(52,211,153,0.35);border-radius:16px;
                  padding:1.5rem;text-align:center;margin-top:1rem;display:none;}
      .win-banner.show{display:block;}
      .win-title{font-size:1.6rem;font-weight:900;color:#e5e7eb;margin-bottom:0.3rem;}
      .win-sub{font-size:0.9rem;color:#9ca3af;}
      .rbtn{margin-top:1rem;padding:0.65rem 1.5rem;font-size:0.9rem;font-weight:700;
            color:#000;background:linear-gradient(135deg,#34d399,#00d4ff);border:none;
            border-radius:999px;cursor:pointer;box-shadow:0 8px 20px rgba(52,211,153,0.25);
            transition:transform 0.15s;display:inline-flex;align-items:center;gap:6px;}
      .rbtn:hover{transform:scale(1.05);}
    </style>
    </head><body>
    <div class="gw">
      <div class="scoreboard">
        <div class="sc"><div class="sv" id="mMoves">0</div><div class="sl">Moves</div></div>
        <div class="sc"><div class="sv" id="mMatches" style="-webkit-text-fill-color:#34d399;color:#34d399;">0/8</div><div class="sl">Matched</div></div>
        <div class="sc"><div class="sv" id="mTime" style="font-size:1.1rem;">0:00</div><div class="sl">Time</div></div>
      </div>
      <div class="grid" id="mgrid"></div>
      <div class="win-banner" id="winBanner">
        <div style="width:56px;height:56px;background:rgba(52,211,153,0.15);border:1px solid rgba(52,211,153,0.35);border-radius:16px;display:flex;align-items:center;justify-content:center;margin:0 auto 0.8rem;">
          <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#34d399" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/>
            <path d="M4 22h16"/><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"/>
            <path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"/>
            <path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"/>
          </svg>
        </div>
        <div class="win-title">Congratulations!</div>
        <div class="win-sub" id="winMsg"></div>
        <button class="rbtn" onclick="startGame()">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 12a9 9 0 0 0-9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/>
            <path d="M3 12a9 9 0 0 0 9 9 9.75 9.75 0 0 0 6.74-2.74L21 16"/><path d="M16 21h5v-5"/>
          </svg>
          Play Again
        </button>
      </div>
    </div>
    <script>
    const ICONS=[
      `<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2v20"/><path d="M2 12h20"/></svg>`,
      `<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#ff6bcb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>`,
      `<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#34d399" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/></svg>`,
      `<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#fde047" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>`,
      `<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#a78bfa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg>`,
      `<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#fb923c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>`,
      `<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#f472b6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>`,
      `<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#60a5fa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>`,
    ];
    const BACK_ICON=`<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="rgba(148,163,184,0.4)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="6" y1="12" x2="10" y2="12"/><line x1="8" y1="10" x2="8" y2="14"/><line x1="15" y1="13" x2="15.01" y2="13"/><line x1="18" y1="11" x2="18.01" y2="11"/><rect x="2" y="6" width="20" height="12" rx="2"/></svg>`;
    let cards=[],flipped=[],matched=0,moves=0,lock=false,timerInt=null,secs=0,started=false;
    function pad(n){return String(n).padStart(2,'0');}
    function fmtTime(s){return`${Math.floor(s/60)}:${pad(s%60)}`;}
    function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
    function startGame(){
      cards=shuffle([...ICONS,...ICONS].map((icon,i)=>({id:i,icon,flipped:false,matched:false})));
      flipped=[];matched=0;moves=0;lock=false;secs=0;started=false;
      clearInterval(timerInt);
      document.getElementById('mMoves').textContent=0;
      document.getElementById('mMatches').textContent='0/8';
      document.getElementById('mTime').textContent='0:00';
      document.getElementById('winBanner').classList.remove('show');
      renderGrid();
    }
    function renderGrid(){
      const g=document.getElementById('mgrid');g.innerHTML='';
      cards.forEach((c,i)=>{
        const el=document.createElement('div');
        el.className='card'+(c.flipped||c.matched?' flipped':'');
        if(c.matched)el.classList.add('matched');
        el.innerHTML=`<div class="card-inner"><div class="card-front">${BACK_ICON}</div><div class="card-back">${c.icon}</div></div>`;
        el.addEventListener('click',()=>flip(i));
        g.appendChild(el);
      });
    }
    function flip(i){
      if(lock||cards[i].flipped||cards[i].matched)return;
      if(!started){started=true;timerInt=setInterval(()=>{secs++;document.getElementById('mTime').textContent=fmtTime(secs);},1000);}
      cards[i].flipped=true;flipped.push(i);renderGrid();
      if(flipped.length===2){
        moves++;document.getElementById('mMoves').textContent=moves;lock=true;
        const [a,b]=flipped;
        if(cards[a].icon===cards[b].icon){cards[a].matched=cards[b].matched=true;matched++;document.getElementById('mMatches').textContent=`${matched}/8`;flipped=[];lock=false;renderGrid();if(matched===8)win();}
        else{setTimeout(()=>{cards[a].flipped=cards[b].flipped=false;flipped=[];lock=false;renderGrid();},900);}
      }
    }
    function win(){clearInterval(timerInt);const t=fmtTime(secs);const r=moves<=20?'Perfect memory!':moves<=30?'Great job!':'Keep practising!';document.getElementById('winMsg').innerHTML=`Finished in <strong style="color:#00d4ff;">${moves} moves</strong> · <strong style="color:#34d399;">${t}</strong><br><span style="color:#fde047;margin-top:4px;display:block;">${r}</span>`;document.getElementById('winBanner').classList.add('show');}
    startGame();
    </script>
    </body></html>
    """, height=600)

# ═══════════════════════════════════════════════════════
#                    FLAPPY BIRD GAME
# ═══════════════════════════════════════════════════════
if st.session_state.selected_game == "flappy":
    components.html("""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
      .gh{font-family:'Inter',sans-serif;}
      .gh-tag{font-size:0.76rem;text-transform:uppercase;letter-spacing:0.2em;color:#fbbf24;}
      .gh-title{font-size:1.9rem;font-weight:900;color:#e5e7eb;margin:0.3rem 0 0.4rem;display:flex;align-items:center;gap:10px;}
      .gh-icon{width:42px;height:42px;background:rgba(251,191,36,0.12);border:1px solid rgba(251,191,36,0.25);border-radius:12px;display:flex;align-items:center;justify-content:center;}
      .ctrl-chip{display:inline-flex;align-items:center;gap:5px;background:rgba(251,191,36,0.08);border:1px solid rgba(251,191,36,0.2);border-radius:999px;padding:0.25rem 0.75rem;font-size:0.75rem;color:#fbbf24;margin-right:6px;}
    </style>
    <div class="gh">
      <div class="gh-tag">Endless · Reflex</div>
      <div class="gh-title">
        <div class="gh-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#fbbf24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M17 4c0 1.5-1.5 3-3.5 3C11.5 7 10 5.5 10 4s1.5-3 3.5-3S17 2.5 17 4z"/>
            <path d="M10 7c-2 0-4 1-5 3l-2 4h5l1 4h3l1-4h2l2-4c-1-2-3-3-5-3"/>
          </svg>
        </div>
        Flappy Bird
      </div>
      <p style="color:#9ca3af;font-size:0.92rem;margin:0;">
        <span class="ctrl-chip">
          <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
          Space / Click
        </span>
        <span class="ctrl-chip">
          <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2"/></svg>
          Tap screen / Flap button
        </span>
      </p>
    </div>
    """, height=120)

    components.html("""
    <!DOCTYPE html><html lang="en"><head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=no"/>
    <style>
      *{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent;}
      body{background:transparent;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
           display:flex;flex-direction:column;align-items:center;padding:0 4px;}
      .gw{width:100%;max-width:400px;}
      .scoreboard{display:grid;grid-template-columns:repeat(2,1fr);gap:8px;margin-bottom:10px;}
      .sc{background:rgba(15,23,42,0.97);border:1px solid rgba(148,163,184,0.18);border-radius:12px;padding:10px 6px;text-align:center;}
      .sv{font-size:1.6rem;font-weight:900;background:linear-gradient(135deg,#fbbf24,#fb923c);-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1;}
      .sl{font-size:0.62rem;text-transform:uppercase;letter-spacing:0.1em;color:#9ca3af;margin-top:3px;}
      .cwrap{position:relative;border-radius:16px;overflow:hidden;border:2px solid rgba(251,191,36,0.35);
             box-shadow:0 0 40px rgba(251,191,36,0.1),0 24px 60px rgba(0,0,0,0.9);touch-action:none;cursor:pointer;}
      canvas{display:block;width:100%;height:auto;}
      .ov{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;
          background:rgba(2,6,23,0.93);backdrop-filter:blur(10px);border-radius:14px;text-align:center;padding:1.5rem;}
      .ov-icon{width:68px;height:68px;background:rgba(251,191,36,0.1);border:1px solid rgba(251,191,36,0.3);
               border-radius:18px;display:flex;align-items:center;justify-content:center;margin:0 auto 1rem;}
      .ov-title{font-size:1.7rem;font-weight:900;color:#e5e7eb;margin-bottom:0.5rem;}
      .ov-sub{font-size:0.88rem;color:#9ca3af;line-height:1.6;}
      .pbtn{margin-top:1.2rem;padding:0.75rem 2rem;font-size:1rem;font-weight:700;color:#000;
            background:linear-gradient(135deg,#fbbf24,#fb923c);border:none;border-radius:999px;
            cursor:pointer;box-shadow:0 8px 24px rgba(251,191,36,0.3);transition:transform 0.15s;
            display:flex;align-items:center;gap:8px;}
      .pbtn:hover{transform:scale(1.05);}
      .hidden{display:none!important;}
      .flap-btn{width:100%;margin-top:12px;padding:1rem;font-size:1.1rem;font-weight:700;
                background:linear-gradient(135deg,rgba(251,191,36,0.15),rgba(251,146,60,0.15));
                border:2px solid rgba(251,191,36,0.4);border-radius:16px;color:#fbbf24;
                cursor:pointer;transition:all 0.1s;display:flex;align-items:center;justify-content:center;gap:8px;
                user-select:none;}
      .flap-btn:active{transform:scale(0.97);background:rgba(251,191,36,0.25);}
    </style>
    </head><body>
    <div class="gw">
      <div class="scoreboard">
        <div class="sc"><div class="sv" id="fScore">0</div><div class="sl">Score</div></div>
        <div class="sc"><div class="sv" id="fBest" style="-webkit-text-fill-color:#34d399;color:#34d399;">0</div><div class="sl">Best</div></div>
      </div>
      <div class="cwrap" id="fcwrap">
        <canvas id="fc" width="320" height="480"></canvas>
        <div class="ov" id="fStart">
          <div class="ov-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#fbbf24" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
              <path d="M17 4c0 1.5-1.5 3-3.5 3C11.5 7 10 5.5 10 4s1.5-3 3.5-3S17 2.5 17 4z"/>
              <path d="M10 7c-2 0-4 1-5 3l-2 4h5l1 4h3l1-4h2l2-4c-1-2-3-3-5-3"/>
            </svg>
          </div>
          <div class="ov-title">Flappy Bird</div>
          <div class="ov-sub">Tap · Click · or Press Space<br>to flap your wings!</div>
          <button class="pbtn" id="fStartBtn">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>
            Fly Now
          </button>
        </div>
        <div class="ov hidden" id="fOver">
          <div class="ov-icon" style="background:rgba(255,107,203,0.1);border-color:rgba(255,107,203,0.3);">
            <svg xmlns="http://www.w3.org/2000/svg" width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#ff6bcb" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"/>
              <path d="M16 16s-1.5-2-4-2-4 2-4 2"/>
              <line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/>
            </svg>
          </div>
          <div class="ov-title">Crashed!</div>
          <div class="ov-sub" id="fMsg"></div>
          <button class="pbtn" id="fRestart">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 12a9 9 0 0 0-9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/>
              <path d="M3 12a9 9 0 0 0 9 9 9.75 9.75 0 0 0 6.74-2.74L21 16"/><path d="M16 21h5v-5"/>
            </svg>
            Try Again
          </button>
        </div>
      </div>
      <button class="flap-btn" id="flapBtn">
        <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="18 15 12 9 6 15"/>
        </svg>
        FLAP!
      </button>
    </div>
    <script>
    const cv=document.getElementById('fc'),ctx=cv.getContext('2d');
    const W=cv.width,H=cv.height;
    let bird,pipes,score,best=0,raf=null,running=false,frame=0;
    const GAP=140,PW=52,SPEED=2.4,GRAVITY=0.45,FLAP=-8.5;
    function reset(){bird={x:80,y:H/2,v:0,r:18,angle:0};pipes=[];score=0;frame=0;hud();}
    function hud(){document.getElementById('fScore').textContent=score;document.getElementById('fBest').textContent=best;}
    function flap(){if(!running)return;bird.v=FLAP;}
    function start(){if(running)return;reset();running=true;['fStart','fOver'].forEach(id=>document.getElementById(id).classList.add('hidden'));if(raf)cancelAnimationFrame(raf);loop();}
    function loop(){if(!running)return;update();draw();raf=requestAnimationFrame(loop);}
    function update(){
      bird.v+=GRAVITY;bird.y+=bird.v;bird.angle=Math.min(Math.PI/4,Math.max(-Math.PI/4,bird.v*0.06));
      frame++;if(frame%90===0){const top=60+Math.random()*(H-GAP-120);pipes.push({x:W,top,bottom:top+GAP,scored:false});}
      pipes.forEach(p=>{p.x-=SPEED;if(!p.scored&&p.x+PW<bird.x){p.scored=true;score++;if(score>best)best=score;hud();}});
      pipes=pipes.filter(p=>p.x+PW>0);
      if(bird.y-bird.r<0||bird.y+bird.r>H)endGame();
      pipes.forEach(p=>{if(bird.x+bird.r>p.x&&bird.x-bird.r<p.x+PW&&(bird.y-bird.r<p.top||bird.y+bird.r>p.bottom))endGame();});
    }
    function endGame(){running=false;cancelAnimationFrame(raf);document.getElementById('fMsg').innerHTML=`<strong style="color:#fbbf24;font-size:1.2rem;">${score} pipes</strong><br>${score>=20?'Legendary!':score>=10?'Amazing!':score>=5?'Getting there!':'Try again!'}`;document.getElementById('fOver').classList.remove('hidden');}
    function draw(){
      // sky
      const sky=ctx.createLinearGradient(0,0,0,H);
      sky.addColorStop(0,'#020617');sky.addColorStop(1,'#0f172a');
      ctx.fillStyle=sky;ctx.fillRect(0,0,W,H);
      // stars
      if(frame%2===0){ctx.fillStyle='rgba(255,255,255,0.6)';for(let i=0;i<3;i++){ctx.beginPath();ctx.arc(Math.random()*W,Math.random()*H*0.6,1,0,Math.PI*2);ctx.fill();}}
      // pipes
      pipes.forEach(p=>{
        const pg=ctx.createLinearGradient(p.x,0,p.x+PW,0);
        pg.addColorStop(0,'#34d399');pg.addColorStop(1,'#059669');
        ctx.fillStyle=pg;
        ctx.beginPath();ctx.roundRect(p.x,0,PW,p.top,4);ctx.fill();
        ctx.beginPath();ctx.roundRect(p.x,p.bottom,PW,H-p.bottom,4);ctx.fill();
        // pipe caps
        ctx.fillStyle='#10b981';
        ctx.beginPath();ctx.roundRect(p.x-4,p.top-14,PW+8,14,4);ctx.fill();
        ctx.beginPath();ctx.roundRect(p.x-4,p.bottom,PW+8,14,4);ctx.fill();
      });
      // bird
      ctx.save();ctx.translate(bird.x,bird.y);ctx.rotate(bird.angle);
      // glow
      const bg=ctx.createRadialGradient(0,0,0,0,0,bird.r*2);
      bg.addColorStop(0,'rgba(251,191,36,0.5)');bg.addColorStop(1,'transparent');
      ctx.fillStyle=bg;ctx.beginPath();ctx.arc(0,0,bird.r*2,0,Math.PI*2);ctx.fill();
      // body
      ctx.fillStyle='#fbbf24';ctx.beginPath();ctx.ellipse(0,0,bird.r,bird.r*0.85,0,0,Math.PI*2);ctx.fill();
      // wing
      ctx.fillStyle='#f59e0b';
      const wFlap=Math.sin(frame*0.3)*0.4;
      ctx.beginPath();ctx.ellipse(-4,2+wFlap*8,10,6,wFlap,0,Math.PI*2);ctx.fill();
      // eye
      ctx.fillStyle='#fff';ctx.beginPath();ctx.arc(8,-4,5,0,Math.PI*2);ctx.fill();
      ctx.fillStyle='#1e293b';ctx.beginPath();ctx.arc(9.5,-4,2.5,0,Math.PI*2);ctx.fill();
      // beak
      ctx.fillStyle='#fb923c';ctx.beginPath();ctx.moveTo(bird.r-2,0);ctx.lineTo(bird.r+10,3);ctx.lineTo(bird.r-2,6);ctx.closePath();ctx.fill();
      ctx.restore();
      // score
      ctx.fillStyle='rgba(15,23,42,0.7)';ctx.beginPath();ctx.roundRect(W/2-35,14,70,36,10);ctx.fill();
      ctx.fillStyle='#fbbf24';ctx.font='bold 22px sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';
      ctx.fillText(score,W/2,33);
    }
    document.addEventListener('keydown',e=>{if(e.key===' '||e.key==='ArrowUp'){e.preventDefault();flap();}});
    const cw=document.getElementById('fcwrap');
    cw.addEventListener('click',()=>{if(!running)start();else flap();});
    cw.addEventListener('touchstart',e=>{e.preventDefault();if(!running)start();else flap();},{passive:false});
    document.getElementById('flapBtn').addEventListener('click',()=>{if(!running)start();else flap();});
    document.getElementById('fStartBtn').addEventListener('click',start);
    document.getElementById('fRestart').addEventListener('click',start);
    reset();draw();
    </script>
    </body></html>
    """, height=640)

# ═══════════════════════════════════════════════════════
#                    WHACK-A-MOLE GAME
# ═══════════════════════════════════════════════════════
if st.session_state.selected_game == "whack":
    components.html("""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
      .gh{font-family:'Inter',sans-serif;}
      .gh-tag{font-size:0.76rem;text-transform:uppercase;letter-spacing:0.2em;color:#f472b6;}
      .gh-title{font-size:1.9rem;font-weight:900;color:#e5e7eb;margin:0.3rem 0 0.4rem;display:flex;align-items:center;gap:10px;}
      .gh-icon{width:42px;height:42px;background:rgba(244,114,182,0.12);border:1px solid rgba(244,114,182,0.25);border-radius:12px;display:flex;align-items:center;justify-content:center;}
      .ctrl-chip{display:inline-flex;align-items:center;gap:5px;background:rgba(244,114,182,0.08);border:1px solid rgba(244,114,182,0.2);border-radius:999px;padding:0.25rem 0.75rem;font-size:0.75rem;color:#f472b6;margin-right:6px;}
    </style>
    <div class="gh">
      <div class="gh-tag">Reflex · Reaction</div>
      <div class="gh-title">
        <div class="gh-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#f472b6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="8" r="5"/>
            <path d="M3 21a9 9 0 0 1 18 0"/>
            <line x1="12" y1="13" x2="12" y2="16"/>
          </svg>
        </div>
        Whack-a-Mole
      </div>
      <p style="color:#9ca3af;font-size:0.92rem;margin:0;">
        <span class="ctrl-chip">
          <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
          Click / Tap the moles fast!
        </span>
      </p>
    </div>
    """, height=120)

    components.html("""
    <!DOCTYPE html><html lang="en"><head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=no"/>
    <style>
      *{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent;}
      body{background:transparent;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
           display:flex;flex-direction:column;align-items:center;padding:0 4px;}
      .gw{width:100%;max-width:540px;}
      .scoreboard{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:14px;}
      .sc{background:rgba(15,23,42,0.97);border:1px solid rgba(148,163,184,0.18);border-radius:12px;padding:10px 6px;text-align:center;}
      .sv{font-size:1.5rem;font-weight:900;background:linear-gradient(135deg,#f472b6,#fb923c);-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1;}
      .sl{font-size:0.62rem;text-transform:uppercase;letter-spacing:0.1em;color:#9ca3af;margin-top:3px;}
      .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;padding:4px;}
      .hole{position:relative;aspect-ratio:1;border-radius:50%;background:rgba(15,23,42,0.97);
            border:2px solid rgba(148,163,184,0.15);overflow:hidden;cursor:pointer;
            box-shadow:inset 0 8px 24px rgba(0,0,0,0.6);}
      .hole:active{transform:scale(0.97);}
      .mole{position:absolute;bottom:-100%;left:50%;transform:translateX(-50%);
            width:70%;transition:bottom 0.18s cubic-bezier(0.4,0,0.2,1);display:flex;flex-direction:column;align-items:center;}
      .hole.up .mole{bottom:0%;}
      .hole.whacked .mole{bottom:10%;}
      .mole-face{width:100%;aspect-ratio:1;}
      .hole.whacked{background:rgba(244,114,182,0.15);border-color:rgba(244,114,182,0.5);}
      .hit-effect{position:absolute;top:20%;left:50%;transform:translate(-50%,-50%);
                  font-size:1.4rem;font-weight:900;color:#f472b6;opacity:0;
                  transition:opacity 0.1s,transform 0.3s;pointer-events:none;white-space:nowrap;}
      .hit-effect.show{opacity:1;transform:translate(-50%,-120%);}
      .start-btn{display:block;width:100%;margin-top:14px;padding:1rem;font-size:1.1rem;font-weight:800;
                 background:linear-gradient(135deg,#f472b6,#fb923c);border:none;border-radius:16px;
                 color:#000;cursor:pointer;box-shadow:0 8px 24px rgba(244,114,182,0.3);
                 transition:transform 0.15s;display:flex;align-items:center;justify-content:center;gap:8px;}
      .start-btn:hover{transform:scale(1.02);}
      .timer-bar{width:100%;height:8px;background:rgba(148,163,184,0.15);border-radius:999px;
                 margin-bottom:10px;overflow:hidden;}
      .timer-fill{height:100%;border-radius:999px;background:linear-gradient(90deg,#f472b6,#fb923c);
                  transition:width 0.1s linear;}
      .result-banner{background:rgba(15,23,42,0.97);border:1px solid rgba(244,114,182,0.3);
                     border-radius:16px;padding:1.5rem;text-align:center;margin-top:12px;display:none;}
      .result-banner.show{display:block;}
      .res-title{font-size:1.6rem;font-weight:900;color:#e5e7eb;margin-bottom:0.3rem;}
      .res-sub{font-size:0.9rem;color:#9ca3af;}
    </style>
    </head><body>
    <div class="gw">
      <div class="scoreboard">
        <div class="sc"><div class="sv" id="wScore">0</div><div class="sl">Score</div></div>
        <div class="sc"><div class="sv" id="wBest" style="-webkit-text-fill-color:#34d399;color:#34d399;">0</div><div class="sl">Best</div></div>
        <div class="sc"><div class="sv" id="wTime" style="font-size:1.1rem;">30</div><div class="sl">Time</div></div>
      </div>
      <div class="timer-bar"><div class="timer-fill" id="timerFill" style="width:100%;"></div></div>
      <div class="grid" id="wgrid"></div>
      <button class="start-btn" id="wStart" style="margin-top:14px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <polygon points="5 3 19 12 5 21 5 3"/>
        </svg>
        Start Game — 30 seconds!
      </button>
      <div class="result-banner" id="wResult">
        <div style="width:56px;height:56px;background:rgba(244,114,182,0.12);border:1px solid rgba(244,114,182,0.35);border-radius:16px;display:flex;align-items:center;justify-content:center;margin:0 auto 0.8rem;">
          <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#f472b6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="8" r="5"/>
            <path d="M3 21a9 9 0 0 1 18 0"/>
          </svg>
        </div>
        <div class="res-title">Time's Up!</div>
        <div class="res-sub" id="wResMsg"></div>
        <button class="start-btn" onclick="startGame()" style="margin-top:1rem;">
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 12a9 9 0 0 0-9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/>
            <path d="M3 12a9 9 0 0 0 9 9 9.75 9.75 0 0 0 6.74-2.74L21 16"/><path d="M16 21h5v-5"/>
          </svg>
          Play Again
        </button>
      </div>
    </div>
    <script>
    const MOLE_SVG=`<svg class="mole-face" viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
      <ellipse cx="40" cy="50" rx="28" ry="32" fill="#a78bfa"/>
      <ellipse cx="40" cy="46" rx="22" ry="26" fill="#c4b5fd"/>
      <circle cx="28" cy="36" r="6" fill="#fff"/>
      <circle cx="52" cy="36" r="6" fill="#fff"/>
      <circle cx="30" cy="37" r="3" fill="#1e1b4b"/>
      <circle cx="54" cy="37" r="3" fill="#1e1b4b"/>
      <circle cx="31" cy="36" r="1" fill="#fff"/>
      <circle cx="55" cy="36" r="1" fill="#fff"/>
      <ellipse cx="40" cy="52" rx="12" ry="8" fill="#f9a8d4"/>
      <ellipse cx="34" cy="52" rx="4" ry="3" fill="#f472b6"/>
      <ellipse cx="46" cy="52" rx="4" ry="3" fill="#f472b6"/>
      <path d="M34 58 Q40 63 46 58" stroke="#7c3aed" stroke-width="2" fill="none" stroke-linecap="round"/>
      <line x1="16" y1="50" x2="28" y2="52" stroke="#7c3aed" stroke-width="1.5"/>
      <line x1="16" y1="54" x2="28" y2="54" stroke="#7c3aed" stroke-width="1.5"/>
      <line x1="52" y1="52" x2="64" y2="50" stroke="#7c3aed" stroke-width="1.5"/>
      <line x1="52" y1="54" x2="64" y2="54" stroke="#7c3aed" stroke-width="1.5"/>
    </svg>`;
    const WHACK_SVG=`<svg class="mole-face" viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
      <ellipse cx="40" cy="50" rx="28" ry="32" fill="#7c3aed"/>
      <ellipse cx="40" cy="46" rx="22" ry="26" fill="#8b5cf6"/>
      <path d="M25 35 L35 45 M35 35 L25 45" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
      <path d="M45 35 L55 45 M55 35 L45 45" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
      <path d="M30 56 Q40 50 50 56" stroke="#f9a8d4" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    </svg>`;
    const N=9;let holes=Array(N).fill(false),timers=[],score=0,best=0,timeLeft=30,gameTimer=null,moleTimer=null,running=false;
    function hud(){document.getElementById('wScore').textContent=score;document.getElementById('wBest').textContent=best;document.getElementById('wTime').textContent=timeLeft;document.getElementById('timerFill').style.width=(timeLeft/30*100)+'%';}
    function renderGrid(){
      const g=document.getElementById('wgrid');g.innerHTML='';
      for(let i=0;i<N;i++){
        const h=document.createElement('div');
        h.className='hole'+(holes[i]===true?' up':holes[i]==='whacked'?' whacked':'');
        h.innerHTML=`<div class="mole">${holes[i]==='whacked'?WHACK_SVG:MOLE_SVG}</div><div class="hit-effect" id="hit${i}">+10</div>`;
        h.addEventListener('click',()=>whack(i));
        h.addEventListener('touchstart',e=>{e.preventDefault();whack(i);},{passive:false});
        g.appendChild(h);
      }
    }
    function whack(i){
      if(!running||holes[i]!==true)return;
      clearTimeout(timers[i]);holes[i]='whacked';score+=10;if(score>best)best=score;hud();renderGrid();
      const hitEl=document.getElementById('hit'+i);if(hitEl){hitEl.classList.add('show');setTimeout(()=>hitEl&&hitEl.classList.remove('show'),300);}
      setTimeout(()=>{if(holes[i]==='whacked'){holes[i]=false;renderGrid();}},400);
    }
    function showMole(){
      if(!running)return;
      const avail=holes.map((h,i)=>h===false?i:-1).filter(i=>i>=0);
      if(avail.length===0)return;
      const i=avail[Math.floor(Math.random()*avail.length)];
      holes[i]=true;renderGrid();
      const dur=Math.max(600,1200-score*4);
      timers[i]=setTimeout(()=>{if(holes[i]===true){holes[i]=false;renderGrid();}},dur);
    }
    function startGame(){
      score=0;timeLeft=30;holes=Array(N).fill(false);running=true;
      clearInterval(gameTimer);clearInterval(moleTimer);timers.forEach(t=>clearTimeout(t));
      document.getElementById('wStart').style.display='none';
      document.getElementById('wResult').classList.remove('show');
      hud();renderGrid();
      moleTimer=setInterval(showMole,700);
      gameTimer=setInterval(()=>{
        timeLeft--;hud();
        if(timeLeft<=0){
          running=false;clearInterval(gameTimer);clearInterval(moleTimer);
          timers.forEach(t=>clearTimeout(t));holes=Array(N).fill(false);renderGrid();
          const r=score>=150?'Incredible reflexes!':score>=80?'Great job!':score>=40?'Not bad!':'Keep practising!';
          document.getElementById('wResMsg').innerHTML=`<strong style="color:#f472b6;font-size:1.2rem;">${score} pts</strong><br>${r}`;
          document.getElementById('wResult').classList.add('show');
          document.getElementById('wStart').style.display='flex';
        }
      },1000);
    }
    document.getElementById('wStart').addEventListener('click',startGame);
    renderGrid();
    </script>
    </body></html>
    """, height=680)

# ═══════════════════════════════════════════════════════
#                    PROGRAMMING QUIZ
# ═══════════════════════════════════════════════════════
if st.session_state.selected_game == "quiz":
    if not st.session_state.quiz_initialized:
        st.session_state.quiz_initialized = True
        st.session_state.quiz_finished = False
        st.session_state.quiz_index = 0
        st.session_state.quiz_score = 0
        st.session_state.quiz_answers = {}
        st.session_state.quiz_submitted = {}
        
        QUIZ_QUESTIONS = [
            {"question":"Which Python web framework is known for its 'batteries included' philosophy?","options":["Flask","Django","FastAPI","Pyramid"],"answer":"Django","category":"Backend","explanation":"Django follows the 'batteries included' philosophy, providing built-in features like ORM, authentication, admin panel, and more."},
            {"question":"What does CSS stand for?","options":["Computer Style Sheets","Cascading Style Sheets","Creative Style Sheets","Colorful Style Sheets"],"answer":"Cascading Style Sheets","category":"Frontend","explanation":"CSS (Cascading Style Sheets) is used to style and layout web pages."},
            {"question":"Which database is known as an in-memory data structure store?","options":["MySQL","PostgreSQL","MongoDB","Redis"],"answer":"Redis","category":"Databases","explanation":"Redis is an in-memory data structure store, used as a database, cache, and message broker."},
            {"question":"What is the purpose of Git?","options":["Website hosting","Version control","Database management","Server deployment"],"answer":"Version control","category":"Tools","explanation":"Git is a distributed version control system for tracking changes in source code."},
            {"question":"Which Python library is commonly used for data manipulation and analysis?","options":["NumPy","Requests","Pandas","Matplotlib"],"answer":"Pandas","category":"Python","explanation":"Pandas provides high-performance, easy-to-use data structures and data analysis tools."},
            {"question":"What does API stand for?","options":["Application Programming Interface","Advanced Programming Interface","Automated Programming Interface","Application Process Integration"],"answer":"Application Programming Interface","category":"General","explanation":"API (Application Programming Interface) allows different software applications to communicate."},
            {"question":"Which JavaScript framework was developed by Meta (Facebook)?","options":["Angular","Vue","React","Svelte"],"answer":"React","category":"Frontend","explanation":"React was created by Jordan Walke, a software engineer at Meta (Facebook)."},
            {"question":"What is the default port for HTTP?","options":["21","80","443","8080"],"answer":"80","category":"Networking","explanation":"Port 80 is the default port for HTTP (HyperText Transfer Protocol)."},
            {"question":"Which CSS property creates a flex container?","options":["flex-container: true","display: flex","flexbox: true","container: flex"],"answer":"display: flex","category":"Frontend","explanation":"The 'display: flex' property creates a flex container enabling flex layout."},
            {"question":"What is the purpose of a virtual environment in Python?","options":["To run Python faster","To isolate project dependencies","To compile Python to machine code","To connect to remote servers"],"answer":"To isolate project dependencies","category":"Python","explanation":"Virtual environments create isolated spaces for Python projects with their own dependencies."},
            {"question":"What does SQL stand for?","options":["Structured Query Language","Simple Query Language","Sequential Query Language","Standard Query Language"],"answer":"Structured Query Language","category":"Databases","explanation":"SQL (Structured Query Language) is used to communicate with relational databases."},
            {"question":"Which HTTP method is used to update data on a server?","options":["GET","POST","PUT","DELETE"],"answer":"PUT","category":"Backend","explanation":"PUT is used to update/replace existing data on the server."},
        ]
        random.shuffle(QUIZ_QUESTIONS)
        st.session_state.quiz_questions = QUIZ_QUESTIONS[:5]

    NUM_QUESTIONS = len(st.session_state.quiz_questions)

    components.html("""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
      .gh{font-family:'Inter',sans-serif;}
      .gh-tag{font-size:0.76rem;text-transform:uppercase;letter-spacing:0.2em;color:#fde047;}
      .gh-title{font-size:1.9rem;font-weight:900;color:#e5e7eb;margin:0.3rem 0 0.4rem;display:flex;align-items:center;gap:10px;}
      .gh-icon{width:42px;height:42px;background:rgba(253,224,71,0.12);border:1px solid rgba(253,224,71,0.25);border-radius:12px;display:flex;align-items:center;justify-content:center;}
      .ctrl-chip{display:inline-flex;align-items:center;gap:5px;background:rgba(253,224,71,0.08);border:1px solid rgba(253,224,71,0.2);border-radius:999px;padding:0.25rem 0.75rem;font-size:0.75rem;color:#fde047;margin-right:6px;}
    </style>
    <div class="gh">
      <div class="gh-tag">Trivia · Knowledge</div>
      <div class="gh-title">
        <div class="gh-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#fde047" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/>
            <path d="M9 18h6"/><path d="M10 22h4"/>
          </svg>
        </div>
        Dev Quiz
      </div>
      <p style="color:#9ca3af;font-size:0.92rem;margin:0;">
        <span class="ctrl-chip">
          <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
          5 random programming questions
        </span>
      </p>
    </div>
    """, height=120)

    if st.session_state.quiz_finished:
        score = st.session_state.quiz_score
        total = NUM_QUESTIONS
        pct = int((score / total) * 100)
        if score == total: msg, icon_color = "Perfect score! Brilliant!", "#fde047"
        elif score >= total * 0.8: msg, icon_color = "Excellent! Almost flawless!", "#34d399"
        elif score >= total * 0.6: msg, icon_color = "Good job! Keep learning!", "#00d4ff"
        elif score >= total * 0.4: msg, icon_color = "Not bad — review below!", "#fb923c"
        else: msg, icon_color = "Keep going — practice makes perfect!", "#f472b6"
        
        components.html(f"""
        <div style="background:linear-gradient(135deg,rgba(253,224,71,0.06),rgba(0,212,255,0.06));
             border:1px solid rgba(253,224,71,0.25);border-radius:18px;
             padding:2.2rem 2rem;text-align:center;
             font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;margin-bottom:1rem;">
          <div style="width:72px;height:72px;background:rgba(253,224,71,0.1);border:1px solid rgba(253,224,71,0.3);border-radius:20px;display:flex;align-items:center;justify-content:center;margin:0 auto 1rem;">
            <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="{icon_color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
              <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/>
              <path d="M4 22h16"/><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"/>
              <path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"/>
              <path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"/>
            </svg>
          </div>
          <div style="font-size:4.5rem;font-weight:900;background:linear-gradient(135deg,#fde047,#00d4ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1;">{score}/{total}</div>
          <div style="color:#e5e7eb;font-size:1.1rem;font-weight:600;margin-top:0.5rem;">{msg}</div>
          <div style="width:100%;max-width:260px;height:10px;border-radius:999px;background:rgba(148,163,184,0.15);margin:1.2rem auto 0;overflow:hidden;">
            <div style="width:{pct}%;height:100%;border-radius:999px;background:linear-gradient(135deg,#fde047,#00d4ff);"></div>
          </div>
          <div style="color:#9ca3af;font-size:0.85rem;margin-top:0.6rem;">{pct}% correct</div>
        </div>
        """, height=340)
        
        components.html("""
        <h3 style="font-family:sans-serif;color:#e5e7eb;font-size:1.15rem;font-weight:700;margin-bottom:0.4rem;display:flex;align-items:center;gap:8px;">
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#e5e7eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/>
            <path d="M15 2H9a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V3a1 1 0 0 0-1-1Z"/>
          </svg>
          Answer Review
        </h3>
        """, height=45)
        
        for i, q in enumerate(st.session_state.quiz_questions):
            user_ans = st.session_state.quiz_answers.get(i, "—")
            is_correct = user_ans == q["answer"]
            bg = "rgba(16,185,129,0.07)" if is_correct else "rgba(239,68,68,0.07)"
            bdr = "rgba(16,185,129,0.3)" if is_correct else "rgba(239,68,68,0.3)"
            icon_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#6ee7b7" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>' if is_correct else '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fca5a5" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>'
            
            components.html(f"""
            <div style="background:{bg};border:1px solid {bdr};border-radius:14px;padding:1rem 1.2rem;margin-bottom:0.7rem;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:0.5rem;">
                <div style="flex:1;">
                  <div style="font-size:0.7rem;color:#00d4ff;background:rgba(0,212,255,0.1);border:1px solid rgba(0,212,255,0.2);border-radius:999px;padding:0.15rem 0.6rem;display:inline-block;margin-bottom:0.5rem;">{q['category']}</div>
                  <div style="font-size:0.95rem;font-weight:600;color:#e5e7eb;line-height:1.5;">{i+1}. {q['question']}</div>
                </div>
                <div style="flex-shrink:0;margin-top:4px;">{icon_svg}</div>
              </div>
              <div style="font-size:0.88rem;margin-top:0.6rem;color:#9ca3af;">Your answer: <span style="color:{'#6ee7b7' if is_correct else '#fca5a5'};font-weight:600;">{user_ans}</span></div>
              {'' if is_correct else f'<div style="font-size:0.88rem;margin-top:0.2rem;color:#9ca3af;">Correct: <span style="color:#6ee7b7;font-weight:600;">{q["answer"]}</span></div>'}
              <div style="font-size:0.83rem;color:#9ca3af;line-height:1.5;margin-top:0.6rem;padding-top:0.6rem;border-top:1px solid rgba(148,163,184,0.12);">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#9ca3af" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-right:4px;"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg>
                {q['explanation']}
              </div>
            </div>
            """, height=210 if is_correct else 240)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Play Again", key="restart_quiz_btn", use_container_width=True, type="primary"):
            st.session_state.quiz_finished = False
            st.session_state.quiz_index = 0
            st.session_state.quiz_score = 0
            st.session_state.quiz_answers = {}
            st.session_state.quiz_submitted = {}
            random.shuffle(st.session_state.quiz_questions)
            st.rerun()
    else:
        idx = st.session_state.quiz_index
        q = st.session_state.quiz_questions[idx]
        progress = (idx + 1) / NUM_QUESTIONS
        
        components.html(f"""
        <div style="font-family:sans-serif;margin-bottom:1rem;">
          <div style="display:flex;justify-content:space-between;align-items:center;font-size:0.8rem;color:#9ca3af;margin-bottom:0.5rem;">
            <span style="display:flex;align-items:center;gap:6px;">
              <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fde047" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
              Question {idx+1} of {NUM_QUESTIONS}
            </span>
            <span style="color:#fde047;font-weight:700;">{int(progress*100)}%</span>
          </div>
          <div style="width:100%;height:8px;border-radius:999px;background:rgba(148,163,184,0.12);overflow:hidden;">
            <div style="width:{progress*100}%;height:100%;border-radius:999px;background:linear-gradient(90deg,#fde047,#00d4ff);transition:width 0.3s ease;"></div>
          </div>
        </div>
        """, height=60)
        
        components.html(f"""
        <div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
             background:rgba(15,23,42,0.97);border:1px solid rgba(148,163,184,0.2);
             border-radius:18px;padding:1.8rem 2rem;box-shadow:0 24px 60px rgba(0,0,0,0.9);margin-bottom:0.5rem;">
          <span style="background:rgba(253,224,71,0.1);border:1px solid rgba(253,224,71,0.25);border-radius:999px;padding:0.2rem 0.8rem;font-size:0.72rem;color:#fde047;font-weight:600;">{q['category']}</span>
          <div style="font-size:1.12rem;font-weight:700;color:#e5e7eb;margin-top:0.9rem;line-height:1.55;">{q['question']}</div>
        </div>
        """, height=150)
        
        already_submitted = st.session_state.quiz_submitted.get(idx, False)
        if not already_submitted:
            selected = st.radio("Select your answer:", ["— Select an answer —"] + q["options"],
                                key=f"quiz_answer_{idx}", label_visibility="collapsed")
            if selected != "— Select an answer —":
                st.session_state.quiz_answers[idx] = selected
        else:
            st.markdown(f"**Your answer:** `{st.session_state.quiz_answers.get(idx, '—')}`")
        
        col1, col2 = st.columns([1,1])
        with col1:
            if not already_submitted:
                if st.button("Submit Answer", key=f"quiz_submit_{idx}", use_container_width=True, type="primary"):
                    ans = st.session_state.quiz_answers.get(idx)
                    if not ans or ans == "— Select an answer —":
                        st.warning("Please select an answer first!")
                    else:
                        st.session_state.quiz_submitted[idx] = True
                        if ans == q["answer"]: st.session_state.quiz_score += 1
                        st.rerun()
        with col2:
            if already_submitted:
                is_last = idx == NUM_QUESTIONS - 1
                btn_text = "See Results" if is_last else "Next Question →"
                if st.button(btn_text, key=f"quiz_next_{idx}", use_container_width=True):
                    if is_last: st.session_state.quiz_finished = True
                    else: st.session_state.quiz_index += 1
                    st.rerun()
        
        if already_submitted:
            user_ans = st.session_state.quiz_answers.get(idx, "")
            is_correct = user_ans == q["answer"]
            if is_correct:
                components.html(f"""
                <div style="background:rgba(16,185,129,0.08);border:1px solid rgba(16,185,129,0.35);border-radius:12px;padding:1rem 1.2rem;font-family:sans-serif;margin-top:0.5rem;">
                  <div style="color:#6ee7b7;font-weight:700;font-size:1rem;display:flex;align-items:center;gap:8px;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#6ee7b7" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
                    Correct! Well done!
                  </div>
                  <div style="color:#9ca3af;font-size:0.85rem;margin-top:0.5rem;line-height:1.55;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#9ca3af" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-right:4px;"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg>
                    {q['explanation']}
                  </div>
                </div>
                """, height=115)
            else:
                components.html(f"""
                <div style="background:rgba(239,68,68,0.08);border:1px solid rgba(239,68,68,0.3);border-radius:12px;padding:1rem 1.2rem;font-family:sans-serif;margin-top:0.5rem;">
                  <div style="color:#fca5a5;font-weight:700;font-size:1rem;display:flex;align-items:center;gap:8px;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fca5a5" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
                    Incorrect
                  </div>
                  <div style="color:#9ca3af;font-size:0.88rem;margin-top:0.4rem;">Your answer: <span style="color:#fca5a5;font-weight:600;">{user_ans}</span></div>
                  <div style="color:#9ca3af;font-size:0.88rem;margin-top:0.2rem;">Correct: <span style="color:#6ee7b7;font-weight:600;">{q['answer']}</span></div>
                  <div style="color:#9ca3af;font-size:0.85rem;line-height:1.55;margin-top:0.5rem;padding-top:0.5rem;border-top:1px solid rgba(148,163,184,0.12);">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#9ca3af" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-right:4px;"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg>
                    {q['explanation']}
                  </div>
                </div>
                """, height=175)

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
      <line x1="6" y1="12" x2="10" y2="12"></line>
      <line x1="8" y1="10" x2="8" y2="14"></line>
      <line x1="15" y1="13" x2="15.01" y2="13"></line>
      <line x1="18" y1="11" x2="18.01" y2="11"></line>
      <rect x="2" y="6" width="20" height="12" rx="2"></rect>
    </svg>
    Game Page
</div>
</div>
</body>
</html>
""", height=46)