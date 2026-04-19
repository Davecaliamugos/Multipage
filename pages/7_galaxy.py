import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import streamlit.components.v1 as components
from components import apply_global_effects

st.set_page_config(
    page_title="Galaxy Explorer | Dave Campo",
    page_icon="🚀",
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

components.html("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
<title>Galaxy Explorer 3D</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;600&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }

html, body {
    background: #000;
    overflow: hidden;
    font-family: 'Inter', sans-serif;
    color: #fff;
    width: 100%;
    height: 100%;
    position: fixed;
    touch-action: none;
}

#canvas3d {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    z-index: 0;
}

/* ── HUD ── */
#hud {
    position: fixed;
    top: 0; left: 0; right: 0;
    z-index: 100;
    pointer-events: none;
}

.top-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 20px;
    background: linear-gradient(180deg, rgba(0,0,0,0.85) 0%, transparent 100%);
    flex-wrap: nowrap;
    gap: 8px;
}

.mission-title {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.55rem, 2vw, 1rem);
    font-weight: 700;
    color: #00d4ff;
    letter-spacing: 2px;
    text-transform: uppercase;
    text-shadow: 0 0 20px rgba(0,212,255,0.8);
    white-space: nowrap;
}

.top-center {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
    flex: 1;
    min-width: 0;
}

.destination-label {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.45rem, 1.5vw, 0.65rem);
    color: #9ca3af;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.destination-name {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.7rem, 2.5vw, 1.1rem);
    font-weight: 900;
    color: #fff;
    text-shadow: 0 0 30px rgba(255,255,255,0.5);
    transition: all 0.4s ease;
    text-align: center;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 200px;
}

.velocity-box {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.55rem, 1.5vw, 0.75rem);
    color: #34d399;
    text-align: right;
    letter-spacing: 1px;
    white-space: nowrap;
}

.progress-track {
    margin: 0 20px;
    height: 2px;
    background: rgba(255,255,255,0.08);
    border-radius: 2px;
    overflow: visible;
    position: relative;
}

.progress-glow {
    height: 100%;
    background: linear-gradient(90deg, #3b82f6, #8b5cf6, #ec4899, #f59e0b);
    border-radius: 2px;
    transition: width 0.8s cubic-bezier(0.4,0,0.2,1);
    position: relative;
    box-shadow: 0 0 12px rgba(0,212,255,0.6);
}

.progress-dot {
    position: absolute;
    right: -5px;
    top: -4px;
    width: 10px;
    height: 10px;
    background: #fff;
    border-radius: 50%;
    box-shadow: 0 0 10px #00d4ff, 0 0 20px #00d4ff;
}

/* Distance counter */
.distance-hud {
    position: fixed;
    top: 80px;
    left: 20px;
    z-index: 100;
    font-family: 'Orbitron', monospace;
}

.dist-label {
    font-size: clamp(0.45rem, 1.2vw, 0.55rem);
    color: #6b7280;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 2px;
}

.dist-value {
    font-size: clamp(0.9rem, 3vw, 1.4rem);
    font-weight: 700;
    color: #00d4ff;
    text-shadow: 0 0 20px rgba(0,212,255,0.5);
    transition: all 0.5s ease;
}

/* Info Panel */
#infoPanel {
    position: fixed;
    bottom: 110px;
    left: 20px;
    z-index: 100;
    width: min(340px, calc(100vw - 60px));
    background: rgba(5,10,25,0.92);
    border: 1px solid rgba(0,212,255,0.2);
    border-left: 3px solid #00d4ff;
    border-radius: 0 12px 12px 0;
    padding: 16px 18px;
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    transform: translateX(-120%);
    transition: transform 0.6s cubic-bezier(0.4,0,0.2,1);
    pointer-events: none;
}

#infoPanel.visible {
    transform: translateX(0);
}

.info-category {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.45rem, 1.3vw, 0.55rem);
    color: #00d4ff;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 6px;
}

.info-title {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.9rem, 3vw, 1.3rem);
    font-weight: 900;
    color: #fff;
    margin-bottom: 8px;
    line-height: 1.2;
}

.info-desc {
    font-size: clamp(0.72rem, 2vw, 0.82rem);
    color: #9ca3af;
    line-height: 1.6;
    margin-bottom: 12px;
}

.stats-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
}

.stat-item {
    background: rgba(0,212,255,0.07);
    border: 1px solid rgba(0,212,255,0.15);
    border-radius: 6px;
    padding: 6px 8px;
}

.stat-val {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.65rem, 2vw, 0.85rem);
    font-weight: 700;
    color: #00d4ff;
}

.stat-lbl {
    font-size: clamp(0.55rem, 1.5vw, 0.65rem);
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 2px;
}

/* Nav Controls */
#navControls {
    position: fixed;
    bottom: 24px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 200;
    display: flex;
    align-items: center;
    gap: 12px;
}

.nav-btn {
    padding: clamp(10px, 2.5vw, 12px) clamp(18px, 4vw, 32px);
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.6rem, 1.8vw, 0.75rem);
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #fff;
    background: rgba(5,10,25,0.9);
    border: 1px solid rgba(0,212,255,0.4);
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.3s;
    position: relative;
    overflow: hidden;
    -webkit-tap-highlight-color: transparent;
    touch-action: manipulation;
    user-select: none;
    -webkit-user-select: none;
    white-space: nowrap;
}

.nav-btn::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(0,212,255,0.15), transparent);
    opacity: 0;
    transition: opacity 0.3s;
}

.nav-btn:hover::before,
.nav-btn:active::before { opacity: 1; }

.nav-btn:hover,
.nav-btn:active {
    border-color: #00d4ff;
    box-shadow: 0 0 20px rgba(0,212,255,0.3), inset 0 0 20px rgba(0,212,255,0.05);
    transform: translateY(-2px);
}

.nav-btn:disabled {
    opacity: 0.3;
    cursor: not-allowed;
    transform: none;
    pointer-events: none;
}

.nav-btn.primary {
    background: linear-gradient(135deg, rgba(0,212,255,0.2), rgba(139,92,246,0.2));
    border-color: #00d4ff;
    box-shadow: 0 0 20px rgba(0,212,255,0.2);
}

.step-counter {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.55rem, 1.5vw, 0.7rem);
    color: #9ca3af;
    letter-spacing: 2px;
    min-width: 60px;
    text-align: center;
}

/* Swipe hint for mobile */
#swipeHint {
    position: fixed;
    bottom: 80px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 200;
    font-family: 'Orbitron', monospace;
    font-size: 0.55rem;
    letter-spacing: 2px;
    color: rgba(0,212,255,0.4);
    text-transform: uppercase;
    display: none;
    animation: swipePulse 2s ease-in-out infinite;
    white-space: nowrap;
}

@keyframes swipePulse {
    0%,100% { opacity: 0.3; }
    50% { opacity: 0.8; }
}

/* Minimap */
#minimap {
    position: fixed;
    right: 18px;
    top: 50%;
    transform: translateY(-50%);
    z-index: 100;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0;
}

.minimap-line {
    width: 1px;
    height: 22px;
    background: rgba(255,255,255,0.1);
}

.minimap-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: rgba(255,255,255,0.2);
    border: 1px solid rgba(255,255,255,0.15);
    cursor: pointer;
    transition: all 0.3s;
    position: relative;
    touch-action: manipulation;
}

.minimap-dot.active {
    background: #00d4ff;
    border-color: #00d4ff;
    box-shadow: 0 0 10px #00d4ff;
    transform: scale(1.5);
}

.minimap-dot.visited {
    background: rgba(0,212,255,0.4);
    border-color: rgba(0,212,255,0.4);
}

.minimap-dot:hover::after,
.minimap-dot:focus::after {
    content: attr(data-name);
    position: absolute;
    right: 16px;
    top: 50%;
    transform: translateY(-50%);
    font-family: 'Orbitron', monospace;
    font-size: 0.6rem;
    color: #fff;
    white-space: nowrap;
    background: rgba(0,0,0,0.8);
    padding: 3px 8px;
    border-radius: 3px;
    pointer-events: none;
}

