import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
import streamlit.components.v1 as components
import base64
from components import apply_global_effects

st.set_page_config(
    page_title="Dave Campo | Portfolio",
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

a[data-testid="stLinkButton"] {
    border-radius: 999px !important;
    border: 1px solid rgba(148,163,184,0.4) !important;
    background: rgba(15,23,42,0.9) !important;
    color: #e5e7eb !important;
    font-size: 0.88rem !important;
    transition: all 0.2s !important;
}
a[data-testid="stLinkButton"]:hover {
    border-color: #00d4ff !important;
    background: linear-gradient(135deg,#00d4ff,#ff6bcb) !important;
    color: #000 !important;
}

hr { border-color: rgba(148,163,184,0.2) !important; margin: 2rem 0 !important; }
iframe { display: block; border: none !important; }

@keyframes floatUp {
    from { opacity:0; transform:translateY(12px); }
    to   { opacity:1; transform:translateY(0); }
}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
#                    HERO SECTION
# ═══════════════════════════════════════════════════════
with st.container():
    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        with open("assets/profile/profile.png", "rb") as f:
            b64 = base64.b64encode(f.read()).decode()

        components.html(f"""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
        <div style="
            width:270px; max-width:100%; aspect-ratio:1;
            border-radius:26px;
            background: radial-gradient(circle at top,rgba(56,189,248,0.3),transparent 60%),
                        linear-gradient(145deg,#020617,#0f172a);
            border:1px solid rgba(148,163,184,0.3);
            box-shadow:
                0 0 0 1px rgba(0,212,255,0.08),
                0 24px 60px rgba(0,0,0,0.9),
                0 0 80px rgba(0,212,255,0.08);
            overflow:hidden;
            padding:5px;
            animation: floatUp 0.85s ease-out both;
            margin: 0 auto;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        "
        onmouseover="this.style.transform='translateY(-6px) scale(1.02)';
                     this.style.boxShadow='0 0 0 1px rgba(0,212,255,0.15), 0 32px 70px rgba(0,0,0,0.95), 0 0 100px rgba(0,212,255,0.15)';"
        onmouseout="this.style.transform='translateY(0) scale(1)';
                    this.style.boxShadow='0 0 0 1px rgba(0,212,255,0.08), 0 24px 60px rgba(0,0,0,0.9), 0 0 80px rgba(0,212,255,0.08)';"
        >
          <img
            src="data:image/png;base64,{b64}"
            style="
                width:100%; height:100%;
                border-radius:22px;
                object-fit:cover;
                filter:saturate(1.15);
                display:block;
            "
            alt="Dave Campo"
          />
        </div>

        <style>
        @keyframes floatUp {{
          from {{ opacity:0; transform:translateY(12px); }}
          to   {{ opacity:1; transform:translateY(0); }}
        }}
        </style>
        """, height=295)

    with col2:
        components.html("""
        <!DOCTYPE html>
        <html>
        <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
        <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { background: transparent; }

        @keyframes floatUp {
          from { opacity:0; transform:translateY(12px); }
          to   { opacity:1; transform:translateY(0); }
        }

        .hero-wrapper {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            animation: floatUp 0.9s ease-out 0.05s both;
            padding-top: 0.3rem;
        }

        /* ── Eyebrow ── */
        .eyebrow {
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 0.22em;
            color: #00d4ff;
            font-weight: 600;
            margin: 0 0 0.85rem;
            opacity: 0.9;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            flex-wrap: wrap;
        }

        .eyebrow-sep {
            color: rgba(148,163,184,0.4);
            font-size: 0.6rem;
        }

        .eyebrow i {
            font-size: 0.75rem;
            opacity: 0.85;
        }

        /* ── Heading ── */
        .heading {
            font-size: 3.3rem;
            font-weight: 800;
            line-height: 1.08;
            color: #e5e7eb;
            margin: 0 0 0.85rem;
            display: flex;
            align-items: center;
            gap: 0.4rem;
            flex-wrap: wrap;
        }

        .heading-icon {
            font-size: 2rem;
            background: linear-gradient(135deg, #00d4ff, #ff6bcb);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-right: 6px;
            flex-shrink: 0;
        }

        /* ── Typing + Glitch Name ── */
        .name-wrap {
            display: inline-flex;
            align-items: center;
        }

        .name-text {
            background: linear-gradient(120deg, #00d4ff, #ff6bcb);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            display: inline-block;
            position: relative;
        }

        .cursor {
            display: inline-block;
            width: 3px;
            height: 3.3rem;
            background: linear-gradient(180deg, #00d4ff, #ff6bcb);
            margin-left: 2px;
            vertical-align: middle;
            animation: blink 0.8s step-end infinite;
            border-radius: 2px;
            opacity: 0;
        }

        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0; }
        }

        /* Glitch effect */
        .glitch { position: relative; }

        .glitch::before,
        .glitch::after {
            content: attr(data-text);
            position: absolute;
            top: 0; left: 0;
            background: linear-gradient(120deg, #00d4ff, #ff6bcb);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            opacity: 0;
        }

        .glitch::before {
            animation: glitchTop 3s infinite linear;
            clip-path: polygon(0 0, 100% 0, 100% 35%, 0 35%);
            transform: translateX(-2px);
        }

        .glitch::after {
            animation: glitchBot 3s infinite linear;
            clip-path: polygon(0 65%, 100% 65%, 100% 100%, 0 100%);
            transform: translateX(2px);
        }

        @keyframes glitchTop {
            0%, 80%, 100% { opacity: 0; transform: translateX(0); }
            82% { opacity: 0.9; transform: translateX(-4px); filter: hue-rotate(90deg); }
            84% { opacity: 0; transform: translateX(3px); }
            86% { opacity: 0.7; transform: translateX(-2px); }
            88% { opacity: 0; }
        }

        @keyframes glitchBot {
            0%, 80%, 100% { opacity: 0; transform: translateX(0); }
            83% { opacity: 0.9; transform: translateX(4px); filter: hue-rotate(-90deg); }
            85% { opacity: 0; transform: translateX(-3px); }
            87% { opacity: 0.7; transform: translateX(2px); }
            89% { opacity: 0; }
        }

        @keyframes rgbFlicker {
            0%, 79%, 100% { text-shadow: none; }
            80% {
                text-shadow:
                    -3px 0 rgba(255, 0, 100, 0.8),
                     3px 0 rgba(0, 212, 255, 0.8);
            }
            81% { text-shadow: none; }
            83% {
                text-shadow:
                    2px 0 rgba(255, 107, 203, 0.9),
                    -2px 0 rgba(0, 212, 255, 0.9);
            }
            85% { text-shadow: none; }
        }

        /* ── Bio ── */
        .bio {
            font-size: 1.05rem;
            color: #9ca3af;
            max-width: 36rem;
            line-height: 1.75;
            margin: 0 0 1.4rem;
        }

        .bio i {
            margin-right: 4px;
            font-size: 0.9rem;
        }

        /* ── Stat pills ── */
        .stats-row {
            display: flex;
            gap: 0.6rem;
            flex-wrap: wrap;
            margin-top: 1.2rem;
        }

        .stat-pill {
            display: flex;
            align-items: center;
            gap: 0.4rem;
            background: rgba(15,23,42,0.85);
            border: 1px solid rgba(148,163,184,0.2);
            border-radius: 999px;
            padding: 0.3rem 0.85rem;
            font-size: 0.8rem;
            color: #9ca3af;
            transition: border-color 0.2s;
        }

        .stat-pill:hover { border-color: rgba(0,212,255,0.4); }

        .stat-pill i {
            font-size: 0.75rem;
            color: #00d4ff;
        }
        </style>
        </head>
        <body>
        <div class="hero-wrapper">

          <!-- Eyebrow -->
          <p class="eyebrow">
            <i class="fa-solid fa-code"></i>Full-Stack Developer
            <span class="eyebrow-sep">&#9670;</span>
            <i class="fa-brands fa-python"></i>Django Specialist
            <span class="eyebrow-sep">&#9670;</span>
            <i class="fa-solid fa-graduation-cap"></i>3rd Year Student
          </p>

          <!-- Heading -->
          <h1 class="heading">
            <i class="fa-solid fa-hand-wave heading-icon"></i>
            Hi, I'm
            <span class="name-wrap">
              <span
                class="name-text glitch"
                id="nameEl"
                data-text="Dave"
                style="min-width:120px;"
              ></span>
              <span class="cursor" id="cursor"></span>
            </span>
          </h1>

          <!-- Bio -->
          <p class="bio">
            I build clean, fast, and real web applications — from backend APIs
            to smooth frontends. Specializing in
            <strong style="color:#86efac;">
              <i class="fa-brands fa-python"></i>Django
            </strong>,
            <strong style="color:#93c5fd;">
              <i class="fa-solid fa-snake"></i>Python
            </strong>, and
            <strong style="color:#7dd3fc;">
              <i class="fa-brands fa-react"></i>React
            </strong>.
            Currently a
            <strong style="color:#e5e7eb;">
              <i class="fa-solid fa-graduation-cap" style="color:#fde68a;"></i>
              3rd year CS student
            </strong>
            turning ideas into products.
          </p>

          <!-- Stat pills -->
          <div class="stats-row">
            <div class="stat-pill">
              <i class="fa-solid fa-briefcase"></i> 4+ Projects
            </div>
            <div class="stat-pill">
              <i class="fa-solid fa-calendar-days"></i> 2024 – Present
            </div>
            <div class="stat-pill">
              <i class="fa-solid fa-location-dot"></i> Philippines
            </div>
            <div class="stat-pill">
              <i class="fa-solid fa-circle" style="color:#34d399;font-size:0.5rem;"></i>
              Open to work
            </div>
          </div>

        </div>

        <script>
        const nameEl   = document.getElementById('nameEl');
        const cursor   = document.getElementById('cursor');
        const fullName = 'Dave';
        let charIndex  = 0;
        let typed      = false;

        function typeChar() {
            if (charIndex < fullName.length) {
                nameEl.textContent = fullName.slice(0, charIndex + 1);
                nameEl.setAttribute('data-text', nameEl.textContent);
                charIndex++;
                cursor.style.opacity = '1';
                setTimeout(typeChar, 110 + Math.random() * 60);
            } else {
                typed = true;
                setTimeout(() => {
                    cursor.style.animation = 'none';
                    cursor.style.opacity   = '0';
                }, 1800);
                setTimeout(triggerGlitch, 2200);
            }
        }

        function triggerGlitch() {
            nameEl.style.animation = 'rgbFlicker 0.6s steps(1) forwards';
            setTimeout(() => { nameEl.style.animation = ''; }, 700);
        }

        setInterval(() => { if (typed) triggerGlitch(); }, 4000);
        setTimeout(typeChar, 600);
        </script>
        </body>
        </html>
        """, height=380)

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