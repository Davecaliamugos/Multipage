import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import streamlit.components.v1 as components
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
hr { border-color: rgba(148,163,184,0.2) !important; margin: 1.5rem 0 !important; }
iframe { display: block; border: none !important; }
</style>
""", unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no"/>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
<style>
  *, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }

  :root {
    --cyan:   #00d4ff;
    --pink:   #ff6bcb;
    --green:  #34d399;
    --yellow: #fde68a;
    --surface: rgba(15,23,42,0.96);
    --border:  rgba(148,163,184,0.18);
    --text:    #e5e7eb;
    --muted:   #9ca3af;
  }

  html { font-size: 16px; }

  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: transparent;
    color: var(--text);
    padding: 0;
    overflow-x: hidden;
  }

  /* ════════════════════════════════
     HERO SECTION
  ════════════════════════════════ */
  .hero {
    background: var(--surface);
    border-radius: 16px;
    border: 1px solid rgba(148,163,184,0.3);
    padding: clamp(1.2rem, 4vw, 2.2rem);
    box-shadow: 0 24px 60px rgba(0,0,0,0.8);
    backdrop-filter: blur(18px);
    margin-bottom: 20px;
  }

  .hero-eyebrow {
    font-size: clamp(0.68rem, 1.5vw, 0.82rem);
    text-transform: uppercase;
    letter-spacing: 0.22em;
    color: var(--cyan);
    margin-bottom: 0.6rem;
  }

  .hero-title {
    font-size: clamp(1.6rem, 5vw, 2.6rem);
    font-weight: 800;
    color: var(--text);
    margin-bottom: 0.5rem;
    line-height: 1.15;
  }

  .hero-title i { color: var(--cyan); margin-right: 0.4rem; }

  .hero-sub {
    font-size: clamp(0.85rem, 2vw, 1rem);
    color: var(--muted);
    line-height: 1.65;
  }

  /* ════════════════════════════════
     FILTER BAR
  ════════════════════════════════ */
  .filter-bar {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 20px;
    align-items: center;
  }

  .filter-label {
    color: var(--muted);
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    flex-shrink: 0;
  }

  .filter-btn {
    background: rgba(15,23,42,0.9);
    border: 1px solid rgba(148,163,184,0.22);
    border-radius: 999px;
    color: var(--muted);
    font-size: clamp(0.72rem, 1.8vw, 0.82rem);
    padding: 6px 14px;
    cursor: pointer;
    transition: all 0.2s;
    font-family: inherit;
    white-space: nowrap;
  }

  .filter-btn:hover { border-color: rgba(0,212,255,0.5); color: var(--cyan); }
  .filter-btn.active {
    background: rgba(0,212,255,0.12);
    border-color: var(--cyan);
    color: var(--cyan);
    font-weight: 700;
  }

  /* ════════════════════════════════
     GRID
  ════════════════════════════════ */
  .grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
  }

  @media (max-width: 900px) {
    .grid { grid-template-columns: repeat(2, 1fr); }
  }

  @media (max-width: 540px) {
    .grid { grid-template-columns: 1fr; }
  }

  /* ════════════════════════════════
     CARD
  ════════════════════════════════ */
  .card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
    cursor: pointer;
    transition: transform 0.25s, border-color 0.25s, box-shadow 0.25s;
    position: relative;
    display: flex;
    flex-direction: column;
  }

  @media (hover: hover) {
    .card:hover {
      transform: translateY(-5px);
      border-color: rgba(0,212,255,0.4);
      box-shadow: 0 18px 45px rgba(0,0,0,0.65), 0 0 0 1px rgba(0,212,255,0.12);
    }
  }

  .card:active { transform: scale(0.98); }

  /* Card image */
  .card-img {
    width: 100%;
    aspect-ratio: 16 / 9;
    position: relative;
    overflow: hidden;
    background: #0a0f1e;
  }

  .card-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top;
    transition: transform 0.4s;
    display: block;
  }

  @media (hover: hover) {
    .card:hover .card-img img { transform: scale(1.05); }
  }

  .card-placeholder {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .card-placeholder i { font-size: clamp(2rem, 5vw, 3.2rem); opacity: 0.65; }

  /* Overlays on image */
  .card-status-badge {
    position: absolute;
    top: 10px;
    right: 10px;
    border-radius: 999px;
    padding: 4px 10px;
    font-size: 0.68rem;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 4px;
    backdrop-filter: blur(8px);
    white-space: nowrap;
  }

  .card-year-badge {
    position: absolute;
    bottom: 10px;
    left: 10px;
    background: rgba(2,6,23,0.78);
    border: 1px solid rgba(148,163,184,0.2);
    border-radius: 999px;
    padding: 3px 10px;
    font-size: 0.66rem;
    color: var(--muted);
    display: flex;
    align-items: center;
    gap: 4px;
    backdrop-filter: blur(6px);
  }

  .card-hover-cta {
    position: absolute;
    inset: 0;
    background: rgba(0,212,255,0.07);
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity 0.25s;
  }

  @media (hover: hover) {
    .card:hover .card-hover-cta { opacity: 1; }
  }

  .card-hover-cta span {
    background: rgba(0,212,255,0.92);
    color: #000;
    font-weight: 800;
    font-size: 0.82rem;
    padding: 8px 18px;
    border-radius: 999px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  /* Card body */
  .card-body {
    padding: clamp(10px, 3vw, 15px) clamp(12px, 3vw, 16px) clamp(12px, 3vw, 16px);
    display: flex;
    flex-direction: column;
    flex: 1;
  }

  .card-title {
    font-size: clamp(0.9rem, 2.2vw, 1.05rem);
    font-weight: 800;
    color: var(--text);
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 8px;
    line-height: 1.3;
  }

  .card-title i { font-size: 0.95em; flex-shrink: 0; }

  .card-desc {
    font-size: clamp(0.76rem, 1.8vw, 0.83rem);
    color: var(--muted);
    line-height: 1.55;
    margin-bottom: 12px;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    flex: 1;
  }

  .card-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 5px;
  }

  .tag {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(148,163,184,0.18);
    border-radius: 6px;
    padding: 3px 9px;
    font-size: clamp(0.65rem, 1.5vw, 0.72rem);
    color: var(--muted);
    font-weight: 500;
  }

  /* ════════════════════════════════
     MODAL BACKDROP
  ════════════════════════════════ */
  .modal-backdrop {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(2,6,23,0.88);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    z-index: 9999;
    align-items: center;
    justify-content: center;
    padding: clamp(8px, 3vw, 20px);
    animation: bdFadeIn 0.2s ease;
    overflow-y: auto;
  }

  .modal-backdrop.open { display: flex; }

  @keyframes bdFadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
  }

  /* ════════════════════════════════
     MODAL PANEL
  ════════════════════════════════ */
  .modal {
    background: rgba(15,23,42,0.99);
    border: 1px solid rgba(148,163,184,0.22);
    border-radius: 20px;
    width: 100%;
    max-width: 620px;
    max-height: calc(100vh - 32px);
    overflow-y: auto;
    box-shadow: 0 40px 100px rgba(0,0,0,0.95);
    animation: modalUp 0.25s ease;
    scrollbar-width: thin;
    scrollbar-color: rgba(0,212,255,0.3) transparent;
    position: relative;
    margin: auto;
  }

  .modal::-webkit-scrollbar { width: 3px; }
  .modal::-webkit-scrollbar-thumb { background: rgba(0,212,255,0.3); border-radius: 999px; }

  @keyframes modalUp {
    from { transform: translateY(28px); opacity: 0; }
    to   { transform: translateY(0);    opacity: 1; }
  }

  /* Modal image */
  .modal-img {
    width: 100%;
    aspect-ratio: 16 / 8;
    position: relative;
    border-radius: 20px 20px 0 0;
    overflow: hidden;
  }

  .modal-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top;
    display: block;
  }

  .modal-img-placeholder {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .modal-img-placeholder i { font-size: clamp(3.5rem, 8vw, 5rem); opacity: 0.55; }

  /* Close button */
  .modal-close {
    position: absolute;
    top: 12px;
    right: 12px;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: rgba(2,6,23,0.82);
    border: 1px solid rgba(148,163,184,0.28);
    color: var(--text);
    font-size: 0.9rem;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.15s, border-color 0.15s, color 0.15s;
    z-index: 10;
    flex-shrink: 0;
  }

  .modal-close:hover {
    background: rgba(255,107,203,0.18);
    border-color: var(--pink);
    color: var(--pink);
  }

  /* Modal content */
  .modal-content {
    padding: clamp(14px, 4vw, 22px) clamp(16px, 4vw, 24px) clamp(20px, 4vw, 28px);
  }

  .modal-header {
    display: flex;
    align-items: flex-start;
    gap: clamp(10px, 3vw, 14px);
    margin-bottom: 12px;
  }

  .modal-icon-box {
    width: clamp(42px, 8vw, 52px);
    height: clamp(42px, 8vw, 52px);
    border-radius: 13px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    border: 1px solid rgba(0,212,255,0.3);
    background: linear-gradient(135deg,rgba(0,212,255,0.12),rgba(255,107,203,0.12));
  }

  .modal-icon-box i { font-size: clamp(1.2rem, 3vw, 1.5rem); }

  .modal-title-block { flex: 1; min-width: 0; }

  .modal-title {
    font-size: clamp(1.1rem, 3.5vw, 1.4rem);
    font-weight: 800;
    color: var(--text);
    margin-bottom: 7px;
    word-break: break-word;
  }

  .modal-badges {
    display: flex;
    gap: 5px;
    flex-wrap: wrap;
  }

  .badge {
    border-radius: 999px;
    padding: clamp(2px,0.5vw,4px) clamp(8px,2vw,11px);
    font-size: clamp(0.65rem, 1.5vw, 0.73rem);
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    white-space: nowrap;
  }

  .modal-desc {
    font-size: clamp(0.85rem, 2.2vw, 0.93rem);
    color: var(--muted);
    line-height: 1.7;
    margin-bottom: 18px;
  }

  /* Section label */
  .section-label {
    font-size: clamp(0.62rem, 1.5vw, 0.7rem);
    text-transform: uppercase;
    letter-spacing: 0.18em;
    color: #6b7280;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .section-label i { color: var(--cyan); }

  /* Tech */
  .tech-row {
    display: flex;
    flex-wrap: wrap;
    gap: 7px;
    margin-bottom: 18px;
  }

  .tech-tag {
    background: rgba(0,212,255,0.08);
    border: 1px solid rgba(0,212,255,0.28);
    border-radius: 8px;
    padding: clamp(4px, 1vw, 6px) clamp(10px, 2vw, 14px);
    font-size: clamp(0.74rem, 1.8vw, 0.82rem);
    color: var(--cyan);
    font-weight: 600;
  }

  /* Features */
  .features-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 7px;
    margin-bottom: 20px;
  }

  @media (max-width: 400px) {
    .features-grid { grid-template-columns: 1fr; }
  }

  .feature-item {
    display: flex;
    align-items: center;
    gap: 8px;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(148,163,184,0.1);
    border-radius: 10px;
    padding: clamp(6px, 1.5vw, 9px) clamp(8px, 2vw, 12px);
    font-size: clamp(0.76rem, 1.8vw, 0.83rem);
    color: var(--muted);
    line-height: 1.3;
  }

  .feature-item i { color: var(--cyan); font-size: 0.75rem; flex-shrink: 0; }

  /* Action buttons */
  .modal-actions {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
  }

  .action-btn {
    flex: 1;
    min-width: clamp(110px, 30vw, 140px);
    padding: clamp(9px, 2vw, 11px) clamp(14px, 3vw, 20px);
    border-radius: 12px;
    font-size: clamp(0.82rem, 2vw, 0.9rem);
    font-weight: 700;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    text-decoration: none;
    transition: opacity 0.15s, transform 0.12s;
    font-family: inherit;
    border: none;
    text-align: center;
  }

  .action-btn:hover  { opacity: 0.85; }
  .action-btn:active { transform: scale(0.97); }

  .btn-live   { background: linear-gradient(135deg, var(--cyan), var(--pink)); color: #000; }
  .btn-source { background: rgba(255,255,255,0.05); border: 1px solid rgba(148,163,184,0.22) !important; color: var(--text); }

  /* ════════════════════════════════
     EMPTY STATE
  ════════════════════════════════ */
  .empty-state {
    grid-column: 1 / -1;
    text-align: center;
    padding: 3rem 1rem;
    color: var(--muted);
  }

  .empty-state i { font-size: 2.5rem; color: rgba(148,163,184,0.3); margin-bottom: 12px; display: block; }
  .empty-state p { font-size: 0.95rem; }

  /* ════════════════════════════════
     FOOTER
  ════════════════════════════════ */
  .footer {
    margin-top: 28px;
    padding-top: 16px;
    border-top: 1px solid rgba(148,163,184,0.15);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 8px;
    color: #6b7280;
    font-size: clamp(0.74rem, 1.8vw, 0.82rem);
  }

  .footer strong { color: var(--muted); }
  .footer i { margin: 0 3px; }

  /* ════════════════════════════════
     SCROLLBAR (webkit)
  ════════════════════════════════ */
  ::-webkit-scrollbar { width: 4px; height: 4px; }
  ::-webkit-scrollbar-track { background: transparent; }
  ::-webkit-scrollbar-thumb { background: rgba(0,212,255,0.25); border-radius: 999px; }
</style>
</head>
<body>

<!-- ── Hero ─────────────────────────────────── -->
<div class="hero">
  <p class="hero-eyebrow">
    <i class="fa-solid fa-code" style="margin-right:6px;"></i>Selected work
  </p>
  <h1 class="hero-title">
    <i class="fa-solid fa-briefcase"></i>Projects
  </h1>
  <p class="hero-sub">
    A glimpse into some of the projects I've built — tap any card to explore details.
  </p>
</div>

<!-- ── Filter Bar ────────────────────────────── -->
<div class="filter-bar">
  <span class="filter-label">
    <i class="fa-solid fa-filter" style="color:var(--cyan);margin-right:5px;"></i>Filter:
  </span>
  <button class="filter-btn active" onclick="filterCards('all', this)">
    <i class="fa-solid fa-border-all" style="margin-right:4px;"></i>All
  </button>
  <button class="filter-btn" onclick="filterCards('Live', this)">
    <i class="fa-solid fa-circle-dot" style="color:#6ee7b7;margin-right:4px;"></i>Live
  </button>
  <button class="filter-btn" onclick="filterCards('Completed', this)">
    <i class="fa-solid fa-circle-check" style="color:#00d4ff;margin-right:4px;"></i>Completed
  </button>
  <button class="filter-btn" onclick="filterCards('In Progress', this)">
    <i class="fa-solid fa-spinner" style="color:#fde68a;margin-right:4px;"></i>In Progress
  </button>
</div>

<!-- ── Grid ─────────────────────────────────── -->
<div class="grid" id="projectGrid"></div>

<!-- ── Modal ────────────────────────────────── -->
<div class="modal-backdrop" id="modalBackdrop">
  <div class="modal" id="modal" role="dialog" aria-modal="true" aria-labelledby="modalTitle">

    <div class="modal-img" id="modalImg"></div>

    <button class="modal-close" id="modalClose" aria-label="Close">
      <i class="fa-solid fa-xmark"></i>
    </button>

    <div class="modal-content">
      <div class="modal-header">
        <div class="modal-icon-box" id="modalIconBox">
          <i id="modalIcon"></i>
        </div>
        <div class="modal-title-block">
          <div class="modal-title" id="modalTitleText"></div>
          <div class="modal-badges" id="modalBadges"></div>
        </div>
      </div>

      <p class="modal-desc" id="modalDesc"></p>

      <div class="section-label">
        <i class="fa-solid fa-layer-group"></i> Tech Stack
      </div>
      <div class="tech-row" id="modalTech"></div>

      <div class="section-label">
        <i class="fa-solid fa-list-check"></i> Key Features
      </div>
      <div class="features-grid" id="modalFeatures"></div>

      <div class="modal-actions" id="modalActions"></div>
    </div>
  </div>
</div>

<!-- ── Footer ────────────────────────────────── -->
<div class="footer">
  <div style="display:flex;align-items:center;gap:0.4rem;color:#6b7280;font-size:0.8rem;">
    <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13"
         viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2"
         stroke-linecap="round" stroke-linejoin="round">
      <path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/>
      <circle cx="12" cy="10" r="3"/>
    </svg>
    © 2026 <strong style="color:#9ca3af;">Dave Campo</strong> · Built with Python &amp; Streamlit
  </div>
  <div style="display:flex;align-items:center;gap:0.4rem;color:#6b7280;font-size:0.78rem;">
    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12"
         viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2"
         stroke-linecap="round" stroke-linejoin="round">
      <polygon points="12 2 2 7 12 12 22 7 12 2"/>
      <polyline points="2 17 12 22 22 17"/>
      <polyline points="2 12 12 17 22 12"/>
    </svg>
    <span id="projectCount"></span>
  </div>
</div>

<script>
// ── Config ────────────────────────────────────────────────────
const STATUS = {
  "Live":        { bg:"rgba(16,185,129,0.15)",  border:"rgba(16,185,129,0.5)",  text:"#6ee7b7", icon:"fa-circle-dot" },
  "Completed":   { bg:"rgba(0,212,255,0.12)",   border:"rgba(0,212,255,0.4)",   text:"#00d4ff", icon:"fa-circle-check" },
  "In Progress": { bg:"rgba(251,191,36,0.12)",  border:"rgba(251,191,36,0.4)",  text:"#fde68a", icon:"fa-spinner" },
};

const DIFF = {
  "Beginner":     "#34d399",
  "Intermediate": "#00d4ff",
  "Advanced":     "#ff6bcb",
};

// ── Project Data ─────────────────────────────────────────────
// Set `image` to a screenshot URL or leave null for gradient placeholder
const PROJECTS = [
  {
    id: "portfolio",
    title: "Portfolio Website",
    icon: "fa-solid fa-globe",
    color: "#00d4ff",
    ga: "#00d4ff", gb: "#0ea5e9",
    description: "A personal portfolio built with Streamlit featuring smooth navigation, dark theme UI, animations, and interactive components showcasing my work and skills.",
    tech: ["Python", "Streamlit", "CSS", "HTML"],
    status: "Live",
    year: "2024",
    difficulty: "Intermediate",
    features: ["Responsive design", "Dark theme", "Smooth animations", "Custom navigation"],
    image: null,
    liveUrl: "#",
    sourceUrl: "#",
  },
  {
    id: "face",
    title: "Face Recognition System",
    icon: "fa-solid fa-face-viewfinder",
    color: "#ff6bcb",
    ga: "#ff6bcb", gb: "#e879f9",
    description: "AI-powered attendance system using facial recognition with real-time detection, logging, and an admin dashboard for managing records efficiently.",
    tech: ["Python", "OpenCV", "DeepFace", "SQLite"],
    status: "Completed",
    year: "2024",
    difficulty: "Advanced",
    features: ["Real-time detection", "Auto attendance log", "Admin dashboard", "98% accuracy"],
    image: null,
    liveUrl: null,
    sourceUrl: "#",
  },
  {
    id: "grocery",
    title: "Grocery Web App",
    icon: "fa-solid fa-cart-shopping",
    color: "#a78bfa",
    ga: "#a78bfa", gb: "#818cf8",
    description: "Full-stack e-commerce grocery platform with product listings, cart management, checkout flow, payment integration, and order tracking.",
    tech: ["React", "Node.js", "MongoDB", "Stripe"],
    status: "In Progress",
    year: "2024",
    difficulty: "Advanced",
    features: ["Cart & checkout", "Payment integration", "Order tracking", "Admin panel"],
    image: null,
    liveUrl: null,
    sourceUrl: "#",
  },
  {
    id: "dashboard",
    title: "Data Dashboard",
    icon: "fa-solid fa-chart-line",
    color: "#34d399",
    ga: "#34d399", gb: "#10b981",
    description: "Interactive analytics dashboard with live charts, CSV upload, dynamic filters, drill-down views, and exportable PDF/CSV reports.",
    tech: ["Python", "Plotly", "Pandas", "Streamlit"],
    status: "Completed",
    year: "2023",
    difficulty: "Intermediate",
    features: ["Live charts", "CSV upload", "Export reports", "Filters & drill-down"],
    image: null,
    liveUrl: "#",
    sourceUrl: "#",
  },
  {
    id: "weather",
    title: "Weather App",
    icon: "fa-solid fa-cloud-sun",
    color: "#fde68a",
    ga: "#fde68a", gb: "#f59e0b",
    description: "Real-time weather application with 7-day forecasts, location search, interactive maps, and beautiful weather condition animations.",
    tech: ["React", "OpenWeather API", "Leaflet", "Tailwind"],
    status: "Completed",
    year: "2023",
    difficulty: "Intermediate",
    features: ["7-day forecast", "Location search", "Interactive map", "Weather alerts"],
    image: null,
    liveUrl: "#",
    sourceUrl: "#",
  },
  {
    id: "chat",
    title: "AI Chat Assistant",
    icon: "fa-solid fa-robot",
    color: "#818cf8",
    ga: "#818cf8", gb: "#6366f1",
    description: "Conversational AI assistant powered by GPT with context memory, markdown rendering, code highlighting, and chat export functionality.",
    tech: ["Python", "OpenAI API", "FastAPI", "React"],
    status: "In Progress",
    year: "2024",
    difficulty: "Advanced",
    features: ["Context memory", "Code highlighting", "Chat export", "Multi-model support"],
    image: null,
    liveUrl: null,
    sourceUrl: "#",
  },
];

// ── Utility ───────────────────────────────────────────────────
function hexRgb(hex) {
  const r = parseInt(hex.slice(1,3),16);
  const g = parseInt(hex.slice(3,5),16);
  const b = parseInt(hex.slice(5,7),16);
  return `${r},${g},${b}`;
}

function placeholderStyle(p) {
  return `background:linear-gradient(135deg,rgba(${hexRgb(p.ga)},0.14) 0%,rgba(${hexRgb(p.gb)},0.07) 100%);`;
}

// ── Render Grid ───────────────────────────────────────────────
let currentFilter = 'all';

function renderGrid(filter) {
  currentFilter = filter;
  const grid = document.getElementById('projectGrid');
  grid.innerHTML = '';

  const list = filter === 'all'
    ? PROJECTS
    : PROJECTS.filter(p => p.status === filter);

  document.getElementById('projectCount').textContent =
    `${list.length} project${list.length !== 1 ? 's' : ''}`;

  if (list.length === 0) {
    grid.innerHTML = `
      <div class="empty-state">
        <i class="fa-solid fa-folder-open"></i>
        <p>No projects found for this filter.</p>
      </div>`;
    return;
  }

  list.forEach(p => {
    const ss = STATUS[p.status] || STATUS["Completed"];
    const card = document.createElement('div');
    card.className = 'card';
    card.setAttribute('role', 'button');
    card.setAttribute('tabindex', '0');
    card.setAttribute('aria-label', `View ${p.title} project details`);

    const imgHTML = p.image
      ? `<img src="${p.image}" alt="${p.title}" loading="lazy"
            onerror="this.parentElement.innerHTML='<div class=\\'card-placeholder\\'
            style=\\'${placeholderStyle(p)}\\'><i class=\\"${p.icon}\\" style=\\"color:${p.color};\\"></i></div>'">`
      : `<div class="card-placeholder" style="${placeholderStyle(p)}">
           <i class="${p.icon}" style="color:${p.color};"></i>
         </div>`;

    const visibleTags = p.tech.slice(0, 3);
    const extraTags   = p.tech.length > 3 ? p.tech.length - 3 : 0;

    card.innerHTML = `
      <div class="card-img">
        ${imgHTML}
        <div class="card-status-badge"
          style="background:${ss.bg};border:1px solid ${ss.border};color:${ss.text};">
          <i class="fa-solid ${ss.icon}" style="font-size:0.6rem;"></i>${p.status}
        </div>
        <div class="card-year-badge">
          <i class="fa-solid fa-calendar" style="font-size:0.58rem;"></i>${p.year}
        </div>
        <div class="card-hover-cta">
          <span><i class="fa-solid fa-expand"></i> View Details</span>
        </div>
      </div>
      <div class="card-body">
        <div class="card-title">
          <i class="${p.icon}" style="color:${p.color};"></i>
          ${p.title}
        </div>
        <p class="card-desc">${p.description}</p>
        <div class="card-tags">
          ${visibleTags.map(t => `<span class="tag">${t}</span>`).join('')}
          ${extraTags ? `<span class="tag">+${extraTags} more</span>` : ''}
        </div>
      </div>`;

    card.addEventListener('click', () => openModal(p));
    card.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openModal(p); } });
    grid.appendChild(card);
  });
}

// ── Filter ────────────────────────────────────────────────────
function filterCards(status, btn) {
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  renderGrid(status);
}

// ── Modal open ────────────────────────────────────────────────
function openModal(p) {
  const ss = STATUS[p.status] || STATUS["Completed"];
  const dc = DIFF[p.difficulty] || "#9ca3af";

  // Image
  const imgWrap = document.getElementById('modalImg');
  imgWrap.innerHTML = p.image
    ? `<img src="${p.image}" alt="${p.title}">`
    : `<div class="modal-img-placeholder" style="${placeholderStyle(p)}">
         <i class="${p.icon}" style="color:${p.color};"></i>
       </div>`;

  // Icon
  const mi = document.getElementById('modalIcon');
  mi.className = p.icon;
  mi.style.color = p.color;
  mi.style.fontSize = 'clamp(1.2rem, 3vw, 1.5rem)';

  // Title
  document.getElementById('modalTitleText').textContent = p.title;

  // Badges
  document.getElementById('modalBadges').innerHTML = `
    <span class="badge" style="background:${ss.bg};border:1px solid ${ss.border};color:${ss.text};">
      <i class="fa-solid ${ss.icon}"></i>${p.status}
    </span>
    <span class="badge" style="background:rgba(148,163,184,0.07);border:1px solid rgba(148,163,184,0.18);color:${dc};">
      <i class="fa-solid fa-signal"></i>${p.difficulty}
    </span>
    <span class="badge" style="background:rgba(148,163,184,0.05);border:1px solid rgba(148,163,184,0.14);color:#9ca3af;">
      <i class="fa-solid fa-calendar"></i>${p.year}
    </span>`;

  // Description
  document.getElementById('modalDesc').textContent = p.description;

  // Tech
  document.getElementById('modalTech').innerHTML =
    p.tech.map(t => `<span class="tech-tag">${t}</span>`).join('');

  // Features
  document.getElementById('modalFeatures').innerHTML =
    p.features.map(f => `
      <div class="feature-item">
        <i class="fa-solid fa-circle-check"></i>
        <span>${f}</span>
      </div>`).join('');

  // Actions
  let acts = '';
  if (p.liveUrl) {
    acts += `<a class="action-btn btn-live" href="${p.liveUrl}" target="_blank" rel="noopener noreferrer">
      <i class="fa-solid fa-arrow-up-right-from-square"></i> Live Demo
    </a>`;
  }
  if (p.sourceUrl) {
    acts += `<a class="action-btn btn-source" href="${p.sourceUrl}" target="_blank" rel="noopener noreferrer">
      <i class="fa-brands fa-github"></i> Source Code
    </a>`;
  }
  if (!p.liveUrl && !p.sourceUrl) {
    acts = `<div style="color:#9ca3af;font-size:0.85rem;display:flex;align-items:center;gap:6px;padding:8px 0;">
      <i class="fa-solid fa-lock" style="color:#6b7280;"></i> Links coming soon
    </div>`;
  }
  document.getElementById('modalActions').innerHTML = acts;

  // Open
  const bd = document.getElementById('modalBackdrop');
  bd.classList.add('open');
  document.body.style.overflow = 'hidden';

  // Focus trap — focus close btn
  requestAnimationFrame(() => document.getElementById('modalClose').focus());
}

// ── Modal close ───────────────────────────────────────────────
function closeModal() {
  document.getElementById('modalBackdrop').classList.remove('open');
  document.body.style.overflow = '';
}

document.getElementById('modalClose').addEventListener('click', closeModal);

document.getElementById('modalBackdrop').addEventListener('click', function(e) {
  if (e.target === this) closeModal();
});

document.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeModal();
});

// Prevent modal scroll from propagating to body
document.getElementById('modal').addEventListener('touchmove', e => e.stopPropagation(), { passive: true });

// ── Init ──────────────────────────────────────────────────────
renderGrid('all');
</script>
</body>
</html>
""", height=1050, scrolling=True)