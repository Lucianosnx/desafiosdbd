import streamlit as st
import random

# ---- CONFIGURAÇÕES DA PÁGINA ----
st.set_page_config(
    page_title="Sorteio Desafios Dead By Daylight",
    layout="centered"
)

# ---- CSS CUSTOM: para deixar tabs em destaque, centralizar, etc. ----
st.markdown("""
<style>
/* Centraliza todo o app */
.main > div {
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* Ajusta a área das tabs para ficar no centro e com mais destaque */
div[data-testid="stTabs"] button {
    font-size: 1.1rem !important; /* aumenta a fonte das abas */
    font-weight: bold !important;
    margin: 0 5px; /* pequeno espaçamento lateral */
    border-radius: 8px !important;
    padding: 0.5rem 1rem !important;
    box-shadow: none !important;
    outline: none !important;
    border: 3px solid #aaa !important; /* borda “base” das abas */
}

/* Deixa a primeira aba (Killer) vermelha */
div[data-testid="stTabs"] > div > button:nth-of-type(1) {
    color: #fff !important;
    background-color: #ff5c57 !important;
    border-color: #ff5c57 !important; 
}
div[data-testid="stTabs"] > div > button:nth-of-type(1):hover {
    background-color: #ff3c37 !important;
    border-color: #ff3c37 !important;
}

/* Deixa a segunda aba (Survivors) azul */
div[data-testid="stTabs"] > div > button:nth-of-type(2) {
    color: #fff !important;
    background-color: #337ab7 !important;
    border-color: #337ab7 !important;
}
div[data-testid="stTabs"] > div > button:nth-of-type(2):hover {
    background-color: #285e8e !important;
    border-color: #285e8e !important;
}

/* Centraliza tudo dentro das tabs */
.section-container {
    background-color: #2f2f2f;
    padding: 1rem;
    border-radius: 8px;
    margin-bottom: 1rem;
    width: 100%;
    max-width: 800px; /* limite de largura */
    color: #f0f0f0;
}

/* Título dentro do container */
.section-container h3 {
    margin-top: 0;
    text-align: center;
}

/* Botões vermelhos (Killer) */
.red-button {
    background-color: #ff5c57;
    color: #fff;
    border: none;
    border-radius: 4px;
    font-weight: bold;
    padding: 0.5rem 1rem;
    margin: 0.2rem;
    cursor: pointer;
}
.red-button:hover {
    background-color: #ff3c37;
}

/* Botões azuis (Survivor) */
.blue-button {
    background-color: #337ab7;
    color: #fff;
    border: none;
    border-radius: 4px;
    font-weight: bold;
    padding: 0.5rem 1rem;
    margin: 0.2rem;
    cursor: pointer;
}
.blue-button:hover {
    background-color: #285e8e;
}

/* Deixa o número de Escapes e Mortes maior */
.big-number {
    font-size: 2rem; /* aumenta para destacar */
    font-weight: bold;
    text-align: center;
    margin: 1rem 0;
    color: #ffd47e; /* cor “dourada” */
}

/* Tabela de desafios */
.custom-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 0.5rem;
}
.custom-table th, .custom-table td {
    border: 1px solid #444;
    padding: 0.5rem;
}
.custom-table th {
    background-color: #444;
}
.reroll-cell {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


# ---- LISTAS E DICIONÁRIOS ----

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

    # Extras
    "Charles Lee Ray (The Good Guy)": "https://via.placeholder.com/200?text=Charles+Lee+Ray",
    "Unknown (The Unknown)": "https://via.placeholder.com/200?text=Unknown",
    "Vecna (The Lich)": "https://via.placeholder.com/200?text=Vecna",
    "Dracula (The Dark Lord)": "https://via.placeholder.com/200?text=Dracula",
    "Portia Maye (The Houndmaster)": "https://via.placeholder.com/200?text=Portia+Maye"
}

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


# ---- FUNÇÕES DE SORTEIO ----

def sortear_desafios_killer(qtd=4):
    return random.sample(desafiosKiller, k=qtd)

def sortear_killer():
    return random.choice(killers)

def sortear_mortes():
    return random.randint(1, 4)

def sortear_desafios_survivors(qtd=4):
    return random.sample(desafiosSurvivors, k=qtd)

def sortear_escapes():
    return random.randint(1, 4)


# ---- SESSION STATE (para guardar os valores sorteados) ----
if "desafios_killer" not in st.session_state:
    st.session_state.desafios_killer = []
if "killer_sorteado" not in st.session_state:
    st.session_state.killer_sorteado = ""
if "mortes_sorteadas" not in st.session_state:
    st.session_state.mortes_sorteadas = 0

if "desafios_survivors" not in st.session_state:
    st.session_state.desafios_survivors = []
if "escapes_sorteados" not in st.session_state:
    st.session_state.escapes_sorteados = 0


# ---- TÍTULO ----
st.title("Sorteio Desafios Dead By Daylight")

# ---- TABS: Killer e Survivors ----
tab1, tab2 = st.tabs(["Killer", "Survivors"])

# ==============================================
# ================ ABA: KILLER ================
# ==============================================
with tab1:
    # Container principal para agrupar tudo
    with st.container():
        st.markdown("<div class='section-container'>", unsafe_allow_html=True)
        st.markdown("### Desafios (Killer)")

        # Botão para sortear DESAFIOS (apenas isso)
        # bugfix: só atualiza os desafios, não mexe no resto
        if st.button("Sortear Desafios (Killer)", key="btnDesafiosKiller", help="Sorteia apenas os desafios de Killer."):
            st.session_state.desafios_killer = sortear_desafios_killer()

        # Mostra os desafios em tabela, cada linha com Reroll
        if st.session_state.desafios_killer:
            st.write(f"Desafios sorteados ({len(st.session_state.desafios_killer)}):")
            # Cabeçalho
            st.markdown("<table class='custom-table'>", unsafe_allow_html=True)
            st.markdown("<thead><tr><th>Desafio</th><th>Reroll</th></tr></thead>", unsafe_allow_html=True)
            st.markdown("<tbody>", unsafe_allow_html=True)
            for i, desafio in enumerate(st.session_state.desafios_killer):
                # Montamos uma linha da tabela
                col_desafio = f"<td>{desafio}</td>"
                # Criamos um botão de reroll *por desafio*:
                # Para identificar cada button de reroll, usamos "key" único
                reroll_btn = st.button("Reroll", key=f"reroll_killer_{i}", help=f"Rerollar desafio {i+1}")
                if reroll_btn:
                    # Fazemos um re-sorteio individual
                    novo = random.choice([d for d in desafiosKiller if d not in st.session_state.desafios_killer])
                    st.session_state.desafios_killer[i] = novo
                    st.experimental_rerun()  # Recarrega a página para atualizar
                col_reroll = "<td class='reroll-cell'>Reroll_button_here</td>"
                # Vamos substituir esse placeholder por HTML mesmo
                st.markdown(f"<tr>{col_desafio}{col_reroll}</tr>", unsafe_allow_html=True)
            st.markdown("</tbody></table>", unsafe_allow_html=True)

            # Precisamos injetar o "botão" reroll no lugar do placeholder "Reroll_button_here", mas não é trivial em HTML
            # Então, acima, a gente usou st.button() e reexibimos a tabela a cada iteração. 
            # O "Reroll_button_here" é só um placeholder de layout.
        else:
            st.write("Nenhum desafio sorteado ainda.")

        st.markdown("</div>", unsafe_allow_html=True)

    # Container para killer e escapes lado a lado
    colKiller, colMortes = st.columns([1,1])

    with colKiller:
        st.markdown("<div class='section-container'>", unsafe_allow_html=True)
        st.markdown("### Sorteio de Killer")
        # Botão para sortear KILLER (apenas isso)
        if st.button("Sortear Killer", key="btnSortearKiller", help="Sorteia apenas o Killer"):
            st.session_state.killer_sorteado = sortear_killer()

        if st.session_state.killer_sorteado:
            st.write("**Killer Sorteado:**", st.session_state.killer_sorteado)
            if st.session_state.killer_sorteado in killerImages:
                st.image(killerImages[st.session_state.killer_sorteado], width=200)
        else:
            st.write("**Killer Sorteado:** –")

        st.markdown("</div>", unsafe_allow_html=True)

    with colMortes:
        st.markdown("<div class='section-container'>", unsafe_allow_html=True)
        st.markdown("### Mortes Necessárias")
        if st.button("Sortear Mortes", key="btnSortearMortes", help="Sorteia apenas as mortes necessárias (1 a 4)"):
            st.session_state.mortes_sorteadas = sortear_mortes()

        if st.session_state.mortes_sorteadas > 0:
            st.markdown(f"<div class='big-number'>{st.session_state.mortes_sorteadas}</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='big-number'>-</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    # Botão para "Sortear Tudo (Killer)" - Faz TUDO ao mesmo tempo
    with st.container():
        st.markdown("<div class='section-container' style='text-align:center;'>", unsafe_allow_html=True)
        if st.button("Sortear Tudo (Killer)", key="btnSortearTudoKiller", help="Sorteia desafios, killer e mortes"):
            st.session_state.desafios_killer = sortear_desafios_killer()
            st.session_state.killer_sorteado = sortear_killer()
            st.session_state.mortes_sorteadas = sortear_mortes()
            st.success("Tudo sorteado com sucesso!")
        st.markdown("</div>", unsafe_allow_html=True)


# ==============================================
# ============== ABA: SURVIVORS ===============
# ==============================================
with tab2:
    # Container para Desafios e Escapes lado a lado
    colDesafios, colEscapes = st.columns([1,1])

    with colDesafios:
        st.markdown("<div class='section-container'>", unsafe_allow_html=True)
        st.markdown("### Desafios (Survivors)")
        
        # Botão para sortear DESAFIOS (apenas isso)
        if st.button("Sortear Desafios (Survivors)", key="btnDesafiosSurvivors"):
            st.session_state.desafios_survivors = sortear_desafios_survivors()

        # Exibe a tabela de desafios + reroll
        if st.session_state.desafios_survivors:
            st.write(f"Desafios sorteados ({len(st.session_state.desafios_survivors)}):")
            st.markdown("<table class='custom-table'>", unsafe_allow_html=True)
            st.markdown("<thead><tr><th>Desafio</th><th>Reroll</th></tr></thead>", unsafe_allow_html=True)
            st.markdown("<tbody>", unsafe_allow_html=True)
            for i, d in enumerate(st.session_state.desafios_survivors):
                col_desafio = f"<td>{d}</td>"
                reroll_btn = st.button("Reroll", key=f"reroll_surv_{i}", help=f"Rerollar desafio {i+1}")
                if reroll_btn:
                    novo = random.choice([x for x in desafiosSurvivors if x not in st.session_state.desafios_survivors])
                    st.session_state.desafios_survivors[i] = novo
                    st.experimental_rerun()
                col_reroll = "<td class='reroll-cell'>Reroll_button_here</td>"
                st.markdown(f"<tr>{col_desafio}{col_reroll}</tr>", unsafe_allow_html=True)
            st.markdown("</tbody></table>", unsafe_allow_html=True)
        else:
            st.write("Nenhum desafio sorteado ainda.")

        st.markdown("</div>", unsafe_allow_html=True)

    with colEscapes:
        st.markdown("<div class='section-container'>", unsafe_allow_html=True)
        st.markdown("### Escapes Necessários")
        if st.button("Sortear Escapes", key="btnSortearEscapes"):
            st.session_state.escapes_sorteados = sortear_escapes()

        if st.session_state.escapes_sorteados > 0:
            st.markdown(f"<div class='big-number'>{st.session_state.escapes_sorteados}</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='big-number'>-</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    # Botão para "Sortear Tudo (Survivors)"
    with st.container():
        st.markdown("<div class='section-container' style='text-align:center;'>", unsafe_allow_html=True)
        if st.button("Sortear Tudo (Survivors)", key="btnSortearTudoSurvivors", help="Sorteia desafios e escapes"):
            st.session_state.desafios_survivors = sortear_desafios_survivors()
            st.session_state.escapes_sorteados = sortear_escapes()
            st.success("Tudo sorteado com sucesso!")
        st.markdown("</div>", unsafe_allow_html=True)


# ---- FOOTER ----
st.write("---")
st.caption("Feito por Sinnex - @lucianosnx")
