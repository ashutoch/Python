#! Pomodoro Timer - Study Break Timer with Alarm

import streamlit as st
import time
import winsound

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Pomodoro Timer", page_icon="🍅", layout="centered")

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;600;700&family=JetBrains+Mono:wght@400;700&display=swap');

/* ── Base ── */
html, body, [data-testid="stAppViewContainer"] {
    background: #0b0f1a !important;
    color: #e8e4d9 !important;
    font-family: 'Space Grotesk', sans-serif;
}
[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stSidebar"] { display: none; }
.block-container { padding: 2rem 1.5rem 4rem !important; max-width: 680px; margin: auto; }

/* ── Title ── */
.title-wrap { text-align: center; margin-bottom: 2.5rem; }
.title-wrap h1 {
    font-size: 2.6rem;
    font-weight: 700;
    letter-spacing: -0.03em;
    background: linear-gradient(135deg, #f5a623 0%, #f97316 50%, #e84393 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
}
.title-wrap p {
    color: #6b7280;
    font-size: 0.9rem;
    margin: 0.4rem 0 0;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

/* ── Input cards ── */
.input-row {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.5rem;
}
.stNumberInput > div > div > input {
    background: #141929 !important;
    border: 1px solid #1e2740 !important;
    border-radius: 12px !important;
    color: #e8e4d9 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 1.1rem !important;
    text-align: center;
    padding: 0.6rem !important;
}
.stNumberInput > div > div > input:focus {
    border-color: #f5a623 !important;
    box-shadow: 0 0 0 2px rgba(245,166,35,0.15) !important;
}
label[data-testid="stWidgetLabel"] p {
    color: #9ca3af !important;
    font-size: 0.78rem !important;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

/* ── Start button ── */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #f5a623, #f97316) !important;
    color: #0b0f1a !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    letter-spacing: 0.05em;
    border: none !important;
    border-radius: 14px !important;
    padding: 0.85rem 2rem !important;
    cursor: pointer;
    transition: transform 0.15s, box-shadow 0.15s;
    margin-top: 0.5rem;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(249,115,22,0.35) !important;
}
.stButton > button:active { transform: translateY(0); }

/* ── Timer ring card ── */
.timer-card {
    background: #141929;
    border: 1px solid #1e2740;
    border-radius: 24px;
    padding: 2rem 1.5rem;
    text-align: center;
    margin: 1.5rem 0;
    position: relative;
    overflow: hidden;
}
.timer-card::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 200px; height: 200px;
    border-radius: 50%;
    opacity: 0.04;
    background: var(--glow, #f5a623);
    filter: blur(40px);
}

/* ── SVG ring ── */
.ring-wrap { display: flex; justify-content: center; margin-bottom: 1rem; }
.ring-wrap svg { filter: drop-shadow(0 0 12px var(--ring-glow, rgba(245,166,35,0.4))); }

/* ── Time display ── */
.time-display {
    font-family: 'JetBrains Mono', monospace;
    font-size: 3.8rem;
    font-weight: 700;
    letter-spacing: -0.02em;
    line-height: 1;
    color: #f0ece0;
}
.phase-label {
    font-size: 0.75rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #6b7280;
    margin-top: 0.4rem;
}

/* ── Cycle dots ── */
.cycle-dots { display: flex; justify-content: center; gap: 0.5rem; margin: 1.2rem 0 0; }
.dot {
    width: 8px; height: 8px; border-radius: 50%;
    background: #1e2740;
    transition: background 0.3s;
}
.dot.done { background: #f5a623; }
.dot.active { background: #f97316; box-shadow: 0 0 6px rgba(249,115,22,0.6); }

/* ── Status banners ── */
.banner {
    border-radius: 12px;
    padding: 0.75rem 1.2rem;
    font-size: 0.88rem;
    font-weight: 600;
    letter-spacing: 0.02em;
    margin: 0.8rem 0;
    text-align: center;
}
.banner-study  { background: rgba(245,166,35,0.1);  color: #f5a623;  border: 1px solid rgba(245,166,35,0.2);  }
.banner-break  { background: rgba(20,184,166,0.1);  color: #2dd4bf;  border: 1px solid rgba(20,184,166,0.2);  }
.banner-done   { background: rgba(168,85,247,0.1);  color: #c084fc;  border: 1px solid rgba(168,85,247,0.2);  }

/* ── Streamlit alert overrides ── */
[data-testid="stAlert"] { display: none !important; }
</style>
""", unsafe_allow_html=True)


# ── Helpers ──────────────────────────────────────────────────────────────────
def beep(frequency=1000, duration=500):
    try:
        winsound.Beep(frequency, duration)
    except:
        pass


def ring_svg(progress: float, color: str, glow: str) -> str:
    """Circular progress ring. progress = 0.0 → 1.0"""
    r, cx, cy, stroke = 80, 100, 100, 10
    circumference = 2 * 3.14159 * r
    dash = circumference * progress
    return f"""
    <svg width="200" height="200" viewBox="0 0 200 200" style="--ring-glow:{glow}">
        <circle cx="{cx}" cy="{cy}" r="{r}"
        fill="none" stroke="#1e2740" stroke-width="{stroke}"/>
        <circle cx="{cx}" cy="{cy}" r="{r}"
        fill="none" stroke="{color}" stroke-width="{stroke}"
        stroke-linecap="round"
        stroke-dasharray="{dash:.1f} {circumference:.1f}"
        transform="rotate(-90 {cx} {cy})"
        style="transition: stroke-dasharray 0.8s ease;"/>
    </svg>"""


def dots_html(total, done, active):
    html = '<div class="cycle-dots">'
    for i in range(1, total + 1):
        if i < active:
            cls = "dot done"
        elif i == active:
            cls = "dot active"
        else:
            cls = "dot"
        html += f'<div class="{cls}"></div>'
    html += '</div>'
    return html


def banner(text, kind="study"):
    st.markdown(f'<div class="banner banner-{kind}">{text}</div>', unsafe_allow_html=True)


def countdown(total_secs, phase, current_cycle, total_cycles):
    is_study = phase == "study"
    color     = "#f5a623" if is_study else "#2dd4bf"
    glow      = "rgba(245,166,35,0.4)" if is_study else "rgba(45,212,191,0.4)"
    label     = "🧠 FOCUS" if is_study else "☕ BREAK"

    ring_ph  = st.empty()
    time_ph  = st.empty()
    dots_ph  = st.empty()

    t = total_secs
    while t >= 0:
        mins, secs = divmod(t, 60)
        progress = 1 - (t / total_secs) if total_secs > 0 else 1

        ring_ph.markdown(f"""
        <div class="timer-card">
            <div class="ring-wrap">{ring_svg(progress, color, glow)}</div>
            <div class="time-display">{mins:02d}:{secs:02d}</div>
            <div class="phase-label">{label} &nbsp;·&nbsp; CYCLE {current_cycle}/{total_cycles}</div>
        </div>""", unsafe_allow_html=True)

        dots_ph.markdown(dots_html(total_cycles, current_cycle - 1, current_cycle),
                        unsafe_allow_html=True)

        if t == 10:
            beep(600, 300)
        if t == 0:
            break

        time.sleep(1)
        t -= 1

    beep(900, 600)
    time.sleep(0.15)
    beep(900, 600)


def run_timer(study_mins, break_mins, cycles):
    for cycle in range(1, cycles + 1):
        banner(f"Cycle {cycle} of {cycles} — time to focus 🎯", "study")
        countdown(study_mins * 60, "study", cycle, cycles)
        banner("Study phase done! Take a breath ☕", "break")

        if cycle < cycles:
            countdown(break_mins * 60, "break", cycle, cycles)
            banner("Break over — back to it 💪", "study")

    st.markdown('<div class="banner banner-done">🎉 All cycles complete — great work!</div>',
                unsafe_allow_html=True)
    st.balloons()
    for f in [800, 1000, 1200]:
        beep(f, 200)
        time.sleep(0.1)


# ── UI ────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="title-wrap">
    <h1>Pomodoro Timer</h1>
    <p>Stay focused · Stay sharp</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    study_time = st.number_input("Study (mins)", min_value=1, step=1, value=25)
with col2:
    break_time = st.number_input("Break (mins)", min_value=0, step=1, value=5)
with col3:
    cycles = st.number_input("Cycles", min_value=1, step=1, value=4)

if st.button("▶  Start Session"):
    run_timer(study_time, break_time, cycles)