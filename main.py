import math
import streamlit as st

st.set_page_config(
    page_title="HIRELYZER — Intelligent Career Platform",
    page_icon="⬡",
    layout="wide",
)

APP_URL = "https://hirelyzer-career-based-saas-platform-24rstwtacwlmwetzpxmwyn.streamlit.app/"
SUPPORT_EMAIL = "swagato_bmca2024@msit.edu.in"

# ─── helpers ──────────────────────────────────────────────────────────────────
def H(s):
    st.markdown(s, unsafe_allow_html=True)

def CSS(s):
    st.markdown("<style>" + s + "</style>", unsafe_allow_html=True)

# ─── CSS ──────────────────────────────────────────────────────────────────────
CSS("""
@import url('https://fonts.googleapis.com/css2?family=Clash+Display:wght@400;500;600;700&family=Sora:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
  --blue:    #0a84ff;
  --green:   #30d158;
  --purple:  #bf5af2;
  --amber:   #ff9f0a;
  --red:     #ff453a;
  --sky:     #4db3ff;
  --fg:      #f5f5f7;
  --fg2:     rgba(245,245,247,0.5);
  --fg3:     rgba(245,245,247,0.28);
  --border:  rgba(255,255,255,0.08);
  --surface: #0a0a0c;
  --surface2:#111115;
  --glow-blue: rgba(10,132,255,0.18);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
  background-color: #000 !important;
  color: var(--fg) !important;
  font-family: 'Sora', sans-serif !important;
  overflow-x: hidden !important;
  -webkit-font-smoothing: antialiased !important;
}

[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stSidebar"],
[data-testid="stStatusWidget"],
footer,
#MainMenu { display: none !important; }

section[data-testid="stAppViewContainer"] > div { padding: 0 !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
div[data-testid="stMarkdownContainer"] > p { margin: 0 !important; }

/* ── Scroll progress bar ── */
#sp {
  position: fixed; top: 0; left: 0; right: 0; height: 2px; width: 0%;
  background: linear-gradient(90deg, #0a84ff, #30d158, #bf5af2, #0a84ff);
  background-size: 200% 100%;
  z-index: 9999; transition: width 0.05s linear; pointer-events: none;
  animation: gradientShift 3s linear infinite;
}

/* ── Noise texture overlay ── */
.hl-noise {
  position: fixed; inset: 0; z-index: 1; pointer-events: none;
  opacity: 0.025;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  background-repeat: repeat; background-size: 128px 128px;
}

/* ── Toast notification ── */
#hl-toast {
  position: fixed; bottom: 90px; left: 50%; transform: translateX(-50%) translateY(20px);
  background: rgba(10,10,12,0.95); border: 1px solid rgba(255,255,255,0.14); border-radius: 100px;
  padding: 12px 22px; font-size: 13px; font-weight: 600; color: var(--fg);
  display: flex; align-items: center; gap: 8px; z-index: 9998;
  opacity: 0; transition: opacity 0.3s ease, transform 0.3s ease; pointer-events: none;
  box-shadow: 0 12px 48px rgba(0,0,0,0.7), 0 0 0 1px rgba(255,255,255,0.04);
  backdrop-filter: blur(20px);
}
#hl-toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }
#hl-toast-dot { width: 7px; height: 7px; border-radius: 50%; background: #30d158; flex-shrink: 0; box-shadow: 0 0 8px #30d158; }

/* ── Sticky bottom CTA ── */
#hl-sticky-cta {
  position: fixed; bottom: 0; left: 0; right: 0; z-index: 890;
  background: rgba(0,0,0,0.92); border-top: 1px solid var(--border);
  backdrop-filter: blur(28px); -webkit-backdrop-filter: blur(28px);
  padding: 14px 32px; display: flex; align-items: center; justify-content: space-between;
  transform: translateY(100%); transition: transform 0.4s cubic-bezier(0.16,1,0.3,1);
  max-width: 100%;
}
#hl-sticky-cta.visible { transform: translateY(0); }
.hl-sticky-inner { max-width: 1140px; width: 100%; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; gap: 16px; }
.hl-sticky-text { font-size: 14px; font-weight: 600; color: var(--fg2); }
.hl-sticky-text span { color: var(--fg); }
.hl-sticky-btns { display: flex; gap: 10px; align-items: center; flex-shrink: 0; }
#hl-sticky-dismiss { background: none; border: none; color: var(--fg3); font-size: 20px; cursor: pointer; padding: 4px 8px; line-height: 1; transition: color 0.2s; }
#hl-sticky-dismiss:hover { color: var(--fg2); }

/* ── Section dot nav ── */
#hl-dots {
  position: fixed; right: 24px; top: 50%; transform: translateY(-50%);
  display: flex; flex-direction: column; gap: 10px; z-index: 800;
}
.hl-dot-nav {
  width: 7px; height: 7px; border-radius: 50%;
  background: rgba(255,255,255,0.2); cursor: pointer;
  transition: background 0.3s, transform 0.3s, box-shadow 0.3s; border: none; padding: 0;
}
.hl-dot-nav.active { background: var(--blue); transform: scale(1.5); box-shadow: 0 0 8px var(--blue); }
.hl-dot-nav:hover { background: rgba(255,255,255,0.5); }
@media (max-width: 900px) { #hl-dots { display: none; } }

/* ── Mobile hamburger ── */
.hl-hamburger {
  display: none; flex-direction: column; gap: 5px; cursor: pointer;
  background: none; border: none; padding: 6px;
}
.hl-hamburger span {
  display: block; width: 22px; height: 2px; background: var(--fg2);
  border-radius: 2px; transition: transform 0.3s ease, opacity 0.3s ease;
}
.hl-hamburger.open span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
.hl-hamburger.open span:nth-child(2) { opacity: 0; }
.hl-hamburger.open span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }

/* ── Mobile drawer ── */
#hl-drawer {
  position: fixed; top: 0; left: 0; right: 0; bottom: 0; z-index: 850;
  background: rgba(0,0,0,0.98); display: flex; flex-direction: column;
  align-items: center; justify-content: center; gap: 32px;
  transform: translateY(-100%); transition: transform 0.4s cubic-bezier(0.16,1,0.3,1);
  pointer-events: none;
}
#hl-drawer.open { transform: translateY(0); pointer-events: all; }
#hl-drawer a {
  font-size: 28px; font-weight: 700; color: var(--fg2);
  text-decoration: none; letter-spacing: -1px; transition: color 0.2s;
  font-family: 'Sora', sans-serif;
}
#hl-drawer a:hover { color: var(--fg); }
#hl-drawer-close {
  position: absolute; top: 24px; right: 24px;
  background: none; border: none; color: var(--fg3);
  font-size: 28px; cursor: pointer; line-height: 1;
}

/* ── Announcement banner ── */
.hl-banner {
  background: linear-gradient(90deg, rgba(10,132,255,0.1), rgba(48,209,88,0.06), rgba(191,90,242,0.08), rgba(10,132,255,0.1));
  background-size: 300% 100%;
  border-bottom: 1px solid rgba(10,132,255,0.18);
  padding: 10px 32px; text-align: center; position: relative; z-index: 901;
  font-size: 12.5px; color: var(--fg2); font-weight: 500;
  display: flex; align-items: center; justify-content: center; gap: 10px;
  animation: shimmerBg 5s linear infinite;
}
.hl-banner-badge {
  padding: 2px 10px; border-radius: 100px;
  background: linear-gradient(135deg, rgba(10,132,255,0.25), rgba(48,209,88,0.15));
  border: 1px solid rgba(10,132,255,0.4); color: var(--blue);
  font-size: 10px; font-weight: 700; letter-spacing: 0.8px; text-transform: uppercase;
  flex-shrink: 0; box-shadow: 0 0 12px rgba(10,132,255,0.2);
}
.hl-banner a { color: var(--blue); font-weight: 600; text-decoration: none; transition: color 0.2s; }
.hl-banner a:hover { color: var(--sky); }

/* ── Nav ── */
.hl-nav {
  position: sticky; top: 0; left: 0; right: 0; z-index: 900;
  height: 62px; display: flex; align-items: center; justify-content: center;
  background: rgba(0,0,0,0.82);
  border-bottom: 1px solid rgba(255,255,255,0.06);
  backdrop-filter: blur(32px); -webkit-backdrop-filter: blur(32px);
  transition: box-shadow 0.4s ease, border-color 0.4s ease;
}
.hl-nav.scrolled { box-shadow: 0 8px 48px rgba(0,0,0,0.7); border-color: rgba(255,255,255,0.09); }
.hl-nav-inner {
  width: 100%; max-width: 1140px;
  display: flex; align-items: center; justify-content: space-between; padding: 0 32px;
}
.hl-logo {
  display: flex; align-items: center; gap: 10px;
  font-family: 'Sora', sans-serif;
  font-size: 13.5px; font-weight: 800; color: var(--fg); text-decoration: none; letter-spacing: 0.8px;
}
.hl-logo-icon {
  width: 34px; height: 34px; border-radius: 10px;
  background: linear-gradient(135deg, #1a6fff, #0044bb);
  display: flex; align-items: center; justify-content: center; flex-shrink: 0;
  box-shadow: 0 4px 20px rgba(10,132,255,0.45), 0 0 0 1px rgba(10,132,255,0.2);
  transition: box-shadow 0.2s;
}
.hl-logo:hover .hl-logo-icon { box-shadow: 0 6px 28px rgba(10,132,255,0.6), 0 0 0 1px rgba(10,132,255,0.3); }
.hl-nav-links { display: flex; align-items: center; gap: 30px; }
.hl-nav-links a {
  font-size: 13px; font-weight: 500; color: var(--fg3); text-decoration: none;
  transition: color 0.2s; position: relative; padding-bottom: 4px;
}
.hl-nav-links a::after {
  content: ''; position: absolute; bottom: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, var(--blue), var(--green));
  transform: scaleX(0); transition: transform 0.25s ease; transform-origin: left;
}
.hl-nav-links a:hover { color: var(--fg); }
.hl-nav-links a:hover::after { transform: scaleX(1); }
.hl-nav-links a.hl-nav-active { color: var(--fg); }
.hl-nav-links a.hl-nav-active::after { transform: scaleX(1); }
.hl-nav-right { display: flex; align-items: center; gap: 12px; }
.hl-nav-cta {
  display: inline-flex; align-items: center; gap: 7px;
  padding: 8px 20px; border-radius: 100px;
  background: linear-gradient(135deg, #1a6fff, #0055d4);
  color: #fff; font-size: 13px; font-weight: 600; text-decoration: none;
  box-shadow: 0 4px 20px rgba(10,132,255,0.35); 
  transition: transform 0.15s, box-shadow 0.2s;
  position: relative; overflow: hidden;
}
.hl-nav-cta::before {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(135deg, rgba(255,255,255,0.12), transparent);
  border-radius: inherit;
}
.hl-nav-cta:hover { transform: translateY(-1px); box-shadow: 0 6px 28px rgba(10,132,255,0.5); }

/* ── Hero ── */
.hl-hero {
  min-height: 100vh; display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  text-align: center; padding: 80px 32px 80px;
  position: relative; overflow: hidden; background: #000;
}

/* Aurora mesh background */
.hl-aurora {
  position: absolute; inset: 0; pointer-events: none; z-index: 0; overflow: hidden;
}
.hl-aurora-1 {
  position: absolute; width: 800px; height: 800px; border-radius: 50%;
  background: radial-gradient(circle, rgba(10,132,255,0.12) 0%, transparent 65%);
  top: -200px; left: 10%; animation: auroraFloat1 12s ease-in-out infinite;
}
.hl-aurora-2 {
  position: absolute; width: 700px; height: 700px; border-radius: 50%;
  background: radial-gradient(circle, rgba(48,209,88,0.07) 0%, transparent 60%);
  top: 0; right: 5%; animation: auroraFloat2 15s ease-in-out infinite;
}
.hl-aurora-3 {
  position: absolute; width: 600px; height: 600px; border-radius: 50%;
  background: radial-gradient(circle, rgba(191,90,242,0.07) 0%, transparent 60%);
  bottom: -100px; left: 30%; animation: auroraFloat3 18s ease-in-out infinite;
}
@keyframes auroraFloat1 {
  0%, 100% { transform: translate(0, 0) scale(1); }
  33% { transform: translate(60px, 40px) scale(1.05); }
  66% { transform: translate(-40px, 80px) scale(0.96); }
}
@keyframes auroraFloat2 {
  0%, 100% { transform: translate(0, 0) scale(1); }
  40% { transform: translate(-80px, 60px) scale(1.08); }
  70% { transform: translate(40px, -40px) scale(0.94); }
}
@keyframes auroraFloat3 {
  0%, 100% { transform: translate(0, 0) scale(1); }
  30% { transform: translate(50px, -60px) scale(1.06); }
  60% { transform: translate(-60px, 20px) scale(1.02); }
}

/* Cursor spotlight */
#hl-spotlight {
  position: absolute; pointer-events: none; z-index: 0;
  width: 700px; height: 700px; border-radius: 50%;
  background: radial-gradient(circle, rgba(10,132,255,0.07) 0%, transparent 60%);
  transform: translate(-50%, -50%); transition: left 0.1s ease, top 0.1s ease;
  left: 50%; top: 50%;
}

/* Floating particles canvas */
#hl-particles {
  position: absolute; inset: 0; pointer-events: none; z-index: 0;
}

.hl-hero-grid {
  position: absolute; inset: 0; pointer-events: none; z-index: 0;
  background-image: linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
  background-size: 56px 56px;
  mask-image: radial-gradient(ellipse 70% 50% at 50% 0%, black 40%, transparent 100%);
}
.hl-hero-fade {
  position: absolute; bottom: 0; left: 0; right: 0; height: 280px;
  background: linear-gradient(to bottom, transparent, #000);
  pointer-events: none; z-index: 0;
}
.hl-hero-content {
  position: relative; z-index: 1; width: 100%; display: flex; flex-direction: column; align-items: center;
}

.hl-eyebrow {
  display: inline-flex; align-items: center; gap: 8px;
  font-size: 10.5px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase;
  color: var(--blue); padding: 6px 16px; border-radius: 100px;
  border: 1px solid rgba(10,132,255,0.3); background: rgba(10,132,255,0.08); margin-bottom: 28px;
  animation: fadeUp 0.6s ease both;
  box-shadow: 0 0 20px rgba(10,132,255,0.1);
}

.hl-eyebrow-dot {
  width: 6px; height: 6px; border-radius: 50%; background: var(--blue);
  box-shadow: 0 0 8px var(--blue); animation: pulse 2s ease infinite;
}

.hl-h1 {
  font-family: 'Sora', sans-serif;
  font-size: clamp(44px, 7.5vw, 96px); font-weight: 800; line-height: 1.0;
  letter-spacing: -4px; color: var(--fg); max-width: 1020px;
  animation: fadeUp 0.6s 0.1s ease both;
}
.hl-h1-blue { color: var(--blue); }
.hl-h1-gradient {
  background: linear-gradient(135deg, #1a6fff 0%, #30d158 55%, #1a6fff 100%);
  background-size: 200% 100%; -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text; animation: gradientShift 4s ease infinite;
}

/* Typewriter */
#hl-typewriter {
  display: inline-block; min-width: 120px;
  background: linear-gradient(135deg, #1a6fff 0%, #30d158 55%, #1a6fff 100%);
  background-size: 200% 100%; -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text; animation: gradientShift 4s ease infinite;
}
.hl-cursor {
  display: inline-block; width: 3px; height: 0.82em; background: var(--blue);
  margin-left: 3px; vertical-align: middle; border-radius: 2px;
  animation: blink 1s step-end infinite; box-shadow: 0 0 8px var(--blue);
}
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }

.hl-hero-sub {
  font-size: clamp(15px, 1.9vw, 19px); color: var(--fg2); line-height: 1.75;
  max-width: 580px; margin: 28px auto 0; animation: fadeUp 0.6s 0.2s ease both;
  text-align: center;
}

.hl-ctas {
  display: flex; gap: 14px; justify-content: center; margin-top: 48px; flex-wrap: wrap;
  animation: fadeUp 0.6s 0.3s ease both;
}

/* Primary button */
.hl-btn-p {
  display: inline-flex; align-items: center; gap: 8px; padding: 15px 34px;
  border-radius: 100px;
  background: linear-gradient(135deg, #1a6fff, #0055d4);
  color: #fff; font-size: 15px; font-weight: 600; text-decoration: none; letter-spacing: -0.2px;
  box-shadow: 0 8px 32px rgba(10,132,255,0.4), 0 0 0 1px rgba(255,255,255,0.08) inset;
  transition: transform 0.15s, box-shadow 0.2s; position: relative; overflow: hidden;
}
.hl-btn-p::before {
  content: ''; position: absolute; inset: 0; border-radius: inherit;
  background: linear-gradient(135deg, rgba(255,255,255,0.15) 0%, transparent 60%);
}
.hl-btn-p:hover { transform: translateY(-2px); box-shadow: 0 14px 48px rgba(10,132,255,0.55), 0 0 0 1px rgba(255,255,255,0.1) inset; }
.hl-btn-p:active { transform: scale(0.97); }

/* Ghost button */
.hl-btn-g {
  display: inline-flex; align-items: center; gap: 8px; padding: 15px 32px;
  border-radius: 100px; background: rgba(255,255,255,0.04); color: var(--fg);
  font-size: 15px; font-weight: 600; text-decoration: none; letter-spacing: -0.2px;
  border: 1px solid rgba(255,255,255,0.1);
  transition: border-color 0.2s, background 0.2s, box-shadow 0.2s;
  backdrop-filter: blur(8px);
}
.hl-btn-g:hover { border-color: rgba(255,255,255,0.22); background: rgba(255,255,255,0.07); box-shadow: 0 4px 20px rgba(0,0,0,0.3); }
.hl-btn-g:active { transform: scale(0.97); }

/* ── Hero feature strip ── */
.hl-hero-features {
  display: flex; align-items: center; gap: 0; flex-wrap: wrap; justify-content: center;
  margin-top: 52px; padding: 13px 26px;
  background: rgba(255,255,255,0.025);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 100px; animation: fadeUp 0.6s 0.4s ease both;
  backdrop-filter: blur(12px);
}
.hl-hf-item {
  display: flex; align-items: center; gap: 7px; padding: 0 18px;
  font-size: 12.5px; font-weight: 600; color: var(--fg3);
  white-space: nowrap;
}
.hl-hf-sep { width: 1px; height: 14px; background: var(--border); flex-shrink: 0; }

/* ── Hero card / panel ── */
.hl-card {
  margin-top: 72px; width: 100%; max-width: 880px;
  background: rgba(10,10,14,0.9);
  border-radius: 26px; border: 1px solid rgba(255,255,255,0.09); overflow: hidden;
  box-shadow: 0 60px 120px rgba(0,0,0,0.9), 0 0 0 1px rgba(10,132,255,0.05), 0 0 80px rgba(10,132,255,0.05);
  animation: fadeUp 0.6s 0.44s ease both;
  backdrop-filter: blur(16px);
}
.hl-card-bar {
  height: 44px; background: rgba(20,20,24,0.95); border-bottom: 1px solid rgba(255,255,255,0.07);
  display: flex; align-items: center; padding: 0 16px; gap: 8px;
}
.hl-dot { width: 12px; height: 12px; border-radius: 50%; flex-shrink: 0; }
.hl-card-tab { margin-left: 6px; font-size: 11px; color: var(--fg3); font-family: 'JetBrains Mono', monospace; }
.hl-card-body { padding: 28px; }
.hl-card-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; }

.hl-ptitle {
  font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px;
  color: var(--fg3); display: flex; align-items: center; gap: 7px; margin-bottom: 18px;
}

.hl-bar { margin-bottom: 10px; }
.hl-bar-row {
  display: flex; justify-content: space-between; font-size: 11px;
  color: var(--fg2); margin-bottom: 5px; font-weight: 500;
}
.hl-bar-track { height: 4px; background: rgba(255,255,255,0.06); border-radius: 2px; overflow: hidden; }
.hl-bar-fill { height: 100%; border-radius: 2px; transition: width 1s cubic-bezier(0.4,0,0.2,1); }

.hl-words { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 12px; }
.wc { padding: 4px 11px; border-radius: 7px; font-size: 11px; font-weight: 600; font-family: 'JetBrains Mono', monospace; }
.wc-m { background: rgba(10,132,255,0.1); color: #4db3ff; border: 1px solid rgba(10,132,255,0.2); }
.wc-f { background: rgba(191,90,242,0.1); color: #d07ef7; border: 1px solid rgba(191,90,242,0.2); }
.wc-n { background: rgba(48,209,88,0.1); color: #4cd964; border: 1px solid rgba(48,209,88,0.2); }

/* ── Stats row ── */
.hl-stats {
  display: flex; gap: 14px; flex-wrap: wrap; justify-content: center; margin: 36px 0 0;
  animation: fadeUp 0.6s 0.55s ease both;
}
.hl-stat {
  display: flex; flex-direction: column; align-items: center; padding: 22px 36px;
  border-radius: 20px;
  background: rgba(10,10,14,0.8);
  border: 1px solid rgba(255,255,255,0.07); min-width: 130px;
  position: relative; overflow: hidden;
  transition: border-color 0.25s, transform 0.25s, box-shadow 0.25s;
  backdrop-filter: blur(12px);
}
.hl-stat:hover { transform: translateY(-3px); border-color: rgba(255,255,255,0.16); box-shadow: 0 20px 60px rgba(0,0,0,0.5); }
.hl-stat::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(10,132,255,0.5), rgba(48,209,88,0.3), transparent);
}
.hl-stat-n { font-size: 30px; font-weight: 800; color: var(--fg); letter-spacing: -1.5px; }
.hl-stat-l { font-size: 10px; color: var(--fg3); font-weight: 600; margin-top: 4px; text-transform: uppercase; letter-spacing: 0.9px; }

/* ── Section ── */
.hl-section { max-width: 1140px; margin: 0 auto; padding: 0 32px; }

/* ── Divider ── */
.hl-divider {
  font-size: 10px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase;
  color: var(--fg3); display: flex; align-items: center; gap: 18px; margin-bottom: 64px;
}
.hl-divider::before,
.hl-divider::after {
  content: ''; flex: 1; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.07), transparent);
}

/* ── How it works ── */
.hl-steps { display: grid; grid-template-columns: repeat(4,1fr); gap: 2px; }
.hl-step {
  padding: 36px 28px;
  background: rgba(8,8,10,0.9);
  border: 1px solid rgba(255,255,255,0.06); position: relative; overflow: hidden;
  transition: background 0.25s, border-color 0.25s, transform 0.25s;
}
.hl-step::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.06), transparent);
}
.hl-step:hover { background: rgba(14,14,18,0.95); border-color: rgba(255,255,255,0.11); transform: translateY(-3px); }
.hl-step:first-child { border-radius: 20px 0 0 20px; }
.hl-step:last-child  { border-radius: 0 20px 20px 0; }
.hl-step-n { font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 600; color: var(--fg3); margin-bottom: 18px; display: block; }
.hl-step-icon { width: 48px; height: 48px; margin-bottom: 20px; }
.hl-step-title { font-size: 14px; font-weight: 700; color: var(--fg); margin-bottom: 9px; letter-spacing: -0.3px; }
.hl-step-desc  { font-size: 13px; color: var(--fg2); line-height: 1.72; }

/* Connector lines */
.hl-step:not(:last-child)::after {
  content: ''; position: absolute; right: -1px; top: 50%; transform: translateY(-50%);
  width: 2px; height: 30px;
  background: linear-gradient(to bottom, transparent, rgba(255,255,255,0.06), transparent);
}

/* ── Story sections ── */
.hl-story     { padding: 120px 0; background: #000; }
.hl-story-alt { padding: 120px 0; background: #030305; }
.hl-story-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 96px; align-items: center; }

/* ── Scroll-reveal ── */
.hl-reveal.hl-animate { animation: revealUp 0.75s cubic-bezier(0.16,1,0.3,1) both; }
.hl-reveal-delay-1.hl-animate { animation-delay: 0.08s; }
.hl-reveal-delay-2.hl-animate { animation-delay: 0.18s; }
.hl-reveal-delay-3.hl-animate { animation-delay: 0.28s; }
@keyframes revealUp {
  from { opacity: 0; transform: translateY(28px); }
  to   { opacity: 1; transform: none; }
}

.hl-story-num {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10.5px; font-weight: 600; color: var(--fg3); letter-spacing: 1px; margin-bottom: 18px;
}
.hl-story-h { font-size: clamp(28px, 3.8vw, 48px); font-weight: 800; letter-spacing: -2.2px; line-height: 1.06; color: var(--fg); margin-bottom: 22px; }
.hl-story-h .hl-blue  { color: var(--blue); }
.hl-story-h .hl-green { color: var(--green); }
.hl-story-h .hl-amber { color: var(--amber); }
.hl-story-h .hl-purp  { color: var(--purple); }
.hl-cta p, .hl-story p, .hl-story-alt p,
.hl-hero p, .hl-compare p {
  margin: 0 !important; text-align: inherit !important;
}
.hl-story-p { font-size: 15px; color: var(--fg2); line-height: 1.84; margin-bottom: 18px; }

/* ── Pills ── */
.hl-pills { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px; }
.hl-pill {
  padding: 6px 14px; border-radius: 100px; font-size: 11.5px; font-weight: 600;
  border: 1px solid rgba(255,255,255,0.09); color: var(--fg2);
  background: rgba(255,255,255,0.03);
  transition: border-color 0.2s, color 0.2s, background 0.2s;
  backdrop-filter: blur(4px);
}
.hl-pill:hover { border-color: rgba(255,255,255,0.2); color: var(--fg); background: rgba(255,255,255,0.05); }

/* ── Panel ── */
.hl-panel {
  background: rgba(8,8,12,0.95);
  border-radius: 24px; border: 1px solid rgba(255,255,255,0.08);
  padding: 28px; overflow: hidden; position: relative;
  box-shadow: 0 40px 80px rgba(0,0,0,0.6), 0 0 0 1px rgba(255,255,255,0.02) inset;
  transition: border-color 0.3s, box-shadow 0.3s, transform 0.3s;
  backdrop-filter: blur(16px);
}
.hl-panel:hover { border-color: rgba(255,255,255,0.13); box-shadow: 0 60px 120px rgba(0,0,0,0.7); transform: translateY(-2px); }
.hl-panel::before {
  content: ''; position: absolute; top: 0; left: 24px; right: 24px; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
}

/* ── Radar animation ── */
.hl-radar-polygon {
  stroke-dasharray: 1000;
  stroke-dashoffset: 1000;
  transition: stroke-dashoffset 1.6s cubic-bezier(0.4,0,0.2,1);
}
.hl-radar-polygon.drawn { stroke-dashoffset: 0; }
.hl-radar-dot {
  opacity: 0; transform: scale(0);
  transition: opacity 0.4s ease, transform 0.4s ease;
}
.hl-radar-dot.drawn { opacity: 1; transform: scale(1); }

/* ── Templates ── */
.hl-tmpl-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 10px; margin-bottom: 14px; }
.hl-tmpl {
  border-radius: 11px; border: 1px solid rgba(255,255,255,0.07);
  background: rgba(18,18,22,0.9); overflow: hidden; display: flex;
  flex-direction: column; min-height: 115px; position: relative; cursor: pointer;
  transition: border-color 0.18s, box-shadow 0.18s, transform 0.18s;
}
.hl-tmpl:hover { border-color: rgba(255,255,255,0.2); transform: translateY(-3px); box-shadow: 0 12px 32px rgba(0,0,0,0.5); }
.hl-tmpl-act { border-color: var(--blue) !important; box-shadow: 0 0 0 2px rgba(10,132,255,0.25), 0 0 20px rgba(10,132,255,0.15) !important; }
.hl-tmpl-hdr { height: 5px; border-radius: 2px; }
.hl-tmpl-ln  { height: 3px; border-radius: 1.5px; background: rgba(255,255,255,0.13); }
.hl-tmpl-badge {
  position: absolute; bottom: 6px; left: 6px; right: 6px;
  background: rgba(10,132,255,0.14); border: 1px solid rgba(10,132,255,0.28);
  border-radius: 5px; padding: 3px 6px; font-size: 9px; font-weight: 700;
  color: var(--blue); text-align: center; letter-spacing: 0.5px; text-transform: uppercase;
}

/* ── Jobs ── */
.hl-job {
  padding: 13px 15px; border-radius: 13px;
  background: rgba(16,16,20,0.9);
  border: 1px solid rgba(255,255,255,0.07); display: flex; align-items: center; gap: 12px; margin-bottom: 8px;
  transition: border-color 0.18s, background 0.18s, transform 0.18s;
}
.hl-job:hover { background: rgba(22,22,28,0.95); border-color: rgba(255,255,255,0.13); transform: translateX(3px); }
.hl-job-logo { width: 36px; height: 36px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 13px; flex-shrink: 0; font-family: 'JetBrains Mono', monospace; }
.hl-job-title { font-size: 13px; font-weight: 600; color: var(--fg); }
.hl-job-co    { font-size: 11px; color: var(--fg3); margin-top: 2px; }
.hl-job-badge { padding: 3px 10px; border-radius: 100px; font-size: 11px; font-weight: 600; white-space: nowrap; flex-shrink: 0; }

/* ── Interview ── */
.hl-radar-wrap { display: flex; flex-direction: column; align-items: center; }
.hl-qa { margin-bottom: 14px; }
.hl-q { font-size: 13px; font-weight: 600; color: var(--fg); margin-bottom: 7px; display: flex; gap: 8px; align-items: flex-start; }
.hl-a { font-size: 12px; color: var(--fg2); line-height: 1.68; padding-left: 22px; }
.hl-score-badge {
  display: inline-flex; align-items: center; gap: 6px; padding: 5px 12px; border-radius: 100px;
  font-size: 12px; font-weight: 700; background: rgba(48,209,88,0.1); color: var(--green);
  border: 1px solid rgba(48,209,88,0.25); box-shadow: 0 0 12px rgba(48,209,88,0.12);
}

/* ── Comparison ── */
.hl-compare { padding: 100px 0; background: #000; }
.hl-compare-wrap {
  margin-top: 52px; border-radius: 24px; border: 1px solid rgba(255,255,255,0.08); overflow: hidden;
  box-shadow: 0 40px 80px rgba(0,0,0,0.4);
}
.hl-compare-head {
  display: grid; grid-template-columns: 1.6fr 1fr 1fr 1fr;
  background: rgba(8,8,12,0.98); border-bottom: 1px solid rgba(255,255,255,0.07);
}
.hl-compare-row {
  display: grid; grid-template-columns: 1.6fr 1fr 1fr 1fr;
  border-bottom: 1px solid rgba(255,255,255,0.04);
  transition: background 0.15s;
}
.hl-compare-row:last-child { border-bottom: none; }
.hl-compare-row:hover { background: rgba(255,255,255,0.015); }
.hl-ch { padding: 16px 24px; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: var(--fg3); }
.hl-ch-hl {
  background: rgba(10,132,255,0.07); border-left: 1px solid rgba(10,132,255,0.14);
  border-right: 1px solid rgba(10,132,255,0.14); color: var(--blue);
  display: flex; align-items: center; gap: 7px; justify-content: center;
}
.hl-cc { padding: 16px 24px; font-size: 13px; color: var(--fg2); display: flex; align-items: center; }
.hl-cc-feat { font-weight: 600; color: var(--fg); font-size: 13.5px; }
.hl-cc-feat small { display: block; font-size: 11px; color: var(--fg3); font-weight: 400; margin-top: 2px; }
.hl-cc-hl {
  background: rgba(10,132,255,0.04);
  border-left: 1px solid rgba(10,132,255,0.1); border-right: 1px solid rgba(10,132,255,0.1);
  justify-content: center; font-weight: 600; color: var(--fg);
}
.hl-cc-center { justify-content: center; }
.hl-chk-y { color: var(--green); font-size: 16px; filter: drop-shadow(0 0 4px rgba(48,209,88,0.4)); }
.hl-chk-n { color: rgba(245,245,247,0.18); font-size: 18px; }
.hl-chk-p { color: var(--amber); font-size: 11px; font-weight: 700; }

/* ── Feature Highlights ── */
.hl-highlights { padding: 0 0 100px; background: #000; }
.hl-highlight-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 2px; margin-top: 48px; }
.hl-highlight {
  padding: 34px 30px; background: rgba(8,8,12,0.95); border: 1px solid rgba(255,255,255,0.06);
  position: relative; overflow: hidden;
  transition: background 0.25s, border-color 0.25s, transform 0.25s;
}
.hl-highlight:first-child { border-radius: 20px 0 0 0; }
.hl-highlight:nth-child(3) { border-radius: 0 20px 0 0; }
.hl-highlight:nth-child(4) { border-radius: 0 0 0 20px; }
.hl-highlight:last-child { border-radius: 0 0 20px 0; }
.hl-highlight:hover { background: rgba(14,14,18,0.98); border-color: rgba(255,255,255,0.11); transform: translateY(-3px); }
.hl-highlight::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.07), transparent);
}
/* Glow on hover - per card */
.hl-highlight::after {
  content: ''; position: absolute; inset: 0;
  background: radial-gradient(circle at 30% 30%, var(--card-glow, rgba(10,132,255,0.04)), transparent 65%);
  opacity: 0; transition: opacity 0.3s;
}
.hl-highlight:hover::after { opacity: 1; }
.hl-hi-icon {
  width: 46px; height: 46px; border-radius: 13px; display: flex; align-items: center;
  justify-content: center; margin-bottom: 20px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.3);
}
.hl-hi-title { font-size: 15px; font-weight: 700; color: var(--fg); margin-bottom: 9px; letter-spacing: -0.3px; }
.hl-hi-desc { font-size: 13px; color: var(--fg2); line-height: 1.74; }

/* ── FAQ ── */
.hl-faq { padding: 100px 0; background: #030305; }
.hl-faq-list { max-width: 720px; margin: 48px auto 0; display: flex; flex-direction: column; gap: 3px; }
.hl-faq-item {
  background: rgba(8,8,12,0.9); border: 1px solid rgba(255,255,255,0.07); border-radius: 16px; overflow: hidden;
  transition: border-color 0.2s, box-shadow 0.2s;
}
.hl-faq-item:hover { border-color: rgba(255,255,255,0.13); box-shadow: 0 8px 32px rgba(0,0,0,0.3); }
.hl-faq-q {
  padding: 20px 24px; font-size: 14px; font-weight: 600; color: var(--fg);
  display: flex; justify-content: space-between; align-items: center; cursor: pointer; gap: 12px;
}
.hl-faq-q-icon {
  width: 26px; height: 26px; border-radius: 50%; background: rgba(255,255,255,0.06);
  display: flex; align-items: center; justify-content: center; flex-shrink: 0;
  font-size: 16px; color: var(--fg2);
  transition: background 0.2s, transform 0.2s;
}
.hl-faq-item:hover .hl-faq-q-icon { background: rgba(10,132,255,0.1); color: var(--blue); }
.hl-faq-a { padding: 0 24px 20px; font-size: 14px; color: var(--fg2); line-height: 1.8; }

/* ── CTA section ── */
.hl-cta {
  margin: 0 0 120px; padding: 96px 60px; border-radius: 32px;
  background: rgba(6,6,10,0.95);
  border: 1px solid rgba(255,255,255,0.08); text-align: center; position: relative; overflow: hidden;
  box-shadow: 0 40px 80px rgba(0,0,0,0.5);
}
.hl-cta-glow {
  position: absolute; top: -300px; left: 50%; transform: translateX(-50%);
  width: 800px; height: 800px;
  background: radial-gradient(ellipse at center, rgba(10,132,255,0.12) 0%, rgba(48,209,88,0.05) 45%, transparent 68%);
  pointer-events: none; animation: auroraFloat1 10s ease-in-out infinite;
}
.hl-cta-h { font-size: clamp(28px, 4.5vw, 56px); font-weight: 800; letter-spacing: -2.5px; color: var(--fg); line-height: 1.04; max-width: 700px; margin: 0 auto 22px; position: relative; z-index: 1; }
.hl-cta-sub { font-size: 16px; color: var(--fg2); margin: 0 auto 40px; position: relative; z-index: 1; max-width: 520px; line-height: 1.72; text-align: center; }
.hl-cta-btns { display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; position: relative; z-index: 1; }

/* ── Checklist ── */
.hl-checks { display: flex; justify-content: center; gap: 28px; flex-wrap: wrap; margin-top: 40px; }
.hl-check  { display: flex; align-items: center; gap: 7px; font-size: 13px; color: var(--fg3); }

/* ── Contact section ── */
.hl-contact-card {
  background: rgba(8,8,12,0.9); border-radius: 24px; border: 1px solid rgba(255,255,255,0.07);
  padding: 44px; max-width: 560px; margin: 0 auto 100px;
  text-align: center; backdrop-filter: blur(12px);
  box-shadow: 0 20px 60px rgba(0,0,0,0.4);
}
.hl-contact-card h3 { font-size: 22px; font-weight: 800; color: var(--fg); letter-spacing: -0.8px; margin-bottom: 10px; }
.hl-contact-card p { font-size: 14px; color: var(--fg3); line-height: 1.7; margin-bottom: 28px; }
.hl-contact-email {
  display: inline-flex; align-items: center; gap: 10px;
  padding: 14px 28px; border-radius: 14px;
  background: rgba(10,132,255,0.07); border: 1px solid rgba(10,132,255,0.22);
  color: #4db3ff; font-size: 14px; font-weight: 600; text-decoration: none;
  font-family: 'JetBrains Mono', monospace;
  transition: background 0.2s, border-color 0.2s, box-shadow 0.2s;
  word-break: break-all;
}
.hl-contact-email:hover { background: rgba(10,132,255,0.13); border-color: rgba(10,132,255,0.4); box-shadow: 0 0 24px rgba(10,132,255,0.15); }
.hl-contact-meta { margin-top: 20px; font-size: 12px; color: rgba(245,245,247,0.24); }

/* ── Footer ── */
.hl-footer {
  border-top: 1px solid rgba(255,255,255,0.06); padding: 44px 32px;
  display: grid; grid-template-columns: 1fr auto; align-items: center;
  max-width: 1140px; margin: 0 auto; gap: 20px;
}
.hl-footer-left { display: flex; flex-direction: column; gap: 10px; }
.hl-footer-copy { font-size: 13px; font-weight: 600; color: var(--fg3); }
.hl-footer-tagline { font-size: 12px; color: rgba(245,245,247,0.18); }
.hl-footer-links { display: flex; gap: 24px; }
.hl-footer-links a { font-size: 13px; color: rgba(245,245,247,0.28); text-decoration: none; transition: color 0.2s; }
.hl-footer-links a:hover { color: var(--fg2); }

/* ── Testimonial ticker ── */
.hl-ticker-wrap {
  overflow: hidden; padding: 48px 0; background: #000;
  border-top: 1px solid rgba(255,255,255,0.05);
  border-bottom: 1px solid rgba(255,255,255,0.05);
  mask-image: linear-gradient(90deg, transparent, black 8%, black 92%, transparent);
}
.hl-ticker-track {
  display: flex; gap: 24px; width: max-content;
  animation: tickerScroll 36s linear infinite;
}
.hl-ticker-track:hover { animation-play-state: paused; }
.hl-ticker-item {
  background: rgba(10,10,14,0.9); border: 1px solid rgba(255,255,255,0.08);
  border-radius: 18px; padding: 20px 26px; min-width: 320px; max-width: 360px;
  flex-shrink: 0; backdrop-filter: blur(8px);
  transition: border-color 0.2s, transform 0.2s;
}
.hl-ticker-item:hover { border-color: rgba(255,255,255,0.16); transform: translateY(-3px); }
.hl-ticker-quote { font-size: 13px; color: var(--fg2); line-height: 1.74; margin-bottom: 14px; font-style: italic; }
.hl-ticker-author { display: flex; align-items: center; gap: 10px; }
.hl-ticker-avatar { width: 34px; height: 34px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700; flex-shrink: 0; }
.hl-ticker-name { font-size: 12px; font-weight: 700; color: var(--fg); }
.hl-ticker-role { font-size: 11px; color: var(--fg3); margin-top: 1px; }

/* Stars in ticker */
.hl-ticker-stars { color: #ff9f0a; font-size: 10px; margin-bottom: 8px; letter-spacing: 1px; }

/* ── Keyframes ── */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(32px); }
  to   { opacity: 1; transform: none; }
}
@keyframes gradientShift {
  0%   { background-position: 0% 50%; }
  50%  { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
@keyframes shimmerBg {
  0%   { background-position: 200% center; }
  100% { background-position: -200% center; }
}
@keyframes pulse {
  0%, 100% { opacity: 1; box-shadow: 0 0 8px var(--blue); }
  50%       { opacity: 0.5; box-shadow: 0 0 4px var(--blue); }
}
@keyframes tickerScroll {
  0%   { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
@keyframes spin {
  to { transform: rotate(360deg); }
}
@keyframes heroOrb {
  0%, 100% { transform: translate(-50%, -50%) scale(1); }
  50% { transform: translate(-50%, -50%) scale(1.08); }
}

/* ── Orb decoration in hero ── */
.hl-orb {
  position: absolute; border-radius: 50%; pointer-events: none;
  animation: heroOrb 8s ease-in-out infinite;
}
.hl-orb-1 {
  width: 400px; height: 400px; top: 20%; left: 50%;
  transform: translate(-50%, -50%);
  background: conic-gradient(from 0deg, rgba(10,132,255,0) 0deg, rgba(10,132,255,0.08) 120deg, rgba(48,209,88,0.06) 240deg, rgba(10,132,255,0) 360deg);
  border: 1px solid rgba(255,255,255,0.04); z-index: 0;
  animation-duration: 12s;
}
.hl-orb-ring {
  position: absolute; border-radius: 50%; pointer-events: none; z-index: 0;
  border: 1px solid rgba(255,255,255,0.03);
}

/* ── Responsive ── */
@media (max-width: 900px) {
  .hl-story-grid { grid-template-columns: 1fr; gap: 44px; }
  .hl-steps { grid-template-columns: 1fr 1fr; }
  .hl-step:first-child  { border-radius: 20px 0 0 0; }
  .hl-step:nth-child(2) { border-radius: 0 20px 0 0; }
  .hl-step:nth-child(3) { border-radius: 0 0 0 20px; }
  .hl-step:last-child   { border-radius: 0 0 20px 0; }
  .hl-ctas { flex-direction: column; align-items: center; }
  .hl-nav-links { display: none; }
  .hl-hamburger { display: flex; }
  .hl-cta { padding: 56px 28px; }
  .hl-card-grid { grid-template-columns: 1fr; }
  .hl-compare-head, .hl-compare-row { grid-template-columns: 1.4fr 1fr; }
  .hl-compare-head > *:nth-child(3),
  .hl-compare-head > *:nth-child(4),
  .hl-compare-row > *:nth-child(3),
  .hl-compare-row > *:nth-child(4) { display: none; }
  .hl-highlight-grid { grid-template-columns: 1fr 1fr; }
  .hl-highlight:first-child { border-radius: 20px 0 0 0; }
  .hl-highlight:nth-child(2) { border-radius: 0 20px 0 0; }
  .hl-highlight:nth-child(5) { border-radius: 0 0 0 20px; }
  .hl-highlight:last-child { border-radius: 0 0 20px 0; }
  .hl-footer { grid-template-columns: 1fr; }
  .hl-sticky-text { display: none; }
}
""")

