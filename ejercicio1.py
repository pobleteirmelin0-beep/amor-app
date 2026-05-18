import streamlit as st
import time
import random
from datetime import date

st.set_page_config(page_title="💖 Para mi amor 💖", page_icon="💖")

# 🌸 ESTILO ROSA PASTEL
st.markdown("""
<style>
.stApp {
    background: #ffd6e7;
}
h1, h2, h3, p, label {
    color: #ffffff !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# 💖 INICIO
st.title("💖 Bienvenido querido mío 💖")

st.markdown("<h3 style='color:white;text-align:center'><3</h3>", unsafe_allow_html=True)

st.write("esta app fue hecha con mucho amor para usted, el motivo de cada latido")

# 🎀 MENÚ
opcion = st.selectbox(
    "💖 Elige una opción 💖",
    ["🏠 Inicio", "💌 Carta", "📖 Poemas", "💖 Contador", "✨ Sorpresa", "🎮 Juego"]
)

# 🏠 INICIO
if opcion == "🏠 Inicio":
    st.write("esta app fue hecha con mucho amor para usted, el motivo de cada latido")

# 💌 CARTA (INTACTA)
elif opcion == "💌 Carta":
    st.subheader("💌 Carta de amor")

    st.markdown("""
    <div style="color:white; font-size:18px; line-height:1.8; font-weight:bold;">
    💖 Carta<br><br>
    Si existen otras vidas, otras muertes y otros universos, espero encontrarte en cada uno de ellos. Porque siento que incluso el fin del tiempo sería incapaz de acabar con lo que siento por ti. Aun cuando mi cuerpo desaparezca y solo queden cenizas de mí, sé que incluso ellas seguirían amándote, porque no creo poder dejar de enamorarme de cada parte de ti, de cada lunar, de cada detalle y de esos ojitos suyos en los que podría perderme durante horas sin sentir que es suficiente, porque no existe universo en el que mi corazón no vuelva a elegirlo a usted, ni versión de mí que no termine enamorándose nuevamente de usted, porque sin importar cuándo, dónde o en qué vida sea, mi corazón siempre va a encontrar el camino de regreso a usted, y te aseguro que podría pasar una eternidad admirándolo y aún así sentir que me faltaría tiempo para seguir amándolo…
    </div>
    """, unsafe_allow_html=True)

# 📖 POEMAS (CON NAVEGACIÓN)
elif opcion == "📖 Poemas":

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
suave, dulce y sentida.
En cualquier lugar yo te vuelvo a amar,
sin poderte soltar te vuelvo a buscar.
Porque en ti aprendí a querer,
y en ti quiero permanecer.
Y aunque el mundo pueda cambiar,
yo te voy a recordar.""",

        """Te pienso sin poder parar,
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

    if "poema_i" not in st.session_state:
        st.session_state.poema_i = 0

    def corazon():
        st.markdown("💖💖💖")

    st.subheader(f"📖 Poema {st.session_state.poema_i + 1}")

    st.write(poemas[st.session_state.poema_i])

    col1, col2 = st.columns(2)

    if col1.button("◀ Anterior"):
        if st.session_state.poema_i > 0:
            st.session_state.poema_i -= 1
            corazon()

    if col2.button("▶ Siguiente"):
        if st.session_state.poema_i < len(poemas) - 1:
            st.session_state.poema_i += 1
            corazon()

# 💖 CONTADOR
elif opcion == "💖 Contador":

    st.subheader("💖 Nuestro amor")

    inicio = date(date.today().year, 4, 22)
    dias = (date.today() - inicio).days

    st.success(f"💖 Llevamos {dias} días juntos 💖")

    st.markdown("💖💖💖")

# ✨ SORPRESA
elif opcion == "✨ Sorpresa":

    st.subheader("Buscando al amor de mi vida...")

    barra = st.progress(0)

    for i in range(100):
        time.sleep(0.03)
        barra.progress(i + 1)

    st.success("encontrado, usted")

# 🎮 JUEGO
elif opcion == "🎮 Juego":

    st.subheader("🎮 Adivina el corazón secreto 💖")

    if "secreto" not in st.session_state:
        st.session_state.secreto = random.randint(1, 5)

    num = st.number_input("Elige un número (1-5)", 1, 5)

    if st.button("Probar suerte 💖"):
        if num == st.session_state.secreto:
            st.success("lo lograste, te amo 💖")
            st.balloons()
            st.session_state.secreto = random.randint(1, 5)
        else:
            st.error("💔 intenta otra vez")
