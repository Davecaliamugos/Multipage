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

st.markdown("""
<style>
/* Sidebar text colors - from games.py */
.stApp, .stApp * { color: #e5e7eb; }
[data-testid="stSidebar"] .block-container { color: #e5e7eb !important; }
[data-testid="stSidebar"] p, [data-testid="stSidebar"] span,
[data-testid="stSidebar"] a, [data-testid="stSidebar"] div { color: #e5e7eb !important; }
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 { color: #e5e7eb !important; }
</style>
""", unsafe_allow_html=True)

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

*,*::before,*::after{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent;-webkit-touch-callout:none;}
html{height:100%;overflow:hidden;}
body{
  background:#000;overflow:hidden;font-family:'Inter',sans-serif;color:#fff;
  width:100%;height:100%;position:fixed;top:0;left:0;
  touch-action:none;user-select:none;-webkit-user-select:none;
}

#canvas3d{position:fixed;top:0;left:0;width:100%;height:100%;z-index:0;touch-action:none;}
#particleCanvas{position:fixed;top:0;left:0;width:100%;height:100%;z-index:5;pointer-events:none;}
#portalCanvas{position:fixed;top:0;left:0;width:100%;height:100%;z-index:280;pointer-events:none;display:none;}

#fsBtn{
  position:fixed;top:12px;right:52px;z-index:500;
  font-family:'Orbitron',monospace;font-size:0.55rem;font-weight:700;
  letter-spacing:2px;text-transform:uppercase;color:#00d4ff;
  background:rgba(0,0,0,0.7);border:1px solid rgba(0,212,255,0.4);
  padding:7px 14px;border-radius:4px;cursor:pointer;
  transition:all 0.2s;touch-action:manipulation;
  backdrop-filter:blur(10px);
  display:flex;align-items:center;gap:6px;
}
#fsBtn:hover,#fsBtn:active{background:rgba(0,212,255,0.15);border-color:#00d4ff;box-shadow:0 0 15px rgba(0,212,255,0.4);}
#fsBtn svg{width:14px;height:14px;fill:currentColor;}

/* Gyro permission button */
#gyroBtn{
  position:fixed;top:12px;right:160px;z-index:500;
  font-family:'Orbitron',monospace;font-size:0.55rem;font-weight:700;
  letter-spacing:2px;text-transform:uppercase;color:#34d399;
  background:rgba(0,0,0,0.7);border:1px solid rgba(52,211,153,0.4);
  padding:7px 14px;border-radius:4px;cursor:pointer;
  transition:all 0.2s;touch-action:manipulation;
  backdrop-filter:blur(10px);
  display:none;align-items:center;gap:6px;
}
#gyroBtn:active{background:rgba(52,211,153,0.15);}

