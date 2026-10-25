"""Theme, CSS and small HTML helpers for BlushAI (baby-pink design system)."""
from __future__ import annotations

import html

import streamlit as st

PALETTE = {
    "primary": "#F4B6C2",    # Baby Pink
    "secondary": "#E8A0BF",  # Soft Rose
    "bg": "#FFF7FA",         # Very Light Pink
    "card": "#FFFFFF",
    "accent": "#C8B6FF",     # Lavender
    "text": "#3D2938",       # Deep Plum
    "muted": "#80717D",      # Soft Gray
    "success": "#A8D5BA",
    "error": "#F08080",
}


def esc(value) -> str:
    return html.escape(str(value), quote=True)


def _h(markup: str) -> str:
    """Collapse HTML to one line so Markdown never mistakes it for a code block."""
    return " ".join(line.strip() for line in markup.strip().splitlines() if line.strip())


CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root{
  --primary:#F4B6C2; --secondary:#E8A0BF; --bg:#FFF7FA; --card:#FFFFFF;
  --accent:#C8B6FF; --text:#3D2938; --muted:#80717D;
  --success:#A8D5BA; --error:#F08080;
  --border:#F6D5DE; --radius:18px;
  --shadow:0 6px 24px #F6D5DE;
  --shadow-hover:0 12px 32px rgba(232,160,191,.30);
}

