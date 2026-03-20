import streamlit as st
import pandas as pd
import datetime
import random

# ==========================================
# 1. CONFIGURAZIONE MOBILE-FIRST HIGH-END
# ==========================================
st.set_page_config(
    page_title="Coach AI 360",
    page_icon="🤖",
    layout="centered", # Necessario per centraggio mobile
    initial_sidebar_state="collapsed"
)

# Inizializzazione Session State Avanzata
if 'onboarded' not in st.session_state: st.session_state.onboarded = False
if 'page' not in st.session_state: st.session_state.page = 'dashboard'
if 'user_data' not in st.session_state: st.session_state.user_data = {}
if 'gemini_open' not in st.session_state: st.session_state.gemini_open = False
if 'health_score' not in st.session_state: st.session_state.health_score = random.randint(60, 95)
if 'pasti_inseriti' not in st.session_state: st.session_state.pasti_inseriti = {'colazione': False, 'pranzo': False, 'cena': False}

# Dati Storici Simulati per l'Ufficio Coach
if 'pesi_storico' not in st.session_state: 
    st.session_state.pesi_storico = pd.DataFrame({'Data': [datetime.date.today() - datetime.timedelta(days=7)], 'Peso kg': [75.2]})

# ==========================================
# 2. ADVANCED CSS INJECTION (The "Beautiful" Part)
# ==========================================
# Questo CSS forza Streamlit a sembrare un'app nativa Premium (One UI / iOS inspired)
st.markdown("""
    <style>
    /* Reset & Mobile Viewport Constraint (Forza formato telefono su PC) */
    [data-testid="stAppViewContainer"] {
        max-width: 420px;
        margin: 0 auto;
        background-color: #000000; /* Dark Mode di base */
        overflow: hidden; /* Niente scorrimento in home */
    }
    .stAppHeader { display: none !important; }
    .block-container { padding: 15px !important; }

    /* --- PREMIUM DARK MODE & TYPOGRAPHY --- */
    h1, h2, h3, h4, p, span, label { 
        color: #FFFFFF !important; 
        font-family: '-apple-system', 'BlinkMacSystemFont', 'SF Pro Text', 'Helvetica Neue', 'Roboto', sans-serif !important; 
    }
    .stMarkdown p { color: #CCCCCC !important; font-size: 14px; }
    
    /* Input Fields Moderni (Dark) */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>div {
        background-color: #1A1A1A !important;
        border: 1px solid #333333 !important;
        border-radius: 12px !important;
        color: white !important;
    }

    /* --- CARD 2x2 HOME: EFFETTO PRESSIONE MORBIDA (One UI Style) --- */
    /* Modifichiamo il comportamento dei bottoni standard di streamlit per farli sembrare card interattive */
    div.stButton > button {
        width: 100% !important;
        height: 140px !important;
        border-radius: 24px !important;
        border: none !important;
        background: linear-gradient(135deg, #1A1A1A, #111111) !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5) !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important; /* Animazione morbida linear-out */
        display: flex; flex-direction: column; align-items: start; justify-content: start;
        padding: 20px !important;
        color: white !important;
        font-weight: 700 !important; font-size: 18px !important; text-align: left !important;
    }
    /* Effetto 'pressione' premium al tocco */
    div.stButton > button:active {
        transform: scale(0.96) !important; /* Leggera contrazione */
        background: linear-gradient(135deg, #111111, #080808) !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.8) !important;
    }
    /* Sotto-testo grigio dentro la card */
    div.stButton > button span { color: #999999 !important; font-weight: 400 !important; font-size: 12px !important; }

    /* --- INFO CARDS (Salutari & Salute) --- */
    .info-card {
        background-color: #1A1A1A; border-radius: 20px; padding: 15px;
        margin-bottom: 15px; border: 1px solid #2A2A2A;
    }
    
    /* Mini-Grafico Macro Interattivo (Pillole) */
    .macro-container { display: flex; gap: 8px; margin-top: 10px; }
    .macro-pill { flex: 1; height: 6px; border-radius: 3px; background-color: #333; overflow: hidden; }
    .macro-progress { height: 100%; border-radius: 3px; }

    /* --- FLOATING ELEMENTS & ANIMATIONS --- */
    
    /* 1. Tasto Coach Tondo Gradiente Animato (One UI Search/Gemini style) */
    .fab-coach {
        position: fixed; bottom: 100px; right: 20px;
        width: 65px; height: 65px; border-radius: 50%;
        background: linear-gradient(135deg, #007AFF, #00C7FF, #007AFF);
        background-size: 200% 200%;
        animation: geminiGradient 4s ease infinite;
        box-shadow: 0 8px 25px rgba(0,122,255,0.5);
        display: flex; align-items: center; justify-content: center;
        z-index: 1001; cursor: pointer; border: none;
        transition: transform 0.2s;
    }
    .fab-coach:active { transform: scale(0.9); }
    
    /* 2. Floating Navigation Bar (Pillola sospesa iOS/Pixel Style) */
    .nav-bar-floating {
        position: fixed; bottom: 25px; left: 50%; transform: translateX(-50%);
        width: 90%; max-width: 380px;
        background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(15px); /* Trasparenza blur */
        display: flex; justify-content: space-around; align-items: center;
        padding: 18px; border-radius: 35px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.3); z-index: 1000;
        border: 1px solid rgba(255,255,255,0.2);
    }
    .nav-item { font-size: 26px; color: #666 !important; cursor: pointer; transition: 0.2s; }
    .nav-item:hover { color: #007AFF !important; transform: translateY(-3px); }
    .nav-item.active { color: #007AFF !important; }

    /* --- ANIMAZIONI --- */
    @keyframes geminiGradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes geminiOverlayIn {
        from { opacity: 0; transform: translateY(100px) scale(0.8); }
        to { opacity: 1; transform: translateY(0) scale(1); }
    }
    
    /* Overlay Chat Coach (Gemini Animation) */
    .gemini-overlay {
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0,0,0,0.85); z-index: 2000;
        display: flex; flex-direction: column; padding: 20px;
        animation: geminiOverlayIn 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(10px);
    }

    /* Container per layout fisso no-scroll */
    .fixed-viewport {
        height: 100vh; display: flex; flex-direction: column;
        justify-content: start; padding-bottom: 180px; /* Padding per floating elements */
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. HELPER FUNCTIONS (Logica IA)
# ==========================================

def get_dynamic_greeting():
    """Genera header motivazionale basato sull'ora e lo stato"""
    hour = datetime.datetime.now().hour
    score = st.session_state.health_score
    
    if hour < 12: greet = "Buongiorno, Mich! ☀️"
    elif hour < 18: greet = "Buon pomeriggio, Mich! 🦾"
    else: greet = "Buonasera, Mich! 🌕"
    
    # Logica Tirata d'orecchio / Congratulazioni
    if score > 85:
        msg = "Oggi sei una macchina! Tutti i parametri sono eccellenti. Continua così!"
    elif score < 70:
        msg = "Tirata d'orecchio! 🤨 Oggi ti vedo stanco e l'idratazione è bassa. Recuperiamo!"
    else:
        msg = "Situazione stabile. Ottimo l'allenamento di ieri, oggi focalizzati sull'alimentazione."
        
    return greet, msg

def get_dynamic_diet_status():
    """Ritorna lo stato dinamico della card alimentazione basato sull'ora"""
    hour = datetime.datetime.now().hour
    pasti = st.session_state.pasti_inseriti
    
    if hour < 10:
        if pasti['colazione']: return "Colazione registrata ✅", "#4CD964"
        return "⏰ Inserisci Colazione", "#FFCC00"
    elif hour < 15:
        if pasti['pranzo']: return "Pranzo registrato ✅", "#4CD964"
        return "⏰ Aggiungi Pranzo", "#FFCC00"
    else:
        if pasti['cena']: return "Cena registrata ✅", "#4CD964"
        return "⏰ Decidiamo la Cena?", "#FFCC00"

def get_lifestyle_color():
    """Ritorna un colore tenue (glow) basato sullo health score"""
    score = st.session_state.health_score
    if score > 85: return "rgba(76, 217, 100, 0.15)" # Verde tenue
    if score > 70: return "rgba(255, 204, 0, 0.1)"  # Giallo tenue
    return "rgba(255, 59, 48, 0.1)" # Rosso tenue

# ==========================================
# 4. GESTIONE NAVIGAZIONE & PAGINE
# ==========================================

# Container principale fisso
app_container = st.container()

# --- A. DETAILED ONBOARDING (Questionario Deep Dive) ---
if not st.session_state.onboarded:
    with app_container:
        st.title("🤖 Ciao Michelantonio!")
        st.subheader("Configuriamo il tuo Coach IA 360")
        st.write("Crea il tuo profilo perfetto in 3 step. Più dettagli fornisci, più sarò preciso.")
        
        with st.form("deep_onboarding"):
            # Step 1: Obiettivi & Frequenza
            st.markdown("#### 🎯 Step 1: Obiettivi")
            obiettivo = st.selectbox("Cosa vogliamo ottenere?", ["Ricomposizione Corporea", "Massa Muscolare", "Definizione Estrema", "Forza"])
            infortuni = st.text_area("Hai infortuni, fastidi o allergie alimentari? (es. spalla dx, celiachia)", height=70)
            frequenza = st.selectbox("Quanto spesso ti alleni?", ["3 volte (Lun-Mer-Ven)", "4 volte", "5 volte", "Creiamo noi un piano?"])
            
            # Step 2: Alimentazione (Upload + Note Cena)
            st.markdown("---")
            st.markdown("#### 🍎 Step 2: Alimentazione")
            dieta_file = st.file_uploader("Carica Dieta Nutrizionista (PDF/Foto)", type=['png', 'jpg', 'pdf'])
            dieta_note = st.text_area("Note Alimentazione (es. 'Cena non inclusa, la decidiamo ogni giorno')", height=70, placeholder="Non hai una dieta? Scrivi qui come mangi.")
            
            # Step 3: Allenamento (Multi-file + Note Giorni)
            st.markdown("---")
            st.markdown("#### 🔥 Step 3: Allenamento")
            scheda_file = st.file_uploader("Carica Foto Scheda (Multi-file)", accept_multiple_files=True, type=['png', 'jpg', 'pdf'])
            scheda_note = st.text_area("Note Allenamento (es. 'Mi alleno i giorni dispari, oggi Petto')", height=70, placeholder="Non hai una scheda? Scrivi qui cosa vuoi fare.")
            
            submit = st.form_submit_button("🚀 Avvia il mio Coach AI Premium", use_container_width=True)
            if submit:
                # Salvataggio Dati (In produzione andrebbero su DB)
                st.session_state.user_data = {
                    'obiettivo': obiettivo, 'infortuni': infortuni, 'frequenza': frequenza,
                    'dieta_file': dieta_file, 'dieta_note': dieta_note,
                    'scheda_file': scheda_file, 'scheda_note': scheda_note
                }
                st.session_state.onboarded = True
                st.rerun()

# --- B. APP REALE (Dashboard & Sezioni) ---
else:
    # 1. FLOATING ELEMENTS (Sempre visibili sopra il contenuto)
    # Tasto Coach Gemini (con logica click)
    st.markdown('<button class="fab-coach" onclick="alert(\'Apertura Overlay Gemini...\')">💬</button>', unsafe_allow_html=True)
    # Floating Nav Bar (iOS Style)
    active_dash = "active" if st.session_state.page == 'dashboard' else ""
    st.markdown(f"""
        <div class="nav-bar-floating">
            <span class="nav-item {active_dash}">🏠</span>
            <span class="nav-item">🏋️‍♂️</span>
            <span class="nav-item">🍎</span>
            <span class="nav-item">📈</span>
            <span class="nav-item">🏢</span>
        </div>
        """, unsafe_allow_html=True)

    # 2. CHAT OVERLAY (Simulazione Gemini)
    if st.session_state.gemini_open:
        st.markdown('<div class="gemini-overlay">', unsafe_allow_html=True)
        st.subheader("🤖 Coach IA (Gemini)")
        if st.button("❌ Chiudi", use_container_width=True):
            st.session_state.gemini_open = False
            st.rerun()
        st.write("Sto ascoltando... Prova a mandare un audio:")
        st.audio_input("Messaggio Vocale al Coach")
        st.chat_input("Scrivi qui...")
        st.markdown('</div>', unsafe_allow_html=True)

    # 3. PAGINE CONTENT
    with app_container:
        st.markdown('<div class="fixed-viewport">', unsafe_allow_html=True)

        # ----------------------------------
        # --- PAGINA: DASHBOARD (Home) ---
        # ----------------------------------
        if st.session_state.page == 'dashboard':
            # Header Motivazionale Dinamico
            greet, msg_coach = get_dynamic_greeting()
            st.markdown(f"### {greet}")
            st.markdown(f"""
                <div style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 15px; border-left: 3px solid #007AFF; margin-bottom: 15px;">
                    🤖 <b>Coach AI:</b> <span style="font-weight: 300; font-size:14px;">{msg_coach}</span>
                </div>
            """, unsafe_allow_html=True)
            
            # Notifica Pesata Settimanale (Simulata)
            if datetime.datetime.now().weekday() == 5: # Sabato
                st.warning("⚖️ Notifica: Pesata settimanale del Sabato mattina alle 8:00 inserita.")

            # Row 1: Widget Salute & Macro (Simulati Apple Health/Fit)
            col_health, col_macro = st.columns([1, 1.2])
            with col_health:
                st.markdown(f"""
                    <div class="info-card" style="height: 125px;">
                        <h4 style="margin:0; font-size: 16px;">⌚ Salute</h4>
                        <p style="margin:5px 0;">👣 <b>7.240</b> passi</p>
                        <p style="margin:0;">💤 <b>7h 15m</b> (Buono)</p>
                    </div>
                """, unsafe_allow_html=True)
            
            with col_macro:
                # Cliccando la card macro si va al dettaglio alimentazione
                if st.button("🍎 Macro di Oggi", help="Vedi Dettaglio", use_container_width=True):
                    st.toast("Apertura Dettaglio Alimentazione...")
                st.markdown("""
                    <div class="macro-container" style="margin-top: -10px; margin-bottom: 15px; padding: 0 10px;">
                        <div class="macro-pill"><div class="macro-progress" style="width: 22%; background:#007AFF;"></div></div>
                        <div class="macro-pill"><div class="macro-progress" style="width: 30%; background:#FF3B30;"></div></div>
                        <div class="macro-pill"><div class="macro-progress" style="width: 15%; background:#4CD964;"></div></div>
                    </div>
                """, unsafe_allow_html=True)

            # Row 2: LE 4 CARD 2x2 (PREMIUM INTERACTIVE)
            st.markdown("#### Le tue Aree")
            c1, c2 = st.columns(2)
            
            # Card 🔥 ALLENAMENTO (Dinamica su Frequenza)
            with c1:
                if st.button(f"🔥\nAllenamento\n<span>Oggi: Petto/Tricipiti ({st.session_state.user_data.get('frequenza', '')})</span>", use_container_width=True):
                    st.session_state.page = 'allenamento'; st.rerun()
            
            # Card 🍎 DIETA (Dinamica su Ora)
            diet_status, diet_color = get_dynamic_diet_status()
            with c2:
                if st.button(f"🍎\nDieta\n<span style='color:{diet_color} !important; font-weight:700;'>{diet_status}</span>", use_container_width=True):
                    st.session_state.page = 'dieta'; st.rerun()
            
            c3, c4 = st.columns(2)
            
            # Card 🧬 LIFESTYLE (Dinamica su Health Score + Glow)
            ls_glow = get_lifestyle_color()
            with c3:
                # Iniettiamo CSS specifico per il glow di questa card
                st.markdown(f"<style>div.stButton > button:contains('Lifestyle') {{ background: linear-gradient(135deg, {ls_glow}, #111) !important; border: 1px solid {ls_glow.replace('0.1', '0.3')} !important; }}</style>", unsafe_allow_html=True)
                if st.button(f"🧬\nLifestyle\n<span>Smart Scale: {st.session_state.pesi_storico.iloc[-1]['Peso kg']}kg (Score: {st.session_state.health_score})</span>", use_container_width=True):
                    st.session_state.page = 'lifestyle'; st.rerun()
            
            # Card 🏢 UFFICIO COACH
            with c4:
                if st.button(f"🏢\nUfficio Coach\n<span>Analisi & Suggerimenti settimanali</span>", use_container_width=True):
                    st.session_state.page = 'ufficio'; st.rerun()

        # ----------------------------------
        # --- ALTRE PAGINE (Temporary Placeholder) ---
        # ----------------------------------
        else:
            if st.button("⬅️ Torna alla Home", use_container_width=True):
                st.session_state.page = 'dashboard'; st.rerun()
            st.title(f"Sezione {st.session_state.page.upper()}")
            st.write("Qui caricheremo le funzionalità dettagliate (es. conta calorie dettagliato, storico pesi smart scale, esercizi, ecc.) nelle prossime fasi.")

        st.markdown('</div>', unsafe_allow_html=True) # Chiusura viewport
