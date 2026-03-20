import streamlit as st
import random

# ==========================================
# 1. SETUP & SESSION
# ==========================================
st.set_page_config(page_title="Coach AI 360", layout="centered", initial_sidebar_state="collapsed")

if 'page' not in st.session_state: st.session_state.page = 'home'
if 'peso_attuale' not in st.session_state: st.session_state.peso_attuale = 85.0

# ==========================================
# 2. CSS PREMIUM (ZERO BARRE, SOLO PILLOLA)
# ==========================================
# Cambia lo scroll in base alla pagina
scroll_behavior = "hidden" if st.session_state.page == 'home' else "auto"

st.markdown(f"""
    <style>
    /* Reset Totale */
    [data-testid="stAppViewContainer"] {{
        background-color: #000000;
        max-width: 400px; margin: 0 auto;
        overflow: {scroll_behavior};
    }}
    .stAppHeader {{ display: none !important; }}
    footer {{ display: none !important; }}
    [data-testid="stVerticalBlock"] {{ gap: 0rem; }}

    /* Font e Testi */
    * {{ font-family: 'SF Pro Display', '-apple-system', sans-serif !important; color: white !important; }}
    
    /* CARD MINIMALI */
    div.stButton > button {{
        background: #1C1C1E !important;
        border: 1px solid #2C2C2E !important;
        border-radius: 20px !important;
        padding: 20px !important;
        height: 120px !important;
        text-align: left !important;
        transition: transform 0.1s ease;
    }}
    div.stButton > button:active {{ transform: scale(0.96); }}
    
    /* PILLOLA PARLA COL COACH (Style Reference Image 12) */
    .coach-pill {{
        position: fixed;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        width: 80%;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 30px;
        padding: 12px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 9999;
        cursor: pointer;
    }}
    .pill-text {{ color: rgba(255,255,255,0.7) !important; font-size: 15px; }}

    /* FRECCIA INDIETRO */
    .back-arrow {{
        font-size: 24px;
        color: #007AFF !important;
        cursor: pointer;
        margin-bottom: 20px;
        display: inline-block;
    }}

    /* Widget Macro */
    .macro-card {{
        background: #1C1C1E;
        border-radius: 20px;
        padding: 15px;
        border: 1px solid #2C2C2E;
        margin-bottom: 20px;
    }}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. LOGICA NAVIGAZIONE
# ==========================================
def go_to(page):
    st.session_state.page = page
    st.rerun()

# --- PILLOLA FISSA "PARLA COL COACH" ---
st.markdown(f"""
    <div class="coach-pill" onclick="window.parent.postMessage('open_chat', '*')">
        <span class="pill-text">Chiedi al Coach...</span>
        <span>🎙️</span>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 4. PAGINE
# ==========================================

# --- HOME ---
if st.session_state.page == 'home':
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Buonasera, Mich! 🦾")
    
    # BOX IA
    st.markdown("""
        <div style="background: rgba(0, 122, 255, 0.1); border-left: 4px solid #007AFF; padding: 15px; border-radius: 12px; margin-bottom: 25px;">
            <p style="margin:0; font-size: 14px;">🤖 <b>Coach:</b> Ottimo lavoro ieri. Hai dormito bene, oggi spingi forte nell'allenamento!</p>
        </div>
    """, unsafe_allow_html=True)

    # RIGA 1: SALUTE E MACRO
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="macro-card">
                <p style="margin:0; font-size: 12px; opacity: 0.6;">⌚ SALUTE</p>
                <p style="margin:5px 0; font-size: 16px;">👣 7.240 passi</p>
                <p style="margin:0; font-size: 16px;">💤 7h 15m</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        if st.button("🍎 Macro\n2500 kcal\n(Dettagli)"): go_to('macro')

    # LE TUE AREE (GRIGLIA PULITA)
    st.markdown("<p style='opacity:0.6; font-size:13px; margin-top:10px;'>LE TUE AREE</p>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔥 Allenamento\n\nPetto / Tri"): go_to('allenamento')
        if st.button("🧬 Lifestyle\n\nPeso: 85kg"): go_to('lifestyle')
    with c2:
        if st.button("🍎 Dieta\n\nPranzo OK"): go_to('dieta')
        if st.button("🏢 Ufficio\n\nReport"): go_to('ufficio')

# --- PAGINE INTERNE (SBLOCCATE) ---
elif st.session_state.page == 'allenamento':
    if st.markdown('<p class="back-arrow">←</p>', unsafe_allow_html=True): pass
    if st.button("Torna alla Home"): go_to('home') # Bottone temporaneo finché non mappiamo il click sulla freccia
    
    st.title("🔥 Allenamento")
    st.write("Ora puoi scorrere verso il basso per vedere tutta la scheda senza blocchi.")
    for i in range(1, 11):
        st.markdown(f"""
            <div style="background:#1C1C1E; padding:20px; border-radius:15px; margin-bottom:10px; border:1px solid #2C2C2E;">
                <h4>Esercizio {i}</h4>
                <p style="opacity:0.7;">4 Serie x 10 Ripetizioni - Recupero 90"</p>
            </div>
        """, unsafe_allow_html=True)

elif st.session_state.page == 'lifestyle':
    if st.button("← Home"): go_to('home')
    st.title("🧬 Lifestyle")
    st.markdown("### Inserisci Peso")
    peso = st.number_input("Peso di oggi (kg)", value=st.session_state.peso_attuale)
    if st.button("Salva Pesata"):
        st.session_state.peso_attuale = peso
        st.success("Peso aggiornato!")

elif st.session_state.page == 'macro':
    if st.button("← Home"): go_to('home')
    st.title("📊 Macro di Oggi")
    st.progress(0.7, text="Calorie: 1800 / 2500")
    st.progress(0.8, text="Proteine: 120g / 150g")

elif st.session_state.page == 'dieta':
    if st.button("← Home"): go_to('home')
    st.title("🍎 Alimentazione")
    st.info("Carica qui la foto del tuo pasto per l'analisi istantanea.")
    st.file_uploader("Scatta foto al piatto")

elif st.session_state.page == 'ufficio':
    if st.button("← Home"): go_to('home')
    st.title("🏢 Ufficio Coach")
    st.write("Analisi professionale dei tuoi progressi.")
