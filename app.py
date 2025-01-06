import streamlit as st
import random

# Configuração básica da página
st.set_page_config(
    page_title="Sorteio Desafios Dead By Daylight",
    layout="centered"
)

########################
# LISTAS E DICIONÁRIOS #
########################

# Lista de desafios para Killer
desafiosKiller = [
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

# Lista de Killers
killers = [
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
    "Charles Lee Ray (The Good Guy)",
    "Unknown (The Unknown)",
    "Vecna (The Lich)",
    "Dracula (The Dark Lord)",
    "Portia Maye (The Houndmaster)"
]

# URLs de imagens de cada Killer (quando não houver imagem oficial, usamos placeholder)
killerImages = {
    "The Trapper": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/f/f4/K01_TheTrapper_Portrait.png/revision/latest?cb=20240517102909",
    "The Wraith": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/c/c2/K02_TheWraith_Portrait.png/revision/latest?cb=20240517102909",
    "The Hillbilly": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/a/a1/K03_TheHillbilly_Portrait.png/revision/latest?cb=20240517102909",
    "The Nurse": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/4/4b/K04_TheNurse_Portrait.png/revision/latest?cb=20240517102909",
    "The Shape (Michael Myers)": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/4/4b/K05_TheShape_Portrait.png/revision/latest?cb=20240517102909",
    "The Hag": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/c/c5/K06_TheHag_Portrait.png/revision/latest?cb=20240517102909",
    "The Doctor": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/b/bd/K07_TheDoctor_Portrait.png/revision/latest?cb=20240517102909",
    "The Huntress": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/3/3b/K08_TheHuntress_Portrait.png/revision/latest?cb=20240517102909",
    "The Cannibal (Leatherface)": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/0/02/K09_TheCannibal_Portrait.png/revision/latest?cb=20240517102909",
    "The Nightmare (Freddy Krueger)": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/e/ed/K10_TheNightmare_Portrait.png/revision/latest?cb=20240517102909",
    "The Pig": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/7/71/K11_ThePig_Portrait.png/revision/latest?cb=20240517102909",
    "The Clown": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/b/b4/K12_TheClown_Portrait.png/revision/latest?cb=20240517102909",
    "The Spirit": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/5/53/K13_TheSpirit_Portrait.png/revision/latest?cb=20240517102909",
    "The Legion": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/a/a2/K14_TheLegion_Portrait.png/revision/latest?cb=20240517102909",
    "The Plague": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/3/3b/K15_ThePlague_Portrait.png/revision/latest?cb=20240517102909",
    "The Ghost Face": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/7/70/K16_TheGhostFace_Portrait.png/revision/latest?cb=20240517102909",
    "The Demogorgon": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/9/9b/K17_TheDemogorgon_Portrait.png/revision/latest?cb=20240517102909",
    "The Oni": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/4/41/K18_TheOni_Portrait.png/revision/latest?cb=20240517102909",
    "The Deathslinger": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/1/16/K19_TheDeathslinger_Portrait.png/revision/latest?cb=20240517102909",
    "The Executioner (Pyramid Head)": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/9/9b/K20_TheExecutioner_Portrait.png/revision/latest?cb=20240517102909",
    "The Blight": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/f/f3/K21_TheBlight_Portrait.png/revision/latest?cb=20240517102909",
    "The Twins": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/9/96/K22_TheTwins_Portrait.png/revision/latest?cb=20240517102909",
    "The Trickster": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/e/e7/K23_TheTrickster_Portrait.png/revision/latest?cb=20240517102909",
    "The Nemesis": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/3/37/K24_TheNemesis_Portrait.png/revision/latest?cb=20240517102909",
    "The Cenobite (Pinhead)": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/7/74/K25_TheCenobite_Portrait.png/revision/latest?cb=20240517102909",
    "The Artist": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/d/d6/K26_TheArtist_Portrait.png/revision/latest?cb=20240517102909",
    "The Onryō (Sadako)": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/4/4e/K27_TheOnryo_Portrait.png/revision/latest?cb=20240517102909",
    "The Dredge": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/9/9a/K28_TheDredge_Portrait.png/revision/latest?cb=20240517102909",
    "The Mastermind (Albert Wesker)": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/0/09/K29_TheMastermind_Portrait.png/revision/latest?cb=20240517102909",
    "The Knight": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/8/86/K30_TheKnight_Portrait.png/revision/latest?cb=20240517102909",
    "The Skull Merchant": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/a/ac/K31_TheSkullMerchant_Portrait.png/revision/latest?cb=20240517102909",
    "The Xenomorph": "https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/3/3b/K32_TheXenomorph_Portrait.png/revision/latest?cb=20240517102909",

    # Extras com placeholder
    "Charles Lee Ray (The Good Guy)": "https://via.placeholder.com/200?text=Charles+Lee+Ray",
    "Unknown (The Unknown)": "https://via.placeholder.com/200?text=Unknown",
    "Vecna (The Lich)": "https://via.placeholder.com/200?text=Vecna",
    "Dracula (The Dark Lord)": "https://via.placeholder.com/200?text=Dracula",
    "Portia Maye (The Houndmaster)": "https://via.placeholder.com/200?text=Portia+Maye"
}

# Lista de desafios para Survivors
desafiosSurvivors = [
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


#######################
# FUNÇÕES DE SORTEIO  #
#######################

def sortear_desafios_killer(qtd=4):
    """Retorna uma lista de 'qtd' desafios distintos para Killer."""
    return random.sample(desafiosKiller, k=qtd)

def sortear_killer():
    """Retorna um Killer aleatório da lista 'killers'."""
    return random.choice(killers)

def sortear_mortes():
    """Retorna um valor aleatório entre 1 e 4 (mortes necessárias)."""
    return random.randint(1, 4)

def sortear_desafios_survivors(qtd=4):
    """Retorna uma lista de 'qtd' desafios distintos para Survivors."""
    return random.sample(desafiosSurvivors, k=qtd)

def sortear_escapes():
    """Retorna um valor aleatório entre 1 e 4 (escapes necessários)."""
    return random.randint(1, 4)


###################
# SESSION STATE   #
###################
# Aqui inicializamos as variáveis de sessão que armazenam o que já foi sorteado.

# Aba Killer
if "desafios_killer" not in st.session_state:
    st.session_state.desafios_killer = []
if "killer_sorteado" not in st.session_state:
    st.session_state.killer_sorteado = ""
if "mortes_sorteadas" not in st.session_state:
    st.session_state.mortes_sorteadas = 0

# Aba Survivors
if "desafios_survivors" not in st.session_state:
    st.session_state.desafios_survivors = []
if "escapes_sorteados" not in st.session_state:
    st.session_state.escapes_sorteados = 0


##############
# LAYOUT UI  #
##############
st.title("Sorteio Desafios Dead By Daylight")

# Criamos duas abas: Killer e Survivors
tab1, tab2 = st.tabs(["Killer", "Survivors"])

#
# ABA: KILLER
#
with tab1:
    st.subheader("Desafios (Killer)")

    # Botão para sortear DESAFIOS
    if st.button("Sortear Desafios (Killer)"):
        st.session_state.desafios_killer = sortear_desafios_killer()

    # Exibe os desafios sorteados
    if len(st.session_state.desafios_killer) > 0:
        st.write("**Desafios Sorteados:**")
        for i, d in enumerate(st.session_state.desafios_killer, start=1):
            st.write(f"{i}) {d}")

    st.write("---")

    # Botão para sortear KILLER
    if st.button("Sortear Killer"):
        st.session_state.killer_sorteado = sortear_killer()

    # Exibe o Killer sorteado e a imagem correspondente, se existir
    if st.session_state.killer_sorteado:
        st.write("**Killer Sorteado:**", st.session_state.killer_sorteado)
        if st.session_state.killer_sorteado in killerImages:
            st.image(killerImages[st.session_state.killer_sorteado], width=200)
    else:
        st.write("**Killer Sorteado:** -")

    st.write("---")

    # Botão para sortear MORTES
    if st.button("Sortear Mortes"):
        st.session_state.mortes_sorteadas = sortear_mortes()
    if st.session_state.mortes_sorteadas > 0:
        st.write("**Mortes Necessárias:**", st.session_state.mortes_sorteadas)
    else:
        st.write("**Mortes Necessárias:** -")

    st.write("---")

    # Botão para "Sortear Tudo"
    if st.button("Sortear Tudo (Killer)"):
        st.session_state.desafios_killer = sortear_desafios_killer()
        st.session_state.killer_sorteado = sortear_killer()
        st.session_state.mortes_sorteadas = sortear_mortes()
        st.success("Tudo sorteado com sucesso!")


#
# ABA: SURVIVORS
#
with tab2:
    st.subheader("Desafios (Survivors)")

    # Botão para sortear DESAFIOS
    if st.button("Sortear Desafios (Survivors)"):
        st.session_state.desafios_survivors = sortear_desafios_survivors()

    # Exibe os desafios sorteados
    if len(st.session_state.desafios_survivors) > 0:
        st.write("**Desafios Sorteados:**")
        for i, d in enumerate(st.session_state.desafios_survivors, start=1):
            st.write(f"{i}) {d}")

    st.write("---")

    # Botão para sortear ESCAPES
    if st.button("Sortear Escapes"):
        st.session_state.escapes_sorteados = sortear_escapes()
    if st.session_state.escapes_sorteados > 0:
        st.write("**Escapes Necessários:**", st.session_state.escapes_sorteados)
    else:
        st.write("**Escapes Necessários:** -")

    st.write("---")

    # Botão para "Sortear Tudo"
    if st.button("Sortear Tudo (Survivors)"):
        st.session_state.desafios_survivors = sortear_desafios_survivors()
        st.session_state.escapes_sorteados = sortear_escapes()
        st.success("Tudo sorteado com sucesso!")


#################
# FOOTER / RODAPÉ
#################
st.write("---")
st.caption("Feito por Sinnex - @lucianosnx")
