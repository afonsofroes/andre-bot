import random

import streamlit as st

st.title("André Bot")

MESSAGES = [
    "Eu jogo basket",
    "Tens de fazer mais deathmatches bro",
]

if st.button("Carrega aqui"):
    st.header(random.choice(MESSAGES))