/* Landing screen */
#landing {
    position: fixed;
    inset: 0;
    z-index: 500;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: radial-gradient(ellipse at center, rgba(0,20,40,0.95) 0%, rgba(0,0,0,0.98) 100%);
    transition: opacity 0.8s ease, visibility 0.8s;
    padding: 20px;
}

#landing.hidden {
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
}

.landing-badge {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.5rem, 1.5vw, 0.6rem);
    letter-spacing: 4px;
    color: #00d4ff;
    text-transform: uppercase;
    margin-bottom: 24px;
    opacity: 0.8;
    text-align: center;
}

.landing-title {
    font-family: 'Orbitron', monospace;
    font-size: clamp(2rem, 8vw, 4.5rem);
    font-weight: 900;
    text-align: center;
    line-height: 1.1;
    margin-bottom: 16px;
    background: linear-gradient(135deg, #fff 0%, #00d4ff 40%, #8b5cf6 70%, #ff6bcb 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.landing-sub {
    font-size: clamp(0.8rem, 2.5vw, 1rem);
    color: #6b7280;
    text-align: center;
    max-width: 480px;
    line-height: 1.6;
    margin-bottom: 40px;
}

.launch-btn {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.7rem, 2vw, 0.85rem);
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #000;
    background: linear-gradient(135deg, #00d4ff, #8b5cf6);
    border: none;
    padding: clamp(12px, 3vw, 16px) clamp(30px, 7vw, 50px);
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.3s;
    position: relative;
    overflow: hidden;
    touch-action: manipulation;
    -webkit-tap-highlight-color: transparent;
}

.launch-btn::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.2), transparent);
    opacity: 0;
    transition: opacity 0.3s;
}

.launch-btn:hover, .launch-btn:active {
    transform: scale(1.05);
    box-shadow: 0 0 40px rgba(0,212,255,0.5), 0 0 80px rgba(139,92,246,0.3);
}

.launch-btn:hover::after,
.launch-btn:active::after { opacity: 1; }

.scroll-hint {
    position: absolute;
    bottom: 32px;
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.5rem, 1.3vw, 0.6rem);
    letter-spacing: 2px;
    color: #374151;
    text-transform: uppercase;
    animation: pulse 2s ease-in-out infinite;
    text-align: center;
    padding: 0 20px;
}

@keyframes pulse {
    0%,100% { opacity: 0.4; }
    50% { opacity: 1; }
}

/* Completion */
#completion {
    position: fixed;
    inset: 0;
    z-index: 500;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: radial-gradient(ellipse at center, rgba(0,10,30,0.97) 0%, rgba(0,0,0,0.99) 100%);
    opacity: 0;
    visibility: hidden;
    transition: all 0.8s ease;
    padding: 20px;
}

#completion.visible {
    opacity: 1;
    visibility: visible;
}

.complete-label {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.5rem, 1.5vw, 0.6rem);
    letter-spacing: 6px;
    color: #34d399;
    text-transform: uppercase;
    margin-bottom: 16px;
    text-align: center;
}

.complete-title {
    font-family: 'Orbitron', monospace;
    font-size: clamp(1.5rem, 5vw, 3.5rem);
    font-weight: 900;
    text-align: center;
    margin-bottom: 14px;
    background: linear-gradient(135deg, #34d399, #00d4ff, #8b5cf6, #ff6bcb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.complete-dist {
    font-family: 'Orbitron', monospace;
    font-size: clamp(1.2rem, 4vw, 2rem);
    font-weight: 900;
    color: #00d4ff;
    text-shadow: 0 0 30px rgba(0,212,255,0.5);
    margin-bottom: 10px;
    text-align: center;
}

.complete-text {
    font-size: clamp(0.75rem, 2vw, 0.9rem);
    color: #6b7280;
    text-align: center;
    max-width: 500px;
    line-height: 1.8;
    margin-bottom: 36px;
}

.restart-btn {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.65rem, 2vw, 0.75rem);
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #fff;
    background: transparent;
    border: 1px solid rgba(0,212,255,0.5);
    padding: clamp(10px, 2.5vw, 14px) clamp(24px, 6vw, 40px);
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.3s;
    touch-action: manipulation;
}

.restart-btn:hover, .restart-btn:active {
    background: rgba(0,212,255,0.1);
    border-color: #00d4ff;
    box-shadow: 0 0 20px rgba(0,212,255,0.3);
}

/* Warp effect */
#warpOverlay {
    position: fixed;
    inset: 0;
    z-index: 300;
    pointer-events: none;
    opacity: 0;
    background: radial-gradient(ellipse at center, transparent 0%, transparent 30%, rgba(0,212,255,0.05) 60%, rgba(0,0,0,0.3) 100%);
    transition: opacity 0.3s;
}

#warpOverlay.active { opacity: 1; }

/* Particle burst overlay */
#particleCanvas {
    position: fixed;
    inset: 0;
    z-index: 50;
    pointer-events: none;
}

/* Scan lines */
.scanlines {
    position: fixed;
    inset: 0;
    z-index: 50;
    background: repeating-linear-gradient(
        0deg,
        transparent,
        transparent 2px,
        rgba(0,0,0,0.03) 2px,
        rgba(0,0,0,0.03) 4px
    );
    pointer-events: none;
}

/* Corner decorations */
.corner {
    position: fixed;
    z-index: 100;
    width: 32px;
    height: 32px;
    pointer-events: none;
}
.corner-tl { top: 10px; left: 10px; border-top: 1px solid rgba(0,212,255,0.4); border-left: 1px solid rgba(0,212,255,0.4); }
.corner-tr { top: 10px; right: 10px; border-top: 1px solid rgba(0,212,255,0.4); border-right: 1px solid rgba(0,212,255,0.4); }
.corner-bl { bottom: 10px; left: 10px; border-bottom: 1px solid rgba(0,212,255,0.4); border-left: 1px solid rgba(0,212,255,0.4); }
.corner-br { bottom: 10px; right: 10px; border-bottom: 1px solid rgba(0,212,255,0.4); border-right: 1px solid rgba(0,212,255,0.4); }

/* Motion: floating particles */
@keyframes floatUp {
    0%   { transform: translateY(0) scale(1); opacity: 0.7; }
    100% { transform: translateY(-120px) scale(0); opacity: 0; }
}

/* Gyro indicator */
#gyroIndicator {
    position: fixed;
    top: 80px;
    right: 18px;
    z-index: 100;
    font-family: 'Orbitron', monospace;
    font-size: 0.5rem;
    color: rgba(0,212,255,0.5);
    letter-spacing: 1px;
    display: none;
    text-align: center;
}

/* Object name pop */
@keyframes namePop {
    0%   { opacity: 0; transform: translateY(10px) scale(0.9); }
    20%  { opacity: 1; transform: translateY(0) scale(1); }
    80%  { opacity: 1; }
    100% { opacity: 0; }
}

.name-pop {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 250;
    font-family: 'Orbitron', monospace;
    font-size: clamp(1.5rem, 5vw, 3rem);
    font-weight: 900;
    color: #fff;
    text-shadow: 0 0 40px rgba(0,212,255,0.8), 0 0 80px rgba(139,92,246,0.5);
    pointer-events: none;
    animation: namePop 2s ease forwards;
    white-space: nowrap;
}

/* Ripple on tap */
.tap-ripple {
    position: fixed;
    border-radius: 50%;
    background: rgba(0,212,255,0.3);
    pointer-events: none;
    z-index: 400;
    animation: rippleOut 0.6s ease forwards;
}

@keyframes rippleOut {
    0%   { width: 0; height: 0; opacity: 0.8; margin: 0; }
    100% { width: 80px; height: 80px; opacity: 0; margin: -40px; }
}
</style>
</head>
<body>

<canvas id="canvas3d"></canvas>
<canvas id="particleCanvas"></canvas>
<div class="scanlines"></div>
<div class="corner corner-tl"></div>
<div class="corner corner-tr"></div>
<div class="corner corner-bl"></div>
<div class="corner corner-br"></div>
<div id="warpOverlay"></div>