# ─── SVG helpers ──────────────────────────────────────────────────────────────
def ats_ring(score=78):
    r, c, sw = 38, 48, 5
    circ = 2 * math.pi * r
    fill = (score / 100) * circ
    off  = circ * 0.25
    return (
        '<svg width="96" height="96" viewBox="0 0 96 96" fill="none">'
        '<circle cx="' + str(c) + '" cy="' + str(c) + '" r="' + str(r) + '" stroke="rgba(255,255,255,0.05)" stroke-width="' + str(sw) + '"/>'
        '<circle cx="' + str(c) + '" cy="' + str(c) + '" r="' + str(r) + '" stroke="url(#ag)" stroke-width="' + str(sw) + '"'
        ' stroke-dasharray="' + str(round(fill,1)) + ' ' + str(round(circ,1)) + '"'
        ' stroke-dashoffset="-' + str(round(off,1)) + '" stroke-linecap="round" filter="drop-shadow(0 0 4px rgba(48,209,88,0.4))"/>'
        '<text x="' + str(c) + '" y="' + str(c+1) + '" text-anchor="middle" dominant-baseline="middle"'
        ' fill="#f5f5f7" font-size="18" font-weight="800" font-family="Sora,sans-serif">' + str(score) + '</text>'
        '<defs><linearGradient id="ag" x1="0" y1="0" x2="96" y2="96" gradientUnits="userSpaceOnUse">'
        '<stop offset="0%" stop-color="#30d158"/><stop offset="100%" stop-color="#0a84ff"/>'
        '</linearGradient></defs></svg>'
    )

