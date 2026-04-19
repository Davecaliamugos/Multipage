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

*, *::before, *::after {
    margin: 0; padding: 0;
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
    -webkit-touch-callout: none;
}

html {
    height: 100%;
    overflow: hidden;
}

body {
    background: #000;
    overflow: hidden;
    font-family: 'Inter', sans-serif;
    color: #fff;
    width: 100%;
    height: 100%;
    position: fixed;
    top: 0; left: 0;
    touch-action: none;
    user-select: none;
    -webkit-user-select: none;
}

#canvas3d {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    z-index: 0;
    touch-action: none;
}

#particleCanvas {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    z-index: 5;
    pointer-events: none;
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
    padding: clamp(8px,2vw,16px) clamp(12px,3vw,28px);
    background: linear-gradient(180deg, rgba(0,0,0,0.9) 0%, transparent 100%);
    gap: 8px;
}

.mission-title {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.5rem, 2vw, 1rem);
    font-weight: 700;
    color: #00d4ff;
    letter-spacing: clamp(1px, 0.5vw, 3px);
    text-transform: uppercase;
    text-shadow: 0 0 20px rgba(0,212,255,0.8);
    white-space: nowrap;
    flex-shrink: 0;
}

.top-center {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 3px;
    flex: 1;
    min-width: 0;
    padding: 0 8px;
}

.destination-label {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.4rem, 1.2vw, 0.65rem);
    color: #9ca3af;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.destination-name {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.65rem, 2.5vw, 1.1rem);
    font-weight: 900;
    color: #fff;
    text-shadow: 0 0 30px rgba(255,255,255,0.5);
    transition: all 0.4s ease;
    text-align: center;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    width: 100%;
}

.velocity-box {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.5rem, 1.5vw, 0.75rem);
    color: #34d399;
    text-align: right;
    letter-spacing: 1px;
    white-space: nowrap;
    flex-shrink: 0;
}

.progress-track {
    margin: 0 clamp(12px,3vw,28px);
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
    right: -5px; top: -4px;
    width: 10px; height: 10px;
    background: #fff;
    border-radius: 50%;
    box-shadow: 0 0 10px #00d4ff, 0 0 20px #00d4ff;
}

.distance-hud {
    position: fixed;
    top: clamp(60px,10vw,90px);
    left: clamp(12px,3vw,28px);
    z-index: 100;
    font-family: 'Orbitron', monospace;
}

.dist-label {
    font-size: clamp(0.4rem,1.2vw,0.55rem);
    color: #6b7280;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 2px;
}

.dist-value {
    font-size: clamp(0.85rem,3vw,1.4rem);
    font-weight: 700;
    color: #00d4ff;
    text-shadow: 0 0 20px rgba(0,212,255,0.5);
    transition: all 0.5s ease;
}

/* Info Panel */
#infoPanel {
    position: fixed;
    bottom: clamp(90px,15vw,110px);
    left: clamp(12px,3vw,28px);
    z-index: 100;
    width: min(320px, calc(100vw - 50px));
    background: rgba(5,10,25,0.92);
    border: 1px solid rgba(0,212,255,0.2);
    border-left: 3px solid #00d4ff;
    border-radius: 0 12px 12px 0;
    padding: clamp(12px,2.5vw,20px) clamp(14px,3vw,22px);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    transform: translateX(-120%);
    transition: transform 0.6s cubic-bezier(0.4,0,0.2,1);
    pointer-events: none;
}

#infoPanel.visible { transform: translateX(0); }

.info-category {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.4rem,1.3vw,0.55rem);
    color: #00d4ff;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 6px;
}

.info-title {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.85rem,3vw,1.3rem);
    font-weight: 900;
    color: #fff;
    margin-bottom: 8px;
    line-height: 1.2;
}

.info-desc {
    font-size: clamp(0.7rem,1.8vw,0.82rem);
    color: #9ca3af;
    line-height: 1.6;
    margin-bottom: 12px;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    overflow: hidden;
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
    font-size: clamp(0.6rem,1.8vw,0.85rem);
    font-weight: 700;
    color: #00d4ff;
}

.stat-lbl {
    font-size: clamp(0.5rem,1.3vw,0.65rem);
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 2px;
}

/* Nav Controls */
#navControls {
    position: fixed;
    bottom: clamp(16px,4vw,30px);
    left: 50%;
    transform: translateX(-50%);
    z-index: 200;
    display: flex;
    align-items: center;
    gap: clamp(8px,2vw,16px);
}

.nav-btn {
    padding: clamp(11px,2.5vw,13px) clamp(20px,4.5vw,32px);
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.58rem,1.8vw,0.75rem);
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #fff;
    background: rgba(5,10,25,0.9);
    border: 1px solid rgba(0,212,255,0.4);
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.2s;
    position: relative;
    overflow: hidden;
    touch-action: manipulation;
    -webkit-tap-highlight-color: transparent;
    white-space: nowrap;
    min-height: 44px; /* iOS touch target */
    min-width: 44px;
}

.nav-btn:active {
    background: rgba(0,212,255,0.15);
    border-color: #00d4ff;
    box-shadow: 0 0 20px rgba(0,212,255,0.4);
    transform: scale(0.96);
}

.nav-btn:disabled {
    opacity: 0.3;
    pointer-events: none;
}

.nav-btn.primary {
    background: linear-gradient(135deg,rgba(0,212,255,0.2),rgba(139,92,246,0.2));
    border-color: #00d4ff;
    box-shadow: 0 0 20px rgba(0,212,255,0.2);
}

.step-counter {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.55rem,1.5vw,0.7rem);
    color: #9ca3af;
    letter-spacing: 2px;
    min-width: 55px;
    text-align: center;
}

/* Minimap */
#minimap {
    position: fixed;
    right: clamp(12px,2.5vw,24px);
    top: 50%;
    transform: translateY(-50%);
    z-index: 100;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.minimap-line {
    width: 1px;
    height: clamp(14px,2.5vw,22px);
    background: rgba(255,255,255,0.1);
}

.minimap-dot {
    width: clamp(6px,1.5vw,8px);
    height: clamp(6px,1.5vw,8px);
    border-radius: 50%;
    background: rgba(255,255,255,0.2);
    border: 1px solid rgba(255,255,255,0.15);
    cursor: pointer;
    transition: all 0.3s;
    position: relative;
    touch-action: manipulation;
    min-width: 24px; /* larger touch area */
    min-height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.minimap-dot::before {
    content: '';
    width: clamp(6px,1.5vw,8px);
    height: clamp(6px,1.5vw,8px);
    border-radius: 50%;
    background: inherit;
    border: inherit;
    display: block;
}

.minimap-dot.active::before { background: #00d4ff; border-color: #00d4ff; box-shadow: 0 0 10px #00d4ff; }
.minimap-dot.visited::before { background: rgba(0,212,255,0.4); border-color: rgba(0,212,255,0.4); }

/* Swipe indicator */
#swipeIndicator {
    position: fixed;
    bottom: clamp(76px,12vw,90px);
    left: 50%;
    transform: translateX(-50%);
    z-index: 150;
    display: none;
    flex-direction: row;
    align-items: center;
    gap: 16px;
    font-family: 'Orbitron', monospace;
    font-size: 0.55rem;
    color: rgba(0,212,255,0.5);
    letter-spacing: 2px;
    text-transform: uppercase;
    white-space: nowrap;
    animation: swipePulse 2s ease-in-out infinite;
}

@keyframes swipePulse {
    0%,100% { opacity: 0.3; }
    50%      { opacity: 1; }
}

.swipe-arrow {
    font-size: 1rem;
    animation: swipeArrow 1.2s ease-in-out infinite;
}
.swipe-arrow.left  { animation-delay: 0s; }
.swipe-arrow.right { animation-delay: 0.3s; }

@keyframes swipeArrow {
    0%,100% { transform: translateX(0); opacity: 0.4; }
    50%      { transform: translateX(4px); opacity: 1; }
}

/* Motion tilt indicator */
#motionIndicator {
    position: fixed;
    top: clamp(60px,10vw,90px);
    right: clamp(12px,3vw,28px);
    z-index: 100;
    display: none;
    flex-direction: column;
    align-items: center;
    gap: 4px;
}

