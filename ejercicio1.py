import streamlit as st
import time

st.set_page_config(page_title="💖 Para mi amor 💖", page_icon="💖")

# =========================================================
# 💖 ESTILO ROSA
# =========================================================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
}

h1, h2, h3, p, label {
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

# =========================================================
# 💖 SORPRESA + CORAZONES FLOTANTES
# =========================================================
if opcion == "Sorpresa ✨":

    st.write("💖 Buscando al amor de mi vida...")

    barra = st.progress(0)

    for i in range(100):
        time.sleep(0.02)
        barra.progress(i + 1)

    st.success("Encontrado, usted 💖")

    st.markdown("""
    <style>
    .hearts {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 9999;
    }

    .heart {
        position: absolute;
        bottom: -50px;
        color: #ff2e88;
        font-size: 26px;
        animation: floatUp 6s linear infinite;
    }

    .heart:nth-child(1){left:10%;}
    .heart:nth-child(2){left:25%;}
    .heart:nth-child(3){left:40%;}
    .heart:nth-child(4){left:55%;}
    .heart:nth-child(5){left:70%;}
    .heart:nth-child(6){left:85%;}

    @keyframes floatUp {
        0% {transform: translateY(0); opacity: 1;}
        100% {transform: translateY(-120vh); opacity: 0;}
    }
    </style>

    <div class="hearts">
        <div class="heart">💖</div>
        <div class="heart">💖</div>
        <div class="heart">💖</div>
        <div class="heart">💖</div>
        <div class="heart">💖</div>
        <div class="heart">💖</div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# 💖 POEMAS CON FLECHAS + CORAZONES + FIX FINAL
# =========================================================
if opcion == "Poemas 💖":

    if "poema_idx" not in st.session_state:
        st.session_state.poema_idx = 1
        st.session_state.show_hearts = False

    def hearts_animation():
        st.markdown("""
        <style>
        .hearts {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 9999;
        }

        .heart {
            position: absolute;
            bottom: -50px;
            color: #ff2e88;
            font-size: 26px;
            animation: floatUp 2s linear infinite;
        }

        .heart:nth-child(1){left:10%;}
        .heart:nth-child(2){left:30%;}
        .heart:nth-child(3){left:50%;}
        .heart:nth-child(4){left:70%;}
        .heart:nth-child(5){left:90%;}

        @keyframes floatUp {
            0% {transform: translateY(0); opacity: 1;}
            100% {transform: translateY(-120vh); opacity: 0;}
        }
        </style>

        <div class="hearts">
            <div class="heart">💖</div>
            <div class="heart">💖</div>
            <div class="heart">💖</div>
            <div class="heart">💖</div>
            <div class="heart">💖</div>
        </div>
        """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    if col1.button("⬅ Anterior"):
        if st.session_state.poema_idx > 1:
            st.session_state.poema_idx -= 1
            st.session_state.show_hearts = True
            st.rerun()

    if col2.button("💖 Cambiar"):
        st.session_state.show_hearts = True
        st.rerun()

    if col3.button("Siguiente ➜"):
        if st.session_state.poema_idx < 4:
            st.session_state.poema_idx += 1
            st.session_state.show_hearts = True
            st.rerun()

    if st.session_state.show_hearts:
        hearts_animation()
        time.sleep(1)
        st.session_state.show_hearts = False

    # =========================================================
    # 💖 POEMA 1
    # =========================================================
    if st.session_state.poema_idx == 1:
        st.markdown("""
💖 Tu sonrisa es mi lugar,  
en tu mirada quiero habitar.  

Te voy a amar sin parar,  
y contigo quiero caminar.  

No te dejo de imaginar,  
lo que siento no se va.  

Ni el tiempo lo borrará,  
en mi alma siempre estarás.  

Hasta el último respirar,  
te voy a amar sin parar.
""")

    # =========================================================
    # 💖 POEMA 2
    # =========================================================
    if st.session_state.poema_idx == 2:
        st.markdown("""
💖 Si el mundo llega a callar,  
tu voz me vuelve a guiar.  

Si me pierdo al caminar,  
sé que te voy a encontrar.  

Porque no dejo de pensar,  
que contigo quiero estar.  

Y aunque todo pueda cambiar,  
yo te vuelvo a amar.  

En cada instante al recordar,  
siempre vuelvo a tu mirar.
""")

    # =========================================================
    # 💖 POEMA 3
    # =========================================================
    if st.session_state.poema_idx == 3:
        st.markdown("""
💖 Te pienso incluso en silencio,  
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
yo te voy a recordar.
""")

    # =========================================================
    # 💖 POEMA 4
    # =========================================================
    if st.session_state.poema_idx == 4:
        st.markdown("""
💖 Te pienso sin poder parar,  
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
y mi razón de quedar.
""")
