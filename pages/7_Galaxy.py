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
body{background:#000;overflow:hidden;font-family:'Inter',sans-serif;color:#fff;width:100%;height:100%;position:fixed;top:0;left:0;touch-action:none;user-select:none;-webkit-user-select:none;}
#canvas3d{position:fixed;top:0;left:0;width:100%;height:100%;z-index:0;touch-action:none;}
#particleCanvas{position:fixed;top:0;left:0;width:100%;height:100%;z-index:5;pointer-events:none;}
#portalCanvas{position:fixed;top:0;left:0;width:100%;height:100%;z-index:280;pointer-events:none;display:none;}
#fsBtn{position:fixed;top:12px;right:52px;z-index:500;font-family:'Orbitron',monospace;font-size:0.55rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#00d4ff;background:rgba(0,0,0,0.7);border:1px solid rgba(0,212,255,0.4);padding:7px 14px;border-radius:4px;cursor:pointer;transition:all 0.2s;touch-action:manipulation;backdrop-filter:blur(10px);display:flex;align-items:center;gap:6px;}
#fsBtn:hover,#fsBtn:active{background:rgba(0,212,255,0.15);border-color:#00d4ff;box-shadow:0 0 15px rgba(0,212,255,0.4);}
#fsBtn svg{width:14px;height:14px;fill:currentColor;}
#soundBtn{position:fixed;top:12px;right:160px;z-index:500;font-family:'Orbitron',monospace;font-size:0.55rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#34d399;background:rgba(0,0,0,0.7);border:1px solid rgba(52,211,153,0.4);padding:7px 14px;border-radius:4px;cursor:pointer;transition:all 0.2s;touch-action:manipulation;backdrop-filter:blur(10px);display:flex;align-items:center;gap:6px;}
#soundBtn:hover,#soundBtn:active{background:rgba(52,211,153,0.15);border-color:#34d399;box-shadow:0 0 15px rgba(52,211,153,0.4);}
#volControl{position:fixed;top:48px;right:160px;z-index:500;display:none;align-items:center;gap:8px;background:rgba(0,0,0,0.85);border:1px solid rgba(52,211,153,0.3);padding:6px 10px;border-radius:4px;backdrop-filter:blur(10px);}
#volControl input{width:80px;accent-color:#34d399;cursor:pointer;}
#volControl span{font-family:'Orbitron',monospace;font-size:0.48rem;color:#34d399;letter-spacing:1px;}
#soundViz{position:fixed;bottom:clamp(115px,16vw,132px);right:clamp(10px,2vw,20px);z-index:100;display:none;flex-direction:column;align-items:center;gap:2px;}
.viz-bar{width:3px;border-radius:2px;background:#34d399;box-shadow:0 0 4px #34d399;transition:height 0.08s ease;min-height:2px;}
#soundToast{position:fixed;bottom:clamp(115px,16vw,132px);left:clamp(12px,3vw,24px);z-index:150;font-family:'Orbitron',monospace;font-size:0.48rem;letter-spacing:2px;color:rgba(52,211,153,0.7);text-transform:uppercase;opacity:0;transition:opacity 0.4s ease;pointer-events:none;}
#soundToast.show{opacity:1;}
#gyroBtn{position:fixed;top:12px;right:280px;z-index:500;font-family:'Orbitron',monospace;font-size:0.55rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#f59e0b;background:rgba(0,0,0,0.7);border:1px solid rgba(245,158,11,0.4);padding:7px 14px;border-radius:4px;cursor:pointer;transition:all 0.2s;touch-action:manipulation;backdrop-filter:blur(10px);display:none;align-items:center;gap:6px;}
#hud{position:fixed;top:0;left:0;right:0;z-index:100;pointer-events:none;}
.top-bar{display:flex;align-items:center;justify-content:space-between;padding:clamp(8px,2vw,14px) clamp(12px,3vw,24px);padding-right:clamp(80px,12vw,120px);background:linear-gradient(180deg,rgba(0,0,0,0.9) 0%,transparent 100%);gap:8px;}
.mission-title{font-family:'Orbitron',monospace;font-size:clamp(0.48rem,1.8vw,0.9rem);font-weight:700;color:#00d4ff;letter-spacing:clamp(1px,0.4vw,3px);text-transform:uppercase;text-shadow:0 0 20px rgba(0,212,255,0.8);white-space:nowrap;flex-shrink:0;}
.top-center{display:flex;flex-direction:column;align-items:center;gap:3px;flex:1;min-width:0;padding:0 8px;}
.destination-label{font-family:'Orbitron',monospace;font-size:clamp(0.38rem,1.1vw,0.6rem);color:#9ca3af;letter-spacing:2px;text-transform:uppercase;}
.destination-name{font-family:'Orbitron',monospace;font-size:clamp(0.62rem,2.2vw,1rem);font-weight:900;color:#fff;text-shadow:0 0 30px rgba(255,255,255,0.5);transition:all 0.4s ease;text-align:center;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;width:100%;}
.velocity-box{font-family:'Orbitron',monospace;font-size:clamp(0.48rem,1.4vw,0.7rem);color:#34d399;text-align:right;letter-spacing:1px;white-space:nowrap;flex-shrink:0;}
.progress-track{margin:0 clamp(12px,3vw,24px);height:2px;background:rgba(255,255,255,0.08);border-radius:2px;overflow:visible;position:relative;}
.progress-glow{height:100%;background:linear-gradient(90deg,#3b82f6,#8b5cf6,#ec4899,#f59e0b);border-radius:2px;transition:width 0.8s cubic-bezier(0.4,0,0.2,1);position:relative;box-shadow:0 0 12px rgba(0,212,255,0.6);}
.progress-dot{position:absolute;right:-5px;top:-4px;width:10px;height:10px;background:#fff;border-radius:50%;box-shadow:0 0 10px #00d4ff,0 0 20px #00d4ff;}
.distance-hud{position:fixed;top:clamp(56px,9vw,82px);left:clamp(12px,3vw,24px);z-index:100;font-family:'Orbitron',monospace;}
.dist-label{font-size:clamp(0.38rem,1.1vw,0.52rem);color:#6b7280;letter-spacing:2px;text-transform:uppercase;margin-bottom:2px;}
.dist-value{font-size:clamp(0.82rem,2.8vw,1.3rem);font-weight:700;color:#00d4ff;text-shadow:0 0 20px rgba(0,212,255,0.5);transition:all 0.5s ease;}
#infoPanel{position:fixed;bottom:clamp(86px,14vw,105px);left:clamp(12px,3vw,24px);z-index:100;width:min(310px,calc(100vw - 48px));background:rgba(3,8,20,0.94);border:1px solid rgba(0,212,255,0.22);border-left:3px solid #00d4ff;border-radius:0 14px 14px 0;padding:clamp(12px,2.5vw,18px) clamp(14px,3vw,20px);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);transform:translateX(-120%);transition:transform 0.7s cubic-bezier(0.4,0,0.2,1);pointer-events:none;box-shadow:0 0 40px rgba(0,212,255,0.08),inset 0 0 20px rgba(0,212,255,0.02);}
#infoPanel.visible{transform:translateX(0);}
.info-category{font-family:'Orbitron',monospace;font-size:clamp(0.38rem,1.2vw,0.52rem);color:#00d4ff;letter-spacing:3px;text-transform:uppercase;margin-bottom:5px;}
.info-title{font-family:'Orbitron',monospace;font-size:clamp(0.82rem,2.8vw,1.2rem);font-weight:900;color:#fff;margin-bottom:7px;line-height:1.2;}
.info-desc{font-size:clamp(0.68rem,1.7vw,0.8rem);color:#9ca3af;line-height:1.6;margin-bottom:11px;display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden;}
.stats-row{display:grid;grid-template-columns:1fr 1fr;gap:5px;}
.stat-item{background:rgba(0,212,255,0.06);border:1px solid rgba(0,212,255,0.14);border-radius:8px;padding:6px 8px;}
.stat-val{font-family:'Orbitron',monospace;font-size:clamp(0.58rem,1.7vw,0.8rem);font-weight:700;color:#00d4ff;}
.stat-lbl{font-size:clamp(0.48rem,1.2vw,0.62rem);color:#6b7280;text-transform:uppercase;letter-spacing:0.5px;margin-top:2px;}
#navControls{position:fixed;bottom:clamp(14px,3.5vw,26px);left:50%;transform:translateX(-50%);z-index:200;display:flex;align-items:center;gap:clamp(8px,2vw,14px);}
.nav-btn{padding:clamp(11px,2.5vw,13px) clamp(18px,4vw,28px);font-family:'Orbitron',monospace;font-size:clamp(0.56rem,1.7vw,0.72rem);font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#fff;background:rgba(3,8,20,0.92);border:1px solid rgba(0,212,255,0.4);border-radius:4px;cursor:pointer;transition:all 0.2s;touch-action:manipulation;white-space:nowrap;min-height:44px;min-width:44px;}
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
#swipeIndicator{position:fixed;bottom:clamp(72px,11vw,86px);left:50%;transform:translateX(-50%);z-index:150;display:none;flex-direction:row;align-items:center;gap:14px;font-family:'Orbitron',monospace;font-size:0.52rem;color:rgba(0,212,255,0.5);letter-spacing:2px;text-transform:uppercase;white-space:nowrap;animation:swipePulse 2s ease-in-out infinite;}
@keyframes swipePulse{0%,100%{opacity:0.3}50%{opacity:1}}
#motionIndicator{position:fixed;top:clamp(56px,9vw,82px);right:clamp(52px,8vw,72px);z-index:100;display:none;flex-direction:column;align-items:center;gap:4px;}
.motion-dot{width:6px;height:6px;border-radius:50%;background:#00d4ff;box-shadow:0 0 6px #00d4ff;animation:motionPulse 1s ease-in-out infinite;}
@keyframes motionPulse{0%,100%{transform:scale(1);opacity:0.6}50%{transform:scale(1.4);opacity:1}}
.motion-label{font-family:'Orbitron',monospace;font-size:0.42rem;color:rgba(0,212,255,0.6);letter-spacing:1px;text-transform:uppercase;}
#landing{position:fixed;inset:0;z-index:500;display:flex;flex-direction:column;align-items:center;justify-content:center;background:radial-gradient(ellipse at center,rgba(0,15,35,0.97) 0%,rgba(0,0,0,1) 100%);transition:opacity 0.9s ease,visibility 0.9s;padding:clamp(16px,5vw,40px);text-align:center;}
#landing.hidden{opacity:0;visibility:hidden;pointer-events:none;}
.landing-badge{font-family:'Orbitron',monospace;font-size:clamp(0.46rem,1.4vw,0.58rem);letter-spacing:5px;color:#00d4ff;text-transform:uppercase;margin-bottom:clamp(14px,3.5vw,28px);opacity:0.8;}
.landing-title{font-family:'Orbitron',monospace;font-size:clamp(2rem,9.5vw,5rem);font-weight:900;line-height:1.0;margin-bottom:clamp(10px,2.5vw,18px);background:linear-gradient(135deg,#fff 0%,#00d4ff 35%,#8b5cf6 65%,#ff6bcb 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;filter:drop-shadow(0 0 30px rgba(0,212,255,0.3));}
.landing-sub{font-size:clamp(0.75rem,2.3vw,0.96rem);color:#6b7280;max-width:440px;line-height:1.7;margin-bottom:clamp(26px,5.5vw,46px);}
.launch-btn{font-family:'Orbitron',monospace;font-size:clamp(0.66rem,1.9vw,0.82rem);font-weight:700;letter-spacing:4px;text-transform:uppercase;color:#000;background:linear-gradient(135deg,#00d4ff,#8b5cf6);border:none;padding:clamp(13px,3.5vw,16px) clamp(26px,6.5vw,46px);border-radius:4px;cursor:pointer;transition:all 0.3s;touch-action:manipulation;min-height:48px;box-shadow:0 0 30px rgba(0,212,255,0.3);}
.launch-btn:active{transform:scale(0.96);box-shadow:0 0 50px rgba(0,212,255,0.6);}
.scroll-hint{position:absolute;bottom:clamp(18px,3.5vw,36px);font-family:'Orbitron',monospace;font-size:clamp(0.42rem,1.1vw,0.56rem);letter-spacing:2px;color:#374151;text-transform:uppercase;animation:pulse 2s ease-in-out infinite;}
@keyframes pulse{0%,100%{opacity:.4}50%{opacity:1}}
#completion{position:fixed;inset:0;z-index:500;display:flex;flex-direction:column;align-items:center;justify-content:center;background:radial-gradient(ellipse at center,rgba(0,10,30,0.98) 0%,rgba(0,0,0,1) 100%);opacity:0;visibility:hidden;transition:all 0.8s ease;padding:clamp(16px,5vw,40px);text-align:center;}
#completion.visible{opacity:1;visibility:visible;}
.complete-label{font-family:'Orbitron',monospace;font-size:clamp(0.46rem,1.4vw,0.58rem);letter-spacing:6px;color:#34d399;text-transform:uppercase;margin-bottom:clamp(10px,2.5vw,18px);}
.complete-title{font-family:'Orbitron',monospace;font-size:clamp(1.5rem,5.5vw,3.2rem);font-weight:900;margin-bottom:clamp(9px,2vw,14px);background:linear-gradient(135deg,#34d399,#00d4ff,#8b5cf6,#ff6bcb);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.complete-dist{font-family:'Orbitron',monospace;font-size:clamp(1rem,3.8vw,1.9rem);font-weight:900;color:#00d4ff;text-shadow:0 0 30px rgba(0,212,255,0.5);margin-bottom:9px;}
.complete-text{font-size:clamp(0.7rem,1.9vw,0.88rem);color:#6b7280;max-width:480px;line-height:1.8;margin-bottom:clamp(22px,4.5vw,36px);}
.restart-btn{font-family:'Orbitron',monospace;font-size:clamp(0.6rem,1.7vw,0.72rem);font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#fff;background:transparent;border:1px solid rgba(0,212,255,0.5);padding:clamp(11px,2.5vw,14px) clamp(20px,4.5vw,36px);border-radius:4px;cursor:pointer;transition:all 0.2s;touch-action:manipulation;min-height:44px;}
.restart-btn:active{background:rgba(0,212,255,0.1);border-color:#00d4ff;box-shadow:0 0 20px rgba(0,212,255,0.3);}
#warpOverlay{position:fixed;inset:0;z-index:270;pointer-events:none;opacity:0;transition:opacity 0.15s;}
.scanlines{position:fixed;inset:0;z-index:50;background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,0,0,0.025) 2px,rgba(0,0,0,0.025) 4px);pointer-events:none;}
.corner{position:fixed;z-index:100;width:clamp(20px,4.5vw,36px);height:clamp(20px,4.5vw,36px);pointer-events:none;}
.corner-tl{top:8px;left:8px;border-top:1px solid rgba(0,212,255,0.5);border-left:1px solid rgba(0,212,255,0.5);}
.corner-tr{top:8px;right:8px;border-top:1px solid rgba(0,212,255,0.5);border-right:1px solid rgba(0,212,255,0.5);}
.corner-bl{bottom:8px;left:8px;border-bottom:1px solid rgba(0,212,255,0.5);border-left:1px solid rgba(0,212,255,0.5);}
.corner-br{bottom:8px;right:8px;border-bottom:1px solid rgba(0,212,255,0.5);border-right:1px solid rgba(0,212,255,0.5);}
@keyframes namePop{0%{opacity:0;transform:translate(-50%,-50%) scale(0.5) translateY(20px);}25%{opacity:1;transform:translate(-50%,-50%) scale(1.06) translateY(0);}75%{opacity:1;transform:translate(-50%,-50%) scale(1) translateY(0);}100%{opacity:0;transform:translate(-50%,-50%) scale(0.95) translateY(-8px);}}
.name-pop{position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);z-index:250;font-family:'Orbitron',monospace;font-size:clamp(1.1rem,4.5vw,2.8rem);font-weight:900;color:#fff;text-shadow:0 0 40px rgba(0,212,255,1),0 0 80px rgba(139,92,246,0.8);pointer-events:none;animation:namePop 2.2s cubic-bezier(0.4,0,0.2,1) forwards;white-space:nowrap;text-align:center;}
@keyframes rippleOut{0%{width:0;height:0;opacity:0.9;}100%{width:120px;height:120px;opacity:0;}}
.tap-ripple{position:fixed;border-radius:50%;background:radial-gradient(circle,rgba(0,212,255,0.4),transparent);pointer-events:none;z-index:400;transform:translate(-50%,-50%);animation:rippleOut 0.8s ease-out forwards;}
</style>
</head>
<body>
<canvas id="canvas3d"></canvas>
<canvas id="particleCanvas"></canvas>
<canvas id="portalCanvas"></canvas>
<div class="scanlines"></div>
<div class="corner corner-tl"></div><div class="corner corner-tr"></div>
<div class="corner corner-bl"></div><div class="corner corner-br"></div>
<div id="warpOverlay"></div>

<button id="fsBtn" onclick="toggleFullscreen()" title="Fullscreen">
  <svg id="fsIcon" viewBox="0 0 24 24"><path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/></svg>
  <span id="fsLabel">FULL</span>
</button>
<button id="soundBtn" onclick="toggleSound()" title="Toggle Sound">
  <span id="soundIcon">🔊</span><span id="soundLabel">SOUND ON</span>
</button>
<div id="volControl">
  <span>VOL</span>
  <input type="range" id="volSlider" min="0" max="100" value="55" oninput="setVolume(this.value)"/>
  <span id="volPct">55%</span>
</div>
<button id="gyroBtn" onclick="requestGyroPermission()" title="Enable Gyroscope">📱 GYRO</button>

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
    <div class="progress-glow" id="progressBar" style="width:0%"><div class="progress-dot"></div></div>
  </div>
</div>

<div class="distance-hud">
  <div class="dist-label">Distance Traveled</div>
  <div class="dist-value" id="distValue">0 ly</div>
</div>
<div id="motionIndicator"><div class="motion-dot"></div><div class="motion-label">TILT</div></div>
<div id="soundViz">
  <div class="viz-bar" id="vb1" style="height:4px;"></div>
  <div class="viz-bar" id="vb2" style="height:4px;"></div>
  <div class="viz-bar" id="vb3" style="height:4px;"></div>
  <div class="viz-bar" id="vb4" style="height:4px;"></div>
  <div class="viz-bar" id="vb5" style="height:4px;"></div>
</div>
<div id="soundToast">♪ LOADING...</div>

<div id="infoPanel">
  <div class="info-category" id="infoCategory">SOLAR SYSTEM</div>
  <div class="info-title" id="infoTitle">Earth</div>
  <div class="info-desc" id="infoDesc">Our pale blue dot.</div>
  <div class="stats-row" id="statsRow"></div>
</div>
<div id="minimap"></div>
<div id="swipeIndicator"><span>←</span> SWIPE TO NAVIGATE <span>→</span></div>
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
   AUDIO ENGINE
══════════════════════════════════════════ */
let audioCtx=null,masterGain=null,masterVolume=0.55,soundEnabled=true;
let currentSoundNodes=[],analyserNode=null,analyserData=null;

const SOUND_PROFILES=["EARTH BIOSPHERE","LUNAR RESONANCE","MARTIAN WINDS","JOVIAN PLASMA WAVES","SATURN RING HARMONICS","URANIAN ICE FIELDS","NEPTUNIAN GALE","OORT CLOUD SILENCE","STELLAR CORONA","GALACTIC CORE RUMBLE","ANDROMEDA COLLISION WAVE","QUASAR RADIATION","COSMIC WEB FILAMENTS","BIG BANG ECHO"];

function initAudio(){
  if(audioCtx) return true;
  try{
    audioCtx=new(window.AudioContext||window.webkitAudioContext)();
    masterGain=audioCtx.createGain();
    masterGain.gain.setValueAtTime(masterVolume,audioCtx.currentTime);
    analyserNode=audioCtx.createAnalyser();
    analyserNode.fftSize=32;
    analyserData=new Uint8Array(analyserNode.frequencyBinCount);
    masterGain.connect(analyserNode);
    analyserNode.connect(audioCtx.destination);
    return true;
  }catch(e){return false;}
}
function resumeAudio(){if(audioCtx&&audioCtx.state==='suspended')audioCtx.resume();}
function stopAllSounds(fadeTime=0.8){
  currentSoundNodes.forEach(node=>{
    try{
      if(node.gain){node.gain.gain.cancelScheduledValues(audioCtx.currentTime);node.gain.gain.setValueAtTime(node.gain.gain.value,audioCtx.currentTime);node.gain.gain.linearRampToValueAtTime(0,audioCtx.currentTime+fadeTime);}
      if(node.stop)setTimeout(()=>{try{node.stop();}catch(e){}},fadeTime*1000+100);
      if(node.disconnect)setTimeout(()=>{try{node.disconnect();}catch(e){}},fadeTime*1000+200);
    }catch(e){}
  });
  currentSoundNodes=[];
}
function setVolume(val){masterVolume=val/100;document.getElementById('volPct').textContent=val+'%';if(masterGain)masterGain.gain.setValueAtTime(masterVolume,audioCtx.currentTime);}
function toggleSound(){
  soundEnabled=!soundEnabled;
  const btn=document.getElementById('soundBtn'),icon=document.getElementById('soundIcon'),lbl=document.getElementById('soundLabel');
  if(soundEnabled){icon.textContent='🔊';lbl.textContent='SOUND ON';btn.style.color='#34d399';btn.style.borderColor='rgba(52,211,153,0.4)';resumeAudio();document.getElementById('soundViz').style.display='flex';if(currentIndex>=0)playDestinationSound(currentIndex);}
  else{icon.textContent='🔇';lbl.textContent='SOUND OFF';btn.style.color='#6b7280';btn.style.borderColor='rgba(107,114,128,0.3)';stopAllSounds(0.3);document.getElementById('soundViz').style.display='none';}
}
document.getElementById('soundBtn').addEventListener('mouseenter',()=>document.getElementById('volControl').style.display='flex');
document.getElementById('soundBtn').addEventListener('mouseleave',()=>setTimeout(()=>{if(!document.getElementById('volControl').matches(':hover'))document.getElementById('volControl').style.display='none';},300));
document.getElementById('volControl').addEventListener('mouseleave',()=>document.getElementById('volControl').style.display='none');

function makeNoiseBuffer(type='white',duration=3){
  const sr=audioCtx.sampleRate,len=sr*duration,buf=audioCtx.createBuffer(1,len,sr),data=buf.getChannelData(0);
  if(type==='white'){for(let i=0;i<len;i++)data[i]=Math.random()*2-1;}
  else if(type==='pink'){let b0=0,b1=0,b2=0,b3=0,b4=0,b5=0,b6=0;for(let i=0;i<len;i++){const wh=Math.random()*2-1;b0=0.99886*b0+wh*0.0555179;b1=0.99332*b1+wh*0.0750759;b2=0.96900*b2+wh*0.1538520;b3=0.86650*b3+wh*0.3104856;b4=0.55000*b4+wh*0.5329522;b5=-0.7616*b5-wh*0.0168980;data[i]=(b0+b1+b2+b3+b4+b5+b6+wh*0.5362)*0.11;b6=wh*0.115926;}}
  else if(type==='brown'){let last=0;for(let i=0;i<len;i++){const wh=Math.random()*2-1;last=(last+0.02*wh)/1.02;data[i]=last*3.5;}}
  return buf;
}
function makeNoise(type,gainVal,filterFreq=null,filterType='lowpass',Q=1){
  const src=audioCtx.createBufferSource();src.buffer=makeNoiseBuffer(type,4);src.loop=true;
  const g=audioCtx.createGain();g.gain.setValueAtTime(0,audioCtx.currentTime);g.gain.linearRampToValueAtTime(gainVal,audioCtx.currentTime+1.5);
  if(filterFreq!==null){const f=audioCtx.createBiquadFilter();f.type=filterType;f.frequency.setValueAtTime(filterFreq,audioCtx.currentTime);f.Q.setValueAtTime(Q,audioCtx.currentTime);src.connect(f);f.connect(g);}else{src.connect(g);}
  g.connect(masterGain);src.start();
  currentSoundNodes.push({stop:()=>src.stop(),disconnect:()=>g.disconnect(),gain:g});
  return{src,gain:g};
}
function makeDrone(freq,waveform,gainVal,detune=0){
  const osc=audioCtx.createOscillator();osc.type=waveform;osc.frequency.setValueAtTime(freq,audioCtx.currentTime);
  if(detune)osc.detune.setValueAtTime(detune,audioCtx.currentTime);
  const g=audioCtx.createGain();g.gain.setValueAtTime(0,audioCtx.currentTime);g.gain.linearRampToValueAtTime(gainVal,audioCtx.currentTime+2.0);
  osc.connect(g);g.connect(masterGain);osc.start();
  currentSoundNodes.push({stop:()=>osc.stop(),disconnect:()=>g.disconnect(),gain:g});
  return{osc,gain:g};
}
function makeLFODrone(freq,waveform,gainVal,lfoRate,lfoDepth){
  const{osc,gain}=makeDrone(freq,waveform,gainVal);
  const lfo=audioCtx.createOscillator();lfo.type='sine';lfo.frequency.setValueAtTime(lfoRate,audioCtx.currentTime);
  const lfoGain=audioCtx.createGain();lfoGain.gain.setValueAtTime(lfoDepth,audioCtx.currentTime);
  lfo.connect(lfoGain);lfoGain.connect(osc.frequency);lfo.start();
  currentSoundNodes.push({stop:()=>lfo.stop(),disconnect:()=>lfoGain.disconnect(),gain:lfoGain});
  return{osc,gain};
}
function makePulse(freq,interval,gainVal,duration=0.08){
  let active=true;
  const schedule=()=>{
    if(!active||!soundEnabled)return;
    try{const osc=audioCtx.createOscillator(),env=audioCtx.createGain();osc.type='sine';osc.frequency.setValueAtTime(freq,audioCtx.currentTime);env.gain.setValueAtTime(0,audioCtx.currentTime);env.gain.linearRampToValueAtTime(gainVal,audioCtx.currentTime+0.01);env.gain.exponentialRampToValueAtTime(0.0001,audioCtx.currentTime+duration);osc.connect(env);env.connect(masterGain);osc.start();osc.stop(audioCtx.currentTime+duration+0.05);}catch(e){}
    setTimeout(schedule,interval);
  };
  schedule();
  currentSoundNodes.push({stop:()=>{active=false;},disconnect:()=>{},gain:{gain:{value:gainVal}}});
}
function makeReverb(decayTime=4,wet=0.4){
  const sr=audioCtx.sampleRate,len=sr*decayTime,ir=audioCtx.createBuffer(2,len,sr);
  for(let ch=0;ch<2;ch++){const d=ir.getChannelData(ch);for(let i=0;i<len;i++)d[i]=(Math.random()*2-1)*Math.pow(1-i/len,2.0);}
  const conv=audioCtx.createConvolver();conv.buffer=ir;
  const wetGain=audioCtx.createGain();wetGain.gain.setValueAtTime(wet,audioCtx.currentTime);
  conv.connect(wetGain);wetGain.connect(masterGain);
  currentSoundNodes.push({stop:()=>{},disconnect:()=>{conv.disconnect();wetGain.disconnect();},gain:wetGain});
  return conv;
}
function makeChord(freqs,gainVal){
  const rev=makeReverb(6,0.35);
  freqs.forEach((f,i)=>{
    const osc=audioCtx.createOscillator();osc.type=i%2===0?'sine':'triangle';osc.frequency.setValueAtTime(f,audioCtx.currentTime);osc.detune.setValueAtTime((Math.random()-0.5)*12,audioCtx.currentTime);
    const g=audioCtx.createGain();g.gain.setValueAtTime(0,audioCtx.currentTime);g.gain.linearRampToValueAtTime(gainVal/freqs.length,audioCtx.currentTime+2.5+i*0.3);
    osc.connect(g);g.connect(masterGain);g.connect(rev);osc.start();
    currentSoundNodes.push({stop:()=>osc.stop(),disconnect:()=>g.disconnect(),gain:g});
  });
}

function playDestinationSound(index){
  if(!soundEnabled||!audioCtx)return;
  resumeAudio();
  const t=DESTINATIONS[index].type;
  switch(t){
    case 'earth':makeNoise('pink',0.055,800,'lowpass',0.8);makeNoise('white',0.018,3200,'bandpass',2.5);makeChord([220,277.18,329.63,440,523.25],0.028);makeLFODrone(110,'sine',0.022,0.18,8);makeLFODrone(220,'sine',0.015,0.12,5);makePulse(55,1400,0.018,0.25);break;
    case 'moon':makeNoise('brown',0.028,120,'lowpass',0.5);makeNoise('white',0.006,400,'lowpass',0.3);makeChord([55,82.4,110],0.022);makeLFODrone(28,'sine',0.035,0.04,3);makeLFODrone(55,'triangle',0.012,0.06,2);break;
    case 'mars':makeNoise('pink',0.065,600,'bandpass',1.2);makeNoise('white',0.022,1800,'highpass',0.8);makeNoise('brown',0.045,80,'lowpass',0.6);makeLFODrone(73.4,'sawtooth',0.015,0.08,15);makeChord([73.4,110,146.8],0.02);makePulse(180,3800,0.012,0.6);break;
    case 'jupiter':makeNoise('brown',0.07,200,'lowpass',1.5);makeNoise('pink',0.04,1200,'bandpass',3);makeLFODrone(36.7,'sawtooth',0.04,0.22,18);makeLFODrone(55,'square',0.018,0.35,12);makeLFODrone(18.3,'sine',0.055,0.08,6);makeNoise('brown',0.06,45,'lowpass',2.0);makePulse(440,2200,0.025,0.12);makePulse(880,3100,0.018,0.08);makeChord([36.7,55,73.4,110],0.025);break;
    case 'saturn':makeChord([261.6,392,523.25,784,1046.5],0.022);makeNoise('white',0.025,4000,'bandpass',8);makeNoise('pink',0.035,500,'bandpass',2);makeLFODrone(27.5,'sine',0.045,0.11,10);makeLFODrone(41.2,'triangle',0.025,0.14,7);makeLFODrone(1200,'sine',0.008,0.55,300);makeLFODrone(1320,'sine',0.006,0.48,280);makeNoise('brown',0.04,100,'lowpass',1.0);break;
    case 'uranus':makeNoise('white',0.018,3500,'highpass',0.6);makeNoise('pink',0.028,200,'lowpass',0.8);makeLFODrone(49,'sine',0.03,0.19,22);makeLFODrone(98,'triangle',0.018,0.13,11);makeLFODrone(196,'sine',0.012,0.09,8);makeChord([523.25,659.25,783.99,1046.5,1318.5],0.016);makeLFODrone(2100,'sine',0.006,1.2,150);break;
    case 'neptune':makeNoise('white',0.055,2200,'bandpass',2.5);makeNoise('pink',0.045,800,'bandpass',1.8);makeNoise('brown',0.06,120,'lowpass',1.5);makeLFODrone(41.2,'sawtooth',0.035,0.25,30);makeLFODrone(82.4,'sawtooth',0.022,0.18,22);makeLFODrone(130.8,'triangle',0.02,0.08,14);makeChord([41.2,55,82.4,110],0.022);makePulse(220,1800,0.028,0.45);break;
    case 'oort':makeNoise('white',0.008,150,'lowpass',0.3);makeNoise('pink',0.005,80,'lowpass',0.2);makeLFODrone(27.5,'sine',0.018,0.02,1.5);makeChord([27.5,32.7,36.7],0.01);makePulse(2800,8500,0.008,0.15);break;
    case 'star':makeNoise('white',0.045,6000,'highpass',1.5);makeNoise('pink',0.06,1200,'bandpass',2.0);makeNoise('brown',0.05,200,'lowpass',1.8);makeLFODrone(55,'sawtooth',0.04,0.18,25);makeLFODrone(110,'sine',0.025,0.12,18);makePulse(330,1600,0.022,0.18);makePulse(660,2800,0.015,0.1);makeLFODrone(3300,'sine',0.008,2.5,400);makeChord([55,82.4,110,165.5],0.022);break;
    case 'galaxy_core':makeLFODrone(10.9,'sine',0.065,0.04,3);makeLFODrone(21.8,'sine',0.04,0.05,4);makeNoise('brown',0.08,60,'lowpass',2.5);makeNoise('pink',0.05,400,'bandpass',3);makeLFODrone(73.4,'sawtooth',0.025,0.28,35);makeLFODrone(146.8,'square',0.015,0.22,28);makePulse(880,600,0.022,0.05);makePulse(1760,1200,0.015,0.04);makeChord([10.9,21.8,43.6,87.3,174.6],0.028);makeNoise('white',0.02,8000,'highpass',0.5);break;
    case 'galaxy':makeNoise('pink',0.04,600,'bandpass',1.5);makeNoise('brown',0.05,100,'lowpass',1.8);makeLFODrone(27.5,'sine',0.038,0.06,8);makeLFODrone(55,'triangle',0.025,0.08,6);makeLFODrone(82.4,'sine',0.018,0.05,5);makeLFODrone(220,'sine',0.012,0.15,20);makeChord([82.4,110,130.8,164.8,196,220,261.6],0.018);makeNoise('white',0.015,5000,'highpass',0.4);break;
    case 'blackhole':makeNoise('brown',0.09,40,'lowpass',3.0);makeNoise('pink',0.04,200,'lowpass',2.0);makeLFODrone(5.5,'sine',0.08,0.02,1);makeLFODrone(11,'sine',0.055,0.03,2);makeLFODrone(22,'sine',0.035,0.04,3);makeNoise('white',0.012,18000,'highpass',0.5);makeLFODrone(880,'sawtooth',0.018,3.5,200);makeLFODrone(440,'sawtooth',0.022,2.8,150);makePulse(55,3500,0.035,0.8);makeChord([27.5,38.9,55,77.8],0.025);makeNoise('white',0.008,12000,'highpass',2);break;
    case 'cosmic_web':makeNoise('pink',0.025,300,'bandpass',1.0);makeNoise('brown',0.035,60,'lowpass',1.5);makeNoise('white',0.010,8000,'highpass',0.4);makeChord([16.4,20.6,27.5,32.7,41.2,55,82.4],0.015);makeLFODrone(16.4,'sine',0.04,0.03,2);makeLFODrone(20.6,'triangle',0.028,0.04,3);makeLFODrone(32.7,'sine',0.018,0.05,2.5);makeLFODrone(8200,'sine',0.005,0.8,200);makePulse(110,12000,0.012,1.5);break;
    case 'universe_edge':makeNoise('brown',0.06,30,'lowpass',2.5);makeNoise('pink',0.04,120,'bandpass',1.5);makeNoise('white',0.015,400,'bandpass',0.8);makeChord([6.875,10.9,16.4,20.6,27.5,41.2,55,82.4,110],0.012);makeLFODrone(6.875,'sine',0.055,0.01,0.5);makeLFODrone(13.75,'sine',0.038,0.015,0.8);makeLFODrone(27.5,'sine',0.025,0.02,1.2);makeLFODrone(55,'sine',0.018,0.03,1.5);makeLFODrone(110,'sine',0.012,0.04,2);makeLFODrone(220,'sine',0.008,0.05,2.5);makeNoise('white',0.025,15000,'highpass',0.3);makePulse(440,4200,0.018,2.5);makePulse(880,7800,0.012,1.8);makeReverb(12,0.5);break;
  }
  showSoundToast(SOUND_PROFILES[index]||'SPACE AMBIENCE');
}
function showSoundToast(name){const el=document.getElementById('soundToast');el.textContent='♪  '+name;el.classList.add('show');clearTimeout(el._tid);el._tid=setTimeout(()=>el.classList.remove('show'),3500);}
function tickVisualizer(){
  if(!analyserNode||!soundEnabled){requestAnimationFrame(tickVisualizer);return;}
  analyserNode.getByteFrequencyData(analyserData);
  const bars=['vb1','vb2','vb3','vb4','vb5'],slotSize=Math.floor(analyserData.length/bars.length);
  bars.forEach((id,i)=>{let sum=0;for(let j=i*slotSize;j<(i+1)*slotSize;j++)sum+=analyserData[j]||0;const avg=sum/slotSize;document.getElementById(id).style.height=(2+(avg/255)*22)+'px';});
  requestAnimationFrame(tickVisualizer);
}

function playWarpSound(rgb){
  if(!soundEnabled||!audioCtx)return;
  resumeAudio();
  const now=audioCtx.currentTime,baseFreq=80+(rgb[0]+rgb[1]+rgb[2])/3*0.5;
  const subOsc=audioCtx.createOscillator(),subGain=audioCtx.createGain();
  subOsc.type='sine';subOsc.frequency.setValueAtTime(baseFreq*2,now);subOsc.frequency.exponentialRampToValueAtTime(baseFreq*0.3,now+0.8);
  subGain.gain.setValueAtTime(0,now);subGain.gain.linearRampToValueAtTime(masterVolume*0.35,now+0.12);subGain.gain.exponentialRampToValueAtTime(0.001,now+1.0);
  subOsc.connect(subGain);subGain.connect(masterGain);subOsc.start(now);subOsc.stop(now+1.0);
  const carrier=audioCtx.createOscillator(),modulator=audioCtx.createOscillator(),fmGain=audioCtx.createGain(),metallicGain=audioCtx.createGain();
  carrier.type='triangle';modulator.type='sine';modulator.frequency.setValueAtTime(baseFreq*8,now);modulator.frequency.exponentialRampToValueAtTime(baseFreq*4,now+0.6);
  fmGain.gain.setValueAtTime(120,now);fmGain.gain.exponentialRampToValueAtTime(8,now+0.7);
  metallicGain.gain.setValueAtTime(0,now);metallicGain.gain.linearRampToValueAtTime(masterVolume*0.12,now+0.08);metallicGain.gain.exponentialRampToValueAtTime(0.001,now+0.9);
  modulator.connect(fmGain);fmGain.connect(carrier.frequency);carrier.connect(metallicGain);metallicGain.connect(masterGain);
  carrier.start(now);modulator.start(now);carrier.stop(now+0.9);modulator.stop(now+0.9);
  const snapNoise=audioCtx.createBufferSource(),snapFilter=audioCtx.createBiquadFilter(),snapGain=audioCtx.createGain();
  snapNoise.buffer=makeNoiseBuffer('white',0.3);snapFilter.type='bandpass';snapFilter.frequency.setValueAtTime(3500,now+0.35);snapFilter.Q.setValueAtTime(1.5,now+0.35);
  snapGain.gain.setValueAtTime(0,now+0.35);snapGain.gain.linearRampToValueAtTime(masterVolume*0.28,now+0.38);snapGain.gain.exponentialRampToValueAtTime(0.001,now+0.48);
  snapNoise.connect(snapFilter);snapFilter.connect(snapGain);snapGain.connect(masterGain);snapNoise.start(now+0.35);snapNoise.stop(now+0.48);
}

/* ══════════════════════════════════════════
   FULLSCREEN
══════════════════════════════════════════ */
function toggleFullscreen(){
  if(!document.fullscreenElement&&!document.webkitFullscreenElement){const el=document.documentElement;if(el.requestFullscreen)el.requestFullscreen();else if(el.webkitRequestFullscreen)el.webkitRequestFullscreen();}
  else{if(document.exitFullscreen)document.exitFullscreen();else if(document.webkitExitFullscreen)document.webkitExitFullscreen();}
}
document.addEventListener('fullscreenchange',updateFsBtn);document.addEventListener('webkitfullscreenchange',updateFsBtn);
function updateFsBtn(){const icon=document.getElementById('fsIcon'),lbl=document.getElementById('fsLabel'),btn=document.getElementById('fsBtn');if(document.fullscreenElement||document.webkitFullscreenElement){icon.innerHTML='<path d="M5 16h3v3h2v-5H5v2zm3-8H5v2h5V5H8v3zm6 11h2v-3h3v-2h-5v5zm2-11V5h-2v5h5V8h-3z"/>';lbl.textContent='EXIT';btn.style.borderColor='rgba(255,100,100,0.5)';btn.style.color='#ff6464';}else{icon.innerHTML='<path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/>';lbl.textContent='FULL';btn.style.borderColor='rgba(0,212,255,0.4)';btn.style.color='#00d4ff';}}

/* ══════════════════════════════════════════
   GYROSCOPE
══════════════════════════════════════════ */
let gyroEnabled=false,gyroX=0,gyroY=0,gyroCalibrated=false,gyroBaseBeta=0,gyroBaseGamma=0;
function checkGyroSupport(){const isTouch=('ontouchstart' in window)||navigator.maxTouchPoints>0;if(!isTouch)return;if(typeof DeviceOrientationEvent!=='undefined'&&typeof DeviceOrientationEvent.requestPermission==='function')document.getElementById('gyroBtn').style.display='flex';else if('DeviceOrientationEvent' in window)startGyro();}
function requestGyroPermission(){if(typeof DeviceOrientationEvent.requestPermission==='function'){DeviceOrientationEvent.requestPermission().then(state=>{if(state==='granted'){startGyro();document.getElementById('gyroBtn').style.display='none';document.getElementById('motionIndicator').style.display='flex';}}).catch(()=>startGyro());}else{startGyro();document.getElementById('gyroBtn').style.display='none';}}
function startGyro(){window.addEventListener('deviceorientation',onDeviceOrientation,true);gyroEnabled=true;document.getElementById('motionIndicator').style.display='flex';}
function onDeviceOrientation(e){if(e.beta===null||e.gamma===null)return;if(!gyroCalibrated){gyroBaseBeta=e.beta;gyroBaseGamma=e.gamma;gyroCalibrated=true;return;}const orient=window.screen&&window.screen.orientation?window.screen.orientation.angle:(window.orientation||0);let rawX,rawY;if(Math.abs(orient)===90){rawX=THREE.MathUtils.clamp((e.beta-gyroBaseBeta)/40,-1,1);rawY=THREE.MathUtils.clamp((e.gamma-gyroBaseGamma)/40,-1,1);}else{rawX=THREE.MathUtils.clamp((e.gamma-gyroBaseGamma)/40,-1,1);rawY=THREE.MathUtils.clamp((e.beta-gyroBaseBeta)/40,-1,1);}gyroX+=(rawX-gyroX)*0.15;gyroY+=(rawY-gyroY)*0.15;}
function recalibrateGyro(){gyroCalibrated=false;}
checkGyroSupport();

function handleNext(e){e.preventDefault();e.stopPropagation();nextDest();}
function handlePrev(e){e.preventDefault();e.stopPropagation();prevDest();}
function handleLaunch(e){e.preventDefault();e.stopPropagation();launchMission();}
function handleRestart(e){e.preventDefault();e.stopPropagation();restartMission();}

/* ══════════════════════════════════════════
   DESTINATIONS
══════════════════════════════════════════ */
const DESTINATIONS=[
  {name:"Earth",category:"SOLAR SYSTEM — INNER",desc:"Our pale blue dot — the only known harbor of life. Oceans cover 71% of its surface. A thin atmosphere shields 8 billion lives from the void.",distance:0,type:"earth",accentColor:"#1d6fa4",stats:[{v:"12,742 km",l:"Diameter"},{v:"1 AU",l:"From Sun"},{v:"4.5B yrs",l:"Age"},{v:"7.9B",l:"Population"}]},
  {name:"The Moon",category:"EARTH SYSTEM",desc:"Earth's ancient companion, sculpted by billions of years of impacts. 384,400 km away — humanity's first step into the cosmos.",distance:0.0000016,type:"moon",accentColor:"#9ca3af",stats:[{v:"3,474 km",l:"Diameter"},{v:"27.3 days",l:"Orbit"},{v:"-173°C",l:"Min Temp"},{v:"127°C",l:"Max Temp"}]},
  {name:"Mars",category:"SOLAR SYSTEM — INNER",desc:"The Red Planet. Olympus Mons stands 22 km tall. Ancient riverbeds hint at a wetter past. Humanity's next frontier.",distance:0.000042,type:"mars",accentColor:"#c1440e",stats:[{v:"6,779 km",l:"Diameter"},{v:"1.5 AU",l:"From Sun"},{v:"687 days",l:"Year"},{v:"-80°C",l:"Avg Temp"}]},
  {name:"Jupiter",category:"SOLAR SYSTEM — OUTER",desc:"The solar system's titan. The Great Red Spot — a storm three times Earth's size — has raged for 350+ years. 95 moons orbit its crushing gravity.",distance:0.00052,type:"jupiter",accentColor:"#c88b3a",stats:[{v:"139,820 km",l:"Diameter"},{v:"5.2 AU",l:"From Sun"},{v:"95 moons",l:"Satellites"},{v:"11.9 yrs",l:"Year"}]},
  {name:"Saturn",category:"SOLAR SYSTEM — OUTER",desc:"The jewel of the solar system. Rings spanning 282,000 km yet barely 10 meters thick — ice and rock in perfect gravitational harmony.",distance:0.0010,type:"saturn",accentColor:"#e8c97a",stats:[{v:"116,460 km",l:"Diameter"},{v:"9.5 AU",l:"From Sun"},{v:"146 moons",l:"Satellites"},{v:"0.687",l:"Density g/cm³"}]},
  {name:"Uranus",category:"SOLAR SYSTEM — OUTER",desc:"The tilted ice giant, rolling on its side at 98°. Methane absorbs red light, giving it an ethereal cyan hue.",distance:0.0019,type:"uranus",accentColor:"#4fd1c5",stats:[{v:"50,724 km",l:"Diameter"},{v:"19.2 AU",l:"From Sun"},{v:"98°",l:"Axial Tilt"},{v:"-224°C",l:"Avg Temp"}]},
  {name:"Neptune",category:"SOLAR SYSTEM — OUTER",desc:"The windiest world known — gusts reach 2,100 km/h. Its moon Triton orbits backwards, slowly spiraling toward a catastrophic end.",distance:0.0030,type:"neptune",accentColor:"#2b4eff",stats:[{v:"49,244 km",l:"Diameter"},{v:"30.1 AU",l:"From Sun"},{v:"2,100 km/h",l:"Winds"},{v:"-214°C",l:"Avg Temp"}]},
  {name:"Oort Cloud",category:"SOLAR SYSTEM BOUNDARY",desc:"A vast spherical shell of trillions of icy bodies, stretching up to 2 light-years from the Sun. Origin of long-period comets.",distance:0.5,type:"oort",accentColor:"#a0c4ff",stats:[{v:"1-2 ly",l:"Thickness"},{v:"Trillions",l:"Icy Bodies"},{v:"100,000 AU",l:"Max Dist"},{v:"-270°C",l:"Temp"}]},
  {name:"Proxima Centauri",category:"INTERSTELLAR SPACE",desc:"Our nearest stellar neighbor — a red dwarf 4.24 ly away. Proxima b orbits in the habitable zone, but fierce flares may strip away any atmosphere.",distance:4.24,type:"star",accentColor:"#ff6b35",stats:[{v:"Red Dwarf",l:"Type"},{v:"4.24 ly",l:"Distance"},{v:"Proxima b",l:"Exoplanet"},{v:"2,700°C",l:"Surface"}]},
  {name:"Galactic Center",category:"MILKY WAY",desc:"Sagittarius A* — 4 million solar masses compressed into a singularity. Stars orbit at 30 million km/h. The beating heart of our galaxy.",distance:26000,type:"galaxy_core",accentColor:"#ffd700",stats:[{v:"4M × Sun",l:"BH Mass"},{v:"26,000 ly",l:"Distance"},{v:"200-400B",l:"Stars"},{v:"100,000 ly",l:"Diameter"}]},
  {name:"Andromeda Galaxy",category:"LOCAL GROUP",desc:"2.5 million light-years away yet visible to the naked eye. One trillion stars. Racing toward us at 110 km/s — collision in 4.5 billion years.",distance:2537000,type:"galaxy",accentColor:"#c8b8ff",stats:[{v:"1 trillion",l:"Stars"},{v:"2.5M ly",l:"Distance"},{v:"220,000 ly",l:"Diameter"},{v:"110 km/s",l:"Approach"}]},
  {name:"TON 618",category:"DEEP UNIVERSE",desc:"A hyperluminous quasar — 66 billion solar masses. Its event horizon is larger than our entire solar system. Outshines 140 trillion suns.",distance:55000000,type:"blackhole",accentColor:"#8b00ff",stats:[{v:"66B × Sun",l:"Mass"},{v:"10.4B ly",l:"Distance"},{v:"1,300 AU",l:"Radius"},{v:"140T × Sun",l:"Luminosity"}]},
  {name:"Cosmic Web",category:"LARGE SCALE STRUCTURE",desc:"The universe's skeleton — vast filaments of dark matter and galaxies stretching billions of light-years, surrounding enormous cosmic voids.",distance:1000000000,type:"cosmic_web",accentColor:"#ff6bcb",stats:[{v:"Filaments",l:"Structure"},{v:"~100M ly",l:"Void Size"},{v:"Dark Matter",l:"Scaffold"},{v:"Billions",l:"Galaxies"}]},
  {name:"Edge of Universe",category:"COSMIC HORIZON",desc:"The observable universe's boundary — 46.5 billion light-years. Beyond this horizon, light hasn't had time to reach us since the Big Bang.",distance:46500000000,type:"universe_edge",accentColor:"#ff00ff",stats:[{v:"46.5B ly",l:"Radius"},{v:"93B ly",l:"Diameter"},{v:"2 Trillion",l:"Galaxies"},{v:"∞",l:"Beyond"}]},
];

/* ══════════════════════════════════════════
   THREE.JS
══════════════════════════════════════════ */
const canvas3d=document.getElementById('canvas3d');
const renderer=new THREE.WebGLRenderer({canvas:canvas3d,antialias:true,alpha:false,powerPreference:'high-performance'});
renderer.setPixelRatio(Math.min(window.devicePixelRatio,2));
renderer.setSize(window.innerWidth,window.innerHeight);
renderer.toneMapping=THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure=1.1;
renderer.shadowMap.enabled=true;
renderer.shadowMap.type=THREE.PCFSoftShadowMap;

const scene=new THREE.Scene();
scene.background=new THREE.Color(0x000005);
scene.fog=new THREE.FogExp2(0x000008,0.005);

const camera=new THREE.PerspectiveCamera(60,window.innerWidth/window.innerHeight,0.01,8000);
camera.position.set(0,2,10);

scene.add(new THREE.AmbientLight(0x111133,0.8));
const sunLight=new THREE.PointLight(0xfff5e0,4,200);
sunLight.position.set(15,15,15);sunLight.castShadow=true;scene.add(sunLight);
const rimLight=new THREE.DirectionalLight(0x0033ff,0.4);
rimLight.position.set(-8,4,-8);scene.add(rimLight);

/* ── TEXTURES ── */
function makeTex(size,fn){const c=document.createElement('canvas');c.width=c.height=size;fn(c.getContext('2d'),size);return new THREE.CanvasTexture(c);}
function makeCircleSprite(){const c=document.createElement('canvas');c.width=c.height=64;const ctx=c.getContext('2d'),grad=ctx.createRadialGradient(32,32,0,32,32,32);grad.addColorStop(0,'rgba(255,255,255,1)');grad.addColorStop(0.4,'rgba(255,255,255,0.8)');grad.addColorStop(1,'rgba(255,255,255,0)');ctx.fillStyle=grad;ctx.beginPath();ctx.arc(32,32,32,0,Math.PI*2);ctx.fill();return new THREE.CanvasTexture(c);}
const circleSprite=makeCircleSprite();

const earthTex=makeTex(512,(ctx,s)=>{const g=ctx.createRadialGradient(s/2,s/2,0,s/2,s/2,s/2);g.addColorStop(0,'#1a5276');g.addColorStop(1,'#0d2b45');ctx.fillStyle=g;ctx.fillRect(0,0,s,s);ctx.fillStyle='#2d7d32';[[100,120,90,60],[260,80,120,70],[320,180,80,50],[180,250,110,60],[80,280,60,40],[380,120,50,35]].forEach(([x,y,w,h])=>{ctx.beginPath();ctx.ellipse(x,y,w,h,Math.random(),0,Math.PI*2);ctx.fill();});ctx.fillStyle='#dde8f0';ctx.fillRect(0,0,s,28);ctx.fillRect(0,s-22,s,22);});
const moonTex=makeTex(512,(ctx,s)=>{ctx.fillStyle='#8a8a8a';ctx.fillRect(0,0,s,s);for(let i=0;i<60;i++){const x=Math.random()*s,y=Math.random()*s,r=Math.random()*18+3;const g=ctx.createRadialGradient(x,y,0,x,y,r);g.addColorStop(0,'rgba(55,55,55,0.9)');g.addColorStop(1,'rgba(138,138,138,0)');ctx.fillStyle=g;ctx.beginPath();ctx.arc(x,y,r,0,Math.PI*2);ctx.fill();}ctx.fillStyle='rgba(48,48,52,0.6)';[[150,180,80],[300,120,60],[200,300,50]].forEach(([x,y,r])=>{ctx.beginPath();ctx.arc(x,y,r,0,Math.PI*2);ctx.fill();});});
const marsTex=makeTex(512,(ctx,s)=>{const g=ctx.createLinearGradient(0,0,s,s);g.addColorStop(0,'#8b2500');g.addColorStop(0.5,'#c1440e');g.addColorStop(1,'#8b2500');ctx.fillStyle=g;ctx.fillRect(0,0,s,s);for(let i=0;i<30;i++){const x=Math.random()*s,y=Math.random()*s,r=Math.random()*20+5;const cg=ctx.createRadialGradient(x,y,0,x,y,r);cg.addColorStop(0,'rgba(50,8,0,0.8)');cg.addColorStop(1,'rgba(150,50,10,0)');ctx.fillStyle=cg;ctx.beginPath();ctx.arc(x,y,r,0,Math.PI*2);ctx.fill();}ctx.fillStyle='rgba(218,230,240,0.7)';ctx.beginPath();ctx.ellipse(s/2,18,s/3,22,0,0,Math.PI*2);ctx.fill();});
const jupiterTex=makeTex(512,(ctx,s)=>{[{y:0,h:40,c:'#c9a05a'},{y:40,h:30,c:'#b8784a'},{y:70,h:45,c:'#d4a860'},{y:115,h:25,c:'#c87840'},{y:140,h:50,c:'#e8c890'},{y:190,h:30,c:'#b86828'},{y:220,h:60,c:'#c9a05a'},{y:280,h:35,c:'#d4a860'},{y:315,h:45,c:'#c87840'},{y:360,h:40,c:'#e8c890'},{y:400,h:55,c:'#b86828'},{y:455,h:57,c:'#c9a05a'}].forEach(b=>{ctx.fillStyle=b.c;ctx.fillRect(0,b.y,s,b.h);});ctx.globalAlpha=0.25;for(let i=0;i<150;i++){ctx.fillStyle='rgba(180,120,60,0.4)';ctx.beginPath();ctx.ellipse(Math.random()*s,Math.random()*s,Math.random()*18+4,Math.random()*3+1,0,0,Math.PI*2);ctx.fill();}ctx.globalAlpha=1;const grs=ctx.createRadialGradient(s*.65,s*.55,0,s*.65,s*.55,38);grs.addColorStop(0,'rgba(170,45,18,0.95)');grs.addColorStop(1,'rgba(170,45,18,0)');ctx.fillStyle=grs;ctx.beginPath();ctx.ellipse(s*.65,s*.55,36,22,0,0,Math.PI*2);ctx.fill();});
const saturnTex=makeTex(512,(ctx,s)=>{[{y:0,h:50,c:'#e8d08a'},{y:50,h:35,c:'#d4b870'},{y:85,h:55,c:'#f0dca0'},{y:140,h:40,c:'#c8a850'},{y:180,h:65,c:'#e8d08a'},{y:245,h:45,c:'#d4b870'},{y:290,h:222,c:'#e8d08a'}].forEach(b=>{ctx.fillStyle=b.c;ctx.fillRect(0,b.y,s,b.h);});});

/* ══════════════════════════════════════════
   ASTEROID BUILDER — realistic lumpy rocks
══════════════════════════════════════════ */
function makeAsteroid(size=0.08, colorHex=0x8a7560){
  const geo = new THREE.DodecahedronGeometry(size, 1);
  const pos = geo.attributes.position;
  for(let i=0;i<pos.count;i++){
    const nx=pos.getX(i)+( Math.random()-0.5)*size*0.55;
    const ny=pos.getY(i)+(Math.random()-0.5)*size*0.55;
    const nz=pos.getZ(i)+(Math.random()-0.5)*size*0.55;
    pos.setXYZ(i,nx,ny,nz);
  }
  geo.computeVertexNormals();
  return new THREE.Mesh(geo,new THREE.MeshPhongMaterial({color:colorHex,shininess:4,flatShading:true}));
}

/* ══════════════════════════════════════════
   MOON BUILDER
══════════════════════════════════════════ */
function makeMoon(r,color,orbitR,orbitSpeed,orbitY=0,inclination=0){
  const m=new THREE.Mesh(new THREE.SphereGeometry(r,14,14),new THREE.MeshPhongMaterial({color,shininess:5,flatShading:false}));
  m.userData={orbitR,orbitSpeed,orbitAngle:Math.random()*Math.PI*2,orbitY,inclination};
  return m;
}

/* ══════════════════════════════════════════
   COMET BUILDER
══════════════════════════════════════════ */
function makeComet(g){
  const head=new THREE.Mesh(new THREE.SphereGeometry(0.04,8,8),new THREE.MeshBasicMaterial({color:0xaaddff}));
  // tail: cone pointing away from origin
  const tail=new THREE.Mesh(new THREE.ConeGeometry(0.015,0.4,6),new THREE.MeshBasicMaterial({color:0x88aaff,transparent:true,opacity:0.35,depthWrite:false}));
  tail.rotation.z=Math.PI/2;tail.position.x=-0.2;
  const comet=new THREE.Group();comet.add(head);comet.add(tail);
  const angle=Math.random()*Math.PI*2,r=5+Math.random()*4,y=(Math.random()-0.5)*3;
  comet.position.set(Math.cos(angle)*r,y,Math.sin(angle)*r);
  comet.userData={orbitR:r,orbitSpeed:0.002+Math.random()*0.003,orbitAngle:angle,orbitY:y,isComet:true};
  g.add(comet);
  return comet;
}

/* ══════════════════════════════════════════
   ATMOSPHERE / GLOW HELPERS
══════════════════════════════════════════ */
function makeAtmo(r,color,op=0.18){return new THREE.Mesh(new THREE.SphereGeometry(r*1.08,48,48),new THREE.MeshPhongMaterial({color,transparent:true,opacity:op,side:THREE.BackSide,shininess:0}));}
function makeGlowSphere(r,color,op=0.10){return new THREE.Mesh(new THREE.SphereGeometry(r*1.5,24,24),new THREE.MeshBasicMaterial({color,transparent:true,opacity:op,side:THREE.BackSide,depthWrite:false}));}

/* ══════════════════════════════════════════
   ASTEROID BELT BUILDER
══════════════════════════════════════════ */
function makeAsteroidBelt(g, count, innerR, outerR, ySpread=0.4, colorHex=0x8a7560, sizeMin=0.04, sizeMax=0.14){
  for(let i=0;i<count;i++){
    const ast=makeAsteroid(sizeMin+Math.random()*(sizeMax-sizeMin),colorHex);
    const angle=Math.random()*Math.PI*2;
    const r=innerR+Math.random()*(outerR-innerR);
    ast.position.set(Math.cos(angle)*r,(Math.random()-0.5)*ySpread,Math.sin(angle)*r);
    ast.rotation.set(Math.random()*Math.PI,Math.random()*Math.PI,Math.random()*Math.PI);
    ast.userData={orbitR:r,orbitSpeed:(0.0005+Math.random()*0.0015)*(Math.random()>0.5?1:-1),orbitAngle:angle,orbitY:ast.position.y,isAsteroid:true};
    g.add(ast);
  }
}

/* ══════════════════════════════════════════
   PLANET BUILDER — FULLY ENHANCED
══════════════════════════════════════════ */
function makePlanet(d){
  const g=new THREE.Group();
  const t=d.type;

  if(t==='earth'){
    const r=2.0;
    g.add(new THREE.Mesh(new THREE.SphereGeometry(r,64,64),new THREE.MeshPhongMaterial({map:earthTex,shininess:100,specular:new THREE.Color(0x4488cc)})));
    const clouds=new THREE.Mesh(new THREE.SphereGeometry(r+0.06,48,48),new THREE.MeshPhongMaterial({map:makeTex(512,(ctx,s)=>{ctx.clearRect(0,0,s,s);for(let i=0;i<70;i++){const x=Math.random()*s,y=Math.random()*s;const cg=ctx.createRadialGradient(x,y,0,x,y,Math.random()*38+12);cg.addColorStop(0,'rgba(255,255,255,0.9)');cg.addColorStop(1,'rgba(255,255,255,0)');ctx.fillStyle=cg;ctx.beginPath();ctx.ellipse(x,y,Math.random()*38+12,Math.random()*14+4,Math.random()*Math.PI,0,Math.PI*2);ctx.fill();}}),transparent:true,opacity:0.72,depthWrite:false}));
    clouds.userData.rotSpeed=0.0005;g.add(clouds);
    g.add(makeAtmo(r,0x4488ff,0.20));g.add(makeGlowSphere(r,0x2266ff,0.07));
    // ISS orbit (tiny)
    const iss=new THREE.Mesh(new THREE.BoxGeometry(0.06,0.015,0.03),new THREE.MeshPhongMaterial({color:0xccddee,shininess:80}));
    iss.userData={orbitR:r+0.18,orbitSpeed:0.022,orbitAngle:0,orbitY:0.1};g.add(iss);
    // Moon
    const moon=makeMoon(0.28,0x9a9a9a,r+1.8,0.004,0.05,0.09);moon.children;g.add(moon);
    // Near-Earth asteroid
    const nea=makeAsteroid(0.035,0x7a6a50);nea.userData={orbitR:r+2.5,orbitSpeed:0.0035,orbitAngle:1.2,orbitY:-0.2,isAsteroid:true};g.add(nea);
    // Debris cloud at L4
    makeAsteroidBelt(g,18,r+1.4,r+1.6,0.1,0x665544,0.015,0.03);

  } else if(t==='moon'){
    const r=1.1;
    g.add(new THREE.Mesh(new THREE.SphereGeometry(r,48,48),new THREE.MeshPhongMaterial({map:moonTex,shininess:4,specular:new THREE.Color(0x111111)})));
    // craters as dark bumps
    for(let i=0;i<8;i++){const c=new THREE.Mesh(new THREE.CircleGeometry(0.05+Math.random()*0.12,8),new THREE.MeshPhongMaterial({color:0x555555,shininess:2}));const phi=Math.random()*Math.PI,theta=Math.random()*Math.PI*2;c.position.set(r*1.001*Math.sin(phi)*Math.cos(theta),r*1.001*Math.sin(phi)*Math.sin(theta),r*1.001*Math.cos(phi));c.lookAt(0,0,0);c.rotateX(Math.PI/2);g.add(c);}
    // Orbiting rocks
    makeAsteroidBelt(g,12,r+0.4,r+0.7,0.06,0x888888,0.012,0.03);

  } else if(t==='mars'){
    const r=1.4;
    g.add(new THREE.Mesh(new THREE.SphereGeometry(r,64,64),new THREE.MeshPhongMaterial({map:marsTex,shininess:8})));
    g.add(makeAtmo(r,0xcc6633,0.09));g.add(makeGlowSphere(r,0xdd7744,0.05));
    // Phobos
    const phobos=makeMoon(0.08,0x887060,r+0.5,0.018,0.02);g.add(phobos);
    // Deimos
    const deimos=makeMoon(0.05,0x998070,r+0.9,0.008,-0.06);g.add(deimos);
    // Mars trojans & surface rocks
    makeAsteroidBelt(g,25,r+1.1,r+1.5,0.12,0x8b5c30,0.02,0.06);
    // Olympus Mons hint (large bump)
    const mons=new THREE.Mesh(new THREE.ConeGeometry(0.22,0.14,8),new THREE.MeshPhongMaterial({color:0xa03010,shininess:3,flatShading:true}));mons.position.set(r*0.7,r*0.7,0);mons.lookAt(0,0,0);g.add(mons);

  } else if(t==='jupiter'){
    const r=2.8;
    g.add(new THREE.Mesh(new THREE.SphereGeometry(r,64,64),new THREE.MeshPhongMaterial({map:jupiterTex,shininess:18})));
    g.add(makeGlowSphere(r,0xff9933,0.06));
    // Galilean moons
    const moonsData=[{r:0.18,c:0xddcc88,orR:r+1.0,spd:0.016},{r:0.19,c:0x886644,orR:r+1.6,spd:0.011},{r:0.22,c:0x7799cc,orR:r+2.2,spd:0.008},{r:0.20,c:0x998877,orR:r+2.9,spd:0.005}];
    moonsData.forEach(m=>{g.add(makeMoon(m.r,m.c,m.orR,m.spd,0));});
    // Inner asteroid/debris ring
    makeAsteroidBelt(g,30,r+0.5,r+0.8,0.05,0xaa8855,0.015,0.035);
    // Trojan asteroids L4/L5 (further out)
    makeAsteroidBelt(g,40,r+3.8,r+4.5,0.3,0x7a6040,0.02,0.055);
    // Thin faint ring
    const ring=new THREE.Mesh(new THREE.RingGeometry(r+0.4,r+0.55,64),new THREE.MeshBasicMaterial({color:0xaa8844,side:THREE.DoubleSide,transparent:true,opacity:0.15,depthWrite:false}));ring.rotation.x=Math.PI/2;g.add(ring);

  } else if(t==='saturn'){
    const r=2.4;
    g.add(new THREE.Mesh(new THREE.SphereGeometry(r,64,64),new THREE.MeshPhongMaterial({map:saturnTex,shininess:22})));
    // Layered rings
    [{ir:r*1.12,or:r*1.3,c:0x9a8060,op:0.28},{ir:r*1.30,or:r*1.56,c:0xd4a870,op:0.68},{ir:r*1.56,or:r*2.00,c:0xe8c890,op:0.82},{ir:r*2.02,or:r*2.06,c:0x221108,op:0.92},{ir:r*2.06,or:r*2.45,c:0xd4b870,op:0.58},{ir:r*2.48,or:r*2.6,c:0xa89060,op:0.22}].forEach(rd=>{const ring=new THREE.Mesh(new THREE.RingGeometry(rd.ir,rd.or,128),new THREE.MeshBasicMaterial({color:rd.c,side:THREE.DoubleSide,transparent:true,opacity:rd.op,depthWrite:false}));ring.rotation.x=-Math.PI/2.5+0.05;g.add(ring);});
    // Ring asteroids/ice chunks
    makeAsteroidBelt(g,50,r*1.35,r*1.95,0.015,0xd4c8a0,0.008,0.025);
    // Major moons
    g.add(makeMoon(0.24,0xddcc99,r+3.2,0.005,0,0));    // Titan
    g.add(makeMoon(0.12,0xffffff,r+2.6,0.008,0.08,0.02)); // Enceladus
    g.add(makeMoon(0.10,0x998877,r+4.0,0.003,-0.1,0.01)); // Iapetus
    g.add(makeMoon(0.09,0x777788,r+1.5,0.014,0.04,0.03)); // Mimas
    // Tiny shepherd moons
    g.add(makeMoon(0.03,0xccbbaa,r*2.52,0.012,0.002,0));
    g.add(makeMoon(0.03,0xccbbaa,r*1.08,0.018,-0.002,0));

  } else if(t==='uranus'){
    const r=1.9;
    g.add(new THREE.Mesh(new THREE.SphereGeometry(r,48,48),new THREE.MeshPhongMaterial({color:0x4fd1c5,emissive:0x052220,shininess:70,specular:new THREE.Color(0x66dddd)})));
    [[r*1.3,r*1.5,0.28],[r*1.5,r*1.65,0.42],[r*1.68,r*1.8,0.18]].forEach(([ir,or,op])=>{const ring=new THREE.Mesh(new THREE.RingGeometry(ir,or,64),new THREE.MeshBasicMaterial({color:0x88cccc,side:THREE.DoubleSide,transparent:true,opacity:op,depthWrite:false}));ring.rotation.z=Math.PI/2+0.05;g.add(ring);});
    g.add(makeAtmo(r,0x00cccc,0.16));g.add(makeGlowSphere(r,0x00eedd,0.07));
    // Moons (all tilted orbit like Uranus)
    g.add(makeMoon(0.14,0xaabb99,r+1.1,0.010,0,Math.PI/2));  // Titania
    g.add(makeMoon(0.12,0x99aabb,r+1.6,0.007,0,Math.PI/2));  // Oberon
    g.add(makeMoon(0.09,0xbbaacc,r+0.7,0.016,0,Math.PI/2));  // Umbriel
    // Dark ring particles
    makeAsteroidBelt(g,20,r*1.32,r*1.48,0.005,0x225555,0.008,0.018);

  } else if(t==='neptune'){
    const r=1.8;
    g.add(new THREE.Mesh(new THREE.SphereGeometry(r,48,48),new THREE.MeshPhongMaterial({color:0x2b4eff,emissive:0x020830,shininess:80,specular:new THREE.Color(0x4466ff)})));
    g.add(makeAtmo(r,0x2244ff,0.18));g.add(makeGlowSphere(r,0x3355ff,0.09));
    // Triton — retrograde (negative speed)
    const triton=makeMoon(0.16,0xccddee,r+1.4,-0.009,0.1,0.15);g.add(triton);
    // Nereid
    g.add(makeMoon(0.05,0xaabbcc,r+2.8,0.003,-0.3,0.05));
    // Adams ring
    const adamsRing=new THREE.Mesh(new THREE.RingGeometry(r+1.1,r+1.14,64),new THREE.MeshBasicMaterial({color:0x4466aa,side:THREE.DoubleSide,transparent:true,opacity:0.22,depthWrite:false}));adamsRing.rotation.x=Math.PI/2+0.08;g.add(adamsRing);
    // Storm spots (dark ovals)
    const gds=new THREE.Mesh(new THREE.SphereGeometry(r*0.18,12,8),new THREE.MeshPhongMaterial({color:0x112288,shininess:0,transparent:true,opacity:0.7}));gds.position.set(r*0.8,r*0.3,r*0.3);g.add(gds);

  } else if(t==='oort'){
    // Icy bodies cloud
    for(let i=0;i<700;i++){const phi=Math.acos(2*Math.random()-1),theta=Math.random()*Math.PI*2,r=5+Math.random()*3.5;const m=new THREE.Mesh(new THREE.SphereGeometry(0.012+Math.random()*0.05,4,4),new THREE.MeshBasicMaterial({color:new THREE.Color(0.5+Math.random()*0.3,0.6+Math.random()*0.2,0.8+Math.random()*0.2),transparent:true,opacity:0.5+Math.random()*0.5}));m.position.set(r*Math.sin(phi)*Math.cos(theta),r*Math.sin(phi)*Math.sin(theta),r*Math.cos(phi));m.userData={orbitR:r,orbitSpeed:0.0001+Math.random()*0.0003,orbitAngle:theta,orbitY:m.position.y,isAsteroid:true};g.add(m);}
    // Shell wireframe
    g.add(new THREE.Mesh(new THREE.SphereGeometry(7,32,32),new THREE.MeshBasicMaterial({color:0x8aacdd,wireframe:true,transparent:true,opacity:0.025})));
    // Comets
    for(let i=0;i<5;i++)makeComet(g);

  } else if(t==='star'){
    const r=1.6;
    const coreTex=makeTex(256,(ctx,s)=>{const gr=ctx.createRadialGradient(s/2,s/2,0,s/2,s/2,s/2);gr.addColorStop(0,'#fff8f0');gr.addColorStop(0.25,'#ffcc88');gr.addColorStop(0.5,'#ff8844');gr.addColorStop(0.75,'#ff4400');gr.addColorStop(1,'#cc2200');ctx.fillStyle=gr;ctx.fillRect(0,0,s,s);});
    g.add(new THREE.Mesh(new THREE.SphereGeometry(r,48,48),new THREE.MeshBasicMaterial({map:coreTex})));
    [{scale:1.25,color:0xff9944,op:0.18},{scale:1.55,color:0xff7722,op:0.10},{scale:1.90,color:0xff5500,op:0.055},{scale:2.40,color:0xff3300,op:0.028},{scale:3.20,color:0xff2200,op:0.012}].forEach(gl=>{g.add(new THREE.Mesh(new THREE.SphereGeometry(r*gl.scale,32,32),new THREE.MeshBasicMaterial({color:gl.color,transparent:true,opacity:gl.op,side:THREE.BackSide,depthWrite:false,blending:THREE.AdditiveBlending})));});
    const coronaMat=new THREE.MeshBasicMaterial({color:0xff6622,transparent:true,opacity:0.08,side:THREE.BackSide,depthWrite:false,blending:THREE.AdditiveBlending});
    const corona=new THREE.Mesh(new THREE.SphereGeometry(r*2.8,16,16),coronaMat);corona.userData.pulse=true;g.add(corona);
    g.add(new THREE.PointLight(0xff6633,5,50));
    // Proxima b exoplanet
    const proxb=new THREE.Mesh(new THREE.SphereGeometry(0.18,20,20),new THREE.MeshPhongMaterial({color:0x336688,shininess:40}));
    proxb.userData={orbitR:r+2.2,orbitSpeed:0.006,orbitAngle:0,orbitY:0.05};g.add(proxb);
    // Exoplanet atmosphere glow
    const proxAtmo=new THREE.Mesh(new THREE.SphereGeometry(0.22,16,16),new THREE.MeshBasicMaterial({color:0x4488aa,transparent:true,opacity:0.12,side:THREE.BackSide}));
    proxAtmo.userData={orbitR:r+2.2,orbitSpeed:0.006,orbitAngle:0,orbitY:0.05};g.add(proxAtmo);
    // Solar flare arcs
    for(let i=0;i<3;i++){const arc=new THREE.Mesh(new THREE.TorusGeometry(r*1.15+i*0.08,0.018,6,24,Math.PI*0.7),new THREE.MeshBasicMaterial({color:0xff8822,transparent:true,opacity:0.22-i*0.06,depthWrite:false,blending:THREE.AdditiveBlending}));arc.rotation.set(Math.random()*Math.PI,Math.random()*Math.PI,0);arc.userData.rotSpeed=0.004+i*0.002;g.add(arc);}
    // Asteroid debris field around star
    makeAsteroidBelt(g,20,r+3.0,r+4.0,0.2,0x885533,0.02,0.05);

  } else if(t==='galaxy_core'){
    // Dense star cluster
    for(let i=0;i<1000;i++){const r=Math.pow(Math.random(),1.5)*4,theta=Math.random()*Math.PI*2,phi=(Math.random()-0.5)*0.7;const b=Math.max(0.2,1-r/5);const m=new THREE.Mesh(new THREE.SphereGeometry(0.008+Math.random()*0.04,4,4),new THREE.MeshBasicMaterial({color:new THREE.Color(b,b*0.85,b*0.4),transparent:true,opacity:0.6+Math.random()*0.4}));m.position.set(r*Math.cos(theta),r*Math.sin(phi)*0.5,r*Math.sin(theta));g.add(m);}
    // 4 spiral arms
    for(let arm=0;arm<4;arm++){for(let i=0;i<400;i++){const t2=i/400,angle=arm*(Math.PI/2)+t2*Math.PI*2.5,r=0.5+t2*8;const m=new THREE.Mesh(new THREE.SphereGeometry(0.012+Math.random()*0.032,3,3),new THREE.MeshBasicMaterial({color:new THREE.Color(1-t2*0.6,(1-t2*0.6)*0.75,(1-t2*0.6)*0.25),transparent:true,opacity:(0.7-t2*0.4)*(0.5+Math.random()*0.5)}));m.position.set(r*Math.cos(angle)+(Math.random()-0.5)*0.8,(Math.random()-0.5)*0.5*Math.exp(-t2*2),r*Math.sin(angle)+(Math.random()-0.5)*0.8);g.add(m);}}
    // Central BH
    g.add(new THREE.Mesh(new THREE.SphereGeometry(0.6,16,16),new THREE.MeshBasicMaterial({color:0xffeeaa,transparent:true,opacity:0.95})));
    g.add(new THREE.Mesh(new THREE.SphereGeometry(1.2,16,16),new THREE.MeshBasicMaterial({color:0xffcc44,transparent:true,opacity:0.15,side:THREE.BackSide})));
    g.add(new THREE.PointLight(0xffd700,4,25));
    // Accretion disk
    const accDisk=new THREE.Mesh(new THREE.RingGeometry(0.7,2.0,64),new THREE.MeshBasicMaterial({color:0xffaa00,side:THREE.DoubleSide,transparent:true,opacity:0.3,depthWrite:false,blending:THREE.AdditiveBlending}));accDisk.rotation.x=Math.PI/2+0.1;accDisk.userData.rotSpeed=0.008;g.add(accDisk);
    // Stellar streams (random bright streaks)
    for(let i=0;i<6;i++){const pts=[new THREE.Vector3(0,0,0),new THREE.Vector3((Math.random()-0.5)*10,(Math.random()-0.5)*3,(Math.random()-0.5)*10)];const geo2=new THREE.BufferGeometry().setFromPoints(pts);g.add(new THREE.Line(geo2,new THREE.LineBasicMaterial({color:0xffddaa,transparent:true,opacity:0.08})));}
    // Globular clusters
    for(let gc=0;gc<4;gc++){const gcG=new THREE.Group();for(let i=0;i<30;i++){const m=new THREE.Mesh(new THREE.SphereGeometry(0.015+Math.random()*0.02,4,4),new THREE.MeshBasicMaterial({color:0xffeedd,transparent:true,opacity:0.7+Math.random()*0.3}));m.position.set((Math.random()-0.5)*0.5,(Math.random()-0.5)*0.5,(Math.random()-0.5)*0.5);gcG.add(m);}const angle=gc*(Math.PI/2)+Math.random();const r=5+Math.random()*3;gcG.position.set(r*Math.cos(angle),(Math.random()-0.5)*2,r*Math.sin(angle));g.add(gcG);}

  } else if(t==='galaxy'){
    // Andromeda — 3 massive spiral arms + bulge + halo
    // Bulge
    for(let i=0;i<400;i++){const r=Math.pow(Math.random(),2)*2,theta=Math.random()*Math.PI*2,phi=(Math.random()-0.5)*0.8;const b=0.8+Math.random()*0.2;const m=new THREE.Mesh(new THREE.SphereGeometry(0.01+Math.random()*0.03,3,3),new THREE.MeshBasicMaterial({color:new THREE.Color(b,b*0.9,b*0.65),transparent:true,opacity:0.6+Math.random()*0.4}));m.position.set(r*Math.cos(theta),r*Math.sin(phi)*0.4,r*Math.sin(theta));g.add(m);}
    // Spiral arms
    for(let arm=0;arm<3;arm++){for(let i=0;i<800;i++){const t2=i/800,angle=arm*(Math.PI*2/3)+t2*Math.PI*3.2,r=0.2+t2*7,h=0.65+t2*0.28;const m=new THREE.Mesh(new THREE.SphereGeometry(0.010+Math.random()*0.022,3,3),new THREE.MeshBasicMaterial({color:new THREE.Color(h*0.72,h*0.76,Math.min(1,h*1.1)),transparent:true,opacity:(0.8-t2*0.5)*(0.4+Math.random()*0.6)}));m.position.set(r*Math.cos(angle)+(Math.random()-0.5)*(1-t2)*0.7,(Math.random()-0.5)*0.35*Math.exp(-t2*1.5),r*Math.sin(angle)+(Math.random()-0.5)*(1-t2)*0.7);g.add(m);}}
    // H-II regions (bright pink star-forming blobs)
    for(let i=0;i<12;i++){const angle=Math.random()*Math.PI*2,r=1.5+Math.random()*4;const hii=new THREE.Mesh(new THREE.SphereGeometry(0.06+Math.random()*0.08,6,6),new THREE.MeshBasicMaterial({color:new THREE.Color(1,0.4+Math.random()*0.3,0.6+Math.random()*0.2),transparent:true,opacity:0.5+Math.random()*0.4,blending:THREE.AdditiveBlending,depthWrite:false}));hii.position.set(r*Math.cos(angle),(Math.random()-0.5)*0.3,r*Math.sin(angle));g.add(hii);}
    // Dark dust lanes
    for(let i=0;i<8;i++){const angle=Math.random()*Math.PI*2,r=0.8+Math.random()*4;const dust=new THREE.Mesh(new THREE.SphereGeometry(0.08+Math.random()*0.2,5,5),new THREE.MeshBasicMaterial({color:0x111111,transparent:true,opacity:0.15+Math.random()*0.2}));dust.position.set(r*Math.cos(angle),(Math.random()-0.5)*0.1,r*Math.sin(angle));dust.scale.set(3,0.4,1);dust.rotation.y=angle;g.add(dust);}
    // Halo globular clusters
    for(let i=0;i<8;i++){const phi=Math.acos(2*Math.random()-1),theta=Math.random()*Math.PI*2,r=5+Math.random()*4;const cl=new THREE.Group();for(let j=0;j<20;j++){const m=new THREE.Mesh(new THREE.SphereGeometry(0.012+Math.random()*0.018,3,3),new THREE.MeshBasicMaterial({color:0xffeecc,transparent:true,opacity:0.6+Math.random()*0.4}));m.position.set((Math.random()-0.5)*0.4,(Math.random()-0.5)*0.4,(Math.random()-0.5)*0.4);cl.add(m);}cl.position.set(r*Math.sin(phi)*Math.cos(theta),r*Math.sin(phi)*Math.sin(theta)*0.3,r*Math.cos(phi));g.add(cl);}
    // Satellite galaxies (M32, M110)
    [[-5,1,-3],[4,-0.5,5]].forEach(([x,y,z])=>{const sat=new THREE.Group();for(let i=0;i<80;i++){const r=Math.random()*0.4,th=Math.random()*Math.PI*2,ph=Math.random()*Math.PI;const m=new THREE.Mesh(new THREE.SphereGeometry(0.008+Math.random()*0.015,3,3),new THREE.MeshBasicMaterial({color:0xffddbb,transparent:true,opacity:0.5+Math.random()*0.5}));m.position.set(r*Math.sin(ph)*Math.cos(th),r*Math.sin(ph)*Math.sin(th)*0.5,r*Math.cos(ph));sat.add(m);}sat.position.set(x,y,z);g.add(sat);});
    g.add(new THREE.Mesh(new THREE.SphereGeometry(1.5,8,8),new THREE.MeshBasicMaterial({color:0xbbbbff,transparent:true,opacity:0.06,side:THREE.BackSide})));

  } else if(t==='blackhole'){
    const r=1.8;
    g.add(new THREE.Mesh(new THREE.SphereGeometry(r,64,64),new THREE.MeshBasicMaterial({color:0x000000})));
    g.add(new THREE.Mesh(new THREE.SphereGeometry(r*1.05,32,32),new THREE.MeshBasicMaterial({color:0x334488,transparent:true,opacity:0.12,side:THREE.BackSide,depthWrite:false})));
    // Photon sphere
    const photonSphere=new THREE.Mesh(new THREE.SphereGeometry(r*1.5,32,32),new THREE.MeshBasicMaterial({color:0xffdd44,transparent:true,opacity:0.04,side:THREE.BackSide,depthWrite:false,blending:THREE.AdditiveBlending}));g.add(photonSphere);
    // Accretion disk layers
    [{ir:r*1.3,or:r*1.6,c:new THREE.Color(1.0,0.9,0.4),op:0.9},{ir:r*1.6,or:r*2.0,c:new THREE.Color(1.0,0.5,0.1),op:0.75},{ir:r*2.0,or:r*2.5,c:new THREE.Color(0.9,0.2,0.05),op:0.55},{ir:r*2.5,or:r*3.2,c:new THREE.Color(0.5,0.1,0.02),op:0.35},{ir:r*3.2,or:r*4.0,c:new THREE.Color(0.2,0.04,0.01),op:0.15}].forEach((dk,idx)=>{const ring=new THREE.Mesh(new THREE.RingGeometry(dk.ir,dk.or,128),new THREE.MeshBasicMaterial({color:dk.c,side:THREE.DoubleSide,transparent:true,opacity:dk.op,depthWrite:false,blending:THREE.AdditiveBlending}));ring.rotation.x=Math.PI*0.12;ring.userData.rotSpeed=(0.007-idx*0.001)*(idx%2?1:-1);g.add(ring);});
    // Relativistic jets
    [1,-1].forEach(dir=>{const jet=new THREE.Mesh(new THREE.CylinderGeometry(0,0.35,12,16,6,true),new THREE.MeshBasicMaterial({color:0x00aaff,side:THREE.DoubleSide,transparent:true,opacity:0.10,depthWrite:false,blending:THREE.AdditiveBlending}));jet.position.y=dir*6;if(dir<0)jet.rotation.x=Math.PI;jet.userData.rotSpeed=0.003;g.add(jet);});
    // Stars being torn apart (tidal disruption)
    for(let i=0;i<8;i++){const angle=i*(Math.PI*2/8),rad=r*3.5+Math.random()*r;const star=new THREE.Mesh(new THREE.SphereGeometry(0.04+Math.random()*0.06,6,6),new THREE.MeshBasicMaterial({color:new THREE.Color(1,0.8+Math.random()*0.2,0.4),transparent:true,opacity:0.7+Math.random()*0.3,blending:THREE.AdditiveBlending,depthWrite:false}));star.position.set(Math.cos(angle)*rad,( Math.random()-0.5)*0.3,Math.sin(angle)*rad);star.userData={orbitR:rad,orbitSpeed:0.004+Math.random()*0.006,orbitAngle:angle,orbitY:star.position.y,isAsteroid:true};g.add(star);}
    // Gravitational lens rings
    for(let i=0;i<3;i++){const lr=new THREE.Mesh(new THREE.TorusGeometry(r*1.6+i*0.4,0.03,8,64),new THREE.MeshBasicMaterial({color:0xffeebb,transparent:true,opacity:0.12-i*0.03,depthWrite:false,blending:THREE.AdditiveBlending}));lr.rotation.x=Math.PI/2+(i*0.15);lr.userData.rotSpeed=0.002*(i%2?1:-1);g.add(lr);}
    g.add(new THREE.PointLight(0xff6600,3,30));g.add(makeGlowSphere(r,0x441100,0.22));

  } else if(t==='cosmic_web'){
    // Filaments
    for(let f=0;f<40;f++){const pts=[];let x=(Math.random()-0.5)*5,y=(Math.random()-0.5)*5,z=(Math.random()-0.5)*5;pts.push(new THREE.Vector3(x,y,z));for(let p=1;p<16;p++){x+=(Math.random()-0.5)*1.6;y+=(Math.random()-0.5)*0.7;z+=(Math.random()-0.5)*1.6;pts.push(new THREE.Vector3(x,y,z));}const curve=new THREE.CatmullRomCurve3(pts);const filGeo=new THREE.TubeGeometry(curve,40,0.005+Math.random()*0.012,5,false);g.add(new THREE.Mesh(filGeo,new THREE.MeshBasicMaterial({color:new THREE.Color(0.4+Math.random()*0.3,0.3+Math.random()*0.2,0.6+Math.random()*0.3),transparent:true,opacity:0.1+Math.random()*0.2,depthWrite:false})));}
    // Galaxy clusters at filament intersections
    for(let i=0;i<50;i++){const angle=Math.random()*Math.PI*2,r=Math.random()*7;const cl=new THREE.Group();for(let j=0;j<12;j++){const m=new THREE.Mesh(new THREE.SphereGeometry(0.02+Math.random()*0.045,4,4),new THREE.MeshBasicMaterial({color:new THREE.Color(0.7+Math.random()*0.2,0.7+Math.random()*0.2,0.9+Math.random()*0.1),transparent:true,opacity:0.45+Math.random()*0.5}));m.position.set((Math.random()-0.5)*0.5,(Math.random()-0.5)*0.4,(Math.random()-0.5)*0.5);cl.add(m);}cl.position.set(Math.cos(angle)*r,(Math.random()-0.5)*4,Math.sin(angle)*r);g.add(cl);}
    // Mini galaxy spirals scattered
    for(let i=0;i<8;i++){const mg=new THREE.Group();for(let j=0;j<60;j++){const t2=j/60,angle2=t2*Math.PI*4,rr=0.1+t2*0.5;const m=new THREE.Mesh(new THREE.SphereGeometry(0.008+Math.random()*0.012,3,3),new THREE.MeshBasicMaterial({color:new THREE.Color(0.6+Math.random()*0.4,0.6+Math.random()*0.4,1),transparent:true,opacity:0.4+Math.random()*0.5}));m.position.set(rr*Math.cos(angle2),(Math.random()-0.5)*0.08,rr*Math.sin(angle2));mg.add(m);}const phi=Math.acos(2*Math.random()-1),theta2=Math.random()*Math.PI*2,rr=2+Math.random()*5;mg.position.set(rr*Math.sin(phi)*Math.cos(theta2),(Math.random()-0.5)*3,rr*Math.cos(phi));mg.rotation.set(Math.random()*Math.PI,Math.random()*Math.PI,0);g.add(mg);}
    // Quasar-like bright point sources in voids
    for(let i=0;i<5;i++){const qsr=new THREE.Mesh(new THREE.SphereGeometry(0.06+Math.random()*0.04,8,8),new THREE.MeshBasicMaterial({color:0xffffff,transparent:true,opacity:0.9,blending:THREE.AdditiveBlending,depthWrite:false}));const angle=Math.random()*Math.PI*2,r=3+Math.random()*4;qsr.position.set(Math.cos(angle)*r,(Math.random()-0.5)*3,Math.sin(angle)*r);g.add(qsr);}

  } else if(t==='universe_edge'){
    // CMB background
    const cmbTex=makeTex(512,(ctx,s)=>{for(let i=0;i<s;i+=4){for(let j=0;j<s;j+=4){const n=Math.sin(i*0.08)*Math.cos(j*0.06)+Math.sin(i*0.13+j*0.09)*0.5;const t2=(n+1.5)/3;ctx.fillStyle=`rgb(${Math.floor(200+t2*55)},${Math.floor(80+t2*38)},${Math.floor(50+t2*24)})`;ctx.fillRect(i,j,4,4);}}});
    g.add(new THREE.Mesh(new THREE.SphereGeometry(9,48,48),new THREE.MeshBasicMaterial({map:cmbTex,side:THREE.BackSide,transparent:true,opacity:0.55})));
    // Primordial galaxies (many, varied)
    for(let i=0;i<1800;i++){const phi=Math.acos(2*Math.random()-1),theta=Math.random()*Math.PI*2,r=3+Math.random()*5;const hue=Math.random();let col=hue<0.35?new THREE.Color(1,0.85,0.6):hue<0.65?new THREE.Color(0.6,0.7,1.0):new THREE.Color(1,0.5,0.3);col.multiplyScalar(0.4+Math.random()*0.6);const m=new THREE.Mesh(new THREE.SphereGeometry(0.012+Math.random()*0.04,4,4),new THREE.MeshBasicMaterial({color:col,transparent:true,opacity:0.3+Math.random()*0.6}));m.position.set(r*Math.sin(phi)*Math.cos(theta),r*Math.sin(phi)*Math.sin(theta),r*Math.cos(phi));g.add(m);}
    // First-light galaxy clusters
    for(let i=0;i<10;i++){const cl=new THREE.Group();const angle=Math.random()*Math.PI*2,r=4+Math.random()*3;for(let j=0;j<25;j++){const m=new THREE.Mesh(new THREE.SphereGeometry(0.02+Math.random()*0.035,4,4),new THREE.MeshBasicMaterial({color:new THREE.Color(1,0.7+Math.random()*0.3,0.4+Math.random()*0.3),transparent:true,opacity:0.5+Math.random()*0.5}));m.position.set((Math.random()-0.5)*0.6,(Math.random()-0.5)*0.5,(Math.random()-0.5)*0.6);cl.add(m);}cl.position.set(Math.cos(angle)*r,(Math.random()-0.5)*3,Math.sin(angle)*r);g.add(cl);}
    // Expanding universe rings
    for(let i=0;i<6;i++){const ring=new THREE.Mesh(new THREE.TorusGeometry(2.5+i*0.8,0.025,8,128),new THREE.MeshBasicMaterial({color:new THREE.Color(0.8,0.2+i*0.1,0.8-i*0.1),transparent:true,opacity:0.07-i*0.008,depthWrite:false,blending:THREE.AdditiveBlending}));ring.rotation.x=Math.random()*Math.PI;ring.rotation.y=Math.random()*Math.PI;ring.userData.rotSpeed=0.0006*(i%2?1:-1);g.add(ring);}
    // Singularity
    g.add(new THREE.Mesh(new THREE.SphereGeometry(0.55,16,16),new THREE.MeshBasicMaterial({color:0xffffff,transparent:true,opacity:0.95})));
    g.add(new THREE.Mesh(new THREE.SphereGeometry(1.3,16,16),new THREE.MeshBasicMaterial({color:0xffaaff,transparent:true,opacity:0.18,side:THREE.BackSide})));
    // Big bang remnant filaments
    for(let f=0;f<15;f++){const pts=[];let x=0,y=0,z=0;for(let p=0;p<8;p++){const angle=Math.random()*Math.PI*2,phi2=Math.acos(2*Math.random()-1);const step=0.5+Math.random()*0.5;x+=Math.sin(phi2)*Math.cos(angle)*step;y+=Math.sin(phi2)*Math.sin(angle)*step;z+=Math.cos(phi2)*step;pts.push(new THREE.Vector3(x,y,z));}if(pts.length>1){const curve=new THREE.CatmullRomCurve3(pts);const geo2=new THREE.TubeGeometry(curve,20,0.012+Math.random()*0.02,4,false);g.add(new THREE.Mesh(geo2,new THREE.MeshBasicMaterial({color:new THREE.Color(0.9,0.5+Math.random()*0.5,0.9),transparent:true,opacity:0.08+Math.random()*0.1,depthWrite:false,blending:THREE.AdditiveBlending})));}}
    g.add(new THREE.PointLight(0xcc00ff,4,35));
    g.add(makeGlowSphere(7,0x440088,0.04));
  }
  return g;
}

/* ══════════════════════════════════════════
   ENHANCED STARFIELD — 5 layers of depth
══════════════════════════════════════════ */
function createStarfield(){
  const count=16000;
  const geo=new THREE.BufferGeometry();
  const pos=new Float32Array(count*3),col=new Float32Array(count*3),sizes=new Float32Array(count);
  for(let i=0;i<count;i++){
    const theta=Math.random()*Math.PI*2,phi=Math.acos(2*Math.random()-1),r=200+Math.random()*800;
    pos[i*3]=r*Math.sin(phi)*Math.cos(theta);pos[i*3+1]=r*Math.sin(phi)*Math.sin(theta);pos[i*3+2]=r*Math.cos(phi);
    const t=Math.random();
    if(t<0.50){col[i*3]=1;col[i*3+1]=1;col[i*3+2]=1;sizes[i]=0.9+Math.random()*0.8;}
    else if(t<0.65){col[i*3]=0.7;col[i*3+1]=0.8;col[i*3+2]=1;sizes[i]=0.7+Math.random()*0.5;}
    else if(t<0.78){col[i*3]=1;col[i*3+1]=0.9;col[i*3+2]=0.65;sizes[i]=0.8+Math.random()*0.6;}
    else if(t<0.90){col[i*3]=1;col[i*3+1]=0.45;col[i*3+2]=0.35;sizes[i]=1.0+Math.random()*0.8;}
    else{col[i*3]=0.8;col[i*3+1]=0.85;col[i*3+2]=1;sizes[i]=1.8+Math.random()*1.2;} // blue giants
  }
  geo.setAttribute('position',new THREE.BufferAttribute(pos,3));
  geo.setAttribute('color',new THREE.BufferAttribute(col,3));
  return new THREE.Points(geo,new THREE.PointsMaterial({size:1.4,sizeAttenuation:true,vertexColors:true,transparent:true,opacity:0.92,map:circleSprite,alphaTest:0.01,depthWrite:false}));
}
const starfield=createStarfield();scene.add(starfield);

// Secondary close star layer
function createCloseStars(){
  const count=3000;const geo=new THREE.BufferGeometry();const pos=new Float32Array(count*3),col=new Float32Array(count*3);
  for(let i=0;i<count;i++){
    const theta=Math.random()*Math.PI*2,phi=Math.acos(2*Math.random()-1),r=80+Math.random()*150;
    pos[i*3]=r*Math.sin(phi)*Math.cos(theta);pos[i*3+1]=r*Math.sin(phi)*Math.sin(theta);pos[i*3+2]=r*Math.cos(phi);
    const t=Math.random();
    if(t<0.6){col[i*3]=1;col[i*3+1]=1;col[i*3+2]=1;}
    else if(t<0.8){col[i*3]=1;col[i*3+1]=0.8;col[i*3+2]=0.5;}
    else{col[i*3]=0.5;col[i*3+1]=0.7;col[i*3+2]=1;}
  }
  geo.setAttribute('position',new THREE.BufferAttribute(pos,3));
  geo.setAttribute('color',new THREE.BufferAttribute(col,3));
  return new THREE.Points(geo,new THREE.PointsMaterial({size:0.9,sizeAttenuation:true,vertexColors:true,transparent:true,opacity:0.7,map:circleSprite,alphaTest:0.01,depthWrite:false}));
}
const closeStars=createCloseStars();scene.add(closeStars);

/* ── 8 NEBULAS ── */
function createNebula(pos,color,scale,op=0.032){
  const g=new THREE.Group();
  for(let i=0;i<90;i++){const m=new THREE.Mesh(new THREE.SphereGeometry(Math.random()*5+1,5,5),new THREE.MeshBasicMaterial({color,transparent:true,opacity:Math.random()*op+0.004,side:THREE.BackSide,depthWrite:false}));m.position.set((Math.random()-.5)*32*scale,(Math.random()-.5)*16*scale,(Math.random()-.5)*22*scale);g.add(m);}
  g.position.copy(pos);return g;
}
scene.add(createNebula(new THREE.Vector3(-50,8,-100),0x4466ff,1.6));
scene.add(createNebula(new THREE.Vector3(60,-12,-140),0xff4488,2.2,0.028));
scene.add(createNebula(new THREE.Vector3(-70,18,-220),0x8844ff,2.0));
scene.add(createNebula(new THREE.Vector3(40,25,-180),0x44ffaa,1.4,0.020));
scene.add(createNebula(new THREE.Vector3(90,-20,-300),0xff8822,1.8,0.022));
scene.add(createNebula(new THREE.Vector3(-90,30,-260),0x22ffcc,1.5,0.018));
scene.add(createNebula(new THREE.Vector3(0,-40,-350),0xff2266,2.5,0.015));
scene.add(createNebula(new THREE.Vector3(-40,50,-400),0xaaffff,1.2,0.014));

/* ── DISTANT BACKGROUND GALAXIES (static, far away) ── */
function createBackgroundGalaxies(){
  const g=new THREE.Group();
  for(let i=0;i<80;i++){
    const galaxyG=new THREE.Group();
    const r=0.3+Math.random()*1.2;
    // Elliptical or disk
    const isElliptical=Math.random()>0.5;
    for(let j=0;j<(isElliptical?30:50);j++){
      const t2=j/(isElliptical?30:50);
      let px,py,pz;
      if(isElliptical){px=(Math.random()-0.5)*r*2;py=(Math.random()-0.5)*r*0.8;pz=(Math.random()-0.5)*r*2;}
      else{const ang=t2*Math.PI*4;px=Math.cos(ang)*t2*r;py=(Math.random()-0.5)*0.05;pz=Math.sin(ang)*t2*r;}
      const brightness=0.5+Math.random()*0.5;
      const hue=Math.random();
      const col=hue<0.5?new THREE.Color(brightness,brightness*0.9,brightness*0.65):new THREE.Color(brightness*0.7,brightness*0.8,brightness);
      const m=new THREE.Mesh(new THREE.SphereGeometry(0.01+Math.random()*0.02,3,3),new THREE.MeshBasicMaterial({color:col,transparent:true,opacity:0.4+Math.random()*0.5}));
      m.position.set(px,py,pz);galaxyG.add(m);
    }
    const phi=Math.acos(2*Math.random()-1),theta=Math.random()*Math.PI*2,dist=150+Math.random()*500;
    galaxyG.position.set(dist*Math.sin(phi)*Math.cos(theta),dist*Math.sin(phi)*Math.sin(theta)*0.4,dist*Math.cos(phi));
    galaxyG.rotation.set(Math.random()*Math.PI,Math.random()*Math.PI,Math.random()*Math.PI);
    g.add(galaxyG);
  }
  return g;
}
const bgGalaxies=createBackgroundGalaxies();scene.add(bgGalaxies);

/* ══════════════════════════════════════════
   PORTAL
══════════════════════════════════════════ */
const portalCanvas=document.getElementById('portalCanvas');
const portalCtx=portalCanvas.getContext('2d');
portalCanvas.width=window.innerWidth;portalCanvas.height=window.innerHeight;
let portal={active:false,phase:'idle',t:0,color:[0,212,255],onMidpoint:null};
function startPortal(color,onMidpoint){portal.color=color||[0,212,255];portal.onMidpoint=onMidpoint;portal.active=true;portal.phase='shrink';portal.t=0;portalCanvas.style.display='block';}
function stopPortal(){portal.active=false;portal.phase='idle';portalCanvas.style.display='none';portalCtx.clearRect(0,0,portalCanvas.width,portalCanvas.height);}
function easeInQuart(t){return t*t*t*t;}
function easeOutQuart(t){return 1-Math.pow(1-t,4);}
function drawPortal(dt){
  if(!portal.active)return;portal.t+=dt;
  const W=portalCanvas.width,H=portalCanvas.height,cx=W/2,cy=H/2,maxR=Math.sqrt(cx*cx+cy*cy)*1.05;
  const [pr,pg,pb]=portal.color;portalCtx.clearRect(0,0,W,H);let holeR=0;
  if(portal.phase==='shrink'){const dur=0.7,progress=Math.min(portal.t/dur,1);holeR=maxR*(1-easeInQuart(progress));if(progress>=1){portal.phase='travel';portal.t=0;if(portal.onMidpoint){portal.onMidpoint();portal.onMidpoint=null;}}renderIris(portalCtx,cx,cy,W,H,holeR,maxR,pr,pg,pb,progress,'shrink');}
  else if(portal.phase==='travel'){const dur=0.35,progress=Math.min(portal.t/dur,1);portalCtx.fillStyle='rgba(0,0,0,0.98)';portalCtx.fillRect(0,0,W,H);const flashR=maxR*0.12*Math.sin(progress*Math.PI);if(flashR>0){const fg=portalCtx.createRadialGradient(cx,cy,0,cx,cy,flashR);fg.addColorStop(0,`rgba(${pr},${pg},${pb},0.9)`);fg.addColorStop(0.4,`rgba(${pr},${pg},${pb},0.4)`);fg.addColorStop(1,'rgba(0,0,0,0)');portalCtx.fillStyle=fg;portalCtx.beginPath();portalCtx.arc(cx,cy,flashR,0,Math.PI*2);portalCtx.fill();}if(progress>=1){portal.phase='expand';portal.t=0;}}
  else if(portal.phase==='expand'){const dur=0.75,progress=Math.min(portal.t/dur,1);holeR=maxR*easeOutQuart(progress);renderIris(portalCtx,cx,cy,W,H,holeR,maxR,pr,pg,pb,progress,'expand');if(progress>=1)stopPortal();}
}
function renderIris(ctx,cx,cy,W,H,holeR,maxR,pr,pg,pb,progress,phase){
  ctx.fillStyle='rgba(0,0,0,0.97)';ctx.fillRect(0,0,W,H);
  if(holeR>1){ctx.save();ctx.globalCompositeOperation='destination-out';const hg=ctx.createRadialGradient(cx,cy,holeR*0.75,cx,cy,holeR);hg.addColorStop(0,'rgba(0,0,0,1)');hg.addColorStop(0.85,'rgba(0,0,0,1)');hg.addColorStop(1,'rgba(0,0,0,0)');ctx.fillStyle=hg;ctx.beginPath();ctx.arc(cx,cy,holeR,0,Math.PI*2);ctx.fill();ctx.restore();}
  for(let ri=0;ri<5;ri++){const ringR=holeR+ri*2.5,ringOp=(1-ri/5)*(phase==='shrink'?0.9-progress*0.3:progress*0.6+0.3);ctx.save();ctx.strokeStyle=`rgba(${pr},${pg},${pb},${ringOp})`;ctx.lineWidth=Math.max(0.5,3-ri*0.5);ctx.shadowColor=`rgba(${pr},${pg},${pb},${ringOp*0.8})`;ctx.shadowBlur=8+ri*6;ctx.beginPath();ctx.arc(cx,cy,ringR,0,Math.PI*2);ctx.stroke();ctx.restore();}
  if(holeR>10){const rg=ctx.createRadialGradient(cx,cy,holeR*0.6,cx,cy,holeR*1.2);rg.addColorStop(0,'rgba(0,0,0,0)');rg.addColorStop(0.7,`rgba(${pr},${pg},${pb},0.04)`);rg.addColorStop(1,'rgba(0,0,0,0)');ctx.save();ctx.fillStyle=rg;ctx.fillRect(0,0,W,H);ctx.restore();}
}

/* ── WARP PARTICLES ── */
function createWarpParticles(rgb){
  const wGeo=new THREE.BufferGeometry(),wPos=new Float32Array(800*3);
  for(let i=0;i<800;i++){wPos[i*3]=(Math.random()-.5)*28;wPos[i*3+1]=(Math.random()-.5)*16;wPos[i*3+2]=(Math.random()-.5)*55;}
  wGeo.setAttribute('position',new THREE.BufferAttribute(wPos,3));
  return new THREE.Points(wGeo,new THREE.PointsMaterial({color:new THREE.Color(rgb[0]/255,rgb[1]/255,rgb[2]/255),size:0.20,transparent:true,opacity:0.9,blending:THREE.AdditiveBlending,map:circleSprite,alphaTest:0.01,depthWrite:false}));
}

/* ── 2D PARTICLES ── */
const pCanvas=document.getElementById('particleCanvas');
const pCtx=pCanvas.getContext('2d');
pCanvas.width=window.innerWidth;pCanvas.height=window.innerHeight;
const particles=[];
function spawnParticles(n=50){
  const cx=window.innerWidth/2,cy=window.innerHeight/2;
  for(let i=0;i<n;i++){const angle=Math.random()*Math.PI*2,speed=2+Math.random()*6;particles.push({x:cx,y:cy,vx:Math.cos(angle)*speed,vy:Math.sin(angle)*speed,life:1,decay:0.012+Math.random()*0.018,size:2+Math.random()*4,hue:190+Math.random()*60,type:Math.random()>0.7?'star':'circle'});}
}
function tickParticles(){
  pCtx.clearRect(0,0,pCanvas.width,pCanvas.height);
  for(let i=particles.length-1;i>=0;i--){const p=particles[i];p.x+=p.vx;p.y+=p.vy;p.vy+=0.06;p.vx*=0.97;p.life-=p.decay;if(p.life<=0){particles.splice(i,1);continue;}pCtx.save();pCtx.globalAlpha=p.life*0.85;pCtx.fillStyle=`hsl(${p.hue},100%,65%)`;pCtx.shadowColor=`hsl(${p.hue},100%,70%)`;pCtx.shadowBlur=8;if(p.type==='star'){const s=p.size*p.life;pCtx.beginPath();for(let j=0;j<5;j++){const a=j*Math.PI*2/5-Math.PI/2,ia=(j+0.5)*Math.PI*2/5-Math.PI/2;if(j===0)pCtx.moveTo(p.x+Math.cos(a)*s,p.y+Math.sin(a)*s);else pCtx.lineTo(p.x+Math.cos(a)*s,p.y+Math.sin(a)*s);pCtx.lineTo(p.x+Math.cos(ia)*s*0.4,p.y+Math.sin(ia)*s*0.4);}pCtx.closePath();pCtx.fill();}else{pCtx.beginPath();pCtx.arc(p.x,p.y,p.size*p.life,0,Math.PI*2);pCtx.fill();}pCtx.restore();}
}
function showNamePop(name){const old=document.querySelector('.name-pop');if(old)old.remove();const el=document.createElement('div');el.className='name-pop';el.textContent=name;document.body.appendChild(el);setTimeout(()=>{if(el.parentNode)el.remove();},2400);}
function easeOutBack(t){const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(t-1,3)+c1*Math.pow(t-1,2);}

/* ── INPUT ── */
let smoothX=0,smoothY=0,rawX=0,rawY=0;
document.addEventListener('mousemove',(e)=>{rawX=(e.clientX/window.innerWidth-0.5)*2;rawY=(e.clientY/window.innerHeight-0.5)*2;});
let touchStartX=0,touchStartY=0,touchT=0,touchActive=false;
canvas3d.addEventListener('touchstart',(e)=>{if(e.touches.length!==1)return;touchStartX=e.touches[0].clientX;touchStartY=e.touches[0].clientY;touchT=Date.now();touchActive=true;recalibrateGyro();},{passive:true});
canvas3d.addEventListener('touchmove',(e)=>{if(!touchActive||e.touches.length!==1)return;rawX=(e.touches[0].clientX/window.innerWidth-0.5)*2;rawY=(e.touches[0].clientY/window.innerHeight-0.5)*2;},{passive:true});
canvas3d.addEventListener('touchend',(e)=>{if(!touchActive)return;touchActive=false;const dx=e.changedTouches[0].clientX-touchStartX,dy=e.changedTouches[0].clientY-touchStartY,dt=Date.now()-touchT,dist=Math.sqrt(dx*dx+dy*dy);if(dist>40&&dt<600){if(Math.abs(dx)>=Math.abs(dy)){if(dx<-40)nextDest();else if(dx>40)prevDest();}else{if(dy<-40)nextDest();else if(dy>40)prevDest();}}else if(dist<12){spawnRipple(e.changedTouches[0].clientX,e.changedTouches[0].clientY);}},{passive:true});
canvas3d.addEventListener('touchmove',(e)=>e.preventDefault(),{passive:false});
let wheelLock=false;
window.addEventListener('wheel',(e)=>{if(wheelLock)return;wheelLock=true;if(e.deltaY>30)nextDest();else if(e.deltaY<-30)prevDest();setTimeout(()=>wheelLock=false,900);},{passive:true});
function spawnRipple(x,y){const r=document.createElement('div');r.className='tap-ripple';r.style.left=x+'px';r.style.top=y+'px';document.body.appendChild(r);setTimeout(()=>r.remove(),850);}

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
function updateMinimap(){document.querySelectorAll('.minimap-dot').forEach((dot,i)=>{dot.classList.remove('active','visited');if(i===currentIndex)dot.classList.add('active');else if(i<currentIndex)dot.classList.add('visited');});}
function formatDist(ly){if(ly===0)return"0 km";if(ly<0.001)return(ly*9.461e12).toExponential(1)+" km";if(ly<1)return(ly*63241).toFixed(0)+" AU";if(ly<1000)return ly.toFixed(2)+" ly";if(ly<1e6)return(ly/1000).toFixed(1)+"K ly";if(ly<1e9)return(ly/1e6).toFixed(1)+"M ly";return(ly/1e9).toFixed(1)+"B ly";}
function hexToRgb(hex){const r=/^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);return r?[parseInt(r[1],16),parseInt(r[2],16),parseInt(r[3],16)]:[0,212,255];}

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
  const camZ=['oort'].includes(d.type)?14:['jupiter','saturn'].includes(d.type)?12:['galaxy_core','galaxy','universe_edge','cosmic_web'].includes(d.type)?17:10;
  cameraTargetPos.set(0,2,camZ);
  let scaleT=0;
  const animScale=()=>{scaleT=Math.min(scaleT+0.055,1);const s=easeOutBack(scaleT);if(currentObject)currentObject.scale.setScalar(Math.max(0.001,s));if(scaleT<1)scaleAnimId=requestAnimationFrame(animScale);else scaleAnimId=null;};
  scaleAnimId=requestAnimationFrame(animScale);
  showNamePop(d.name);spawnParticles(65);updateMinimap();
  stopAllSounds(0.6);
  setTimeout(()=>{if(soundEnabled&&audioCtx)playDestinationSound(index);},650);
}

/* ── NAV ── */
function warpTo(index){
  if(isTransitioning)return;
  isTransitioning=true;
  document.getElementById('infoPanel').classList.remove('visible');
  const d=DESTINATIONS[index];const rgb=hexToRgb(d.accentColor||'#00d4ff');
  playWarpSound(rgb);
  const warpMesh=createWarpParticles(rgb);scene.add(warpMesh);
  let wT=0;
  const stepWarp=()=>{wT+=0.03;const arr=warpMesh.geometry.attributes.position.array;for(let i=0;i<arr.length;i+=3){arr[i+2]-=3*(1+wT*1.5);if(arr[i+2]<-30)arr[i+2]=26;}warpMesh.geometry.attributes.position.needsUpdate=true;warpMesh.material.size=0.20+wT*0.9;if(wT<1.5)requestAnimationFrame(stepWarp);else scene.remove(warpMesh);};
  requestAnimationFrame(stepWarp);
  startPortal(rgb,()=>{loadDestination(index);setTimeout(()=>{isTransitioning=false;},500);});
}
function jumpTo(i){currentIndex=i;warpTo(i);}
function nextDest(){if(isTransitioning)return;if(currentIndex<DESTINATIONS.length-1){currentIndex++;warpTo(currentIndex);}else showCompletion();}
function prevDest(){if(isTransitioning||currentIndex<=0)return;currentIndex--;warpTo(currentIndex);}

function launchMission(){
  if(initAudio()){document.getElementById('soundViz').style.display=soundEnabled?'flex':'none';tickVisualizer();}
  document.getElementById('landing').classList.add('hidden');
  document.getElementById('navControls').style.display='flex';
  if('ontouchstart' in window||navigator.maxTouchPoints>0){const si=document.getElementById('swipeIndicator');si.style.display='flex';setTimeout(()=>si.style.display='none',5000);}
  currentIndex=0;loadDestination(0);
}
function showCompletion(){
  document.getElementById('infoPanel').classList.remove('visible');document.getElementById('navControls').style.display='none';spawnParticles(180);
  stopAllSounds(1.0);setTimeout(()=>{if(soundEnabled&&audioCtx)playDestinationSound(13);},600);
  setTimeout(()=>document.getElementById('completion').classList.add('visible'),500);
}
function restartMission(){
  document.getElementById('completion').classList.remove('visible');
  if(currentObject){scene.remove(currentObject);currentObject=null;}
  stopAllSounds(0.5);currentIndex=-1;
  document.getElementById('progressBar').style.width='0%';document.getElementById('distValue').textContent='0 km';document.getElementById('destName').textContent='— AWAITING LAUNCH —';
  updateMinimap();gyroCalibrated=false;
  setTimeout(()=>document.getElementById('landing').classList.remove('hidden'),400);
}

/* ══════════════════════════════════════════
   RENDER LOOP — handles all orbit animations
══════════════════════════════════════════ */
const clock=new THREE.Clock();
let coronaPulseT=0;

function animate(){
  requestAnimationFrame(animate);
  const dt=clock.getDelta(),elapsed=clock.getElapsedTime();
  coronaPulseT+=dt;

  const inputX=gyroEnabled?gyroX*0.8+rawX*0.2:rawX;
  const inputY=gyroEnabled?gyroY*0.8+rawY*0.2:rawY;
  smoothX+=(inputX-smoothX)*Math.min(1,dt*4.5);
  smoothY+=(inputY-smoothY)*Math.min(1,dt*4.5);

  starfield.rotation.y+=dt*0.003+smoothX*0.0005;
  starfield.rotation.x+=dt*0.0015+smoothY*0.0003;
  closeStars.rotation.y+=dt*0.005+smoothX*0.0007;
  bgGalaxies.rotation.y+=dt*0.0008;

  if(currentObject){
    currentObject.rotation.y+=dt*0.18;
    currentObject.rotation.x+=(smoothY*0.20-currentObject.rotation.x)*Math.min(1,dt*2.5);
    currentObject.rotation.z+=(-smoothX*0.10-currentObject.rotation.z)*Math.min(1,dt*2.5);
    currentObject.position.y=Math.sin(elapsed*0.65)*0.14;

    currentObject.children.forEach(child=>{
      // Orbit animation (moons, asteroids, ISS, etc.)
      if(child.userData.orbitR!==undefined&&child.userData.orbitSpeed!==undefined){
        child.userData.orbitAngle=(child.userData.orbitAngle||0)+child.userData.orbitSpeed;
        const oR=child.userData.orbitR,oA=child.userData.orbitAngle;
        const inclination=child.userData.inclination||0;
        if(child.userData.isComet){
          // Comets orbit in 3D
          child.position.x=Math.cos(oA)*oR;
          child.position.z=Math.sin(oA)*oR;
          child.position.y=child.userData.orbitY||0;
          // tail always points away
          child.children[1].rotation.z=oA+Math.PI/2;
        } else {
          child.position.x=Math.cos(oA)*oR*Math.cos(inclination);
          child.position.z=Math.sin(oA)*oR;
          child.position.y=(child.userData.orbitY||0)+Math.sin(oA)*oR*Math.sin(inclination);
        }
        // Spin individual asteroids
        if(child.userData.isAsteroid){child.rotation.x+=dt*0.8;child.rotation.y+=dt*0.5;}
      }
      // Ring rotation
      if(child.userData.rotSpeed)child.rotation.z+=child.userData.rotSpeed;
      // Corona pulse
      if(child.userData.pulse){child.material.opacity=0.05+Math.sin(coronaPulseT*2.2)*0.04;}
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
  camera.aspect=window.innerWidth/window.innerHeight;camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth,window.innerHeight);
  pCanvas.width=window.innerWidth;pCanvas.height=window.innerHeight;
  portalCanvas.width=window.innerWidth;portalCanvas.height=window.innerHeight;
});
document.addEventListener('keydown',e=>{
  if(e.key==='ArrowRight'||e.key==='ArrowDown'){e.preventDefault();nextDest();}
  if(e.key==='ArrowLeft'||e.key==='ArrowUp'){e.preventDefault();prevDest();}
  if(e.key==='f'||e.key==='F')toggleFullscreen();
  if(e.key==='m'||e.key==='M')toggleSound();
});
</script>
</body>
</html>
""", height=870, scrolling=False)