.motion-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #00d4ff;
    box-shadow: 0 0 6px #00d4ff;
    animation: motionPulse 1s ease-in-out infinite;
}

@keyframes motionPulse {
    0%,100% { transform: scale(1); opacity: 0.6; }
    50%      { transform: scale(1.4); opacity: 1; }
}

.motion-label {
    font-family: 'Orbitron', monospace;
    font-size: 0.45rem;
    color: rgba(0,212,255,0.6);
    letter-spacing: 1px;
    text-transform: uppercase;
}

/* Landing */
#landing {
    position: fixed;
    inset: 0;
    z-index: 500;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: radial-gradient(ellipse at center, rgba(0,20,40,0.96) 0%, rgba(0,0,0,0.99) 100%);
    transition: opacity 0.8s ease, visibility 0.8s;
    padding: clamp(16px,5vw,40px);
    text-align: center;
}

#landing.hidden {
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
}

.landing-badge {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.48rem,1.5vw,0.6rem);
    letter-spacing: 4px;
    color: #00d4ff;
    text-transform: uppercase;
    margin-bottom: clamp(16px,4vw,30px);
    opacity: 0.8;
}

.landing-title {
    font-family: 'Orbitron', monospace;
    font-size: clamp(2.2rem,10vw,4.5rem);
    font-weight: 900;
    line-height: 1.05;
    margin-bottom: clamp(12px,3vw,20px);
    background: linear-gradient(135deg, #fff 0%, #00d4ff 40%, #8b5cf6 70%, #ff6bcb 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.landing-sub {
    font-size: clamp(0.78rem,2.5vw,1rem);
    color: #6b7280;
    max-width: 460px;
    line-height: 1.6;
    margin-bottom: clamp(28px,6vw,50px);
}

.launch-btn {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.68rem,2vw,0.85rem);
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #000;
    background: linear-gradient(135deg, #00d4ff, #8b5cf6);
    border: none;
    padding: clamp(13px,3.5vw,16px) clamp(28px,7vw,50px);
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.2s;
    touch-action: manipulation;
    min-height: 48px;
}

.launch-btn:active {
    transform: scale(0.97);
    box-shadow: 0 0 40px rgba(0,212,255,0.5);
}

.scroll-hint {
    position: absolute;
    bottom: clamp(20px,4vw,40px);
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.45rem,1.2vw,0.6rem);
    letter-spacing: 2px;
    color: #374151;
    text-transform: uppercase;
    animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse { 0%,100%{opacity:.4} 50%{opacity:1} }

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
    padding: clamp(16px,5vw,40px);
    text-align: center;
}

#completion.visible { opacity: 1; visibility: visible; }

.complete-label {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.48rem,1.5vw,0.6rem);
    letter-spacing: 6px;
    color: #34d399;
    text-transform: uppercase;
    margin-bottom: clamp(10px,2.5vw,20px);
}

.complete-title {
    font-family: 'Orbitron', monospace;
    font-size: clamp(1.6rem,6vw,3.5rem);
    font-weight: 900;
    margin-bottom: clamp(10px,2.5vw,16px);
    background: linear-gradient(135deg, #34d399, #00d4ff, #8b5cf6, #ff6bcb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.complete-dist {
    font-family: 'Orbitron', monospace;
    font-size: clamp(1.1rem,4vw,2rem);
    font-weight: 900;
    color: #00d4ff;
    text-shadow: 0 0 30px rgba(0,212,255,0.5);
    margin-bottom: 10px;
}

.complete-text {
    font-size: clamp(0.72rem,2vw,0.9rem);
    color: #6b7280;
    max-width: 500px;
    line-height: 1.8;
    margin-bottom: clamp(24px,5vw,40px);
}

.restart-btn {
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.62rem,1.8vw,0.75rem);
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #fff;
    background: transparent;
    border: 1px solid rgba(0,212,255,0.5);
    padding: clamp(11px,2.5vw,14px) clamp(22px,5vw,40px);
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.2s;
    touch-action: manipulation;
    min-height: 44px;
}

.restart-btn:active {
    background: rgba(0,212,255,0.1);
    border-color: #00d4ff;
    box-shadow: 0 0 20px rgba(0,212,255,0.3);
}

/* Warp overlay */
#warpOverlay {
    position: fixed;
    inset: 0;
    z-index: 300;
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.3s;
}
#warpOverlay.active { opacity: 1; }

/* Scanlines */
.scanlines {
    position: fixed;
    inset: 0;
    z-index: 50;
    background: repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,0,0,0.03) 2px,rgba(0,0,0,0.03) 4px);
    pointer-events: none;
}

/* Corners */
.corner { position:fixed; z-index:100; width:clamp(22px,5vw,40px); height:clamp(22px,5vw,40px); pointer-events:none; }
.corner-tl { top:8px; left:8px; border-top:1px solid rgba(0,212,255,0.4); border-left:1px solid rgba(0,212,255,0.4); }
.corner-tr { top:8px; right:8px; border-top:1px solid rgba(0,212,255,0.4); border-right:1px solid rgba(0,212,255,0.4); }
.corner-bl { bottom:8px; left:8px; border-bottom:1px solid rgba(0,212,255,0.4); border-left:1px solid rgba(0,212,255,0.4); }
.corner-br { bottom:8px; right:8px; border-bottom:1px solid rgba(0,212,255,0.4); border-right:1px solid rgba(0,212,255,0.4); }

/* Name pop */
@keyframes namePop {
    0%   { opacity:0; transform:translate(-50%,-50%) scale(0.7); }
    20%  { opacity:1; transform:translate(-50%,-50%) scale(1.05); }
    80%  { opacity:1; transform:translate(-50%,-50%) scale(1); }
    100% { opacity:0; transform:translate(-50%,-50%) scale(0.9); }
}
.name-pop {
    position: fixed;
    top: 50%; left: 50%;
    transform: translate(-50%,-50%);
    z-index: 250;
    font-family: 'Orbitron', monospace;
    font-size: clamp(1.2rem,5vw,3rem);
    font-weight: 900;
    color: #fff;
    text-shadow: 0 0 40px rgba(0,212,255,0.8), 0 0 80px rgba(139,92,246,0.5);
    pointer-events: none;
    animation: namePop 2s ease forwards;
    white-space: nowrap;
    text-align: center;
}

