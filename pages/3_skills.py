import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import streamlit.components.v1 as components
import random
from components import apply_global_effects

st.set_page_config(
    page_title="Skills | Dave Campo",
    page_icon="brain-circuit",
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
iframe { display: block; border: none !important; }
.stApp, .stApp * { color: #e5e7eb; }

div[data-testid="stSelectbox"] > div > div {
    background-color: #0f172a !important;
    border: 1px solid rgba(148,163,184,0.35) !important;
    border-radius: 10px !important;
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
div[data-testid="stRadio"] label p { color: #e5e7eb !important; font-size: 0.95rem !important; }
div[data-testid="stRadio"] > div { gap: 1rem; }
div[data-testid="stRadio"] > div > label {
    background: rgba(15,23,42,0.6) !important;
    border: 1px solid rgba(148,163,184,0.25) !important;
    border-radius: 8px !important;
    padding: 0.4rem 1rem !important;
}
div[data-testid="stRadio"] > div > label:hover { border-color: #00d4ff !important; }
div[data-testid="stButton"] button {
    background: linear-gradient(135deg, #00d4ff, #ff6bcb) !important;
    color: #000 !important; font-weight: 700 !important;
    border: none !important; border-radius: 10px !important;
    padding: 0.55rem 1.8rem !important; font-size: 0.97rem !important;
}
div[data-testid="stButton"] button p { color: #000 !important; }
div[data-testid="stAlert"] {
    border-radius: 10px !important;
    background: rgba(15,23,42,0.8) !important;
    border: 1px solid rgba(148,163,184,0.3) !important;
}
div[data-testid="stAlert"] p { color: #e5e7eb !important; }
h1, h2, h3, h4 { color: #e5e7eb !important; }
hr { border-color: rgba(148,163,184,0.2) !important; margin: 1.5rem 0 !important; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#   SKILL CATEGORIES DATA
# ─────────────────────────────────────────────
SKILL_CATEGORIES = [
    {
        "label": "Languages",
        "icon": "monitor",
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
        "icon": "globe",
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
        "icon": "zap",
        "color": "#86efac",
        "border": "rgba(22,163,74,0.35)",
        "bg": "rgba(22,163,74,0.08)",
        "skills": [
            ("Django",               50),
            ("Django REST Framework",45),
            ("Django Channels",      35),
            ("Django Allauth",       60),

        ],
    },
    {
        "label": "Databases",
        "icon": "database",
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
        "icon": "code",
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
        "icon": "wrench",
        "color": "#c4b5fd",
        "border": "rgba(167,139,250,0.35)",
        "bg": "rgba(167,139,250,0.08)",
        "skills": [
            ("GitHub", 78),
            ("VS Code",      85),
            ("Canva",        72),
            ("Spline 3D",    60),
            ("ChatGpt",        90),
        ],
    },
]

# ─────────────────────────────────────────────
#   QUIZ DATA
# ─────────────────────────────────────────────
QUESTION_BANK = [
    {"question":"What does HTML stand for?",
     "options":["HyperText Markup Language","HighText Machine Language","HyperText and links Markup Language","None of the above"],
     "answer":"HyperText Markup Language","explanation":"HTML stands for HyperText Markup Language — the standard language for creating web pages.","category":"Frontend"},
    {"question":"Which Python keyword is used to define a function?",
     "options":["func","define","def","function"],"answer":"def",
     "explanation":"`def` is the keyword used to define a function in Python.","category":"Python"},
    {"question":"What is the time complexity of binary search?",
     "options":["O(n)","O(n²)","O(log n)","O(1)"],"answer":"O(log n)",
     "explanation":"Binary search repeatedly halves the search space, giving O(log n) time complexity.","category":"Algorithms"},
    {"question":"Which of the following is NOT a JavaScript data type?",
     "options":["String","Boolean","Integer","Symbol"],"answer":"Integer",
     "explanation":"JavaScript has Number (not Integer), String, Boolean, Symbol, BigInt, Object, undefined, and null.","category":"Frontend"},
    {"question":"What does CSS stand for?",
     "options":["Creative Style Sheets","Cascading Style Sheets","Computer Style Sheets","Colorful Style Sheets"],
     "answer":"Cascading Style Sheets","explanation":"CSS stands for Cascading Style Sheets — used to style HTML documents.","category":"Frontend"},
    {"question":"Which HTTP method is typically used to CREATE a resource?",
     "options":["GET","PUT","DELETE","POST"],"answer":"POST",
     "explanation":"POST is used to create a new resource on the server in RESTful APIs.","category":"Backend"},
    {"question":"In Python, what is the output of `type([])`?",
     "options":["<class 'tuple'>","<class 'dict'>","<class 'list'>","<class 'set'>"],
     "answer":"<class 'list'>","explanation":"`[]` creates an empty list, so `type([])` returns `<class 'list'>`.","category":"Python"},
    {"question":"Which SQL clause is used to filter records?",
     "options":["ORDER BY","GROUP BY","WHERE","HAVING"],"answer":"WHERE",
     "explanation":"The WHERE clause filters rows before any grouping or aggregation.","category":"Backend"},
    {"question":"What does 'git clone' do?",
     "options":["Creates a new branch","Copies a remote repository locally","Merges two branches","Stages files for commit"],
     "answer":"Copies a remote repository locally","explanation":"`git clone` downloads a full copy of a remote repository to your machine.","category":"DevOps"},
    {"question":"Which design principle means a class should have only one reason to change?",
     "options":["Open/Closed Principle","Liskov Substitution","Single Responsibility Principle","Interface Segregation"],
     "answer":"Single Responsibility Principle","explanation":"The Single Responsibility Principle (SRP) states a class should have only one job.","category":"Software Design"},
    {"question":"What is a Python list comprehension?",
     "options":["A way to import modules","A concise way to create lists using a single line","A method to sort lists","A type of Python loop only"],
     "answer":"A concise way to create lists using a single line","explanation":"List comprehensions like `[x*2 for x in range(5)]` let you build lists concisely.","category":"Python"},
    {"question":"Which data structure operates on LIFO (Last In, First Out)?",
     "options":["Queue","Stack","Linked List","Tree"],"answer":"Stack",
     "explanation":"A Stack follows LIFO — the last element pushed is the first one popped.","category":"Algorithms"},
    {"question":"What is the purpose of a REST API?",
     "options":["Style web pages","Manage databases directly","Allow communication between client and server over HTTP","Compile Python code"],
     "answer":"Allow communication between client and server over HTTP","explanation":"REST APIs expose endpoints that clients call over HTTP to exchange data with a server.","category":"Backend"},
    {"question":"In UI/UX, what does 'affordance' mean?",
     "options":["The cost of a design tool","A visual cue that suggests how an object should be used","The loading speed of a page","A type of color scheme"],
     "answer":"A visual cue that suggests how an object should be used","explanation":"Affordance refers to design properties that hint at how something should be interacted with.","category":"UI/UX"},
    {"question":"Which Python library is most commonly used for data manipulation?",
     "options":["NumPy","Flask","Pandas","Requests"],"answer":"Pandas",
     "explanation":"Pandas provides powerful DataFrames for data analysis and manipulation.","category":"Python"},
    {"question":"What does Django ORM stand for?",
     "options":["Object Relational Mapper","Object Resource Manager","Online Request Model","Open Routing Method"],
     "answer":"Object Relational Mapper","explanation":"Django ORM (Object Relational Mapper) lets you interact with your database using Python instead of SQL.","category":"Django"},
    {"question":"Which Django library is used for real-time WebSocket support?",
     "options":["Django REST Framework","Django Allauth","Django Channels","Celery"],
     "answer":"Django Channels","explanation":"Django Channels extends Django to handle WebSockets, enabling real-time features.","category":"Django"},
    {"question":"What is Celery used for in Django projects?",
     "options":["Frontend styling","Database migrations","Background task processing","User authentication"],
     "answer":"Background task processing","explanation":"Celery is a distributed task queue used to run background jobs asynchronously in Django apps.","category":"Django"},
    {"question":"Which C++ concept allows a function to have multiple forms?",
     "options":["Encapsulation","Polymorphism","Abstraction","Inheritance"],
     "answer":"Polymorphism","explanation":"Polymorphism allows functions or methods to take multiple forms in C++ (e.g., function overloading).","category":"C++"},
    {"question":"In MySQL, which command retrieves data from a table?",
     "options":["INSERT","UPDATE","SELECT","DELETE"],
     "answer":"SELECT","explanation":"SELECT is the SQL command used to retrieve data from one or more tables in MySQL.","category":"Database"},
]

NUM_QUESTIONS = 5

def init_quiz():
    selected = random.sample(QUESTION_BANK, NUM_QUESTIONS)
    st.session_state.quiz_questions = selected
    st.session_state.quiz_index     = 0
    st.session_state.quiz_score     = 0
    st.session_state.quiz_answers   = {}
    st.session_state.quiz_submitted = {}
    st.session_state.quiz_finished  = False
    st.session_state.quiz_started   = True

if "quiz_started" not in st.session_state:
    init_quiz()

# ═══════════════════════════════════════════════════════
#   HERO CARD
# ═══════════════════════════════════════════════════════
components.html("""
<div style="
    font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
    background:rgba(15,23,42,0.96);
    border-radius:18px;
    border:1px solid rgba(148,163,184,0.35);
    padding:2rem 2.2rem 1.8rem;
    box-shadow:0 24px 60px rgba(0,0,0,0.85);
    backdrop-filter:blur(18px);
    margin-bottom:0.5rem;
">
  <p style="font-size:0.82rem;text-transform:uppercase;letter-spacing:0.22em;
            color:#00d4ff;margin:0 0 0.7rem;">What I work with</p>
  <h1 style="font-size:2.6rem;font-weight:800;color:#e5e7eb;margin:0 0 0.6rem;"><svg xmlns=\"http://www.w3.org/2000/svg\" width=\"32\" height=\"32\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#00d4ff\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;margin-right:8px;\"><path d=\"M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24l.67-.23a2.5 2.5 0 0 0 1.32-4.24l-.11-.47\"/><path d=\"M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24l-.67-.23a2.5 2.5 0 0 1-1.32-4.24l.11-.47\"/></svg>Skills</h1>
  <p style="font-size:1rem;color:#9ca3af;line-height:1.65;margin:0;">
    A full-stack developer's 
    Here's everything I work with.
  </p>
</div>
""", height=210)

# ═══════════════════════════════════════════════════════
#   SKILL CATEGORIES — one card per category
# ═══════════════════════════════════════════════════════
for cat in SKILL_CATEGORIES:
    # Build bars HTML
    bars_html = ""
    for skill_name, pct in cat["skills"]:
        bars_html += f"""
        <div style="margin-bottom:0.85rem;">
          <div style="display:flex;justify-content:space-between;margin-bottom:0.28rem;">
            <span style="color:#e5e7eb;font-size:0.92rem;font-weight:500;">{skill_name}</span>
            <span style="color:{cat['color']};font-size:0.82rem;font-weight:700;">{pct}%</span>
          </div>
          <div style="width:100%;height:8px;border-radius:999px;
               background:rgba(148,163,184,0.1);
               border:1px solid rgba(148,163,184,0.15);overflow:hidden;">
            <div style="width:{pct}%;height:100%;border-radius:999px;
                 background:linear-gradient(135deg,{cat['color']},rgba(255,255,255,0.25));
                 box-shadow:0 0 10px {cat['bg']};"></div>
          </div>
        </div>
        """

    card_height = len(cat["skills"]) * 52 + 90

    components.html(f"""
    <div style="
        font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
        background:rgba(15,23,42,0.96);
        border:1px solid {cat['border']};
        border-radius:16px;
        padding:1.4rem 1.6rem;
        margin-bottom:0.8rem;
        box-shadow:0 8px 30px rgba(0,0,0,0.5);
    ">
      <!-- Category header -->
      <div style="display:flex;align-items:center;gap:0.6rem;margin-bottom:1.1rem;">
        <span style="font-size:1.3rem;">{cat['icon']}</span>
        <div>
          <div style="font-size:0.68rem;text-transform:uppercase;letter-spacing:0.16em;
                      color:{cat['color']};margin-bottom:0.1rem;">{cat['label']}</div>
          <div style="font-size:0.78rem;color:#6b7280;">{len(cat['skills'])} technologies</div>
        </div>
      </div>
      <!-- Bars -->
      {bars_html}
    </div>
    """, height=card_height)

# ═══════════════════════════════════════════════════════
#   TECH BADGE CLOUD
# ═══════════════════════════════════════════════════════
all_badges = [
    # (label, color, bg, border)
    ("C",                    "#fca5a5","rgba(239,68,68,0.1)","rgba(239,68,68,0.35)"),
    ("C++",                  "#fca5a5","rgba(239,68,68,0.1)","rgba(239,68,68,0.35)"),
    ("Python",               "#93c5fd","rgba(59,130,246,0.1)","rgba(59,130,246,0.35)"),
    ("JavaScript",           "#fde047","rgba(253,224,71,0.08)","rgba(253,224,71,0.3)"),
    ("HTML",                 "#fdba74","rgba(251,146,60,0.1)","rgba(251,146,60,0.35)"),
    ("CSS",                  "#7dd3fc","rgba(56,189,248,0.1)","rgba(56,189,248,0.3)"),
    ("React",                "#7dd3fc","rgba(56,189,248,0.1)","rgba(56,189,248,0.3)"),
    ("Django",               "#86efac","rgba(22,163,74,0.1)","rgba(22,163,74,0.35)"),
    ("Django REST",          "#86efac","rgba(22,163,74,0.1)","rgba(22,163,74,0.35)"),
    ("Django Channels",      "#86efac","rgba(22,163,74,0.1)","rgba(22,163,74,0.35)"),
    ("Celery",               "#86efac","rgba(22,163,74,0.1)","rgba(22,163,74,0.35)"),
    ("Django Allauth",       "#86efac","rgba(22,163,74,0.1)","rgba(22,163,74,0.35)"),
    ("Django ORM",           "#86efac","rgba(22,163,74,0.1)","rgba(22,163,74,0.35)"),
    ("MySQL",                "#fde68a","rgba(234,179,8,0.08)","rgba(234,179,8,0.3)"),
    ("MS Access",            "#fde68a","rgba(234,179,8,0.08)","rgba(234,179,8,0.3)"),
    ("SQLite",               "#fde68a","rgba(234,179,8,0.08)","rgba(234,179,8,0.3)"),
    ("Streamlit",            "#00d4ff","rgba(0,212,255,0.08)","rgba(0,212,255,0.3)"),
    ("OpenCV",               "#93c5fd","rgba(59,130,246,0.1)","rgba(59,130,246,0.3)"),
    ("Pandas",               "#93c5fd","rgba(59,130,246,0.1)","rgba(59,130,246,0.3)"),
    ("NumPy",                "#93c5fd","rgba(59,130,246,0.1)","rgba(59,130,246,0.3)"),
    ("Spline 3D",            "#c4b5fd","rgba(167,139,250,0.1)","rgba(167,139,250,0.3)"),
    ("Canva",                "#ff6bcb","rgba(255,107,203,0.1)","rgba(255,107,203,0.3)"),
    ("Git & GitHub",         "#fdba74","rgba(251,146,60,0.1)","rgba(251,146,60,0.3)"),
    ("VS Code",              "#9ca3af","rgba(148,163,184,0.08)","rgba(148,163,184,0.25)"),
]

badges_html = "".join([
    f'<span style="background:{bg};border:1px solid {border};border-radius:999px;'
    f'padding:0.28rem 0.85rem;font-size:0.8rem;color:{color};font-weight:600;'
    f'white-space:nowrap;">{label}</span>'
    for label, color, bg, border in all_badges
])

components.html(f"""
<div style="
    font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
    background:rgba(15,23,42,0.96);
    border:1px solid rgba(148,163,184,0.2);
    border-radius:16px;
    padding:1.4rem 1.6rem;
    margin-bottom:0.8rem;
">
  <div style="font-size:0.68rem;text-transform:uppercase;letter-spacing:0.16em;
              color:#00d4ff;margin-bottom:0.5rem;">Full Tech Stack</div>
  <div style="font-size:1rem;font-weight:700;color:#e5e7eb;margin-bottom:1rem;">
    <svg xmlns=\"http://www.w3.org/2000/svg\" width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#00d4ff\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;margin-right:6px;\"><path d=\"M12 2H2v10l9.29 9.29c.94.94 2.48.94 3.42 0l6.58-6.58c.94-.94.94-2.48 0-3.42L12 2Z\"/><path d=\"M7 7h.01\"/></svg>All Technologies at a Glance
  </div>
  <div style="display:flex;flex-wrap:wrap;gap:0.45rem;">
    {badges_html}
  </div>
</div>
""", height=185)

# ═══════════════════════════════════════════════════════
#   INTEREST RADIO
# ═══════════════════════════════════════════════════════
st.markdown("---")
st.markdown("""
<p style="color:#9ca3af;font-size:0.9rem;margin-bottom:0.3rem;">
  Which area interests you most?
</p>
""", unsafe_allow_html=True)

choice = st.radio(
    "Which area interests you most?",
    ["Frontend", "Backend", "AI / Python", "Django"],
    index=0, horizontal=True, label_visibility="collapsed",
)

interest_map = {
    "Frontend":    ("React, HTML, CSS, JavaScript, Spline & Canva for UI/UX design.", "#7dd3fc", "rgba(56,189,248,0.08)", "rgba(56,189,248,0.3)"),
    "Backend":     ("Django, DRF, Django Channels, Celery, MySQL & REST API development.", "#86efac", "rgba(22,163,74,0.08)", "rgba(22,163,74,0.3)"),
    "AI / Python": ("OpenCV, DeepFace, Pandas, NumPy, Streamlit & Python scripting.", "#93c5fd", "rgba(59,130,246,0.08)", "rgba(59,130,246,0.3)"),
    "Django":      ("Full Django ecosystem — ORM, REST, Channels, Celery, Allauth & more.", "#86efac", "rgba(22,163,74,0.08)", "rgba(22,163,74,0.3)"),
}

desc, col, bg, border = interest_map[choice]

st.markdown(f"""
<div style="
    background:{bg};border:1px solid {border};
    border-radius:10px;padding:0.75rem 1rem;
    margin-top:0.5rem;font-size:0.95rem;color:#e5e7eb;
">
  <svg xmlns=\"http://www.w3.org/2000/svg\" width=\"16\" height=\"16\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"{col}\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;margin-right:4px;\"><path d=\"m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z\"/></svg><strong style="color:{col};">{choice}:</strong> {desc}
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
#   QUIZ SECTION
# ═══════════════════════════════════════════════════════
st.markdown("---")

components.html("""
<div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
            margin-bottom:0.5rem;">
  <span style="font-size:0.78rem;text-transform:uppercase;
               letter-spacing:0.2em;color:#00d4ff;">Test your knowledge</span>
  <h2 style="font-size:1.9rem;font-weight:800;color:#e5e7eb;margin:0.3rem 0 0.4rem;">
    <svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#fde047\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;margin-right:8px;\"><path d=\"M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5\"/><path d=\"M9 18h6\"/><path d=\"M10 22h4\"/></svg>Programming Quiz
  </h2>
  <p style="color:#9ca3af;font-size:0.97rem;margin:0;">
    Answer 5 randomly selected questions from my actual tech stack and see how you score!
  </p>
</div>
""", height=110)

# ── Finished ──────────────────────────────────────────
if st.session_state.quiz_finished:
    score = st.session_state.quiz_score
    total = NUM_QUESTIONS
    pct   = int((score / total) * 100)

    if score == total:       emoji, msg = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"16\" height=\"16\" viewBox=\"0 0 24 24\" fill=\"#fde047\" stroke=\"#fde047\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;\"><path d=\"M6 9H4.5a2.5 2.5 0 0 1 0-5H6\"/><path d=\"M18 9h1.5a2.5 2.5 0 0 0 0-5H18\"/><path d=\"M4 22h16\"/><path d=\"M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22\"/><path d=\"M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22\"/><path d=\"M18 2H6v7a6 6 0 0 0 12 0V2Z\"/></svg>", "Perfect score! You know my stack!"
    elif score >= total*0.8: emoji, msg = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"16\" height=\"16\" viewBox=\"0 0 24 24\" fill=\"#ff6bcb\" stroke=\"#ff6bcb\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;\"><path d=\"M6 9H4.5a2.5 2.5 0 0 1 0-5H6\"/><path d=\"M18 9h1.5a2.5 2.5 0 0 0 0-5H18\"/><path d=\"M4 22h16\"/><path d=\"M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22\"/><path d=\"M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22\"/><path d=\"M18 2H6v7a6 6 0 0 0 12 0V2Z\"/></svg>", "Excellent work! Almost flawless!"
    elif score >= total*0.6: emoji, msg = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"16\" height=\"16\" viewBox=\"0 0 24 24\" fill=\"#00d4ff\" stroke=\"#00d4ff\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;\"><path d=\"M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3\"/></svg>", "Good job! Keep practising!"
    elif score >= total*0.4: emoji, msg = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"16\" height=\"16\" viewBox=\"0 0 24 24\" fill=\"#fde047\" stroke=\"#fde047\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;\"><path d=\"M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20\"/></svg>", "Not bad — review the explanations below!"
    else:                    emoji, msg = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"16\" height=\"16\" viewBox=\"0 0 24 24\" fill=\"#34d399\" stroke=\"#34d399\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;\"><path d=\"M6.5 6.5h11.9\"/><path d=\"M2.8 12.2h19.4\"/><path d=\"M2.8 17.8h19.4\"/></svg>", "Keep going — every expert was once a beginner!"

    components.html(f"""
    <div style="background:linear-gradient(135deg,rgba(0,212,255,0.08),rgba(255,107,203,0.08));
         border:1px solid rgba(0,212,255,0.3);border-radius:18px;
         padding:2.2rem 2rem;text-align:center;
         font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;">
      <div style="font-size:3.5rem;">{emoji}</div>
      <div style="font-size:4.5rem;font-weight:900;
                  background:linear-gradient(135deg,#00d4ff,#ff6bcb);
                  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                  line-height:1.1;margin-top:0.4rem;">{score} / {total}</div>
      <div style="color:#9ca3af;font-size:1rem;margin-top:0.3rem;">{pct}% correct</div>
      <div style="color:#e5e7eb;font-size:1.2rem;font-weight:700;margin-top:1rem;">{msg}</div>
      <div style="width:80%;height:8px;border-radius:999px;background:rgba(148,163,184,0.15);
           margin:1.2rem auto 0;overflow:hidden;">
        <div style="width:{pct}%;height:100%;border-radius:999px;
             background:linear-gradient(135deg,#00d4ff,#ff6bcb);"></div>
      </div>
    </div>
    """, height=310)

    components.html("""
    <h3 style="font-family:sans-serif;color:#e5e7eb;font-size:1.2rem;
               font-weight:700;margin-top:1rem;margin-bottom:0.2rem;">
      <svg xmlns=\"http://www.w3.org/2000/svg\" width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#e5e7eb\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;margin-right:6px;\"><path d=\"M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2\"/><path d=\"M15 2H9a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V3a1 1 0 0 0-1-1Z\"/></svg>Answer Review
    </h3>
    """, height=50)

    for i, q in enumerate(st.session_state.quiz_questions):
        user_ans   = st.session_state.quiz_answers.get(i, "—")
        correct    = q["answer"]
        is_correct = user_ans == correct
        icon       = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"16\" height=\"16\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#6ee7b7\" stroke-width=\"3\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;\"><polyline points=\"20 6 9 17 4 12\"/></svg>" if is_correct else "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"16\" height=\"16\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#fca5a5\" stroke-width=\"3\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;\"><path d=\"M18 6 6 18\"/><path d=\"m6 6 12 12\"/></svg>"
        bg         = "rgba(16,185,129,0.08)"  if is_correct else "rgba(239,68,68,0.08)"
        bdr        = "rgba(16,185,129,0.35)"  if is_correct else "rgba(239,68,68,0.35)"
        a_col      = "#6ee7b7"                if is_correct else "#fca5a5"
        wrong_row  = "" if is_correct else f'<div style="font-size:0.88rem;margin-top:0.2rem;"><span style="color:#9ca3af;">Correct: </span><span style="color:#6ee7b7;font-weight:600;">{correct}</span></div>'

        components.html(f"""
        <div style="background:{bg};border:1px solid {bdr};border-radius:12px;
             padding:1rem 1.2rem;margin-bottom:0.6rem;
             font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:0.5rem;">
            <div style="color:#e5e7eb;font-weight:600;font-size:0.95rem;line-height:1.45;flex:1;">
              {icon} Q{i+1}: {q['question']}
            </div>
            <span style="background:rgba(0,212,255,0.1);border:1px solid rgba(0,212,255,0.3);
                  border-radius:999px;padding:0.15rem 0.7rem;
                  font-size:0.7rem;color:#00d4ff;white-space:nowrap;">{q['category']}</span>
          </div>
          <div style="font-size:0.88rem;margin-top:0.6rem;">
            <span style="color:#9ca3af;">Your answer: </span>
            <span style="color:{a_col};font-weight:600;">{user_ans}</span>
          </div>
          {wrong_row}
          <div style="font-size:0.83rem;color:#9ca3af;line-height:1.5;
               margin-top:0.6rem;padding-top:0.6rem;
               border-top:1px solid rgba(148,163,184,0.15);">
            <svg xmlns=\"http://www.w3.org/2000/svg\" width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#9ca3af\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;margin-right:4px;\"><path d=\"M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5\"/><path d=\"M9 18h6\"/><path d=\"M10 22h4\"/></svg>{q['explanation']}
          </div>
        </div>
        """, height=200 if is_correct else 225)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#00d4ff\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;margin-right:4px;\"><path d=\"M21 12a9 9 0 0 0-9-9 9.75 9.75 0 0 0-6.74 2.74L3 8\"/><path d=\"M3 3v5h5\"/><path d=\"M3 12a9 9 0 0 0 9 9 9.75 9.75 0 0 0 6.74-2.74L21 16\"/><path d=\"M16 21h5v-5\"/></svg>Restart Quiz", key="restart_btn"):
        init_quiz()
        st.rerun()

# ── Active quiz ────────────────────────────────────────
else:
    idx      = st.session_state.quiz_index
    q        = st.session_state.quiz_questions[idx]
    progress = idx / NUM_QUESTIONS

    col_prog, col_score = st.columns([3, 1])
    with col_prog:
        components.html(f"""
        <div style="font-family:sans-serif;">
          <div style="color:#9ca3af;font-size:0.83rem;margin-bottom:0.45rem;">
            Question {idx+1} of {NUM_QUESTIONS}
          </div>
          <div style="width:100%;height:7px;border-radius:999px;
               background:rgba(148,163,184,0.15);overflow:hidden;">
            <div style="width:{int(progress*100)}%;height:100%;border-radius:999px;
                 background:linear-gradient(135deg,#00d4ff,#ff6bcb);"></div>
          </div>
        </div>
        """, height=52)

    with col_score:
        components.html(f"""
        <div style="font-family:sans-serif;text-align:right;">
          <div style="display:inline-block;
               background:linear-gradient(135deg,rgba(0,212,255,0.12),rgba(255,107,203,0.12));
               border:1px solid rgba(0,212,255,0.35);border-radius:999px;
               padding:0.3rem 1rem;font-size:0.88rem;color:#00d4ff;font-weight:700;">
            Score: {st.session_state.quiz_score}/{NUM_QUESTIONS}
          </div>
        </div>
        """, height=52)

    components.html(f"""
    <div style="background:rgba(15,23,42,0.96);border:1px solid rgba(148,163,184,0.35);
         border-radius:14px;padding:1.5rem 1.6rem 1.3rem;
         font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
         margin-bottom:0.3rem;">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.7rem;">
        <span style="font-size:0.72rem;text-transform:uppercase;letter-spacing:0.18em;color:#00d4ff;">
          Question {idx+1}
        </span>
        <span style="background:rgba(0,212,255,0.1);border:1px solid rgba(0,212,255,0.3);
               border-radius:999px;padding:0.15rem 0.75rem;font-size:0.72rem;color:#00d4ff;">
          {q['category']}
        </span>
      </div>
      <div style="font-size:1.12rem;font-weight:700;color:#e5e7eb;line-height:1.5;">
        {q['question']}
      </div>
    </div>
    """, height=130)

    already_submitted = idx in st.session_state.quiz_submitted
    current_answer    = st.session_state.quiz_answers.get(idx, None)

    options_html = ""
    for opt in q["options"]:
        is_sel = current_answer == opt
        if already_submitted:
            if opt == q["answer"]:
                bg,bdr,dot,lc = "rgba(16,185,129,0.15)","rgba(16,185,129,0.6)","#6ee7b7","#6ee7b7"
            elif is_sel and opt != q["answer"]:
                bg,bdr,dot,lc = "rgba(239,68,68,0.12)","rgba(239,68,68,0.55)","#fca5a5","#fca5a5"
            else:
                bg,bdr,dot,lc = "rgba(15,23,42,0.5)","rgba(148,163,184,0.2)","transparent","#4b5563"
        else:
            bg  = "rgba(0,212,255,0.1)"  if is_sel else "rgba(15,23,42,0.5)"
            bdr = "rgba(0,212,255,0.5)"  if is_sel else "rgba(148,163,184,0.25)"
            dot = "#00d4ff"              if is_sel else "transparent"
            lc  = "#e5e7eb"

        options_html += f"""
        <div style="display:flex;align-items:center;gap:0.75rem;
             background:{bg};border:1px solid {bdr};border-radius:10px;
             padding:0.75rem 1rem;margin-bottom:0.5rem;">
          <div style="width:16px;height:16px;border-radius:50%;
               border:2px solid {bdr};background:{dot};flex-shrink:0;"></div>
          <span style="color:{lc};font-size:0.95rem;font-weight:500;">{opt}</span>
        </div>
        """

    components.html(f"""
    <div style="font-family:sans-serif;margin-bottom:0.5rem;">
      <div style="color:#9ca3af;font-size:0.83rem;margin-bottom:0.6rem;
                  text-transform:uppercase;letter-spacing:0.12em;">Choose your answer</div>
      {options_html}
    </div>
    """, height=len(q["options"])*68+40)

    if not already_submitted:
        st.markdown('<div style="color:#9ca3af;font-size:0.82rem;margin-bottom:0.2rem;">Select from dropdown to confirm:</div>', unsafe_allow_html=True)
        selected = st.selectbox("Answer", ["— Select an answer —"] + q["options"],
                                key=f"answer_{idx}", label_visibility="collapsed")
        if selected != "— Select an answer —":
            st.session_state.quiz_answers[idx] = selected
    else:
        selected = st.session_state.quiz_answers.get(idx, "—")

    bc1, bc2, _ = st.columns([1, 1, 3])
    with bc1:
        if not already_submitted:
            if st.button("<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#6ee7b7\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;margin-right:4px;\"><polyline points=\"20 6 9 17 4 12\"/></svg>Submit", key=f"submit_{idx}"):
                ans = st.session_state.quiz_answers.get(idx)
                if not ans:
                    st.markdown('<div style="background:rgba(251,191,36,0.1);border:1px solid rgba(251,191,36,0.4);border-radius:8px;padding:0.6rem 1rem;color:#fde68a;font-size:0.9rem;"><svg xmlns=\"http://www.w3.org/2000/svg\" width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#fde047\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;margin-right:4px;\"><path d=\"m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z\"/><path d=\"M12 9v4\"/><path d=\"M12 17h.01\"/></svg>Please select an answer first!</div>', unsafe_allow_html=True)
                else:
                    st.session_state.quiz_submitted[idx] = True
                    if ans == q["answer"]: st.session_state.quiz_score += 1
                    st.rerun()
    with bc2:
        if already_submitted:
            is_last = idx == NUM_QUESTIONS - 1
            if st.button("<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#00d4ff\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;margin-right:4px;\"><path d=\"M6 9H4.5a2.5 2.5 0 0 1 0-5H6\"/><path d=\"M18 9h1.5a2.5 2.5 0 0 0 0-5H18\"/><path d=\"M4 22h16\"/><path d=\"M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22\"/><path d=\"M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22\"/><path d=\"M18 2H6v7a6 6 0 0 0 12 0V2Z\"/></svg>See Results" if is_last else "Next <svg xmlns=\"http://www.w3.org/2000/svg\" width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#00d4ff\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;\"><path d=\"m9 18 6-6-6-6\"/></svg>", key=f"next_{idx}"):
                if is_last: st.session_state.quiz_finished = True
                else:
                    st.session_state.quiz_index += 1
                st.rerun()

    if already_submitted:
        user_ans   = st.session_state.quiz_answers.get(idx, "")
        is_correct = user_ans == q["answer"]
        if is_correct:
            components.html(f"""
            <div style="background:rgba(16,185,129,0.12);border:1px solid rgba(16,185,129,0.45);
                 border-radius:10px;padding:1rem 1.2rem;
                 font-family:sans-serif;margin-top:0.5rem;">
              <div style="color:#6ee7b7;font-weight:700;font-size:1rem;"><svg xmlns=\"http://www.w3.org/2000/svg\" width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#6ee7b7\" stroke-width=\"3\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;margin-right:4px;\"><polyline points=\"20 6 9 17 4 12\"/></svg>Correct! Well done!</div>
              <div style="color:#9ca3af;font-size:0.85rem;margin-top:0.4rem;line-height:1.5;">
                <svg xmlns=\"http://www.w3.org/2000/svg\" width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#9ca3af\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;margin-right:4px;\"><path d=\"M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5\"/><path d=\"M9 18h6\"/><path d=\"M10 22h4\"/></svg>{q['explanation']}
              </div>
            </div>
            """, height=115)
        else:
            components.html(f"""
            <div style="background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.4);
                 border-radius:10px;padding:1rem 1.2rem;
                 font-family:sans-serif;margin-top:0.5rem;">
              <div style="color:#fca5a5;font-weight:700;font-size:1rem;"><svg xmlns=\"http://www.w3.org/2000/svg\" width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#fca5a5\" stroke-width=\"3\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;margin-right:4px;\"><path d=\"M18 6 6 18\"/><path d=\"m6 6 12 12\"/></svg>Incorrect</div>
              <div style="color:#9ca3af;font-size:0.88rem;margin-top:0.35rem;">
                Your answer: <span style="color:#fca5a5;font-weight:600;">{user_ans}</span>
              </div>
              <div style="color:#9ca3af;font-size:0.88rem;margin-top:0.2rem;">
                Correct: <span style="color:#6ee7b7;font-weight:600;">{q['answer']}</span>
              </div>
              <div style="color:#9ca3af;font-size:0.85rem;line-height:1.5;
                   margin-top:0.5rem;padding-top:0.5rem;
                   border-top:1px solid rgba(148,163,184,0.15);">
                <svg xmlns=\"http://www.w3.org/2000/svg\" width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#9ca3af\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:middle;margin-right:4px;\"><path d=\"M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5\"/><path d=\"M9 18h6\"/><path d=\"M10 22h4\"/></svg>{q['explanation']}
              </div>
            </div>
            """, height=170)
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