def radar_svg():
    cats   = ["Communication","Technical","Confidence","Structure","Examples"]
    scores = [0.82, 0.74, 0.88, 0.70, 0.78]
    cx = cy = 110; R = 62; n = len(cats)
    def pt(i, frac):
        angle = math.pi/2 + 2*math.pi*i/n
        return cx + R*frac*math.cos(angle), cy - R*frac*math.sin(angle)
    grid = ""
    for lv in [0.25, 0.5, 0.75, 1.0]:
        pts = " ".join(str(round(pt(i,lv)[0],1))+","+str(round(pt(i,lv)[1],1)) for i in range(n))
        op = 0.04 + lv * 0.06
        grid += '<polygon points="'+pts+'" fill="none" stroke="rgba(255,255,255,'+str(round(op,2))+')" stroke-width="1"/>'
    axes = "".join('<line x1="'+str(cx)+'" y1="'+str(cy)+'" x2="'+str(round(pt(i,1)[0],1))+'" y2="'+str(round(pt(i,1)[1],1))+'" stroke="rgba(255,255,255,0.07)" stroke-width="1"/>' for i in range(n))
    poly = " ".join(str(round(pt(i,scores[i])[0],1))+","+str(round(pt(i,scores[i])[1],1)) for i in range(n))
    dots = "".join('<circle class="hl-radar-dot" cx="'+str(round(pt(i,scores[i])[0],1))+'" cy="'+str(round(pt(i,scores[i])[1],1))+'" r="4" fill="#0a84ff" stroke="rgba(10,132,255,0.3)" stroke-width="6" style="transition-delay:'+str(1.2+i*0.1)+'s" filter="drop-shadow(0 0 3px rgba(10,132,255,0.8))"/>' for i in range(n))
    labels = "".join('<text x="'+str(round(pt(i,1.32)[0],1))+'" y="'+str(round(pt(i,1.32)[1],1))+'" text-anchor="middle" dominant-baseline="middle" fill="rgba(245,245,247,0.38)" font-size="8.5" font-family="Sora,sans-serif" font-weight="500">'+cats[i]+'</text>' for i in range(n))
    return ('<svg id="hl-radar-svg" width="220" height="220" viewBox="0 0 220 220" fill="none">'
            +grid+axes
            +'<polygon id="hl-radar-poly" class="hl-radar-polygon" points="'+poly+'" fill="rgba(10,132,255,0.12)" stroke="url(#radarGrad)" stroke-width="1.8"/>'
            +dots+labels
            +'<defs><linearGradient id="radarGrad" x1="0" y1="0" x2="220" y2="220" gradientUnits="userSpaceOnUse">'
            '<stop offset="0%" stop-color="#0a84ff"/><stop offset="100%" stop-color="#30d158"/>'
            '</linearGradient></defs>'
            +'</svg>')