#hud{position:fixed;top:0;left:0;right:0;z-index:100;pointer-events:none;}
.top-bar{
  display:flex;align-items:center;justify-content:space-between;
  padding:clamp(8px,2vw,14px) clamp(12px,3vw,24px);
  padding-right:clamp(80px,12vw,120px);
  background:linear-gradient(180deg,rgba(0,0,0,0.9) 0%,transparent 100%);
  gap:8px;
}
.mission-title{
  font-family:'Orbitron',monospace;font-size:clamp(0.48rem,1.8vw,0.9rem);
  font-weight:700;color:#00d4ff;letter-spacing:clamp(1px,0.4vw,3px);
  text-transform:uppercase;text-shadow:0 0 20px rgba(0,212,255,0.8);
  white-space:nowrap;flex-shrink:0;
}
.top-center{display:flex;flex-direction:column;align-items:center;gap:3px;flex:1;min-width:0;padding:0 8px;}
.destination-label{font-family:'Orbitron',monospace;font-size:clamp(0.38rem,1.1vw,0.6rem);color:#9ca3af;letter-spacing:2px;text-transform:uppercase;}
.destination-name{
  font-family:'Orbitron',monospace;font-size:clamp(0.62rem,2.2vw,1rem);
  font-weight:900;color:#fff;text-shadow:0 0 30px rgba(255,255,255,0.5);
  transition:all 0.4s ease;text-align:center;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis;width:100%;
}
.velocity-box{font-family:'Orbitron',monospace;font-size:clamp(0.48rem,1.4vw,0.7rem);color:#34d399;text-align:right;letter-spacing:1px;white-space:nowrap;flex-shrink:0;}
.progress-track{margin:0 clamp(12px,3vw,24px);height:2px;background:rgba(255,255,255,0.08);border-radius:2px;overflow:visible;position:relative;}
.progress-glow{height:100%;background:linear-gradient(90deg,#3b82f6,#8b5cf6,#ec4899,#f59e0b);border-radius:2px;transition:width 0.8s cubic-bezier(0.4,0,0.2,1);position:relative;box-shadow:0 0 12px rgba(0,212,255,0.6);}
.progress-dot{position:absolute;right:-5px;top:-4px;width:10px;height:10px;background:#fff;border-radius:50%;box-shadow:0 0 10px #00d4ff,0 0 20px #00d4ff;}

.distance-hud{position:fixed;top:clamp(56px,9vw,82px);left:clamp(12px,3vw,24px);z-index:100;font-family:'Orbitron',monospace;}
.dist-label{font-size:clamp(0.38rem,1.1vw,0.52rem);color:#6b7280;letter-spacing:2px;text-transform:uppercase;margin-bottom:2px;}
.dist-value{font-size:clamp(0.82rem,2.8vw,1.3rem);font-weight:700;color:#00d4ff;text-shadow:0 0 20px rgba(0,212,255,0.5);transition:all 0.5s ease;}

#infoPanel{
  position:fixed;bottom:clamp(86px,14vw,105px);left:clamp(12px,3vw,24px);
  z-index:100;width:min(310px,calc(100vw - 48px));
  background:rgba(3,8,20,0.94);
  border:1px solid rgba(0,212,255,0.22);border-left:3px solid #00d4ff;
  border-radius:0 14px 14px 0;
  padding:clamp(12px,2.5vw,18px) clamp(14px,3vw,20px);
  backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);
  transform:translateX(-120%);transition:transform 0.7s cubic-bezier(0.4,0,0.2,1);
  pointer-events:none;
  box-shadow:0 0 40px rgba(0,212,255,0.08),inset 0 0 20px rgba(0,212,255,0.02);
}
#infoPanel.visible{transform:translateX(0);}
.info-category{font-family:'Orbitron',monospace;font-size:clamp(0.38rem,1.2vw,0.52rem);color:#00d4ff;letter-spacing:3px;text-transform:uppercase;margin-bottom:5px;}
.info-title{font-family:'Orbitron',monospace;font-size:clamp(0.82rem,2.8vw,1.2rem);font-weight:900;color:#fff;margin-bottom:7px;line-height:1.2;}
.info-desc{font-size:clamp(0.68rem,1.7vw,0.8rem);color:#9ca3af;line-height:1.6;margin-bottom:11px;display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden;}
.stats-row{display:grid;grid-template-columns:1fr 1fr;gap:5px;}
.stat-item{background:rgba(0,212,255,0.06);border:1px solid rgba(0,212,255,0.14);border-radius:8px;padding:6px 8px;}
.stat-val{font-family:'Orbitron',monospace;font-size:clamp(0.58rem,1.7vw,0.8rem);font-weight:700;color:#00d4ff;}
.stat-lbl{font-size:clamp(0.48rem,1.2vw,0.62rem);color:#6b7280;text-transform:uppercase;letter-spacing:0.5px;margin-top:2px;}

#navControls{
  position:fixed;bottom:clamp(14px,3.5vw,26px);left:50%;
  transform:translateX(-50%);z-index:200;
  display:flex;align-items:center;gap:clamp(8px,2vw,14px);
}
.nav-btn{
  padding:clamp(11px,2.5vw,13px) clamp(18px,4vw,28px);
  font-family:'Orbitron',monospace;font-size:clamp(0.56rem,1.7vw,0.72rem);
  font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#fff;
  background:rgba(3,8,20,0.92);border:1px solid rgba(0,212,255,0.4);
  border-radius:4px;cursor:pointer;transition:all 0.2s;
  touch-action:manipulation;white-space:nowrap;min-height:44px;min-width:44px;
}
.nav-btn:active{background:rgba(0,212,255,0.15);border-color:#00d4ff;box-shadow:0 0 25px rgba(0,212,255,0.5);transform:scale(0.95);}
.nav-btn:disabled{opacity:0.3;pointer-events:none;}
.nav-btn.primary{background:linear-gradient(135deg,rgba(0,212,255,0.18),rgba(139,92,246,0.18));border-color:#00d4ff;box-shadow:0 0 20px rgba(0,212,255,0.2);}
.step-counter{font-family:'Orbitron',monospace;font-size:clamp(0.52rem,1.4vw,0.68rem);color:#9ca3af;letter-spacing:2px;min-width:52px;text-align:center;}

#minimap{position:fixed;right:clamp(10px,2vw,20px);top:50%;transform:translateY(-50%);z-index:100;display:flex;flex-direction:column;align-items:center;}
.minimap-line{width:1px;height:clamp(12px,2.2vw,20px);background:rgba(255,255,255,0.1);}
.minimap-dot{border-radius:50%;cursor:pointer;transition:all 0.3s;touch-action:manipulation;min-width:22px;min-height:22px;display:flex;align-items:center;justify-content:center;}
.minimap-dot::before{content:'';width:clamp(5px,1.3vw,7px);height:clamp(5px,1.3vw,7px);border-radius:50%;background:rgba(255,255,255,0.2);border:1px solid rgba(255,255,255,0.15);display:block;transition:all 0.3s;}
.minimap-dot.active::before{background:#00d4ff;border-color:#00d4ff;box-shadow:0 0 12px #00d4ff,0 0 24px rgba(0,212,255,0.5);}
.minimap-dot.visited::before{background:rgba(0,212,255,0.4);border-color:rgba(0,212,255,0.4);}

#swipeIndicator{
  position:fixed;bottom:clamp(72px,11vw,86px);left:50%;transform:translateX(-50%);
  z-index:150;display:none;flex-direction:row;align-items:center;gap:14px;
  font-family:'Orbitron',monospace;font-size:0.52rem;color:rgba(0,212,255,0.5);
  letter-spacing:2px;text-transform:uppercase;white-space:nowrap;
  animation:swipePulse 2s ease-in-out infinite;
}
@keyframes swipePulse{0%,100%{opacity:0.3}50%{opacity:1}}

#motionIndicator{position:fixed;top:clamp(56px,9vw,82px);right:clamp(52px,8vw,72px);z-index:100;display:none;flex-direction:column;align-items:center;gap:4px;}
.motion-dot{width:6px;height:6px;border-radius:50%;background:#00d4ff;box-shadow:0 0 6px #00d4ff;animation:motionPulse 1s ease-in-out infinite;}
@keyframes motionPulse{0%,100%{transform:scale(1);opacity:0.6}50%{transform:scale(1.4);opacity:1}}
.motion-label{font-family:'Orbitron',monospace;font-size:0.42rem;color:rgba(0,212,255,0.6);letter-spacing:1px;text-transform:uppercase;}

#landing{
  position:fixed;inset:0;z-index:500;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  background:radial-gradient(ellipse at center,rgba(0,15,35,0.97) 0%,rgba(0,0,0,1) 100%);
  transition:opacity 0.9s ease,visibility 0.9s;
  padding:clamp(16px,5vw,40px);text-align:center;
}
#landing.hidden{opacity:0;visibility:hidden;pointer-events:none;}
.landing-badge{font-family:'Orbitron',monospace;font-size:clamp(0.46rem,1.4vw,0.58rem);letter-spacing:5px;color:#00d4ff;text-transform:uppercase;margin-bottom:clamp(14px,3.5vw,28px);opacity:0.8;}
.landing-title{font-family:'Orbitron',monospace;font-size:clamp(2rem,9.5vw,5rem);font-weight:900;line-height:1.0;margin-bottom:clamp(10px,2.5vw,18px);background:linear-gradient(135deg,#fff 0%,#00d4ff 35%,#8b5cf6 65%,#ff6bcb 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;filter:drop-shadow(0 0 30px rgba(0,212,255,0.3));}
.landing-sub{font-size:clamp(0.75rem,2.3vw,0.96rem);color:#6b7280;max-width:440px;line-height:1.7;margin-bottom:clamp(26px,5.5vw,46px);}
.launch-btn{font-family:'Orbitron',monospace;font-size:clamp(0.66rem,1.9vw,0.82rem);font-weight:700;letter-spacing:4px;text-transform:uppercase;color:#000;background:linear-gradient(135deg,#00d4ff,#8b5cf6);border:none;padding:clamp(13px,3.5vw,16px) clamp(26px,6.5vw,46px);border-radius:4px;cursor:pointer;transition:all 0.3s;touch-action:manipulation;min-height:48px;box-shadow:0 0 30px rgba(0,212,255,0.3);}
.launch-btn:active{transform:scale(0.96);box-shadow:0 0 50px rgba(0,212,255,0.6);}
.scroll-hint{position:absolute;bottom:clamp(18px,3.5vw,36px);font-family:'Orbitron',monospace;font-size:clamp(0.42rem,1.1vw,0.56rem);letter-spacing:2px;color:#374151;text-transform:uppercase;animation:pulse 2s ease-in-out infinite;}
@keyframes pulse{0%,100%{opacity:.4}50%{opacity:1}}

#completion{
  position:fixed;inset:0;z-index:500;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  background:radial-gradient(ellipse at center,rgba(0,10,30,0.98) 0%,rgba(0,0,0,1) 100%);
  opacity:0;visibility:hidden;transition:all 0.8s ease;
  padding:clamp(16px,5vw,40px);text-align:center;
}
#completion.visible{opacity:1;visibility:visible;}
.complete-label{font-family:'Orbitron',monospace;font-size:clamp(0.46rem,1.4vw,0.58rem);letter-spacing:6px;color:#34d399;text-transform:uppercase;margin-bottom:clamp(10px,2.5vw,18px);}
.complete-title{font-family:'Orbitron',monospace;font-size:clamp(1.5rem,5.5vw,3.2rem);font-weight:900;margin-bottom:clamp(9px,2vw,14px);background:linear-gradient(135deg,#34d399,#00d4ff,#8b5cf6,#ff6bcb);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.complete-dist{font-family:'Orbitron',monospace;font-size:clamp(1rem,3.8vw,1.9rem);font-weight:900;color:#00d4ff;text-shadow:0 0 30px rgba(0,212,255,0.5);margin-bottom:9px;}
.complete-text{font-size:clamp(0.7rem,1.9vw,0.88rem);color:#6b7280;max-width:480px;line-height:1.8;margin-bottom:clamp(22px,4.5vw,36px);}
.restart-btn{font-family:'Orbitron',monospace;font-size:clamp(0.6rem,1.7vw,0.72rem);font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#fff;background:transparent;border:1px solid rgba(0,212,255,0.5);padding:clamp(11px,2.5vw,14px) clamp(20px,4.5vw,36px);border-radius:4px;cursor:pointer;transition:all 0.2s;touch-action:manipulation;min-height:44px;}
.restart-btn:active{background:rgba(0,212,255,0.1);border-color:#00d4ff;box-shadow:0 0 20px rgba(0,212,255,0.3);}

#warpOverlay{position:fixed;inset:0;z-index:270;pointer-events:none;opacity:0;transition:opacity 0.15s;}
#warpOverlay.active{opacity:1;}

.scanlines{position:fixed;inset:0;z-index:50;background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,0,0,0.025) 2px,rgba(0,0,0,0.025) 4px);pointer-events:none;}
.corner{position:fixed;z-index:100;width:clamp(20px,4.5vw,36px);height:clamp(20px,4.5vw,36px);pointer-events:none;}
.corner-tl{top:8px;left:8px;border-top:1px solid rgba(0,212,255,0.5);border-left:1px solid rgba(0,212,255,0.5);}
.corner-tr{top:8px;right:8px;border-top:1px solid rgba(0,212,255,0.5);border-right:1px solid rgba(0,212,255,0.5);}
.corner-bl{bottom:8px;left:8px;border-bottom:1px solid rgba(0,212,255,0.5);border-left:1px solid rgba(0,212,255,0.5);}
.corner-br{bottom:8px;right:8px;border-bottom:1px solid rgba(0,212,255,0.5);border-right:1px solid rgba(0,212,255,0.5);}

@keyframes namePop{
  0%{opacity:0;transform:translate(-50%,-50%) scale(0.5) translateY(20px);}
  25%{opacity:1;transform:translate(-50%,-50%) scale(1.06) translateY(0);}
  75%{opacity:1;transform:translate(-50%,-50%) scale(1) translateY(0);}
  100%{opacity:0;transform:translate(-50%,-50%) scale(0.95) translateY(-8px);}
}
.name-pop{
  position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);
  z-index:250;font-family:'Orbitron',monospace;
  font-size:clamp(1.1rem,4.5vw,2.8rem);font-weight:900;color:#fff;
  text-shadow:0 0 40px rgba(0,212,255,1),0 0 80px rgba(139,92,246,0.8);
  pointer-events:none;animation:namePop 2.2s cubic-bezier(0.4,0,0.2,1) forwards;
  white-space:nowrap;text-align:center;
}

@keyframes rippleOut{0%{width:0;height:0;opacity:0.9;}100%{width:120px;height:120px;opacity:0;}}
.tap-ripple{
  position:fixed;border-radius:50%;
  background:radial-gradient(circle,rgba(0,212,255,0.4),transparent);
  pointer-events:none;z-index:400;transform:translate(-50%,-50%);
  animation:rippleOut 0.8s ease-out forwards;
}
</style>
</head>
<body>

<canvas id="canvas3d"></canvas>
<canvas id="particleCanvas"></canvas>
<canvas id="portalCanvas"></canvas>
<div class="scanlines"></div>
<div class="corner corner-tl"></div>
<div class="corner corner-tr"></div>
<div class="corner corner-bl"></div>
<div class="corner corner-br"></div>
<div id="warpOverlay"></div>

<button id="fsBtn" onclick="toggleFullscreen()" title="Fullscreen">
  <svg id="fsIcon" viewBox="0 0 24 24"><path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/></svg>
  <span id="fsLabel">FULL</span>
</button>

<!-- Gyro permission button (iOS) -->
<button id="gyroBtn" onclick="requestGyroPermission()" title="Enable Gyroscope">
  📱 GYRO
</button>

<div id="hud">
  <div class="top-bar">
    <div class="mission-title">GALAXY EXPLORER</div>
    <div class="top-center">
      <div class="destination-label">Current Destination</div>
      <div class="destination-name" id="destName">— AWAITING LAUNCH —</div>
    </div>
    <div class="velocity-box">
      <div style="font-size:clamp(0.38rem,1.1vw,0.52rem);color:#6b7280;letter-spacing:2px;margin-bottom:2px;">VELOCITY</div>
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

<div id="motionIndicator">
  <div class="motion-dot"></div>
  <div class="motion-label">TILT</div>
</div>

<div id="infoPanel">
  <div class="info-category" id="infoCategory">SOLAR SYSTEM</div>
  <div class="info-title" id="infoTitle">Earth</div>
  <div class="info-desc" id="infoDesc">Our pale blue dot.</div>
  <div class="stats-row" id="statsRow"></div>
</div>

<div id="minimap"></div>

<div id="swipeIndicator">
  <span>←</span> SWIPE TO NAVIGATE <span>→</span>
</div>

<div id="navControls" style="display:none;">
  <button class="nav-btn" id="prevBtn" ontouchend="handlePrev(event)" onclick="prevDest()" disabled>◀ PREV</button>
  <div class="step-counter" id="stepCounter">0 / 14</div>
  <button class="nav-btn primary" id="nextBtn" ontouchend="handleNext(event)" onclick="nextDest()">NEXT ▶</button>
</div>

<div id="landing">
  <div class="landing-badge">Deep Space Mission — 2025</div>
  <h1 class="landing-title">GALAXY<br>EXPLORER</h1>
  <p class="landing-sub">A photorealistic 3D journey from Earth to the edge of the observable universe. 46.5 billion light-years of cosmic wonder await.</p>
  <button class="launch-btn" ontouchend="handleLaunch(event)" onclick="launchMission()">INITIATE LAUNCH</button>
  <div class="scroll-hint">Swipe ← → or use buttons to navigate</div>
</div>

<div id="completion">
  <div class="complete-label">Mission Complete</div>
  <div class="complete-title">EDGE OF THE<br>UNIVERSE REACHED</div>
  <div class="complete-dist">46.5 Billion Light-Years</div>
  <p class="complete-text">You have traversed the full breadth of the observable universe. The universe is 13.8 billion years old and still expanding.</p>
  <button class="restart-btn" ontouchend="handleRestart(event)" onclick="restartMission()">RESTART MISSION</button>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
'use strict';

/* ══════════════════════════════════════════
   FULLSCREEN
══════════════════════════════════════════ */
let isFS = false;
function toggleFullscreen(){
  if(!document.fullscreenElement && !document.webkitFullscreenElement){
    const el = document.documentElement;
    if(el.requestFullscreen) el.requestFullscreen();
    else if(el.webkitRequestFullscreen) el.webkitRequestFullscreen();
    isFS = true;
  } else {
    if(document.exitFullscreen) document.exitFullscreen();
    else if(document.webkitExitFullscreen) document.webkitExitFullscreen();
    isFS = false;
  }
}
document.addEventListener('fullscreenchange', updateFsBtn);
document.addEventListener('webkitfullscreenchange', updateFsBtn);
function updateFsBtn(){
  const icon = document.getElementById('fsIcon');
  const lbl  = document.getElementById('fsLabel');
  const btn  = document.getElementById('fsBtn');
  if(document.fullscreenElement || document.webkitFullscreenElement){
    icon.innerHTML = '<path d="M5 16h3v3h2v-5H5v2zm3-8H5v2h5V5H8v3zm6 11h2v-3h3v-2h-5v5zm2-11V5h-2v5h5V8h-3z"/>';
    lbl.textContent = 'EXIT';
    btn.style.borderColor = 'rgba(255,100,100,0.5)';
    btn.style.color = '#ff6464';
  } else {
    icon.innerHTML = '<path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/>';
    lbl.textContent = 'FULL';
    btn.style.borderColor = 'rgba(0,212,255,0.4)';
    btn.style.color = '#00d4ff';
  }
}

/* ══════════════════════════════════════════
   GYROSCOPE — FIXED FOR iOS + ANDROID
══════════════════════════════════════════ */
let gyroEnabled = false;
let gyroX = 0, gyroY = 0;
let gyroCalibrated = false;
let gyroBaseBeta = 0, gyroBaseGamma = 0;
let gyroAlpha = 0; // smoothed

// Check if we need permission (iOS 13+)
function checkGyroSupport(){
  const isTouch = ('ontouchstart' in window) || navigator.maxTouchPoints > 0;
  if(!isTouch) return;

  if(typeof DeviceOrientationEvent !== 'undefined' &&
     typeof DeviceOrientationEvent.requestPermission === 'function'){
    // iOS 13+ — show button, need user gesture
    document.getElementById('gyroBtn').style.display = 'flex';
  } else if('DeviceOrientationEvent' in window){
    // Android / older iOS — start directly
    startGyro();
  }
}

function requestGyroPermission(){
  if(typeof DeviceOrientationEvent.requestPermission === 'function'){
    DeviceOrientationEvent.requestPermission()
      .then(state => {
        if(state === 'granted'){
          startGyro();
          document.getElementById('gyroBtn').style.display = 'none';
          document.getElementById('motionIndicator').style.display = 'flex';
        } else {
          alert('Gyroscope permission denied. Tilt controls unavailable.');
        }
      })
      .catch(err => {
        console.warn('Gyro permission error:', err);
        // Try starting anyway
        startGyro();
        document.getElementById('gyroBtn').style.display = 'none';
      });
  } else {
    startGyro();
    document.getElementById('gyroBtn').style.display = 'none';
  }
}

function startGyro(){
  window.addEventListener('deviceorientation', onDeviceOrientation, true);
  gyroEnabled = true;
  document.getElementById('motionIndicator').style.display = 'flex';
}

function onDeviceOrientation(e){
  if(e.beta === null || e.gamma === null) return;

  // Auto-calibrate on first reading
  if(!gyroCalibrated){
    gyroBaseBeta  = e.beta;
    gyroBaseGamma = e.gamma;
    gyroCalibrated = true;
    return;
  }

  // Normalize: gamma = left/right tilt, beta = forward/back tilt
  // Handle landscape orientation
  const orient = window.screen && window.screen.orientation
    ? window.screen.orientation.angle
    : (window.orientation || 0);

  let rawX, rawY;
  if(Math.abs(orient) === 90){
    // Landscape
    rawX = THREE.MathUtils.clamp((e.beta  - gyroBaseBeta)  / 40, -1, 1);
    rawY = THREE.MathUtils.clamp((e.gamma - gyroBaseGamma) / 40, -1, 1);
  } else {
    // Portrait
    rawX = THREE.MathUtils.clamp((e.gamma - gyroBaseGamma) / 40, -1, 1);
    rawY = THREE.MathUtils.clamp((e.beta  - gyroBaseBeta)  / 40, -1, 1);
  }

  // Smooth gyro output
  gyroX += (rawX - gyroX) * 0.15;
  gyroY += (rawY - gyroY) * 0.15;
}

function recalibrateGyro(){ gyroCalibrated = false; }

// Call on page load
checkGyroSupport();

/* ══════════════════════════════════════════
   TOUCH HANDLERS
══════════════════════════════════════════ */
function handleNext(e)    { e.preventDefault(); e.stopPropagation(); nextDest(); }
function handlePrev(e)    { e.preventDefault(); e.stopPropagation(); prevDest(); }
function handleLaunch(e)  { e.preventDefault(); e.stopPropagation(); launchMission(); }
function handleRestart(e) { e.preventDefault(); e.stopPropagation(); restartMission(); }

/* ══════════════════════════════════════════
   DESTINATIONS
══════════════════════════════════════════ */
const DESTINATIONS = [
  { name:"Earth",           category:"SOLAR SYSTEM — INNER",    desc:"Our pale blue dot — the only known harbor of life. Oceans cover 71% of its surface. A thin atmosphere shields 8 billion lives from the void.",              distance:0,           type:"earth",        accentColor:"#1d6fa4", stats:[{v:"12,742 km",l:"Diameter"},{v:"1 AU",l:"From Sun"},{v:"4.5B yrs",l:"Age"},{v:"7.9B",l:"Population"}] },
  { name:"The Moon",        category:"EARTH SYSTEM",             desc:"Earth's ancient companion, sculpted by billions of years of impacts. 384,400 km away — humanity's first step into the cosmos.",                             distance:0.0000016,   type:"moon",         accentColor:"#9ca3af", stats:[{v:"3,474 km",l:"Diameter"},{v:"27.3 days",l:"Orbit"},{v:"-173°C",l:"Min Temp"},{v:"127°C",l:"Max Temp"}] },
  { name:"Mars",            category:"SOLAR SYSTEM — INNER",    desc:"The Red Planet. Olympus Mons stands 22 km tall. Ancient riverbeds hint at a wetter past. Humanity's next frontier.",                                        distance:0.000042,    type:"mars",         accentColor:"#c1440e", stats:[{v:"6,779 km",l:"Diameter"},{v:"1.5 AU",l:"From Sun"},{v:"687 days",l:"Year"},{v:"-80°C",l:"Avg Temp"}] },
  { name:"Jupiter",         category:"SOLAR SYSTEM — OUTER",    desc:"The solar system's titan. The Great Red Spot — a storm three times Earth's size — has raged for 350+ years. 95 moons orbit its crushing gravity.",           distance:0.00052,     type:"jupiter",      accentColor:"#c88b3a", stats:[{v:"139,820 km",l:"Diameter"},{v:"5.2 AU",l:"From Sun"},{v:"95 moons",l:"Satellites"},{v:"11.9 yrs",l:"Year"}] },
  { name:"Saturn",          category:"SOLAR SYSTEM — OUTER",    desc:"The jewel of the solar system. Rings spanning 282,000 km yet barely 10 meters thick — ice and rock in perfect gravitational harmony.",                        distance:0.0010,      type:"saturn",       accentColor:"#e8c97a", stats:[{v:"116,460 km",l:"Diameter"},{v:"9.5 AU",l:"From Sun"},{v:"146 moons",l:"Satellites"},{v:"0.687",l:"Density g/cm³"}] },
  { name:"Uranus",          category:"SOLAR SYSTEM — OUTER",    desc:"The tilted ice giant, rolling on its side at 98°. Methane absorbs red light, giving it an ethereal cyan hue.",                                              distance:0.0019,      type:"uranus",       accentColor:"#4fd1c5", stats:[{v:"50,724 km",l:"Diameter"},{v:"19.2 AU",l:"From Sun"},{v:"98°",l:"Axial Tilt"},{v:"-224°C",l:"Avg Temp"}] },
  { name:"Neptune",         category:"SOLAR SYSTEM — OUTER",    desc:"The windiest world known — gusts reach 2,100 km/h. Its moon Triton orbits backwards, slowly spiraling toward a catastrophic end.",                           distance:0.0030,      type:"neptune",      accentColor:"#2b4eff", stats:[{v:"49,244 km",l:"Diameter"},{v:"30.1 AU",l:"From Sun"},{v:"2,100 km/h",l:"Winds"},{v:"-214°C",l:"Avg Temp"}] },
  { name:"Oort Cloud",      category:"SOLAR SYSTEM BOUNDARY",   desc:"A vast spherical shell of trillions of icy bodies, stretching up to 2 light-years from the Sun. Origin of long-period comets.",                             distance:0.5,         type:"oort",         accentColor:"#a0c4ff", stats:[{v:"1-2 ly",l:"Thickness"},{v:"Trillions",l:"Icy Bodies"},{v:"100,000 AU",l:"Max Dist"},{v:"-270°C",l:"Temp"}] },
  { name:"Proxima Centauri",category:"INTERSTELLAR SPACE",      desc:"Our nearest stellar neighbor — a red dwarf 4.24 ly away. Proxima b orbits in the habitable zone, but fierce flares may strip away any atmosphere.",          distance:4.24,        type:"star",         accentColor:"#ff6b35", stats:[{v:"Red Dwarf",l:"Type"},{v:"4.24 ly",l:"Distance"},{v:"Proxima b",l:"Exoplanet"},{v:"2,700°C",l:"Surface"}] },
  { name:"Galactic Center", category:"MILKY WAY",               desc:"Sagittarius A* — 4 million solar masses compressed into a singularity. Stars orbit at 30 million km/h. The beating heart of our galaxy.",                   distance:26000,       type:"galaxy_core",  accentColor:"#ffd700", stats:[{v:"4M × Sun",l:"BH Mass"},{v:"26,000 ly",l:"Distance"},{v:"200-400B",l:"Stars"},{v:"100,000 ly",l:"Diameter"}] },
  { name:"Andromeda Galaxy",category:"LOCAL GROUP",              desc:"2.5 million light-years away yet visible to the naked eye. One trillion stars. Racing toward us at 110 km/s — collision in 4.5 billion years.",              distance:2537000,     type:"galaxy",       accentColor:"#c8b8ff", stats:[{v:"1 trillion",l:"Stars"},{v:"2.5M ly",l:"Distance"},{v:"220,000 ly",l:"Diameter"},{v:"110 km/s",l:"Approach"}] },
  { name:"TON 618",         category:"DEEP UNIVERSE",           desc:"A hyperluminous quasar — 66 billion solar masses. Its event horizon is larger than our entire solar system. Outshines 140 trillion suns.",                  distance:55000000,    type:"blackhole",    accentColor:"#8b00ff", stats:[{v:"66B × Sun",l:"Mass"},{v:"10.4B ly",l:"Distance"},{v:"1,300 AU",l:"Radius"},{v:"140T × Sun",l:"Luminosity"}] },
  { name:"Cosmic Web",      category:"LARGE SCALE STRUCTURE",   desc:"The universe's skeleton — vast filaments of dark matter and galaxies stretching billions of light-years, surrounding enormous cosmic voids.",                 distance:1000000000,  type:"cosmic_web",   accentColor:"#ff6bcb", stats:[{v:"Filaments",l:"Structure"},{v:"~100M ly",l:"Void Size"},{v:"Dark Matter",l:"Scaffold"},{v:"Billions",l:"Galaxies"}] },
  { name:"Edge of Universe",category:"COSMIC HORIZON",          desc:"The observable universe's boundary — 46.5 billion light-years. Beyond this horizon, light hasn't had time to reach us since the Big Bang.",                   distance:46500000000, type:"universe_edge", accentColor:"#ff00ff", stats:[{v:"46.5B ly",l:"Radius"},{v:"93B ly",l:"Diameter"},{v:"2 Trillion",l:"Galaxies"},{v:"∞",l:"Beyond"}] },
];

/* ══════════════════════════════════════════
   THREE.JS SETUP
══════════════════════════════════════════ */
const canvas3d = document.getElementById('canvas3d');
const renderer = new THREE.WebGLRenderer({canvas:canvas3d,antialias:true,alpha:false,powerPreference:'high-performance'});
renderer.setPixelRatio(Math.min(window.devicePixelRatio,2));
renderer.setSize(window.innerWidth,window.innerHeight);
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.0;
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x000005);
scene.fog = new THREE.FogExp2(0x000008,0.006);

const camera = new THREE.PerspectiveCamera(60,window.innerWidth/window.innerHeight,0.01,8000);
camera.position.set(0,2,10);

scene.add(new THREE.AmbientLight(0x111133,0.8));
const sunLight = new THREE.PointLight(0xfff5e0,4,200);
sunLight.position.set(15,15,15); sunLight.castShadow=true; scene.add(sunLight);
const rimLight = new THREE.DirectionalLight(0x0033ff,0.4);
rimLight.position.set(-8,4,-8); scene.add(rimLight);

/* ══════════════════════════════════════════
   TEXTURE HELPERS
══════════════════════════════════════════ */
function makeTex(size,fn){
  const c=document.createElement('canvas'); c.width=c.height=size;
  fn(c.getContext('2d'),size);
  return new THREE.CanvasTexture(c);
}

// Circular sprite texture for Points (fixes the square particle bug)
function makeCircleSprite(){
  const c = document.createElement('canvas'); c.width = c.height = 64;
  const ctx = c.getContext('2d');
  const grad = ctx.createRadialGradient(32,32,0,32,32,32);
  grad.addColorStop(0,'rgba(255,255,255,1)');
  grad.addColorStop(0.4,'rgba(255,255,255,0.8)');
  grad.addColorStop(1,'rgba(255,255,255,0)');
  ctx.fillStyle = grad;
  ctx.beginPath(); ctx.arc(32,32,32,0,Math.PI*2); ctx.fill();
  return new THREE.CanvasTexture(c);
}
const circleSprite = makeCircleSprite();

const earthTex = makeTex(512,(ctx,s)=>{
  const g=ctx.createRadialGradient(s/2,s/2,0,s/2,s/2,s/2);
  g.addColorStop(0,'#1a5276');g.addColorStop(1,'#0d2b45');
  ctx.fillStyle=g;ctx.fillRect(0,0,s,s);
  ctx.fillStyle='#2d7d32';
  [[100,120,90,60],[260,80,120,70],[320,180,80,50],[180,250,110,60],[80,280,60,40],[380,120,50,35]].forEach(([x,y,w,h])=>{ctx.beginPath();ctx.ellipse(x,y,w,h,Math.random(),0,Math.PI*2);ctx.fill();});
  ctx.fillStyle='#dde8f0';ctx.fillRect(0,0,s,28);ctx.fillRect(0,s-22,s,22);
});
const moonTex = makeTex(512,(ctx,s)=>{
  ctx.fillStyle='#8a8a8a';ctx.fillRect(0,0,s,s);
  for(let i=0;i<60;i++){const x=Math.random()*s,y=Math.random()*s,r=Math.random()*18+3;const g=ctx.createRadialGradient(x,y,0,x,y,r);g.addColorStop(0,'rgba(55,55,55,0.9)');g.addColorStop(1,'rgba(138,138,138,0)');ctx.fillStyle=g;ctx.beginPath();ctx.arc(x,y,r,0,Math.PI*2);ctx.fill();}
  ctx.fillStyle='rgba(48,48,52,0.6)';[[150,180,80],[300,120,60],[200,300,50]].forEach(([x,y,r])=>{ctx.beginPath();ctx.arc(x,y,r,0,Math.PI*2);ctx.fill();});
});
const marsTex = makeTex(512,(ctx,s)=>{
  const g=ctx.createLinearGradient(0,0,s,s);
  g.addColorStop(0,'#8b2500');g.addColorStop(0.5,'#c1440e');g.addColorStop(1,'#8b2500');
  ctx.fillStyle=g;ctx.fillRect(0,0,s,s);
  for(let i=0;i<30;i++){const x=Math.random()*s,y=Math.random()*s,r=Math.random()*20+5;const cg=ctx.createRadialGradient(x,y,0,x,y,r);cg.addColorStop(0,'rgba(50,8,0,0.8)');cg.addColorStop(1,'rgba(150,50,10,0)');ctx.fillStyle=cg;ctx.beginPath();ctx.arc(x,y,r,0,Math.PI*2);ctx.fill();}
  ctx.fillStyle='rgba(218,230,240,0.7)';ctx.beginPath();ctx.ellipse(s/2,18,s/3,22,0,0,Math.PI*2);ctx.fill();
});
const jupiterTex = makeTex(512,(ctx,s)=>{
  [{y:0,h:40,c:'#c9a05a'},{y:40,h:30,c:'#b8784a'},{y:70,h:45,c:'#d4a860'},{y:115,h:25,c:'#c87840'},{y:140,h:50,c:'#e8c890'},{y:190,h:30,c:'#b86828'},{y:220,h:60,c:'#c9a05a'},{y:280,h:35,c:'#d4a860'},{y:315,h:45,c:'#c87840'},{y:360,h:40,c:'#e8c890'},{y:400,h:55,c:'#b86828'},{y:455,h:57,c:'#c9a05a'}].forEach(b=>{ctx.fillStyle=b.c;ctx.fillRect(0,b.y,s,b.h);});
  ctx.globalAlpha=0.25;for(let i=0;i<150;i++){ctx.fillStyle='rgba(180,120,60,0.4)';ctx.beginPath();ctx.ellipse(Math.random()*s,Math.random()*s,Math.random()*18+4,Math.random()*3+1,0,0,Math.PI*2);ctx.fill();}ctx.globalAlpha=1;
  const grs=ctx.createRadialGradient(s*.65,s*.55,0,s*.65,s*.55,38);grs.addColorStop(0,'rgba(170,45,18,0.95)');grs.addColorStop(1,'rgba(170,45,18,0)');ctx.fillStyle=grs;ctx.beginPath();ctx.ellipse(s*.65,s*.55,36,22,0,0,Math.PI*2);ctx.fill();
});
const saturnTex = makeTex(512,(ctx,s)=>{
  [{y:0,h:50,c:'#e8d08a'},{y:50,h:35,c:'#d4b870'},{y:85,h:55,c:'#f0dca0'},{y:140,h:40,c:'#c8a850'},{y:180,h:65,c:'#e8d08a'},{y:245,h:45,c:'#d4b870'},{y:290,h:222,c:'#e8d08a'}].forEach(b=>{ctx.fillStyle=b.c;ctx.fillRect(0,b.y,s,b.h);});
});

/* ══════════════════════════════════════════
   PLANET BUILDERS
══════════════════════════════════════════ */
function makeAtmo(r,color,op=0.18){
  return new THREE.Mesh(
    new THREE.SphereGeometry(r*1.08,48,48),
    new THREE.MeshPhongMaterial({color,transparent:true,opacity:op,side:THREE.BackSide,shininess:0})
  );
}
function makeGlowSphere(r,color,op=0.10){
  return new THREE.Mesh(
    new THREE.SphereGeometry(r*1.5,24,24),
    new THREE.MeshBasicMaterial({color,transparent:true,opacity:op,side:THREE.BackSide,depthWrite:false})
  );
}

function makePlanet(d){
  const g=new THREE.Group();
  const t=d.type;

  if(t==='earth'){
    const r=2.0;
    g.add(new THREE.Mesh(new THREE.SphereGeometry(r,64,64),new THREE.MeshPhongMaterial({map:earthTex,shininess:100,specular:new THREE.Color(0x4488cc)})));
    const clouds=new THREE.Mesh(new THREE.SphereGeometry(r+0.06,48,48),new THREE.MeshPhongMaterial({
      map:makeTex(512,(ctx,s)=>{
        ctx.clearRect(0,0,s,s);
        for(let i=0;i<70;i++){
          const x=Math.random()*s,y=Math.random()*s;
          const cg=ctx.createRadialGradient(x,y,0,x,y,Math.random()*38+12);
          cg.addColorStop(0,'rgba(255,255,255,0.9)');cg.addColorStop(1,'rgba(255,255,255,0)');
          ctx.fillStyle=cg;ctx.beginPath();ctx.ellipse(x,y,Math.random()*38+12,Math.random()*14+4,Math.random()*Math.PI,0,Math.PI*2);ctx.fill();
        }
      }),
      transparent:true,opacity:0.72,depthWrite:false
    }));
    clouds.userData.rotSpeed=0.0005; g.add(clouds);
    g.add(makeAtmo(r,0x4488ff,0.20));
    g.add(makeGlowSphere(r,0x2266ff,0.07));

  } else if(t==='moon'){
    const r=1.1;
    g.add(new THREE.Mesh(new THREE.SphereGeometry(r,48,48),new THREE.MeshPhongMaterial({map:moonTex,shininess:4,specular:new THREE.Color(0x111111)})));

  } else if(t==='mars'){
    const r=1.4;
    g.add(new THREE.Mesh(new THREE.SphereGeometry(r,64,64),new THREE.MeshPhongMaterial({map:marsTex,shininess:8})));
    g.add(makeAtmo(r,0xcc6633,0.09));
    g.add(makeGlowSphere(r,0xdd7744,0.05));

  } else if(t==='jupiter'){
    const r=2.8;
    g.add(new THREE.Mesh(new THREE.SphereGeometry(r,64,64),new THREE.MeshPhongMaterial({map:jupiterTex,shininess:18})));
    g.add(makeGlowSphere(r,0xff9933,0.06));

  } else if(t==='saturn'){
    const r=2.4;
    g.add(new THREE.Mesh(new THREE.SphereGeometry(r,64,64),new THREE.MeshPhongMaterial({map:saturnTex,shininess:22})));
    [{ir:r*1.12,or:r*1.3,c:0x9a8060,op:0.3},{ir:r*1.30,or:r*1.56,c:0xd4a870,op:0.7},{ir:r*1.56,or:r*2.00,c:0xe8c890,op:0.85},{ir:r*2.02,or:r*2.06,c:0x221108,op:0.95},{ir:r*2.06,or:r*2.45,c:0xd4b870,op:0.6},{ir:r*2.48,or:r*2.6,c:0xa89060,op:0.25}].forEach(rd=>{
      const ring=new THREE.Mesh(new THREE.RingGeometry(rd.ir,rd.or,128),new THREE.MeshBasicMaterial({color:rd.c,side:THREE.DoubleSide,transparent:true,opacity:rd.op,depthWrite:false}));
      ring.rotation.x=-Math.PI/2.5+0.05; g.add(ring);
    });

  } else if(t==='uranus'){
    const r=1.9;
    g.add(new THREE.Mesh(new THREE.SphereGeometry(r,48,48),new THREE.MeshPhongMaterial({color:0x4fd1c5,emissive:0x052220,shininess:70,specular:new THREE.Color(0x66dddd)})));
    [[r*1.3,r*1.5,0.3],[r*1.5,r*1.65,0.45],[r*1.68,r*1.8,0.2]].forEach(([ir,or,op])=>{
      const ring=new THREE.Mesh(new THREE.RingGeometry(ir,or,64),new THREE.MeshBasicMaterial({color:0x88cccc,side:THREE.DoubleSide,transparent:true,opacity:op,depthWrite:false}));
      ring.rotation.z=Math.PI/2+0.05;g.add(ring);
    });
    g.add(makeAtmo(r,0x00cccc,0.16));
    g.add(makeGlowSphere(r,0x00eedd,0.07));

  } else if(t==='neptune'){
    const r=1.8;
    g.add(new THREE.Mesh(new THREE.SphereGeometry(r,48,48),new THREE.MeshPhongMaterial({color:0x2b4eff,emissive:0x020830,shininess:80,specular:new THREE.Color(0x4466ff)})));
    g.add(makeAtmo(r,0x2244ff,0.18));
    g.add(makeGlowSphere(r,0x3355ff,0.09));

  } else if(t==='oort'){
    for(let i=0;i<500;i++){
      const phi=Math.acos(2*Math.random()-1),theta=Math.random()*Math.PI*2,r=5.5+Math.random()*3;
      const m=new THREE.Mesh(new THREE.SphereGeometry(0.015+Math.random()*0.05,4,4),
        new THREE.MeshBasicMaterial({color:new THREE.Color(0.5+Math.random()*0.3,0.6+Math.random()*0.2,0.8+Math.random()*0.2),transparent:true,opacity:0.5+Math.random()*0.5}));
      m.position.set(r*Math.sin(phi)*Math.cos(theta),r*Math.sin(phi)*Math.sin(theta),r*Math.cos(phi));
      g.add(m);
    }
    g.add(new THREE.Mesh(new THREE.SphereGeometry(7,32,32),new THREE.MeshBasicMaterial({color:0x8aacdd,wireframe:true,transparent:true,opacity:0.03})));

  } else if(t==='star'){
    // FIXED: Use sphere meshes for glow, not Points
    const r=1.6;
    const coreTex=makeTex(256,(ctx,s)=>{
      const gr=ctx.createRadialGradient(s/2,s/2,0,s/2,s/2,s/2);
      gr.addColorStop(0,'#fff8f0');
      gr.addColorStop(0.25,'#ffcc88');
      gr.addColorStop(0.5,'#ff8844');
      gr.addColorStop(0.75,'#ff4400');
      gr.addColorStop(1,'#cc2200');
      ctx.fillStyle=gr;ctx.fillRect(0,0,s,s);
    });
    // Core sphere
    g.add(new THREE.Mesh(new THREE.SphereGeometry(r,48,48),new THREE.MeshBasicMaterial({map:coreTex})));

    // Glow layers — ALL use sphere meshes (NOT Points/sprites)
    const glowLayers=[
      {scale:1.25,color:0xff9944,op:0.18},
      {scale:1.55,color:0xff7722,op:0.10},
      {scale:1.90,color:0xff5500,op:0.055},
      {scale:2.40,color:0xff3300,op:0.028},
      {scale:3.20,color:0xff2200,op:0.012},
    ];
    glowLayers.forEach(gl=>{
      const mesh=new THREE.Mesh(
        new THREE.SphereGeometry(r*gl.scale,32,32),
        new THREE.MeshBasicMaterial({color:gl.color,transparent:true,opacity:gl.op,side:THREE.BackSide,depthWrite:false,blending:THREE.AdditiveBlending})
      );
      g.add(mesh);
    });

    // Solar flare corona (animated in render loop via userData)
    const coronaMat=new THREE.MeshBasicMaterial({color:0xff6622,transparent:true,opacity:0.08,side:THREE.BackSide,depthWrite:false,blending:THREE.AdditiveBlending});
    const corona=new THREE.Mesh(new THREE.SphereGeometry(r*2.8,16,16),coronaMat);
    corona.userData.pulse=true;
    g.add(corona);

    g.add(new THREE.PointLight(0xff6633,5,50));

  } else if(t==='galaxy_core'){
    for(let i=0;i<800;i++){
      const r=Math.pow(Math.random(),1.5)*4,theta=Math.random()*Math.PI*2,phi=(Math.random()-0.5)*0.6;
      const b=Math.max(0.2,1-r/5);
      const m=new THREE.Mesh(new THREE.SphereGeometry(0.01+Math.random()*0.04,4,4),
        new THREE.MeshBasicMaterial({color:new THREE.Color(b,b*0.85,b*0.4),transparent:true,opacity:0.6+Math.random()*0.4}));
      m.position.set(r*Math.cos(theta),r*Math.sin(phi)*0.5,r*Math.sin(theta));
      g.add(m);
    }
    for(let arm=0;arm<4;arm++){
      for(let i=0;i<300;i++){
        const t2=i/300,angle=arm*(Math.PI/2)+t2*Math.PI*2.5,r=0.5+t2*7;
        const m=new THREE.Mesh(new THREE.SphereGeometry(0.015+Math.random()*0.035,3,3),
          new THREE.MeshBasicMaterial({color:new THREE.Color(1-t2*0.6,(1-t2*0.6)*0.75,(1-t2*0.6)*0.25),transparent:true,opacity:(0.7-t2*0.4)*(0.5+Math.random()*0.5)}));
        m.position.set(r*Math.cos(angle)+(Math.random()-0.5)*0.8,(Math.random()-0.5)*0.5*Math.exp(-t2*2),r*Math.sin(angle)+(Math.random()-0.5)*0.8);
        g.add(m);
      }
    }
    g.add(new THREE.Mesh(new THREE.SphereGeometry(0.6,16,16),new THREE.MeshBasicMaterial({color:0xffeeaa,transparent:true,opacity:0.95})));
    g.add(new THREE.Mesh(new THREE.SphereGeometry(1.2,16,16),new THREE.MeshBasicMaterial({color:0xffcc44,transparent:true,opacity:0.15,side:THREE.BackSide})));
    g.add(new THREE.PointLight(0xffd700,4,25));

  } else if(t==='galaxy'){
    for(let arm=0;arm<3;arm++){
      for(let i=0;i<700;i++){
        const t2=i/700,angle=arm*(Math.PI*2/3)+t2*Math.PI*3,r=0.2+t2*6.5,h=0.65+t2*0.25;
        const m=new THREE.Mesh(new THREE.SphereGeometry(0.012+Math.random()*0.022,3,3),
          new THREE.MeshBasicMaterial({color:new THREE.Color(h*0.75,h*0.78,Math.min(1,h*1.1)),transparent:true,opacity:(0.8-t2*0.5)*(0.5+Math.random()*0.5)}));
        m.position.set(r*Math.cos(angle)+(Math.random()-0.5)*(1-t2)*0.6,(Math.random()-0.5)*0.3*Math.exp(-t2*1.5),r*Math.sin(angle)+(Math.random()-0.5)*(1-t2)*0.6);
        g.add(m);
      }
    }
    for(let i=0;i<200;i++){
      const r=Math.random()*1.5,t2=Math.random()*Math.PI*2;
      const m=new THREE.Mesh(new THREE.SphereGeometry(0.02+Math.random()*0.04,3,3),
        new THREE.MeshBasicMaterial({color:new THREE.Color(1,0.92,0.75),transparent:true,opacity:0.7+Math.random()*0.3}));
      m.position.set(r*Math.cos(t2),(Math.random()-0.5)*0.4,r*Math.sin(t2));
      g.add(m);
    }
    g.add(new THREE.Mesh(new THREE.SphereGeometry(1.5,8,8),new THREE.MeshBasicMaterial({color:0xbbbbff,transparent:true,opacity:0.07,side:THREE.BackSide})));

  } else if(t==='blackhole'){
    const r=1.8;
    g.add(new THREE.Mesh(new THREE.SphereGeometry(r,64,64),new THREE.MeshBasicMaterial({color:0x000000})));
    g.add(new THREE.Mesh(new THREE.SphereGeometry(r*1.05,32,32),new THREE.MeshBasicMaterial({color:0x334488,transparent:true,opacity:0.12,side:THREE.BackSide,depthWrite:false})));
    [{ir:r*1.3,or:r*1.6,c:new THREE.Color(1.0,0.9,0.4),op:0.9},
     {ir:r*1.6,or:r*2.0,c:new THREE.Color(1.0,0.5,0.1),op:0.75},
     {ir:r*2.0,or:r*2.5,c:new THREE.Color(0.9,0.2,0.05),op:0.55},
     {ir:r*2.5,or:r*3.2,c:new THREE.Color(0.5,0.1,0.02),op:0.35},
     {ir:r*3.2,or:r*4.0,c:new THREE.Color(0.2,0.04,0.01),op:0.15}
    ].forEach((dk,idx)=>{
      const ring=new THREE.Mesh(new THREE.RingGeometry(dk.ir,dk.or,128),
        new THREE.MeshBasicMaterial({color:dk.c,side:THREE.DoubleSide,transparent:true,opacity:dk.op,depthWrite:false,blending:THREE.AdditiveBlending}));
      ring.rotation.x=Math.PI*0.12;
      ring.userData.rotSpeed=(0.006-idx*0.001)*(idx%2?1:-1);
      g.add(ring);
    });
    [1,-1].forEach(dir=>{
      const jet=new THREE.Mesh(new THREE.CylinderGeometry(0,0.35,11,16,6,true),
        new THREE.MeshBasicMaterial({color:0x00aaff,side:THREE.DoubleSide,transparent:true,opacity:0.10,depthWrite:false,blending:THREE.AdditiveBlending}));
      jet.position.y=dir*5.5; if(dir<0)jet.rotation.x=Math.PI; g.add(jet);
    });
    g.add(new THREE.PointLight(0xff6600,3,30));
    g.add(makeGlowSphere(r,0x441100,0.22));

  } else if(t==='cosmic_web'){
    for(let f=0;f<30;f++){
      const pts=[];let x=(Math.random()-0.5)*4,y=(Math.random()-0.5)*4,z=(Math.random()-0.5)*4;
      pts.push(new THREE.Vector3(x,y,z));
      for(let p=1;p<14;p++){x+=(Math.random()-0.5)*1.5;y+=(Math.random()-0.5)*0.7;z+=(Math.random()-0.5)*1.5;pts.push(new THREE.Vector3(x,y,z));}
      const curve=new THREE.CatmullRomCurve3(pts);
      const filGeo=new THREE.TubeGeometry(curve,40,0.006+Math.random()*0.012,5,false);
      g.add(new THREE.Mesh(filGeo,new THREE.MeshBasicMaterial({color:new THREE.Color(0.4+Math.random()*0.3,0.3+Math.random()*0.2,0.6+Math.random()*0.3),transparent:true,opacity:0.12+Math.random()*0.18,depthWrite:false})));
    }
    for(let i=0;i<40;i++){
      const angle=Math.random()*Math.PI*2,r=Math.random()*6;
      const cl=new THREE.Group();
      for(let j=0;j<7;j++){
        const m=new THREE.Mesh(new THREE.SphereGeometry(0.025+Math.random()*0.04,4,4),
          new THREE.MeshBasicMaterial({color:new THREE.Color(0.7+Math.random()*0.2,0.7+Math.random()*0.2,0.9),transparent:true,opacity:0.5+Math.random()*0.4}));
        m.position.set((Math.random()-0.5)*0.4,(Math.random()-0.5)*0.3,(Math.random()-0.5)*0.4);cl.add(m);
      }
      cl.position.set(Math.cos(angle)*r,(Math.random()-0.5)*3,Math.sin(angle)*r);
      g.add(cl);
    }

  } else if(t==='universe_edge'){
    const cmbTex=makeTex(512,(ctx,s)=>{
      for(let i=0;i<s;i+=4){
        for(let j=0;j<s;j+=4){
          const n=Math.sin(i*0.08)*Math.cos(j*0.06)+Math.sin(i*0.13+j*0.09)*0.5;
          const t2=(n+1.5)/3;
          ctx.fillStyle=`rgb(${Math.floor(200+t2*55)},${Math.floor(80+t2*38)},${Math.floor(50+t2*24)})`;
          ctx.fillRect(i,j,4,4);
        }
      }
    });
    g.add(new THREE.Mesh(new THREE.SphereGeometry(8,48,48),new THREE.MeshBasicMaterial({map:cmbTex,side:THREE.BackSide,transparent:true,opacity:0.48})));
    for(let i=0;i<1200;i++){
      const phi=Math.acos(2*Math.random()-1),theta=Math.random()*Math.PI*2,r=3+Math.random()*4.5;
      const hue=Math.random();let col=hue<0.4?new THREE.Color(1,0.85,0.6):hue<0.7?new THREE.Color(0.6,0.7,1.0):new THREE.Color(1,0.5,0.3);
      col.multiplyScalar(0.4+Math.random()*0.6);
      const m=new THREE.Mesh(new THREE.SphereGeometry(0.015+Math.random()*0.04,4,4),new THREE.MeshBasicMaterial({color:col,transparent:true,opacity:0.3+Math.random()*0.6}));
      m.position.set(r*Math.sin(phi)*Math.cos(theta),r*Math.sin(phi)*Math.sin(theta),r*Math.cos(phi));
      g.add(m);
    }
    for(let i=0;i<6;i++){
      const ring=new THREE.Mesh(new THREE.TorusGeometry(2.5+i*0.7,0.02,8,128),
        new THREE.MeshBasicMaterial({color:new THREE.Color(0.8,0.2+i*0.1,0.8-i*0.1),transparent:true,opacity:0.06-i*0.007,depthWrite:false}));
      ring.rotation.x=Math.random()*Math.PI;ring.rotation.y=Math.random()*Math.PI;
      ring.userData.rotSpeed=0.0008*(i%2?1:-1);g.add(ring);
    }
    g.add(new THREE.Mesh(new THREE.SphereGeometry(0.5,16,16),new THREE.MeshBasicMaterial({color:0xffffff,transparent:true,opacity:0.95})));
    g.add(new THREE.Mesh(new THREE.SphereGeometry(1.2,16,16),new THREE.MeshBasicMaterial({color:0xffaaff,transparent:true,opacity:0.18,side:THREE.BackSide})));
    g.add(new THREE.PointLight(0xcc00ff,4,35));
    g.add(makeGlowSphere(6,0x440088,0.04));
  }
  return g;
}

/* ══════════════════════════════════════════
   STARFIELD & NEBULAS — FIXED with circle sprite
══════════════════════════════════════════ */
function createStarfield(){
  const count=13000;
  const geo=new THREE.BufferGeometry();
  const pos=new Float32Array(count*3),col=new Float32Array(count*3);
  for(let i=0;i<count;i++){
    const theta=Math.random()*Math.PI*2,phi=Math.acos(2*Math.random()-1),r=300+Math.random()*700;
    pos[i*3]=r*Math.sin(phi)*Math.cos(theta);
    pos[i*3+1]=r*Math.sin(phi)*Math.sin(theta);
    pos[i*3+2]=r*Math.cos(phi);
    const t=Math.random();
    if(t<0.55){col[i*3]=1;col[i*3+1]=1;col[i*3+2]=1;}
    else if(t<0.70){col[i*3]=0.7;col[i*3+1]=0.8;col[i*3+2]=1;}
    else if(t<0.82){col[i*3]=1;col[i*3+1]=0.9;col[i*3+2]=0.7;}
    else{col[i*3]=1;col[i*3+1]=0.45;col[i*3+2]=0.35;}
  }
  geo.setAttribute('position',new THREE.BufferAttribute(pos,3));
  geo.setAttribute('color',new THREE.BufferAttribute(col,3));
  // Use circle sprite texture to avoid square particles
  return new THREE.Points(geo,new THREE.PointsMaterial({
    size:1.4,
    sizeAttenuation:true,
    vertexColors:true,
    transparent:true,
    opacity:0.92,
    map:circleSprite,
    alphaTest:0.01,
    depthWrite:false
  }));
}
const starfield=createStarfield(); scene.add(starfield);

function createNebula(pos,color,scale,op=0.032){
  const g=new THREE.Group();
  for(let i=0;i<70;i++){
    const m=new THREE.Mesh(new THREE.SphereGeometry(Math.random()*5+1,5,5),
      new THREE.MeshBasicMaterial({color,transparent:true,opacity:Math.random()*op+0.005,side:THREE.BackSide,depthWrite:false}));
    m.position.set((Math.random()-.5)*32*scale,(Math.random()-.5)*16*scale,(Math.random()-.5)*22*scale);
    g.add(m);
  }
  g.position.copy(pos); return g;
}
scene.add(createNebula(new THREE.Vector3(-50,8,-100),0x4466ff,1.6));
scene.add(createNebula(new THREE.Vector3(60,-12,-140),0xff4488,2.2,0.026));
scene.add(createNebula(new THREE.Vector3(-70,18,-220),0x8844ff,2.0));
scene.add(createNebula(new THREE.Vector3(40,25,-180),0x44ffaa,1.4,0.018));

/* ══════════════════════════════════════════
   PORTAL — SMOOTH CIRCULAR IRIS WIPE
══════════════════════════════════════════ */
const portalCanvas = document.getElementById('portalCanvas');
const portalCtx    = portalCanvas.getContext('2d');
portalCanvas.width  = window.innerWidth;
portalCanvas.height = window.innerHeight;

let portal = { active:false, phase:'idle', t:0, color:[0,212,255], onMidpoint:null };

function startPortal(color, onMidpoint){
  portal.color=color||[0,212,255];
  portal.onMidpoint=onMidpoint;
  portal.active=true;
  portal.phase='shrink';
  portal.t=0;
  portalCanvas.style.display='block';
}
function stopPortal(){
  portal.active=false;portal.phase='idle';
  portalCanvas.style.display='none';
  portalCtx.clearRect(0,0,portalCanvas.width,portalCanvas.height);
}
function easeInQuart(t){return t*t*t*t;}
function easeOutQuart(t){return 1-Math.pow(1-t,4);}

function drawPortal(dt){
  if(!portal.active)return;
  portal.t+=dt;
  const W=portalCanvas.width,H=portalCanvas.height;
  const cx=W/2,cy=H/2;
  const maxR=Math.sqrt(cx*cx+cy*cy)*1.05;
  const [pr,pg,pb]=portal.color;

  portalCtx.clearRect(0,0,W,H);
  let holeR=0;

  if(portal.phase==='shrink'){
    const dur=0.7;
    const progress=Math.min(portal.t/dur,1);
    holeR=maxR*(1-easeInQuart(progress));
    if(progress>=1){
      portal.phase='travel';portal.t=0;
      if(portal.onMidpoint){portal.onMidpoint();portal.onMidpoint=null;}
    }
    renderIris(portalCtx,cx,cy,W,H,holeR,maxR,pr,pg,pb,progress,'shrink');

  } else if(portal.phase==='travel'){
    const dur=0.35;
    const progress=Math.min(portal.t/dur,1);
    portalCtx.fillStyle='rgba(0,0,0,0.98)';
    portalCtx.fillRect(0,0,W,H);
    const flashR=maxR*0.12*Math.sin(progress*Math.PI);
    if(flashR>0){
      const fg=portalCtx.createRadialGradient(cx,cy,0,cx,cy,flashR);
      fg.addColorStop(0,`rgba(${pr},${pg},${pb},0.9)`);
      fg.addColorStop(0.4,`rgba(${pr},${pg},${pb},0.4)`);
      fg.addColorStop(1,'rgba(0,0,0,0)');
      portalCtx.fillStyle=fg;
      portalCtx.beginPath();portalCtx.arc(cx,cy,flashR,0,Math.PI*2);portalCtx.fill();
    }
    if(progress>=1){portal.phase='expand';portal.t=0;}

  } else if(portal.phase==='expand'){
    const dur=0.75;
    const progress=Math.min(portal.t/dur,1);
    holeR=maxR*easeOutQuart(progress);
    renderIris(portalCtx,cx,cy,W,H,holeR,maxR,pr,pg,pb,progress,'expand');
    if(progress>=1){stopPortal();}
  }
}

function renderIris(ctx,cx,cy,W,H,holeR,maxR,pr,pg,pb,progress,phase){
  ctx.fillStyle='rgba(0,0,0,0.97)';
  ctx.fillRect(0,0,W,H);
  if(holeR>1){
    ctx.save();
    ctx.globalCompositeOperation='destination-out';
    const hg=ctx.createRadialGradient(cx,cy,holeR*0.75,cx,cy,holeR);
    hg.addColorStop(0,'rgba(0,0,0,1)');
    hg.addColorStop(0.85,'rgba(0,0,0,1)');
    hg.addColorStop(1,'rgba(0,0,0,0)');
    ctx.fillStyle=hg;
    ctx.beginPath();ctx.arc(cx,cy,holeR,0,Math.PI*2);ctx.fill();
    ctx.restore();
  }
  for(let ri=0;ri<5;ri++){
    const ringR=holeR+ri*2.5;
    const ringOp=(1-ri/5)*(phase==='shrink'?0.9-progress*0.3:progress*0.6+0.3);
    ctx.save();
    ctx.strokeStyle=`rgba(${pr},${pg},${pb},${ringOp})`;
    ctx.lineWidth=Math.max(0.5,3-ri*0.5);
    ctx.shadowColor=`rgba(${pr},${pg},${pb},${ringOp*0.8})`;
    ctx.shadowBlur=8+ri*6;
    ctx.beginPath();ctx.arc(cx,cy,ringR,0,Math.PI*2);ctx.stroke();
    ctx.restore();
  }
  if(holeR>10){
    const rg=ctx.createRadialGradient(cx,cy,holeR*0.6,cx,cy,holeR*1.2);
    rg.addColorStop(0,'rgba(0,0,0,0)');
    rg.addColorStop(0.7,`rgba(${pr},${pg},${pb},0.04)`);
    rg.addColorStop(1,'rgba(0,0,0,0)');
    ctx.save();ctx.fillStyle=rg;ctx.fillRect(0,0,W,H);ctx.restore();
  }
}

/* ══════════════════════════════════════════
   WARP PARTICLES — FIXED with circle sprite
══════════════════════════════════════════ */
function createWarpParticles(rgb){
  const wGeo=new THREE.BufferGeometry();
  const wPos=new Float32Array(600*3);
  for(let i=0;i<600;i++){
    wPos[i*3]=(Math.random()-.5)*24;
    wPos[i*3+1]=(Math.random()-.5)*14;
    wPos[i*3+2]=(Math.random()-.5)*50;
  }
  wGeo.setAttribute('position',new THREE.BufferAttribute(wPos,3));
  return new THREE.Points(wGeo,new THREE.PointsMaterial({
    color:new THREE.Color(rgb[0]/255,rgb[1]/255,rgb[2]/255),
    size:0.22,
    transparent:true,
    opacity:0.9,
    blending:THREE.AdditiveBlending,
    map:circleSprite,
    alphaTest:0.01,
    depthWrite:false
  }));
}

/* ══════════════════════════════════════════
   PARTICLES (2D canvas)
══════════════════════════════════════════ */
const pCanvas=document.getElementById('particleCanvas');
const pCtx=pCanvas.getContext('2d');
pCanvas.width=window.innerWidth; pCanvas.height=window.innerHeight;
const particles=[];

function spawnParticles(n=50){
  const cx=window.innerWidth/2,cy=window.innerHeight/2;
  for(let i=0;i<n;i++){
    const angle=Math.random()*Math.PI*2,speed=2+Math.random()*6;
    particles.push({x:cx,y:cy,vx:Math.cos(angle)*speed,vy:Math.sin(angle)*speed,life:1,decay:0.012+Math.random()*0.018,size:2+Math.random()*4,hue:190+Math.random()*60,type:Math.random()>0.7?'star':'circle'});
  }
}

function tickParticles(){
  pCtx.clearRect(0,0,pCanvas.width,pCanvas.height);
  for(let i=particles.length-1;i>=0;i--){
    const p=particles[i];
    p.x+=p.vx;p.y+=p.vy;p.vy+=0.06;p.vx*=0.97;p.life-=p.decay;
    if(p.life<=0){particles.splice(i,1);continue;}
    pCtx.save();pCtx.globalAlpha=p.life*0.85;
    pCtx.fillStyle=`hsl(${p.hue},100%,65%)`;
    pCtx.shadowColor=`hsl(${p.hue},100%,70%)`;pCtx.shadowBlur=8;
    if(p.type==='star'){
      const s=p.size*p.life;pCtx.beginPath();
      for(let j=0;j<5;j++){
        const a=j*Math.PI*2/5-Math.PI/2,ia=(j+0.5)*Math.PI*2/5-Math.PI/2;
        if(j===0)pCtx.moveTo(p.x+Math.cos(a)*s,p.y+Math.sin(a)*s);
        else pCtx.lineTo(p.x+Math.cos(a)*s,p.y+Math.sin(a)*s);
        pCtx.lineTo(p.x+Math.cos(ia)*s*0.4,p.y+Math.sin(ia)*s*0.4);
      }
      pCtx.closePath();pCtx.fill();
    } else {
      pCtx.beginPath();pCtx.arc(p.x,p.y,p.size*p.life,0,Math.PI*2);pCtx.fill();
    }
    pCtx.restore();
  }
}

function showNamePop(name){
  const old=document.querySelector('.name-pop');if(old)old.remove();
  const el=document.createElement('div');el.className='name-pop';el.textContent=name;
  document.body.appendChild(el);
  setTimeout(()=>{if(el.parentNode)el.remove();},2400);
}

function easeOutBack(t){const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(t-1,3)+c1*Math.pow(t-1,2);}

/* ══════════════════════════════════════════
   MOTION / INPUT
══════════════════════════════════════════ */
let smoothX=0,smoothY=0,rawX=0,rawY=0;

document.addEventListener('mousemove',(e)=>{
  rawX=(e.clientX/window.innerWidth-0.5)*2;
  rawY=(e.clientY/window.innerHeight-0.5)*2;
});

let touchStartX=0,touchStartY=0,touchT=0,touchActive=false;
canvas3d.addEventListener('touchstart',(e)=>{
  if(e.touches.length!==1)return;
  touchStartX=e.touches[0].clientX;touchStartY=e.touches[0].clientY;
  touchT=Date.now();touchActive=true;
  recalibrateGyro();
},{passive:true});
canvas3d.addEventListener('touchmove',(e)=>{
  if(!touchActive||e.touches.length!==1)return;
  rawX=(e.touches[0].clientX/window.innerWidth-0.5)*2;
  rawY=(e.touches[0].clientY/window.innerHeight-0.5)*2;
},{passive:true});
canvas3d.addEventListener('touchend',(e)=>{
  if(!touchActive)return;touchActive=false;
  const dx=e.changedTouches[0].clientX-touchStartX;
  const dy=e.changedTouches[0].clientY-touchStartY;
  const dt=Date.now()-touchT,dist=Math.sqrt(dx*dx+dy*dy);
  if(dist>40&&dt<600){
    if(Math.abs(dx)>=Math.abs(dy)){if(dx<-40)nextDest();else if(dx>40)prevDest();}
    else{if(dy<-40)nextDest();else if(dy>40)prevDest();}
  } else if(dist<12){
    spawnRipple(e.changedTouches[0].clientX,e.changedTouches[0].clientY);
  }
},{passive:true});
canvas3d.addEventListener('touchmove',(e)=>e.preventDefault(),{passive:false});

let wheelLock=false;
window.addEventListener('wheel',(e)=>{
  if(wheelLock)return;wheelLock=true;
  if(e.deltaY>30)nextDest();else if(e.deltaY<-30)prevDest();
  setTimeout(()=>wheelLock=false,900);
},{passive:true});

function spawnRipple(x,y){
  const r=document.createElement('div');r.className='tap-ripple';
  r.style.left=x+'px';r.style.top=y+'px';
  document.body.appendChild(r);setTimeout(()=>r.remove(),850);
}

/* ══════════════════════════════════════════
   STATE
══════════════════════════════════════════ */
let currentIndex=-1,isTransitioning=false,currentObject=null;
let cameraTargetPos=new THREE.Vector3(0,2,10);
let cameraCurrentPos=new THREE.Vector3(0,2,10);
let scaleAnimId=null;

const minimapEl=document.getElementById('minimap');
DESTINATIONS.forEach((d,i)=>{
  if(i>0){const line=document.createElement('div');line.className='minimap-line';minimapEl.appendChild(line);}
  const dot=document.createElement('div');dot.className='minimap-dot';dot.dataset.index=i;
  const go=(e)=>{e.preventDefault();if(!isTransitioning)jumpTo(i);};
  dot.addEventListener('click',go);dot.addEventListener('touchend',go,{passive:false});
  minimapEl.appendChild(dot);
});

function updateMinimap(){
  document.querySelectorAll('.minimap-dot').forEach((dot,i)=>{
    dot.classList.remove('active','visited');
    if(i===currentIndex)dot.classList.add('active');
    else if(i<currentIndex)dot.classList.add('visited');
  });
}

function formatDist(ly){
  if(ly===0)return"0 km";
  if(ly<0.001)return(ly*9.461e12).toExponential(1)+" km";
  if(ly<1)return(ly*63241).toFixed(0)+" AU";
  if(ly<1000)return ly.toFixed(2)+" ly";
  if(ly<1e6)return(ly/1000).toFixed(1)+"K ly";
  if(ly<1e9)return(ly/1e6).toFixed(1)+"M ly";
  return(ly/1e9).toFixed(1)+"B ly";
}
function hexToRgb(hex){
  const r=/^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return r?[parseInt(r[1],16),parseInt(r[2],16),parseInt(r[3],16)]:[0,212,255];
}

function loadDestination(index){
  const d=DESTINATIONS[index];
  if(currentObject){scene.remove(currentObject);currentObject=null;}
  if(scaleAnimId){cancelAnimationFrame(scaleAnimId);scaleAnimId=null;}
  currentObject=makePlanet(d);currentObject.scale.setScalar(0.01);scene.add(currentObject);
  document.getElementById('destName').textContent=d.name;
  document.getElementById('distValue').textContent=formatDist(d.distance);
  const progress=((index+1)/DESTINATIONS.length)*100;
  document.getElementById('progressBar').style.width=progress+'%';
  document.getElementById('stepCounter').textContent=`${index+1} / ${DESTINATIONS.length}`;
  document.getElementById('velocityVal').textContent=index===0?"0.001 c":index<4?"0.1 c":index<8?"0.9 c":"99.99% c";
  document.getElementById('infoCategory').textContent=d.category;
  document.getElementById('infoTitle').textContent=d.name;
  document.getElementById('infoDesc').textContent=d.desc;
  document.getElementById('statsRow').innerHTML=d.stats.map(s=>`<div class="stat-item"><div class="stat-val">${s.v}</div><div class="stat-lbl">${s.l}</div></div>`).join('');
  setTimeout(()=>document.getElementById('infoPanel').classList.add('visible'),350);
  document.getElementById('prevBtn').disabled=(index===0);
  const camZ=['oort'].includes(d.type)?13:['jupiter','saturn'].includes(d.type)?11:['galaxy_core','galaxy','universe_edge','cosmic_web'].includes(d.type)?16:9;
  cameraTargetPos.set(0,2,camZ);
  let scaleT=0;
  const animScale=()=>{
    scaleT=Math.min(scaleT+0.055,1);
    const s=easeOutBack(scaleT);
    if(currentObject)currentObject.scale.setScalar(Math.max(0.001,s));
    if(scaleT<1)scaleAnimId=requestAnimationFrame(animScale);else scaleAnimId=null;
  };
  scaleAnimId=requestAnimationFrame(animScale);
  showNamePop(d.name);spawnParticles(65);updateMinimap();
}

/* ══════════════════════════════════════════
   NAVIGATION
══════════════════════════════════════════ */
function warpTo(index){
  if(isTransitioning)return;
  isTransitioning=true;
  document.getElementById('infoPanel').classList.remove('visible');
  const d=DESTINATIONS[index];
  const rgb=hexToRgb(d.accentColor||'#00d4ff');

  // 3D warp streaks — FIXED with circle sprite
  const warpMesh=createWarpParticles(rgb);
  scene.add(warpMesh);
  let wT=0;
  const stepWarp=()=>{
    wT+=0.03;
    const arr=warpMesh.geometry.attributes.position.array;
    for(let i=0;i<arr.length;i+=3){
      arr[i+2]-=3*(1+wT*1.5);
      if(arr[i+2]<-28)arr[i+2]=24;
    }
    warpMesh.geometry.attributes.position.needsUpdate=true;
    warpMesh.material.size=0.22+wT*0.9;
    if(wT<1.5)requestAnimationFrame(stepWarp);
    else scene.remove(warpMesh);
  };
  requestAnimationFrame(stepWarp);

  startPortal(rgb,()=>{
    loadDestination(index);
    setTimeout(()=>{ isTransitioning=false; },500);
  });
}

function jumpTo(i){currentIndex=i;warpTo(i);}
function nextDest(){if(isTransitioning)return;if(currentIndex<DESTINATIONS.length-1){currentIndex++;warpTo(currentIndex);}else showCompletion();}
function prevDest(){if(isTransitioning||currentIndex<=0)return;currentIndex--;warpTo(currentIndex);}

function launchMission(){
  document.getElementById('landing').classList.add('hidden');
  document.getElementById('navControls').style.display='flex';
  if('ontouchstart' in window||navigator.maxTouchPoints>0){
    const si=document.getElementById('swipeIndicator');si.style.display='flex';
    setTimeout(()=>si.style.display='none',5000);
    // Gyro already initialized via checkGyroSupport()
  }
  currentIndex=0;loadDestination(0);
}

function showCompletion(){
  document.getElementById('infoPanel').classList.remove('visible');
  document.getElementById('navControls').style.display='none';
  spawnParticles(180);
  setTimeout(()=>document.getElementById('completion').classList.add('visible'),500);
}

function restartMission(){
  document.getElementById('completion').classList.remove('visible');
  if(currentObject){scene.remove(currentObject);currentObject=null;}
  currentIndex=-1;
  document.getElementById('progressBar').style.width='0%';
  document.getElementById('distValue').textContent='0 km';
  document.getElementById('destName').textContent='— AWAITING LAUNCH —';
  updateMinimap();gyroCalibrated=false;
  setTimeout(()=>document.getElementById('landing').classList.remove('hidden'),400);
}

/* ══════════════════════════════════════════
   RENDER LOOP
══════════════════════════════════════════ */
const clock=new THREE.Clock();
let coronaPulseT=0;

function animate(){
  requestAnimationFrame(animate);
  const dt=clock.getDelta();
  const elapsed=clock.getElapsedTime();
  coronaPulseT+=dt;

  // Blend gyro + mouse/touch input
  const inputX=gyroEnabled?gyroX*0.8+rawX*0.2:rawX;
  const inputY=gyroEnabled?gyroY*0.8+rawY*0.2:rawY;
  smoothX+=(inputX-smoothX)*Math.min(1,dt*4.5);
  smoothY+=(inputY-smoothY)*Math.min(1,dt*4.5);

  starfield.rotation.y+=dt*0.003+smoothX*0.0005;
  starfield.rotation.x+=dt*0.0015+smoothY*0.0003;

  if(currentObject){
    currentObject.rotation.y+=dt*0.22;
    currentObject.rotation.x+=(smoothY*0.22-currentObject.rotation.x)*Math.min(1,dt*2.5);
    currentObject.rotation.z+=(-smoothX*0.12-currentObject.rotation.z)*Math.min(1,dt*2.5);
    currentObject.position.y=Math.sin(elapsed*0.65)*0.16;
    currentObject.children.forEach(child=>{
      if(child.userData.rotSpeed) child.rotation.z+=child.userData.rotSpeed;
      if(child.userData.pulse){
        // Animate corona opacity
        child.material.opacity=0.05+Math.sin(coronaPulseT*2.2)*0.04;
      }
      if(child.userData.orbitSpeed!==undefined){
        child.userData.orbitAngle=(child.userData.orbitAngle||0)+child.userData.orbitSpeed;
        child.position.x=Math.cos(child.userData.orbitAngle)*child.userData.orbitR;
        child.position.z=Math.sin(child.userData.orbitAngle)*child.userData.orbitR;
        if(child.userData.orbitY!==undefined)child.position.y=child.userData.orbitY;
      }
    });
  }

  cameraCurrentPos.lerp(cameraTargetPos,Math.min(1,dt*1.8));
  camera.position.set(
    cameraCurrentPos.x+smoothX*1.1+Math.sin(elapsed*0.22)*0.18,
    cameraCurrentPos.y+smoothY*0.65+Math.cos(elapsed*0.16)*0.12,
    cameraCurrentPos.z
  );
  camera.lookAt(0,0,0);

  tickParticles();
  drawPortal(dt);
  renderer.render(scene,camera);
}

animate();

window.addEventListener('resize',()=>{
  camera.aspect=window.innerWidth/window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth,window.innerHeight);
  pCanvas.width=window.innerWidth;pCanvas.height=window.innerHeight;
  portalCanvas.width=window.innerWidth;portalCanvas.height=window.innerHeight;
});

document.addEventListener('keydown',e=>{
  if(e.key==='ArrowRight'||e.key==='ArrowDown'){e.preventDefault();nextDest();}
  if(e.key==='ArrowLeft'||e.key==='ArrowUp'){e.preventDefault();prevDest();}
  if(e.key==='f'||e.key==='F'){toggleFullscreen();}
});
</script>
</body>
</html>
""", height=870, scrolling=False)