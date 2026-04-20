import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import streamlit.components.v1 as components
from components import apply_global_effects
import base64
from pathlib import Path

st.set_page_config(
    page_title="Certifications | Dave Campo",
    page_icon="📜",
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
div[data-testid="stDownloadButton"] button {
    background: linear-gradient(135deg, #00d4ff, #ff6bcb) !important;
    color: #000 !important; font-weight: 700 !important;
    border: none !important; border-radius: 999px !important;
    padding: 0.6rem 2rem !important;
    transition: all 0.22s ease !important;
}
div[data-testid="stDownloadButton"] button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 20px 45px rgba(0,212,255,0.4) !important;
}
div[data-testid="stDownloadButton"] button p { color: #000 !important; }
hr { border-color: rgba(148,163,184,0.2) !important; margin: 1.5rem 0 !important; }
@media (max-width: 768px) {
    .block-container {
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
    }
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
#   CERTIFICATE DATA
# ─────────────────────────────────────────────────────────
CERT_DIR = Path("assets/cert")

CERTIFICATES = [
    {
        "file":   "cert1.png",
        "name":   "ChatGpt For Python",
        "issuer": "Simple learn",
        "date":   "2023",
        "skills": ["Python","GPT"],
        "color":  "#93c5fd",
        "border": "rgba(59,130,246,0.5)",
        "glow":   "rgba(59,130,246,0.25)",
        "tag_bg": "rgba(59,130,246,0.12)",
    },
    {
        "file":   "cert2.png",
        "name":   "Python Django 101",
        "issuer": "Simple learn",
        "date":   "2024",
        "skills": ["Python", "Templates"],
        "color":  "#7dd3fc",
        "border": "rgba(56,189,248,0.5)",
        "glow":   "rgba(56,189,248,0.25)",
        "tag_bg": "rgba(56,189,248,0.12)",
    },
    {
        "file":   "cert3.png",
        "name":   "Web Scraping",
        "issuer": "Simple learn",
        "date":   "2024",
        "skills": ["Python"],
        "color":  "#86efac",
        "border": "rgba(22,163,74,0.5)",
        "glow":   "rgba(22,163,74,0.25)",
        "tag_bg": "rgba(22,163,74,0.12)",
    },
    {
        "file":   "cert4.png",
        "name":   "Android App Development",
        "issuer": "Simple learn",
        "date":   "2024",
        "skills": ["Kotlin", "Android Studio"],
        "color":  "#ff6bcb",
        "border": "rgba(255,107,203,0.5)",
        "glow":   "rgba(255,107,203,0.25)",
        "tag_bg": "rgba(255,107,203,0.12)",
    },
    {
        "file":   "cert5.png",
        "name":   "React Js Components",
        "issuer": "Simple learn",
        "date":   "2023",
        "skills": ["React", "Components"],
        "color":  "#fde68a",
        "border": "rgba(234,179,8,0.5)",
        "glow":   "rgba(234,179,8,0.25)",
        "tag_bg": "rgba(234,179,8,0.12)",
    },
]

def load_image_b64(filepath: Path) -> str | None:
    if filepath.exists():
        with open(filepath, "rb") as f:
            ext  = filepath.suffix.lstrip(".").lower()
            mime = "jpeg" if ext in ("jpg","jpeg") else ext
            return f"data:image/{mime};base64," + base64.b64encode(f.read()).decode()
    return None

for cert in CERTIFICATES:
    cert["b64"] = load_image_b64(CERT_DIR / cert["file"])

# Resume
resume_path = Path("assets/resume.pdf")
if resume_path.exists():
    with open(resume_path,"rb") as f:
        resume_data     = f.read()
    resume_filename = "DaveCampo_Resume.pdf"
else:
    resume_data     = b"Dave Campo Resume - PDF coming soon!"
    resume_filename = "DaveCampo_Resume.txt"

total = len(CERTIFICATES)

# ─────────────────────────────────────────────────────────
#   BUILD CARD + MODAL HTML
# ─────────────────────────────────────────────────────────
def build_img(cert, w="100%", h="200px", radius="12px 12px 0 0"):
    if cert["b64"]:
        return (
            f'<img src="{cert["b64"]}" '
            f'style="width:{w};height:{h};object-fit:cover;'
            f'border-radius:{radius};display:block;" />'
        )
    file_hint = cert["file"]
    return f"""
    <div style="width:{w};height:{h};border-radius:{radius};
         background:linear-gradient(135deg,
           rgba(0,212,255,0.06),rgba(255,107,203,0.06));
         display:flex;flex-direction:column;
         align-items:center;justify-content:center;gap:0.6rem;
         border-bottom:1px dashed rgba(148,163,184,0.2);">
      <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40"
           viewBox="0 0 24 24" fill="none" stroke="rgba(148,163,184,0.4)"
           stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12
                 a2 2 0 0 0 2-2V7.5L14.5 2z"/>
        <polyline points="14 2 14 8 20 8"/>
        <path d="M9 13h6"/><path d="M9 17h3"/>
      </svg>
      <span style="color:rgba(148,163,184,0.45);font-size:0.72rem;text-align:center;
                   padding:0 1rem;">
        {file_hint}
      </span>
    </div>"""

cards_html = ""
modals_html = ""

for i, c in enumerate(CERTIFICATES):
    # skill chips for card (show first 2 + count)
    shown   = c["skills"][:2]
    extra   = len(c["skills"]) - 2
    chips_c = "".join([
        f'<span style="background:{c["tag_bg"]};border:1px solid {c["border"]};'
        f'border-radius:999px;padding:0.18rem 0.65rem;font-size:0.7rem;'
        f'color:{c["color"]};font-weight:600;">{s}</span>'
        for s in shown
    ])
    if extra > 0:
        chips_c += (
            f'<span style="background:rgba(148,163,184,0.08);'
            f'border:1px solid rgba(148,163,184,0.2);'
            f'border-radius:999px;padding:0.18rem 0.65rem;font-size:0.7rem;'
            f'color:#9ca3af;font-weight:600;">+{extra} more</span>'
        )

    # all skill chips for modal
    chips_m = "".join([
        f'<span style="background:{c["tag_bg"]};border:1px solid {c["border"]};'
        f'border-radius:999px;padding:0.22rem 0.8rem;font-size:0.78rem;'
        f'color:{c["color"]};font-weight:600;">{s}</span>'
        for s in c["skills"]
    ])

    img_card  = build_img(c, w="100%", h="195px", radius="14px 14px 0 0")
    img_modal = build_img(c, w="100%", h="280px", radius="14px 14px 0 0")

    # ── CARD ──
    cards_html += f"""
    <div class="cert-card" id="card-{i}"
         style="border-color:{c['border']};"
         onclick="openModal({i})">

      <!-- image wrapper with overlay -->
      <div class="card-img-wrap">
        {img_card}
        <div class="card-overlay">
          <div class="view-btn">
            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14"
                 viewBox="0 0 24 24" fill="none" stroke="currentColor"
                 stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M15 3h6v6"/><path d="M10 14 21 3"/>
              <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8
                       a2 2 0 0 1 2-2h6"/>
            </svg>
            View Details
          </div>
        </div>
        <!-- verified badge top-right -->
        <div class="verified-badge">
          <svg xmlns="http://www.w3.org/2000/svg" width="10" height="10"
               viewBox="0 0 24 24" fill="none" stroke="currentColor"
               stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="20 6 9 17 4 12"/>
          </svg>
          Verified
        </div>
      </div>

      <!-- card body -->
      <div class="card-body">
        <div class="card-date">
          <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12"
               viewBox="0 0 24 24" fill="none" stroke="currentColor"
               stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect width="18" height="18" x="3" y="4" rx="2" ry="2"/>
            <line x1="16" x2="16" y1="2" y2="6"/>
            <line x1="8"  x2="8"  y1="2" y2="6"/>
            <line x1="3"  x2="21" y1="10" y2="10"/>
          </svg>
          {c['date']}
        </div>

        <div class="card-title" style="color:{c['color']}">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
               viewBox="0 0 24 24" fill="none" stroke="currentColor"
               stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
               style="flex-shrink:0">
            <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12
                     a2 2 0 0 0 2-2V7.5L14.5 2z"/>
            <polyline points="14 2 14 8 20 8"/>
          </svg>
          {c['name']}
        </div>

        <div class="card-issuer">
          <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12"
               viewBox="0 0 24 24" fill="none" stroke="#9ca3af"
               stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
            <polyline points="9 22 9 12 15 12 15 22"/>
          </svg>
          {c['issuer']}
        </div>

        <div class="card-chips">{chips_c}</div>
      </div>
    </div>
    """

    # ── MODAL ──
    modals_html += f"""
    <div class="modal-backdrop" id="modal-{i}" onclick="closeOnBackdrop(event,{i})">
      <div class="modal-box" style="border-color:{c['border']};
           box-shadow:0 0 60px {c['glow']},0 40px 80px rgba(0,0,0,0.9);">

        <!-- close btn -->
        <button class="modal-close" onclick="closeModal({i})">
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18"
               viewBox="0 0 24 24" fill="none" stroke="currentColor"
               stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M18 6 6 18"/><path d="m6 6 12 12"/>
          </svg>
        </button>

        {img_modal}

        <div class="modal-body">
          <!-- verified -->
          <div class="modal-verified">
            <svg xmlns="http://www.w3.org/2000/svg" width="11" height="11"
                 viewBox="0 0 24 24" fill="none" stroke="currentColor"
                 stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="20 6 9 17 4 12"/>
            </svg>
            Verified Certificate
          </div>

          <div class="modal-title" style="color:{c['color']}">
            {c['name']}
          </div>

          <div class="modal-meta">
            <span class="meta-item">
              <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14"
                   viewBox="0 0 24 24" fill="none" stroke="#9ca3af"
                   stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
                <polyline points="9 22 9 12 15 12 15 22"/>
              </svg>
              {c['issuer']}
            </span>
            <span class="meta-item">
              <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14"
                   viewBox="0 0 24 24" fill="none" stroke="#9ca3af"
                   stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect width="18" height="18" x="3" y="4" rx="2" ry="2"/>
                <line x1="16" x2="16" y1="2" y2="6"/>
                <line x1="8"  x2="8"  y1="2" y2="6"/>
                <line x1="3"  x2="21" y1="10" y2="10"/>
              </svg>
              {c['date']}
            </span>
          </div>

          <div class="modal-skills-label">
            <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13"
                 viewBox="0 0 24 24" fill="none" stroke="#6b7280"
                 stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275
                       L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275
                       L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275
                       L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/>
            </svg>
            Skills Covered
          </div>
          <div class="modal-chips">{chips_m}</div>
        </div>
      </div>
    </div>
    """

# ═══════════════════════════════════════════════════════
#   FULL PAGE HTML
# ═══════════════════════════════════════════════════════
components.html(f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<style>
  *, *::before, *::after {{ box-sizing:border-box; margin:0; padding:0; }}
  body {{
    font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
    background:transparent;
    color:#e5e7eb;
    -webkit-font-smoothing:antialiased;
  }}

  /* ── Keyframes ── */
  @keyframes fadeUp {{
    from {{ opacity:0; transform:translateY(26px); }}
    to   {{ opacity:1; transform:translateY(0); }}
  }}
  @keyframes fadeIn {{
    from {{ opacity:0; }} to {{ opacity:1; }}
  }}
  @keyframes pulse {{
    0%,100% {{ opacity:1; transform:scale(1); }}
    50%      {{ opacity:0.5; transform:scale(1.4); }}
  }}
  @keyframes glowPulse {{
    0%,100% {{ box-shadow:0 0 22px rgba(0,212,255,0.1); }}
    50%      {{ box-shadow:0 0 42px rgba(0,212,255,0.28); }}
  }}
  @keyframes modalIn {{
    from {{ opacity:0; transform:scale(0.92) translateY(20px); }}
    to   {{ opacity:1; transform:scale(1)    translateY(0); }}
  }}
  @keyframes overlayIn {{
    from {{ opacity:0; }}
    to   {{ opacity:1; }}
  }}
  @keyframes cardPop {{
    from {{ opacity:0; transform:translateY(30px) scale(0.96); }}
    to   {{ opacity:1; transform:translateY(0)    scale(1); }}
  }}
  @keyframes statCount {{
    from {{ opacity:0; transform:translateY(10px); }}
    to   {{ opacity:1; transform:translateY(0); }}
  }}

  /* ── Hero ── */
  .hero {{
    background:rgba(15,23,42,0.97);
    border-radius:20px;
    border:1px solid rgba(148,163,184,0.28);
    padding:2.2rem 2.4rem 2rem;
    margin-bottom:1.2rem;
    animation:fadeUp 0.6s ease both, glowPulse 4s ease-in-out infinite;
    position:relative; overflow:hidden;
  }}
  .hero::before {{
    content:'';position:absolute;inset:0;
    background:linear-gradient(135deg,
      rgba(0,212,255,0.04) 0%, transparent 50%,
      rgba(255,107,203,0.04) 100%);
    pointer-events:none;
  }}
  .hero-eyebrow {{
    font-size:0.74rem;text-transform:uppercase;
    letter-spacing:0.22em;color:#00d4ff;
    margin-bottom:0.7rem;
    display:flex;align-items:center;gap:0.5rem;
    animation:fadeIn 0.5s 0.15s ease both;
  }}
  .eyebrow-dot {{
    width:6px;height:6px;border-radius:50%;
    background:#00d4ff;animation:pulse 2s ease-in-out infinite;
  }}
  .hero-title {{
    font-size:clamp(1.9rem,5vw,2.7rem);
    font-weight:800;color:#e5e7eb;
    line-height:1.15;margin-bottom:0.7rem;
    display:flex;align-items:center;gap:0.6rem;
    animation:fadeUp 0.5s 0.1s ease both;
  }}
  .hero-desc {{
    font-size:clamp(0.87rem,2vw,1rem);
    color:#9ca3af;line-height:1.7;
    max-width:580px;
    animation:fadeUp 0.5s 0.2s ease both;
  }}

  /* ── Stats ── */
  .stats-grid {{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:0.75rem;
    margin-bottom:1.4rem;
  }}
  .stat-card {{
    background:rgba(15,23,42,0.96);
    border-radius:14px;
    padding:1.1rem 0.8rem;
    text-align:center;
    animation:statCount 0.5s ease both;
    transition:transform 0.22s ease, box-shadow 0.22s ease;
  }}
  .stat-card:hover {{
    transform:translateY(-4px);
    box-shadow:0 14px 35px rgba(0,0,0,0.6);
  }}
  .stat-num {{
    font-size:2rem;font-weight:900;line-height:1.1;
    background:linear-gradient(135deg,#00d4ff,#ff6bcb);
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;
    background-clip:text;
  }}
  .stat-lbl {{
    color:#9ca3af;font-size:0.72rem;
    text-transform:uppercase;letter-spacing:0.12em;
    margin-top:0.25rem;
  }}

  /* ── Section heading ── */
  .section-head {{
    margin-bottom:1.1rem;
    animation:fadeUp 0.5s 0.05s ease both;
  }}
  .section-eyebrow {{
    font-size:0.7rem;text-transform:uppercase;
    letter-spacing:0.2em;color:#00d4ff;margin-bottom:0.3rem;
  }}
  .section-title {{
    font-size:clamp(1.3rem,3vw,1.7rem);
    font-weight:800;color:#e5e7eb;
    display:flex;align-items:center;gap:0.5rem;
  }}
  .divider {{
    height:1px;background:rgba(148,163,184,0.15);
    margin:1.4rem 0;
  }}

  /* ── Gallery Grid ── */
  .gallery {{
    display:grid;
    grid-template-columns:repeat(auto-fill,minmax(280px,1fr));
    gap:1.1rem;
    margin-bottom:0.5rem;
  }}

  /* ── Certificate Card ── */
  .cert-card {{
    background:rgba(15,23,42,0.97);
    border:1px solid;
    border-radius:16px;
    overflow:hidden;
    cursor:pointer;
    animation:cardPop 0.5s ease both;
    transition:transform 0.26s ease, box-shadow 0.26s ease;
    position:relative;
  }}
  .cert-card:nth-child(1) {{ animation-delay:0.05s; }}
  .cert-card:nth-child(2) {{ animation-delay:0.12s; }}
  .cert-card:nth-child(3) {{ animation-delay:0.19s; }}
  .cert-card:nth-child(4) {{ animation-delay:0.26s; }}
  .cert-card:nth-child(5) {{ animation-delay:0.33s; }}
  .cert-card:hover {{
    transform:translateY(-6px) scale(1.01);
    box-shadow:0 24px 55px rgba(0,0,0,0.7);
  }}

  /* image wrapper + overlay */
  .card-img-wrap {{
    position:relative;overflow:hidden;
  }}
  .card-overlay {{
    position:absolute;inset:0;
    background:rgba(2,6,23,0.55);
    display:flex;align-items:center;justify-content:center;
    opacity:0;
    transition:opacity 0.25s ease;
    backdrop-filter:blur(2px);
  }}
  .cert-card:hover .card-overlay {{ opacity:1; }}
  .view-btn {{
    display:flex;align-items:center;gap:0.45rem;
    background:rgba(0,212,255,0.15);
    border:1.5px solid rgba(0,212,255,0.6);
    border-radius:999px;
    padding:0.45rem 1.1rem;
    font-size:0.82rem;font-weight:700;color:#00d4ff;
    backdrop-filter:blur(8px);
    transition:background 0.2s ease, transform 0.2s ease;
  }}
  .cert-card:hover .view-btn {{
    background:rgba(0,212,255,0.25);
    transform:scale(1.05);
  }}
  .verified-badge {{
    position:absolute;top:0.7rem;right:0.7rem;
    display:flex;align-items:center;gap:0.3rem;
    background:rgba(16,185,129,0.18);
    border:1px solid rgba(16,185,129,0.45);
    border-radius:999px;
    padding:0.2rem 0.65rem;
    font-size:0.68rem;font-weight:700;color:#34d399;
  }}

  /* card body */
  .card-body {{
    padding:1rem 1.1rem 1.1rem;
  }}
  .card-date {{
    display:flex;align-items:center;gap:0.35rem;
    color:#6b7280;font-size:0.75rem;margin-bottom:0.55rem;
  }}
  .card-title {{
    font-size:0.97rem;font-weight:800;
    line-height:1.3;margin-bottom:0.35rem;
    display:flex;align-items:flex-start;gap:0.4rem;
  }}
  .card-issuer {{
    display:flex;align-items:center;gap:0.35rem;
    color:#9ca3af;font-size:0.78rem;
    margin-bottom:0.75rem;line-height:1.4;
  }}
  .card-chips {{
    display:flex;flex-wrap:wrap;gap:0.35rem;
  }}

  /* ── Modal ── */
  .modal-backdrop {{
    display:none;
    position:fixed;inset:0;z-index:9999;
    background:rgba(2,6,23,0.82);
    backdrop-filter:blur(6px);
    align-items:center;justify-content:center;
    padding:1rem;
    animation:overlayIn 0.25s ease both;
  }}
  .modal-backdrop.open {{
    display:flex;
  }}
  .modal-box {{
    background:rgba(15,23,42,0.99);
    border:1px solid;
    border-radius:18px;
    width:100%;max-width:520px;
    max-height:90vh;overflow-y:auto;
    position:relative;
    animation:modalIn 0.3s cubic-bezier(0.34,1.56,0.64,1) both;
    scrollbar-width:none;
  }}
  .modal-box::-webkit-scrollbar {{ display:none; }}
  .modal-close {{
    position:absolute;top:0.9rem;right:0.9rem;z-index:10;
    background:rgba(15,23,42,0.9);
    border:1px solid rgba(148,163,184,0.25);
    border-radius:50%;width:34px;height:34px;
    display:flex;align-items:center;justify-content:center;
    cursor:pointer;color:#9ca3af;
    transition:all 0.2s ease;
  }}
  .modal-close:hover {{
    background:rgba(239,68,68,0.15);
    border-color:rgba(239,68,68,0.4);color:#fca5a5;
    transform:rotate(90deg);
  }}
  .modal-body {{
    padding:1.3rem 1.5rem 1.5rem;
  }}
  .modal-verified {{
    display:inline-flex;align-items:center;gap:0.35rem;
    background:rgba(16,185,129,0.12);
    border:1px solid rgba(16,185,129,0.35);
    border-radius:999px;padding:0.22rem 0.8rem;
    font-size:0.72rem;font-weight:700;color:#34d399;
    margin-bottom:0.75rem;
  }}
  .modal-title {{
    font-size:1.25rem;font-weight:800;
    line-height:1.3;margin-bottom:0.7rem;
  }}
  .modal-meta {{
    display:flex;flex-wrap:wrap;gap:0.8rem;
    margin-bottom:1rem;
    padding-bottom:1rem;
    border-bottom:1px solid rgba(148,163,184,0.1);
  }}
  .meta-item {{
    display:flex;align-items:center;gap:0.4rem;
    color:#9ca3af;font-size:0.84rem;
  }}
  .modal-skills-label {{
    display:flex;align-items:center;gap:0.4rem;
    font-size:0.7rem;text-transform:uppercase;
    letter-spacing:0.14em;color:#6b7280;
    margin-bottom:0.6rem;
  }}
  .modal-chips {{
    display:flex;flex-wrap:wrap;gap:0.45rem;
  }}

  /* ── Download / Resume section ── */
  .resume-card {{
    background:rgba(15,23,42,0.96);
    border:1px solid rgba(52,211,153,0.25);
    border-radius:16px;
    padding:1.4rem 1.6rem;
    display:flex;align-items:center;gap:1rem;flex-wrap:wrap;
    animation:fadeUp 0.5s 0.3s ease both;
    transition:transform 0.22s ease, box-shadow 0.22s ease;
  }}
  .resume-card:hover {{
    transform:translateY(-3px);
    box-shadow:0 14px 38px rgba(52,211,153,0.12);
  }}
  .resume-icon {{
    width:48px;height:48px;border-radius:12px;flex-shrink:0;
    background:rgba(52,211,153,0.1);
    border:1px solid rgba(52,211,153,0.25);
    display:flex;align-items:center;justify-content:center;
  }}
  .resume-info {{ flex:1;min-width:160px; }}
  .resume-title {{
    font-size:1rem;font-weight:700;color:#e5e7eb;margin-bottom:0.2rem;
  }}
  .resume-sub {{ font-size:0.8rem;color:#9ca3af; }}

  /* ── Footer ── */
  .footer {{
    display:flex;justify-content:space-between;align-items:center;
    flex-wrap:wrap;gap:0.5rem;
    padding:1rem 0 0;
    border-top:1px solid rgba(148,163,184,0.12);
    animation:fadeIn 0.6s 0.4s ease both;
  }}
  .footer-left {{
    color:#6b7280;font-size:0.8rem;
    display:flex;align-items:center;gap:0.4rem;
  }}
  .footer-left strong {{ color:#9ca3af; }}

  /* ── Responsive ── */
  @media (max-width:640px) {{
    .hero {{ padding:1.4rem 1.2rem 1.4rem; }}
    .gallery {{ grid-template-columns:1fr; gap:0.85rem; }}
    .stats-grid {{ grid-template-columns:repeat(3,1fr); gap:0.5rem; }}
    .stat-num {{ font-size:1.6rem; }}
    .modal-box {{ max-width:100%; border-radius:14px; }}
    .modal-body {{ padding:1rem 1.1rem 1.2rem; }}
    .resume-card {{ flex-direction:column; text-align:center; }}
  }}
  @media (max-width:400px) {{
    .stats-grid {{ grid-template-columns:1fr; }}
  }}
</style>
</head>
<body>

<!-- ═══ HERO ══════════════════════════════════════════════ -->
<div class="hero">
  <div class="hero-eyebrow">
    <div class="eyebrow-dot"></div>
    Verified skills &amp; learning
  </div>
  <h1 class="hero-title">
    <svg xmlns="http://www.w3.org/2000/svg" width="34" height="34"
         viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2"
         stroke-linecap="round" stroke-linejoin="round">
      <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12
               a2 2 0 0 0 2-2V7.5L14.5 2z"/>
      <polyline points="14 2 14 8 20 8"/>
      <path d="M9 13h6"/><path d="M9 17h3"/>
    </svg>
    Certifications
  </h1>
  <p class="hero-desc">
    A snapshot of the formal learning and training I've completed on my journey
    as a Full Stack Developer. Each certificate represents real hours of study,
    projects, and dedication — not just a badge.
  </p>
</div>

<!-- ═══ STATS ═════════════════════════════════════════════ -->
<div class="stats-grid">
  <div class="stat-card" style="border:1px solid rgba(0,212,255,0.22);
       animation-delay:0.08s;">
    <div class="stat-num">{total}</div>
    <div class="stat-lbl">Certificates</div>
  </div>
  <div class="stat-card" style="border:1px solid rgba(255,107,203,0.22);
       animation-delay:0.16s;">
    <div class="stat-num" style="-webkit-text-fill-color:#ff6bcb;color:#ff6bcb;">
      20+
    </div>
    <div class="stat-lbl">Skills Learned</div>
  </div>
  <div class="stat-card" style="border:1px solid rgba(52,211,153,0.22);
       animation-delay:0.24s;">
    <div class="stat-num" style="-webkit-text-fill-color:#34d399;color:#34d399;">
      2+
    </div>
    <div class="stat-lbl">Years Learning</div>
  </div>  
</div>

<div class="divider"></div>

<!-- ═══ GALLERY HEADING ═══════════════════════════════════ -->
<div class="section-head">
  <div class="section-eyebrow">Gallery</div>
  <div class="section-title">
    <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22"
         viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2"
         stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"/>
      <circle cx="9" cy="9" r="2"/>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/>
    </svg>
    Certificate Gallery
  </div>
</div>

<!-- ═══ GALLERY GRID ══════════════════════════════════════ -->
<div class="gallery">
  {cards_html}
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
      <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12
               a2 2 0 0 0 2-2V7.5L14.5 2z"/>
      <polyline points="14 2 14 8 20 8"/>
    </svg>
    Certifications
  </div>
</div>

<!-- ═══ MODALS ════════════════════════════════════════════ -->
{modals_html}

<script>
  function openModal(i) {{
    var m = document.getElementById('modal-' + i);
    if (m) {{
      m.classList.add('open');
      document.body.style.overflow = 'hidden';
    }}
  }}
  function closeModal(i) {{
    var m = document.getElementById('modal-' + i);
    if (m) {{
      m.classList.remove('open');
      document.body.style.overflow = '';
    }}
  }}
  function closeOnBackdrop(e, i) {{
    if (e.target === e.currentTarget) closeModal(i);
  }}
  document.addEventListener('keydown', function(e) {{
    if (e.key === 'Escape') {{
      document.querySelectorAll('.modal-backdrop.open').forEach(function(m) {{
        m.classList.remove('open');
        document.body.style.overflow = '';
      }});
    }}
  }});
</script>
</body>
</html>
""", height=2200, scrolling=True)