/* Tap ripple */
@keyframes rippleOut {
    0%   { width:0; height:0; opacity:0.8; }
    100% { width:100px; height:100px; opacity:0; }
}
.tap-ripple {
    position: fixed;
    border-radius: 50%;
    background: rgba(0,212,255,0.25);
    pointer-events: none;
    z-index: 400;
    transform: translate(-50%,-50%);
    animation: rippleOut 0.7s ease-out forwards;
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
            <div style="font-size:clamp(0.4rem,1.2vw,0.55rem);color:#6b7280;letter-spacing:2px;margin-bottom:2px;">VELOCITY</div>
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

<!-- Motion indicator -->
<div id="motionIndicator">
    <div class="motion-dot"></div>
    <div class="motion-label">TILT</div>
</div>

<!-- Info Panel -->
<div id="infoPanel">
    <div class="info-category" id="infoCategory">SOLAR SYSTEM</div>
    <div class="info-title" id="infoTitle">Earth</div>
    <div class="info-desc" id="infoDesc">Our pale blue dot.</div>
    <div class="stats-row" id="statsRow"></div>
</div>

<!-- Minimap -->
<div id="minimap"></div>

<!-- Swipe indicator -->
<div id="swipeIndicator">
    <span class="swipe-arrow left">←</span>
    SWIPE TO NAVIGATE
    <span class="swipe-arrow right">→</span>
</div>

<!-- Nav -->
<div id="navControls" style="display:none;">
    <button class="nav-btn" id="prevBtn" ontouchend="handlePrev(event)" onclick="prevDest()" disabled>◀ PREV</button>
    <div class="step-counter" id="stepCounter">0 / 15</div>
    <button class="nav-btn primary" id="nextBtn" ontouchend="handleNext(event)" onclick="nextDest()">NEXT ▶</button>
</div>

<!-- Landing -->
<div id="landing">
    <div class="landing-badge">Deep Space Mission — 2025</div>
    <h1 class="landing-title">GALAXY<br>EXPLORER</h1>
    <p class="landing-sub">A 3D journey from Earth to the edge of the observable universe. 46.5 billion light-years await.</p>
    <button class="launch-btn" ontouchend="handleLaunch(event)" onclick="launchMission()">INITIATE LAUNCH</button>
    <div class="scroll-hint">Swipe ← → or use buttons to navigate</div>
</div>

<!-- Completion -->
<div id="completion">
    <div class="complete-label">Mission Complete</div>
    <div class="complete-title">EDGE OF THE<br>UNIVERSE REACHED</div>
    <div class="complete-dist">46.5 Billion Light-Years</div>
    <p class="complete-text">
        You have traversed the full breadth of the observable universe.
        The universe is 13.8 billion years old and still expanding.
    </p>
    <button class="restart-btn" ontouchend="handleRestart(event)" onclick="restartMission()">RESTART MISSION</button>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
'use strict';

// ── Touch handlers (prevent ghost click on mobile) ──
function handleNext(e)    { e.preventDefault(); e.stopPropagation(); nextDest(); }
function handlePrev(e)    { e.preventDefault(); e.stopPropagation(); prevDest(); }
function handleLaunch(e)  { e.preventDefault(); e.stopPropagation(); launchMission(); }
function handleRestart(e) { e.preventDefault(); e.stopPropagation(); restartMission(); }

// ═══════════════════════════════════════
//  DESTINATION DATA
// ═══════════════════════════════════════
const DESTINATIONS = [
    {
        name:"Earth", category:"SOLAR SYSTEM — INNER",
        desc:"Our pale blue dot — the only known harbor of life in the cosmos. Oceans cover 71% of its surface, and a fragile atmosphere protects all life beneath it.",
        distance:0, type:"earth",
        stats:[{v:"12,742 km",l:"Diameter"},{v:"1 AU",l:"From Sun"},{v:"4.5B yrs",l:"Age"},{v:"7.9B",l:"Population"}]
    },
    {
        name:"The Moon", category:"EARTH SYSTEM",
        desc:"Earth's ancient companion, shaping tides and seasons. Humanity's first foothold in space — 384,400 km from home.",
        distance:0.0000016, type:"moon",
        stats:[{v:"3,474 km",l:"Diameter"},{v:"27.3 days",l:"Orbit"},{v:"-173°C",l:"Min Temp"},{v:"127°C",l:"Max Temp"}]
    },
    {
        name:"Mars", category:"SOLAR SYSTEM — INNER",
        desc:"The Red Planet, humanity's next frontier. Ancient riverbeds suggest it once held liquid water. Olympus Mons rises 22km.",
        distance:0.000042, type:"mars",
        stats:[{v:"6,779 km",l:"Diameter"},{v:"1.5 AU",l:"From Sun"},{v:"687 days",l:"Year"},{v:"-80°C",l:"Avg Temp"}]
    },
    {
        name:"Asteroid Belt", category:"SOLAR SYSTEM — MID",
        desc:"Millions of rocky remnants between Mars and Jupiter, relics from the solar system's formation 4.6 billion years ago.",
        distance:0.00025, type:"asteroids",
        stats:[{v:"1M+",l:"Asteroids"},{v:"Ceres",l:"Largest"},{v:"2.2-3.2 AU",l:"Range"},{v:"4.6B yrs",l:"Age"}]
    },
    {
        name:"Jupiter", category:"SOLAR SYSTEM — OUTER",
        desc:"The colossus of our solar system. Its Great Red Spot — a storm larger than Earth — has raged for over 350 years.",
        distance:0.00052, type:"jupiter",
        stats:[{v:"139,820 km",l:"Diameter"},{v:"5.2 AU",l:"From Sun"},{v:"95 moons",l:"Satellites"},{v:"11.9 yrs",l:"Year"}]
    },
    {
        name:"Saturn", category:"SOLAR SYSTEM — OUTER",
        desc:"The ringed jewel of the solar system. Its rings span 282,000 km yet are barely 10 meters thick.",
        distance:0.0010, type:"saturn",
        stats:[{v:"116,460 km",l:"Diameter"},{v:"9.5 AU",l:"From Sun"},{v:"146 moons",l:"Satellites"},{v:"0.687",l:"Density"}]
    },
    {
        name:"Uranus", category:"SOLAR SYSTEM — OUTER",
        desc:"The tilted ice giant, rotating on its side at 98°. Its methane atmosphere renders it a haunting cyan-blue.",
        distance:0.0019, type:"uranus",
        stats:[{v:"50,724 km",l:"Diameter"},{v:"19.2 AU",l:"From Sun"},{v:"98°",l:"Axial Tilt"},{v:"-224°C",l:"Avg Temp"}]
    },
    {
        name:"Neptune", category:"SOLAR SYSTEM — OUTER",
        desc:"The windiest world in the solar system. Supersonic gales reach 2,100 km/h.",
        distance:0.0030, type:"neptune",
        stats:[{v:"49,244 km",l:"Diameter"},{v:"30.1 AU",l:"From Sun"},{v:"2,100 km/h",l:"Winds"},{v:"-214°C",l:"Avg Temp"}]
    },
    {
        name:"Kuiper Belt", category:"TRANS-NEPTUNIAN",
        desc:"A vast disc of icy debris beyond Neptune. Pluto resides here among thousands of frozen worlds.",
        distance:0.005, type:"kuiper",
        stats:[{v:"100K+",l:"Objects"},{v:"Pluto",l:"Most Famous"},{v:"30-55 AU",l:"Range"},{v:"-240°C",l:"Avg Temp"}]
    },
    {
        name:"Oort Cloud", category:"SOLAR SYSTEM BOUNDARY",
        desc:"A spherical shell of icy bodies enveloping the solar system. Source of long-period comets.",
        distance:0.5, type:"oort",
        stats:[{v:"1-2 ly",l:"Thickness"},{v:"Trillions",l:"Icy Bodies"},{v:"100,000 AU",l:"Max Dist"},{v:"-270°C",l:"Temp"}]
    },
    {
        name:"Proxima Centauri", category:"INTERSTELLAR SPACE",
        desc:"The nearest star to our Sun — a red dwarf 4.24 light-years away with a planet in the habitable zone.",
        distance:4.24, type:"star",
        stats:[{v:"Red Dwarf",l:"Type"},{v:"4.24 ly",l:"Distance"},{v:"Proxima b",l:"Exoplanet"},{v:"2,700°C",l:"Surface"}]
    },
    {
        name:"Galactic Center", category:"MILKY WAY",
        desc:"Sagittarius A* — a supermassive black hole 4 million times the Sun's mass — anchors the Milky Way.",
        distance:26000, type:"galaxy_core",
        stats:[{v:"4M × Sun",l:"BH Mass"},{v:"26,000 ly",l:"Distance"},{v:"200-400B",l:"Stars"},{v:"100,000 ly",l:"Diameter"}]
    },
    {
        name:"Andromeda Galaxy", category:"LOCAL GROUP",
        desc:"Our nearest galactic neighbor — 2.5 million light-years away. It will collide with the Milky Way in 4.5 billion years.",
        distance:2537000, type:"galaxy",
        stats:[{v:"1 trillion",l:"Stars"},{v:"2.5M ly",l:"Distance"},{v:"220,000 ly",l:"Diameter"},{v:"110 km/s",l:"Approach"}]
    },
    {
        name:"TON 618", category:"DEEP UNIVERSE",
        desc:"One of the most massive black holes ever — 66 billion solar masses. Its accretion disk outshines entire galaxies.",
        distance:55000000, type:"blackhole",
        stats:[{v:"66B × Sun",l:"Mass"},{v:"10.4B ly",l:"Distance"},{v:"1,300 AU",l:"Radius"},{v:"140T × Sun",l:"Luminosity"}]
    },
    {
        name:"Edge of Universe", category:"COSMIC HORIZON",
        desc:"The observable universe's boundary — 46.5 billion light-years. The farthest light since the Big Bang, 13.8 billion years ago.",
        distance:46500000000, type:"universe_edge",
        stats:[{v:"46.5B ly",l:"Radius"},{v:"93B ly",l:"Diameter"},{v:"2 Trillion",l:"Galaxies"},{v:"∞",l:"Beyond"}]
    }
];

// ═══════════════════════════════════════
//  THREE.JS SETUP
// ═══════════════════════════════════════
const canvas3d = document.getElementById('canvas3d');
const renderer = new THREE.WebGLRenderer({ canvas: canvas3d, antialias: true, alpha: true, powerPreference: 'high-performance' });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 0.8;

const scene = new THREE.Scene();
scene.fog = new THREE.FogExp2(0x000005, 0.008);

const camera = new THREE.PerspectiveCamera(65, window.innerWidth / window.innerHeight, 0.01, 5000);
camera.position.set(0, 2, 8);

scene.add(new THREE.AmbientLight(0x111122, 0.5));
const sunLight = new THREE.PointLight(0xfff4e0, 3, 100);
sunLight.position.set(10, 10, 10);
scene.add(sunLight);
const rimLight = new THREE.DirectionalLight(0x0044ff, 0.3);
rimLight.position.set(-5, 3, -5);
scene.add(rimLight);

// ── Starfield ──
function createStarfield() {
    const count = 10000;
    const geo = new THREE.BufferGeometry();
    const pos = new Float32Array(count * 3);
    const col = new Float32Array(count * 3);
    for (let i = 0; i < count; i++) {
        const theta = Math.random() * Math.PI * 2;
        const phi   = Math.acos(2 * Math.random() - 1);
        const r     = 200 + Math.random() * 600;
        pos[i*3]   = r * Math.sin(phi) * Math.cos(theta);
        pos[i*3+1] = r * Math.sin(phi) * Math.sin(theta);
        pos[i*3+2] = r * Math.cos(phi);
        const t = Math.random();
        if (t < 0.6)       { col[i*3]=1;   col[i*3+1]=1;   col[i*3+2]=1;   }
        else if (t < 0.75) { col[i*3]=0.6; col[i*3+1]=0.7; col[i*3+2]=1;   }
        else if (t < 0.9)  { col[i*3]=1;   col[i*3+1]=0.8; col[i*3+2]=0.6; }
        else                { col[i*3]=1;   col[i*3+1]=0.4; col[i*3+2]=0.4; }
    }
    geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
    geo.setAttribute('color',    new THREE.BufferAttribute(col, 3));
    return new THREE.Points(geo, new THREE.PointsMaterial({
        size: 0.8, sizeAttenuation: true,
        vertexColors: true, transparent: true, opacity: 0.9
    }));
}
const starfield = createStarfield();
scene.add(starfield);

// Nebulas
function createNebula(pos, color, scale) {
    const g = new THREE.Group();
    for (let i = 0; i < 60; i++) {
        const m = new THREE.Mesh(
            new THREE.SphereGeometry(Math.random()*4+1, 5, 5),
            new THREE.MeshBasicMaterial({ color, transparent:true, opacity:Math.random()*0.04+0.01, side:THREE.BackSide })
        );
        m.position.set((Math.random()-.5)*30*scale,(Math.random()-.5)*15*scale,(Math.random()-.5)*20*scale);
        g.add(m);
    }
    g.position.copy(pos);
    return g;
}
scene.add(createNebula(new THREE.Vector3(-40,5,-80),   0x4466ff, 1.5));
scene.add(createNebula(new THREE.Vector3(50,-10,-120), 0xff4488, 2));
scene.add(createNebula(new THREE.Vector3(-60,15,-200), 0x8844ff, 1.8));

// ── Planet builder ──
function makePlanet(d) {
    const g = new THREE.Group();
    const t = d.type;

    if (t === 'earth') {
        const r = 1.8;
        g.add(new THREE.Mesh(new THREE.SphereGeometry(r,64,64),
            new THREE.MeshPhongMaterial({color:0x1565c0,emissive:0x0a1628,shininess:80,specular:0x4488ff})));
        const land = new THREE.Mesh(new THREE.SphereGeometry(r+0.01,64,64),
            new THREE.MeshPhongMaterial({color:0x2d7d32,emissive:0x0a1f0a,shininess:10,transparent:true,opacity:0.7}));
        g.add(land);
        const clouds = new THREE.Mesh(new THREE.SphereGeometry(r+0.08,32,32),
            new THREE.MeshPhongMaterial({color:0xffffff,transparent:true,opacity:0.25,shininess:0}));
        clouds.userData.rotSpeed = 0.004; g.add(clouds);
        g.add(makeAtmo(r,0x4488ff)); g.add(makeGlow(r,0x1144ff,0.15));

    } else if (t === 'moon') {
        g.add(new THREE.Mesh(new THREE.SphereGeometry(0.9,32,32),
            new THREE.MeshPhongMaterial({color:0x9e9e9e,emissive:0x1a1a1a,shininess:5})));

    } else if (t === 'mars') {
        const r = 1.2;
        g.add(new THREE.Mesh(new THREE.SphereGeometry(r,48,48),
            new THREE.MeshPhongMaterial({color:0xc1440e,emissive:0x2d0a02,shininess:15})));
        const cap = new THREE.Mesh(new THREE.SphereGeometry(r*0.25,16,16,0,Math.PI*2,0,0.4),
            new THREE.MeshBasicMaterial({color:0xdde8f0,transparent:true,opacity:0.85}));
        cap.position.y = r*0.85; g.add(cap);

    } else if (t === 'asteroids') {
        for (let i = 0; i < 100; i++) {
            const m = new THREE.Mesh(new THREE.DodecahedronGeometry(Math.random()*.18+.04,0),
                new THREE.MeshPhongMaterial({color:0x6d5a4a,emissive:0x0d0905,shininess:5}));
            const angle = (i/100)*Math.PI*2, r = 3.5+(Math.random()-.5)*3;
            m.position.set(Math.cos(angle)*r,(Math.random()-.5)*.8,Math.sin(angle)*r);
            m.userData.orbitSpeed = (Math.random()*.0004+.0001)*(Math.random()<.5?1:-1);
            m.userData.orbitAngle = angle; m.userData.orbitR = r;
            g.add(m);
        }
        g.add(new THREE.Mesh(new THREE.SphereGeometry(0.4,16,16),
            new THREE.MeshPhongMaterial({color:0x9e8c7a,emissive:0x1a1510})));

    } else if (t === 'jupiter') {
        const r = 2.5;
        g.add(new THREE.Mesh(new THREE.SphereGeometry(r,48,48),
            new THREE.MeshPhongMaterial({color:0xc9a05a,emissive:0x2a1800,shininess:20})));
        [0xd4a860,0xc87840,0xe8c890,0xb86828].forEach((c,i) => {
            const b = new THREE.Mesh(new THREE.TorusGeometry(r,.1,8,64),
                new THREE.MeshBasicMaterial({color:c,transparent:true,opacity:0.5}));
            b.rotation.x = Math.PI/2; b.position.y = (i-1.5)*.7; g.add(b);
        });
        g.add(makeGlow(r,0xff9933,0.08));

    } else if (t === 'saturn') {
        const r = 2.2;
        g.add(new THREE.Mesh(new THREE.SphereGeometry(r,64,64),
            new THREE.MeshPhongMaterial({color:0xe8d08a,emissive:0x2a1e00,shininess:25})));
        [
            [r*1.25,r*1.9,0xd4b870,0.55],
            [r*1.95,r*2.4,0xc8a860,0.35]
        ].forEach(([ir,or,c,op]) => {
            const ring = new THREE.Mesh(new THREE.RingGeometry(ir,or,80),
                new THREE.MeshBasicMaterial({color:c,side:THREE.DoubleSide,transparent:true,opacity:op}));
            ring.rotation.x = -Math.PI/2.8; g.add(ring);
        });

    } else if (t === 'uranus') {
        const r = 1.8;
        const mesh = new THREE.Mesh(new THREE.SphereGeometry(r,48,48),
            new THREE.MeshPhongMaterial({color:0x4fd1c5,emissive:0x052220,shininess:60,specular:0x88ffff}));
        g.add(mesh);
        const rings = new THREE.Mesh(new THREE.RingGeometry(r*1.3,r*1.7,64),
            new THREE.MeshBasicMaterial({color:0x88cccc,side:THREE.DoubleSide,transparent:true,opacity:0.35}));
        rings.rotation.z = Math.PI/2; g.add(rings);
        g.add(makeAtmo(r,0x00cccc)); g.add(makeGlow(r,0x00ccff,0.12));

    } else if (t === 'neptune') {
        const r = 1.7;
        const mesh = new THREE.Mesh(new THREE.SphereGeometry(r,48,48),
            new THREE.MeshPhongMaterial({color:0x2b4cff,emissive:0x020830,shininess:70,specular:0x4466ff}));
        g.add(mesh);
        g.add(makeAtmo(r,0x2255ff)); g.add(makeGlow(r,0x3355ff,0.15));

    } else if (t === 'kuiper') {
        for (let i = 0; i < 120; i++) {
            const m = new THREE.Mesh(new THREE.SphereGeometry(Math.random()*.1+.02,5,5),
                new THREE.MeshPhongMaterial({color:0x7a6aaf,emissive:0x100820,shininess:30}));
            const angle = Math.random()*Math.PI*2, r = 4+Math.random()*3, y = (Math.random()-.5)*2;
            m.position.set(Math.cos(angle)*r,y,Math.sin(angle)*r);
            m.userData.orbitSpeed = Math.random()*.0002+.00005;
            m.userData.orbitAngle = angle; m.userData.orbitR = r; m.userData.orbitY = y;
            g.add(m);
        }

    } else if (t === 'oort') {
        for (let i = 0; i < 250; i++) {
            const theta = Math.random()*Math.PI*2, phi = Math.acos(2*Math.random()-1), r = 5+Math.random()*3;
            const m = new THREE.Mesh(new THREE.SphereGeometry(.03+Math.random()*.05,4,4),
                new THREE.MeshBasicMaterial({color:0xa0c4ff,transparent:true,opacity:.5+Math.random()*.4}));
            m.position.set(r*Math.sin(phi)*Math.cos(theta),r*Math.sin(phi)*Math.sin(theta),r*Math.cos(phi));
            g.add(m);
        }
        g.add(new THREE.Mesh(new THREE.SphereGeometry(6.5,24,24),
            new THREE.MeshBasicMaterial({color:0x8aacdd,wireframe:true,transparent:true,opacity:0.04})));

    } else if (t === 'star') {
        const r = 1.4;
        g.add(new THREE.Mesh(new THREE.SphereGeometry(r,48,48),new THREE.MeshBasicMaterial({color:0xff6020})));
        for (let i = 0; i < 4; i++) {
            g.add(new THREE.Mesh(new THREE.SphereGeometry(r*(1.3+i*.4),16,16),
                new THREE.MeshBasicMaterial({color:i%2?0xff4400:0xff9933,transparent:true,opacity:.05-i*.008,side:THREE.BackSide})));
        }
        g.add(new THREE.PointLight(0xff6633,2,30));

    } else if (t === 'galaxy_core') {
        for (let i = 0; i < 400; i++) {
            const r = Math.random()*3, theta = Math.random()*Math.PI*2, phi = (Math.random()-.5)*.4;
            const b = 1-r/4;
            const m = new THREE.Mesh(new THREE.SphereGeometry(.015+Math.random()*.04,4,4),
                new THREE.MeshBasicMaterial({color:new THREE.Color(b,b*.8,b*.3)}));
            m.position.set(r*Math.cos(theta),r*Math.sin(phi),r*Math.sin(theta));
            g.add(m);
        }
        for (let arm = 0; arm < 4; arm++) {
            for (let i = 0; i < 150; i++) {
                const t2 = i/150, angle = arm*(Math.PI/2)+t2*Math.PI*3, r = t2*6;
                const m = new THREE.Mesh(new THREE.SphereGeometry(.02+Math.random()*.03,3,3),
                    new THREE.MeshBasicMaterial({color:new THREE.Color(1-t2*.5,.7-t2*.3,.3),transparent:true,opacity:.6-t2*.3}));
                m.position.set(r*Math.cos(angle)+(Math.random()-.5)*.5,(Math.random()-.5)*.3,r*Math.sin(angle)+(Math.random()-.5)*.5);
                g.add(m);
            }
        }
        g.add(new THREE.Mesh(new THREE.SphereGeometry(.5,16,16),new THREE.MeshBasicMaterial({color:0xffffaa})));
        g.add(new THREE.PointLight(0xffd700,3,20));

    } else if (t === 'galaxy') {
        for (let arm = 0; arm < 2; arm++) {
            for (let i = 0; i < 500; i++) {
                const t2=i/500, angle=arm*Math.PI+t2*Math.PI*4, r=.3+t2*5, h=.7+t2*.2;
                const m = new THREE.Mesh(new THREE.SphereGeometry(.015+Math.random()*.025,3,3),
                    new THREE.MeshBasicMaterial({color:new THREE.Color(h*.7,h*.7,1),transparent:true,opacity:.7-t2*.4}));
                m.position.set(r*Math.cos(angle)+(Math.random()-.5)*.4,(Math.random()-.5)*.25,r*Math.sin(angle)+(Math.random()-.5)*.4);
                g.add(m);
            }
        }
        g.add(new THREE.Mesh(new THREE.SphereGeometry(1,8,8),
            new THREE.MeshBasicMaterial({color:0xaaaaff,transparent:true,opacity:.12,side:THREE.BackSide})));

    } else if (t === 'blackhole') {
        const r = 1.5;
        g.add(new THREE.Mesh(new THREE.SphereGeometry(r,32,32),new THREE.MeshBasicMaterial({color:0x000000})));
        for (let i = 0; i < 7; i++) {
            const inner = r*1.4+i*.35, outer = inner+.3, t2 = i/7;
            const ring = new THREE.Mesh(new THREE.RingGeometry(inner,outer,64),
                new THREE.MeshBasicMaterial({color:new THREE.Color(1-t2*.3,.4-t2*.3,t2*.1),side:THREE.DoubleSide,transparent:true,opacity:.6-t2*.3}));
            ring.rotation.x = Math.PI*.15; ring.userData.rotSpeed = .004-t2*.0004; g.add(ring);
        }
        g.add(new THREE.PointLight(0xff6600,2,20));

    } else if (t === 'universe_edge') {
        g.add(new THREE.Mesh(new THREE.SphereGeometry(5,32,32),
            new THREE.MeshBasicMaterial({color:0x220033,side:THREE.BackSide,transparent:true,opacity:.5})));
        for (let i = 0; i < 600; i++) {
            const theta=Math.random()*Math.PI*2, phi=Math.acos(2*Math.random()-1), r2=2+Math.random()*4;
            const c = Math.random();
            const m = new THREE.Mesh(new THREE.SphereGeometry(.02+Math.random()*.05,4,4),
                new THREE.MeshBasicMaterial({color:new THREE.Color(c*.5,c*.3,c),transparent:true,opacity:.4+Math.random()*.5}));
            m.position.set(r2*Math.sin(phi)*Math.cos(theta),r2*Math.sin(phi)*Math.sin(theta),r2*Math.cos(phi));
            g.add(m);
        }
        for (let i = 0; i < 4; i++) {
            const ring = new THREE.Mesh(new THREE.TorusGeometry(2+i*.6,.05,8,64),
                new THREE.MeshBasicMaterial({color:0xff00ff,transparent:true,opacity:.08-i*.015}));
            ring.rotation.x=Math.random()*Math.PI; ring.rotation.y=Math.random()*Math.PI;
            ring.userData.rotSpeed = .001*(i%2?1:-1); g.add(ring);
        }
        g.add(new THREE.Mesh(new THREE.SphereGeometry(.6,8,8),new THREE.MeshBasicMaterial({color:0xffffff,transparent:true,opacity:.9})));
        g.add(new THREE.PointLight(0xcc00ff,3,30));
    }
    return g;
}

function makeAtmo(r,color) {
    return new THREE.Mesh(new THREE.SphereGeometry(r*1.12,32,32),
        new THREE.MeshPhongMaterial({color,transparent:true,opacity:0.15,side:THREE.BackSide}));
}
function makeGlow(r,color,op) {
    return new THREE.Mesh(new THREE.SphereGeometry(r*1.6,16,16),
        new THREE.MeshBasicMaterial({color,transparent:true,opacity:op,side:THREE.BackSide}));
}

// ═══════════════════════════════════════
//  MOTION SYSTEM
// ═══════════════════════════════════════

// Smoothed values
let smoothX = 0, smoothY = 0;
let rawX = 0, rawY = 0;

// Mouse (desktop)
document.addEventListener('mousemove', (e) => {
    rawX = (e.clientX / window.innerWidth  - 0.5) * 2;
    rawY = (e.clientY / window.innerHeight - 0.5) * 2;
});

// ── Gyroscope / DeviceOrientation ──
let gyroEnabled = false;
let gyroBaseAlpha = null, gyroBaseBeta = null, gyroBaseGamma = null;
let gyroX = 0, gyroY = 0;
let gyroCalibrated = false;

function initGyro() {
    // iOS 13+ needs permission
    if (typeof DeviceOrientationEvent !== 'undefined' &&
        typeof DeviceOrientationEvent.requestPermission === 'function') {
        DeviceOrientationEvent.requestPermission()
            .then(state => {
                if (state === 'granted') startGyro();
            })
            .catch(() => {});
    } else if ('DeviceOrientationEvent' in window) {
        startGyro();
    }
}

function startGyro() {
    window.addEventListener('deviceorientation', onDeviceOrientation, true);
    gyroEnabled = true;
    document.getElementById('motionIndicator').style.display = 'flex';
}

function onDeviceOrientation(e) {
    if (e.beta === null || e.gamma === null) return;

    // Calibrate on first reading
    if (!gyroCalibrated) {
        gyroBaseBeta  = e.beta;
        gyroBaseGamma = e.gamma;
        gyroCalibrated = true;
        return;
    }

    // Delta from calibrated baseline — clamp to ±45°
    const dBeta  = THREE.MathUtils.clamp((e.beta  - gyroBaseBeta)  / 45, -1, 1);
    const dGamma = THREE.MathUtils.clamp((e.gamma - gyroBaseGamma) / 45, -1, 1);

    gyroX = dGamma; // left-right tilt → X
    gyroY = dBeta;  // forward-back  → Y
}

// Recalibrate on tap (resets gyro baseline)
function recalibrateGyro() {
    gyroCalibrated = false;
}

// ── Touch / Swipe ──
let touchStartX = 0, touchStartY = 0, touchT = 0;
let touchActive = false;
let touchMoveX = 0, touchMoveY = 0;

canvas3d.addEventListener('touchstart', (e) => {
    if (e.touches.length !== 1) return;
    touchStartX = e.touches[0].clientX;
    touchStartY = e.touches[0].clientY;
    touchT = Date.now();
    touchActive = true;
    recalibrateGyro();
}, { passive: true });

canvas3d.addEventListener('touchmove', (e) => {
    if (!touchActive || e.touches.length !== 1) return;
    touchMoveX = e.touches[0].clientX;
    touchMoveY = e.touches[0].clientY;
    // Live parallax from touch position
    rawX = (touchMoveX / window.innerWidth  - 0.5) * 2;
    rawY = (touchMoveY / window.innerHeight - 0.5) * 2;
}, { passive: true });

canvas3d.addEventListener('touchend', (e) => {
    if (!touchActive) return;
    touchActive = false;
    const dx = e.changedTouches[0].clientX - touchStartX;
    const dy = e.changedTouches[0].clientY - touchStartY;
    const dt = Date.now() - touchT;
    const dist = Math.sqrt(dx*dx + dy*dy);

    if (dist > 40 && dt < 600) {
        // Swipe
        if (Math.abs(dx) >= Math.abs(dy)) {
            if (dx < -40) nextDest();
            else if (dx > 40) prevDest();
        } else {
            if (dy < -40) nextDest();
            else if (dy > 40) prevDest();
        }
    } else if (dist < 12) {
        // Tap ripple
        spawnRipple(e.changedTouches[0].clientX, e.changedTouches[0].clientY);
    }
}, { passive: true });

// Prevent default scroll on canvas
canvas3d.addEventListener('touchmove', (e) => e.preventDefault(), { passive: false });

// ── Scroll wheel ──
let wheelLock = false;
window.addEventListener('wheel', (e) => {
    if (wheelLock) return;
    wheelLock = true;
    if (e.deltaY > 30) nextDest();
    else if (e.deltaY < -30) prevDest();
    setTimeout(() => wheelLock = false, 900);
}, { passive: true });

// ── Ripple ──
function spawnRipple(x, y) {
    const r = document.createElement('div');
    r.className = 'tap-ripple';
    r.style.left = x + 'px';
    r.style.top  = y + 'px';
    document.body.appendChild(r);
    setTimeout(() => r.remove(), 750);
}

// ═══════════════════════════════════════
//  2D PARTICLE CANVAS
// ═══════════════════════════════════════
const pCanvas = document.getElementById('particleCanvas');
const pCtx    = pCanvas.getContext('2d');
pCanvas.width  = window.innerWidth;
pCanvas.height = window.innerHeight;

const particles = [];

function spawnParticles(n = 50) {
    const cx = window.innerWidth  / 2;
    const cy = window.innerHeight / 2;
    for (let i = 0; i < n; i++) {
        const angle = Math.random() * Math.PI * 2;
        const speed = 1.5 + Math.random() * 5;
        particles.push({
            x: cx, y: cy,
            vx: Math.cos(angle) * speed,
            vy: Math.sin(angle) * speed,
            life: 1,
            decay: 0.014 + Math.random() * 0.018,
            size: 2 + Math.random() * 3,
            hue: 180 + Math.random() * 80
        });
    }
}

function tickParticles() {
    pCtx.clearRect(0, 0, pCanvas.width, pCanvas.height);
    for (let i = particles.length - 1; i >= 0; i--) {
        const p = particles[i];
        p.x += p.vx; p.y += p.vy;
        p.vy += 0.05;
        p.vx *= 0.98;
        p.life -= p.decay;
        if (p.life <= 0) { particles.splice(i, 1); continue; }
        pCtx.save();
        pCtx.globalAlpha = p.life * 0.9;
        pCtx.fillStyle = `hsl(${p.hue},100%,65%)`;
        pCtx.shadowColor = `hsl(${p.hue},100%,65%)`;
        pCtx.shadowBlur  = 6;
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
    setTimeout(() => { if (el.parentNode) el.remove(); }, 2200);
}

// ── Ease ──
function easeOutBack(t) {
    const c1=1.70158, c3=c1+1;
    return 1 + c3*Math.pow(t-1,3) + c1*Math.pow(t-1,2);
}

// ═══════════════════════════════════════
//  STATE & NAVIGATION
// ═══════════════════════════════════════
let currentIndex = -1;
let isTransitioning = false;
let currentObject = null;
let cameraTargetPos  = new THREE.Vector3(0, 2, 8);
let cameraCurrentPos = new THREE.Vector3(0, 2, 8);
let scaleAnimId = null;

// ── Minimap ──
const minimapEl = document.getElementById('minimap');
DESTINATIONS.forEach((d, i) => {
    if (i > 0) {
        const line = document.createElement('div');
        line.className = 'minimap-line';
        minimapEl.appendChild(line);
    }
    const dot = document.createElement('div');
    dot.className = 'minimap-dot';
    dot.dataset.name  = d.name;
    dot.dataset.index = i;

    // Both click and touch
    const go = (e) => {
        e.preventDefault();
        if (!isTransitioning) jumpTo(i);
    };
    dot.addEventListener('click',     go);
    dot.addEventListener('touchend',  go, { passive: false });
    minimapEl.appendChild(dot);
});

function updateMinimap() {
    document.querySelectorAll('.minimap-dot').forEach((dot, i) => {
        dot.classList.remove('active','visited');
        if (i === currentIndex)    dot.classList.add('active');
        else if (i < currentIndex) dot.classList.add('visited');
    });
}

// ── Distance formatter ──
function formatDist(ly) {
    if (ly === 0)    return "0 km";
    if (ly < 0.001)  return (ly * 9.461e12).toExponential(1) + " km";
    if (ly < 1)      return (ly * 63241).toFixed(0) + " AU";
    if (ly < 1000)   return ly.toFixed(2) + " ly";
    if (ly < 1e6)    return (ly/1000).toFixed(1) + "K ly";
    if (ly < 1e9)    return (ly/1e6).toFixed(1) + "M ly";
    return (ly/1e9).toFixed(1) + "B ly";
}

// ── Load destination ──
function loadDestination(index) {
    const d = DESTINATIONS[index];

    // Remove previous
    if (currentObject) { scene.remove(currentObject); currentObject = null; }
    if (scaleAnimId)   { cancelAnimationFrame(scaleAnimId); scaleAnimId = null; }

    // Build & add
    currentObject = makePlanet(d);
    currentObject.scale.setScalar(0.01);
    scene.add(currentObject);

    // HUD updates
    document.getElementById('destName').textContent  = d.name;
    document.getElementById('distValue').textContent = formatDist(d.distance);
    const progress = ((index+1) / DESTINATIONS.length) * 100;
    document.getElementById('progressBar').style.width = progress + '%';
    document.getElementById('stepCounter').textContent = `${index+1} / ${DESTINATIONS.length}`;
    document.getElementById('velocityVal').textContent =
        index===0 ? "0.001 c" : index<4 ? "0.1 c" : index<8 ? "0.9 c" : "99.99% c";
    document.getElementById('infoCategory').textContent = d.category;
    document.getElementById('infoTitle').textContent    = d.name;
    document.getElementById('infoDesc').textContent     = d.desc;
    document.getElementById('statsRow').innerHTML = d.stats.map(s =>
        `<div class="stat-item"><div class="stat-val">${s.v}</div><div class="stat-lbl">${s.l}</div></div>`
    ).join('');

    setTimeout(() => document.getElementById('infoPanel').classList.add('visible'), 300);
    document.getElementById('prevBtn').disabled = (index === 0);

    // Camera distance
    const camZ = ['asteroids','kuiper','oort'].includes(d.type) ? 12 :
                 ['jupiter','saturn'].includes(d.type) ? 10 :
                 ['galaxy_core','galaxy','universe_edge'].includes(d.type) ? 15 : 8;
    cameraTargetPos.set(0, 2, camZ);

    // Scale pop-in animation
    let scaleT = 0;
    const animScale = () => {
        scaleT = Math.min(scaleT + 0.06, 1);
        const s = easeOutBack(scaleT);
        if (currentObject) currentObject.scale.setScalar(Math.max(0.001, s));
        if (scaleT < 1) scaleAnimId = requestAnimationFrame(animScale);
        else scaleAnimId = null;
    };
    scaleAnimId = requestAnimationFrame(animScale);

    showNamePop(d.name);
    spawnParticles(60);
    updateMinimap();
}

// ── Warp transition ──
function warpTo(index) {
    if (isTransitioning) return;
    isTransitioning = true;

    const overlay = document.getElementById('warpOverlay');
    overlay.style.background = 'radial-gradient(ellipse at center, rgba(0,212,255,0.4) 0%, rgba(0,0,30,0.92) 100%)';
    overlay.classList.add('active');
    document.getElementById('infoPanel').classList.remove('visible');

    // Warp stars
    const wGeo = new THREE.BufferGeometry();
    const wPos = new Float32Array(400 * 3);
    for (let i = 0; i < 400; i++) {
        wPos[i*3]   = (Math.random()-.5)*20;
        wPos[i*3+1] = (Math.random()-.5)*10;
        wPos[i*3+2] = (Math.random()-.5)*40;
    }
    wGeo.setAttribute('position', new THREE.BufferAttribute(wPos,3));
    const warpMesh = new THREE.Points(wGeo,
        new THREE.PointsMaterial({color:0x00d4ff,size:.15,transparent:true,opacity:.8}));
    scene.add(warpMesh);

    let wT = 0;
    const step = () => {
        wT += 0.035;
        const arr = warpMesh.geometry.attributes.position.array;
        for (let i = 0; i < arr.length; i+=3) {
            arr[i+2] -= 2.5;
            if (arr[i+2] < -22) arr[i+2] = 22;
        }
        warpMesh.geometry.attributes.position.needsUpdate = true;
        if (wT < 1) { requestAnimationFrame(step); return; }
        scene.remove(warpMesh);
        overlay.style.background = 'radial-gradient(ellipse at center,transparent 0%,rgba(0,0,0,0.5) 100%)';
        loadDestination(index);
        setTimeout(() => { overlay.classList.remove('active'); isTransitioning = false; }, 500);
    };
    requestAnimationFrame(step);
}

function jumpTo(i)  { currentIndex = i; warpTo(i); }
function nextDest() { if (isTransitioning) return; if (currentIndex < DESTINATIONS.length-1) { currentIndex++; warpTo(currentIndex); } else showCompletion(); }
function prevDest() { if (isTransitioning || currentIndex<=0) return; currentIndex--; warpTo(currentIndex); }

function launchMission() {
    document.getElementById('landing').classList.add('hidden');
    document.getElementById('navControls').style.display = 'flex';

    // Mobile extras
    if ('ontouchstart' in window || navigator.maxTouchPoints > 0) {
        const si = document.getElementById('swipeIndicator');
        si.style.display = 'flex';
        setTimeout(() => si.style.display = 'none', 5000);
        initGyro();
    }

    currentIndex = 0;
    loadDestination(0);
}

function showCompletion() {
    document.getElementById('infoPanel').classList.remove('visible');
    document.getElementById('navControls').style.display = 'none';
    spawnParticles(150);
    setTimeout(() => document.getElementById('completion').classList.add('visible'), 500);
}

function restartMission() {
    document.getElementById('completion').classList.remove('visible');
    if (currentObject) { scene.remove(currentObject); currentObject = null; }
    currentIndex = -1;
    document.getElementById('progressBar').style.width = '0%';
    document.getElementById('distValue').textContent = '0 km';
    document.getElementById('destName').textContent  = '— AWAITING LAUNCH —';
    updateMinimap();
    gyroCalibrated = false;
    setTimeout(() => document.getElementById('landing').classList.remove('hidden'), 400);
}

// ═══════════════════════════════════════
//  RENDER LOOP
// ═══════════════════════════════════════
const clock = new THREE.Clock();

function animate() {
    requestAnimationFrame(animate);
    const dt      = clock.getDelta();
    const elapsed = clock.getElapsedTime();

    // Smooth input — blend gyro + touch/mouse
    const inputX = gyroEnabled ? gyroX * 0.7 + rawX * 0.3 : rawX;
    const inputY = gyroEnabled ? gyroY * 0.7 + rawY * 0.3 : rawY;
    smoothX += (inputX - smoothX) * Math.min(1, dt * 5);
    smoothY += (inputY - smoothY) * Math.min(1, dt * 5);

    // Starfield parallax
    starfield.rotation.y += dt * 0.004 + smoothX * 0.0006;
    starfield.rotation.x += dt * 0.002 + smoothY * 0.0004;

    // Object animation
    if (currentObject) {
        // Spin
        currentObject.rotation.y += dt * 0.3;

        // Tilt from motion input
        currentObject.rotation.x += (smoothY * 0.25 - currentObject.rotation.x) * Math.min(1, dt * 3);
        currentObject.rotation.z += (-smoothX * 0.15 - currentObject.rotation.z) * Math.min(1, dt * 3);

        // Floating bob
        currentObject.position.y = Math.sin(elapsed * 0.7) * 0.14;

        // Sub-object animations
        currentObject.children.forEach(child => {
            if (child.userData.rotSpeed) {
                child.rotation.y += child.userData.rotSpeed;
                if (child.rotation) child.rotation.z += child.userData.rotSpeed * 0.5;
            }
            if (child.userData.orbitSpeed !== undefined) {
                child.userData.orbitAngle += child.userData.orbitSpeed;
                const r = child.userData.orbitR;
                child.position.x = Math.cos(child.userData.orbitAngle) * r;
                child.position.z = Math.sin(child.userData.orbitAngle) * r;
                if (child.userData.orbitY !== undefined)
                    child.position.y = child.userData.orbitY;
            }
        });
    }

    // Camera — smooth follow + parallax
    cameraCurrentPos.lerp(cameraTargetPos, Math.min(1, dt * 2));
    camera.position.set(
        cameraCurrentPos.x + smoothX * 1.0 + Math.sin(elapsed * 0.25) * 0.15,
        cameraCurrentPos.y + smoothY * 0.6 + Math.cos(elapsed * 0.18) * 0.1,
        cameraCurrentPos.z
    );
    camera.lookAt(0, 0, 0);

    tickParticles();
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
</script>
</body>
</html>
""", height=850, scrolling=False)