# ─── fragment builders ────────────────────────────────────────────────────────
def ats_bars():
    data = [("Format & Layout",92,"#30d158"),("Keyword Coverage",71,"#ff9f0a"),("Sections Present",85,"#0a84ff"),("Action Verbs",68,"#ff9f0a"),("Contact Info",100,"#30d158"),("Date Consistency",80,"#0a84ff")]
    return "".join(
        '<div class="hl-bar">'
        '<div class="hl-bar-row"><span>'+lbl+'</span><span style="color:'+col+';font-weight:700;font-size:11px">'+str(pct)+'%</span></div>'
        '<div class="hl-bar-track"><div class="hl-bar-fill" style="width:'+str(pct)+'%;background:linear-gradient(90deg,'+col+','+col+'cc);box-shadow:0 0 8px '+col+'44"></div></div>'
        '</div>'
        for lbl,pct,col in data)

def score_bars():
    data = [("Communication","85%","#0a84ff"),("Technical","79%","#bf5af2"),("Confidence","88%","#30d158"),("Structure","74%","#ff9f0a")]
    return "".join(
        '<div style="display:flex;justify-content:space-between;font-size:11px;color:rgba(245,245,247,0.54);margin-bottom:5px"><span>'+dim+'</span><span style="color:'+col+';font-weight:700">'+sc+'</span></div>'
        '<div style="height:3px;background:rgba(255,255,255,0.06);border-radius:2px;margin-bottom:8px;overflow:hidden">'
        '<div style="width:'+sc+';height:100%;background:linear-gradient(90deg,'+col+','+col+'cc);border-radius:2px;box-shadow:0 0 6px '+col+'44"></div></div>'
        for dim,sc,col in data)

def _mini_resume(name, accent, layout="single", active=False, sidebar_bg=None, header_style="bar"):
    act = ' hl-tmpl-act' if active else ''
    badge = ('<div class="hl-tmpl-badge">'+name+'</div>') if active else ''
    def ln(w, col="rgba(255,255,255,0.15)", h="2px", mt="3px"):
        return f'<div style="height:{h};width:{w};background:{col};border-radius:1px;margin-top:{mt}"></div>'
    def name_block(col):
        return (f'<div style="height:4px;width:55%;background:{col};border-radius:1px;margin-bottom:2px"></div>'
                f'<div style="height:2px;width:38%;background:{col};opacity:.5;border-radius:1px"></div>')
    def section_lines(n=3, w_list=None, col="rgba(255,255,255,0.13)"):
        ws = w_list or ["85%","70%","78%","60%","75%"]
        return "".join(ln(ws[i % len(ws)], col) for i in range(n))
    def section_label(col):
        return f'<div style="height:2px;width:40%;background:{col};opacity:.7;border-radius:1px;margin-top:4px;margin-bottom:2px"></div>'
    body = ""
    if layout == "sidebar":
        sb = sidebar_bg or "#1e293b"
        body = (
            f'<div style="display:flex;gap:0;flex:1;min-height:0">'
            f'<div style="width:32%;background:{sb};padding:4px 3px;display:flex;flex-direction:column;gap:2px;">'
            + (f'<div style="height:16px;width:16px;border-radius:50%;background:{accent};opacity:.7;margin:0 auto 3px"></div>' if not sidebar_bg else '')
            + name_block(accent)
            + ln("90%", "rgba(255,255,255,0.2)", "1px")
            + section_label(accent) + ln("80%", "rgba(255,255,255,0.18)") + ln("65%", "rgba(255,255,255,0.18)")
            + section_label(accent) + ln("70%", "rgba(255,255,255,0.18)") + ln("55%", "rgba(255,255,255,0.18)")
            + f'</div>'
            f'<div style="flex:1;padding:4px 4px;display:flex;flex-direction:column;gap:0;">'
            + section_label(accent) + ln("90%") + ln("80%") + ln("70%")
            + section_label(accent) + ln("85%") + ln("75%") + ln("60%")
            + f'</div></div>'
        )
    elif layout == "two-col":
        body = (
            f'<div style="display:flex;gap:4px;flex:1;min-height:0;padding:2px;">'
            f'<div style="flex:1;display:flex;flex-direction:column;gap:0;">'
            + section_label(accent) + ln("90%") + ln("75%") + ln("80%")
            + section_label(accent) + ln("85%") + ln("70%") + ln("65%")
            + f'</div>'
            f'<div style="flex:1;display:flex;flex-direction:column;gap:0;">'
            + section_label(accent) + ln("80%") + ln("90%") + ln("70%")
            + section_label(accent) + ln("75%") + ln("60%") + ln("80%")
            + f'</div></div>'
        )
    elif layout == "timeline":
        body = (
            f'<div style="flex:1;padding:2px 3px;display:flex;flex-direction:column;gap:0;">'
            + section_label(accent)
            + (f'<div style="display:flex;align-items:flex-start;gap:3px;margin-top:2px">'
               f'<div style="width:4px;height:4px;border-radius:50%;background:{accent};flex-shrink:0;margin-top:1px"></div>'
               f'<div style="flex:1">' + ln("85%") + ln("70%") + f'</div></div>'
               f'<div style="margin-left:3px;width:1px;height:5px;background:{accent};opacity:.3;margin-left:5px"></div>'
               f'<div style="display:flex;align-items:flex-start;gap:3px">'
               f'<div style="width:4px;height:4px;border-radius:50%;background:{accent};flex-shrink:0;margin-top:1px"></div>'
               f'<div style="flex:1">' + ln("78%") + ln("62%") + f'</div></div>')
            + section_label(accent) + ln("90%") + ln("75%")
            + f'</div>'
        )
    else:
        body = (
            f'<div style="flex:1;padding:2px 3px;display:flex;flex-direction:column;gap:0;">'
            + section_label(accent) + ln("90%") + ln("80%") + ln("72%")
            + section_label(accent) + ln("85%") + ln("68%") + ln("76%")
            + section_label(accent) + ln("70%") + ln("55%")
            + f'</div>'
        )
    if header_style == "band":
        hdr = (f'<div style="background:{accent};padding:4px 5px;border-radius:3px 3px 0 0;">'
               f'<div style="height:3px;width:50%;background:rgba(255,255,255,0.9);border-radius:1px;margin-bottom:1px"></div>'
               f'<div style="height:2px;width:32%;background:rgba(255,255,255,0.55);border-radius:1px"></div></div>')
    elif header_style == "left-accent":
        hdr = (f'<div style="border-left:2px solid {accent};padding:3px 5px;">'
               f'<div style="height:3px;width:50%;background:rgba(255,255,255,0.7);border-radius:1px;margin-bottom:1px"></div>'
               f'<div style="height:2px;width:30%;background:{accent};border-radius:1px"></div>'
               f'<div style="margin-top:2px;display:flex;gap:3px">'
               f'<div style="height:2px;width:22%;background:rgba(255,255,255,0.2);border-radius:1px"></div>'
               f'<div style="height:2px;width:18%;background:rgba(255,255,255,0.2);border-radius:1px"></div>'
               f'</div></div>')
    elif header_style == "center":
        hdr = (f'<div style="text-align:center;padding:4px 3px;border-bottom:1px solid {accent}20;">'
               f'<div style="height:3px;width:45%;background:rgba(255,255,255,0.75);border-radius:1px;margin:0 auto 2px"></div>'
               f'<div style="height:2px;width:28%;background:{accent};border-radius:1px;margin:0 auto 2px"></div>'
               f'<div style="display:flex;justify-content:center;gap:3px">'
               f'<div style="height:1.5px;width:14%;background:rgba(255,255,255,0.2);border-radius:1px"></div>'
               f'<div style="height:1.5px;width:14%;background:rgba(255,255,255,0.2);border-radius:1px"></div>'
               f'</div></div>')
    else:
        if layout == "sidebar":
            hdr = ""
        else:
            hdr = (f'<div style="height:4px;background:{accent};border-radius:3px 3px 0 0;margin-bottom:3px"></div>'
                   f'<div style="padding:0 4px 2px;">'
                   f'<div style="height:3px;width:52%;background:rgba(255,255,255,0.7);border-radius:1px;margin-bottom:2px"></div>'
                   f'<div style="height:2px;width:34%;background:{accent};opacity:.6;border-radius:1px"></div>'
                   f'<div style="display:flex;gap:3px;margin-top:2px">'
                   f'<div style="height:1.5px;width:16%;background:rgba(255,255,255,0.18);border-radius:1px"></div>'
                   f'<div style="height:1.5px;width:16%;background:rgba(255,255,255,0.18);border-radius:1px"></div>'
                   f'</div></div>')
    return (f'<div class="hl-tmpl{act}" style="display:flex;flex-direction:column;padding:0;overflow:hidden;">'
            + hdr + body + badge + f'</div>')

def tmpl_gallery():
    templates = [
        ("Modern",    "#0a84ff", "center",   "center",       None,      True),
        ("Classic",   "#f5f5f7", "single",   "left-accent",  None,      False),
        ("Executive", "#ff9f0a", "single",   "band",         None,      False),
        ("Timeline",  "#30d158", "timeline", "bar",          None,      False),
        ("Corporate", "#1d4ed8", "sidebar",  "bar",          "#1a2744", False),
        ("Slate",     "#64748b", "sidebar",  "bar",          "#1a1f2a", False),
        ("Rose",      "#fb7185", "single",   "band",         None,      False),
        ("Midnight",  "#a78bfa", "two-col",  "bar",          None,      False),
    ]
    out = ""
    for name, accent, layout, hdr_style, sb_bg, active in templates[:8]:
        out += _mini_resume(name, accent, layout, active, sb_bg, hdr_style)
    return out

