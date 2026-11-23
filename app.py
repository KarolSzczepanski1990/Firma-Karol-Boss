import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta
import html

# ==========================================
# FIRMAPRO ULTRA AI 5.0
# ==========================================

st.set_page_config(
    page_title="FirmaPRO ULTRA AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# WYGLĄD FUTURYSTYCZNY
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

html, body, .stApp {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            ellipse at 85% 0%,
            #17345B 0%,
            transparent 42%
        ),
        radial-gradient(
            ellipse at 0% 85%,
            #102B3B 0%,
            transparent 45%
        ),
        #070D19;
    color: #EAF2FF;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1250px;
    padding-top: 1.5rem;
    padding-bottom: 5rem;
}

h1, h2, h3 {
    color: #F8FAFC !important;
    letter-spacing: -0.7px;
}

.hero {
    background: linear-gradient(
        125deg,
        rgba(24,48,79,.95),
        rgba(10,20,38,.95)
    );
    border: 1px solid #315174;
    border-radius: 26px;
    padding: 28px 22px;
    margin-bottom: 22px;
    box-shadow: 0 15px 45px #00000055;
}

.logo {
    font-size: 34px;
    font-weight: 900;
    color: white;
    letter-spacing: -1.5px;
}

.gold {
    color: #F5C86A;
}

.neon {
    color: #5DE1E6;
}

.subtitle {
    color: #A7BEDA;
    font-size: 12px;
    margin-top: 7px;
    letter-spacing: 1.5px;
}

.card {
    background: linear-gradient(
        145deg,
        #192E49,
        #101C30
    );
    border: 1px solid #2E4967;
    border-radius: 21px;
    padding: 19px;
    margin: 7px 0;
    box-shadow: 0 8px 25px #00000025;
}

.card-label {
    color: #A8BDD5;
    font-size: 12px;
    font-weight: 600;
}

.card-number {
    color: #FFFFFF;
    font-size: 31px;
    font-weight: 900;
    margin-top: 9px;
}

.card-footer {
    color: #5DE1E6;
    font-size: 11px;
    margin-top: 7px;
}

.employee {
    background: #14243A;
    border: 1px solid #2B4663;
    padding: 17px;
    border-radius: 16px;
    margin-bottom: 10px;
}

.badge {
    display: inline-block;
    background: #173B43;
    color: #6EE7D2;
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 11px;
    margin-top: 10px;
}

.stButton > button,
[data-testid="stFormSubmitButton"] button {
    border-radius: 12px;
    background: linear-gradient(
        120deg,
        #2165E8,
        #368CF8
    );
    color: white;
    border: 1px solid #438AF5;
    font-weight: 700;
}

.stButton > button:hover,
[data-testid="stFormSubmitButton"] button:hover {
    color: white;
    border-color: #F5C86A;
}

[data-testid="stMetric"] {
    background: #14243A;
    border: 1px solid #2A4563;
    padding: 15px;
    border-radius: 16px;
}

[data-testid="stMetricValue"] {
    color: #F5C86A;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-color: #2A4563;
    border-radius: 17px;
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    border-radius: 11px;
}

[data-testid="stSidebar"] {
    background: #0D192B;
}

hr {
    border-color: #263B55;
}

