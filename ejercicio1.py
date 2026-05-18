import streamlit as st
import time
import random
from datetime import date

st.set_page_config(page_title="💖 Para mi amor 💖", page_icon="💖")

# 🎀 ESTILO
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffd1dc, #ffe4ec);
}

p, h1, h2, h3, label {
    color: white !important;
    font-weight: bold;
}

.stButton>button {
    background-color: #ff6fae;
    color: white;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

# 💖 INICIO SIMPLE
st.title("<3")

st.markdown("### Esta app fue hecha con mucho amor para usted, el motivo de cada latido 💖")

# 🎀 MENÚ
opcion = st.selectbox(
    "💖 Elige una opción 💖",
    ["🏠 Inicio", "💌 Carta", "📖 Poemas", "💖 Contador de días", "✨ Sorpresa", "🎮 Juego secreto"]
)

# 🏠 INICIO
if opcion == "🏠 Inicio":
    st.write("💖 <3")

# 💌 CARTA (SIN CAMBIOS)
elif opcion == "💌 Carta":
    st.subheader("💌 Carta de amor")

    st.markdown("""
    <div style="color:white; font-size:18px; line-height:1.8; font-weight:bold;">
    💖 Carta<br><br>
    Si existen otras vidas, otras muertes y otros universos, espero encontrarte en cada uno de ellos. Porque siento que incluso el fin del tiempo sería incapaz de acabar con lo que siento por ti. Aun cuando mi cuerpo desaparezca y solo queden cenizas de mí, sé que incluso ellas seguirían amándote, porque no creo poder dejar de enamorarme de cada parte de ti, de cada lunar, de cada detalle y de esos ojitos suyos en los que podría perderme durante horas sin sentir que es suficiente, porque no existe universo en el que mi corazón no vuelva a elegirlo a usted, ni versión de mí que no termine enamorándose nuevamente de usted, porque sin importar cuándo, dónde o en qué vida sea, mi corazón siempre va a encontrar el camino de regreso a usted, y te aseguro que podría pasar una eternidad admirándolo y aun así sentir que me faltaría tiempo para seguir amándolo…
    </div>
    """, unsafe_allow_html=True)

# 📖 POEMAS (SIN CAMBIOS + CORAZONES ANIMADOS)
elif opcion == "📖 Poemas":
    st.subheader("📖 Poemas")

    poemas = [
"""💖 Tu sonrisa es mi lugar,
en tu mirada quiero habitar.

Te voy a amar sin parar,
y contigo quiero caminar.

No te dejo de imaginar,
lo que siento no se va.

Ni el tiempo lo borrará,
en mi alma siempre estarás.

Hasta el último respirar,
te voy a amar sin parar.""",

"""💖 Si el mundo llega a callar,
tu voz me vuelve a guiar.

Si me pierdo al caminar,
sé que te voy a encontrar.

Porque no dejo de pensar,
que contigo quiero estar.

Y aunque todo pueda cambiar,
yo te vuelvo a amar.

En cada instante al recordar,
siempre vuelvo a tu mirar.""",

"""💖 Te pienso incluso en silencio,
te llevo en cada pensamiento.

Mi refugio en tus brazos,
calma todos mis pasos.

Eres la parte más querida,
de esta alma perdida.

Y en ti volvió mi vida,
suave, dulce y sentida.

En cualquier lugar yo te vuelvo a amar,
sin poderte soltar te vuelvo a buscar.

Porque en ti aprendí a querer,
y en ti quiero permanecer.

Y aunque el mundo pueda cambiar,
yo te voy a recordar.""",

"""💖 Te pienso sin poder parar,
aunque el tiempo quiera cambiar.

Sin importar lo que pase,
siempre vuelvo a amar.

En cada latido estás,
no te puedo soltar.

Mi alma te vuelve a buscar,
sin dejar de soñar.

Porque en cada vida te amaré,
sin poderte olvidar.

Y aunque todo quiera acabar,
yo te vuelvo a encontrar.

Eres mi forma de amar,
y mi razón de quedar."""
    ]

    if "p" not in st.session_state:
        st.session_state.p = 0

    col1, col2 = st.columns(2)

    if col1.button("⬅️"):
        st.session_state.p = (st.session_state.p - 1) % len(poemas)

    if col2.button("➡️"):
        st.session_state.p = (st.session_state.p + 1) % len(poemas)

    hearts = ["💖","💘","💝","💗","💞","❤️"]

    texto = poemas[st.session_state.p]

    animated = ""
    for line in texto.split("\n"):
        animated += line + " " + random.choice(hearts) + "\n"

    st.markdown(f"<pre style='color:white; font-size:18px'>{animated}</pre>", unsafe_allow_html=True)

# 💖 CONTADOR
elif opcion == "💖 Contador de días":
    st.subheader("💖 Contador de amor")

    inicio = date(2024, 4, 22)
    hoy = date.today()

    dias = (hoy - inicio).days

    st.success(f"💖 {dias} días juntos 💖")
    st.write("<3")

# ✨ SORPRESA
elif opcion == "✨ Sorpresa":
    hearts = ["💖", "💘", "💝", "💗", "💞", "❤️"]
    placeholder = st.empty()

    for _ in range(20):
        screen = ""
        for _ in range(12):
            screen += (" " * random.randint(0, 50)) + random.choice(hearts) + "\n"

        placeholder.markdown(f"<pre style='font-size:22px'>{screen}</pre>", unsafe_allow_html=True)
        time.sleep(0.1)

    st.snow()

# 🎮 JUEGO
elif opcion == "🎮 Juego secreto":
    st.subheader("🎮 Encuentra el corazón secreto 💖")

    if "secreto" not in st.session_state:
        st.session_state.secreto = random.randint(1, 5)

    num = st.number_input("Elige un número del 1 al 5 💖", 1, 5)

    if st.button("Probar 💖"):
        if num == st.session_state.secreto:
            st.success("💖 ¡Correcto! 💖")
            st.balloons()
            st.session_state.secreto = random.randint(1, 5)
        else:
            st.error("💔 Intenta otra vez")