def job_cards():
    jobs = [
        ("SDE II","Google","Mountain View · Full-time","#4285f4","G",True),
        ("ML Engineer","Anthropic","Remote · Full-time","#d97706","A",False),
        ("Backend Dev","Razorpay","Bangalore · Full-time","#2563eb","R",False),
        ("Data Analyst","Zepto","Mumbai · Hybrid","#7c3aed","Z",False)
    ]
    out = ""
    for title,co,meta,col,letter,featured in jobs:
        bb  = "rgba(10,132,255,0.12)" if featured else "rgba(255,255,255,0.04)"
        bc  = "#4db3ff"               if featured else "rgba(245,245,247,0.3)"
        btx = "Featured"              if featured else "New"
        badge_shadow = ";box-shadow:0 0 10px rgba(10,132,255,0.2)" if featured else ""
        out += '<div class="hl-job"><div class="hl-job-logo" style="background:'+col+'22;color:'+col+'">'+letter+'</div><div style="flex:1;min-width:0"><div class="hl-job-title">'+title+' — '+co+'</div><div class="hl-job-co">'+meta+'</div></div><div class="hl-job-badge" style="background:'+bb+';color:'+bc+';border:1px solid '+bc+'44'+badge_shadow+'">'+btx+'</div></div>'
    return out

def checklist():
    items = ["ATS score in seconds","Bias detection & rewrite","15 resume templates","Cover letter generator","Live job search","AI Interview Coach"]
    chk = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    return "".join('<div class="hl-check">'+chk+'<span>'+item+'</span></div>' for item in items)

def pills(labels):
    return "".join('<span class="hl-pill">'+l+'</span>' for l in labels)

def chk_y():
    return '<span class="hl-chk-y">&#10003;</span>'

def chk_n():
    return '<span class="hl-chk-n">&mdash;</span>'

def chk_p(t):
    return '<span class="hl-chk-p">' + t + '</span>'

# ─── SECTIONS ─────────────────────────────────────────────────────────────────
def render_banner():
    H('<div class="hl-banner">'
      '<span class="hl-banner-badge">New</span>'
      'AI Interview Coach is live &mdash; Practice with resume-based questions &amp; get instant scoring. '
      '<a href="' + APP_URL + '" target="_blank">Try it free &rarr;</a>'
      '</div>')

def render_nav():
    H('<div id="sp"></div>'
      '<div class="hl-noise"></div>'
      # Mobile drawer
      '<div id="hl-drawer">'
      '<button id="hl-drawer-close" onclick="closeDrawer()">&times;</button>'
      '<a href="#how" onclick="closeDrawer()">How it works</a>'
      '<a href="#analyzer" onclick="closeDrawer()">Analyzer</a>'
      '<a href="#builder" onclick="closeDrawer()">Builder</a>'
      '<a href="#career" onclick="closeDrawer()">Career Hub</a>'
      '<a href="#compare" onclick="closeDrawer()">Compare</a>'
      '<a href="#contact" onclick="closeDrawer()">Contact</a>'
      '<a href="' + APP_URL + '" target="_blank" style="color:#0a84ff!important">Open App &rarr;</a>'
      '</div>'
      # Toast
      '<div id="hl-toast"><div id="hl-toast-dot"></div><span id="hl-toast-msg"></span></div>'
      # Sticky CTA
      '<div id="hl-sticky-cta">'
      '<div class="hl-sticky-inner">'
      '<div class="hl-sticky-text">Ready to land your next role? <span>Hirelyzer is 100% free.</span></div>'
      '<div class="hl-sticky-btns">'
      '<a href="' + APP_URL + '" target="_blank" class="hl-btn-p" style="padding:10px 22px;font-size:13px">'
      '<svg width="12" height="12" viewBox="0 0 24 24" fill="#fff"><path d="M12 2L13.8 8.2L20 10L13.8 11.8L12 18L10.2 11.8L4 10L10.2 8.2L12 2Z"/></svg>'
      'Analyse my resume free</a>'
      '<button id="hl-sticky-dismiss" onclick="dismissSticky()" title="Dismiss">&times;</button>'
      '</div></div></div>'
      # Section dot nav
      '<div id="hl-dots">'
      '<button class="hl-dot-nav" data-section="hl-hero-anchor" title="Hero"></button>'
      '<button class="hl-dot-nav" data-section="how" title="How it works"></button>'
      '<button class="hl-dot-nav" data-section="analyzer" title="Analyzer"></button>'
      '<button class="hl-dot-nav" data-section="builder" title="Builder"></button>'
      '<button class="hl-dot-nav" data-section="career" title="Career Hub"></button>'
      '<button class="hl-dot-nav" data-section="compare" title="Compare"></button>'
      '<button class="hl-dot-nav" data-section="contact" title="Contact"></button>'
      '</div>'
      # Nav bar
      '<nav class="hl-nav" id="hl-nav">'
      '<div class="hl-nav-inner">'
      '<a href="#hl-hero-anchor" class="hl-logo">'
      '<div class="hl-logo-icon">'
      '<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M12 2L2 7l10 5 10-5-10-5z M2 17l10 5 10-5 M2 12l10 5 10-5" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
      '</div>HIRELYZER'
      '</a>'
      '<div class="hl-nav-links">'
      '<a href="#how" data-nav="how">How it works</a>'
      '<a href="#analyzer" data-nav="analyzer">Analyzer</a>'
      '<a href="#builder" data-nav="builder">Builder</a>'
      '<a href="#career" data-nav="career">Career Hub</a>'
      '<a href="#compare" data-nav="compare">Compare</a>'
      '</div>'
      '<div class="hl-nav-right">'
      '<button class="hl-hamburger" id="hl-hamburger" onclick="openDrawer()" aria-label="Open menu">'
      '<span></span><span></span><span></span>'
      '</button>'
      '<a href="' + APP_URL + '" target="_blank" class="hl-nav-cta">'
      '<svg width="12" height="12" viewBox="0 0 24 24" fill="#fff"><path d="M12 2L13.8 8.2L20 10L13.8 11.8L12 18L10.2 11.8L4 10L10.2 8.2L12 2Z"/></svg>'
      'Try it free'
      '</a>'
      '</div>'
      '</div></nav>')

def render_hero():
    H('<div class="hl-hero">'
      '<div id="hl-hero-anchor" style="position:absolute;top:0;pointer-events:none"></div>'

      # Aurora layers
      '<div class="hl-aurora">'
      '<div class="hl-aurora-1"></div>'
      '<div class="hl-aurora-2"></div>'
      '<div class="hl-aurora-3"></div>'
      '</div>'

      # Orbital rings
      '<div class="hl-orb hl-orb-1"></div>'
      '<div class="hl-orb-ring" style="width:560px;height:560px;top:50%;left:50%;transform:translate(-50%,-50%) translateY(-80px)"></div>'
      '<div class="hl-orb-ring" style="width:720px;height:720px;top:50%;left:50%;transform:translate(-50%,-50%) translateY(-80px)"></div>'

      # Particle canvas
      '<canvas id="hl-particles"></canvas>'

      # Grid + spotlight
      '<div class="hl-hero-grid"></div>'
      '<div id="hl-spotlight"></div>'
      '<div class="hl-hero-fade"></div>'

      '<div class="hl-hero-content">'
      '<div class="hl-eyebrow">'
      '<div class="hl-eyebrow-dot"></div>'
      'AI-Powered Career Platform &mdash; 100% Free'
      '</div>'

      '<h1 class="hl-h1">The career tools<br>everyone <span id="hl-typewriter">needs</span><span class="hl-cursor"></span></h1>'

      '<p class="hl-hero-sub">ATS scoring, bias detection, 15 resume templates, live job search, and an AI interview coach &mdash; everything in one intelligent platform.</p>'

      '<div class="hl-ctas">'
      '<a href="' + APP_URL + '" target="_blank" class="hl-btn-p" style="font-size:15px;padding:16px 36px">'
      '<svg width="15" height="15" viewBox="0 0 24 24" fill="#fff"><path d="M12 2L13.8 8.2L20 10L13.8 11.8L12 18L10.2 11.8L4 10L10.2 8.2L12 2Z"/></svg>'
      'Analyse my resume free'
      '</a>'
      '<a href="#how" class="hl-btn-g" style="font-size:15px;padding:16px 32px">'
      '<svg width="15" height="15" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="1.6" fill="none"/><path d="M10 8l6 4-6 4V8z" fill="currentColor"/></svg>'
      'See how it works'
      '</a>'
      '</div>'

      '<div class="hl-hero-features">'
      '<div class="hl-hf-item"><svg width="12" height="12" viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.2" stroke-linecap="round"/></svg>ATS Scoring</div>'
      '<div class="hl-hf-sep"></div>'
      '<div class="hl-hf-item"><svg width="12" height="12" viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.2" stroke-linecap="round"/></svg>Bias Detection</div>'
      '<div class="hl-hf-sep"></div>'
      '<div class="hl-hf-item"><svg width="12" height="12" viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.2" stroke-linecap="round"/></svg>15 Templates</div>'
      '<div class="hl-hf-sep"></div>'
      '<div class="hl-hf-item"><svg width="12" height="12" viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.2" stroke-linecap="round"/></svg>Job Search</div>'
      '<div class="hl-hf-sep"></div>'
      '<div class="hl-hf-item"><svg width="12" height="12" viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.2" stroke-linecap="round"/></svg>Interview Coach</div>'
      '</div>'

      # Hero mock UI card
      '<div class="hl-card">'
      '<div class="hl-card-bar">'
      '<div class="hl-dot" style="background:#ff453a"></div>'
      '<div class="hl-dot" style="background:#ff9f0a"></div>'
      '<div class="hl-dot" style="background:#30d158"></div>'
      '<span class="hl-card-tab">hirelyzer.app &mdash; ATS Analysis</span>'
      '</div>'
      '<div class="hl-card-body">'
      '<div class="hl-card-grid">'

      # Panel 1: ATS Score
      '<div>'
      '<div class="hl-ptitle"><svg width="8" height="8" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#30d158"/></svg> ATS Score</div>'
      '<div style="display:flex;align-items:center;gap:14px;margin-bottom:16px">'
      + ats_ring(78) +
      '<div>'
      '<div style="font-size:8px;color:rgba(245,245,247,0.34);text-transform:uppercase;letter-spacing:.9px;font-weight:700;margin-bottom:4px">Status</div>'
      '<div style="font-size:11px;color:#30d158;font-weight:700">Good &middot; Minor fixes</div>'
      '<div style="font-size:10px;color:rgba(245,245,247,0.3);margin-top:4px">Parsed in 1.4s</div>'
      '</div></div>'
      + ats_bars() +
      '</div>'

      # Panel 2: Bias
      '<div>'
      '<div class="hl-ptitle"><svg width="8" height="8" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#bf5af2"/></svg> Bias Analysis</div>'
      '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:14px">'
      '<div style="padding:12px;background:rgba(10,132,255,0.07);border-radius:10px;border:1px solid rgba(10,132,255,0.16)"><div style="font-size:8px;text-transform:uppercase;letter-spacing:.9px;color:rgba(245,245,247,0.3);font-weight:700;margin-bottom:5px">Masculine</div><div style="font-size:24px;font-weight:800;color:#4db3ff">8</div></div>'
      '<div style="padding:12px;background:rgba(191,90,242,0.07);border-radius:10px;border:1px solid rgba(191,90,242,0.16)"><div style="font-size:8px;text-transform:uppercase;letter-spacing:.9px;color:rgba(245,245,247,0.3);font-weight:700;margin-bottom:5px">Feminine</div><div style="font-size:24px;font-weight:800;color:#d07ef7">3</div></div>'
      '</div>'
      '<div style="font-size:9px;color:rgba(245,245,247,0.3);font-weight:700;text-transform:uppercase;letter-spacing:.9px;margin-bottom:9px">Flagged words</div>'
      '<div class="hl-words"><span class="wc wc-m">driven</span><span class="wc wc-m">aggressive</span><span class="wc wc-m">dominate</span><span class="wc wc-f">nurture</span><span class="wc wc-n">deliver</span><span class="wc wc-n">execute</span></div>'
      '<div style="padding:12px;background:rgba(48,209,88,0.07);border-radius:10px;border:1px solid rgba(48,209,88,0.18);margin-top:10px">'
      '<div style="font-size:10px;font-weight:700;color:#30d158;margin-bottom:5px">AI Rewrite</div>'
      '<div style="font-size:11px;color:rgba(245,245,247,0.5);line-height:1.6"><span style="text-decoration:line-through;opacity:.4">Aggressively drove</span> &rarr; <span style="color:#30d158">Accelerated results</span></div>'
      '</div>'
      '</div>'

      # Panel 3: Fix list
      '<div>'
      '<div class="hl-ptitle"><svg width="8" height="8" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#ff9f0a"/></svg> Priority Fixes</div>'
      '<div style="padding:9px 12px;background:rgba(255,159,10,0.07);border-radius:9px;border:1px solid rgba(255,159,10,0.18);display:flex;align-items:center;gap:8px;margin-bottom:8px">'
      '<svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M12 9v4M12 17h.01" stroke="#ff9f0a" stroke-width="2" stroke-linecap="round"/><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z" stroke="#ff9f0a" stroke-width="1.5" fill="none"/></svg>'
      '<span style="font-size:12px;color:#ff9f0a;font-weight:600">Add measurable impact</span>'
      '</div>'
      '<div style="padding:9px 12px;background:rgba(255,159,10,0.07);border-radius:9px;border:1px solid rgba(255,159,10,0.18);display:flex;align-items:center;gap:8px;margin-bottom:8px">'
      '<svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M12 9v4M12 17h.01" stroke="#ff9f0a" stroke-width="2" stroke-linecap="round"/><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z" stroke="#ff9f0a" stroke-width="1.5" fill="none"/></svg>'
      '<span style="font-size:12px;color:#ff9f0a;font-weight:600">Missing 4 key skills</span>'
      '</div>'
      '<div style="padding:9px 12px;background:rgba(255,69,58,0.07);border-radius:9px;border:1px solid rgba(255,69,58,0.18);display:flex;align-items:center;gap:8px">'
      '<svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M18 6L6 18M6 6l12 12" stroke="#ff453a" stroke-width="2" stroke-linecap="round"/></svg>'
      '<span style="font-size:12px;color:#ff453a;font-weight:600">Objective outdated</span>'
      '</div>'
      '</div>'

      '</div>'  # grid
      '</div>'  # body
      '</div>'  # card

      # Stats
      '<div class="hl-stats">'
      '<div class="hl-stat"><div class="hl-stat-n" data-count="15" data-suffix="+">15+</div><div class="hl-stat-l">Templates</div></div>'
      '<div class="hl-stat"><div class="hl-stat-n" data-count="10" data-suffix="k+">10k+</div><div class="hl-stat-l">Resumes Scored</div></div>'
      '<div class="hl-stat"><div class="hl-stat-n">AI</div><div class="hl-stat-l">LLM Powered</div></div>'
      '<div class="hl-stat"><div class="hl-stat-n">Free</div><div class="hl-stat-l">No Sign-up</div></div>'
      '<div class="hl-stat"><div class="hl-stat-n" data-count="5">5</div><div class="hl-stat-l">Core Modules</div></div>'
      '</div>'

      '</div>'  # hero-content
      '</div>')  # hero

