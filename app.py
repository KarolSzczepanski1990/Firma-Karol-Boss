import streamlit as st

st.set_page_config(
    page_title="FirmaPRO",
    page_icon="🏢",
    layout="centered"
)

st.title("🏢 FirmaPRO")
st.success("Witaj w aplikacji FirmaPRO! 😎")

if "pracownicy" not in st.session_state:
    st.session_state.pracownicy = [
        "Kamil", "Adam", "Tomek"
    ]

st.subheader("📊 Panel główny")
st.metric("Liczba pracowników",
          len(st.session_state.pracownicy))

st.subheader("👥 Pracownicy")

for osoba in st.session_state.pracownicy:
    st.write("👤", osoba)

nowy = st.text_input("Imię nowego pracownika")

if st.button("➕ Dodaj pracownika"):
    if nowy.strip():
        st.session_state.pracownicy.append(nowy.strip())
        st.rerun()
