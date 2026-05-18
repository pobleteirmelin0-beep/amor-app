import streamlit as st
import time

st.set_page_config(page_title="💖 Para mi amor 💖", page_icon="💖")

# =========================================================
# 🌌 ESTILO GALAXIA ROSADA
# =========================================================
st.markdown("""
<style>

/* =========================================================
🌌 FONDO GALAXIA
========================================================= */

.stApp {
    background: linear-gradient(
        -45deg,
        #120018,
        #2b1055,
        #4b1d6b,
        #ff4da6
    );

    background-size: 400% 400%;
    animation: galaxyBG 15s ease infinite;
    overflow: hidden;
}

/* Movimiento galaxia */

@keyframes galaxyBG {

    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}

/* =========================================================
✨ TEXTOS
========================================================= */

h1, h2, h3, p, label, div {
    color: #ffd6f0 !important;
    font-weight: bold;
    text-shadow: 0 0 10px rgba(255,255,255,0.25);
}

/* =========================================================
💖 BOTONES
========================================================= */

.stButton>button {

    background: rgba(255, 77, 166, 0.25);

    color: white;

    border-radius: 20px;

    border: 1px solid rgba(255,255,255,0.3);

    padding: 12px 25px;

    font-size: 18px;

    backdrop-filter: blur(8px);

    box-shadow:
        0 0 10px rgba(255, 77, 166, 0.5),
        0 0 20px rgba(255, 77, 166, 0.3);

    transition: all 0.3s ease;
}

.stButton>button:hover {

    transform: scale(1.08);

    background: rgba(255, 77, 166, 0.45);

    box-shadow:
        0 0 20px rgba(255, 77, 166, 0.9),
        0 0 40px rgba(255, 77, 166, 0.6);
}

/* =========================================================
💖⭐🐢 FLOTANTES
========================================================= */

.floating {
    position: fixed;

    width: 100%;
    height: 100%;

    top: 0;
    left: 0;

    pointer-events: none;

    z-index: 9999;
}

.float-item {

    position: absolute;

    bottom: -50px;

    animation: floatUp linear infinite;

    opacity: 0.8;
}

/* posiciones */

.float-item:nth-child(1){
    left: 10%;
    font-size: 22px;
    animation-duration: 10s;
}

.float-item:nth-child(2){
    left: 25%;
    font-size: 28px;
    animation-duration: 14s;
}

.float-item:nth-child(3){
    left: 40%;
    font-size: 20px;
    animation-duration: 12s;
}

.float-item:nth-child(4){
    left: 55%;
    font-size: 30px;
    animation-duration: 16s;
}

.float-item:nth-child(5){
    left: 70%;
    font-size: 24px;
    animation-duration: 13s;
}

.float-item:nth-child(6){
    left: 85%;
    font-size: 20px;
    animation-duration: 11s;
}

/* animación */

@keyframes floatUp {

    0% {
        transform: translateY(0) rotate(0deg);
        opacity: 0;
    }

    20% {
        opacity: 1;
    }

    100% {
        transform: translateY(-120vh) rotate(360deg);
        opacity: 0;
    }
}

</style>

<!-- 🌌 ELEMENTOS FLOTANTES -->

<div class="floating">

    <div class="float-item">💖</div>

    <div class="float-item">⭐</div>

    <div class="float-item">🐢</div>

    <div class="float-item">💖</div>

    <div class="float-item">⭐</div>

    <div class="float-item">🐢</div>

</div>

""", unsafe_allow_html=True)

st.title("💖 Hola mi querido 💖")

# =========================================================
# 🎵 MÚSICA
# =========================================================
st.write("🎵 I Wanna Be Yours - Arctic Monkeys 💖")
st.video("https://www.youtube.com/watch?v=nyuo9-OjNNg")

# =========================================================
# 📌 OPCIONES
# =========================================================
opcion = st.selectbox(
    "Elige una opción:",
    ["Carta", "Cuánto te amo", "Sorpresa ✨", "Poemas 💖"]
)

# =========================================================
# 💌 CARTA
# =========================================================
if opcion == "Carta":

    st.subheader("💖 Carta")

    st.write("""
Si existen otras vidas, otras muertes y otros universos, espero encontrarte en cada uno de ellos.
Porque siento que incluso el fin del tiempo sería incapaz de acabar con lo que siento por ti.
Aun cuando mi cuerpo desaparezca y solo queden cenizas de mí, sé que incluso ellas seguirían amándote,
porque no creo poder dejar de enamorarme de cada parte de ti, de cada lunar, de cada detalle y de esos ojitos suyos
en los que podría perderme durante horas sin sentir que es suficiente, porque no existe universo en el que mi corazón
no vuelva a elegirlo a usted, ni versión de mí que no termine enamorándose nuevamente de usted,
porque sin importar cuándo, dónde o en qué vida sea, mi corazón siempre va a encontrar el camino de regreso a usted,
y te aseguro que podría pasar una eternidad admirándolo y aun así sentir que me faltaría tiempo para seguir amándolo…
""")

# =========================================================
# 💖 CUÁNTO TE AMO
# =========================================================
if opcion == "Cuánto te amo":

    if "run" not in st.session_state:
        st.session_state.run = False
        st.session_state.num = 1
        st.session_state.final = False

    col1, col2 = st.columns(2)

    if col1.button("💖 Iniciar"):
        st.session_state.run = True
        st.session_state.final = False

    if col2.button("🛑 Detener"):
        st.session_state.run = False
        st.session_state.final = True

    box = st.empty()

    if st.session_state.run:
        while st.session_state.run:
            box.markdown(f"### 💖 {st.session_state.num} te amo 💖")
            st.session_state.num += 1
            time.sleep(0.05)
            st.rerun()

    if st.session_state.final:
        st.success("Encontrado, usted 💖")
