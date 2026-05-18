import streamlit as st
import time
import random

st.set_page_config(page_title="💖 Para mi amor 💖", page_icon="💖")

# ---------------- ESTILO ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
}

p, h1, h2, h3, label {
    color: #ff2e88 !important;
    font-weight: bold;
}

.stButton>button {
    background-color: #ff4da6;
    color: white;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

st.title("💖 Hola mi querido 💖")

# ---------------- MÚSICA (FUNCIONA SIEMPRE) ----------------
st.write("🎵 Música romántica 💖")

st.audio(
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
)

# ---------------- OPCIONES (NO CAMBIADAS) ----------------
opcion = st.selectbox(
    "Elige una opción:",
    ["Carta", "Cuánto te amo", "Sorpresa ✨"]
)

# =========================================================
# 💌 CARTA
# =========================================================
if opcion == "Carta":

    st.subheader("💌 Carta")

    st.markdown("""
    <div style="color:#ff2e88; font-size:18px; line-height:1.8; font-weight:bold;">

    Si existen otras vidas, otras muertes y otros universos, espero encontrarte en cada uno de ellos. Porque siento que incluso el fin del tiempo sería incapaz de acabar con lo que siento por ti. aun cuando mi cuerpo desaparezca y solo queden cenizas de mí, sé que incluso ellas seguirían amándote, porque no creo poder dejar de enamorarme de cada parte de ti, de cada lunar, de cada detalle y de esos ojitos suyos en los que podría perderme durante horas sin sentir que es suficiente, porque no existe universo en el que mi corazón no vuelva a elegirlo a usted, ni versión de mí que no termine enamorándose nuevamente de usted, porque sin importar cuándo, dónde o en qué vida sea, mi corazón siempre va a encontrar el camino de regreso a usted, y te seguro que podría pasar una eternidad admirándolo y aún así sentir que me faltaría tiempo para seguir amándolo…

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# 💖 CUÁNTO TE AMO (ARREGLADO SIN BLOQUEOS)
# =========================================================
if opcion == "Cuánto te amo":

    if "num" not in st.session_state:
        st.session_state.num = 1

    if st.button("💖 Aumentar amor"):
        st.session_state.num += 1

    if st.button("🛑 Reiniciar"):
        st.session_state.num = 1

    st.markdown(f"### 💖 {st.session_state.num} te amo infinito 💖")

# =========================================================
# 💖 SORPRESA (CORAZONES CAYENDO + JUEGOS)
# =========================================================
if opcion == "Sorpresa ✨":

    st.write("💭 Buscando el amor de mi vida...")

    barra = st.progress(0)

    for i in range(100):
        time.sleep(0.02)
        barra.progress(i + 1)

    st.success("💖 Usted 💖")

    # ---------------- CORAZONES CAYENDO ----------------
    st.subheader("💞 Lluvia de corazones")

    placeholder = st.empty()
    hearts = ["💖", "💘", "💝", "💗", "💞", "❤️"]

    for _ in range(20):
        screen = ""
        for _ in range(12):
            screen += (" " * random.randint(0, 50)) + random.choice(hearts) + "\n"

        placeholder.markdown(f"<pre style='font-size:22px'>{screen}</pre>", unsafe_allow_html=True)
        time.sleep(0.15)

    # ---------------- MINI JUEGO 1 ----------------
    st.subheader("🎮 Juego: ¿Cuánto me amas?")

    opcion_juego = st.radio("Elige:", ["Poco", "Mucho", "Infinito 💖"])

    if opcion_juego == "Infinito 💖":
        st.success("💖 Correcto 💖")
    else:
        st.error("💔 Intenta otra vez")

    # ---------------- MINI JUEGO 2 ----------------
    st.subheader("🎮 Juego: Adivina el corazón")

    num = st.number_input("Elige un número (1-5)", 1, 5)

    secreto = 3

    if num == secreto:
        st.success("💖 Ganaste un beso virtual 💖")
    else:
        st.info("💞 Sigue intentando")