<!-- HUD -->
<div id="hud">
    <div class="top-bar">
        <div class="mission-title">GALAXY EXPLORER</div>
        <div class="top-center">
            <div class="destination-label">Current Destination</div>
            <div class="destination-name" id="destName">— AWAITING LAUNCH —</div>
        </div>
        <div class="velocity-box">
            <div style="font-size:clamp(0.45rem,1.2vw,0.55rem);color:#6b7280;letter-spacing:2px;margin-bottom:2px;">VELOCITY</div>
            <div id="velocityVal">0 c</div>
        </div>
    </div>
    <div class="progress-track">
        <div class="progress-glow" id="progressBar" style="width:0%">
            <div class="progress-dot"></div>
        </div>
    </div>
</div>

<div class="distance-hud">
    <div class="dist-label">Distance Traveled</div>
    <div class="dist-value" id="distValue">0 ly</div>
</div>

<div id="gyroIndicator">GYRO<br>ACTIVE</div>

<!-- Info Panel -->
<div id="infoPanel">
    <div class="info-category" id="infoCategory">SOLAR SYSTEM</div>
    <div class="info-title" id="infoTitle">Earth</div>
    <div class="info-desc" id="infoDesc">Our pale blue dot.</div>
    <div class="stats-row" id="statsRow"></div>
</div>

<!-- Minimap -->
<div id="minimap"></div>

<!-- Swipe hint -->
<div id="swipeHint">← SWIPE TO NAVIGATE →</div>

<!-- Nav -->
<div id="navControls" style="display:none;">
    <button class="nav-btn" id="prevBtn" onclick="prevDest()" disabled>◀ PREV</button>
    <div class="step-counter" id="stepCounter">0 / 15</div>
    <button class="nav-btn primary" id="nextBtn" onclick="nextDest()">NEXT ▶</button>
</div>

<!-- Landing -->
<div id="landing">
    <div class="landing-badge">Deep Space Mission — 2025</div>
    <h1 class="landing-title">GALAXY<br>EXPLORER</h1>
    <p class="landing-sub">A 3D journey from Earth to the edge of the observable universe. 46.5 billion light-years of cosmic wonder await.</p>
    <button class="launch-btn" onclick="launchMission()">INITIATE LAUNCH</button>
    <div class="scroll-hint">↑ Swipe, arrow keys, or buttons to navigate ↑</div>
</div>

<!-- Completion -->
<div id="completion">
    <div class="complete-label">Mission Complete</div>
    <div class="complete-title">EDGE OF THE<br>UNIVERSE REACHED</div>
    <div class="complete-dist">46.5 Billion Light-Years</div>
    <p class="complete-text">
        You have traversed the full breadth of the observable universe — from Earth through our solar system,
        past distant stars, neighboring galaxies, and beyond to the cosmic horizon.
        The universe is 13.8 billion years old and still expanding.
    </p>
    <button class="restart-btn" onclick="restartMission()">RESTART MISSION</button>
</div>

<!-- Three.js -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

<script>
// ═══════════════════════════════════════
//  DESTINATION DATA
// ═══════════════════════════════════════
const DESTINATIONS = [
    {
        name: "Earth", category: "SOLAR SYSTEM — INNER",
        desc: "Our pale blue dot — the only known harbor of life in the cosmos. Oceans cover 71% of its surface, and a fragile atmosphere protects all life beneath it.",
        distance: 0,
        color: 0x1d6fa4, emissive: 0x0a2a40,
        type: "earth",
        stats: [
            { v: "12,742 km", l: "Diameter" }, { v: "1 AU", l: "From Sun" },
            { v: "4.5B yrs", l: "Age" },       { v: "7.9B", l: "Population" }
        ]
    },
    {
        name: "The Moon", category: "EARTH SYSTEM",
        desc: "Earth's ancient companion, shaping tides and seasons. Humanity's first foothold in space — 384,400 km from home.",
        distance: 0.0000016,
        color: 0x9ca3af, emissive: 0x1a1a1a,
        type: "moon",
        stats: [
            { v: "3,474 km", l: "Diameter" },   { v: "27.3 days", l: "Orbit" },
            { v: "-173°C", l: "Min Temp" },      { v: "127°C", l: "Max Temp" }
        ]
    },
    {
        name: "Mars", category: "SOLAR SYSTEM — INNER",
        desc: "The Red Planet, humanity's next frontier. Ancient riverbeds suggest it once held liquid water. Olympus Mons rises 22km — the tallest volcano in the solar system.",
        distance: 0.000042,
        color: 0xc1440e, emissive: 0x3d1005,
        type: "mars",
        stats: [
            { v: "6,779 km", l: "Diameter" },  { v: "1.5 AU", l: "From Sun" },
            { v: "687 days", l: "Year" },       { v: "-80°C", l: "Avg Temp" }
        ]
    },
    {
        name: "Asteroid Belt", category: "SOLAR SYSTEM — MID",
        desc: "Millions of rocky remnants between Mars and Jupiter, relics from the solar system's formation 4.6 billion years ago. Ceres, a dwarf planet, reigns here.",
        distance: 0.00025,
        color: 0x7c6a5a, emissive: 0x1a1208,
        type: "asteroids",
        stats: [
            { v: "1M+", l: "Asteroids" },   { v: "Ceres", l: "Largest" },
            { v: "2.2-3.2 AU", l: "Range" }, { v: "4.6B yrs", l: "Age" }
        ]
    },
    {
        name: "Jupiter", category: "SOLAR SYSTEM — OUTER",
        desc: "The colossus of our solar system. Its Great Red Spot — a storm larger than Earth — has raged for over 350 years. 95 known moons orbit its immense gravity well.",
        distance: 0.00052,
        color: 0xc88b3a, emissive: 0x3d2200,
        type: "jupiter",
        stats: [
            { v: "139,820 km", l: "Diameter" }, { v: "5.2 AU", l: "From Sun" },
            { v: "95 moons", l: "Satellites" },  { v: "11.9 yrs", l: "Year" }
        ]
    },
    {
        name: "Saturn", category: "SOLAR SYSTEM — OUTER",
        desc: "The ringed jewel of the solar system. Its iconic rings span 282,000 km yet are barely 10 meters thick — mostly ice and rock orbiting in perfect harmony.",
        distance: 0.0010,
        color: 0xe8c97a, emissive: 0x3d2e00,
        type: "saturn",
        stats: [
            { v: "116,460 km", l: "Diameter" }, { v: "9.5 AU", l: "From Sun" },
            { v: "146 moons", l: "Satellites" }, { v: "0.687", l: "Density (g/cm³)" }
        ]
    },
    {
        name: "Uranus", category: "SOLAR SYSTEM — OUTER",
        desc: "The tilted ice giant, rotating on its side at 98°. Its methane atmosphere absorbs red light, rendering it a haunting cyan-blue. Discovered in 1781 by Herschel.",
        distance: 0.0019,
        color: 0x4fd1c5, emissive: 0x0a2a28,
        type: "uranus",
        stats: [
            { v: "50,724 km", l: "Diameter" }, { v: "19.2 AU", l: "From Sun" },
            { v: "98°", l: "Axial Tilt" },    { v: "-224°C", l: "Avg Temp" }
        ]
    },
    {
        name: "Neptune", category: "SOLAR SYSTEM — OUTER",
        desc: "The windiest world in the solar system. Supersonic gales reach 2,100 km/h. Its moon Triton orbits backwards and is slowly spiraling inward to its doom.",
        distance: 0.0030,
        color: 0x2b4eff, emissive: 0x050a3d,
        type: "neptune",
        stats: [
            { v: "49,244 km", l: "Diameter" }, { v: "30.1 AU", l: "From Sun" },
            { v: "2,100 km/h", l: "Winds" },   { v: "-214°C", l: "Avg Temp" }
        ]
    },
    {
        name: "Kuiper Belt", category: "TRANS-NEPTUNIAN REGION",
        desc: "A vast disc of icy debris beyond Neptune, stretching from 30 to 55 AU. Pluto resides here among thousands of frozen worlds. The origin of short-period comets.",
        distance: 0.005,
        color: 0x7c5caf, emissive: 0x150a2a,
        type: "kuiper",
        stats: [
            { v: "100K+", l: "Objects" },   { v: "Pluto", l: "Most Famous" },
            { v: "30-55 AU", l: "Range" },  { v: "-240°C", l: "Avg Temp" }
        ]
    },
    {
        name: "Oort Cloud", category: "SOLAR SYSTEM BOUNDARY",
        desc: "A theoretical spherical shell of icy bodies enveloping the solar system at up to 100,000 AU. The source of long-period comets — some taking millions of years to orbit.",
        distance: 0.5,
        color: 0xa0c4ff, emissive: 0x05102a,
        type: "oort",
        stats: [
            { v: "1-2 ly", l: "Thickness" },    { v: "Trillions", l: "Icy Bodies" },
            { v: "100,000 AU", l: "Max Dist" }, { v: "-270°C", l: "Temp" }
        ]
    },
    {
        name: "Proxima Centauri", category: "INTERSTELLAR SPACE",
        desc: "The nearest star to our Sun — a red dwarf 4.24 light-years away. Its planet Proxima b sits in the habitable zone, though intense stellar flares may threaten life.",
        distance: 4.24,
        color: 0xff6b35, emissive: 0x3d1500,
        type: "star",
        stats: [
            { v: "Red Dwarf", l: "Type" },   { v: "4.24 ly", l: "Distance" },
            { v: "Proxima b", l: "Exoplanet" }, { v: "2,700°C", l: "Surface" }
        ]
    },
    {
        name: "Galactic Center", category: "MILKY WAY",
        desc: "Sagittarius A* — a supermassive black hole 4 million times the mass of our Sun — anchors the Milky Way. Dense star clusters orbit within light-years of this gravitational titan.",
        distance: 26000,
        color: 0xffd700, emissive: 0x3d2800,
        type: "galaxy_core",
        stats: [
            { v: "4M × Sun", l: "BH Mass" },  { v: "26,000 ly", l: "Distance" },
            { v: "200-400B", l: "Stars" },     { v: "100,000 ly", l: "Diameter" }
        ]
    },
    {
        name: "Andromeda Galaxy", category: "LOCAL GROUP",
        desc: "Our nearest galactic neighbor — 2.5 million light-years away — containing over 1 trillion stars. It's approaching us at 110 km/s and will collide with the Milky Way in 4.5 billion years.",
        distance: 2537000,
        color: 0xc8b8ff, emissive: 0x100a3d,
        type: "galaxy",
        stats: [
            { v: "1 trillion", l: "Stars" },   { v: "2.5M ly", l: "Distance" },
            { v: "220,000 ly", l: "Diameter" }, { v: "110 km/s", l: "Approach" }
        ]
    },
    {
        name: "TON 618", category: "DEEP UNIVERSE",
        desc: "One of the most massive black holes ever discovered — 66 billion solar masses. Its accretion disk outshines entire galaxies. Located 10.4 billion light-years from Earth.",
        distance: 55000000,
        color: 0x1a0a2e, emissive: 0x4a0080,
        type: "blackhole",
        stats: [
            { v: "66B × Sun", l: "Mass" },      { v: "10.4B ly", l: "Distance" },
            { v: "1,300 AU", l: "Radius" },     { v: "140T × Sun", l: "Luminosity" }
        ]
    },
    {
        name: "Edge of Universe", category: "COSMIC HORIZON",
        desc: "The observable universe's boundary — 46.5 billion light-years from Earth. This is the farthest light that has reached us since the Big Bang, 13.8 billion years ago. Beyond: the unknown.",
        distance: 46500000000,
        color: 0xff00ff, emissive: 0x2a0040,
        type: "universe_edge",
        stats: [
            { v: "46.5B ly", l: "Radius" },     { v: "93B ly", l: "Diameter" },
            { v: "2 Trillion", l: "Galaxies" }, { v: "∞", l: "Beyond" }
        ]
    }
];

