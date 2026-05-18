import streamlit as st
import time
import random
from datetime import date

st.set_page_config(page_title="💖 Para mi amor 💖", page_icon="💖")

# 🌟 BIENVENIDA
st.title("💖 Bienvenido querido mío 💖")

mensaje = "Preparando nuestro mundo..."
texto = st.empty()

typed = ""
for letra in mensaje:
    typed += letra
    texto.markdown(f"### {typed}")
    time.sleep(0.04)

st.write("💖 Todo listo para ti 💖")

# 🎵 CANCION (YOUTUBE)
st.subheader("🎵 Música para ti 💖")

st.video("https://www.youtube.com/watch?v=nyuo9-OjNNg")

# 🎀 MENÚ
opcion = st.selectbox(
    "💖 Elige una opción 💖",
    ["🏠 Inicio", "💌 Carta", "📖 Poemas", "💖 Contador de días", "✨ Sorpresa", "🎮 Juego secreto"]
)

# 🏠 INICIO
if opcion == "🏠 Inicio":
    st.subheader("💖 Inicio")
    st.write("💖 Esta app fue hecha con amor 💖")

# 💌 CARTA
elif opcion == "💌 Carta":
    st.subheader("💌 Carta de amor")

    st.markdown("""
    <div style="color:#ff2e88; font-size:18px; line-height:1.8; font-weight:bold;">
    💖 Carta<br><br>
    Si existen otras vidas, otras muertes y otros universos, espero encontrarte en cada uno de ellos. Porque siento que incluso el fin del tiempo sería incapaz de acabar con lo que siento por ti. Aun cuando mi cuerpo desaparezca y solo queden cenizas de mí, sé que incluso ellas seguirían amándote, porque no creo poder dejar de enamorarme de cada parte de ti, de cada lunar, de cada detalle y de esos ojitos suyos en los que podría perderme durante horas sin sentir que es suficiente, porque no existe universo en el que mi corazón no vuelva a elegirlo a usted, ni versión de mí que no termine enamorándose nuevamente de usted, porque sin importar cuándo, dónde o en qué vida sea, mi corazón siempre va a encontrar el camino de regreso a usted, y te aseguro que podría pasar una eternidad admirándolo y aun así sentir que me faltaría tiempo para seguir amándolo…
    </div>
    """, unsafe_allow_html=True)

# 📖 POEMAS (CORAZONES ANIMADOS)
elif opcion == "📖 Poemas":
    st.subheader("📖 Poemas")

    hearts = ["💖", "💘", "💝", "💗", "💞", "❤️"]

    texto_poemas = """
💖 Tu sonrisa es mi lugar,
en tu mirada quiero habitar.

Te voy a amar sin parar,
y contigo quiero caminar.

💖 Si el mundo llega a callar,
tu voz me vuelve a guiar.

Si me pierdo al caminar,
sé que te voy a encontrar.

💖 Te pienso incluso en silencio,
te llevo en cada pensamiento.

Eres mi refugio eterno,
mi amor más sincero.

💖 Te pienso sin poder parar,
aunque el tiempo quiera cambiar.

En cada vida te amaré,
sin poderte olvidar.
"""

    placeholder = st.empty()

    for _ in range(30):
        animated = ""
        for line in texto_poemas.split("\n"):
            animated += line + " " + random.choice(hearts) + "\n"

        placeholder.markdown(
            f"<pre style='color:#ff2e88; font-size:18px'>{animated}</pre>",
            unsafe_allow_html=True
        )

        time.sleep(0.2)

# 💖 CONTADOR
elif opcion == "💖 Contador de días":
    st.subheader("💖 Nuestro amor en el tiempo")

    inicio = date(2024, 4, 22)
    hoy = date.today()

    dias = (hoy - inicio).days

    st.success(f"💖 Llevamos {dias} días juntos 💖")
    st.balloons()

# ✨ SORPRESA
elif opcion == "✨ Sorpresa":
    st.subheader("💖 Lluvia de amor")

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

    if st.button("Probar suerte 💖"):
        if num == st.session_state.secreto:
            st.success("💖 ¡Lo encontraste! 💖")
            st.balloons()
            st.session_state.secreto = random.randint(1, 5)
        else:
            st.error("💔 No era ese... intenta otra vez")
