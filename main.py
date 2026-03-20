import streamlit as st
import datetime
import random

# ==========================================
# 1. CONFIGURAZIONE MOBILE PREMIUM
# ==========================================
st.set_page_config(page_title="Coach AI 360", page_icon="🤖", layout="centered", initial_sidebar_state="collapsed")

# Inizializzazione Session State
if 'api_key' not in st.session_state: st.session_state.api_key = None
if 'onboarded' not in st.session_state: st.session_state.onboarded = False
if 'page' not in st.session_state: st.session_state.page = 'home'
if 'user_data' not in st.session_state: st.session_state.user_data = {}
if 'health_score' not in st.session_state: st.session_state.health_score = random.randint(70, 95)
if 'peso_attuale' not in st.session_state: st.session_state.peso_attuale = 0.0

# ==========================================
# 2. INIEZIONE CSS AVANZATO (Dark Mode Pura & Animazioni)
# ==========================================
# Dinamico: blocca lo scorrimento solo se siamo nella Home
scroll_css = "overflow: hidden;" if st.session_state.page == 'home' else "overflow: auto; padding-bottom: 120px;"

st.markdown(f"""
    <style>
    /* Forza layout Mobile-First */
    [data-testid="stAppViewContainer"] {{
        max-width: 420px; margin: 0 auto;
        background-color: #000000; /* Nero OLED profondo */
        {scroll_css}
    }}
    .stAppHeader {{ display: none !important; }}
    
    /* Tipografia Pulita (Font di sistema) */
    * {{ font-family: '-apple-system', 'BlinkMacSystemFont', 'SF Pro Text', 'Helvetica Neue', sans-serif !important; color: #FFFFFF !important; }}
    p, span {{ color: #CCCCCC !important; font-size: 14px; }}
    
    /* Nasconde elementi superflui Streamlit */
    footer {{ display: none !important; }}

    /* Stile Input (Dark Premium) */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>div, .stNumberInput>div>div>input {{
        background-color: #1C1C1E !important; border: 1px solid #2C2C2E !important; border-radius: 12px !important; color: white !important;
    }}

    /* BOTTONI E CARD (Effetto aptico morbido) */
    div.stButton > button {{
        background-color: #1C1C1E !important; border: 1px solid #2C2C2E !important; border-radius: 20px !important;
        padding: 15px !important; font-weight: 600 !important; font-size: 16px !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        width: 100% !important; text-align: left !important; display: block !important;
    }}
    div.stButton > button:active {{
        transform: scale(0.95) !important; background-color: #2C2C2E !important;
    }}
    
    /* Card 2x2 Altezza Fissa */
    .card-2x2 div.stButton > button {{ height: 130px !important; align-items: flex-start !important; }}

    /* Freccia Indietro Minimal */
    .back-btn div.stButton > button {{
        background: transparent !important; border: none !important; color: #007AFF !important;
        font-size: 18px !important; padding: 0 !important; width: auto !important; height: auto !important; margin-bottom: 15px;
    }}

    /* FLOATING NAV BAR (Solo schede interne) */
    .nav-bar-floating {{
        position: fixed; bottom: 30px; left: 50%; transform: translateX(-50%); width: 85%; max-width: 360px;
        background: rgba(30, 30, 30, 0.85); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
        display: flex; justify-content: space-around; align-items: center; padding: 15px; border-radius: 40px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.5); z-index: 1000; border: 1px solid rgba(255,255,255,0.1);
    }}
    .nav-item {{ font-size: 24px; text-decoration: none; cursor: pointer; transition: 0.2s; }}
    
    /* FAB COACH (Sempre presente in basso a destra) */
    .fab-coach {{
        position: fixed; bottom: 110px; right: 20px; width: 60px; height: 60px; border-radius: 30px;
        background: linear-gradient(135deg, #007AFF, #00C7FF); box-shadow: 0 8px 25px rgba(0,122,255,0.4);
        display: flex; align-items: center; justify-content: center; z-index: 1001; cursor: pointer; border: none; font-size: 26px;
    }}
    .fab-coach:active {{ transform: scale(0.9); }}
    </style>
""", unsafe_allow_html=True)


