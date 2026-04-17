import streamlit as st
import streamlit.components.v1 as components

def apply_global_effects():
    """
    Apply honeycomb background and falling particles effect to all pages.
    Uses Streamlit's default sidebar navigation.
    """
    # Honeycomb background + falling particles CSS and HTML
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

    /* ========== GLOBAL RESETS ========== */
    .stApp {
        background: radial-gradient(ellipse at 10% 0%, #0a0f1a 0%, #020617 50%, #000 100%) !important;
        min-height: 100vh;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        position: relative;
    }

    /* Honeycomb Background Pattern */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image:
            radial-gradient(circle at 50% 50%, rgba(0, 212, 255, 0.03) 0%, transparent 50%),
            url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='28' height='49' viewBox='0 0 28 49'%3E%3Cg fill-rule='evenodd'%3E%3Cg id='hexagons' fill='%2300d4ff' fill-opacity='0.05' fill-rule='nonzero'%3E%3Cpath d='M13.99 9.25l13 7.5v15l-13 7.5L1 31.75v-15l12.99-7.5zM3 17.9v12.7l10.99 6.34 11-6.35V17.9l-11-6.34L3 17.9zM0 15l12.98-7.5V0h-2v6.35L0 12.69v2.3zm0 18.5L12.98 41v8h-2v-6.85L0 35.81v-2.3zM15 0v7.5L27.99 15H28v-2.31h-.01L17 6.35V0h-2zm0 49v-7.5L27.99 34H28v2.31h-.01L17 42.65V49h-2z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
        background-size: 100% 100%, 28px 49px;
        pointer-events: none;
        z-index: 0;
        animation: honeycombPulse 8s ease-in-out infinite;
    }

    @keyframes honeycombPulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.85; }
    }

    /* Ensure content is above background */
    .main .block-container {
        position: relative;
        z-index: 1;
    }

    /* Minimal header - keeps sidebar toggle visible */
    header[data-testid="stHeader"] {
        background: transparent !important;
        height: auto !important;
    }

    /* Ensure sidebar toggle button is visible */
    header[data-testid="stHeader"] button[data-testid="baseButton-header"],
    button[kind="header"],
    button[kind="headerNoPadding"] {
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
        position: fixed !important;
        top: 0.5rem !important;
        left: 0.5rem !important;
        z-index: 999999 !important;
    }

    /* Mobile sidebar overlay */
    @media (max-width: 768px) {
        /* Ensure sidebar overlay works properly */
        .stApp[data-testid="stApp"] {
            position: relative;
        }

        /* Sidebar expanded state */
        section[data-testid="stSidebar"][data-testid="stSidebar"][aria-expanded="true"] {
            box-shadow: 0 0 50px rgba(0,0,0,0.8) !important;
        }
    }

    .main {
        background-color: transparent !important;
    }

    /* ========== MAIN CONTENT CONTAINER ========== */
    .block-container {
        padding-top: 1.5rem !important;
        max-width: 1200px !important;
        padding-left: 2.5rem !important;
        padding-right: 2.5rem !important;
    }

    /* ========== SIDEBAR STYLING ========== */
    /* Main sidebar container */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.98) 0%, rgba(5, 8, 22, 0.98) 100%) !important;
        border-right: 1px solid rgba(0, 212, 255, 0.1) !important;
    }

    /* Sidebar navigation items */
    [data-testid="stSidebarNav"] a {
        color: #c8cdd3 !important;
        border-radius: 8px !important;
        transition: all 0.2s ease !important;
    }

    [data-testid="stSidebarNav"] a:hover {
        background: rgba(0, 212, 255, 0.1) !important;
        color: #00d4ff !important;
    }

    [data-testid="stSidebarNav"] a[aria-current="page"] {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.15), rgba(255, 107, 203, 0.1)) !important;
        color: #00d4ff !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
        font-weight: 600 !important;
    }

    /* ========== RESPONSIVE SIDEBAR ========== */
    /* Mobile sidebar improvements */
    @media (max-width: 768px) {
        .block-container {
            padding-left: 1.5rem !important;
            padding-right: 1.5rem !important;
            padding-top: 1rem !important;
        }

        /* Ensure sidebar is accessible on mobile */
        section[data-testid="stSidebar"] {
            min-width: 280px !important;
            max-width: 85vw !important;
        }

        /* Sidebar navigation items - better touch targets */
        [data-testid="stSidebarNav"] a {
            padding: 0.75rem 1rem !important;
            font-size: 0.95rem !important;
        }

        /* Sidebar toggle button visibility */
        button[kind="headerNoPadding"] {
            z-index: 999999 !important;
        }
    }

    @media (max-width: 480px) {
        .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }

        /* Smaller screens - compact sidebar */
        section[data-testid="stSidebar"] {
            min-width: 260px !important;
            max-width: 90vw !important;
        }

        [data-testid="stSidebarNav"] a {
            padding: 0.6rem 0.8rem !important;
            font-size: 0.9rem !important;
        }
    }

    /* Ensure sidebar content is readable */
    [data-testid="stSidebar"] .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
    </style>

    <!-- Falling Particles Container -->
    <div id="particles-container" style="
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 0;
        overflow: hidden;
    "></div>

    <script>
    // Falling Particles System
    (function() {
        const container = document.getElementById('particles-container');
        const particleCount = 25;
        const particles = [];
        const colors = ['#00d4ff', '#ff6bcb', '#34d399', '#fde68a', '#a78bfa'];

        function createParticle() {
            const particle = document.createElement('div');
            const size = Math.random() * 4 + 2;
            const color = colors[Math.floor(Math.random() * colors.length)];
            const startX = Math.random() * window.innerWidth;
            const duration = Math.random() * 10 + 8;
            const delay = Math.random() * 5;

            particle.style.cssText = `
                position: absolute;
                width: ${size}px;
                height: ${size}px;
                background: ${color};
                border-radius: 50%;
                left: ${startX}px;
                top: -10px;
                opacity: ${Math.random() * 0.5 + 0.3};
                box-shadow: 0 0 ${size * 2}px ${color};
                animation: fall ${duration}s linear ${delay}s infinite;
            `;

            container.appendChild(particle);
            particles.push(particle);
        }

        // Add falling animation keyframes
        const style = document.createElement('style');
        style.textContent = `
            @keyframes fall {
                0% {
                    transform: translateY(-10px) rotate(0deg);
                    opacity: 0;
                }
                10% {
                    opacity: 0.6;
                }
                90% {
                    opacity: 0.6;
                }
                100% {
                    transform: translateY(${window.innerHeight + 20}px) rotate(360deg);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);

        // Create initial particles
        for (let i = 0; i < particleCount; i++) {
            setTimeout(() => createParticle(), i * 100);
        }

        // Recreate particles on resize
        window.addEventListener('resize', () => {
            container.innerHTML = '';
            particles.length = 0;
            for (let i = 0; i < particleCount; i++) {
                createParticle();
            }
        });
    })();
    </script>
    """, unsafe_allow_html=True)

    # Additional particles via components for better performance
    components.html("""
    <style>
    .particle-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1;
        overflow: hidden;
    }
    .dot {
        position: absolute;
        width: 3px;
        height: 3px;
        border-radius: 50%;
        opacity: 0.4;
        animation: fallDown linear infinite;
    }
    @keyframes fallDown {
        0% {
            transform: translateY(-10px);
            opacity: 0;
        }
        5% {
            opacity: 0.4;
        }
        95% {
            opacity: 0.4;
        }
        100% {
            transform: translateY(100vh);
            opacity: 0;
        }
    }
    </style>
    <div class="particle-overlay" id="dotParticles"></div>
    <script>
    (function() {
        const overlay = document.getElementById('dotParticles');
        const colors = ['#00d4ff', '#ff6bcb', '#34d399'];

        for (let i = 0; i < 15; i++) {
            const dot = document.createElement('div');
            dot.className = 'dot';
            dot.style.left = Math.random() * 100 + '%';
            dot.style.background = colors[Math.floor(Math.random() * colors.length)];
            dot.style.boxShadow = `0 0 6px ${dot.style.background}`;
            dot.style.animationDuration = (Math.random() * 8 + 6) + 's';
            dot.style.animationDelay = Math.random() * 5 + 's';
            overlay.appendChild(dot);
        }
    })();
    </script>
    """, height=0)

# Keep old function name for backward compatibility during transition
def render_navigation(active_page: str = "home"):
    """Deprecated: Use apply_global_effects() instead."""
    apply_global_effects()