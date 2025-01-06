import random
import streamlit as st

# ========== CONFIGURAÇÕES INICIAIS ==========

# CSS para centralizar conteúdo e dar um visual melhor
st.markdown("""
<style>
/* Centralizar todo o conteúdo da página */
main.block-container {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.title("Sorteio Desafios Dead By Daylight")

# ========== DADOS (LISTAS) ==========

DESAFIOS_KILLER = [
    "sem perks",
    "não pode deixar concluir 5 gens",
    "não pode enganchar personagens femininos (até remover os masculinos)",
    "não pode sluggar (derrubou tem que pegar)",
    "não pode quebrar pallets",
    "não pode pular janelas",
    "não pode tunelar",
    "não pode campar",
    "não pode chutar gerador",
    "não pode usar o poder do assassino",
    "não pode ter dois sobreviventes feridos ao mesmo tempo",
    "não pode enganchar personagens masculinos (até remover os femininos)",
    "apenas 1 perk",
    "apenas 2 perks",
    "não pode dar hit com bloodlust",
    "não pode deixar concluir 3 gens",
    "não pode sair do trigen",
    "não pode usar perks anti gen",
    "só pode matar no slug",
    "tem que ficar parado na frente do gancho",
    "só pode hitar o primeiro sobrevivente que foi visto (até remover ele da partida)",
    "1 minuto afk",
    "campar no chão o primeiro sobrevivente que cair (até que ele morra)",
    "só pode enganchar no basement",
    "não pode usar addons",
    "não pode demorar mais de 2 minutos para derrubar um sobrevivente",
    "não pode hitar personagens masculinos (até remover os femininos)",
    "não pode hitar personagens femininos (até remover os masculinos)"
]

KILLERS = [
    "The Trapper",
    "The Wraith",
    "The Hillbilly",
    "The Nurse",
    "The Shape (Michael Myers)",
    "The Hag",
    "The Doctor",
    "The Huntress",
    "The Cannibal (Leatherface)",
    "The Nightmare (Freddy Krueger)",
    "The Pig",
    "The Clown",
    "The Spirit",
    "The Legion",
    "The Plague",
    "The Ghost Face",
    "The Demogorgon",
    "The Oni",
    "The Deathslinger",
    "The Executioner (Pyramid Head)",
    "The Blight",
    "The Twins",
    "The Trickster",
    "The Nemesis",
    "The Cenobite (Pinhead)",
    "The Artist",
    "The Onryō (Sadako)",
    "The Dredge",
    "The Mastermind (Albert Wesker)",
    "The Knight",
    "The Skull Merchant",
    "The Xenomorph",
    # Exemplos fictícios
    "Charles Lee Ray (The Good Guy)",
    "Unknown (The Unknown)",
    "Vecna (The Lich)",
    "Dracula (The Dark Lord)",
    "Portia Maye (The Houndmaster)"
]

KILLER_IMAGES = {
    "The Trapper": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/f/f4/K01_TheTrapper_Portrait.png",
    "The Wraith": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/c/c2/K02_TheWraith_Portrait.png",
    "The Hillbilly": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/a/a1/K03_TheHillbilly_Portrait.png",
    "The Nurse": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/4/4b/K04_TheNurse_Portrait.png",
    "The Shape (Michael Myers)": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/4/4b/K05_TheShape_Portrait.png",
    "The Hag": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/c/c5/K06_TheHag_Portrait.png",
    "The Doctor": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/b/bd/K07_TheDoctor_Portrait.png",
    "The Huntress": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/3/3b/K08_TheHuntress_Portrait.png",
    "The Cannibal (Leatherface)": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/0/02/K09_TheCannibal_Portrait.png",
    "The Nightmare (Freddy Krueger)": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/e/ed/K10_TheNightmare_Portrait.png",
    "The Pig": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/7/71/K11_ThePig_Portrait.png",
    "The Clown": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/b/b4/K12_TheClown_Portrait.png",
    "The Spirit": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/5/53/K13_TheSpirit_Portrait.png",
    "The Legion": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/a/a2/K14_TheLegion_Portrait.png",
    "The Plague": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/3/3b/K15_ThePlague_Portrait.png",
    "The Ghost Face": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/7/70/K16_TheGhostFace_Portrait.png",
    "The Demogorgon": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/9/9b/K17_TheDemogorgon_Portrait.png",
    "The Oni": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/4/41/K18_TheOni_Portrait.png",
    "The Deathslinger": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/1/16/K19_TheDeathslinger_Portrait.png",
    "The Executioner (Pyramid Head)": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/9/9b/K20_TheExecutioner_Portrait.png",
    "The Blight": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/f/f3/K21_TheBlight_Portrait.png",
    "The Twins": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/9/96/K22_TheTwins_Portrait.png",
    "The Trickster": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/e/e7/K23_TheTrickster_Portrait.png",
    "The Nemesis": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/3/37/K24_TheNemesis_Portrait.png",
    "The Cenobite (Pinhead)": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/7/74/K25_TheCenobite_Portrait.png",
    "The Artist": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/d/d6/K26_TheArtist_Portrait.png",
    "The Onryō (Sadako)": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/4/4e/K27_TheOnryo_Portrait.png",
    "The Dredge": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/9/9a/K28_TheDredge_Portrait.png",
    "The Mastermind (Albert Wesker)": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/0/09/K29_TheMastermind_Portrait.png",
    "The Knight": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/8/86/K30_TheKnight_Portrait.png",
    "The Skull Merchant": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/a/ac/K31_TheSkullMerchant_Portrait.png",
    "The Xenomorph": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/3/3b/K32_TheXenomorph_Portrait.png",

    # Fictícios (placeholders)
    "Charles Lee Ray (The Good Guy)": "https://via.placeholder.com/200?text=Charles+Lee+Ray",
    "Unknown (The Unknown)": "https://via.placeholder.com/200?text=Unknown",
    "Vecna (The Lich)": "https://via.placeholder.com/200?text=Vecna",
    "Dracula (The Dark Lord)": "https://via.placeholder.com/200?text=Dracula",
    "Portia Maye (The Houndmaster)": "https://via.placeholder.com/200?text=Portia+Maye"
}

DESAFIOS_SURVIVORS = [
    "sem perks",
    "sem dropar pallets",
    "sem pular janelas",
    "sem tomar gancho",
    "sem cair",
    "2 minutos sem fazer gen",
    "se tomar gancho tem que quitar",
    "sem se curar",
    "2 perks cada",
    "2 minutos sem ser visto",
    "sem correr",
    "4 personagens iguais",
    "sempre agachado",
    "se clicar no gen não pode mais soltar",
    "só pode ir pro gancho tomando catch",
    "sem itens",
    "só pode fazer gen em dupla",
    "se alguém morrer todos tem que quitar",
    "somente 1 gerador pode ser reparado por vez",
    "não pode iniciar outro gerador até completar o primeiro que foi iniciado",
    "o primeiro gerador tem que ser concluído em trio",
    "sem tomar hit",
    "todos com no mither",
    "2 minutos sem sair do armário",
    "2 flashlight ou 2 pallet save"
]

# ========== SESSION STATE ==========

if "desafios_killer" not in st.session_state:
    st.session_state["desafios_killer"] = []
if "desafios_survivors" not in st.session_state:
    st.session_state["desafios_survivors"] = []
if "killer_atual" not in st.session_state:
    st.session_state["killer_atual"] = None
if "killer_img" not in st.session_state:
    st.session_state["killer_img"] = None
if "mortes" not in st.session_state:
    st.session_state["mortes"] = None
if "escapes" not in st.session_state:
    st.session_state["escapes"] = None


# ========== FUNÇÕES ==========

def capitalizar(texto: str) -> str:
    if not texto:
        return texto
    return texto[0].upper() + texto[1:]


# --- Killer ---
def sortear_desafios_killer():
    st.session_state["desafios_killer"] = random.sample(DESAFIOS_KILLER, 4)

def reroll_desafio_killer(index):
    disponiveis = set(DESAFIOS_KILLER) - set(st.session_state["desafios_killer"])
    if disponiveis:
        novo = random.choice(list(disponiveis))
        st.session_state["desafios_killer"][index] = novo
    else:
        st.warning("Não há mais desafios disponíveis para re-roll.")

def sortear_killer():
    sorteado = random.choice(KILLERS)
    st.session_state["killer_atual"] = sorteado
    st.session_state["killer_img"] = KILLER_IMAGES.get(sorteado)

def sortear_mortes():
    st.session_state["mortes"] = random.randint(1,4)

def sortear_tudo_killer():
    sortear_desafios_killer()
    sortear_killer()
    sortear_mortes()

# --- Survivors ---
def sortear_desafios_survivors():
    st.session_state["desafios_survivors"] = random.sample(DESAFIOS_SURVIVORS, 4)

def reroll_desafio_survivors(index):
    disponiveis = set(DESAFIOS_SURVIVORS) - set(st.session_state["desafios_survivors"])
    if disponiveis:
        novo = random.choice(list(disponiveis))
        st.session_state["desafios_survivors"][index] = novo
    else:
        st.warning("Não há mais desafios disponíveis para re-roll.")

def sortear_escapes():
    st.session_state["escapes"] = random.randint(1,4)

def sortear_tudo_survivors():
    sortear_desafios_survivors()
    sortear_escapes()


# ========== LAYOUT COM TABS ==========

tab_killer, tab_survivors = st.tabs(["Killer", "Survivors"])

# ========== ABA: KILLER ==========

with tab_killer:
    with st.container():
        st.subheader("1) Desafios (Killer)")
        # Botão principal para sortear 4 desafios
        if st.button("Sortear Desafios (Killer)"):
            sortear_desafios_killer()

        # Mostrar cada desafio
        for i, desafio in enumerate(st.session_state["desafios_killer"]):
            cols = st.columns([4,1])  # 4 partes pro texto, 1 pro botão
            with cols[0]:
                st.info(capitalizar(desafio))
            with cols[1]:
                # Botão Reroll
                if st.button(f"Reroll {i+1}", key=f"reroll_killer_{i}"):
                    reroll_desafio_killer(i)

    with st.container():
        st.subheader("2) Killer Sorteado")
        # Botão para sortear 1 killer
        if st.button("Sortear Killer"):
            sortear_killer()

        # Mostrar killer sorteado
        if st.session_state["killer_atual"]:
            st.markdown(f"**{st.session_state['killer_atual']}**")
            if st.session_state["killer_img"]:
                st.image(st.session_state["killer_img"], width=200)

    with st.container():
        st.subheader("3) Mortes Necessárias (1 a 4)")
        # Botão para sortear mortes
        if st.button("Sortear Mortes"):
            sortear_mortes()

        # Mostrar mortes
        if st.session_state["mortes"] is not None:
            st.markdown(f"**Mortes:** {st.session_state['mortes']}")

    # Botão para sortear tudo
    with st.container():
        if st.button("Sortear Tudo (Killer)"):
            sortear_tudo_killer()

# ========== ABA: SURVIVORS ==========

with tab_survivors:
    with st.container():
        st.subheader("1) Desafios (Survivors)")
        # Botão para sortear 4 desafios
        if st.button("Sortear Desafios (Survivors)"):
            sortear_desafios_survivors()

        # Mostrar cada desafio
        for i, desafio in enumerate(st.session_state["desafios_survivors"]):
            cols = st.columns([4,1])
            with cols[0]:
                st.info(capitalizar(desafio))
            with cols[1]:
                # Botão Reroll
                if st.button(f"Reroll S{i+1}", key=f"reroll_survivor_{i}"):
                    reroll_desafio_survivors(i)

    with st.container():
        st.subheader("2) Escapes Necessários (1 a 4)")
        # Botão para sortear escapes
        if st.button("Sortear Escapes"):
            sortear_escapes()

        # Mostrar escapes
        if st.session_state["escapes"] is not None:
            st.markdown(f"**Escapes:** {st.session_state['escapes']}")

    # Botão para sortear tudo
    with st.container():
        if st.button("Sortear Tudo (Survivors)"):
            sortear_tudo_survivors()

st.markdown("---")
st.caption("Feito por Sinnex - @lucianosnx")