// ═══════════════════════════════════════
//  THREE.JS SETUP
// ═══════════════════════════════════════
const canvas = document.getElementById('canvas3d');
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 0.8;

const scene = new THREE.Scene();
scene.fog = new THREE.FogExp2(0x000005, 0.008);

const camera = new THREE.PerspectiveCamera(65, window.innerWidth / window.innerHeight, 0.01, 10000);
camera.position.set(0, 2, 8);
camera.lookAt(0, 0, 0);

// ── Lighting ──
const ambientLight = new THREE.AmbientLight(0x111122, 0.5);
scene.add(ambientLight);
const sunLight = new THREE.PointLight(0xfff4e0, 3, 100);
sunLight.position.set(10, 10, 10);
scene.add(sunLight);
const rimLight = new THREE.DirectionalLight(0x0044ff, 0.3);
rimLight.position.set(-5, 3, -5);
scene.add(rimLight);

// ── Starfield ──
function createStarfield() {
    const geometry = new THREE.BufferGeometry();
    const count = 12000;
    const positions = new Float32Array(count * 3);
    const sizes = new Float32Array(count);
    const colors = new Float32Array(count * 3);
    for (let i = 0; i < count; i++) {
        const theta = Math.random() * Math.PI * 2;
        const phi = Math.acos(2 * Math.random() - 1);
        const r = 200 + Math.random() * 800;
        positions[i*3]   = r * Math.sin(phi) * Math.cos(theta);
        positions[i*3+1] = r * Math.sin(phi) * Math.sin(theta);
        positions[i*3+2] = r * Math.cos(phi);
        sizes[i] = Math.random() * 2.5 + 0.5;
        const t = Math.random();
        if (t < 0.6)      { colors[i*3]=1;   colors[i*3+1]=1;   colors[i*3+2]=1;   }
        else if (t < 0.75){ colors[i*3]=0.6; colors[i*3+1]=0.7; colors[i*3+2]=1;   }
        else if (t < 0.9) { colors[i*3]=1;   colors[i*3+1]=0.8; colors[i*3+2]=0.6; }
        else               { colors[i*3]=1;   colors[i*3+1]=0.4; colors[i*3+2]=0.4; }
    }
    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    geometry.setAttribute('size',     new THREE.BufferAttribute(sizes, 1));
    geometry.setAttribute('color',    new THREE.BufferAttribute(colors, 3));
    const mat = new THREE.PointsMaterial({
        size: 0.8, sizeAttenuation: true, vertexColors: true,
        transparent: true, opacity: 0.9
    });
    return new THREE.Points(geometry, mat);
}
const starfield = createStarfield();
scene.add(starfield);

// Nebula clouds
function createNebula(pos, color, scale) {
    const group = new THREE.Group();
    for (let i = 0; i < 80; i++) {
        const geo = new THREE.SphereGeometry(Math.random()*4+1, 6, 6);
        const mat = new THREE.MeshBasicMaterial({
            color, transparent: true,
            opacity: Math.random()*0.04+0.01,
            side: THREE.BackSide
        });
        const mesh = new THREE.Mesh(geo, mat);
        mesh.position.set(
            (Math.random()-0.5)*30*scale,
            (Math.random()-0.5)*15*scale,
            (Math.random()-0.5)*20*scale
        );
        group.add(mesh);
    }
    group.position.copy(pos);
    return group;
}
scene.add(createNebula(new THREE.Vector3(-40,5,-80),   0x4466ff, 1.5));
scene.add(createNebula(new THREE.Vector3(50,-10,-120), 0xff4488, 2));
scene.add(createNebula(new THREE.Vector3(-60,15,-200), 0x8844ff, 1.8));

