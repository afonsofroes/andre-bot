import random

import streamlit as st

st.title("André Bot")

MESSAGES = [
    "Eu jogo basket",
    "Tens de fazer mais deathmatches bro",
    "Estes gajos são uma de merda",
    "Estes gajos não jogam um caralho",
    "Odeio este jogo",
    "Gonçalo, baitaste-me bro",
]

if st.button("Carrega aqui"):
    st.header(random.choice(MESSAGES))
