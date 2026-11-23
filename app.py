import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta
import html

# ==========================================
# FIRMAPRO ULTRA AI 3.0
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
    st.markdown(f"""
    <div class="card">
        <div class="card-label">
            {ikona} {html.escape(str(nazwa))}
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
        🚀 Firma<span class="gold">PRO</span>
        <span class="neon"> ULTRA</span>
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
    "📋 Historia"
]

menu = st.selectbox(
    "🧭 Centrum nawigacji",
    opcje
)

pracownicy = st.session_state.pracownicy

# ==========================================
# DASHBOARD
# ==========================================

if menu == "🏠 Dashboard":

    st.header("Centrum dowodzenia")
    st.caption("FirmaPRO Intelligence Dashboard")

    przychody, koszty, bilans = (
        podsumowanie_finansow()
    )

    liczba = len(pracownicy)

    pozostalo = sum(
        p["urlop"]
        for p in pracownicy.values()
    )

    c1, c2 = st.columns(2)

    with c1:
        karta(
            "👥",
            "PRACOWNICY",
            liczba,
            "Aktywny zespół"
        )

        karta(
            "💰",
            "PRZYCHODY",
            pieniadze(przychody),
            "Zarejestrowane wpływy"
        )

    with c2:
        karta(
            "🏖️",
            "DNI URLOPU",
            pozostalo,
            "Pozostałe dni"
        )

        karta(
            "📊",
            "BILANS",
            pieniadze(bilans),
            "Przychody minus wydatki"
        )

    st.subheader("📈 Analiza zespołu")

    if pracownicy:
        df = pd.DataFrame([
            {
                "Pracownik": p["imie"],
                "Dni urlopu": p["urlop"]
            }
            for p in pracownicy.values()
        ])

        st.bar_chart(
            df.set_index("Pracownik"),
            color="#F5C86A"
        )

    st.subheader("⚡ Szybkie informacje")

    a, b = st.columns(2)

    with a:
        st.metric(
            "📅 Zadania",
            len(st.session_state.zadania)
        )

    with b:
        st.metric(
            "🚚 Pojazdy",
            len(st.session_state.pojazdy)
        )

    st.subheader("👥 Twój zespół")

    for p in pracownicy.values():
        st.markdown(f"""
        <div class="employee">
            👤 <b>{html.escape(p['imie'])}</b><br>
            <span style="
                color:#9DB3CF;
                font-size:12px;
            ">
                {html.escape(p['stanowisko'])}
                • {p['urlop']} dni urlopu
            </span>
        </div>
        """, unsafe_allow_html=True)

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
     
