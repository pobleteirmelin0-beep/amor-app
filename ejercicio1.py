import streamlit as st
import time
import random
from datetime import date

st.set_page_config(page_title="💖 Para mi amor 💖", page_icon="💖")

# 💖 ESTILO + CORAZONES FLOTANTES
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffd1dc, #ffe4ec);
    overflow: hidden;
}

/* letras */
p, h1, h2, h3, label {
    color: white !important;
    font-weight: bold;
}

/* botones */
.stButton>button {
    background-color: #ff6fae;
    color: white;
    border-radius: 15px;
}

/* 💖 CORAZONES FLOTANTES REALES */
.heart {
    position: fixed;
    bottom: -10px;
    font-size: 20px;
    animation: floatUp 6s linear infinite;
    opacity: 0.7;
}

@keyframes floatUp {
    0% {transform: translateY(0) rotate(0deg);}
    100% {transform: translateY(-100vh) rotate(360deg);}
}
</style>
""", unsafe_allow_html=True)

# 💖 CORAZONES EN FONDO (ANIMADOS)
hearts = ["💖","💘","💝","💗","💞","❤️"]

for i in range(15):
    st.markdown(
        f"<div class='heart' style='left:{random.randint(0,100)}vw; animation-delay:{random.random()*5}s'>"
        f"{random.choice(hearts)}</div>",
        unsafe_allow_html=True
    )

# 💖 TITULO
st.title("💖 Bienvenido querido mío 💖")
st.markdown("### El motivo de cada latido es de usted 💖")

# 🎵 CANCIÓN (SOLO UNA)
st.subheader("🎵 Música 💖")
st.video("https://www.youtube.com/watch?v=nyuo9-OjNNg")

# 🎀 MENÚ
opcion = st.selectbox(
    "💖 Elige una opción 💖",
    ["🏠 Inicio", "💌 Carta", "📖 Poemas", "💖 Contador de días", "✨ Sorpresa", "🎮 Juego secreto"]
)

# 🏠 INICIO
if opcion == "🏠 Inicio":
    st.write("<3")

# 💌 CARTA (SIN CAMBIOS)
elif opcion == "💌 Carta":
    st.subheader("💌 Carta de amor")

    st.markdown("""
    <div style="color:white; font-size:18px; line-height:1.8; font-weight:bold;">
    💖 Carta<br><br>
    Si existen otras vidas, otras muertes y otros universos, espero encontrarte en cada uno de ellos. Porque siento que incluso el fin del tiempo sería incapaz de acabar con lo que siento por ti. Aun cuando mi cuerpo desaparezca y solo queden cenizas de mí, sé que incluso ellas seguirían amándote...
    </div>
    """, unsafe_allow_html=True)

# 📖 POEMAS (FORMATO LIMPIO VERTICAL)
elif opcion == "📖 Poemas":
    st.subheader("📖 Poemas")

    poemas = [
"""Tu sonrisa es mi lugar,
en tu mirada quiero habitar.

Te voy a amar sin parar,
y contigo quiero caminar.

No te dejo de imaginar,
lo que siento no se va.

Ni el tiempo lo borrará,
en mi alma siempre estarás.

Hasta el último respirar,
te voy a amar sin parar.""",

"""Si el mundo llega a callar,
tu voz me vuelve a guiar.

Si me pierdo al caminar,
sé que te voy a encontrar.

Porque no dejo de pensar,
que contigo quiero estar.

Y aunque todo pueda cambiar,
yo te vuelvo a amar.

En cada instante al recordar,
siempre vuelvo a tu mirar.""",

"""Te pienso incluso en silencio,
te llevo en cada pensamiento.

Mi refugio en tus brazos,
calma todos mis pasos.

Eres la parte más querida,
de esta alma perdida.

Y en ti volvió mi vida,
suave, dulce y sentida.""",

"""Te pienso sin poder parar,
aunque el tiempo quiera cambiar.

Sin importar lo que pase,
siempre vuelvo a amar.

En cada latido estás,
no te puedo soltar.

Mi alma te vuelve a buscar,
sin dejar de soñar."""
    ]

    if "p" not in st.session_state:
        st.session_state.p = 0

    col1, col2 = st.columns(2)

    if col1.button("⬅️"):
        st.session_state.p = (st.session_state.p - 1) % len(poemas)

    if col2.button("➡️"):
        st.session_state.p = (st.session_state.p + 1) % len(poemas)

    st.markdown(
        f"<pre style='color:white; font-size:18px; white-space:pre-wrap'>{poemas[st.session_state.p]}</pre>",
        unsafe_allow_html=True
    )

# 💖 CONTADOR (NO CAMBIADO)
elif opcion == "💖 Contador de días":
    st.subheader("💖 Nuestro amor en el tiempo")

    inicio = date(2026, 4, 22)
    hoy = date.today()

    dias = (hoy - inicio).days

    st.success(f"💖 Llevamos {dias} días juntos 💖")
    st.write("<3")

# ✨ SORPRESA (NO CAMBIADO)
elif opcion == "✨ Sorpresa":
    st.subheader("💖 Buscando el amor de mi vida...")

    barra = st.progress(0)

    for i in range(101):
        time.sleep(0.02)
        barra.progress(i)

    st.success("💖 Encontrado, usted 💖")
    st.write("<3")

# 🎮 JUEGO (NO CAMBIADO)
elif opcion == "🎮 Juego secreto":
    st.subheader("🎮 Encuentra el corazón secreto 💖")

    if "secreto" not in st.session_state:
        st.session_state.secreto = random.randint(1, 5)

    num = st.number_input("Elige un número del 1 al 5 💖", 1, 5)

    if st.button("Probar 💖"):
        if num == st.session_state.secreto:
            st.success("💖 Ganaste, te amo 💖")
            st.balloons()
            st.session_state.secreto = random.randint(1, 5)
        else:
            st.error("💔 Intenta otra vez")