// ── Planet builders (unchanged from original) ──
function addAtmosphere(planet, color) {
    const geo = new THREE.SphereGeometry(planet.geometry.parameters.radius*1.12,32,32);
    const mat = new THREE.MeshPhongMaterial({ color, transparent:true, opacity:0.15, side:THREE.BackSide });
    planet.add(new THREE.Mesh(geo,mat));
}
function addRings(group, innerR, outerR, color) {
    const geo = new THREE.RingGeometry(innerR,outerR,80);
    const pos=geo.attributes.position, uv=geo.attributes.uv;
    for(let i=0;i<pos.count;i++){
        const v=new THREE.Vector3().fromBufferAttribute(pos,i);
        const t=(v.length()-innerR)/(outerR-innerR);
        uv.setXY(i,t,0);
    }
    const mat=new THREE.MeshBasicMaterial({color,side:THREE.DoubleSide,transparent:true,opacity:0.55});
    const ring=new THREE.Mesh(geo,mat); ring.rotation.x=-Math.PI/2.8; group.add(ring);
    const geo2=new THREE.RingGeometry(outerR+0.3,outerR+1.2,80);
    const mat2=new THREE.MeshBasicMaterial({color:0xfde68a,side:THREE.DoubleSide,transparent:true,opacity:0.2});
    const ring2=new THREE.Mesh(geo2,mat2); ring2.rotation.x=-Math.PI/2.8; group.add(ring2);
}
function addGlow(group,radius,color,intensity=0.4){
    const geo=new THREE.SphereGeometry(radius*1.6,16,16);
    const mat=new THREE.MeshBasicMaterial({color,transparent:true,opacity:intensity,side:THREE.BackSide});
    group.add(new THREE.Mesh(geo,mat));
}

