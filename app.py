import streamlit as st
import random

#####################################
# Configurações Básicas do Streamlit
#####################################
st.set_page_config(
    page_title="Sorteio Desafios Dead By Daylight",
    layout="wide"
)

#########################################
# CSS personalizado para deixar mais bonito
#########################################
# Observação: Esse CSS deixa as Tabs mais evidentes e estiliza botões e caixas.
# Você pode ajustar as cores conforme desejar.
custom_css = """
<style>
/* Deixa as tabs maiores e destacadas */
[data-baseweb="tabs"] .stTabs [role="tablist"] {
    border-bottom: 3px solid #777;
}
[data-baseweb="tabs"] .stTabs [role="tab"] {
    font-size: 1.1rem;
    padding: 10px 20px;
    margin-right: 5px;
    border-radius: 8px 8px 0 0;
    border: 1px solid #777;
    background-color: #333;
    color: #fff;
}
[data-baseweb="tabs"] .stTabs [role="tab"][aria-selected="true"] {
    background-color: #555;
    border-bottom: 3px solid #f00; /* Borda inferior vermelha ao selecionado */
    color: #fff;
}

/* Botão padrão do Streamlit com cor e borda customizadas */
div.stButton > button {
    background-color: #555 !important;
    color: #fff !important;
    border: 1px solid #888 !important;
    border-radius: 5px !important;
    padding: 0.4em 1em !important;
    font-weight: bold !important;
    cursor: pointer !important;
}

/* Hover no botão */
div.stButton > button:hover {
    background-color: #666 !important;
    border-color: #999 !important;
}

/* Caixa 'vermelha' para Killer */
.killer-box {
    background-color: #2c1414;
    padding: 20px;
    border: 2px solid #ff3c37;
    border-radius: 8px;
}

/* Caixa 'azul' para Survivors */
.surv-box {
    background-color: #1b2b3a;
    padding: 20px;
    border: 2px solid #285e8e;
    border-radius: 8px;
}

/* Título da caixa killer */
.killer-title {
    color: #ff5c57;
    margin-bottom: 10px;
}

/* Título da caixa survivor */
.surv-title {
    color: #337ab7;
    margin-bottom: 10px;
}

/* Para deixar os números (Kills/Escapes) maiores */
.big-number {
    font-size: 2rem;
    font-weight: bold;
    color: #fff;
}

/* Para dar espaço entre blocos */
.block-space {
    margin-top: 20px;
}

/* Ajustar tabela */
table {
    width: 100%;
    border-collapse: collapse;
}
table thead tr {
    background-color: #444;
}
table th, table td {
    padding: 6px 8px;
    border: 1px solid #777;
}
table th {
    color: #fff;
    text-align: left;
}
table td {
    color: #eee;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

#############################################
# LISTAS DE DESAFIOS, KILLERS E FUNÇÕES ÚTEIS
#############################################

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
    # Placeholders
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

# Funções
def sortear_desafios_killer(qtd=4):
    return random.sample(desafiosKiller, k=qtd)

def reRoll_desafio_killer(index):
    """Rerolla UM desafio para killer no índice indicado, garantindo que seja diferente do atual."""
    possiveis = set(desafiosKiller) - set(st.session_state.desafios_killer)
    if not possiveis:
        # Se não tiver mais o que sortear, retorna o mesmo
        return st.session_state.desafios_killer[index]
    return random.choice(list(possiveis))

def sortear_killer():
    return random.choice(killers)

def sortear_mortes():
    return random.randint(1, 4)

def sortear_desafios_survivors(qtd=4):
    return random.sample(desafiosSurvivors, k=qtd)

def reRoll_desafio_survivor(index):
    """Rerolla UM desafio para survivor no índice indicado."""
    possiveis = set(desafiosSurvivors) - set(st.session_state.desafios_survivors)
    if not possiveis:
        return st.session_state.desafios_survivors[index]
    return random.choice(list(possiveis))

def sortear_escapes():
    return random.randint(1, 4)

#############################################################
# Sessão: Armazenamos as variáveis sorteadas no session_state
#############################################################
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

###################################
# Layout do App
###################################
st.title("Sorteio Desafios Dead By Daylight")

# Criamos duas abas mais evidentes
tab_killer, tab_survivor = st.tabs(["Killer", "Survivors"])

###################################
# ABA KILLER
###################################
with tab_killer:
    # Título grande vermelho
    st.markdown("<h2 style='text-align:center; color:#ff3c37;'>Killer</h2>", unsafe_allow_html=True)
    
    # Linha superior: (desafios) | (killer sorteado)
    col_desafios_k, col_killer = st.columns([1,1])

    with col_desafios_k:
        st.markdown("<div class='killer-box'>", unsafe_allow_html=True)
        st.markdown("<h4 class='killer-title'>Desafios (Killer)</h4>", unsafe_allow_html=True)

        # Botão para sortear 4 desafios
        if st.button("Sortear 4 Desafios (Killer)", key="sortear_desafios_killer"):
            st.session_state.desafios_killer = sortear_desafios_killer()

        # Exibir em forma de tabela + botões de reroll
        if st.session_state.desafios_killer:
            st.markdown("<table>", unsafe_allow_html=True)
            st.markdown("<thead><tr><th>Desafio</th><th>Reroll</th></tr></thead>", unsafe_allow_html=True)
            st.markdown("<tbody>", unsafe_allow_html=True)
            
            for i, d in enumerate(st.session_state.desafios_killer):
                # Cada linha da tabela
                col_d = d
                # Botão ↩ (reroll)
                reroll_button = f"<button style='background-color:#ff5c57;color:#fff;border:none;border-radius:4px;padding:5px 10px;cursor:pointer;'>↩</button>"
                
                # Montamos a linha como HTML, mas para acionar reroll, precisamos do st.button
                # Então vamos usar technique: Tabela "visual" + st.button ao lado
                st.markdown(f"<tr><td>{col_d}</td><td>", unsafe_allow_html=True)
                # Botão de reroll
                # Precisamos do "mesmo" local para exibir, mas st.button() não funciona dentro do markdown.
                # Faremos a approach de "inline button" usando colunas do Streamlit mesmo.
                
                # Para simplificar, fechamos a tag aqui:
                st.markdown("</td></tr>", unsafe_allow_html=True)
                
                # Agora, criamos UM row com colunas invisíveis (só para o button):
                # Mas exibir a tabela e os botões juntos é mais complexo no Streamlit.
                # Em vez disso, vamos "fingir" uma tabela com st.columns a cada item:
                
                # => Nova abordagem: Encerrar a tabela, criar a row e reabrir a tabela (ou exibir a tabela via for).
                
            st.markdown("</tbody></table>", unsafe_allow_html=True)

            # Precisamos realmente de reroll em cada item com um button Streamlit:
            # Vamos criar outro FOR (fora do HTML) para exibir botões inline:
            for i, d in enumerate(st.session_state.desafios_killer):
                # Uma linha "invisível" (pode ser comentada ou deixada)
                c1, c2 = st.columns([9,1])
                c1.write(f"**{i+1})** {d}")
                if c2.button("↩", key=f"reroll_killer_{i}"):
                    # Reroll
                    st.session_state.desafios_killer[i] = reRoll_desafio_killer(i)
                    st.experimental_rerun()

        st.markdown("</div>", unsafe_allow_html=True)  # fim killer-box


    with col_killer:
        st.markdown("<div class='killer-box'>", unsafe_allow_html=True)
        st.markdown("<h4 class='killer-title'>Killer Sorteado</h4>", unsafe_allow_html=True)

        # Botão para sortear Killer
        if st.button("Sortear Killer", key="botao_killer"):
            st.session_state.killer_sorteado = sortear_killer()

        if st.session_state.killer_sorteado:
            st.write(f"**{st.session_state.killer_sorteado}**")
            if st.session_state.killer_sorteado in killerImages:
                st.image(killerImages[st.session_state.killer_sorteado], width=200)
        else:
            st.write("_Nenhum Killer sorteado ainda_")

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='block-space'></div>", unsafe_allow_html=True)

    # Abaixo, container de 'Mortes Necessárias'
    with st.container():
        st.markdown("<div class='killer-box'>", unsafe_allow_html=True)
        st.markdown("<h4 class='killer-title'>Mortes Necessárias (1 a 4)</h4>", unsafe_allow_html=True)

        if st.button("Sortear Mortes", key="botao_mortes"):
            st.session_state.mortes_sorteadas = sortear_mortes()

        if st.session_state.mortes_sorteadas > 0:
            st.markdown(f"<p class='big-number'>{st.session_state.mortes_sorteadas}</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p class='big-number'>-</p>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='block-space'></div>", unsafe_allow_html=True)

    # Botão "Sortear Tudo (Killer)"
    st.markdown("<div class='killer-box'>", unsafe_allow_html=True)
    if st.button("Sortear Tudo (Killer)", key="botao_tudo_killer"):
        st.session_state.desafios_killer = sortear_desafios_killer()
        st.session_state.killer_sorteado = sortear_killer()
        st.session_state.mortes_sorteadas = sortear_mortes()
        st.success("Tudo (Killer) sorteado com sucesso!")
    st.markdown("</div>", unsafe_allow_html=True)


###################################
# ABA SURVIVORS
###################################
with tab_survivor:
    # Título grande azul
    st.markdown("<h2 style='text-align:center; color:#337ab7;'>Survivors</h2>", unsafe_allow_html=True)

    # Linha superior: (desafios) | (escapes)
    col_desafios_s, col_escapes = st.columns([1,1])

    with col_desafios_s:
        st.markdown("<div class='surv-box'>", unsafe_allow_html=True)
        st.markdown("<h4 class='surv-title'>Desafios (Survivors)</h4>", unsafe_allow_html=True)

        # Botão para sortear 4 desafios
        if st.button("Sortear 4 Desafios (Survivors)", key="sortear_desafios_surv"):
            st.session_state.desafios_survivors = sortear_desafios_survivors()

        # Exibir + reroll
        if st.session_state.desafios_survivors:
            st.markdown("<table>", unsafe_allow_html=True)
            st.markdown("<thead><tr><th>Desafio</th><th>Reroll</th></tr></thead>", unsafe_allow_html=True)
            st.markdown("<tbody>", unsafe_allow_html=True)
            st.markdown("</tbody></table>", unsafe_allow_html=True)

            for i, d in enumerate(st.session_state.desafios_survivors):
                c1, c2 = st.columns([9,1])
                c1.write(f"**{i+1})** {d}")
                if c2.button("↩", key=f"reroll_surv_{i}"):
                    st.session_state.desafios_survivors[i] = reRoll_desafio_survivor(i)
                    st.experimental_rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    with col_escapes:
        st.markdown("<div class='surv-box'>", unsafe_allow_html=True)
        st.markdown("<h4 class='surv-title'>Escapes Necessários (1 a 4)</h4>", unsafe_allow_html=True)

        if st.button("Sortear Escapes", key="botao_escapes"):
            st.session_state.escapes_sorteados = sortear_escapes()

        if st.session_state.escapes_sorteados > 0:
            st.markdown(f"<p class='big-number'>{st.session_state.escapes_sorteados}</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p class='big-number'>-</p>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='block-space'></div>", unsafe_allow_html=True)

    # Botão "Sortear Tudo (Survivors)"
    st.markdown("<div class='surv-box'>", unsafe_allow_html=True)
    if st.button("Sortear Tudo (Survivors)", key="botao_tudo_surv"):
        st.session_state.desafios_survivors = sortear_desafios_survivors()
        st.session_state.escapes_sorteados = sortear_escapes()
        st.success("Tudo (Survivors) sorteado com sucesso!")
    st.markdown("</div>", unsafe_allow_html=True)

###################################
# Rodapé
###################################
st.write("---")
st.caption("Feito por Sinnex - @lucianosnx")