def render_how():
    H('<div id="how" style="padding:100px 0 60px;background:#000">'
      '<div class="hl-section">'
      '<div class="hl-divider hl-reveal">How it works</div>'
      '<div class="hl-steps">'

      '<div class="hl-step hl-reveal hl-reveal-delay-1"><span class="hl-step-n">01</span>'
      '<svg class="hl-step-icon" viewBox="0 0 44 44" fill="none"><rect width="44" height="44" rx="12" fill="rgba(10,132,255,0.1)"/><path d="M22 28V20M22 20L19 23M22 20L25 23" stroke="#0a84ff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M15 30h14" stroke="#0a84ff" stroke-width="1.6" stroke-linecap="round"/><rect x="14" y="13" width="16" height="19" rx="3" stroke="#0a84ff" stroke-width="1.4" stroke-dasharray="3 2" fill="none"/></svg>'
      '<div class="hl-step-title">Upload your resume</div>'
      '<div class="hl-step-desc">Drop any PDF. Our parser handles messy formats, multi-column layouts, and scanned documents via OCR fallback.</div></div>'

      '<div class="hl-step hl-reveal hl-reveal-delay-2"><span class="hl-step-n">02</span>'
      '<svg class="hl-step-icon" viewBox="0 0 44 44" fill="none"><rect width="44" height="44" rx="12" fill="rgba(48,209,88,0.1)"/><circle cx="20" cy="20" r="7" stroke="#30d158" stroke-width="1.5" fill="none"/><path d="M20 17v3l2 1.5" stroke="#30d158" stroke-width="1.5" stroke-linecap="round"/><path d="M25.2 25.2l3.5 3.5" stroke="#30d158" stroke-width="1.7" stroke-linecap="round"/></svg>'
      '<div class="hl-step-title">Instant AI analysis</div>'
      '<div class="hl-step-desc">ATS scoring, bias detection, grammar check, keyword matching &mdash; all computed in seconds with detailed feedback.</div></div>'

      '<div class="hl-step hl-reveal hl-reveal-delay-3"><span class="hl-step-n">03</span>'
      '<svg class="hl-step-icon" viewBox="0 0 44 44" fill="none"><rect width="44" height="44" rx="12" fill="rgba(191,90,242,0.1)"/><rect x="12" y="11" width="13" height="18" rx="2.5" stroke="#bf5af2" stroke-width="1.5" fill="none"/><rect x="19" y="16" width="14" height="18" rx="2.5" fill="rgba(191,90,242,0.08)" stroke="#bf5af2" stroke-width="1.5"/><path d="M22 21h8M22 24.5h8M22 28h5" stroke="#bf5af2" stroke-width="1.3" stroke-linecap="round"/><circle cx="32" cy="13" r="4" fill="#bf5af2"/><path d="M30.5 13l1 1 2-2" stroke="#fff" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
      '<div class="hl-step-title">Build or rewrite</div>'
      '<div class="hl-step-desc">Use the AI rewriter or open the full Resume Builder. Choose from 15 templates, generate a cover letter, export to PDF or DOCX.</div></div>'

      '<div class="hl-step hl-reveal hl-reveal-delay-3"><span class="hl-step-n">04</span>'
      '<svg class="hl-step-icon" viewBox="0 0 44 44" fill="none"><rect width="44" height="44" rx="12" fill="rgba(255,159,10,0.1)"/><path d="M22 28c-3.31 0-6-2.69-6-6 0-4 3-8 6-9 3 1 6 5 6 9 0 3.31-2.69 6-6 6z" stroke="#ff9f0a" stroke-width="1.5" fill="none"/><circle cx="22" cy="22" r="2" fill="#ff9f0a"/><path d="M29 13l-2 2M15 13l2 2" stroke="#ff9f0a" stroke-width="1.4" stroke-linecap="round"/></svg>'
      '<div class="hl-step-title">Apply with confidence</div>'
      '<div class="hl-step-desc">Discover live job listings, salary benchmarks, curated courses, and practice with the AI Interview Coach before applying.</div></div>'

      '</div></div></div>')

def render_story_ats():
    ring = ats_ring(78)
    bars = ats_bars()
    p = pills(["ATS Score","6-Dimension Breakdown","Keyword Gap","Grammar Check","Downloadable Report"])
    H('<div id="analyzer" class="hl-story"><div class="hl-section"><div class="hl-story-grid">'
      '<div class="hl-reveal">'
      '<div class="hl-story-num">Feature 01 &mdash; Resume Analyzer</div>'
      '<h2 class="hl-story-h">Your resume, <span class="hl-blue">scored like a machine</span> reads it</h2>'
      '<p class="hl-story-p">Most resumes never reach a human. Applicant Tracking Systems silently filter them on format, missing keywords, or structural issues. Hirelyzer&rsquo;s analyzer replicates how ATS parsers actually read your document &mdash; not just a surface keyword match.</p>'
      '<p class="hl-story-p">You get a score across six dimensions, a prioritised fix list, grammar and readability signals, and a full keyword-gap report mapped to the roles you care about.</p>'
      '<div class="hl-pills">' + p + '</div>'
      '</div>'
      '<div class="hl-reveal hl-reveal-delay-2"><div class="hl-panel">'
      '<div class="hl-ptitle"><svg width="11" height="11" viewBox="0 0 11 11"><circle cx="5.5" cy="5.5" r="5.5" fill="#30d158"/></svg>ATS Analysis Report</div>'
      '<div style="display:flex;align-items:center;gap:18px;margin-bottom:22px">'
      + ring +
      '<div>'
      '<div style="font-size:9px;color:rgba(245,245,247,0.34);text-transform:uppercase;letter-spacing:.9px;font-weight:700;margin-bottom:4px">Overall Score</div>'
      '<div style="font-size:11px;color:#30d158;font-weight:700">Good &middot; Minor fixes needed</div>'
      '<div style="font-size:10px;color:rgba(245,245,247,0.3);margin-top:4px">Parsed in 1.4s</div>'
      '</div></div>'
      + bars +
      '</div></div>'
      '</div></div></div>')

def render_story_bias():
    p = pills(["Gender-coded Detection","AI Neutral Rewrite","Lexicon of 400+ Words","One-click Apply"])
    H('<div class="hl-story-alt"><div class="hl-section"><div class="hl-story-grid">'
      '<div style="order:2" class="hl-reveal">'
      '<div class="hl-story-num">Feature 02 &mdash; Bias Detection</div>'
      '<h2 class="hl-story-h">Bias-free language that <span class="hl-purp">opens every door</span></h2>'
      '<p class="hl-story-p">Gender-coded words can unconsciously signal culture fit to recruiters. Hirelyzer scans every verb, adjective, and phrase against a curated bias lexicon of 400+ terms.</p>'
      '<p class="hl-story-p">The AI rewriter suggests impact-neutral alternatives, preserving your achievements while broadening appeal across hiring contexts.</p>'
      '<div class="hl-pills">' + p + '</div>'
      '</div>'
      '<div style="order:1" class="hl-reveal hl-reveal-delay-2"><div class="hl-panel">'
      '<div class="hl-ptitle"><svg width="11" height="11" viewBox="0 0 11 11"><circle cx="5.5" cy="5.5" r="5.5" fill="#bf5af2"/></svg>Bias Analysis Report</div>'
      '<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:16px">'
      '<div style="padding:14px;background:rgba(10,132,255,0.06);border-radius:12px;border:1px solid rgba(10,132,255,0.15)"><div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:rgba(245,245,247,0.34);font-weight:700;margin-bottom:6px">Masculine</div><div style="font-size:26px;font-weight:800;color:#4db3ff;letter-spacing:-1px">8</div><div style="font-size:11px;color:rgba(245,245,247,0.34)">words flagged</div></div>'
      '<div style="padding:14px;background:rgba(191,90,242,0.06);border-radius:12px;border:1px solid rgba(191,90,242,0.15)"><div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:rgba(245,245,247,0.34);font-weight:700;margin-bottom:6px">Feminine</div><div style="font-size:26px;font-weight:800;color:#d07ef7;letter-spacing:-1px">3</div><div style="font-size:11px;color:rgba(245,245,247,0.34)">words flagged</div></div>'
      '</div>'
      '<div style="font-size:10px;color:rgba(245,245,247,0.34);font-weight:700;text-transform:uppercase;letter-spacing:.9px;margin-bottom:10px">Detected language</div>'
      '<div class="hl-words"><span class="wc wc-m">driven</span><span class="wc wc-m">aggressive</span><span class="wc wc-m">dominate</span><span class="wc wc-m">champion</span><span class="wc wc-f">nurture</span><span class="wc wc-f">support</span><span class="wc wc-n">deliver</span><span class="wc wc-n">execute</span></div>'
      '<div style="padding:14px;background:rgba(48,209,88,0.06);border-radius:12px;border:1px solid rgba(48,209,88,0.18);margin-top:4px">'
      '<div style="font-size:11px;font-weight:700;color:#30d158;margin-bottom:6px;display:flex;align-items:center;gap:6px">'
      '<svg width="10" height="10" viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
      'AI Rewrite Applied</div>'
      '<div style="font-size:12px;color:rgba(245,245,247,0.54);line-height:1.65"><span style="text-decoration:line-through;opacity:.45">Aggressively drove growth</span> &rarr; <span style="color:#30d158;font-weight:600">Accelerated high-impact results</span> across 3 teams</div>'
      '</div>'
      '</div></div>'
      '</div></div></div>')

def render_story_builder():
    tmpl = tmpl_gallery()
    p = pills(["15 Templates","DOCX + PDF Export","AI Cover Letter","Live Preview","ATS Single-Column"])
    H('<div id="builder" class="hl-story"><div class="hl-section"><div class="hl-story-grid">'
      '<div class="hl-reveal">'
      '<div class="hl-story-num">Feature 03 &mdash; Resume Builder</div>'
      '<h2 class="hl-story-h">Build resumes that <span class="hl-green">look as good</span> as they parse</h2>'
      '<p class="hl-story-p">Fifteen ATS-optimised templates &mdash; from understated minimal to executive prestige &mdash; all built on strict single-column structures that parse correctly in every major hiring platform.</p>'
      '<p class="hl-story-p">Export to DOCX (three ATS compliance levels) or PDF. One click generates a tailored cover letter for your target company, formatted and ready to send.</p>'
      '<div class="hl-pills">' + p + '</div>'
      '</div>'
      '<div class="hl-reveal hl-reveal-delay-2"><div class="hl-panel">'
      '<div class="hl-ptitle"><svg width="13" height="13" viewBox="0 0 24 24" fill="none"><rect x="3" y="3" width="10" height="14" rx="2" stroke="#30d158" stroke-width="1.5"/><rect x="11" y="7" width="10" height="14" rx="2" fill="rgba(48,209,88,.08)" stroke="#30d158" stroke-width="1.5"/><path d="M14 11h5M14 14h5M14 17h3" stroke="#30d158" stroke-width="1.3" stroke-linecap="round"/></svg>Template Gallery &mdash; 15 Designs</div>'
      '<div class="hl-tmpl-grid">' + tmpl + '</div>'
      '<div style="padding:14px;background:rgba(10,132,255,0.06);border-radius:12px;border:1px solid rgba(10,132,255,0.18);display:flex;align-items:center;justify-content:space-between;gap:12px">'
      '<div><div style="font-size:12px;font-weight:700;color:#0a84ff">Modern &mdash; ATS Certified</div><div style="font-size:11px;color:rgba(245,245,247,0.34);margin-top:2px">Sora &middot; Navy headings &middot; Single-column</div></div>'
      '<a href="' + APP_URL + '" target="_blank" style="padding:8px 18px;background:#0a84ff;color:#fff;border-radius:100px;font-size:12px;font-weight:600;text-decoration:none;white-space:nowrap;flex-shrink:0;box-shadow:0 4px 16px rgba(10,132,255,0.35)">Use this</a>'
      '</div>'
      '</div></div>'
      '</div></div></div>')

def render_story_career():
    cards = job_cards()
    p = pills(["Live Job Listings","Salary Benchmarks","Course Recommendations","Skills Radar","Remote Filter"])
    H('<div id="career" class="hl-story-alt"><div class="hl-section"><div class="hl-story-grid">'
      '<div style="order:2" class="hl-reveal">'
      '<div class="hl-story-num">Feature 04 &mdash; Career Intelligence</div>'
      '<h2 class="hl-story-h">Jobs, salaries, courses &mdash; <span class="hl-amber">one place</span></h2>'
      '<p class="hl-story-p">The Job Search Hub pulls live listings from LinkedIn, Naukri, Foundit, and Indeed &mdash; or uses the JSearch/RapidAPI engine with remote and employment-type filters.</p>'
      '<p class="hl-story-p">Hirelyzer surfaces salary benchmarks by role and market, curated courses mapped to skill gaps in your resume, and prep videos &mdash; all linked to your career profile.</p>'
      '<div class="hl-pills">' + p + '</div>'
      '</div>'
      '<div style="order:1" class="hl-reveal hl-reveal-delay-2"><div class="hl-panel">'
      '<div class="hl-ptitle"><svg width="13" height="13" viewBox="0 0 24 24" fill="none"><rect x="2" y="7" width="20" height="14" rx="2" stroke="#ff9f0a" stroke-width="1.5"/><path d="M16 7V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v2" stroke="#ff9f0a" stroke-width="1.5"/><path d="M2 13h20" stroke="#ff9f0a" stroke-width="1.3" stroke-linecap="round"/></svg>Job Search Hub</div>'
      + cards +
      '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:6px">'
      '<div style="padding:12px;background:rgba(255,159,10,0.06);border-radius:10px;border:1px solid rgba(255,159,10,0.15)"><div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:rgba(245,245,247,0.34);font-weight:700;margin-bottom:5px">Avg Salary</div><div style="font-size:20px;font-weight:800;color:#ff9f0a;letter-spacing:-1px">&#8377;18&ndash;32 LPA</div><div style="font-size:11px;color:rgba(245,245,247,0.34)">Backend &middot; India</div></div>'
      '<div style="padding:12px;background:rgba(10,132,255,0.06);border-radius:10px;border:1px solid rgba(10,132,255,0.15)"><div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:rgba(245,245,247,0.34);font-weight:700;margin-bottom:5px">Platforms</div><div style="font-size:13px;font-weight:700;color:#f5f5f7;line-height:1.7">LinkedIn &middot; Naukri<br>Foundit &middot; Indeed</div></div>'
      '</div>'
      '</div></div>'
      '</div></div></div>')