function makePlanet(d) {
    const group = new THREE.Group();
    if (d.type==="earth") {
        const r=1.8;
        const mesh=new THREE.Mesh(new THREE.SphereGeometry(r,64,64),
            new THREE.MeshPhongMaterial({color:0x1565c0,emissive:0x0a1628,shininess:80,specular:0x4488ff}));
        group.add(mesh);
        const land=new THREE.Mesh(new THREE.SphereGeometry(r+0.01,64,64),
            new THREE.MeshPhongMaterial({color:0x2d7d32,emissive:0x0a1f0a,shininess:10,transparent:true,opacity:0.7}));
        group.add(land);
        const clouds=new THREE.Mesh(new THREE.SphereGeometry(r+0.08,32,32),
            new THREE.MeshPhongMaterial({color:0xffffff,transparent:true,opacity:0.25,shininess:0}));
        clouds.userData.rotSpeed=0.0003; group.add(clouds);
        addAtmosphere(mesh,0x4488ff); addGlow(group,r,0x1144ff,0.15);
    } else if (d.type==="moon") {
        const r=0.9;
        group.add(new THREE.Mesh(new THREE.SphereGeometry(r,32,32),
            new THREE.MeshPhongMaterial({color:0x9e9e9e,emissive:0x1a1a1a,shininess:5})));
        for(let i=0;i<8;i++){
            const cGeo=new THREE.CircleGeometry(Math.random()*0.12+0.04,12);
            const crater=new THREE.Mesh(cGeo,new THREE.MeshBasicMaterial({color:0x757575,transparent:true,opacity:0.6}));
            const theta=Math.random()*Math.PI*2, phi=Math.random()*Math.PI;
            crater.position.set(r*Math.sin(phi)*Math.cos(theta),r*Math.sin(phi)*Math.sin(theta),r*Math.cos(phi));
            crater.lookAt(0,0,0); group.add(crater);
        }
    } else if (d.type==="mars") {
        const r=1.2;
        const mesh=new THREE.Mesh(new THREE.SphereGeometry(r,48,48),
            new THREE.MeshPhongMaterial({color:0xc1440e,emissive:0x2d0a02,shininess:15}));
        group.add(mesh);
        const cap=new THREE.Mesh(new THREE.SphereGeometry(r*0.25,16,16,0,Math.PI*2,0,0.4),
            new THREE.MeshBasicMaterial({color:0xdde8f0,transparent:true,opacity:0.85}));
        cap.position.y=r*0.85; group.add(cap);
        group.add(new THREE.Mesh(new THREE.SphereGeometry(r+0.02,16,16),
            new THREE.MeshBasicMaterial({color:0xd4824a,transparent:true,opacity:0.1})));
        addAtmosphere(mesh,0xd4824a);
    } else if (d.type==="asteroids") {
        for(let i=0;i<120;i++){
            const size=Math.random()*0.18+0.04;
            const mesh=new THREE.Mesh(new THREE.DodecahedronGeometry(size,0),
                new THREE.MeshPhongMaterial({color:0x6d5a4a,emissive:0x0d0905,shininess:5}));
            const angle=(i/120)*Math.PI*2, spread=(Math.random()-0.5)*3, r=3.5+spread;
            mesh.position.set(Math.cos(angle)*r,(Math.random()-0.5)*0.8,Math.sin(angle)*r);
            mesh.rotation.set(Math.random()*Math.PI,Math.random()*Math.PI,0);
            mesh.userData.orbitSpeed=(Math.random()*0.0003+0.0001)*(Math.random()<0.5?1:-1);
            mesh.userData.orbitAngle=angle; mesh.userData.orbitR=r;
            group.add(mesh);
        }
        group.add(new THREE.Mesh(new THREE.SphereGeometry(0.4,16,16),
            new THREE.MeshPhongMaterial({color:0x9e8c7a,emissive:0x1a1510})));
    } else if (d.type==="jupiter") {
        const r=2.5;
        group.add(new THREE.Mesh(new THREE.SphereGeometry(r,64,64),
            new THREE.MeshPhongMaterial({color:0xc9a05a,emissive:0x2a1800,shininess:20})));
        const bColors=[0xd4a860,0xc87840,0xe8c890,0xb86828];
        for(let i=0;i<8;i++){
            const band=new THREE.Mesh(new THREE.TorusGeometry(r,0.12,8,64),
                new THREE.MeshBasicMaterial({color:bColors[i%bColors.length],transparent:true,opacity:0.6}));
            band.rotation.x=Math.PI/2; band.position.y=(i-3.5)*0.55; group.add(band);
        }
        addGlow(group,r,0xff9933,0.08);
    } else if (d.type==="saturn") {
        const r=2.2;
        group.add(new THREE.Mesh(new THREE.SphereGeometry(r,64,64),
            new THREE.MeshPhongMaterial({color:0xe8d08a,emissive:0x2a1e00,shininess:25})));
        addRings(group,r*1.25,r*1.9,0xd4b870);
        addRings(group,r*1.95,r*2.4,0xc8a860);
        for(let i=0;i<5;i++){
            const band=new THREE.Mesh(new THREE.TorusGeometry(r,0.1,8,64),
                new THREE.MeshBasicMaterial({color:0xd4a850,transparent:true,opacity:0.4}));
            band.rotation.x=Math.PI/2; band.position.y=(i-2)*0.7; group.add(band);
        }
    } else if (d.type==="uranus") {
        const r=1.8;
        const mesh=new THREE.Mesh(new THREE.SphereGeometry(r,48,48),
            new THREE.MeshPhongMaterial({color:0x4fd1c5,emissive:0x052220,shininess:60,specular:0x88ffff}));
        group.add(mesh);
        const rings=new THREE.Mesh(new THREE.RingGeometry(r*1.3,r*1.7,64),
            new THREE.MeshBasicMaterial({color:0x88cccc,side:THREE.DoubleSide,transparent:true,opacity:0.35}));
        rings.rotation.z=Math.PI/2; group.add(rings);
        addAtmosphere(mesh,0x00cccc); addGlow(group,r,0x00ccff,0.12);
    } else if (d.type==="neptune") {
        const r=1.7;
        const mesh=new THREE.Mesh(new THREE.SphereGeometry(r,48,48),
            new THREE.MeshPhongMaterial({color:0x2b4cff,emissive:0x020830,shininess:70,specular:0x4466ff}));
        group.add(mesh);
        addAtmosphere(mesh,0x2255ff); addGlow(group,r,0x3355ff,0.15);
    } else if (d.type==="kuiper") {
        for(let i=0;i<150;i++){
            const size=Math.random()*0.12+0.02;
            const mesh=new THREE.Mesh(new THREE.SphereGeometry(size,6,6),
                new THREE.MeshPhongMaterial({color:0x7a6aaf,emissive:0x100820,shininess:30,specular:0x6688bb}));
            const angle=Math.random()*Math.PI*2, r=4+Math.random()*3, y=(Math.random()-0.5)*2;
            mesh.position.set(Math.cos(angle)*r,y,Math.sin(angle)*r);
            mesh.userData.orbitSpeed=Math.random()*0.0002+0.00005;
            mesh.userData.orbitAngle=angle; mesh.userData.orbitR=r; mesh.userData.orbitY=y;
            group.add(mesh);
        }
        const pluto=new THREE.Mesh(new THREE.SphereGeometry(0.35,16,16),
            new THREE.MeshPhongMaterial({color:0xb09070,emissive:0x1a1208}));
        pluto.position.set(3,0,0); group.add(pluto);
    } else if (d.type==="oort") {
        for(let i=0;i<300;i++){
            const theta=Math.random()*Math.PI*2, phi=Math.acos(2*Math.random()-1), r=5+Math.random()*3;
            const mesh=new THREE.Mesh(new THREE.SphereGeometry(0.03+Math.random()*0.06,4,4),
                new THREE.MeshBasicMaterial({color:0xa0c4ff,transparent:true,opacity:0.6+Math.random()*0.4}));
            mesh.position.set(r*Math.sin(phi)*Math.cos(theta),r*Math.sin(phi)*Math.sin(theta),r*Math.cos(phi));
            group.add(mesh);
        }
        group.add(new THREE.Mesh(new THREE.SphereGeometry(6.5,24,24),
            new THREE.MeshBasicMaterial({color:0x8aacdd,wireframe:true,transparent:true,opacity:0.04})));
    } else if (d.type==="star") {
        const r=1.4;
        group.add(new THREE.Mesh(new THREE.SphereGeometry(r,48,48),
            new THREE.MeshBasicMaterial({color:0xff6020})));
        for(let i=0;i<4;i++){
            group.add(new THREE.Mesh(new THREE.SphereGeometry(r*(1.3+i*0.4),16,16),
                new THREE.MeshBasicMaterial({color:i%2?0xff4400:0xff9933,transparent:true,opacity:0.06-i*0.01,side:THREE.BackSide})));
        }
        group.add(new THREE.PointLight(0xff6633,2,30));
    } else if (d.type==="galaxy_core") {
        for(let i=0;i<500;i++){
            const r=Math.random()*3, theta=Math.random()*Math.PI*2, phi=(Math.random()-0.5)*0.4;
            const brightness=1-r/4;
            const mesh=new THREE.Mesh(new THREE.SphereGeometry(0.015+Math.random()*0.04,4,4),
                new THREE.MeshBasicMaterial({color:new THREE.Color(brightness,brightness*0.8,brightness*0.3)}));
            mesh.position.set(r*Math.cos(theta),r*Math.sin(phi),r*Math.sin(theta));
            group.add(mesh);
        }
        for(let arm=0;arm<4;arm++){
            for(let i=0;i<200;i++){
                const t=i/200, angle=arm*(Math.PI/2)+t*Math.PI*3, r=t*6;
                const mesh=new THREE.Mesh(new THREE.SphereGeometry(0.02+Math.random()*0.03,3,3),
                    new THREE.MeshBasicMaterial({color:new THREE.Color(1-t*0.5,0.7-t*0.3,0.3),transparent:true,opacity:0.6-t*0.3}));
                mesh.position.set(r*Math.cos(angle)+(Math.random()-0.5)*0.5,(Math.random()-0.5)*0.3,r*Math.sin(angle)+(Math.random()-0.5)*0.5);
                group.add(mesh);
            }
        }
        group.add(new THREE.Mesh(new THREE.SphereGeometry(0.5,16,16),new THREE.MeshBasicMaterial({color:0xffffaa})));
        group.add(new THREE.PointLight(0xffd700,3,20));
    } else if (d.type==="galaxy") {
        for(let arm=0;arm<2;arm++){
            for(let i=0;i<600;i++){
                const t=i/600, angle=arm*Math.PI+t*Math.PI*4, r=0.3+t*5;
                const h=0.7+t*0.2;
                const mesh=new THREE.Mesh(new THREE.SphereGeometry(0.015+Math.random()*0.025,3,3),
                    new THREE.MeshBasicMaterial({color:new THREE.Color(h*0.7,h*0.7,1),transparent:true,opacity:0.7-t*0.4}));
                mesh.position.set(r*Math.cos(angle)+(Math.random()-0.5)*0.4,(Math.random()-0.5)*0.25,r*Math.sin(angle)+(Math.random()-0.5)*0.4);
                group.add(mesh);
            }
        }
        for(let i=0;i<150;i++){
            const r=Math.random()*1.2, theta=Math.random()*Math.PI*2, phi=(Math.random()-0.5)*0.5;
            group.add(new THREE.Mesh(new THREE.SphereGeometry(0.02+Math.random()*0.05,4,4),
                new THREE.MeshBasicMaterial({color:new THREE.Color(1,0.9,0.7),transparent:true,opacity:0.8})));
        }
        group.add(new THREE.Mesh(new THREE.SphereGeometry(1,8,8),
            new THREE.MeshBasicMaterial({color:0xaaaaff,transparent:true,opacity:0.12,side:THREE.BackSide})));
    } else if (d.type==="blackhole") {
        const r=1.5;
        group.add(new THREE.Mesh(new THREE.SphereGeometry(r,32,32),new THREE.MeshBasicMaterial({color:0x000000})));
        for(let i=0;i<8;i++){
            const inner=r*1.4+i*0.35, outer=inner+0.3, t=i/8;
            const ring=new THREE.Mesh(new THREE.RingGeometry(inner,outer,64),
                new THREE.MeshBasicMaterial({color:new THREE.Color(1-t*0.3,0.4-t*0.3,t*0.1),side:THREE.DoubleSide,transparent:true,opacity:0.6-t*0.3}));
            ring.rotation.x=Math.PI*0.15; ring.userData.rotSpeed=0.003-t*0.0003; group.add(ring);
        }
        const jetMat=new THREE.MeshBasicMaterial({color:0x00d4ff,transparent:true,opacity:0.15,side:THREE.DoubleSide});
        const jetTop=new THREE.Mesh(new THREE.CylinderGeometry(0,0.3,8,8,1,true),jetMat);
        jetTop.position.y=4; group.add(jetTop);
        const jetBot=new THREE.Mesh(new THREE.CylinderGeometry(0,0.3,8,8,1,true),jetMat.clone());
        jetBot.position.y=-4; jetBot.rotation.x=Math.PI; group.add(jetBot);
        group.add(new THREE.PointLight(0xff6600,2,20));
    } else if (d.type==="universe_edge") {
        group.add(new THREE.Mesh(new THREE.SphereGeometry(5,32,32),
            new THREE.MeshBasicMaterial({color:0x220033,side:THREE.BackSide,transparent:true,opacity:0.5})));
        for(let i=0;i<800;i++){
            const theta=Math.random()*Math.PI*2, phi=Math.acos(2*Math.random()-1), r2=2+Math.random()*4;
            const c=Math.random();
            const mesh=new THREE.Mesh(new THREE.SphereGeometry(0.02+Math.random()*0.05,4,4),
                new THREE.MeshBasicMaterial({color:new THREE.Color(c*0.5,c*0.3,c),transparent:true,opacity:0.4+Math.random()*0.5}));
            mesh.position.set(r2*Math.sin(phi)*Math.cos(theta),r2*Math.sin(phi)*Math.sin(theta),r2*Math.cos(phi));
            group.add(mesh);
        }
        for(let i=0;i<5;i++){
            const ring=new THREE.Mesh(new THREE.TorusGeometry(2+i*0.6,0.05,8,64),
                new THREE.MeshBasicMaterial({color:0xff00ff,transparent:true,opacity:0.1-i*0.015}));
            ring.rotation.x=Math.random()*Math.PI; ring.rotation.y=Math.random()*Math.PI;
            ring.userData.rotSpeed=0.001*(i%2?1:-1); group.add(ring);
        }
        group.add(new THREE.Mesh(new THREE.SphereGeometry(0.6,8,8),
            new THREE.MeshBasicMaterial({color:0xffffff,transparent:true,opacity:0.9})));
        group.add(new THREE.PointLight(0xcc00ff,3,30));
    }
    return group;
}

