# 💖 APP COMPLETA GALAXIA ROSADA 💖

import streamlit as st
import time
import random

st.set_page_config(page_title="💖 Para mi amor 💖", page_icon="💖")

# =========================================================

# 🌌 ESTILO GALAXIA

# =========================================================

st.markdown("""

<style>

.stApp {
    background: linear-gradient(-45deg, #1a0029, #3b0a57, #6a0572, #ff4da6);
    background-size: 400% 400%;
    animation: galaxy 15s ease infinite;
}

@keyframes galaxy {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

h1, h2, h3, p, label {
    color: #ffd6f5 !important;
    font-weight: bold;
}

.stButton > button {
    background: rgba(255, 77, 166, 0.25);
    color: white;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.3);
    padding: 10px 20px;
    font-size: 18px;
    box-shadow: 0 0 15px rgba(255, 77, 166, 0.5);
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.05);
    background: rgba(255, 77, 166, 0.5);
}

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

.float-item:nth-child(1){left:10%;font-size:24px;animation-duration:10s;}
.float-item:nth-child(2){left:25%;font-size:30px;animation-duration:12s;}
.float-item:nth-child(3){left:40%;font-size:22px;animation-duration:9s;}
.float-item:nth-child(4){left:55%;font-size:28px;animation-duration:13s;}
.float-item:nth-child(5){left:70%;font-size:24px;animation-duration:11s;}
.float-item:nth-child(6){left:85%;font-size:20px;animation-duration:10s;}

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

<div class="floating">
    <div class="float-item">💖</div>
    <div class="float-item">⭐</div>
    <div class="float-item">🐢</div>
    <div class="float-item">💖</div>
    <div class="float-item">⭐</div>
    <div class="float-item">🐢</div>
</div>

""", unsafe_allow_html=True)

# =========================================================

# 💖 TÍTULO

# =========================================================

st.title("💖 Hola mi querido 💖")

# =========================================================

# 🎵 MÚSICA

# =========================================================

st.write("🎵 I Wanna Be Yours - Arctic Monkeys 💖")
st.video("[https://www.youtube.com/watch?v=nyuo9-OjNNg](https://www.youtube.com/watch?v=nyuo9-OjNNg)")

# =========================================================

# 🌌 FRASES ROMÁNTICAS

# =========================================================

frases = [
"💖 Eres mi lugar favorito.",
"🐢 Te elegiría en todas las vidas.",
"⭐ Tus ojos son mi galaxia favorita.",
"💖 Mi corazón siempre vuelve a ti.",
"🌌 Contigo todo se siente bonito."
]

st.info(random.choice(frases))

# =========================================================

# 📌 OPCIONES

# =========================================================

opcion = st.selectbox(
"Elige una opción:",
[
"Carta",
"Cuánto te amo",
"Sorpresa ✨",
"Poemas 💖",
"Mascota 🐢",
"Mini juego ⭐"
]
)

# =========================================================

# 💌 CARTA

# =========================================================

if opcion == "Carta":

```
st.subheader("💖 Carta")

carta = """
```

Si existen otras vidas, otras muertes y otros universos, espero encontrarte en cada uno de ellos.
Porque siento que incluso el fin del tiempo sería incapaz de acabar con lo que siento por ti.
Aun cuando mi cuerpo desaparezca y solo queden cenizas de mí, sé que incluso ellas seguirían amándote.
"""

```
efecto = st.empty()
texto = ""

for letra in carta:
    texto += letra
    efecto.markdown(texto)
    time.sleep(0.01)
```

# =========================================================

# 💖 CUÁNTO TE AMO

# =========================================================

if opcion == "Cuánto te amo":

```
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
```

# =========================================================

# ✨ SORPRESA

# =========================================================

if opcion == "Sorpresa ✨":

```
st.write("💖 Buscando al amor de mi vida...")

barra = st.progress(0)

for i in range(100):
    time.sleep(0.02)
    barra.progress(i + 1)

st.success("Encontrado, usted 💖")

st.balloons()
```

# =========================================================

# 💖 POEMAS

# =========================================================

if opcion == "Poemas 💖":

```
poemas = [
    "💖 Tu sonrisa es mi lugar favorito.",
    "🌌 Aunque el mundo cambie, yo te vuelvo a amar.",
    "⭐ En cada vida te volvería a elegir.",
    "🐢 Mi corazón siempre encuentra el camino hacia ti."
]

if "poema_idx" not in st.session_state:
    st.session_state.poema_idx = 0

st.markdown(f"## {poemas[st.session_state.poema_idx]}")

c1, c2 = st.columns(2)

if c1.button("⬅ Anterior"):
    st.session_state.poema_idx = (st.session_state.poema_idx - 1) % len(poemas)
    st.rerun()

if c2.button("Siguiente ➜"):
    st.session_state.poema_idx = (st.session_state.poema_idx + 1) % len(poemas)
    st.rerun()
```

# =========================================================

# 🐢 MASCOTA

# =========================================================

if opcion == "Mascota 🐢":

```
st.subheader("🐢 Tortuguita bebé")

st.markdown("# 🐢")

if "energia" not in st.session_state:
    st.session_state.energia = 50

st.write(f"💖 Energía: {st.session_state.energia}")

if st.button("🍓 Dar comida"):
    st.session_state.energia += 10
    st.success("🐢 La tortuguita está feliz 💖")

if st.button("⭐ Jugar"):
    st.session_state.energia -= 5
    st.success("🐢 La tortuguita jugó contigo 🌌")
```

# =========================================================

# ⭐ MINI JUEGO

# =========================================================

if opcion == "Mini juego ⭐":

```
st.subheader("⭐ Atrapa estrellas")

st.write("Presiona el botón para atrapar estrellas 🌌")

if "score" not in st.session_state:
    st.session_state.score = 0

if st.button("⭐ Atrapar"):

    puntos = random.randint(1, 5)

    st.session_state.score += puntos

    st.success(f"¡Ganaste {puntos} estrellas! ⭐")

st.write(f"🌌 Puntos: {st.session_state.score}")
```