/* ---------- Base ---------- */
.stApp{
  background:
    radial-gradient(1200px 600px at 8% -10%, rgba(244,182,194,.30), transparent 60%),
    radial-gradient(900px 500px at 100% 0%, rgba(200,182,255,.22), transparent 60%),
    var(--bg);
  color:var(--text);
  font-family:'Inter',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  overflow-x:hidden;
}
.stApp button,.stApp input,.stApp textarea{font-family:inherit;}
.stApp h1,.stApp h2,.stApp h3,.stApp h4,.stApp p,.stApp label,.stApp li{color:var(--text);}
header[data-testid="stHeader"]{background:transparent;}
#MainMenu,footer{visibility:hidden;}
.block-container{max-width:920px;padding-top:2.2rem;padding-bottom:4rem;position:relative;z-index:1;}
a{color:#9a6fb0;}
:focus-visible{outline:3px solid var(--accent)!important;outline-offset:2px;}

/* ---------- Animations ---------- */
@keyframes blFadeUp{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
@keyframes blFloat{0%,100%{transform:translateY(0) translateX(0)}50%{transform:translateY(-22px) translateX(8px)}}
@keyframes blPop{0%{opacity:0;transform:scale(.94)}60%{transform:scale(1.02)}100%{opacity:1;transform:scale(1)}}
@keyframes blBounce{0%,80%,100%{transform:translateY(0);opacity:.45}40%{transform:translateY(-5px);opacity:1}}
@keyframes blPulse{0%,100%{box-shadow:0 0 0 0 rgba(232,160,191,.55)}50%{box-shadow:0 0 0 7px rgba(232,160,191,0)}}
.bl-fade{animation:blFadeUp .55s ease both;}
.bl-pop{animation:blPop .45s ease both;}

/* ---------- Decorative background ---------- */
.bl-bg{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden;}
.bl-blob{position:absolute;border-radius:50%;filter:blur(2px);opacity:.55;animation:blFloat 12s ease-in-out infinite;}
.bl-blob.b1{width:220px;height:220px;left:-60px;top:18%;background:radial-gradient(circle at 30% 30%,#fff,var(--primary));}
.bl-blob.b2{width:150px;height:150px;right:6%;top:10%;background:radial-gradient(circle at 30% 30%,#fff,var(--accent));animation-delay:-4s;}
.bl-blob.b3{width:190px;height:190px;right:-50px;bottom:8%;background:radial-gradient(circle at 30% 30%,#fff,var(--secondary));animation-delay:-8s;}
.bl-blob.b4{width:70px;height:70px;left:12%;bottom:12%;background:radial-gradient(circle at 30% 30%,#fff,var(--accent));animation-delay:-2s;}

/* ---------- Cards ---------- */
[class*="st-key-card"],[data-testid="stForm"]{
  background:var(--card);border:1px solid var(--border)!important;border-radius:var(--radius)!important;
  padding:1.4rem 1.5rem!important;box-shadow:var(--shadow);margin-bottom:1.1rem;
  transition:box-shadow .25s ease,transform .25s ease;animation:blFadeUp .5s ease both;
}
[class*="st-key-card"]:hover,[data-testid="stForm"]:hover{box-shadow:var(--shadow-hover);transform:translateY(-2px);}
.bl-section{display:flex;align-items:center;gap:.7rem;margin:0 0 .9rem 0;}
.bl-section .ico{width:38px;height:38px;border-radius:12px;display:grid;place-items:center;font-size:1.15rem;
  background:linear-gradient(135deg,var(--primary),var(--accent));}
.bl-section h3{margin:0;font-size:1.15rem;font-weight:700;}
.bl-section p{margin:0;font-size:.85rem;color:var(--muted);}

/* ---------- Hero / welcome ---------- */
.bl-hero{text-align:center;padding:1.2rem 0 1.6rem;}
.bl-hero h1{font-size:2.3rem;line-height:1.15;font-weight:800;margin:.8rem 0 .3rem;letter-spacing:-.02em;}
.bl-hero h1 span{display:block;font-size:1.15rem;font-weight:600;color:var(--muted);margin-top:.35rem;letter-spacing:0;}
.bl-tagline{font-size:1.1rem;font-weight:500;color:var(--text);margin:.4rem 0 1.4rem;}
.bl-steps{display:grid;grid-template-columns:repeat(3,1fr);gap:.9rem;margin:0 auto 1.4rem;text-align:left;}
.bl-step{background:rgba(255,255,255,.85);border:1px solid var(--border);border-radius:16px;padding:1rem;
  box-shadow:var(--shadow);transition:transform .25s ease,box-shadow .25s ease;}
.bl-step:hover{transform:translateY(-3px);box-shadow:var(--shadow-hover);}
.bl-step b{display:block;margin:.35rem 0 .15rem;font-size:.95rem;}
.bl-step span{font-size:.85rem;color:var(--muted);line-height:1.4;display:block;}
.bl-num{width:28px;height:28px;border-radius:50%;display:grid;place-items:center;font-weight:700;font-size:.85rem;
  background:var(--primary);color:var(--text);}
.bl-form-title{font-weight:700;font-size:1.05rem;margin-bottom:.2rem;}
.bl-form-sub{font-size:.85rem;color:var(--muted);margin-bottom:.6rem;}

/* ---------- Header / pills ---------- */
.bl-header{display:flex;align-items:center;gap:.9rem;}
.bl-header h2{margin:0;font-size:1.5rem;font-weight:800;letter-spacing:-.01em;}
.bl-header p{margin:.1rem 0 0;color:var(--muted);font-size:.95rem;}
.bl-pill{display:inline-flex;align-items:center;gap:.45rem;padding:.3rem .75rem;border-radius:999px;font-size:.8rem;font-weight:600;
  background:rgba(168,213,186,.35);border:1px solid var(--success);color:var(--text);margin-bottom:.4rem;}
.bl-pill i{width:8px;height:8px;border-radius:50%;background:#4d9c6e;display:inline-block;animation:blPulse 2s infinite;}
.bl-chips{display:flex;flex-wrap:wrap;gap:.4rem;margin:.3rem 0;}
.bl-chip{padding:.2rem .65rem;border-radius:999px;background:rgba(200,182,255,.28);border:1px solid var(--accent);
  font-size:.78rem;font-weight:600;}

/* ---------- File card ---------- */
.bl-file{display:flex;align-items:center;gap:.9rem;padding:.8rem 1rem;border-radius:14px;margin-top:.7rem;
  background:var(--bg);border:1px solid var(--border);animation:blPop .4s ease both;}
.bl-file .ico{font-size:1.5rem;}
.bl-file .name{font-weight:600;word-break:break-word;overflow-wrap:anywhere;}
.bl-file .meta{font-size:.82rem;color:var(--muted);}

/* ---------- Info cards ---------- */
.bl-info-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:.8rem;}
.bl-info{background:var(--bg);border:1px solid var(--border);border-radius:14px;padding:.9rem 1rem;
  transition:transform .25s ease,box-shadow .25s ease;animation:blPop .5s ease both;}
.bl-info:hover{transform:translateY(-3px);box-shadow:var(--shadow-hover);}
.bl-info .k{font-size:.74rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);font-weight:600;}
.bl-info .v{font-size:1.1rem;font-weight:700;margin-top:.15rem;word-break:break-word;overflow-wrap:anywhere;}

/* ---------- Notices ---------- */
.bl-notice{display:flex;gap:.7rem;align-items:flex-start;padding:.85rem 1rem;border-radius:14px;margin:.6rem 0;
  border:1px solid var(--border);animation:blPop .4s ease both;line-height:1.45;}
.bl-notice.ok{background:rgba(168,213,186,.32);border-color:var(--success);}
.bl-notice.err{background:rgba(240,128,128,.14);border-color:var(--error);}
.bl-notice.warn{background:rgba(244,182,194,.28);border-color:var(--primary);}
.bl-notice.info{background:rgba(200,182,255,.2);border-color:var(--accent);}
.bl-notice .ico{font-size:1.1rem;}

/* ---------- Stage tracker ---------- */
.bl-stages{list-style:none;margin:.4rem 0 .6rem;padding:0;display:flex;flex-wrap:wrap;gap:.5rem;}
.bl-stage{display:flex;align-items:center;gap:.45rem;padding:.3rem .75rem;border-radius:999px;font-size:.8rem;font-weight:600;
  border:1px solid var(--border);background:var(--card);color:var(--muted);transition:all .3s ease;}
.bl-stage .bl-dot{width:8px;height:8px;border-radius:50%;background:var(--border);}
.bl-stage.active{color:var(--text);border-color:var(--secondary);background:rgba(244,182,194,.3);}
.bl-stage.active .bl-dot{background:var(--secondary);animation:blPulse 1.4s infinite;}
.bl-stage.done{color:var(--text);border-color:var(--success);background:rgba(168,213,186,.28);}
.bl-stage.done .bl-dot{background:#4d9c6e;}

/* ---------- Typing indicator ---------- */
.bl-typing{display:inline-flex;align-items:center;gap:.4rem;padding:.6rem 1rem;border-radius:999px;margin:.4rem 0;
  background:var(--card);border:1px solid var(--border);box-shadow:var(--shadow);font-size:.9rem;color:var(--muted);}
.bl-typing span{width:8px;height:8px;border-radius:50%;background:var(--secondary);display:inline-block;animation:blBounce 1.2s infinite;}
.bl-typing span:nth-child(2){animation-delay:.15s}.bl-typing span:nth-child(3){animation-delay:.3s}

/* ---------- Buttons ---------- */
div.stButton>button,div[data-testid="stFormSubmitButton"]>button{
  border-radius:12px;border:1px solid var(--border);background:var(--card);color:var(--text);font-weight:600;
  padding:.55rem 1.2rem;transition:transform .2s ease,box-shadow .2s ease,background .2s ease;}
div.stButton>button:hover,div[data-testid="stFormSubmitButton"]>button:hover{
  transform:translateY(-2px);box-shadow:var(--shadow-hover);border-color:var(--secondary);color:var(--text);}
div.stButton>button:active,div[data-testid="stFormSubmitButton"]>button:active{transform:translateY(0);}
button[kind="primary"],button[data-testid="stBaseButton-primary"],button[data-testid="stBaseButton-primaryFormSubmit"]{
  background:linear-gradient(135deg,var(--primary),var(--secondary))!important;color:var(--text)!important;
  border:none!important;font-weight:700!important;box-shadow:0 4px 14px rgba(232,160,191,.45);}
button[kind="primary"]:hover,button[data-testid="stBaseButton-primary"]:hover,
button[data-testid="stBaseButton-primaryFormSubmit"]:hover{filter:brightness(1.03);}
button:disabled{opacity:.55;transform:none!important;box-shadow:none!important;}
div[data-testid="stFormSubmitButton"]>button{width:100%;}
.st-key-process_btn button{width:100%;}

/* ---------- Inputs ---------- */
div[data-baseweb="input"],div[data-baseweb="base-input"]{border-radius:12px!important;}
div[data-baseweb="input"]{border:1px solid var(--border)!important;background:var(--card)!important;transition:box-shadow .2s ease,border-color .2s ease;}
div[data-baseweb="input"]:focus-within{border-color:var(--secondary)!important;box-shadow:0 0 0 3px rgba(200,182,255,.45);}
.stApp input{color:var(--text)!important;}
.stApp input::placeholder{color:var(--muted)!important;opacity:1;}

/* ---------- Uploader ---------- */
[data-testid="stFileUploaderDropzone"]{background:var(--bg);border:2px dashed var(--primary);border-radius:16px;transition:all .25s ease;}
[data-testid="stFileUploaderDropzone"]:hover{border-color:var(--secondary);background:#fff;box-shadow:var(--shadow);}

/* ---------- Chat ---------- */
[data-testid="stChatMessage"]{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:1rem 1.1rem;
  box-shadow:var(--shadow);margin-bottom:.7rem;animation:blFadeUp .45s ease both;}
[data-testid="stExpander"]{border:1px solid var(--border)!important;border-radius:12px!important;background:var(--bg);}

/* ---------- Progress ---------- */
[data-testid="stProgress"] div[role="progressbar"]>div{background:linear-gradient(90deg,var(--primary),var(--secondary))!important;}

/* ---------- Sidebar ---------- */
[data-testid="stSidebar"]{background:var(--card);border-right:1px solid var(--border);}
[data-testid="stSidebar"] .block-container,[data-testid="stSidebarContent"]{padding-top:1.2rem;}
.bl-side-title{display:flex;align-items:center;gap:.6rem;font-weight:800;font-size:1.15rem;margin-bottom:.8rem;}
.bl-side-label{font-size:.72rem;text-transform:uppercase;letter-spacing:.07em;color:var(--muted);font-weight:700;margin:1rem 0 .3rem;}
.bl-side-doc{background:var(--bg);border:1px solid var(--border);border-radius:12px;padding:.7rem .8rem;font-size:.85rem;word-break:break-word;}
.bl-side-doc b{display:block;margin-bottom:.15rem;}

/* ---------- Responsive ---------- */
@media (max-width:768px){
  .block-container{padding:1rem .8rem 3rem;}
  .bl-hero h1{font-size:1.7rem;}
  .bl-steps{grid-template-columns:1fr;}
  .bl-header h2{font-size:1.25rem;}
  [class*="st-key-card"],[data-testid="stForm"]{padding:1rem!important;}
}

/* =====================================================================
   Force the light palette (fixes invisible text when the browser or
   Streamlit is in dark mode)
   ===================================================================== */
:root,.stApp{color-scheme:light;}

/* Sidebar text */
[data-testid="stSidebar"],[data-testid="stSidebar"] *{color:var(--text);}
[data-testid="stSidebar"] [data-testid="stCaptionContainer"],
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] *{color:var(--muted);}
[data-testid="stSidebar"] .bl-side-label{color:var(--muted);font-size:.74rem;}
[data-testid="stSidebar"] .bl-chip{color:var(--text);background:rgba(200,182,255,.30);border:1px solid var(--accent);}
[data-testid="stSidebar"] .bl-side-doc{background:var(--bg);color:var(--text);border:1px solid var(--border);}
[data-testid="stSidebar"] .bl-side-doc b{color:var(--text);}
[data-testid="stSidebar"] .bl-side-box{background:var(--bg);border:1px solid var(--border);border-radius:12px;padding:.7rem .9rem;margin:.2rem 0 .4rem;}

/* Captions everywhere */
[data-testid="stCaptionContainer"],[data-testid="stCaptionContainer"] *{color:var(--muted)!important;}

/* Buttons (secondary) */
.stApp button[data-testid="stBaseButton-secondary"],
.stApp button[kind="secondary"],
.stApp button[data-testid="stBaseButton-secondaryFormSubmit"],
.stApp div.stButton>button:not([kind="primary"]):not([data-testid="stBaseButton-primary"]){
  background:#FFFFFF!important;color:var(--text)!important;border:1.5px solid var(--primary)!important;}
.stApp button[data-testid="stBaseButton-secondary"] *,
.stApp button[kind="secondary"] *,
.stApp button[data-testid="stBaseButton-secondaryFormSubmit"] *,
.stApp div.stButton>button:not([kind="primary"]):not([data-testid="stBaseButton-primary"]) *{color:var(--text)!important;}
.stApp button[data-testid="stBaseButton-secondary"]:hover,
.stApp button[kind="secondary"]:hover,
.stApp div.stButton>button:not([kind="primary"]):not([data-testid="stBaseButton-primary"]):hover{
  background:var(--bg)!important;border-color:var(--secondary)!important;}
button[kind="primary"] *,button[data-testid="stBaseButton-primary"] *,button[data-testid="stBaseButton-primaryFormSubmit"] *{color:var(--text)!important;}

/* Text inputs (question box, API key) */
.stApp div[data-baseweb="input"],.stApp div[data-baseweb="base-input"],.stApp div[data-baseweb="textarea"]{background:#FFFFFF!important;}
.stApp div[data-baseweb="input"]{border:1.5px solid var(--primary)!important;}
.stApp input,.stApp textarea{background:transparent!important;color:var(--text)!important;
  -webkit-text-fill-color:var(--text)!important;caret-color:var(--secondary);}
.stApp input::placeholder,.stApp textarea::placeholder{color:var(--muted)!important;-webkit-text-fill-color:var(--muted)!important;opacity:1;}
.stApp input:disabled{opacity:1;-webkit-text-fill-color:var(--muted)!important;cursor:not-allowed;}
.stApp div[data-baseweb="input"]:has(input:disabled){background:var(--bg)!important;border-style:dashed!important;}
.stApp div[data-baseweb="input"] button{background:transparent!important;border:none!important;box-shadow:none!important;}
.stApp div[data-baseweb="input"] button *{color:var(--text)!important;fill:var(--text)!important;}
.stApp [data-testid="stWidgetLabel"],.stApp [data-testid="stWidgetLabel"] *{color:var(--text)!important;font-weight:600;}

/* Select boxes and sliders */
.stApp div[data-baseweb="select"]>div{background:#FFFFFF!important;border:1.5px solid var(--primary)!important;border-radius:12px!important;}
.stApp div[data-baseweb="select"] *{color:var(--text)!important;}
div[data-baseweb="popover"] ul,div[data-baseweb="popover"] [role="listbox"]{background:#FFFFFF!important;}
div[data-baseweb="popover"] li,div[data-baseweb="popover"] li *{color:var(--text)!important;}
div[data-baseweb="popover"] li:hover{background:var(--bg)!important;}
[data-testid="stSlider"] *{color:var(--text);}

/* File uploader */
[data-testid="stFileUploaderDropzone"] *{color:var(--text);}
[data-testid="stFileUploaderDropzone"] small{color:var(--muted)!important;}
[data-testid="stFileUploaderFile"],[data-testid="stFileChip"]{background:var(--bg)!important;
  border:1px solid var(--border)!important;border-radius:12px!important;}
[data-testid="stFileUploaderFile"] *,[data-testid="stFileChip"] *{color:var(--text)!important;}

/* Chat, expanders, spinner, progress labels */
[data-testid="stChatMessage"],[data-testid="stChatMessage"] *{color:var(--text);}
[data-testid="stChatMessageAvatarUser"],[data-testid="stChatMessageAvatarAssistant"]{
  background:linear-gradient(135deg,var(--primary),var(--accent))!important;color:var(--text)!important;}
[data-testid="stExpander"] details,[data-testid="stExpander"] summary{background:var(--bg)!important;}
[data-testid="stExpander"] *{color:var(--text);}
[data-testid="stSpinner"] *,[data-testid="stProgress"] p{color:var(--text)!important;}

/* =====================================================================
   Extra animations
   ===================================================================== */
@keyframes blSlideIn{from{opacity:0;transform:translateX(-14px)}to{opacity:1;transform:none}}
@keyframes blLogoFloat{0%,100%{transform:translateY(0) rotate(0)}50%{transform:translateY(-5px) rotate(-3deg)}}
@keyframes blShine{from{transform:translateX(-140%) skewX(-20deg)}to{transform:translateX(320%) skewX(-20deg)}}
@keyframes blBreathe{0%,100%{border-color:var(--primary);box-shadow:0 0 0 0 rgba(244,182,194,0)}
  50%{border-color:var(--secondary);box-shadow:0 0 0 6px rgba(244,182,194,.20)}}
@keyframes blStripes{from{background-position:0 0,0 0}to{background-position:28px 0,0 0}}
@keyframes blShake{0%,100%{transform:translateX(0)}20%{transform:translateX(-5px)}40%{transform:translateX(5px)}60%{transform:translateX(-3px)}80%{transform:translateX(3px)}}

/* Logos float gently */
.bl-hero svg,.bl-header svg,.bl-side-title svg{animation:blLogoFloat 5s ease-in-out infinite;}

/* Sidebar items slide in one after another */
[data-testid="stSidebar"] [data-testid="stElementContainer"],[data-testid="stSidebar"] .element-container{animation:blSlideIn .5s ease both;}
[data-testid="stSidebar"] [data-testid="stElementContainer"]:nth-child(1){animation-delay:.03s}
[data-testid="stSidebar"] [data-testid="stElementContainer"]:nth-child(2){animation-delay:.08s}
[data-testid="stSidebar"] [data-testid="stElementContainer"]:nth-child(3){animation-delay:.13s}
[data-testid="stSidebar"] [data-testid="stElementContainer"]:nth-child(4){animation-delay:.18s}
[data-testid="stSidebar"] [data-testid="stElementContainer"]:nth-child(5){animation-delay:.23s}
[data-testid="stSidebar"] [data-testid="stElementContainer"]:nth-child(6){animation-delay:.28s}
[data-testid="stSidebar"] [data-testid="stElementContainer"]:nth-child(7){animation-delay:.33s}
[data-testid="stSidebar"] [data-testid="stElementContainer"]:nth-child(n+8){animation-delay:.38s}

/* Staggered entrances */
.bl-step{animation:blFadeUp .6s ease both;}
.bl-step:nth-child(1){animation-delay:.1s}.bl-step:nth-child(2){animation-delay:.25s}.bl-step:nth-child(3){animation-delay:.4s}
.bl-info:nth-child(1){animation-delay:.05s}.bl-info:nth-child(2){animation-delay:.12s}.bl-info:nth-child(3){animation-delay:.19s}
.bl-info:nth-child(4){animation-delay:.26s}.bl-info:nth-child(5){animation-delay:.33s}
.bl-chip{animation:blPop .45s ease both;}
.bl-chip:nth-child(1){animation-delay:.1s}.bl-chip:nth-child(2){animation-delay:.2s}
.bl-chip:nth-child(3){animation-delay:.3s}.bl-chip:nth-child(4){animation-delay:.4s}

/* Upload zone breathes softly; file card lifts; section icons tilt on card hover */
[data-testid="stFileUploaderDropzone"]{animation:blBreathe 3.5s ease-in-out infinite;}
.bl-file{transition:transform .25s ease,box-shadow .25s ease;}
.bl-file:hover{transform:translateY(-2px);box-shadow:var(--shadow-hover);}
.bl-section .ico{transition:transform .3s ease;}
[class*="st-key-card"]:hover .bl-section .ico{transform:rotate(-8deg) scale(1.1);}

/* Primary buttons get a light sweep on hover */
button[kind="primary"],button[data-testid="stBaseButton-primary"],button[data-testid="stBaseButton-primaryFormSubmit"]{
  position:relative;overflow:hidden;}
button[kind="primary"]::after,button[data-testid="stBaseButton-primary"]::after,button[data-testid="stBaseButton-primaryFormSubmit"]::after{
  content:"";position:absolute;top:0;left:0;width:35%;height:100%;pointer-events:none;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.6),transparent);transform:translateX(-140%) skewX(-20deg);}
button[kind="primary"]:hover::after,button[data-testid="stBaseButton-primary"]:hover::after,
button[data-testid="stBaseButton-primaryFormSubmit"]:hover::after{animation:blShine .9s ease;}

/* Animated progress bar and error shake */
[data-testid="stProgress"] div[role="progressbar"]>div{
  background-image:linear-gradient(45deg,rgba(255,255,255,.35) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.35) 50%,rgba(255,255,255,.35) 75%,transparent 75%),
    linear-gradient(90deg,var(--primary),var(--secondary))!important;
  background-size:28px 28px,100% 100%!important;animation:blStripes 1s linear infinite;}
.bl-notice.err{animation:blPop .4s ease both,blShake .5s ease .1s;}

/* ---------- Reduced motion ---------- */
@media (prefers-reduced-motion:reduce){
  *,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important;}
}
"""


def inject_css() -> None:
    st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)


def background() -> None:
    st.markdown(_h("""
        <div class="bl-bg" aria-hidden="true">
          <div class="bl-blob b1"></div><div class="bl-blob b2"></div>
          <div class="bl-blob b3"></div><div class="bl-blob b4"></div>
        </div>"""), unsafe_allow_html=True)


# ----------------------------------------------------------------------------
# HTML snippets
# ----------------------------------------------------------------------------
def logo(size: int = 48, uid: str = "a") -> str:
    return _h(f"""
    <svg width="{size}" height="{size}" viewBox="0 0 48 48" role="img" aria-label="BlushAI logo" xmlns="http://www.w3.org/2000/svg">
      <defs><linearGradient id="blg{uid}" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0" stop-color="#F4B6C2"/><stop offset="1" stop-color="#E8A0BF"/></linearGradient></defs>
      <rect width="48" height="48" rx="14" fill="url(#blg{uid})"/>
      <path d="M15 11h13l7 7v19a2 2 0 0 1-2 2H15a2 2 0 0 1-2-2V13a2 2 0 0 1 2-2z" fill="#fff"/>
      <path d="M28 11v7h7z" fill="#C8B6FF"/>
      <rect x="17" y="24" width="14" height="2.4" rx="1.2" fill="#E8A0BF"/>
      <rect x="17" y="29" width="10" height="2.4" rx="1.2" fill="#F4B6C2"/>
      <path d="M38 5l1.5 3.5L43 10l-3.5 1.5L38 15l-1.5-3.5L33 10l3.5-1.5z" fill="#C8B6FF"/>
    </svg>""")


def welcome_hero() -> str:
    return _h(f"""
    <div class="bl-hero bl-fade">
      {logo(76, "hero")}
      <h1>BlushAI <span>\u2014 Your Intelligent Document Assistant</span></h1>
      <div class="bl-tagline">Upload documents. Ask questions. Discover insights.</div>
      <div class="bl-steps">
        <div class="bl-step"><div class="bl-num">1</div><b>Upload</b><span>Add a PDF, CSV, XML or Word document.</span></div>
        <div class="bl-step"><div class="bl-num">2</div><b>Process</b><span>BlushAI reads it and builds a searchable index.</span></div>
        <div class="bl-step"><div class="bl-num">3</div><b>Ask</b><span>Get answers based only on your document, with sources.</span></div>
      </div>
    </div>""")


def section_title(icon: str, title: str, subtitle: str = "") -> str:
    sub = f"<p>{esc(subtitle)}</p>" if subtitle else ""
    return _h(f'<div class="bl-section"><div class="ico" aria-hidden="true">{icon}</div>'
              f'<div><h3>{esc(title)}</h3>{sub}</div></div>')


def app_header() -> str:
    return _h(f"""
    <div class="bl-header bl-fade">
      {logo(52, "hdr")}
      <div><h2>BlushAI</h2><p>What would you like to discover today?</p></div>
    </div>""")


def status_pill(text: str = "Connected") -> str:
    return f'<div class="bl-pill" role="status"><i></i>{esc(text)}</div>'


def chips(items) -> str:
    return '<div class="bl-chips">' + "".join(f'<span class="bl-chip">{esc(i)}</span>' for i in items) + "</div>"


def file_card(name: str, file_type: str, size: str, valid: bool = True) -> str:
    icon = {"PDF": "\U0001F4D5", "CSV": "\U0001F4CA", "XML": "\U0001F9E9", "DOCX": "\U0001F4DD"}.get(file_type, "\U0001F4C4")
    return _h(f"""
    <div class="bl-file"><div class="ico" aria-hidden="true">{icon}</div>
      <div><div class="name">{esc(name)}</div><div class="meta">{esc(file_type)} \u00b7 {esc(size)}</div></div></div>""")


def info_cards(items: list[tuple[str, str]]) -> str:
    cards = "".join(f'<div class="bl-info"><div class="k">{esc(k)}</div><div class="v">{esc(v)}</div></div>'
                    for k, v in items)
    return f'<div class="bl-info-grid">{cards}</div>'


def notice(kind: str, text: str) -> str:
    """kind: ok | err | warn | info"""
    icon = {"ok": "\u2705", "err": "\u26A0\uFE0F", "warn": "\U0001F4A1", "info": "\u2728"}[kind]
    role = "alert" if kind == "err" else "status"
    return _h(f'<div class="bl-notice {kind}" role="{role}"><span class="ico" aria-hidden="true">{icon}</span>'
              f'<div>{esc(text)}</div></div>')


def stage_tracker(stages: list[str], active: int, finished: bool = False) -> str:
    items = []
    for i, label in enumerate(stages):
        state = "done" if (finished or i < active) else ("active" if i == active else "todo")
        items.append(f'<li class="bl-stage {state}"><span class="bl-dot"></span>{esc(label)}</li>')
    return f'<ul class="bl-stages" aria-label="Processing progress">{"".join(items)}</ul>'


def typing_indicator(text: str = "BlushAI is thinking") -> str:
    return (f'<div class="bl-typing" role="status" aria-live="polite"><span></span><span></span>'
            f'<span></span>&nbsp;{esc(text)}\u2026</div>')