// ═══════════════════════════════════════
//  MOTION STATE
// ═══════════════════════════════════════
let mouseX = 0, mouseY = 0;
let targetMouseX = 0, targetMouseY = 0;
let gyroX = 0, gyroY = 0;
let isGyroActive = false;

// Mouse parallax
document.addEventListener('mousemove', (e) => {
    targetMouseX = (e.clientX / window.innerWidth - 0.5) * 2;
    targetMouseY = (e.clientY / window.innerHeight - 0.5) * 2;
});

// Gyroscope (mobile)
function requestGyro() {
    if (typeof DeviceOrientationEvent !== 'undefined' &&
        typeof DeviceOrientationEvent.requestPermission === 'function') {
        DeviceOrientationEvent.requestPermission()
            .then(state => { if (state === 'granted') enableGyro(); })
            .catch(() => {});
    } else if ('DeviceOrientationEvent' in window) {
        enableGyro();
    }
}

function enableGyro() {
    window.addEventListener('deviceorientation', (e) => {
        if (e.beta !== null && e.gamma !== null) {
            gyroY = THREE.MathUtils.clamp(e.gamma / 45, -1, 1);
            gyroX = THREE.MathUtils.clamp((e.beta - 45) / 45, -1, 1);
            if (!isGyroActive) {
                isGyroActive = true;
                document.getElementById('gyroIndicator').style.display = 'block';
            }
        }
    });
}

// ── Touch / Swipe ──
let touchStartX = 0, touchStartY = 0;
let touchStartTime = 0;
let isSwiping = false;

document.addEventListener('touchstart', (e) => {
    touchStartX = e.touches[0].clientX;
    touchStartY = e.touches[0].clientY;
    touchStartTime = Date.now();
    isSwiping = false;
}, { passive: true });

document.addEventListener('touchmove', (e) => {
    if (e.touches.length === 1) {
        const dx = e.touches[0].clientX - touchStartX;
        const dy = e.touches[0].clientY - touchStartY;
        if (Math.abs(dx) > 8 || Math.abs(dy) > 8) isSwiping = true;
        // Live parallax on touch move
        targetMouseX = (e.touches[0].clientX / window.innerWidth - 0.5) * 2;
        targetMouseY = (e.touches[0].clientY / window.innerHeight - 0.5) * 2;
    }
}, { passive: true });

document.addEventListener('touchend', (e) => {
    const dx = e.changedTouches[0].clientX - touchStartX;
    const dy = e.changedTouches[0].clientY - touchStartY;
    const dt = Date.now() - touchStartTime;
    const dist = Math.sqrt(dx*dx + dy*dy);

    if (dist > 50 && dt < 500) {
        // Swipe gesture
        if (Math.abs(dx) > Math.abs(dy)) {
            // Horizontal swipe
            if (dx < -50) nextDest();
            else if (dx > 50) prevDest();
        } else {
            // Vertical swipe
            if (dy < -50) nextDest();
            else if (dy > 50) prevDest();
        }
    } else if (dist < 10) {
        // Tap — ripple effect
        spawnRipple(e.changedTouches[0].clientX, e.changedTouches[0].clientY);
    }
}, { passive: true });

function spawnRipple(x, y) {
    const ripple = document.createElement('div');
    ripple.className = 'tap-ripple';
    ripple.style.left = x + 'px';
    ripple.style.top  = y + 'px';
    document.body.appendChild(ripple);
    setTimeout(() => ripple.remove(), 700);
}

// ─── 2D Particle Canvas ───
const pCanvas = document.getElementById('particleCanvas');
const pCtx = pCanvas.getContext('2d');
pCanvas.width  = window.innerWidth;
pCanvas.height = window.innerHeight;

const particles = [];

function spawnParticles(count = 40) {
    const cx = window.innerWidth / 2;
    const cy = window.innerHeight / 2;
    for (let i = 0; i < count; i++) {
        const angle = Math.random() * Math.PI * 2;
        const speed = 1 + Math.random() * 4;
        particles.push({
            x: cx, y: cy,
            vx: Math.cos(angle) * speed,
            vy: Math.sin(angle) * speed,
            life: 1,
            decay: 0.012 + Math.random() * 0.02,
            size: 1.5 + Math.random() * 3,
            color: `hsl(${180 + Math.random()*60}, 100%, 70%)`
        });
    }
}

function updateParticles() {
    pCtx.clearRect(0, 0, pCanvas.width, pCanvas.height);
    for (let i = particles.length - 1; i >= 0; i--) {
        const p = particles[i];
        p.x  += p.vx;
        p.y  += p.vy;
        p.vy += 0.04; // subtle gravity
        p.life -= p.decay;
        if (p.life <= 0) { particles.splice(i, 1); continue; }
        pCtx.save();
        pCtx.globalAlpha = p.life;
        pCtx.fillStyle = p.color;
        pCtx.beginPath();
        pCtx.arc(p.x, p.y, p.size * p.life, 0, Math.PI * 2);
        pCtx.fill();
        pCtx.restore();
    }
}

// ── Name pop ──
function showNamePop(name) {
    const old = document.querySelector('.name-pop');
    if (old) old.remove();
    const el = document.createElement('div');
    el.className = 'name-pop';
    el.textContent = name;
    document.body.appendChild(el);
    setTimeout(() => el.remove(), 2100);
}

// ── State ──
let currentIndex = -1;
let isTransitioning = false;
let currentObject = null;
let cameraTargetPos  = new THREE.Vector3(0, 2, 8);
let cameraCurrentPos = new THREE.Vector3(0, 2, 8);

// ── Minimap ──
const minimap = document.getElementById('minimap');
DESTINATIONS.forEach((d, i) => {
    if (i > 0) {
        const line = document.createElement('div');
        line.className = 'minimap-line';
        minimap.appendChild(line);
    }
    const dot = document.createElement('div');
    dot.className = 'minimap-dot';
    dot.dataset.name  = d.name;
    dot.dataset.index = i;
    dot.addEventListener('click',      () => { if (!isTransitioning) jumpTo(i); });
    dot.addEventListener('touchstart', () => { if (!isTransitioning) jumpTo(i); }, { passive: true });
    minimap.appendChild(dot);
});

function updateMinimap() {
    document.querySelectorAll('.minimap-dot').forEach((dot, i) => {
        dot.classList.remove('active','visited');
        if (i === currentIndex) dot.classList.add('active');
        else if (i < currentIndex) dot.classList.add('visited');
    });
}

// ── Distance formatter ──
function formatDist(ly) {
    if (ly === 0) return "0 km";
    if (ly < 0.001) return (ly * 9.461e12).toExponential(1) + " km";
    if (ly < 1)     return (ly * 63241).toFixed(0) + " AU";
    if (ly < 1000)  return ly.toFixed(2) + " ly";
    if (ly < 1e6)   return (ly / 1000).toFixed(1) + "K ly";
    if (ly < 1e9)   return (ly / 1e6).toFixed(1) + "M ly";
    return (ly / 1e9).toFixed(1) + "B ly";
}