# ==========================================
# 3. HELPER FUNCTIONS
# ==========================================
def change_page(new_page):
    st.session_state.page = new_page

def back_button():
    st.markdown('<div class="back-btn">', unsafe_allow_html=True)
    if st.button("← Indietro"): change_page('home')
    st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# FASE 1: INSERIMENTO CHIAVE IA (API KEY)
# ==========================================
if not st.session_state.api_key:
    st.title("🤖 Coach AI 360")
    st.markdown("### Benvenuto! Attiva il tuo Coach.")
    st.write("Per darti consigli reali e leggere le tue schede, il Coach ha bisogno della tua Chiave IA gratuita (Google Gemini).")
    
    st.markdown("""
    **Come ottenerla (30 secondi):**
    1. Clicca il link qui sotto.
    2. Accedi con Google e premi *Create API Key*.
    3. Copia il codice lungo e incollalo qui.
    """)
    st.markdown("[👉 Clicca qui per prendere la tua Chiave Gratis](https://aistudio.google.com/app/apikey)", unsafe_allow_html=True)
    
    key_input = st.text_input("Incolla la tua Chiave (API Key) qui:", type="password")
    
    if st.button("🔐 Attiva il Coach e Salva"):
        if len(key_input) > 10:
            st.session_state.api_key = key_input
            st.success("Chiave validata e salvata su Drive (simulato)!")
            st.rerun()
        else:
            st.error("Inserisci una chiave valida.")

# ==========================================
# FASE 2: ONBOARDING PROFONDO
# ==========================================
elif not st.session_state.onboarded:
    st.title("🎯 Profilazione")
    st.write("Configuriamo il tuo punto di partenza.")
    
    with st.form("onboarding_form"):
        col1, col2 = st.columns(2)
        with col1:
            peso = st.number_input("Peso (kg):", min_value=30.0, max_value=200.0, value=75.0)
        with col2:
            altezza = st.number_input("Altezza (cm):", min_value=100, max_value=230, value=175)
            
        corporatura = st.selectbox("Corporatura:", ["Ectomorfo (Magro, fa fatica a crescere)", "Mesomorfo (Atletico, cresce bene)", "Endomorfo (Robusto, accumula facile)"])
        obiettivo = st.selectbox("Obiettivo Principale:", ["Massa Muscolare", "Definizione", "Ricomposizione Corporea", "Forza"])
        
        st.markdown("---")
        st.write("Caricamento Documenti (Opzionale, puoi farlo dopo)")
        scheda = st.file_uploader("Scheda Allenamento (Foto/PDF)", accept_multiple_files=True)
        dieta = st.file_uploader("Dieta Nutrizionista (Foto/PDF)")
        note = st.text_area("Note o Infortuni:")
        
        if st.form_submit_button("🚀 Inizia la Trasformazione"):
            st.session_state.user_data = {'peso': peso, 'altezza': altezza, 'corp': corporatura, 'obiettivo': obiettivo}
            st.session_state.peso_attuale = peso
            st.session_state.onboarded = True
            st.rerun()