def render_story_interview():
    sbars = score_bars()
    radar = radar_svg()
    p = pills(["Resume-based Questions","Real-time AI Scoring","Radar Chart","Session History","Downloadable Report"])
    H('<div class="hl-story"><div class="hl-section"><div class="hl-story-grid">'
      '<div class="hl-reveal">'
      '<div class="hl-story-num">Feature 05 &mdash; AI Interview Coach</div>'
      '<h2 class="hl-story-h">Practice until <span class="hl-blue">every answer</span> lands</h2>'
      '<p class="hl-story-p">Upload your resume and Hirelyzer generates interview questions derived directly from your actual experience &mdash; not generic prompts. Answer in free text; the AI coach scores you on communication, technical depth, confidence, structure, and use of concrete examples.</p>'
      '<p class="hl-story-p">Every session ends with a performance radar chart, a detailed Q&amp;A review, and course recommendations tied to your weakest dimensions.</p>'
      '<div class="hl-pills">' + p + '</div>'
      '</div>'
      '<div class="hl-reveal hl-reveal-delay-2"><div class="hl-panel">'
      '<div class="hl-ptitle" style="justify-content:space-between">'
      '<div style="display:flex;align-items:center;gap:8px"><svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z" stroke="#ff453a" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg>Mock Interview &middot; Session 3</div>'
      '<div class="hl-score-badge"><svg width="8" height="8" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#30d158"/></svg>82 / 100</div>'
      '</div>'
      '<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:start">'
      '<div>'
      '<div class="hl-qa"><div class="hl-q"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" style="flex-shrink:0;margin-top:1px"><circle cx="12" cy="12" r="10" stroke="#0a84ff" stroke-width="1.5"/><path d="M12 16v-4M12 8h.01" stroke="#0a84ff" stroke-width="1.8" stroke-linecap="round"/></svg>Describe your most complex backend system.</div><div class="hl-a">Built a multi-tenant microservices platform handling 2M events/day using Kafka, Redis, and PostgreSQL with 40% lower P99 latency.</div></div>'
      '<div class="hl-qa"><div class="hl-q"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" style="flex-shrink:0;margin-top:1px"><circle cx="12" cy="12" r="10" stroke="#bf5af2" stroke-width="1.5"/><path d="M12 16v-4M12 8h.01" stroke="#bf5af2" stroke-width="1.8" stroke-linecap="round"/></svg>How do you handle technical debt?</div><div class="hl-a">I prioritise tech debt as a first-class roadmap item, quantifying velocity cost before pitching refactors to stakeholders.</div></div>'
      '<div style="margin-top:12px"><div style="font-size:10px;text-transform:uppercase;letter-spacing:.9px;color:rgba(245,245,247,0.34);font-weight:700;margin-bottom:8px">Score breakdown</div>'
      + sbars +
      '</div></div>'
      '<div class="hl-radar-wrap">' + radar + '<div style="font-size:11px;color:rgba(245,245,247,0.34);margin-top:6px;text-align:center">Performance radar</div></div>'
      '</div>'
      '</div></div>'
      '</div></div></div>')

def render_testimonials():
    testimonials = [
        ("&ldquo;Got my ATS score up from 52 to 88 in one session. Landed 3 interviews in a week.&rdquo;", "Arjun M.", "SWE &mdash; Google", "#0a84ff"),
        ("&ldquo;The bias rewriter caught words I had no idea were gendered. Game changer.&rdquo;", "Priya S.", "PM &mdash; Razorpay", "#bf5af2"),
        ("&ldquo;Interview Coach is scary good. It read my actual resume and asked about my internship.&rdquo;", "Rahul D.", "Data Analyst &mdash; Zepto", "#30d158"),
        ("&ldquo;Went from zero callbacks to 4 offers. The keyword gap report was the unlock.&rdquo;", "Sneha K.", "ML Engineer &mdash; Swiggy", "#ff9f0a"),
        ("&ldquo;Best free tool I&rsquo;ve used. The templates are actually beautiful and ATS-safe.&rdquo;", "Amit R.", "Backend Dev &mdash; Freshworks", "#ff453a"),
        ("&ldquo;Spotted that my resume had no skills section. Fixed in 5 min. Callback rate tripled.&rdquo;", "Nisha T.", "Frontend Dev &mdash; Meesho", "#4db3ff"),
    ]

    def card(quote, name, role, color):
        init = name[0]
        return (
            '<div class="hl-ticker-item">'
            '<div class="hl-ticker-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
            '<div class="hl-ticker-quote">' + quote + '</div>'
            '<div class="hl-ticker-author">'
            '<div class="hl-ticker-avatar" style="background:' + color + '22;color:' + color + ';box-shadow:0 0 12px ' + color + '22">' + init + '</div>'
            '<div><div class="hl-ticker-name">' + name + '</div><div class="hl-ticker-role">' + role + '</div></div>'
            '</div></div>'
        )

    cards_html = "".join(card(*t[:4]) for t in testimonials)
    H('<div class="hl-ticker-wrap">'
      '<div class="hl-ticker-track">'
      + cards_html + cards_html +
      '</div></div>')

def render_compare():
    rows = [
        ("ATS Resume Scoring",          chk_y(),       chk_n(),          chk_n()),
        ("6-Dimension Breakdown",        chk_y(),       chk_n(),          chk_n()),
        ("Gender Bias Detection",        chk_y(),       chk_n(),          chk_n()),
        ("AI Neutral Rewrite",           chk_y(),       chk_n(),          chk_n()),
        ("15 Resume Templates",          chk_y(),       chk_p("3&ndash;5"),chk_p("Limited")),
        ("DOCX &amp; PDF Export",        chk_y(),       chk_p("PDF only"), chk_n()),
        ("AI Cover Letter Generator",    chk_y(),       chk_n(),          chk_n()),
        ("Live Job Search (4 platforms)",chk_y(),       chk_n(),          chk_p("1 only")),
        ("Salary Benchmarks",            chk_y(),       chk_n(),          chk_n()),
        ("AI Interview Coach",           chk_y(),       chk_n(),          chk_n()),
        ("Resume-Based Questions",       chk_y(),       chk_n(),          chk_n()),
        ("100% Free, No Sign-up",        chk_y(),       chk_p("Freemium"),chk_p("Paid")),
    ]
    header = (
        '<div class="hl-compare-head">'
        '<div class="hl-ch" style="padding:20px 24px">Feature</div>'
        '<div class="hl-ch hl-ch-hl"><svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M12 2L2 7l10 5 10-5-10-5z M2 17l10 5 10-5 M2 12l10 5 10-5" stroke="#0a84ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Hirelyzer</div>'
        '<div class="hl-ch hl-cc-center">Resumeworded</div>'
        '<div class="hl-ch hl-cc-center">Zety</div>'
        '</div>'
    )
    body = "".join(
        '<div class="hl-compare-row">'
        '<div class="hl-cc hl-cc-feat">' + feat + '</div>'
        '<div class="hl-cc hl-cc-hl hl-cc-center">' + hl + '</div>'
        '<div class="hl-cc hl-cc-center">' + c2 + '</div>'
        '<div class="hl-cc hl-cc-center">' + c3 + '</div>'
        '</div>'
        for feat, hl, c2, c3 in rows
    )
    H('<div id="compare" class="hl-compare">'
      '<div class="hl-section">'
      '<div class="hl-divider hl-reveal">How we compare</div>'
      '<div style="text-align:center;margin-bottom:0" class="hl-reveal">'
      '<h2 style="font-size:clamp(26px,3.5vw,44px);font-weight:800;letter-spacing:-2px;color:#f5f5f7;line-height:1.06">Everything in one place &mdash; <span style="color:#0a84ff">completely free</span></h2>'
      '<div style="font-size:15px;color:rgba(245,245,247,0.5);margin-top:18px;max-width:480px;margin-left:auto;margin-right:auto;line-height:1.74;text-align:center;">No paywalls. No partial features. Hirelyzer gives you the complete career toolkit at zero cost.</div>'
      '</div>'
      '<div class="hl-compare-wrap hl-reveal hl-reveal-delay-2">' + header + body + '</div>'
      '</div></div>')

def render_highlights():
    cards = [
        ("#0a84ff","rgba(10,132,255,0.1)","rgba(10,132,255,0.04)",
         '<path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" stroke="#0a84ff" stroke-width="1.5" fill="none" stroke-linecap="round"/>',
         "ATS-Certified Scoring","Our six-dimension ATS engine parses your resume exactly as real hiring systems do — format, keywords, sections, verbs, contact info, and date consistency."),
        ("#bf5af2","rgba(191,90,242,0.1)","rgba(191,90,242,0.04)",
         '<circle cx="12" cy="12" r="10" stroke="#bf5af2" stroke-width="1.5" fill="none"/><path d="M12 8v4M12 16h.01" stroke="#bf5af2" stroke-width="1.8" stroke-linecap="round"/>',
         "Bias Lexicon of 400+ Terms","A curated gender-coded word database flags masculine and feminine language patterns, then our AI rewrites every phrase to be impact-neutral and inclusive."),
        ("#30d158","rgba(48,209,88,0.1)","rgba(48,209,88,0.04)",
         '<rect x="3" y="3" width="10" height="14" rx="2" stroke="#30d158" stroke-width="1.5" fill="none"/><rect x="11" y="7" width="10" height="14" rx="2" fill="none" stroke="#30d158" stroke-width="1.5"/>',
         "15 ATS-Ready Templates","Every template is single-column, structured to parse in Greenhouse, Lever, Workday, and iCIMS. Export as DOCX (3 compliance tiers) or PDF in one click."),
        ("#ff9f0a","rgba(255,159,10,0.1)","rgba(255,159,10,0.04)",
         '<rect x="2" y="7" width="20" height="14" rx="2" stroke="#ff9f0a" stroke-width="1.5" fill="none"/><path d="M16 7V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v2" stroke="#ff9f0a" stroke-width="1.5"/><path d="M2 13h20" stroke="#ff9f0a" stroke-width="1.3" stroke-linecap="round"/>',
         "Live Job Intelligence","Pull live listings from LinkedIn, Naukri, Foundit, and Indeed with role, location, and remote filters — plus salary benchmarks and curated skill courses."),
        ("#ff453a","rgba(255,69,58,0.1)","rgba(255,69,58,0.04)",
         '<path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z" stroke="#ff453a" stroke-width="1.5" fill="none" stroke-linecap="round"/>',
         "Resume-Based Interview Prep","Questions are generated from your actual resume — not generic prompts. Get scored across 5 competency dimensions with a radar chart and session history."),
        ("#4db3ff","rgba(10,132,255,0.08)","rgba(10,132,255,0.03)",
         '<path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" stroke="#4db3ff" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
         "Instant &mdash; No Sign-up","Upload a PDF and get your full ATS report, bias analysis, keyword gaps, and fix list in under 2 seconds. No account, no email, no credit card."),
    ]
    items = "".join(
        '<div class="hl-highlight hl-reveal" style="--card-glow:' + glow + '">'
        '<div class="hl-hi-icon" style="background:' + bg + ';box-shadow:0 4px 16px ' + glow + '">'
        '<svg width="20" height="20" viewBox="0 0 24 24" fill="none">' + icon + '</svg>'
        '</div>'
        '<div class="hl-hi-title">' + title + '</div>'
        '<div class="hl-hi-desc">' + desc + '</div>'
        '</div>'
        for col, bg, glow, icon, title, desc in cards
    )
    H('<div class="hl-highlights">'
      '<div class="hl-section">'
      '<div class="hl-divider hl-reveal">Why Hirelyzer</div>'
      '<div class="hl-highlight-grid">' + items + '</div>'
      '</div></div>')

def render_faq():
    faqs = [
        ("Is Hirelyzer completely free?", "Yes &mdash; the core features including ATS scoring, bias detection, and job search are fully free. No credit card required to get started."),
        ("What file formats does Hirelyzer accept?", "PDF is the primary input format. Our parser handles standard, multi-column, and OCR-scanned PDFs. Export to DOCX or PDF is available from the Resume Builder."),
        ("How accurate is the ATS scoring?", "Our scoring engine replicates how real ATS systems parse resumes across six dimensions. We test regularly against major platforms like Greenhouse, Lever, and Workday."),
        ("Is my resume data private?", "Your resume is processed securely and never shared with third parties or recruiters. You control your data entirely."),
        ("How does the AI Interview Coach work?", "Upload your resume and Hirelyzer extracts key experiences to generate tailored questions. You answer in free text and our AI scores you across five competency dimensions in real-time."),
    ]
    items = "".join(
        '<div class="hl-faq-item hl-reveal">'
        '<div class="hl-faq-q">' + q + '<div class="hl-faq-q-icon">+</div></div>'
        '<div class="hl-faq-a">' + a + '</div>'
        '</div>'
        for q, a in faqs
    )
    H('<div class="hl-faq">'
      '<div class="hl-section">'
      '<div style="text-align:center;margin-bottom:0">'
      '<div class="hl-divider hl-reveal">FAQ</div>'
      '<h2 style="font-size:clamp(24px,3vw,40px);font-weight:800;letter-spacing:-1.8px;color:#f5f5f7;margin-bottom:0" class="hl-reveal">Frequently asked questions</h2>'
      '</div>'
      '<div class="hl-faq-list">' + items + '</div>'
      '</div></div>')