// ── Load destination ──
function loadDestination(index) {
    const d = DESTINATIONS[index];
    if (currentObject) { scene.remove(currentObject); currentObject = null; }
    currentObject = makePlanet(d);
    // Start scaled down for pop-in
    currentObject.scale.set(0.01, 0.01, 0.01);
    scene.add(currentObject);

    document.getElementById('destName').textContent  = d.name;
    document.getElementById('distValue').textContent = formatDist(d.distance);
    const progress = ((index + 1) / DESTINATIONS.length) * 100;
    document.getElementById('progressBar').style.width = progress + '%';
    document.getElementById('stepCounter').textContent = `${index + 1} / ${DESTINATIONS.length}`;

    const vel = index === 0 ? "0.001 c" : index < 4 ? "0.1 c" : index < 8 ? "0.9 c" : "99.99% c";
    document.getElementById('velocityVal').textContent = vel;

    document.getElementById('infoCategory').textContent = d.category;
    document.getElementById('infoTitle').textContent    = d.name;
    document.getElementById('infoDesc').textContent     = d.desc;
    document.getElementById('statsRow').innerHTML = d.stats.map(s =>
        `<div class="stat-item"><div class="stat-val">${s.v}</div><div class="stat-lbl">${s.l}</div></div>`
    ).join('');

    setTimeout(() => document.getElementById('infoPanel').classList.add('visible'), 300);
    document.getElementById('prevBtn').disabled = (index === 0);

    const camZ = ['asteroids','kuiper','oort'].includes(d.type) ? 12 :
                 ['jupiter','saturn'].includes(d.type) ? 10 :
                 ['galaxy_core','galaxy','universe_edge'].includes(d.type) ? 15 : 8;
    cameraTargetPos.set(0, 2, camZ);

    // Pop-in scale animation
    let scaleT = 0;
    const scaleInterval = setInterval(() => {
        scaleT += 0.07;
        if (scaleT >= 1) { scaleT = 1; clearInterval(scaleInterval); }
        const s = easeOutBack(scaleT);
        if (currentObject) currentObject.scale.set(s, s, s);
    }, 16);

    showNamePop(d.name);
    spawnParticles(50);
    updateMinimap();
}

function easeOutBack(t) {
    const c1 = 1.70158, c3 = c1 + 1;
    return 1 + c3 * Math.pow(t - 1, 3) + c1 * Math.pow(t - 1, 2);
}

// ── Warp transition ──
function warpTo(index) {
    if (isTransitioning) return;
    isTransitioning = true;
    const overlay = document.getElementById('warpOverlay');
    overlay.classList.add('active');
    overlay.style.background = 'radial-gradient(ellipse at center, rgba(0,212,255,0.4) 0%, rgba(0,0,30,0.9) 100%)';
    document.getElementById('infoPanel').classList.remove('visible');

    // Warp star effect
    const warpGeo = new THREE.BufferGeometry();
    const cnt = 500;
    const wPos = new Float32Array(cnt * 3);
    for (let i = 0; i < cnt; i++) {
        wPos[i*3]   = (Math.random()-0.5)*20;
        wPos[i*3+1] = (Math.random()-0.5)*10;
        wPos[i*3+2] = (Math.random()-0.5)*40;
    }
    warpGeo.setAttribute('position', new THREE.BufferAttribute(wPos, 3));
    const warpStars = new THREE.Points(warpGeo,
        new THREE.PointsMaterial({ color: 0x00d4ff, size: 0.15, transparent: true, opacity: 0.8 }));
    scene.add(warpStars);

    let warpT = 0;
    const warpInterval = setInterval(() => {
        warpT += 0.03;
        const pos = warpStars.geometry.attributes.position.array;
        for (let i = 0; i < pos.length; i += 3) {
            pos[i+2] -= 2;
            if (pos[i+2] < -20) pos[i+2] = 20;
        }
        warpStars.geometry.attributes.position.needsUpdate = true;
        if (warpT > 1) {
            clearInterval(warpInterval);
            scene.remove(warpStars);
            overlay.style.background = 'radial-gradient(ellipse at center, transparent 0%, rgba(0,0,0,0.6) 100%)';
            loadDestination(index);
            setTimeout(() => {
                overlay.classList.remove('active');
                isTransitioning = false;
            }, 600);
        }
    }, 16);
}

function jumpTo(index) { currentIndex = index; warpTo(index); }

function nextDest() {
    if (isTransitioning) return;
    if (currentIndex < DESTINATIONS.length - 1) { currentIndex++; warpTo(currentIndex); }
    else showCompletion();
}

function prevDest() {
    if (isTransitioning || currentIndex <= 0) return;
    currentIndex--;
    warpTo(currentIndex);
}

function launchMission() {
    document.getElementById('landing').classList.add('hidden');
    document.getElementById('navControls').style.display = 'flex';
    // Show swipe hint on mobile
    if ('ontouchstart' in window) {
        document.getElementById('swipeHint').style.display = 'block';
        setTimeout(() => document.getElementById('swipeHint').style.display = 'none', 5000);
    }
    requestGyro();
    currentIndex = 0;
    loadDestination(0);
}

function showCompletion() {
    document.getElementById('infoPanel').classList.remove('visible');
    document.getElementById('navControls').style.display = 'none';
    spawnParticles(120);
    setTimeout(() => document.getElementById('completion').classList.add('visible'), 500);
}

function restartMission() {
    document.getElementById('completion').classList.remove('visible');
    currentIndex = -1;
    if (currentObject) { scene.remove(currentObject); currentObject = null; }
    document.getElementById('progressBar').style.width = '0%';
    document.getElementById('distValue').textContent = '0 km';
    document.getElementById('destName').textContent  = '— AWAITING LAUNCH —';
    updateMinimap();
    setTimeout(() => document.getElementById('landing').classList.remove('hidden'), 400);
}

// ── Render Loop ──
const clock = new THREE.Clock();

function animate() {
    requestAnimationFrame(animate);
    const dt      = clock.getDelta();
    const elapsed = clock.getElapsedTime();

    // Smooth mouse/gyro
    mouseX += (targetMouseX - mouseX) * 0.06;
    mouseY += (targetMouseY - mouseY) * 0.06;

    // Starfield rotation
    starfield.rotation.y += dt * 0.005;
    starfield.rotation.x += dt * 0.002;

    // Parallax on starfield
    starfield.rotation.y += mouseX * 0.0005;
    starfield.rotation.x += mouseY * 0.0005;

    // Object rotation + animation
    if (currentObject) {
        currentObject.rotation.y += dt * 0.25;

        // Mouse / gyro tilt on object
        const tiltX = isGyroActive ? gyroX : mouseY;
        const tiltY = isGyroActive ? gyroY : mouseX;
        currentObject.rotation.x += (tiltX * 0.08 - currentObject.rotation.x) * 0.05;

        currentObject.children.forEach(child => {
            if (child.userData.rotSpeed) child.rotation.y += child.userData.rotSpeed;
            if (child.userData.orbitSpeed !== undefined) {
                child.userData.orbitAngle += child.userData.orbitSpeed;
                const r = child.userData.orbitR;
                child.position.x = Math.cos(child.userData.orbitAngle) * r;
                child.position.z = Math.sin(child.userData.orbitAngle) * r;
                if (child.userData.orbitY !== undefined) child.position.y = child.userData.orbitY;
            }
        });

        // Floating bob
        currentObject.position.y = Math.sin(elapsed * 0.6) * 0.12;
    }

    // Smooth camera
    cameraCurrentPos.lerp(cameraTargetPos, dt * 2);
    camera.position.copy(cameraCurrentPos);

    // Camera parallax from mouse / gyro
    const camTiltX = isGyroActive ? gyroY : mouseX;
    const camTiltY = isGyroActive ? gyroX : mouseY;
    camera.position.x += camTiltX * 0.8 + Math.sin(elapsed * 0.3) * 0.15;
    camera.position.y += camTiltY * 0.5 + Math.cos(elapsed * 0.2) * 0.1;
    camera.lookAt(0, 0, 0);

    // 2D particles
    updateParticles();

    renderer.render(scene, camera);
}

animate();

// ── Resize ──
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
    pCanvas.width  = window.innerWidth;
    pCanvas.height = window.innerHeight;
});

// ── Keyboard ──
document.addEventListener('keydown', e => {
    if (e.key==='ArrowRight'||e.key==='ArrowDown') { e.preventDefault(); nextDest(); }
    if (e.key==='ArrowLeft' ||e.key==='ArrowUp')   { e.preventDefault(); prevDest(); }
});

// ── Scroll wheel ──
let wheelLock = false;
window.addEventListener('wheel', (e) => {
    if (wheelLock) return;
    wheelLock = true;
    if (e.deltaY > 30) nextDest();
    else if (e.deltaY < -30) prevDest();
    setTimeout(() => wheelLock = false, 900);
}, { passive: true });
</script>
</body>
</html>
""", height=820, scrolling=False)