import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import streamlit.components.v1 as components
from components import apply_global_effects

st.set_page_config(
    page_title="About | Dave Campo",
    page_icon="user",
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

# ═══════════════════════════════════════════════════════
#                   HERO / ABOUT CARD
# ═══════════════════════════════════════════════════════
components.html("""
<div style="
    font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
    background:rgba(15,23,42,0.96);
    border-radius:18px;
    border:1px solid rgba(148,163,184,0.35);
    padding:2.2rem 2.2rem 2rem;
    box-shadow:0 24px 60px rgba(0,0,0,0.85);
    backdrop-filter:blur(18px);
">
  <p style="font-size:0.82rem;text-transform:uppercase;letter-spacing:0.22em;
            color:#00d4ff;margin:0 0 0.8rem;">A little bit about me</p>

  <h1 style="font-size:2.6rem;font-weight:800;color:#e5e7eb;margin:0 0 1rem;"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-right:8px;"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>About Me</h1>

  <p style="font-size:1rem;color:#9ca3af;line-height:1.75;margin:0 0 1.4rem;">
    I'm <strong style="color:#e5e7eb;">Dave Campo</strong>, a
    <strong style="color:#e5e7eb;">3rd year student</strong> and passionate
    <strong style="
        background:linear-gradient(135deg,#00d4ff,#ff6bcb);
        -webkit-background-clip:text;-webkit-text-fill-color:transparent;
        font-weight:800;
    ">Full Stack Web Developer</strong>
    specializing in <strong style="color:#34d399;">Django</strong>.
    I started coding in <strong style="color:#e5e7eb;">2023</strong> and have been
    building real-world projects ever since to full-stack
    web applications. I love turning ideas into clean, functional products.
  </p>

  <!-- Current status -->
  <div style="
      display:flex;gap:0.6rem;flex-wrap:wrap;margin-bottom:1.4rem;
  ">
    <span style="
        background:rgba(52,211,153,0.12);border:1px solid rgba(52,211,153,0.35);
        border-radius:999px;padding:0.25rem 0.9rem;
        font-size:0.78rem;color:#34d399;font-weight:600;
    "><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#34d399" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-right:4px;"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>4th Year Student</span>
    <span style="
        background:rgba(0,212,255,0.1);border:1px solid rgba(0,212,255,0.3);
        border-radius:999px;padding:0.25rem 0.9rem;
        font-size:0.78rem;color:#00d4ff;font-weight:600;
    "><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-right:4px;"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>Full Stack Web Developer</span>
    <span style="
        background:rgba(22,163,74,0.1);border:1px solid rgba(22,163,74,0.35);
        border-radius:999px;padding:0.25rem 0.9rem;
        font-size:0.78rem;color:#86efac;font-weight:600;
    "><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#86efac" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-right:4px;"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>Django Specialist</span>
  </div>

  </div>
</div>
""", height=460)

# ═══════════════════════════════════════════════════════
#            JOURNEY TIMELINE
# ═══════════════════════════════════════════════════════
components.html("""
<div style="
    font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
    margin-top:1rem;
">
  <div style="font-size:0.78rem;text-transform:uppercase;letter-spacing:0.2em;
              color:#ff6bcb;margin-bottom:0.4rem;">My Journey</div>
  <h2 style="font-size:1.85rem;font-weight:800;color:#e5e7eb;margin:0 0 1.6rem;">
    <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#ff6bcb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-right:8px;"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21"/></svg>How It All Started</h2>

  <div style="position:relative;padding-left:2rem;">

    <!-- Vertical line -->
    <div style="
        position:absolute;left:7px;top:8px;bottom:8px;
        width:2px;
        background:linear-gradient(to bottom,#00d4ff,#ff6bcb,rgba(148,163,184,0.2));
        border-radius:999px;
    "></div>

    <!-- ── 2023 · The Beginning ── -->
    <div style="position:relative;margin-bottom:2rem;">
      <div style="
          position:absolute;left:-1.72rem;top:4px;
          width:14px;height:14px;border-radius:50%;
          background:linear-gradient(135deg,#00d4ff,#0ea5e9);
          box-shadow:0 0 0 4px rgba(0,212,255,0.2),0 0 18px rgba(0,212,255,0.4);
      "></div>

      <div style="
          background:rgba(15,23,42,0.96);
          border:1px solid rgba(0,212,255,0.3);
          border-radius:14px;padding:1.2rem 1.4rem;
      ">
        <div style="display:flex;align-items:center;gap:0.7rem;margin-bottom:0.6rem;flex-wrap:wrap;">
          <span style="
              background:rgba(0,212,255,0.12);border:1px solid rgba(0,212,255,0.35);
              border-radius:999px;padding:0.2rem 0.9rem;
              font-size:0.78rem;color:#00d4ff;font-weight:700;letter-spacing:0.1em;
          ">2023</span>
          <span style="font-size:1rem;font-weight:700;color:#e5e7eb;"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-right:4px;"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/></svg>The Beginning</span>
        </div>
        <p style="color:#9ca3af;font-size:0.9rem;line-height:1.6;margin:0 0 0.9rem;">
          Started my coding journey from scratch. Learned programming fundamentals through
          <strong style="color:#e5e7eb;">C</strong> and
          <strong style="color:#e5e7eb;">C++</strong> — pointers, memory management,
          data structures, and algorithms. Then picked up
          <strong style="color:#e5e7eb;">Python</strong> and discovered how fast
          you can turn ideas into working code. Also worked with
          <strong style="color:#e5e7eb;">MS Access</strong> for database basics.
        </p>
        <div style="display:flex;flex-wrap:wrap;gap:0.4rem;">
          <span style="background:rgba(239,68,68,0.12);border:1px solid rgba(239,68,68,0.35);
                border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#fca5a5;font-weight:600;">C</span>
          <span style="background:rgba(239,68,68,0.12);border:1px solid rgba(239,68,68,0.35);
                border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#fca5a5;font-weight:600;">C++</span>
          <span style="background:rgba(59,130,246,0.12);border:1px solid rgba(59,130,246,0.35);
                border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#93c5fd;font-weight:600;">Python</span>
          <span style="background:rgba(148,163,184,0.08);border:1px solid rgba(148,163,184,0.2);
                border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#9ca3af;font-weight:600;">MS Access</span>
        </div>
      </div>
    </div>

    <!-- ── 2024 · Web Dev & Frontend ── -->
    <div style="position:relative;margin-bottom:2rem;">
      <div style="
          position:absolute;left:-1.72rem;top:4px;
          width:14px;height:14px;border-radius:50%;
          background:linear-gradient(135deg,#ff6bcb,#a78bfa);
          box-shadow:0 0 0 4px rgba(255,107,203,0.2),0 0 18px rgba(255,107,203,0.35);
      "></div>

      <div style="
          background:rgba(15,23,42,0.96);
          border:1px solid rgba(255,107,203,0.3);
          border-radius:14px;padding:1.2rem 1.4rem;
      ">
        <div style="display:flex;align-items:center;gap:0.7rem;margin-bottom:0.6rem;flex-wrap:wrap;">
          <span style="
              background:rgba(255,107,203,0.12);border:1px solid rgba(255,107,203,0.35);
              border-radius:999px;padding:0.2rem 0.9rem;
              font-size:0.78rem;color:#ff6bcb;font-weight:700;letter-spacing:0.1em;
          ">2024</span>
          <span style="font-size:1rem;font-weight:700;color:#e5e7eb;"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ff6bcb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-right:4px;"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>Web Development & Databases</span>
        </div>
        <p style="color:#9ca3af;font-size:0.9rem;line-height:1.6;margin:0 0 0.9rem;">
          Built my first real web projects with
          <strong style="color:#e5e7eb;">HTML, CSS & JavaScript</strong>.
          Learned <strong style="color:#e5e7eb;">MySQL</strong> for proper database management.
          Started working with <strong style="color:#e5e7eb;">React</strong> for
          dynamic, component-based frontends.
          Explored design tools like
          <strong style="color:#e5e7eb;">Canva</strong> and
          <strong style="color:#e5e7eb;">Spline</strong> for UI/UX and 3D design.
        </p>
        <div style="display:flex;flex-wrap:wrap;gap:0.4rem;">
          <span style="background:rgba(251,146,60,0.12);border:1px solid rgba(251,146,60,0.35);
                border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#fdba74;font-weight:600;">HTML</span>
          <span style="background:rgba(59,130,246,0.12);border:1px solid rgba(59,130,246,0.35);
                border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#93c5fd;font-weight:600;">CSS</span>
          <span style="background:rgba(253,224,71,0.12);border:1px solid rgba(253,224,71,0.3);
                border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#fde047;font-weight:600;">JavaScript</span>
          <span style="background:rgba(56,189,248,0.12);border:1px solid rgba(56,189,248,0.3);
                border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#7dd3fc;font-weight:600;">React</span>
          <span style="background:rgba(234,179,8,0.12);border:1px solid rgba(234,179,8,0.3);
                border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#fde68a;font-weight:600;">MySQL</span>
          <span style="background:rgba(167,139,250,0.12);border:1px solid rgba(167,139,250,0.3);
                border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#c4b5fd;font-weight:600;">Spline</span>
          <span style="background:rgba(255,107,203,0.1);border:1px solid rgba(255,107,203,0.3);
                border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#ff6bcb;font-weight:600;">Canva</span>
        </div>
      </div>
    </div>

    <!-- ── 2025 · Full Stack Django ── -->
    <div style="position:relative;margin-bottom:2rem;">
      <div style="
          position:absolute;left:-1.72rem;top:4px;
          width:14px;height:14px;border-radius:50%;
          background:linear-gradient(135deg,#34d399,#059669);
          box-shadow:0 0 0 4px rgba(52,211,153,0.2),0 0 18px rgba(52,211,153,0.35);
      "></div>

      <div style="
          background:rgba(15,23,42,0.96);
          border:1px solid rgba(52,211,153,0.3);
          border-radius:14px;padding:1.2rem 1.4rem;
      ">
        <div style="display:flex;align-items:center;gap:0.7rem;margin-bottom:0.6rem;flex-wrap:wrap;">
          <span style="
              background:rgba(52,211,153,0.12);border:1px solid rgba(52,211,153,0.35);
              border-radius:999px;padding:0.2rem 0.9rem;
              font-size:0.78rem;color:#34d399;font-weight:700;letter-spacing:0.1em;
          ">2025</span>
          <span style="font-size:1rem;font-weight:700;color:#e5e7eb;"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#34d399" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-right:4px;"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>Full Stack with Django</span>
        </div>
        <p style="color:#9ca3af;font-size:0.9rem;line-height:1.6;margin:0 0 0.9rem;">
          Levelled up into full-stack development with
          <strong style="color:#e5e7eb;">Django</strong> as my main backend framework.
          Built APIs with <strong style="color:#e5e7eb;">Django REST Framework</strong>,
          added real-time features with <strong style="color:#e5e7eb;">Django Channels</strong>,
          background tasks with <strong style="color:#e5e7eb;">Celery</strong>,
          and authentication with <strong style="color:#e5e7eb;">Django Allauth</strong>.
          Started integrating AI into projects using
          <strong style="color:#e5e7eb;">OpenCV, Pandas, NumPy & Streamlit</strong>.
        </p>
        <div style="display:flex;flex-wrap:wrap;gap:0.4rem;">
          <span style="background:rgba(22,163,74,0.12);border:1px solid rgba(22,163,74,0.35);
                border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#86efac;font-weight:600;">Django</span>
          <span style="background:rgba(22,163,74,0.12);border:1px solid rgba(22,163,74,0.35);
                border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#86efac;font-weight:600;">Django REST</span>
          <span style="background:rgba(22,163,74,0.12);border:1px solid rgba(22,163,74,0.35);
                border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#86efac;font-weight:600;">Django Channels</span>
          <span style="background:rgba(22,163,74,0.12);border:1px solid rgba(22,163,74,0.35);
                border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#86efac;font-weight:600;">Celery</span>
          <span style="background:rgba(59,130,246,0.12);border:1px solid rgba(59,130,246,0.35);
                border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#93c5fd;font-weight:600;">OpenCV</span>
          <span style="background:rgba(59,130,246,0.12);border:1px solid rgba(59,130,246,0.35);
                border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#93c5fd;font-weight:600;">Pandas</span>
          <span style="background:rgba(0,212,255,0.12);border:1px solid rgba(0,212,255,0.3);
                border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#00d4ff;font-weight:600;">Streamlit</span>
        </div>
      </div>
    </div>

    <!-- ── 2026 · What's Next ── -->
    <div style="position:relative;margin-bottom:0.5rem;">
      <div style="
          position:absolute;left:-1.72rem;top:4px;
          width:14px;height:14px;border-radius:50%;
          background:linear-gradient(135deg,#fde68a,#f59e0b);
          box-shadow:0 0 0 4px rgba(253,230,138,0.2),0 0 18px rgba(253,230,138,0.35);
          animation: pulse 2s infinite;
      "></div>

      <div style="
          background:linear-gradient(135deg,rgba(253,230,138,0.05),rgba(245,158,11,0.05));
          border:1px solid rgba(253,230,138,0.3);
          border-radius:14px;padding:1.2rem 1.4rem;
      ">
        <div style="display:flex;align-items:center;gap:0.7rem;margin-bottom:0.6rem;flex-wrap:wrap;">
          <span style="
              background:rgba(253,230,138,0.12);border:1px solid rgba(253,230,138,0.4);
              border-radius:999px;padding:0.2rem 0.9rem;
              font-size:0.78rem;color:#fde68a;font-weight:700;letter-spacing:0.1em;
          ">2026</span>
          <span style="font-size:1rem;font-weight:700;color:#e5e7eb;"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fde68a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-right:4px;"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>What's Next</span>
          <span style="
              background:rgba(253,230,138,0.1);border:1px solid rgba(253,230,138,0.25);
              border-radius:999px;padding:0.12rem 0.6rem;
              font-size:0.68rem;color:#fde68a;
          ">● In Progress</span>
        </div>
        <p style="color:#9ca3af;font-size:0.9rem;line-height:1.6;margin:0 0 0.9rem;">
          Graduating soon and pushing deeper into
          <strong style="color:#e5e7eb;">AI, automation & systems design</strong>.
          Building smart tools that think, not just execute.
          The journey is just getting started.<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-left:4px;"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/></svg>
        </p>
        <div style="display:flex;flex-wrap:wrap;gap:0.4rem;">
          <span style="background:rgba(253,230,138,0.1);border:1px solid rgba(253,230,138,0.3);
                border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#fde68a;font-weight:600;">AI & Automation</span>
          <span style="background:rgba(253,230,138,0.1);border:1px solid rgba(253,230,138,0.3);
                border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#fde68a;font-weight:600;">Systems Design</span>
          <span style="background:rgba(253,230,138,0.1);border:1px solid rgba(253,230,138,0.3);
                border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#fde68a;font-weight:600;">Graduation<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fde68a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-left:4px;"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg></span>
        </div>
      </div>
    </div>

  </div>
</div>

<style>
@keyframes pulse {
  0%,100% { box-shadow: 0 0 0 4px rgba(253,230,138,0.2), 0 0 18px rgba(253,230,138,0.35); }
  50%     { box-shadow: 0 0 0 7px rgba(253,230,138,0.1), 0 0 30px rgba(253,230,138,0.6); }
}
</style>
""", height=1150)
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