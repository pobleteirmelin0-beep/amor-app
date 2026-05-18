import streamlit as st
import time
import random
from datetime import date

st.set_page_config(page_title="💖 Para mi amor 💖", page_icon="💖")

# 🌟 BIENVENIDA ANIMADA
st.title("💖 Bienvenido querido mío 💖")

mensaje = "Preparando nuestro mundo..."
texto = st.empty()

typed = ""
for letra in mensaje:
    typed += letra
    texto.markdown(f"### {typed}")
    time.sleep(0.04)

st.write("💖 Todo está listo para ti 💖")

# 🎀 MENÚ BONITO
opcion = st.selectbox(
    "💖 Elige una opción 💖",
    ["🏠 Inicio", "💌 Carta", "📖 Poemas", "💖 Contador de días", "✨ Sorpresa", "🎮 Juego secreto"]
)

# 🏠 INICIO
if opcion == "🏠 Inicio":
    st.subheader("💖 Inicio")
    st.write("💖 Esta app fue hecha con mucho amor 💖")

# 💌 CARTA (TU TEXTO EXACTO)
elif opcion == "💌 Carta":
    st.subheader("💌 Carta de amor")

    st.markdown("""
    <div style="color:#ff2e88; font-size:18px; line-height:1.8; font-weight:bold;">
    💖 Carta<br><br>
    Si existen otras vidas, otras muertes y otros universos, espero encontrarte en cada uno de ellos. Porque siento que incluso el fin del tiempo sería incapaz de acabar con lo que siento por ti. Aun cuando mi cuerpo desaparezca y solo queden cenizas de mí, sé que incluso ellas seguirían amándote, porque no creo poder dejar de enamorarme de cada parte de ti, de cada lunar, de cada detalle y de esos ojitos suyos en los que podría perderme durante horas sin sentir que es suficiente, porque no existe universo en el que mi corazón no vuelva a elegirlo a usted, ni versión de mí que no termine enamorándose nuevamente de usted, porque sin importar cuándo, dónde o en qué vida sea, mi corazón siempre va a encontrar el camino de regreso a usted, y te aseguro que podría pasar una eternidad admirándolo y aun así sentir que me faltaría tiempo para seguir amándolo…
    </div>
    """, unsafe_allow_html=True)

# 📖 POEMAS (TODOS EXACTOS)
elif opcion == "📖 Poemas":
    st.subheader("📖 Poemas")

    st.markdown("""
    <div style="color:#ff2e88; font-size:17px; line-height:1.8; font-weight:bold;">

    💖 POEMA 1<br>
    Tu sonrisa es mi lugar,<br>
    en tu mirada quiero habitar.<br>
    Te voy a amar sin parar,<br>
    y contigo quiero caminar.<br>
    No te dejo de imaginar,<br>
    lo que siento no se va.<br>
    Ni el tiempo lo borrará,<br>
    en mi alma siempre estarás.<br>
    Hasta el último respirar,<br>
    te voy a amar sin parar.<br><br>

    💖 POEMA 2<br>
    Si el mundo llega a callar,<br>
    tu voz me vuelve a guiar.<br>
    Si me pierdo al caminar,<br>
    sé que te voy a encontrar.<br>
    Porque no dejo de pensar,<br>
    que contigo quiero estar.<br>
    Y aunque todo pueda cambiar,<br>
    yo te vuelvo a amar.<br>
    En cada instante al recordar,<br>
    siempre vuelvo a tu mirar.<br><br>

    💖 POEMA 3<br>
    Te pienso incluso en silencio,<br>
    te llevo en cada pensamiento.<br>
    Mi refugio en tus brazos,<br>
    calma todos mis pasos.<br>
    Eres la parte más querida,<br>
    de esta alma perdida.<br>
    Y en ti volvió mi vida,<br>
    suave, dulce y sentida.<br>
    En cualquier lugar yo te vuelvo a amar,<br>
    sin poderte soltar te vuelvo a buscar.<br>
    Porque en ti aprendí a querer,<br>
    y en ti quiero permanecer.<br>
    Y aunque el mundo pueda cambiar,<br>
    yo te voy a recordar.<br><br>

    💖 POEMA 4<br>
    Te pienso sin poder parar,<br>
    aunque el tiempo quiera cambiar.<br>
    Sin importar lo que pase,<br>
    siempre vuelvo a amar.<br>
    En cada latido estás,<br>
    no te puedo soltar.<br>
    Mi alma te vuelve a buscar,<br>
    sin dejar de soñar.<br>
    Porque en cada vida te amaré,<br>
    sin poderte olvidar.<br>
    Y aunque todo quiera acabar,<br>
    yo te vuelvo a encontrar.<br>
    Eres mi forma de amar,<br>
    y mi razón de quedar.<br>

    </div>
    """, unsafe_allow_html=True)

# 💖 CONTADOR DE DÍAS
elif opcion == "💖 Contador de días":
    st.subheader("💖 Nuestro amor en el tiempo")

    inicio = date(2024, 4, 22)
    hoy = date.today()

    dias = (hoy - inicio).days

    st.success(f"💖 Llevamos {dias} días juntos 💖")
    st.balloons()

# ✨ SORPRESA (CORAZONES)
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

# 🎮 JUEGO NUEVO (SECRETO)
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
