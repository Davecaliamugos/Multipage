# 🎨 Dave Campo | Developer Portfolio

[![Live Preview](https://img.shields.io/badge/Live%20Preview-View%20Site-00d4ff?style=for-the-badge&logo=streamlit&logoColor=white)](https://d4veeeeeee.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-ff6bcb?style=for-the-badge)](LICENSE)

> 🚀 A stunning, fully responsive multi-page portfolio built with **Streamlit** featuring dark-themed UI, interactive games, smooth animations, and dynamic content.
---

## 📑 Table of Contents

- [🎨 Design](#-design)
- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📁 File Structure](#-file-structure)
- [🚀 Quick Start](#-quick-start)
- [🎯 Pages Overview](#-pages-overview)
- [🎮 Games Collection](#-games-collection)
- [📦 Assets](#-assets)
- [🔧 Components](#-components)
- [📱 Responsive Design](#-responsive-design)
- [🤝 Contributing](#-contributing)

---

## 🎨 Design

### Visual Identity

| Element | Value | Usage |
|---------|-------|-------|
| **Primary Cyan** | `#00d4ff` | Headers, accents, primary buttons |
| **Neon Pink** | `#ff6bcb` | Secondary accents, highlights |
| **Mint Green** | `#34d399` | Success states, badges |
| **Lavender** | `#a78bfa` | Project cards, gradients |
| **Sunny Yellow** | `#fde68a` | Warnings, highlights |
| **Dark Navy** | `#020617` | Background |
| **Surface** | `#0f172a` | Cards, containers |
| **Text** | `#e5e7eb` | Primary text |
| **Muted** | `#9ca3af` | Secondary text |

### Typography

- **Font Family**: Inter (Google Fonts)
- **Weights**: 400, 500, 600, 700, 800, 900
- **Base Size**: 16px with responsive scaling

### Effects

- 🍯 **Honeycomb Background**: Radial gradient with animated honeycomb overlay
- ✨ **Falling Particles**: Dynamic particle animation system
- 🌟 **Glass Morphism**: Backdrop blur and transparency effects
- 🎭 **Smooth Transitions**: CSS animations and hover effects

---

## ✨ Features

### Core Functionality

- ✅ **Multi-page Navigation** - Sidebar-based routing system
- ✅ **Responsive Design** - Mobile-first, works on all devices
- ✅ **Dark Theme** - Consistent dark UI across all pages
- ✅ **Interactive Games** - 6 built-in browser games
- ✅ **Project Showcase** - Filterable project grid with modals
- ✅ **Skills Visualization** - Animated skill bars and categories
- ✅ **Certificate Gallery** - Image viewer with download options
- ✅ **Contact Form** - Functional contact page with social links
- ✅ **Global Effects** - Honeycomb background + particle system

### Interactive Elements

- 🎮 **Snake Game** - Classic arcade with mobile controls
- 🧱 **Tetris** - Block stacking puzzle
- 🧠 **Memory Match** - Card matching game
- 🏓 **Breakout** - Brick breaker arcade
- 🐦 **Flappy Bird** - Side-scrolling game
- 🔨 **Whack-a-Mole** - Reaction time game
- 💻 **Dev Quiz** - Programming knowledge quiz

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core language |
| **Streamlit** | Web app framework |
| **HTML5** | Component templates |
| **CSS3** | Styling and animations |
| **JavaScript** | Game logic and interactivity |
| **Font Awesome** | Icons |
| **Google Fonts** | Typography |

### Python Dependencies

```bash
streamlit>=1.28.0
streamlit-components>=0.1.0
```

---

## 📁 File Structure

```
Activity2/
│
├── 📄 README.md                 # Project documentation
├── 🏠 home.py                   # Main entry point (Home page)
├── 🔧 components.py             # Global components & effects
│
├── 📁 pages/                    # Multi-page application
│   ├── 1_about.py              # About Me page
│   ├── 2_projects.py           # Projects showcase
│   ├── 3_skills.py             # Skills & expertise
│   ├── 4_certificates.py       # Certifications gallery
│   ├── 5_contact.py            # Contact page
│   └── 6_games.py              # Interactive games hub
│
├── 📁 assets/                   # Static assets
│   ├── 📁 cert/                # Certificate images
│   │   ├── cert1.png
│   │   ├── cert2.png
│   │   ├── cert3.png
│   │   ├── cert4.png
│   │   └── cert5.png
│   ├── 📁 profile/             # Profile image
│   │   └── profile.png
│   ├── 📁 project/             # Project screenshots
│   │   ├── pro1.png            # Klee (AI Assistant)
│   │   ├── pro2.png            # 4 Are Left (3D Game)
│   │   ├── pro3.png            # Void 3D (Design Tool)
│   │   ├── pro4.png            # Space Explore (WebGL)
│   │   ├── pro5.png            # Health Care (Management)
│   │   └── pro6.png            # Builder (AI Orchestrator)
│   └── 📄 resume.pdf           # Downloadable resume
│
└── 📁 __pycache__/             # Python cache
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Davecaliamugos/Multipage.git
   cd Activity2
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit
   ```

4. **Run the application**
   ```bash
   streamlit run home.py
   ```

5. **Open in browser**
   - Navigate to `http://localhost:8501`

---

## 🎯 Pages Overview

### 🏠 Home (`home.py`)
- Hero section with animated profile image
- Introduction and role badges
- Quick stats display
- Social links

### 👤 About (`1_about.py`)
- Personal introduction
- Education timeline
- Experience highlights
- Skills summary

### 💼 Projects (`2_projects.py`)
- Filterable project grid (All, Live, Completed, In Progress)
- 6 featured projects with details:
  - **Klee** - OS-level AI Assistant
  - **4 Are Left** - 3D Survival Game
  - **Void 3D** - 3D Design Tool
  - **Space Explore** - WebGL Space Simulation
  - **Health Care** - Management System
  - **Builder** - AI Development Orchestrator
- Modal details with tech stacks
- Live demo & source code links

### 🧠 Skills (`3_skills.py`)
- Categorized skill display
- Animated progress bars
- Programming quiz feature
- Expertise breakdown

### 📜 Certificates (`4_certificates.py`)
- 5 professional certifications:
  - ChatGPT for Python (Simplilearn)
  - Python Django 101 (Simplilearn)
  - Web Scraping (Simplilearn)
  - Android App Development (Simplilearn)
  - React JS Components (Simplilearn)
- Image viewer with download
- Resume download

### 📬 Contact (`5_contact.py`)
- Contact form
- Status badges (Open to Work, etc.)
- Social media links
- Response metrics

### 🎮 Games (`6_games.py`)
- Game selection menu
- 6 playable browser games:
  - Snake
  - Tetris
  - Memory Match
  - Breakout
  - Flappy Bird
  - Whack-a-Mole
- Programming quiz
- Mobile-optimized controls

---

## 🎮 Games Collection

| Game | Genre | Controls | Mobile Ready |
|------|-------|----------|--------------|
| **Snake** | Arcade | Arrow keys / D-Pad | ✅ |
| **Tetris** | Puzzle | Arrow keys / Touch | ✅ |
| **Memory Match** | Brain | Click / Tap | ✅ |
| **Breakout** | Arcade | Mouse / Arrow keys | ✅ |
| **Flappy Bird** | Arcade | Space / Tap | ✅ |
| **Whack-a-Mole** | Reflex | Click / Tap | ✅ |
| **Dev Quiz** | Quiz | Multiple choice | ✅ |

---

## 📦 Assets

### Required Images

Place your images in the following directories:

```
assets/
├── profile/
│   └── profile.png              # Your profile photo (270x270px)
├── cert/
│   ├── cert1.png                # ChatGPT for Python cert
│   ├── cert2.png                # Python Django 101 cert
│   ├── cert3.png                # Web Scraping cert
│   ├── cert4.png                # Android Development cert
│   └── cert5.png                # React JS Components cert
├── project/
│   ├── pro1.png                 # Klee screenshot
│   ├── pro2.png                 # 4 Are Left screenshot
│   ├── pro3.png                 # Void 3D screenshot
│   ├── pro4.png                 # Space Explore screenshot
│   ├── pro5.png                 # Health Care screenshot
│   └── pro6.png                 # Builder screenshot
└── resume.pdf                   # Your resume
```

### Image Guidelines

- **Profile**: 270x270px, PNG format
- **Certificates**: 800x600px or similar, PNG format
- **Projects**: 16:9 aspect ratio, PNG format
- **Resume**: PDF format

---

## 🔧 Components

### Global Effects (`components.py`)

The `apply_global_effects()` function provides:

1. **Honeycomb Background**
   - Animated CSS honeycomb pattern
   - Radial gradient overlay

2. **Falling Particles**
   - Dynamic particle system
   - Configurable count and speed

3. **Sidebar Styling**
   - Custom navigation menu
   - Mobile-responsive

4. **Global CSS**
   - Dark theme variables
   - Button overrides
   - Typography settings

### Usage

```python
from components import apply_global_effects

apply_global_effects()
```

---

## 📱 Responsive Design

### Breakpoints

| Breakpoint | Width | Adjustments |
|------------|-------|-------------|
| Mobile | < 640px | Single column, compact controls |
| Tablet | 640px - 900px | 2-column grid |
| Desktop | > 900px | Full 3-column grid |

### Mobile Optimizations

- Touch-friendly game controls
- Responsive typography (clamp())
- Flexible grid layouts
- Optimized spacing
- Sidebar toggle for navigation

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👨‍💻 Author

**Dave Campo**
- Portfolio: [Live Site](https://your-streamlit-app-url.streamlit.app)
- GitHub: [@Davecaliamugos](https://github.com/Davecaliamugos)

---

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing framework
- [Font Awesome](https://fontawesome.com/) for icons
- [Google Fonts](https://fonts.google.com/) for typography

---

<p align="center">
  Made with ❤️ using Python & Streamlit
</p>