# ==========================================
# FASE 3: APP PRINCIPALE
# ==========================================
else:
    # --- FAB COACH (Sempre visibile) ---
    st.markdown('<button class="fab-coach" onclick="alert(\'Apertura IA in overlay...\')">💬</button>', unsafe_allow_html=True)

    # --- PAGINA HOME (No Scroll) ---
    if st.session_state.page == 'home':
        # Messaggio Motivazionale
        ora = datetime.datetime.now().hour
        saluto = "Buongiorno" if ora < 12 else "Buon pomeriggio" if ora < 18 else "Buonasera"
        st.markdown(f"### {saluto}, Mich! 🦾")
        st.markdown('<div style="background-color: #1C1C1E; padding: 15px; border-radius: 15px; border-left: 3px solid #007AFF; margin-bottom: 20px;"><p style="margin:0;">🤖 <b>Coach:</b> Ottimo lavoro ieri. Hai dormito bene, oggi spingi forte sull\'allenamento!</p></div>', unsafe_allow_html=True)
        
        # Widgets Salute e Macro
        colA, colB = st.columns(2)
        with colA:
            st.markdown('<div style="background-color: #1C1C1E; padding: 15px; border-radius: 15px; border: 1px solid #2C2C2E; height: 110px;">'
                        '<h4 style="margin:0; font-size: 15px;">⌚ Salute</h4>'
                        '<p style="margin:5px 0;">👣 7.240 passi</p>'
                        '<p style="margin:0;">💤 7h 15m</p></div>', unsafe_allow_html=True)
        with colB:
            # Bottone che simula la card cliccabile
            if st.button("🍎 Macro di Oggi\n2500 kcal (Dettagli)"): change_page('macro')

        # Griglia 2x2 (Card Pulite con effetto aptico)
        st.markdown("#### Le tue Aree")
        st.markdown('<div class="card-2x2">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            if st.button("🔥 Allenamento\n\nOggi: Petto/Tricipiti"): change_page('allenamento')
            if st.button("🧬 Lifestyle\n\nPeso: {} kg".format(st.session_state.peso_attuale)): change_page('lifestyle')
        with c2:
            if st.button("🍎 Dieta\n\nPranzo da inserire"): change_page('dieta')
            if st.button("🏢 Ufficio Coach\n\nReport e Analisi"): change_page('ufficio')
        st.markdown('</div>', unsafe_allow_html=True)

    # --- SCHEDE INTERNE (Scorrimento Sbloccato + Tasto Indietro) ---
    
    elif st.session_state.page == 'allenamento':
        back_button()
        st.title("🔥 Allenamento")
        st.write("Qui ci sarà la tua scheda dinamica. Scorri per vedere gli esercizi.")
        for i in range(1, 6):
            st.markdown(f'<div style="background-color: #1C1C1E; padding: 15px; border-radius: 15px; margin-bottom: 10px;"><h3>Esercizio {i}</h3><p>4 serie x 10 ripetizioni</p></div>', unsafe_allow_html=True)

    elif st.session_state.page == 'dieta':
        back_button()
        st.title("🍎 Dieta")
        st.write("Piano alimentare di oggi.")
        st.success("Colazione: Completata")
        st.warning("Pranzo: Da inserire")

    elif st.session_state.page == 'lifestyle':
        back_button()
        st.title("🧬 Lifestyle")
        st.write("Monitoraggio parametri e bilancia.")
        
        # INSERIMENTO MANUALE PESO
        st.markdown("### ⚖️ Bilancia")
        nuovo_peso = st.number_input("Inserisci il tuo peso di oggi (kg):", value=st.session_state.peso_attuale, step=0.1)
        if st.button("💾 Salva Pesata"):
            st.session_state.peso_attuale = nuovo_peso
            st.success("Peso salvato nel database!")
            
        st.markdown("### ⌚ Dati Apple Salute / Fit")
        st.info("Sincronizzazione automatica attiva in background.")

    elif st.session_state.page == 'macro':
        back_button()
        st.title("📊 Dettaglio Macro")
        st.write("Andamento giornaliero in stile Premium.")
        st.progress(0.7, text="Calorie: 1800 / 2500 kcal")
        st.progress(0.8, text="Proteine: 120 / 150 g")
        st.progress(0.4, text="Grassi: 30 / 70 g")
        st.progress(0.6, text="Carboidrati: 180 / 300 g")

    elif st.session_state.page == 'ufficio':
        back_button()
        st.title("🏢 Ufficio Coach")
        st.write("Centro di controllo e report settimanale.")
        st.markdown('<div style="background-color: #1C1C1E; padding: 15px; border-radius: 15px; border-left: 3px solid #007AFF;">'
                    '🤖 <b>Analisi IA:</b> Settimana eccellente. L\'aumento di peso sulla panca conferma che siamo in surplus controllato. Continua così.'
                    '</div>', unsafe_allow_html=True)

    # --- BARRA DI NAVIGAZIONE INFERIORE (Solo se non sei in Home) ---
    if st.session_state.page != 'home':
        st.markdown("""
            <div class="nav-bar-floating">
                <span class="nav-item" onclick="window.parent.postMessage('home', '*');" style="color: #007AFF;">🏠</span>
                <span class="nav-item">🏋️</span>
                <span class="nav-item">🍎</span>
                <span class="nav-item">📊</span>
            </div>
        """, unsafe_allow_html=True)
