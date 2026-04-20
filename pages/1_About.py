import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import streamlit.components.v1 as components
import base64
from components import apply_global_effects

st.set_page_config(
    page_title="About | Dave Campo",
    page_icon="👤",
    layout="wide"
)

apply_global_effects()

with st.sidebar:
    st.markdown("""
    <div style="text-align:center;margin-bottom:1rem;">
        <h2 style="color:#00d4ff;font-size:1.5rem;font-weight:800;margin:0;">Dave.dev</h2>
        <p style="color:#9ca3af;font-size:0.8rem;margin:0.3rem 0 0;">Portfolio</p>
    </div>
    """, unsafe_allow_html=True)
    st.divider()

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
iframe { display: block; border: none !important; }
hr { border-color: rgba(148,163,184,0.2) !important; margin: 1.5rem 0 !important; }
</style>
""", unsafe_allow_html=True)

# ── Load and encode profile image (same pattern as index.py) ──
with open("assets/profile/profile.png", "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

components.html(f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no"/>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
<style>
  *, *::before, *::after {{ margin:0; padding:0; box-sizing:border-box; }}

  :root {{
    --cyan:    #00d4ff;
    --pink:    #ff6bcb;
    --green:   #34d399;
    --yellow:  #fde68a;
    --purple:  #a78bfa;
    --surface: rgba(15,23,42,0.96);
    --border:  rgba(148,163,184,0.2);
    --text:    #e5e7eb;
    --muted:   #9ca3af;
  }}

  html {{ font-size: 16px; scroll-behavior: smooth; }}

  body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: transparent;
    color: var(--text);
    overflow-x: hidden;
    padding: 0;
  }}

  /* ══════════════════════════════════
     SCROLL-REVEAL BASE
  ══════════════════════════════════ */
  .reveal {{
    opacity: 0;
    transform: translateY(32px);
    transition: opacity 0.65s cubic-bezier(.22,1,.36,1),
                transform 0.65s cubic-bezier(.22,1,.36,1);
  }}

  .reveal.visible {{
    opacity: 1;
    transform: translateY(0);
  }}

  .reveal-fast  {{ transition-duration: 0.45s; }}
  .reveal-slow  {{ transition-duration: 0.85s; }}
  .delay-1 {{ transition-delay: 0.08s; }}
  .delay-2 {{ transition-delay: 0.16s; }}
  .delay-3 {{ transition-delay: 0.24s; }}
  .delay-4 {{ transition-delay: 0.32s; }}
  .delay-5 {{ transition-delay: 0.40s; }}

  .reveal-left {{
    opacity: 0;
    transform: translateX(-30px);
    transition: opacity 0.65s cubic-bezier(.22,1,.36,1),
                transform 0.65s cubic-bezier(.22,1,.36,1);
  }}
  .reveal-left.visible {{ opacity:1; transform:translateX(0); }}

  .reveal-right {{
    opacity: 0;
    transform: translateX(30px);
    transition: opacity 0.65s cubic-bezier(.22,1,.36,1),
                transform 0.65s cubic-bezier(.22,1,.36,1);
  }}
  .reveal-right.visible {{ opacity:1; transform:translateX(0); }}

  .reveal-scale {{
    opacity: 0;
    transform: scale(0.88);
    transition: opacity 0.55s cubic-bezier(.22,1,.36,1),
                transform 0.55s cubic-bezier(.22,1,.36,1);
  }}
  .reveal-scale.visible {{ opacity:1; transform:scale(1); }}

  /* ══════════════════════════════════
     HERO CARD
  ══════════════════════════════════ */
  .hero {{
    background: var(--surface);
    border-radius: 20px;
    border: 1px solid rgba(148,163,184,0.28);
    padding: clamp(1.2rem, 4vw, 2.2rem);
    box-shadow: 0 24px 60px rgba(0,0,0,0.85);
    backdrop-filter: blur(18px);
    margin-bottom: 20px;
    overflow: hidden;
    position: relative;
  }}

  .hero::before {{
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 260px; height: 260px;
    background: radial-gradient(circle, rgba(0,212,255,0.08) 0%, transparent 70%);
    pointer-events: none;
    border-radius: 50%;
  }}

  .hero-inner {{
    display: flex;
    gap: clamp(1.2rem, 4vw, 2.5rem);
    align-items: center;
    flex-wrap: wrap;
  }}

  /* ── Avatar ── */
  .avatar-wrap {{
    flex-shrink: 0;
    position: relative;
  }}

  .avatar-ring {{
    width: clamp(100px, 18vw, 150px);
    height: clamp(100px, 18vw, 150px);
    border-radius: 50%;
    padding: 3px;
    background: linear-gradient(135deg, var(--cyan), var(--pink), var(--purple));
    animation: ring-spin 6s linear infinite;
    box-shadow: 0 0 30px rgba(0,212,255,0.25), 0 0 60px rgba(255,107,203,0.12);
  }}

  @keyframes ring-spin {{
    0%   {{ background: linear-gradient(135deg, var(--cyan), var(--pink), var(--purple)); }}
    33%  {{ background: linear-gradient(225deg, var(--pink), var(--purple), var(--cyan)); }}
    66%  {{ background: linear-gradient(315deg, var(--purple), var(--cyan), var(--pink)); }}
    100% {{ background: linear-gradient(135deg, var(--cyan), var(--pink), var(--purple)); }}
  }}

  .avatar-inner {{
    width: 100%;
    height: 100%;
    border-radius: 50%;
    overflow: hidden;
    border: 3px solid #020617;
    background: rgba(15,23,42,0.9);
    display: flex;
    align-items: center;
    justify-content: center;
  }}

  .avatar-inner img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center top;
    transition: transform 0.4s ease;
  }}

  .avatar-ring:hover .avatar-inner img {{
    transform: scale(1.06);
  }}

  .avatar-fallback {{
    font-size: clamp(2.5rem, 6vw, 3.5rem);
    color: var(--cyan);
    opacity: 0.7;
  }}

  .avatar-status {{
    position: absolute;
    bottom: 6px;
    right: 6px;
    width: clamp(14px, 3vw, 18px);
    height: clamp(14px, 3vw, 18px);
    border-radius: 50%;
    background: #22c55e;
    border: 3px solid #020617;
    animation: status-blink 2.5s ease-in-out infinite;
    box-shadow: 0 0 8px rgba(34,197,94,0.6);
  }}

  @keyframes status-blink {{
    0%,100% {{ opacity: 1; box-shadow: 0 0 8px rgba(34,197,94,0.6); }}
    50%     {{ opacity: 0.6; box-shadow: 0 0 14px rgba(34,197,94,0.9); }}
  }}

  /* ── Hero text block ── */
  .hero-text {{ flex: 1; min-width: 220px; }}

  .hero-eyebrow {{
    font-size: clamp(0.66rem, 1.7vw, 0.8rem);
    text-transform: uppercase;
    letter-spacing: 0.22em;
    color: var(--cyan);
    margin-bottom: 0.55rem;
  }}

  .hero-title {{
    font-size: clamp(1.55rem, 5vw, 2.5rem);
    font-weight: 800;
    color: var(--text);
    margin-bottom: 0.85rem;
    line-height: 1.12;
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
  }}

  .hero-title i {{ color: var(--cyan); font-size: 0.82em; }}

  .hero-body {{
    font-size: clamp(0.85rem, 2.1vw, 0.97rem);
    color: var(--muted);
    line-height: 1.8;
    margin-bottom: 1.2rem;
  }}

  .hero-body strong {{ color: var(--text); }}

  .grad-text {{
    background: linear-gradient(135deg, var(--cyan), var(--pink));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
  }}

  /* ── Stat chips ── */
  .stats-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 1.1rem;
  }}

  .stat-chip {{
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(148,163,184,0.18);
    border-radius: 12px;
    padding: 8px 14px;
    text-align: center;
    min-width: 72px;
    transition: border-color 0.2s, background 0.2s;
  }}

  .stat-chip:hover {{
    border-color: rgba(0,212,255,0.4);
    background: rgba(0,212,255,0.06);
  }}

  .stat-num {{
    font-size: clamp(1.1rem, 3vw, 1.4rem);
    font-weight: 900;
    background: linear-gradient(135deg, var(--cyan), var(--pink));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1.1;
  }}

  .stat-lbl {{
    font-size: clamp(0.62rem, 1.4vw, 0.7rem);
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-top: 2px;
  }}

  .badges {{
    display: flex;
    flex-wrap: wrap;
    gap: 7px;
  }}

  .badge {{
    border-radius: 999px;
    padding: clamp(4px,1vw,5px) clamp(10px,2.5vw,13px);
    font-size: clamp(0.68rem, 1.6vw, 0.76rem);
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    white-space: nowrap;
    transition: transform 0.18s, box-shadow 0.18s;
  }}

  .badge:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(0,0,0,0.3);
  }}

  .badge-green {{ background:rgba(52,211,153,0.12); border:1px solid rgba(52,211,153,0.35); color:#34d399; }}
  .badge-cyan  {{ background:rgba(0,212,255,0.10);  border:1px solid rgba(0,212,255,0.30);  color:#00d4ff; }}
  .badge-lime  {{ background:rgba(22,163,74,0.10);  border:1px solid rgba(22,163,74,0.35);  color:#86efac; }}

  /* ══════════════════════════════════
     SECTION HEADER
  ══════════════════════════════════ */
  .section-header {{ margin: 32px 0 22px; }}

  .section-eyebrow {{
    font-size: clamp(0.66rem, 1.5vw, 0.76rem);
    text-transform: uppercase;
    letter-spacing: 0.2em;
    color: var(--pink);
    margin-bottom: 5px;
  }}

  .section-title {{
    font-size: clamp(1.25rem, 3.8vw, 1.8rem);
    font-weight: 800;
    color: var(--text);
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
  }}

  .section-title i {{ color: var(--pink); font-size: 0.88em; }}

  /* ══════════════════════════════════
     TIMELINE
  ══════════════════════════════════ */
  .timeline {{
    position: relative;
    padding-left: clamp(1.5rem, 4vw, 2rem);
  }}

  .timeline::before {{
    content: '';
    position: absolute;
    left: 6px;
    top: 8px;
    bottom: 8px;
    width: 2px;
    background: linear-gradient(to bottom, var(--cyan), var(--pink), rgba(148,163,184,0.12));
    border-radius: 999px;
  }}

  .tl-item {{
    position: relative;
    margin-bottom: clamp(1rem, 3vw, 1.8rem);
  }}

  .tl-item:last-child {{ margin-bottom: 0; }}

  .tl-dot {{
    position: absolute;
    left: clamp(-1.75rem, -4vw, -1.65rem);
    top: 6px;
    width: 13px;
    height: 13px;
    border-radius: 50%;
    z-index: 1;
  }}

  .tl-card {{
    background: var(--surface);
    border-radius: 14px;
    padding: clamp(0.85rem, 2.5vw, 1.2rem) clamp(0.95rem, 2.8vw, 1.4rem);
    transition: transform 0.25s cubic-bezier(.22,1,.36,1),
                box-shadow 0.25s;
    cursor: default;
  }}

  .tl-card:hover {{
    transform: translateX(4px);
    box-shadow: 0 12px 35px rgba(0,0,0,0.4);
  }}

  .tl-card-cyan   {{ border: 1px solid rgba(0,212,255,0.25); }}
  .tl-card-pink   {{ border: 1px solid rgba(255,107,203,0.25); }}
  .tl-card-green  {{ border: 1px solid rgba(52,211,153,0.25); }}
  .tl-card-yellow {{
    border: 1px solid rgba(253,230,138,0.25);
    background: linear-gradient(135deg,rgba(253,230,138,0.04),rgba(245,158,11,0.04));
  }}

  .tl-card-header {{
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 7px;
    margin-bottom: 9px;
  }}

  .tl-year {{
    border-radius: 999px;
    padding: 2px 11px;
    font-size: clamp(0.68rem, 1.6vw, 0.76rem);
    font-weight: 700;
    letter-spacing: 0.1em;
    flex-shrink: 0;
  }}

  .tl-label {{
    font-size: clamp(0.86rem, 2.1vw, 0.98rem);
    font-weight: 700;
    color: var(--text);
    display: flex;
    align-items: center;
    gap: 6px;
  }}

  .tl-label i {{ font-size: 0.88em; flex-shrink: 0; }}

  .tl-in-progress {{
    background: rgba(253,230,138,0.1);
    border: 1px solid rgba(253,230,138,0.25);
    border-radius: 999px;
    padding: 2px 8px;
    font-size: 0.66rem;
    color: var(--yellow);
    white-space: nowrap;
  }}

  .tl-body {{
    font-size: clamp(0.8rem, 1.9vw, 0.88rem);
    color: var(--muted);
    line-height: 1.68;
    margin-bottom: 11px;
  }}

  .tl-body strong {{ color: var(--text); }}

  .pill-row {{ display: flex; flex-wrap: wrap; gap: 5px; }}

  .pill {{
    border-radius: 999px;
    padding: clamp(2px,.5vw,3px) clamp(8px,2vw,11px);
    font-size: clamp(0.66rem, 1.5vw, 0.73rem);
    font-weight: 600;
    transition: transform 0.15s;
  }}

  .pill:hover {{ transform: translateY(-2px); }}

  .pill-red    {{ background:rgba(239,68,68,0.12);   border:1px solid rgba(239,68,68,0.35);   color:#fca5a5; }}
  .pill-blue   {{ background:rgba(59,130,246,0.12);  border:1px solid rgba(59,130,246,0.35);  color:#93c5fd; }}
  .pill-yellow {{ background:rgba(253,224,71,0.10);  border:1px solid rgba(253,224,71,0.28);  color:#fde047; }}
  .pill-sky    {{ background:rgba(56,189,248,0.12);  border:1px solid rgba(56,189,248,0.28);  color:#7dd3fc; }}
  .pill-amber  {{ background:rgba(234,179,8,0.12);   border:1px solid rgba(234,179,8,0.28);   color:#fdba74; }}
  .pill-purple {{ background:rgba(167,139,250,0.12); border:1px solid rgba(167,139,250,0.28); color:#c4b5fd; }}
  .pill-pink   {{ background:rgba(255,107,203,0.10); border:1px solid rgba(255,107,203,0.28); color:#ff6bcb; }}
  .pill-green  {{ background:rgba(22,163,74,0.12);   border:1px solid rgba(22,163,74,0.35);   color:#86efac; }}
  .pill-cyan   {{ background:rgba(0,212,255,0.10);   border:1px solid rgba(0,212,255,0.28);   color:#00d4ff; }}
  .pill-gold   {{ background:rgba(253,230,138,0.10); border:1px solid rgba(253,230,138,0.28); color:#fde68a; }}
  .pill-gray   {{ background:rgba(148,163,184,0.08); border:1px solid rgba(148,163,184,0.2);  color:#9ca3af; }}

  /* ══════════════════════════════════
     PULSE DOT ANIMATION
  ══════════════════════════════════ */
  @keyframes dot-pulse {{
    0%,100% {{ box-shadow: 0 0 0 3px rgba(253,230,138,0.2), 0 0 16px rgba(253,230,138,0.3); }}
    50%     {{ box-shadow: 0 0 0 6px rgba(253,230,138,0.08),0 0 28px rgba(253,230,138,0.55); }}
  }}
  .dot-pulse {{ animation: dot-pulse 2.2s ease-in-out infinite; }}

  /* ══════════════════════════════════
     FOOTER
  ══════════════════════════════════ */
  .footer {{
    margin-top: 30px;
    padding-top: 16px;
    border-top: 1px solid rgba(148,163,184,0.14);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 8px;
    color: #6b7280;
    font-size: clamp(0.7rem, 1.7vw, 0.8rem);
  }}

  .footer strong {{ color: var(--muted); }}
  .footer i {{ margin: 0 3px; }}

  ::-webkit-scrollbar {{ width: 3px; height: 3px; }}
  ::-webkit-scrollbar-track {{ background: transparent; }}
  ::-webkit-scrollbar-thumb {{ background: rgba(0,212,255,0.22); border-radius: 999px; }}
</style>
</head>
<body>

<!-- ══════════════════════════════════════════════
     HERO
═════════════════════════════════════════════════ -->
<div class="hero reveal">
  <div class="hero-inner">

    <!-- Avatar -->
    <div class="avatar-wrap reveal-scale delay-1">
      <div class="avatar-ring">
        <div class="avatar-inner">
          <img
            src="data:image/png;base64,{b64}"
            alt="Dave Campo"
            onerror="this.style.display='none';
                     this.parentElement.innerHTML='<i class=\'fa-solid fa-user avatar-fallback\'></i>';"
          />
        </div>
      </div>
      <div class="avatar-status" title="Available for work"></div>
    </div>

    <!-- Text -->
    <div class="hero-text">
      <p class="hero-eyebrow reveal delay-1">
        <i class="fa-solid fa-circle-info" style="margin-right:5px;"></i>A little bit about me
      </p>

      <h1 class="hero-title reveal delay-2">
        <i class="fa-solid fa-user"></i>About Me
      </h1>

      <p class="hero-body reveal delay-3">
        I'm <strong>Dave Campo</strong>, a <strong>3rd year student</strong> and passionate
        <span class="grad-text">Full Stack Web Developer</span>
        specializing in <strong>Django</strong>.
        I started coding in <strong>2023</strong> and have been building real-world projects
        ever since — from simple scripts to full-stack web applications.
        I love turning ideas into clean, functional products.
      </p>

      <!-- Stats -->
      <div class="stats-row reveal delay-3">
        <div class="stat-chip">
          <div class="stat-num">2+</div>
          <div class="stat-lbl">Yrs coding</div>
        </div>
        <div class="stat-chip">
          <div class="stat-num">10+</div>
          <div class="stat-lbl">Projects</div>
        </div>
        <div class="stat-chip">
          <div class="stat-num">5+</div>
          <div class="stat-lbl">Tech stacks</div>
        </div>
        <div class="stat-chip">
          <div class="stat-num">4th</div>
          <div class="stat-lbl">Year</div>
        </div>
      </div>

      <div class="badges reveal delay-4">
        <span class="badge badge-green">
          <i class="fa-solid fa-graduation-cap"></i>4th Year Student
        </span>
        <span class="badge badge-cyan">
          <i class="fa-solid fa-globe"></i>Full Stack Developer
        </span>
        <span class="badge badge-lime">
          <i class="fa-solid fa-star"></i>Django Specialist
        </span>
      </div>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════════
     TIMELINE SECTION
═════════════════════════════════════════════════ -->
<div class="section-header reveal">
  <div class="section-eyebrow">
    <i class="fa-solid fa-road" style="margin-right:5px;"></i>My Journey
  </div>
  <h2 class="section-title">
    <i class="fa-solid fa-calendar-days"></i>How It All Started
  </h2>
</div>

<div class="timeline">

  <!-- ── 2023 · The Beginning ── -->
  <div class="tl-item reveal reveal-left delay-1">
    <div class="tl-dot" style="
        background:linear-gradient(135deg,#00d4ff,#0ea5e9);
        box-shadow:0 0 0 3px rgba(0,212,255,0.22),0 0 16px rgba(0,212,255,0.4);
    "></div>
    <div class="tl-card tl-card-cyan">
      <div class="tl-card-header">
        <span class="tl-year" style="background:rgba(0,212,255,0.12);border:1px solid rgba(0,212,255,0.35);color:#00d4ff;">2023</span>
        <span class="tl-label">
          <i class="fa-solid fa-rocket" style="color:#00d4ff;"></i>The Beginning
        </span>
      </div>
      <p class="tl-body">
        Started my coding journey from scratch. Learned fundamentals through
        <strong>C</strong> and <strong>C++</strong> — pointers, memory management,
        data structures, and algorithms. Then picked up <strong>Python</strong> and
        discovered how fast you can turn ideas into working code.
        Also worked with <strong>MS Access</strong> for database basics.
      </p>
      <div class="pill-row">
        <span class="pill pill-red">C</span>
        <span class="pill pill-red">C++</span>
        <span class="pill pill-blue">Python</span>
        <span class="pill pill-gray">MS Access</span>
      </div>
    </div>
  </div>

  <!-- ── 2024 · Web Dev ── -->
  <div class="tl-item reveal reveal-left delay-2">
    <div class="tl-dot" style="
        background:linear-gradient(135deg,#ff6bcb,#a78bfa);
        box-shadow:0 0 0 3px rgba(255,107,203,0.22),0 0 16px rgba(255,107,203,0.35);
    "></div>
    <div class="tl-card tl-card-pink">
      <div class="tl-card-header">
        <span class="tl-year" style="background:rgba(255,107,203,0.12);border:1px solid rgba(255,107,203,0.35);color:#ff6bcb;">2024</span>
        <span class="tl-label">
          <i class="fa-solid fa-globe" style="color:#ff6bcb;"></i>Web Development &amp; Databases
        </span>
      </div>
      <p class="tl-body">
        Built my first real web projects with <strong>HTML, CSS &amp; JavaScript</strong>.
        Learned <strong>MySQL</strong> for proper database management.
        Started working with <strong>React</strong> for dynamic, component-based frontends.
        Explored design tools like <strong>Canva</strong> and <strong>Spline</strong>
        for UI/UX and 3D design.
      </p>
      <div class="pill-row">
        <span class="pill pill-amber">HTML</span>
        <span class="pill pill-blue">CSS</span>
        <span class="pill pill-yellow">JavaScript</span>
        <span class="pill pill-sky">React</span>
        <span class="pill pill-amber">MySQL</span>
        <span class="pill pill-purple">Spline</span>
        <span class="pill pill-pink">Canva</span>
      </div>
    </div>
  </div>

  <!-- ── 2025 · Full Stack ── -->
  <div class="tl-item reveal reveal-left delay-3">
    <div class="tl-dot" style="
        background:linear-gradient(135deg,#34d399,#059669);
        box-shadow:0 0 0 3px rgba(52,211,153,0.22),0 0 16px rgba(52,211,153,0.35);
    "></div>
    <div class="tl-card tl-card-green">
      <div class="tl-card-header">
        <span class="tl-year" style="background:rgba(52,211,153,0.12);border:1px solid rgba(52,211,153,0.35);color:#34d399;">2025</span>
        <span class="tl-label">
          <i class="fa-solid fa-bolt" style="color:#34d399;"></i>Full Stack with Django
        </span>
      </div>
      <p class="tl-body">
        Levelled up into full-stack development with <strong>Django</strong> as my main
        backend framework. Built APIs with <strong>Django REST Framework</strong>,
        real-time features with <strong>Django Channels</strong>,
        background tasks with <strong>Celery</strong>, and authentication with
        <strong>Django Allauth</strong>. Started integrating AI using
        <strong>OpenCV, Pandas, NumPy &amp; Streamlit</strong>.
      </p>
      <div class="pill-row">
        <span class="pill pill-green">Django</span>
        <span class="pill pill-green">Django REST</span>
        <span class="pill pill-green">Django Channels</span>
        <span class="pill pill-green">Celery</span>
        <span class="pill pill-blue">OpenCV</span>
        <span class="pill pill-blue">Pandas</span>
        <span class="pill pill-blue">NumPy</span>
        <span class="pill pill-cyan">Streamlit</span>
      </div>
    </div>
  </div>

  <!-- ── 2026 · What's Next ── -->
  <div class="tl-item reveal reveal-left delay-4">
    <div class="tl-dot dot-pulse" style="
        background:linear-gradient(135deg,#fde68a,#f59e0b);
    "></div>
    <div class="tl-card tl-card-yellow">
      <div class="tl-card-header">
        <span class="tl-year" style="background:rgba(253,230,138,0.12);border:1px solid rgba(253,230,138,0.4);color:#fde68a;">2026</span>
        <span class="tl-label">
          <i class="fa-solid fa-circle-info" style="color:#fde68a;"></i>What's Next
        </span>
        <span class="tl-in-progress">
          <i class="fa-solid fa-circle" style="font-size:0.45rem;vertical-align:middle;margin-right:3px;"></i>In Progress
        </span>
      </div>
      <p class="tl-body">
        Graduating soon and pushing deeper into
        <strong>AI, automation &amp; systems design</strong>.
        Building smart tools that think, not just execute.
        The journey is just getting started.
        <i class="fa-solid fa-rocket" style="color:#00d4ff;margin-left:4px;font-size:0.82em;"></i>
      </p>
      <div class="pill-row">
        <span class="pill pill-gold">AI &amp; Automation</span>
        <span class="pill pill-gold">Systems Design</span>
        <span class="pill pill-gold">
          <i class="fa-solid fa-graduation-cap" style="font-size:0.72em;margin-right:3px;"></i>Graduation
        </span>
      </div>
    </div>
  </div>

</div>

<!-- ═══ FOOTER ════════════════════════════════════════════ -->
<div class="footer">
  <div class="footer-left">
    <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13"
         viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2"
         stroke-linecap="round" stroke-linejoin="round">
      <path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/>
      <circle cx="12" cy="10" r="3"/>
    </svg>
    © 2026 <strong>Dave Campo</strong> · Built with Python &amp; Streamlit
  </div>
 <div style="color:#6b7280;font-size:0.78rem;display:flex;
              align-items:center;gap:0.4rem;">
    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12"
         viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2"
         stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="10"></circle>
      <line x1="12" y1="16" x2="12" y2="12"></line>
      <line x1="12" y1="8" x2="12.01" y2="8"></line>
    </svg>
    About Page
 </div>
</div>

<!-- ══════════════════════════════════════════════
     SCROLL REVEAL SCRIPT
═════════════════════════════════════════════════ -->
<script>
(function () {{
  const targets = document.querySelectorAll(
    '.reveal, .reveal-left, .reveal-right, .reveal-scale'
  );

  const io = new IntersectionObserver(
    (entries) => {{
      entries.forEach(entry => {{
        if (entry.isIntersecting) {{
          entry.target.classList.add('visible');
          io.unobserve(entry.target);
        }}
      }});
    }},
    {{ threshold: 0.12, rootMargin: '0px 0px -30px 0px' }}
  );

  targets.forEach(el => io.observe(el));
}})();
</script>

</body>
</html>
""", height=1750, scrolling=True)