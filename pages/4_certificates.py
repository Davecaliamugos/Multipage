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

/* ── Buttons ── */
div[data-testid="stButton"] button {
    background: linear-gradient(135deg, #00d4ff, #ff6bcb) !important;
    color: #000 !important; font-weight: 700 !important;
    border: none !important; border-radius: 10px !important;
    padding: 0.55rem 1.8rem !important; font-size: 0.95rem !important;
    transition: all 0.2s;
}
div[data-testid="stButton"] button p { color: #000 !important; }
div[data-testid="stButton"] button:hover { opacity: 0.85 !important; }

/* ── Download button ── */
div[data-testid="stDownloadButton"] button {
    background: linear-gradient(135deg, #00d4ff, #ff6bcb) !important;
    color: #000 !important; font-weight: 700 !important;
    border: none !important; border-radius: 999px !important;
    padding: 0.55rem 1.8rem !important;
    transition: all 0.22s;
}
div[data-testid="stDownloadButton"] button p { color: #000 !important; }
div[data-testid="stDownloadButton"] button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 20px 45px rgba(0,212,255,0.4) !important;
}

/* ── Alerts ── */
div[data-testid="stAlert"] {
    border-radius: 10px !important;
    background: rgba(15,23,42,0.8) !important;
}
div[data-testid="stAlert"] p { color: #e5e7eb !important; }

/* ── Radio ── */
div[data-testid="stRadio"] label p { color: #e5e7eb !important; }
div[data-testid="stRadio"] > div > label {
    background: rgba(15,23,42,0.6) !important;
    border: 1px solid rgba(148,163,184,0.25) !important;
    border-radius: 8px !important; padding: 0.4rem 1rem !important;
}

/* ── Text input ── */
div[data-testid="stTextInput"] input {
    background: #0f172a !important;
    border: 1px solid rgba(148,163,184,0.35) !important;
    border-radius: 10px !important; color: #e5e7eb !important;
}
div[data-testid="stTextInput"] input::placeholder { color: rgba(148,163,184,0.5) !important; }

/* ── Text area ── */
div[data-testid="stTextArea"] textarea {
    background: #0f172a !important;
    border: 1px solid rgba(148,163,184,0.35) !important;
    border-radius: 10px !important; color: #e5e7eb !important;
}

hr { border-color: rgba(148,163,184,0.2) !important; margin: 1.5rem 0 !important; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
#   LOAD LOCAL CERT IMAGES  (put your files in
#   assets/certificates/  named cert1.jpg, cert2.jpg …)
#   Falls back to a dark placeholder if file not found.
# ─────────────────────────────────────────────────────────
CERT_DIR = Path("assets/certificates")

# Certificate data — edit name/issuer/date/skills to match yours
CERTIFICATES = [
    {
        "file":   "cert1.jpg",          # filename inside assets/certificates/
        "name":   "Python Programming Certificate",
        "issuer": "Coursera / University of Michigan",
        "date":   "2023",
        "skills": ["Python","OOP","Data Structures","Algorithms"],
        "color":  "#93c5fd",
        "border": "rgba(59,130,246,0.35)",
    },
    {
        "file":   "cert2.jpg",
        "name":   "Web Development Bootcamp",
        "issuer": "Udemy",
        "date":   "2024",
        "skills": ["HTML","CSS","JavaScript","React"],
        "color":  "#7dd3fc",
        "border": "rgba(56,189,248,0.35)",
    },
    {
        "file":   "cert3.jpg",
        "name":   "Django Full Stack Developer",
        "issuer": "freeCodeCamp",
        "date":   "2024",
        "skills": ["Django","DRF","MySQL","REST APIs"],
        "color":  "#86efac",
        "border": "rgba(22,163,74,0.35)",
    },
    {
        "file":   "cert4.jpg",
        "name":   "UI/UX Design Fundamentals",
        "issuer": "Google / Coursera",
        "date":   "2024",
        "skills": ["Figma","Canva","Spline","Design Thinking"],
        "color":  "#ff6bcb",
        "border": "rgba(255,107,203,0.35)",
    },
    {
        "file":   "cert5.jpg",
        "name":   "Database Design & MySQL",
        "issuer": "LinkedIn Learning",
        "date":   "2023",
        "skills": ["MySQL","MS Access","SQLite","ERD"],
        "color":  "#fde68a",
        "border": "rgba(234,179,8,0.35)",
    },
]

def load_image_b64(filepath: Path) -> str | None:
    """Return base64-encoded image string or None if file missing."""
    if filepath.exists():
        with open(filepath, "rb") as f:
            ext = filepath.suffix.lstrip(".").lower()
            mime = "jpeg" if ext in ("jpg","jpeg") else ext
            return f"data:image/{mime};base64," + base64.b64encode(f.read()).decode()
    return None

# Preload all images
for cert in CERTIFICATES:
    cert["b64"] = load_image_b64(CERT_DIR / cert["file"])

# Session state
if "cert_idx"      not in st.session_state: st.session_state.cert_idx      = 0
if "liked_certs"   not in st.session_state: st.session_state.liked_certs   = set()
if "cert_comments" not in st.session_state: st.session_state.cert_comments = {}   # {idx: [str,...]}
if "verified_all"  not in st.session_state: st.session_state.verified_all  = False

total = len(CERTIFICATES)

# ═══════════════════════════════════════════════════════
#   HERO CARD
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
    margin-bottom:0.5rem;
">
  <p style="font-size:0.82rem;text-transform:uppercase;letter-spacing:0.22em;
            color:#00d4ff;margin:0 0 0.8rem;">Verified skills &amp; learning</p>
  <h1 style="font-size:2.6rem;font-weight:800;color:#e5e7eb;margin:0 0 0.7rem;">📜 Certifications</h1>
  <p style="font-size:1rem;color:#9ca3af;line-height:1.7;margin:0;">
    A snapshot of the formal learning and training I've completed on my journey
    as a Full Stack Developer. Each certificate represents real hours of study,
    projects, and dedication — not just a badge.
  </p>
</div>
""", height=220)

# ═══════════════════════════════════════════════════════
#   STATS ROW
# ═══════════════════════════════════════════════════════
liked_count = len(st.session_state.liked_certs)
components.html(f"""
<div style="
    font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
    display:grid;grid-template-columns:repeat(3,1fr);gap:0.7rem;
    margin-top:0.8rem;margin-bottom:0.2rem;
">
  <div style="background:rgba(15,23,42,0.96);border:1px solid rgba(0,212,255,0.25);
       border-radius:14px;padding:1rem;text-align:center;">
    <div style="font-size:2rem;font-weight:900;
                background:linear-gradient(135deg,#00d4ff,#ff6bcb);
                -webkit-background-clip:text;-webkit-text-fill-color:transparent;">
      {total}
    </div>
    <div style="color:#9ca3af;font-size:0.75rem;text-transform:uppercase;
                letter-spacing:0.12em;margin-top:0.2rem;">Certificates</div>
  </div>
  <div style="background:rgba(15,23,42,0.96);border:1px solid rgba(255,107,203,0.25);
       border-radius:14px;padding:1rem;text-align:center;">
    <div style="font-size:2rem;font-weight:900;color:#ff6bcb;">{liked_count}</div>
    <div style="color:#9ca3af;font-size:0.75rem;text-transform:uppercase;
                letter-spacing:0.12em;margin-top:0.2rem;">Liked</div>
  </div>
  <div style="background:rgba(15,23,42,0.96);border:1px solid rgba(52,211,153,0.25);
       border-radius:14px;padding:1rem;text-align:center;">
    <div style="font-size:2rem;font-weight:900;color:#34d399;">2+</div>
    <div style="color:#9ca3af;font-size:0.75rem;text-transform:uppercase;
                letter-spacing:0.12em;margin-top:0.2rem;">Years Learning</div>
  </div>
</div>
""", height=115)

# ═══════════════════════════════════════════════════════
#   CERTIFICATE CAROUSEL
# ═══════════════════════════════════════════════════════
st.markdown("---")
components.html("""
<div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
            margin-bottom:0.5rem;">
  <span style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.2em;color:#00d4ff;">
    Gallery
  </span>
  <h2 style="font-size:1.7rem;font-weight:800;color:#e5e7eb;margin:0.3rem 0 0.3rem;">
    📸 Certificate Viewer
  </h2>
  <p style="color:#9ca3af;font-size:0.9rem;margin:0;">
    Browse through my certificates — like, comment, and explore each one!
  </p>
</div>
""", height=100)

idx  = st.session_state.cert_idx
cert = CERTIFICATES[idx]
liked = idx in st.session_state.liked_certs

# ── Navigation arrows ─────────────────────────────────
nav_l, nav_mid, nav_r = st.columns([1, 8, 1])
with nav_l:
    if st.button("◀", key="prev_cert"):
        st.session_state.cert_idx = (idx - 1) % total
        st.rerun()
with nav_r:
    if st.button("▶", key="next_cert"):
        st.session_state.cert_idx = (idx + 1) % total
        st.rerun()

# ── Cert image ────────────────────────────────────────
if cert["b64"]:
    img_tag = f'<img src="{cert["b64"]}" style="width:100%;border-radius:12px;display:block;object-fit:cover;max-height:420px;"/>'
else:
    # Placeholder when image file not found
    img_tag = f"""
    <div style="
        width:100%;height:320px;border-radius:12px;
        background:linear-gradient(135deg,rgba(0,212,255,0.08),rgba(255,107,203,0.08));
        border:2px dashed rgba(148,163,184,0.3);
        display:flex;flex-direction:column;align-items:center;justify-content:center;
        gap:0.8rem;
    ">
      <div style="font-size:3rem;">📜</div>
      <div style="color:#9ca3af;font-size:0.9rem;text-align:center;padding:0 2rem;">
        Add your certificate image to<br/>
        <strong style="color:#00d4ff;">assets/certificates/{cert['file']}</strong>
      </div>
    </div>
    """

# Skills chips
skill_chips = "".join([
    f'<span style="background:rgba(0,212,255,0.1);border:1px solid rgba(0,212,255,0.3);'
    f'border-radius:999px;padding:0.18rem 0.75rem;font-size:0.75rem;color:#00d4ff;'
    f'font-weight:600;margin-right:0.4rem;margin-bottom:0.4rem;display:inline-block;">{s}</span>'
    for s in cert["skills"]
])

# Progress dots
dots = "".join([
    f'<div style="width:{"20px" if i==idx else "8px"};height:8px;border-radius:999px;'
    f'background:{"linear-gradient(135deg,#00d4ff,#ff6bcb)" if i==idx else "rgba(148,163,184,0.25)"};'
    f'transition:width 0.3s ease;"></div>'
    for i in range(total)
])

components.html(f"""
<div style="
    font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
    background:rgba(15,23,42,0.96);
    border:1px solid {cert['border']};
    border-radius:18px;padding:1.5rem;
    box-shadow:0 24px 60px rgba(0,0,0,0.7);
">
  <!-- Image -->
  {img_tag}

  <!-- Info row -->
  <div style="display:flex;justify-content:space-between;align-items:flex-start;
              margin-top:1.1rem;flex-wrap:wrap;gap:0.5rem;">
    <div style="flex:1;min-width:200px;">
      <div style="font-size:1.15rem;font-weight:800;color:#e5e7eb;margin-bottom:0.25rem;">
        {cert['name']}
      </div>
      <div style="font-size:0.85rem;color:#9ca3af;">
        🏛️ {cert['issuer']} &nbsp;·&nbsp; 📅 {cert['date']}
      </div>
    </div>
    <span style="
        background:rgba(52,211,153,0.12);border:1px solid rgba(52,211,153,0.35);
        border-radius:999px;padding:0.25rem 0.9rem;
        font-size:0.75rem;color:#34d399;font-weight:600;align-self:flex-start;
    ">✔ Verified</span>
  </div>

  <!-- Skills -->
  <div style="margin-top:0.8rem;">{skill_chips}</div>

  <!-- Progress dots -->
  <div style="display:flex;align-items:center;gap:0.4rem;
              justify-content:center;margin-top:1.1rem;">
    {dots}
  </div>
  <div style="text-align:center;color:#6b7280;font-size:0.78rem;margin-top:0.4rem;">
    {idx+1} of {total}
  </div>
</div>
""", height=600 if cert["b64"] else 530)

# ── Quick-jump tabs ───────────────────────────────────
st.markdown("""
<div style="color:#9ca3af;font-size:0.82rem;text-transform:uppercase;
            letter-spacing:0.12em;margin-bottom:0.3rem;margin-top:0.5rem;">
  Jump to certificate:
</div>
""", unsafe_allow_html=True)

tab_cols = st.columns(total)
for i, (col, c) in enumerate(zip(tab_cols, CERTIFICATES)):
    with col:
        label = f"{'✅' if i == idx else '📜'} #{i+1}"
        if st.button(label, key=f"jump_{i}"):
            st.session_state.cert_idx = i
            st.rerun()

# ═══════════════════════════════════════════════════════
#   LIKE + COMMENT SECTION
# ═══════════════════════════════════════════════════════
st.markdown("---")

components.html("""
<div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
            margin-bottom:0.4rem;">
  <span style="font-size:0.75rem;text-transform:uppercase;
               letter-spacing:0.18em;color:#ff6bcb;">React & Feedback</span>
  <h2 style="font-size:1.5rem;font-weight:800;color:#e5e7eb;margin:0.3rem 0 0;">
    ❤️ Like & Leave a Note
  </h2>
</div>
""", height=75)

lc1, lc2 = st.columns([1, 3])
with lc1:
    heart = "❤️ Liked!" if liked else "🤍 Like"
    if st.button(heart, key="like_cert_btn"):
        if idx in st.session_state.liked_certs:
            st.session_state.liked_certs.discard(idx)
        else:
            st.session_state.liked_certs.add(idx)
        st.rerun()

with lc2:
    total_likes = len(st.session_state.liked_certs)
    components.html(f"""
    <div style="font-family:sans-serif;color:#9ca3af;font-size:0.88rem;
                padding-top:0.7rem;">
      {'❤️ You liked this certificate!' if liked else ''}
      {f'&nbsp;·&nbsp; {total_likes} certificate{"s" if total_likes!=1 else ""} liked total' if total_likes > 0 else ''}
    </div>
    """, height=40)

# Comments
comments = st.session_state.cert_comments.get(idx, [])
comment_input = st.text_input(
    "Leave a note about this certificate:",
    placeholder="e.g. Impressive! Django is powerful...",
    key=f"comment_input_{idx}",
)

if st.button("💬 Add Note", key=f"add_comment_{idx}"):
    if comment_input.strip():
        if idx not in st.session_state.cert_comments:
            st.session_state.cert_comments[idx] = []
        st.session_state.cert_comments[idx].append(comment_input.strip())
        st.rerun()

if comments:
    comments_html = "".join([
        f"""
        <div style="background:rgba(15,23,42,0.8);border:1px solid rgba(148,163,184,0.2);
             border-radius:10px;padding:0.65rem 1rem;margin-bottom:0.5rem;
             display:flex;align-items:flex-start;gap:0.6rem;">
          <span style="font-size:1rem;flex-shrink:0;">💬</span>
          <span style="color:#e5e7eb;font-size:0.9rem;line-height:1.5;">{c}</span>
        </div>
        """
        for c in comments
    ])
    components.html(f"""
    <div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
                margin-top:0.5rem;">
      <div style="font-size:0.72rem;text-transform:uppercase;letter-spacing:0.14em;
                  color:#9ca3af;margin-bottom:0.5rem;">
        Notes ({len(comments)})
      </div>
      {comments_html}
    </div>
    """, height=len(comments)*75+40)

# ═══════════════════════════════════════════════════════
#   ALL CERTIFICATES LIST (summary)
# ═══════════════════════════════════════════════════════
st.markdown("---")

components.html("""
<div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
            margin-bottom:0.5rem;">
  <span style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.18em;color:#00d4ff;">
    Overview
  </span>
  <h2 style="font-size:1.5rem;font-weight:800;color:#e5e7eb;margin:0.3rem 0 0.3rem;">
    📋 All Certificates
  </h2>
</div>
""", height=75)

for i, c in enumerate(CERTIFICATES):
    is_current = i == st.session_state.cert_idx
    is_liked   = i in st.session_state.liked_certs
    note_count = len(st.session_state.cert_comments.get(i, []))

    skill_row = "".join([
        f'<span style="background:rgba(0,212,255,0.08);border:1px solid rgba(0,212,255,0.2);'
        f'border-radius:999px;padding:0.12rem 0.6rem;font-size:0.7rem;color:#00d4ff;'
        f'margin-right:0.3rem;">{s}</span>'
        for s in c["skills"]
    ])

    bg     = "rgba(0,212,255,0.05)" if is_current else "rgba(15,23,42,0.96)"
    border = "rgba(0,212,255,0.4)"  if is_current else c["border"]

    components.html(f"""
    <div style="
        font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
        background:{bg};border:1px solid {border};
        border-radius:14px;padding:1rem 1.2rem;margin-bottom:0.6rem;
    ">
      <div style="display:flex;justify-content:space-between;
                  align-items:flex-start;flex-wrap:wrap;gap:0.5rem;">
        <div style="flex:1;min-width:180px;">
          <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.25rem;">
            <span style="font-size:0.72rem;background:rgba(0,212,255,0.1);
                  border:1px solid rgba(0,212,255,0.25);border-radius:999px;
                  padding:0.1rem 0.6rem;color:#00d4ff;">#{i+1}</span>
            {'<span style="font-size:0.68rem;color:#00d4ff;font-weight:600;">● Viewing</span>' if is_current else ''}
          </div>
          <div style="font-size:0.98rem;font-weight:700;color:#e5e7eb;margin-bottom:0.2rem;">
            {c['name']}
          </div>
          <div style="font-size:0.82rem;color:#9ca3af;margin-bottom:0.5rem;">
            {c['issuer']} · {c['date']}
          </div>
          <div>{skill_row}</div>
        </div>
        <div style="display:flex;flex-direction:column;align-items:flex-end;gap:0.3rem;">
          <span style="background:rgba(52,211,153,0.1);border:1px solid rgba(52,211,153,0.3);
                border-radius:999px;padding:0.15rem 0.7rem;
                font-size:0.72rem;color:#34d399;">✔ Verified</span>
          {'<span style="font-size:0.75rem;color:#ff6bcb;">❤️ Liked</span>' if is_liked else ''}
          {f'<span style="font-size:0.72rem;color:#9ca3af;">💬 {note_count} note{"s" if note_count!=1 else ""}</span>' if note_count > 0 else ''}
        </div>
      </div>
    </div>
    """, height=160)

# ═══════════════════════════════════════════════════════
#   DOWNLOAD RESUME
# ═══════════════════════════════════════════════════════
st.markdown("---")

components.html("""
<div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
            margin-bottom:0.5rem;">
  <span style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.18em;color:#34d399;">
    Resume
  </span>
  <h2 style="font-size:1.5rem;font-weight:800;color:#e5e7eb;margin:0.3rem 0 0.3rem;">
    📄 Download My Resume
  </h2>
  <p style="color:#9ca3af;font-size:0.9rem;margin:0;">
    Want to know more? Grab a copy of my latest resume.
  </p>
</div>
""", height=100)

# Try to load actual resume PDF
resume_path = Path("assets/resume.pdf")
if resume_path.exists():
    with open(resume_path, "rb") as f:
        resume_data = f.read()
    resume_filename = "DaveCampo_Resume.pdf"
else:
    resume_data     = b"Dave Campo Resume - PDF coming soon!"
    resume_filename = "DaveCampo_Resume.txt"

st.download_button(
    "⬇️ Download Resume",
    data=resume_data,
    file_name=resume_filename,
    key="resume_download",
)

components.html("""
<div style="font-family:sans-serif;color:#6b7280;font-size:0.8rem;margin-top:0.5rem;">
  📌 Place your resume at <strong style="color:#9ca3af;">assets/resume.pdf</strong> to enable PDF download.
</div>
""", height=35)
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