/* PREMIUM MOBILE */
.stApp { color-scheme: dark; }
.stApp [data-testid="stWidgetLabel"] p, .stApp label, .stApp [data-testid="stMarkdownContainer"] p { color: #eaf2ff; }
.stApp [data-testid="stCaptionContainer"] p { color: #b9cce3; }
.stApp input, .stApp textarea { color: #f5f8ff !important; background: #15263e !important; -webkit-text-fill-color: #f5f8ff; }
.stApp input::placeholder, .stApp textarea::placeholder { -webkit-text-fill-color: #a8bdd5; }
.stApp [data-baseweb="input"], .stApp [data-baseweb="base-input"], .stApp [data-baseweb="select"] > div, .stApp [data-baseweb="textarea"] { background: #15263e !important; color: #f5f8ff !important; border-color: #476483 !important; }
.stApp [data-baseweb="select"] svg, .stApp [data-testid="stNumberInput"] button { color: #eaf2ff !important; background: #15263e; }
[data-baseweb="popover"] [role="listbox"], [data-baseweb="popover"] [role="option"] { background: #15263e !important; color: #f5f8ff !important; }
[data-baseweb="popover"] [role="option"]:hover { background: #29496b !important; }
.stApp [data-testid="stExpander"] details { border-color: #476483; }
.stApp [data-testid="stExpander"] summary { color: #eaf2ff; }
.stApp [data-testid="stMetricLabel"] p { color: #dce8fa; }
.stApp [data-testid="stChatMessage"] { background: #14243a; color: #eaf2ff; }
.stApp [data-testid="stButton"] button { transition: box-shadow .2s, transform .2s; }
.stApp [data-testid="stButton"] button:hover { box-shadow: 0 0 16px #368cf855; }
.stApp [data-testid="stButton"] button:active { transform: scale(.98); }
.st-key-nav button { background: #14243a !important; border: 1px solid #476483 !important; min-height: 46px; font-size: .85rem; }
.st-key-nav button[kind="primary"] { background: #176b80 !important; border-color: #5de1e6 !important; }
.st-key-nav [data-testid="stHorizontalBlock"] { flex-wrap: nowrap !important; gap: .4rem; }
.st-key-nav [data-testid="stColumn"] { min-width: 0 !important; flex: 1 1 0 !important; width: 0 !important; }
.st-key-nav button p { font-size: .8rem; overflow-wrap: anywhere; }
.st-key-nav button { padding: .35rem !important; }
.st-key-statgrid [data-testid="stHorizontalBlock"] { flex-wrap: nowrap !important; gap: .6rem; }
.st-key-statgrid [data-testid="stColumn"] { min-width: 0 !important; flex: 1 1 0 !important; width: 0 !important; }
.st-key-statgrid .card { padding: 12px; min-height: 110px; }
.st-key-statgrid .card-number { font-size: clamp(17px, 4vw, 29px); overflow-wrap: anywhere; }
.st-key-statgrid .card-label { font-size: 10px; }
.stApp [class*="st-key-usun_"] button { background: #8f263d !important; border-color: #f07889 !important; }
.stApp [data-testid="stFormSubmitButton"] button { background: #146b56; border-color: #40b99b; }
.hero { padding: 16px; margin-bottom: 8px; }
.logo { font-size: clamp(22px, 5vw, 32px); }
.block-container { padding-top: 2.8rem; }
@media(max-width: 600px) { h1 { font-size: 1.7rem !important; } h2 { font-size: 1.4rem !important; } h3 { font-size: 1.1rem !important; } .block-container { padding-left: .85rem; padding-right: .85rem; } }


.block-container{max-width:850px;padding-top:3rem;padding-bottom:7rem}
.stApp{background:radial-gradient(ellipse at 90% 0%,#102e42,transparent 42%),#050b13}
.hero{background:linear-gradient(125deg,#102c40aa,#09131e);border:1px solid #31546b;border-radius:24px;padding:18px;box-shadow:inset 0 1px 1px #ffffff22,0 12px 32px #0006}
.logo{font-size:28px;letter-spacing:-1px}.subtitle{letter-spacing:2px;font-size:10px}
.card{background:linear-gradient(145deg,#183b50aa,#0b1725);border:1px solid #42677c;border-radius:18px;box-shadow:inset 0 1px 2px #ffffff30,0 5px 20px #00cfff12;position:relative;overflow:hidden}
.card svg{display:block;width:25px;height:25px;margin-bottom:7px;color:#54d9ff;filter:drop-shadow(0 0 6px #37bfff88)}
.card-number{letter-spacing:-.7px}.card-footer{color:#8cebdc}
.st-key-nav button{min-height:82px!important;background:linear-gradient(145deg,#18384b,#0b1725)!important;border-radius:18px!important;box-shadow:inset 0 1px 1px #ffffff35,0 4px 12px #00bfff15!important;flex-direction:column;gap:6px!important}
.st-key-nav button span[data-testid="stIconMaterial"]{font-size:29px!important;color:#68d9ff!important}
.st-key-nav button[kind="primary"]{background:linear-gradient(145deg,#14556b,#102637)!important;box-shadow:0 0 16px #00cfff44!important}
.st-key-bottomnav{position:sticky;bottom:0;z-index:90;background:#091522ed;border:1px solid #35556a;border-radius:22px;padding:8px;backdrop-filter:blur(18px)}
.st-key-bottomnav [data-testid="stHorizontalBlock"]{flex-wrap:nowrap!important;gap:4px}.st-key-bottomnav [data-testid="stColumn"]{min-width:0!important;flex:1 1 0!important;width:0!important}
.st-key-bottomnav button{background:#122638!important;border:0!important;padding:4px!important;min-height:48px;flex-direction:column}.st-key-bottomnav button p{font-size:10px!important}
.st-key-bottomnav button span[data-testid="stIconMaterial"]{color:#5de1e6;font-size:24px}
.progressring{width:88px;height:88px;border-radius:50%;display:grid;place-items:center;margin:12px auto;background:conic-gradient(#00e5cf var(--progress),#26394b 0)}.progressring b{display:grid;place-items:center;width:70px;height:70px;background:#0c1927;border-radius:50%;color:white;font-size:20px}
</style>
""", unsafe_allow_html=True)

# ==========================================
# DANE APLIKACJI
# ==========================================

if "firma" not in st.session_state:
    st.session_state.firma = {
        "nazwa": "Moja Firma",
        "branza": "Transport i logistyka"
    }

if "pracownicy" not in st.session_state:
    st.session_state.pracownicy = {
        1: {
            "imie": "Kamil",
            "stanowisko": "Monter",
            "urlop": 26
        },
        2: {
            "imie": "Adam",
            "stanowisko": "Kierowca",
            "urlop": 26
        },
        3: {
            "imie": "Tomek",
            "stanowisko": "Magazynier",
            "urlop": 26
        }
    }

if "next_id" not in st.session_state:
    st.session_state.next_id = 4

if "urlopy" not in st.session_state:
    st.session_state.urlopy = []

if "zadania" not in st.session_state:
    st.session_state.zadania = []

if "finanse" not in st.session_state:
    st.session_state.finanse = []

if "magazyn" not in st.session_state:
    st.session_state.magazyn = []

if "pojazdy" not in st.session_state:
    st.session_state.pojazdy = []

if "historia" not in st.session_state:
    st.session_state.historia = []

if "chat" not in st.session_state:
    st.session_state.chat = []

# ==========================================
# FUNKCJE
# ==========================================

def historia(opis):
    czas = datetime.now().strftime("%d.%m.%Y %H:%M")
    st.session_state.historia.append(
        f"{czas} • {opis}"
    )

def karta(ikona, nazwa, wartosc, opis):
    paths = {"👥": '<circle cx="9" cy="7" r="3"/><path d="M3 20v-3a6 6 0 0 1 12 0v3M16 4a3 3 0 0 1 0 6m2 3a5 5 0 0 1 3 5v2"/>', "🏖️": '<path d="M2 12a10 10 0 0 1 20 0H2m10 0v9m-5 0h10"/>', "💰": '<ellipse cx="12" cy="6" rx="8" ry="3"/><path d="M4 6v12c0 4 16 4 16 0V6M4 12c0 4 16 4 16 0"/>', "📊": '<path d="M4 20V12h4v8m2 0V7h4v13m2 0V3h4v17"/>'}
    svg = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">'+paths.get(ikona,paths["📊"])+'</svg>'
    st.markdown(f"""
    <div class="card">
        <div class="card-label">
            {svg} {html.escape(str(nazwa))}
        </div>
        <div class="card-number">
            {html.escape(str(wartosc))}
        </div>
        <div class="card-footer">
            {html.escape(str(opis))}
        </div>
    </div>
    """, unsafe_allow_html=True)

def pieniadze(kwota):
    return f"{kwota:,.2f} zł".replace(
        ",", " "
    )

def podsumowanie_finansow():
    przychody = sum(
        x["kwota"]
        for x in st.session_state.finanse
        if x["typ"] == "Przychód"
    )

    koszty = sum(
        x["kwota"]
        for x in st.session_state.finanse
        if x["typ"] == "Wydatek"
    )

    return przychody, koszty, przychody - koszty

def nazwa_pracownika(ident):
    p = st.session_state.pracownicy.get(ident)
    return p["imie"] if p else "Usunięty pracownik"

# ==========================================
# NAGŁÓWEK
# ==========================================

st.markdown("""
<div class="hero">
    <div class="logo">
        <span style="color:#55d9ff">▥</span> Firma<span class="neon">PRO</span> <span style="font-size:14px;color:#8ddfff">ULTRA 5.0</span>
    </div>
    <div class="subtitle">
        AI BUSINESS OPERATING SYSTEM
    </div>
    <div style="
        margin-top:18px;
        color:#DCE8FA;
        font-size:14px;
    ">
        Twoja firma. Twoje dane. Twoje centrum dowodzenia.
    </div>
    <div class="badge">
        ● SYSTEM ONLINE — DEMO
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# WYBÓR BRANŻY
# ==========================================

branze = [
    "Transport i logistyka",
    "Budownictwo",
    "Handel",
    "Magazyn",
    "Produkcja",
    "Usługi",
    "Gastronomia",
    "IT i technologia",
    "Inna branża"
]

with st.expander("⚙️ Ustawienia firmy"):
    nazwa = st.text_input(
        "Nazwa firmy",
        value=st.session_state.firma["nazwa"]
    )

    branza = st.selectbox(
        "Branża",
        branze,
        index=branze.index(
            st.session_state.firma["branza"]
        )
    )

    if st.button("💾 Zapisz ustawienia"):
        st.session_state.firma = {
            "nazwa": nazwa.strip() or "Moja Firma",
            "branza": branza
        }
        historia("Zmieniono ustawienia firmy")
        st.rerun()

st.caption(
    f"🏢 {st.session_state.firma['nazwa']} "
    f"• {st.session_state.firma['branza']}"
)

# ==========================================
# MENU
# ==========================================

opcje = [
    "🏠 Dashboard",
    "👥 Pracownicy",
    "🏖️ Urlopy",
    "📅 Zadania",
    "💰 Finanse",
    "📦 Magazyn",
    "🚚 Transport",
    "🤖 Centrum AI",
    "📋 Historia",
    "📊 Raporty"
]

if "nav_page" not in st.session_state or st.session_state.nav_page not in opcje:
    st.session_state.nav_page = opcje[0]
ikony = dict(zip(opcje, [":material/home:", ":material/groups:", ":material/beach_access:", ":material/event_available:", ":material/payments:", ":material/inventory_2:", ":material/local_shipping:", ":material/memory:", ":material/history:", ":material/monitoring:"]))
menu = st.session_state.nav_page

if menu != opcje[0]:
    with st.container(key="nav"):
        for start in range(0, len(opcje), 3):
            cols = st.columns(3)
            for col, opcja in zip(cols, opcje[start:start+3]):
                with col:
                    if st.button(opcja.split(" ", 1)[1], icon=ikony[opcja], key="nav_" + opcja, use_container_width=True,
                                 type="primary" if st.session_state.nav_page == opcja else "secondary"):
                        st.session_state.nav_page = opcja
                        st.rerun()

pracownicy = st.session_state.pracownicy

# ==========================================
# DASHBOARD
# ==========================================

if menu == "🏠 Dashboard":

    st.header("Witaj w FirmaPRO")
    st.caption("FirmaPRO Intelligence Dashboard")

    przychody, koszty, bilans = (
        podsumowanie_finansow()
    )

    liczba = len(pracownicy)

    pozostalo = sum(
        p["urlop"]
        for p in pracownicy.values()
    )

    with st.container(key="statgrid"):
        c1, c2 = st.columns(2)
        with c1:
            karta("👥", "PRACOWNICY", liczba, "Aktywny zespół")
            karta("💰", "PRZYCHODY", pieniadze(przychody), "Wpływy")
        with c2:
            karta("🏖️", "DNI URLOPU", pozostalo, "Pozostałe dni")
            karta("📊", "WYDATKI", pieniadze(koszty), "Koszty firmy")

    st.subheader("Wynik finansowy")
    st.metric("Bilans", pieniadze(bilans))
    if st.session_state.finanse:
        saldo = 0
        punkty = [0]
        for wpis in st.session_state.finanse:
            saldo += wpis["kwota"] if wpis["typ"] == "Przychód" else -wpis["kwota"]
            punkty.append(saldo)
        st.area_chart(pd.DataFrame({"Bilans": punkty}), color="#00d9d0")
    else:
        st.caption("Dodaj operacje finansowe, aby zobaczyć wykres.")
    total = len(st.session_state.zadania)
    done = sum(z["status"] == "Wykonane" for z in st.session_state.zadania)
    pct = round(100 * done / total) if total else 0
    st.markdown(f'<div class="card"><div class="card-label">Wykonanie zadań</div><div class="progressring" style="--progress:{pct}%"><b>{pct}%</b></div><div style="text-align:center;color:#b8d5e8">{done} / {total} zadań</div></div>', unsafe_allow_html=True)
    st.subheader("Centrum zarządzania")
    with st.container(key="nav"):
        for start in range(0, len(opcje), 3):
            cols = st.columns(3)
            for col, opcja in zip(cols, opcje[start:start+3]):
                with col:
                    if st.button(opcja.split(" ", 1)[1], icon=ikony[opcja], key="nav_" + opcja, use_container_width=True,
                                 type="primary" if st.session_state.nav_page == opcja else "secondary"):
                        st.session_state.nav_page = opcja
                        st.rerun()
    st.subheader("Szybkie akcje")
    for label, target, icon in [("Dodaj pracownika",opcje[1],":material/person_add:"),("Dodaj produkt",opcje[5],":material/add_box:"),("Nowe zadanie",opcje[3],":material/add_task:")]:
        if st.button(label, icon=icon, key="quick_"+label, use_container_width=True):
            st.session_state.nav_page=target
            st.rerun()

# ==========================================
# PRACOWNICY
# ==========================================

elif menu == "👥 Pracownicy":

    st.header("👥 Zarządzanie zespołem")

    with st.expander("➕ Dodaj pracownika"):

        with st.form("dodaj_pracownika"):

            imie = st.text_input(
                "Imię i nazwisko"
            )

            stanowisko = st.text_input(
                "Stanowisko"
            )

            dni = st.number_input(
                "Dni urlopu",
                min_value=0,
                max_value=365,
                value=26
            )

            dodaj = st.form_submit_button(
                "➕ Dodaj pracownika"
            )

        if dodaj:

            imie = imie.strip()

            if not imie:
                st.error("Podaj imię pracownika.")

            elif any(
                p["imie"].casefold() == imie.casefold()
                for p in pracownicy.values()
            ):
                st.warning(
                    "Taki pracownik już istnieje."
                )

            else:
                ident = st.session_state.next_id

                pracownicy[ident] = {
                    "imie": imie,
                    "stanowisko": stanowisko.strip()
                    or "Pracownik",
                    "urlop": dni
                }

                st.session_state.next_id += 1

                historia(
                    f"Dodano pracownika: {imie}"
                )

                st.rerun()

    st.subheader("Lista pracowników")

    for ident, p in list(pracownicy.items()):

        with st.container(border=True):

            st.markdown(
                f"### 👤 {html.escape(p['imie'])}"
            )

            st.caption(
                f"{p['stanowisko']} "
                f"• {p['urlop']} dni urlopu"
            )

            with st.expander("✏️ Edytuj"):

                with st.form(f"edycja_{ident}"):

                    nowe_imie = st.text_input(
                        "Imię i nazwisko",
                        value=p["imie"]
                    )

                    nowe_stanowisko = st.text_input(
                        "Stanowisko",
                        value=p["stanowisko"]
                    )

                    nowe_dni = st.number_input(
                        "Pozostały urlop",
                        min_value=0,
                        max_value=365,
                        value=int(p["urlop"])
                    )

                    zapisz = st.form_submit_button(
                        "💾 Zapisz zmiany"
                    )

                if zapisz:

                    if not nowe_imie.strip():
                        st.error(
                            "Imię nie może być puste."
                        )
                    else:
                        p["imie"] = nowe_imie.strip()
                        p["stanowisko"] = (
                            nowe_stanowisko.strip()
                        )
                        p["urlop"] = nowe_dni

                        historia(
                            f"Zmieniono dane: {p['imie']}"
                        )

                        st.rerun()

            if st.button(
                "🗑️ Usuń pracownika",
                key=f"usun_{ident}"
            ):
                historia(
                    f"Usunięto: {p['imie']}"
                )

                del pracownicy[ident]

                st.rerun()

# ==========================================
# URLOPY
# ==========================================

elif menu == "🏖️ Urlopy":

    st.header("🏖️ Centrum urlopowe")

    if not pracownicy:
        st.warning(
            "Najpierw dodaj pracownika."
        )

    else:

        with st.form("nowy_urlop"):

            ident = st.selectbox(
                "Pracownik",
                list(pracownicy.keys()),
                format_func=nazwa_pracownika
            )

            poczatek = st.date_input(
                "Początek urlopu",
                value=date.today()
            )

            koniec = st.date_input(
                "Koniec urlopu",
                value=date.today()
            )

            zatwierdz = st.form_submit_button(
                "✅ Przyznaj urlop"
            )

        if zatwierdz:

            if koniec < poczatek:
                st.error(
                    "Koniec nie może być przed początkiem."
                )

            else:
                dni = (
                    koniec - poczatek
                ).days + 1

                if dni > pracownicy[ident]["urlop"]:
                    st.error(
                        "Za mało dostępnych dni urlopu."
                    )

                else:
                    pracownicy[ident]["urlop"] -= dni

                    st.session_state.urlopy.append({
                        "id": ident,
                        "imie": pracownicy[ident]["imie"],
                        "od": str(poczatek),
                        "do": str(koniec),
                        "dni": dni
                    })

                    historia(
                        f"Urlop: {pracownicy[ident]['imie']} "
                        f"— {dni} dni"
                    )

                    st.rerun()

        st.subheader("Pozostałe dni")

        for p in pracownicy.values():
            st.write(
                f"👤 {p['imie']}: "
                f"**{p['urlop']} dni**"
            )

        st.subheader("Historia urlopów")

        if st.session_state.urlopy:

            st.dataframe(
                pd.DataFrame(
                    st.session_state.urlopy
                ).drop(columns=["id"]),
                use_container_width=True,
                hide_index=True
            )

        else:
            st.info(
                "Brak zaplanowanych urlopów."
            )

# ==========================================
# ZADANIA
# ==========================================

elif menu == "📅 Zadania":

    st.header("📅 Centrum zadań")

    with st.form("nowe_zadanie"):

        nazwa = st.text_input(
            "Nazwa zadania"
        )

        termin = st.date_input(
            "Termin",
            value=date.today()
        )

        priorytet = st.selectbox(
            "Priorytet",
            ["Niski", "Normalny", "Wysoki"]
        )

        dodaj = st.form_submit_button(
            "➕ Dodaj zadanie"
        )

    if dodaj:

        if nazwa.strip():

            st.session_state.zadania.append({
                "nazwa": nazwa.strip(),
                "termin": str(termin),
                "priorytet": priorytet,
                "status": "Do wykonania"
            })

            historia(
                f"Dodano zadanie: {nazwa}"
            )

            st.rerun()

        else:
            st.error("Wpisz nazwę zadania.")

    for i, zadanie in enumerate(
        st.session_state.zadania
    ):

        with st.container(border=True):

            st.write(
                f"📌 **{zadanie['nazwa']}**"
            )

            st.caption(
                f"Termin: {zadanie['termin']} "
                f"• Priorytet: {zadanie['priorytet']}"
            )

            st.write(
                f"Status: {zadanie['status']}"
            )

            if zadanie["status"] != "Wykonane":

                if st.button(
                    "✅ Zakończ",
                    key=f"zadanie_{i}"
                ):

                    zadanie["status"] = "Wykonane"

                    historia(
                        f"Zakończono zadanie: "
                        f"{zadanie['nazwa']}"
                    )

                    st.rerun()

# ==========================================
# FINANSE
# ==========================================

elif menu == "💰 Finanse":

    st.header("💰 Centrum finansowe")

    przychody, koszty, bilans = (
        podsumowanie_finansow()
    )

    st.metric(
        "Przychody",
        pieniadze(przychody)
    )

    st.metric(
        "Wydatki",
        pieniadze(koszty)
    )

    st.metric(
        "Bilans",
        pieniadze(bilans)
    )

    with st.form("finanse_form"):

        typ = st.selectbox(
            "Rodzaj operacji",
            ["Przychód", "Wydatek"]
        )

        opis = st.text_input(
            "Opis"
        )

        kwota = st.number_input(
            "Kwota w PLN",
            min_value=0.01,
            value=100.0,
            step=10.0
        )

        dodaj = st.form_submit_button(
            "💾 Zapisz operację"
        )

    if dodaj:

        if not opis.strip():
            st.error("Podaj opis.")

        else:
            st.session_state.finanse.append({
                "typ": typ,
                "opis": opis.strip(),
                "kwota": float(kwota),
                "data": str(date.today())
            })

            historia(
                f"Finanse: {typ} — "
                f"{pieniadze(kwota)}"
            )

            st.rerun()

    if st.session_state.finanse:

        st.subheader("Historia finansowa")

        st.dataframe(
            pd.DataFrame(
                st.session_state.finanse
            ),
            use_container_width=True,
            hide_index=True
        )

# ==========================================
# MAGAZYN
# ==========================================

elif menu == "📦 Magazyn":

    st.header("📦 Inteligentny magazyn")

    with st.form("magazyn_form"):

        produkt = st.text_input(
            "Nazwa produktu"
        )

        ilosc = st.number_input(
            "Ilość",
            min_value=1,
            value=1
        )

        dodaj = st.form_submit_button(
            "➕ Dodaj produkt"
        )

    if dodaj:

        if produkt.strip():

            st.session_state.magazyn.append({
                "produkt": produkt.strip(),
                "ilosc": int(ilosc)
            })

            historia(
                f"Magazyn: dodano {produkt}"
            )

            st.rerun()

        else:
            st.error("Podaj nazwę produktu.")

    if st.session_state.magazyn:

        st.dataframe(
            pd.DataFrame(
                st.session_state.magazyn
            ),
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("Magazyn jest pusty.")

elif menu == "🚚 Transport":
    st.header("🚚 Centrum transportu")
    with st.form("transport_form"):
        pojazd = st.text_input("Nazwa pojazdu")
        rejestracja = st.text_input("Numer rejestracyjny")
        dodaj = st.form_submit_button("➕ Dodaj pojazd")
    if dodaj:
        if pojazd.strip():
            st.session_state.pojazdy.append({"pojazd": pojazd.strip(), "rejestracja": rejestracja.strip()})
            historia(f"Dodano pojazd: {pojazd}")
            st.rerun()
        else:
            st.error("Podaj nazwę pojazdu.")
    if st.session_state.pojazdy:
        st.dataframe(pd.DataFrame(st.session_state.pojazdy), hide_index=True, use_container_width=True)
    else:
        st.info("Brak pojazdów w systemie.")

elif menu == "🤖 Centrum AI":
    st.header("🤖 FirmaPRO Intelligence")
    st.caption("Asystent demonstracyjny — bez połączenia z modelem AI.")
    st.info("Zapytaj o pracowników, urlopy, finanse, zadania lub magazyn.")
    for wiadomosc in st.session_state.chat:
        with st.chat_message(wiadomosc["rola"]):
            st.write(wiadomosc["tekst"])
    pytanie = st.chat_input("Zapytaj FirmaPRO...")
    if pytanie:
        st.session_state.chat.append({"rola": "user", "tekst": pytanie})
        tekst = pytanie.lower()
        if "urlop" in tekst:
            odpowiedz = f"Pozostało łącznie {sum(p['urlop'] for p in pracownicy.values())} dni urlopu."
        elif "pracownik" in tekst:
            odpowiedz = f"W firmie pracuje {len(pracownicy)} osób."
        elif any(x in tekst for x in ["finans", "przych", "koszt", "zarob", "bilans"]):
            przychody, koszty, bilans = podsumowanie_finansow()
            odpowiedz = f"Przychody: {pieniadze(przychody)}. Wydatki: {pieniadze(koszty)}. Bilans: {pieniadze(bilans)}."
        elif "zadani" in tekst:
            odpowiedz = f"Liczba zadań: {len(st.session_state.zadania)}."
        elif "magazyn" in tekst:
            odpowiedz = f"Liczba pozycji magazynowych: {len(st.session_state.magazyn)}."
        else:
            odpowiedz = "To wersja demonstracyjna. Zapytaj o pracowników, urlopy, finanse, zadania lub magazyn."
        st.session_state.chat.append({"rola": "assistant", "tekst": odpowiedz})
        st.rerun()

elif menu == "📋 Historia":
    st.header("📋 Historia systemu")
    if st.session_state.historia:
        for wpis in reversed(st.session_state.historia):
            st.write("📌", wpis)
    else:
        st.info("Nie wykonano jeszcze żadnych operacji.")

elif menu == "📊 Raporty":
    st.header("Raporty")
    for nazwa, dane in [("Pracownicy",list(pracownicy.values())),("Finanse",st.session_state.finanse),("Zadania",st.session_state.zadania),("Magazyn",st.session_state.magazyn)]:
        st.download_button("Pobierz: "+nazwa, pd.DataFrame(dane).to_csv(index=False).encode("utf-8-sig"), file_name=nazwa+".csv", mime="text/csv")

with st.container(key="bottomnav"):
    for col, (label, target, icon) in zip(st.columns(5), [("Start",opcje[0],":material/home:"),("Zespół",opcje[1],":material/groups:"),("Dodaj",opcje[3],":material/add_circle:"),("Finanse",opcje[4],":material/payments:"),("Zadania",opcje[3],":material/event:")]):
        with col:
            if st.button(label, icon=icon, key="bottom_"+label, use_container_width=True):
                st.session_state.nav_page=target
                st.rerun()
st.divider()
st.markdown("""
<div style="text-align:center;color:#8196B2;font-size:12px;padding:15px">
🚀 FirmaPRO ULTRA AI 5.0<br>FUTURE BUSINESS OPERATING SYSTEM<br>
<span style="color:#F5C86A">PREMIUM MOBILE • DEMO</span></div>
""", unsafe_allow_html=True)