def render_cta():
    chk = checklist()
    H('<div class="hl-section">'
      '<div id="contact" class="hl-cta hl-reveal"><div class="hl-cta-glow"></div>'
      '<div class="hl-eyebrow" style="margin:0 auto 28px"><div class="hl-eyebrow-dot"></div>Free to use &middot; No credit card required</div>'
      '<div class="hl-cta-h">Your next job starts<br>with a better resume</div>'
      '<div class="hl-cta-sub">'
      'Join professionals already using Hirelyzer to pass ATS filters, remove bias, and land more interviews.'
      '</div>'
      '<div class="hl-cta-btns">'
      '<a href="' + APP_URL + '" target="_blank" class="hl-btn-p" style="font-size:16px;padding:17px 40px"><svg width="14" height="14" viewBox="0 0 24 24" fill="#fff"><path d="M12 2L13.8 8.2L20 10L13.8 11.8L12 18L10.2 11.8L4 10L10.2 8.2L12 2Z"/></svg>Start for free</a>'
      '<a href="mailto:' + SUPPORT_EMAIL + '" class="hl-btn-g" style="font-size:16px;padding:17px 34px"><svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" stroke="currentColor" stroke-width="1.5" fill="none"/><polyline points="22,6 12,13 2,6" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>Contact us</a>'
      '</div>'
      '<div class="hl-checks">' + chk + '</div>'
      '</div></div>')

def render_contact_section():
    H('<div class="hl-section">'
      '<div class="hl-contact-card hl-reveal">'
      '<div style="width:52px;height:52px;border-radius:16px;background:rgba(10,132,255,0.08);border:1px solid rgba(10,132,255,0.2);display:flex;align-items:center;justify-content:center;margin:0 auto 20px;box-shadow:0 0 24px rgba(10,132,255,0.12)">'
      '<svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" stroke="#0a84ff" stroke-width="1.5" fill="none"/><polyline points="22,6 12,13 2,6" stroke="#0a84ff" stroke-width="1.5" fill="none"/></svg>'
      '</div>'
      '<h3>Get in touch</h3>'
      '<div style="font-size:14px;color:rgba(245,245,247,0.44);line-height:1.72;margin-bottom:28px;text-align:center;">Have questions, feedback, or want to report an issue? We typically respond within 24 hours.</div>'
      '<a href="mailto:' + SUPPORT_EMAIL + '" class="hl-contact-email">'
      '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" stroke="#4db3ff" stroke-width="1.5" fill="none"/><polyline points="22,6 12,13 2,6" stroke="#4db3ff" stroke-width="1.5" fill="none"/></svg>'
      + SUPPORT_EMAIL +
      '</a>'
      '<div class="hl-contact-meta">Support &middot; Feedback &middot; Bug reports &middot; Partnership enquiries</div>'
      '</div></div>')

def render_footer():
    H('<footer style="background:#000">'
      '<div class="hl-footer">'
      '<div class="hl-footer-left">'
      '<div style="display:flex;align-items:center;gap:9px;margin-bottom:2px">'
      '<div style="width:28px;height:28px;border-radius:8px;background:linear-gradient(135deg,#1a6fff,#0044bb);display:flex;align-items:center;justify-content:center;box-shadow:0 4px 12px rgba(10,132,255,0.35)">'
      '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M12 2L2 7l10 5 10-5-10-5z M2 17l10 5 10-5 M2 12l10 5 10-5" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
      '</div>'
      '<span style="font-size:13px;font-weight:800;color:rgba(245,245,247,0.6);letter-spacing:1px">HIRELYZER</span>'
      '</div>'
      '<div class="hl-footer-copy">&copy; 2025 HIRELYZER &middot; Intelligent Career Platform</div>'
      '<div class="hl-footer-tagline">Built for the next generation of job seekers</div>'
      '</div>'
      '<div class="hl-footer-links">'
      '<a href="#">Privacy</a>'
      '<a href="#">Terms</a>'
      '<a href="mailto:' + SUPPORT_EMAIL + '">' + SUPPORT_EMAIL + '</a>'
      '<a href="' + APP_URL + '" target="_blank">Open App &rarr;</a>'
      '</div></div></footer>')

def render_js():
    H('<script>'
      '(function(){'

      # ── Scroll progress bar ──
      'var sp=document.getElementById("sp");'
      'function updateProgress(){if(!sp)return;var p=(window.scrollY/(document.documentElement.scrollHeight-window.innerHeight))*100;sp.style.width=Math.min(p,100)+"%";}'
      'window.addEventListener("scroll",updateProgress,{passive:true});'

      # ── Nav scroll shadow ──
      'var nav=document.getElementById("hl-nav");'
      'window.addEventListener("scroll",function(){if(nav){nav.classList.toggle("scrolled",window.scrollY>20);}},{passive:true});'

      # ── Smooth scroll ──
      'document.querySelectorAll("a[href^=\'#\']").forEach(function(a){'
      'a.addEventListener("click",function(e){'
      'var t=document.querySelector(this.getAttribute("href"));'
      'if(t){e.preventDefault();t.scrollIntoView({behavior:"smooth",block:"start"});}'
      '});});'

      # ── FAQ accordion ──
      'document.querySelectorAll(".hl-faq-q").forEach(function(q){'
      'q.addEventListener("click",function(){'
      'var ans=this.nextElementSibling;'
      'var icon=this.querySelector(".hl-faq-q-icon");'
      'var open=ans.style.display==="block";'
      'document.querySelectorAll(".hl-faq-a").forEach(function(a){a.style.display="none";});'
      'document.querySelectorAll(".hl-faq-q-icon").forEach(function(i){i.textContent="+";});'
      'if(!open){ans.style.display="block";icon.textContent="\u2212";}'
      '});});'
      'document.querySelectorAll(".hl-faq-a").forEach(function(a){a.style.display="none";});'

      # ── Scroll-reveal (IntersectionObserver) ──
      'function initReveal(){'
      'var revealObs=new IntersectionObserver(function(entries){'
      'entries.forEach(function(e){'
      'if(e.isIntersecting){e.target.classList.add("hl-animate");revealObs.unobserve(e.target);}'
      '});},{threshold:0.08,rootMargin:"0px 0px -40px 0px"});'
      'document.querySelectorAll(".hl-reveal").forEach(function(el){revealObs.observe(el);});'
      '}'
      'setTimeout(initReveal,400);'

      # ── Radar draw animation ──
      'var radarObs=new IntersectionObserver(function(entries){'
      'entries.forEach(function(e){'
      'if(e.isIntersecting){'
      'var poly=document.getElementById("hl-radar-poly");'
      'if(poly){poly.classList.add("drawn");}'
      'document.querySelectorAll(".hl-radar-dot").forEach(function(d){d.classList.add("drawn");});'
      'radarObs.unobserve(e.target);'
      '}'
      '});},{threshold:0.3});'
      'var radarEl=document.getElementById("hl-radar-svg");'
      'if(radarEl){radarObs.observe(radarEl);}'

      # ── Animated stat counters ──
      'function animateCount(el,target,suffix){'
      'var start=0;var dur=1800;var startTime=null;'
      'function step(ts){'
      'if(!startTime)startTime=ts;'
      'var progress=Math.min((ts-startTime)/dur,1);'
      'var ease=1-Math.pow(1-progress,3);'
      'var val=Math.round(ease*target);'
      'el.textContent=val+(suffix||"");'
      'if(progress<1)requestAnimationFrame(step);'
      '}'
      'requestAnimationFrame(step);'
      '}'
      'var statObs=new IntersectionObserver(function(entries){'
      'entries.forEach(function(e){'
      'if(e.isIntersecting){'
      'var el=e.target;var count=parseInt(el.getAttribute("data-count"));var suf=el.getAttribute("data-suffix")||"";'
      'if(count){animateCount(el,count,suf);}'
      'statObs.unobserve(el);'
      '}'
      '});},{threshold:0.5});'
      'document.querySelectorAll("[data-count]").forEach(function(el){statObs.observe(el);});'

      # ── Sticky CTA bar ──
      'var stickyCTA=document.getElementById("hl-sticky-cta");'
      'var stickyDismissed=false;'
      'function checkSticky(){'
      'if(stickyDismissed||!stickyCTA)return;'
      'var scrollPct=window.scrollY/(document.documentElement.scrollHeight-window.innerHeight);'
      'stickyCTA.classList.toggle("visible",scrollPct>0.3);'
      '}'
      'window.addEventListener("scroll",checkSticky,{passive:true});'
      'window.dismissSticky=function(){'
      'stickyDismissed=true;'
      'if(stickyCTA){stickyCTA.classList.remove("visible");}'
      '};'

      # ── Toast system ──
      'var toastTimer;'
      'window.showToast=function(msg,color){'
      'var t=document.getElementById("hl-toast");'
      'var m=document.getElementById("hl-toast-msg");'
      'var d=document.getElementById("hl-toast-dot");'
      'if(!t||!m)return;'
      'm.textContent=msg;'
      'if(d&&color){d.style.background=color;d.style.boxShadow="0 0 8px "+color;}'
      't.classList.add("show");'
      'clearTimeout(toastTimer);'
      'toastTimer=setTimeout(function(){t.classList.remove("show");},3000);'
      '};'

      # ── Active nav highlight ──
      'var sections=["hl-hero-anchor","how","analyzer","builder","career","compare","contact"];'
      'var navLinks=document.querySelectorAll("[data-nav]");'
      'var navObs=new IntersectionObserver(function(entries){'
      'entries.forEach(function(e){'
      'if(e.isIntersecting){'
      'var id=e.target.id;'
      'navLinks.forEach(function(a){a.classList.toggle("hl-nav-active",a.getAttribute("data-nav")===id);});'
      'var dots=document.querySelectorAll(".hl-dot-nav");'
      'dots.forEach(function(d){d.classList.toggle("active",d.getAttribute("data-section")===id);});'
      '}'
      '});},{threshold:0.4});'
      'sections.forEach(function(id){'
      'var el=document.getElementById(id);'
      'if(el){navObs.observe(el);}'
      '});'

      # ── Section dot nav click ──
      'document.querySelectorAll(".hl-dot-nav").forEach(function(btn){'
      'btn.addEventListener("click",function(){'
      'var id=this.getAttribute("data-section");'
      'var target=document.getElementById(id);'
      'if(target){target.scrollIntoView({behavior:"smooth",block:"start"});}'
      '});});'

      # ── Mobile drawer ──
      'window.openDrawer=function(){'
      'document.getElementById("hl-drawer").classList.add("open");'
      'document.getElementById("hl-hamburger").classList.add("open");'
      'document.body.style.overflow="hidden";'
      '};'
      'window.closeDrawer=function(){'
      'document.getElementById("hl-drawer").classList.remove("open");'
      'document.getElementById("hl-hamburger").classList.remove("open");'
      'document.body.style.overflow="";'
      '};'

      # ── Cursor spotlight on hero ──
      'var heroEl=document.querySelector(".hl-hero");'
      'var spotlight=document.getElementById("hl-spotlight");'
      'if(heroEl&&spotlight){'
      'heroEl.addEventListener("mousemove",function(e){'
      'var rect=heroEl.getBoundingClientRect();'
      'spotlight.style.left=(e.clientX-rect.left)+"px";'
      'spotlight.style.top=(e.clientY-rect.top)+"px";'
      '},{passive:true});'
      'heroEl.addEventListener("mouseleave",function(){'
      'spotlight.style.left="50%";spotlight.style.top="50%";'
      '});'
      '}'

      # ── Typewriter headline ──
      'var words=["need","engineers","designers","developers","job seekers","everyone"];'
      'var tw=document.getElementById("hl-typewriter");'
      'var twIdx=0;var twDeleting=false;var twCurrent="need";var twTimer;'
      'function typeStep(){'
      'if(!tw)return;'
      'var target=words[twIdx];'
      'if(!twDeleting){'
      'twCurrent=target.slice(0,twCurrent.length+1);'
      'tw.textContent=twCurrent;'
      'if(twCurrent===target){twDeleting=true;twTimer=setTimeout(typeStep,2000);return;}'
      'twTimer=setTimeout(typeStep,90);'
      '}else{'
      'twCurrent=twCurrent.slice(0,-1);'
      'tw.textContent=twCurrent;'
      'if(twCurrent.length===0){twDeleting=false;twIdx=(twIdx+1)%words.length;twTimer=setTimeout(typeStep,300);return;}'
      'twTimer=setTimeout(typeStep,55);'
      '}'
      '}'
      'setTimeout(function(){twDeleting=true;typeStep();},2500);'

      # ── Particle canvas ──
      '(function(){'
      'var canvas=document.getElementById("hl-particles");'
      'if(!canvas)return;'
      'var ctx=canvas.getContext("2d");'
      'var particles=[];'
      'var W,H;'
      'function resize(){'
      'var hero=document.querySelector(".hl-hero");'
      'if(!hero)return;'
      'var r=hero.getBoundingClientRect();'
      'W=canvas.width=r.width;H=canvas.height=r.height;'
      'canvas.style.width=r.width+"px";canvas.style.height=r.height+"px";'
      '}'
      'function Particle(){'
      'this.x=Math.random()*W;'
      'this.y=Math.random()*H;'
      'this.vx=(Math.random()-0.5)*0.3;'
      'this.vy=(Math.random()-0.5)*0.3;'
      'this.r=Math.random()*1.5+0.5;'
      'this.a=Math.random()*0.4+0.05;'
      'this.color=["rgba(10,132,255,","rgba(48,209,88,","rgba(191,90,242,"][Math.floor(Math.random()*3)];'
      '}'
      'Particle.prototype.update=function(){'
      'this.x+=this.vx;this.y+=this.vy;'
      'if(this.x<0)this.x=W;if(this.x>W)this.x=0;'
      'if(this.y<0)this.y=H;if(this.y>H)this.y=0;'
      '};'
      'Particle.prototype.draw=function(){'
      'ctx.beginPath();ctx.arc(this.x,this.y,this.r,0,Math.PI*2);'
      'ctx.fillStyle=this.color+this.a+")";ctx.fill();'
      '};'
      'resize();'
      'for(var i=0;i<80;i++){particles.push(new Particle());}'
      'function loop(){'
      'ctx.clearRect(0,0,W,H);'
      'particles.forEach(function(p){p.update();p.draw();});'
      'requestAnimationFrame(loop);'
      '}'
      'loop();'
      'window.addEventListener("resize",resize,{passive:true});'
      '})();'

      '})();'
      '</script>')

# ─── MAIN ─────────────────────────────────────────────────────────────────────
render_banner()
render_nav()
render_hero()
render_how()
render_story_ats()
render_story_bias()
render_story_builder()
render_story_career()
render_story_interview()
render_testimonials()
render_compare()
render_highlights()
render_faq()
render_cta()
render_contact_section()
render_footer()
render_js()
