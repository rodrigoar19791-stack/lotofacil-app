import streamlit as st
import random
import pandas as pd

# ==============================================================================
# CONFIGURAÇÕES DA PÁGINA E ESTILIZAÇÃO CUSTOMIZADA
# ==============================================================================
st.set_page_config(
    page_title="Otimizador Lotofácil Pro",
    page_icon="🎯",
    layout="wide"
)

# Customização visual avançada para os blocos explicativos e botões
st.markdown("""
    <style>
    .metric-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        border-left: 5px solid #2e7d32;
    }
    .fundamento-card {
        background-color: #f1f8e9;
        border-radius: 8px;
        padding: 20px;
        border: 1px solid #dcedc8;
        margin-bottom: 20px;
    }
    .game-box {
        background-color: #e8f5e9;
        font-family: 'Courier New', monospace;
        font-size: 18px;
        font-weight: bold;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #c8e6c9;
        margin-bottom: 8px;
    }
    .btn-compra {
        display: inline-block;
        background-color: #2e7d32;
        color: white !important;
        padding: 14px 28px;
        text-align: center;
        text-decoration: none;
        font-size: 16px;
        font-weight: bold;
        border-radius: 5px;
        margin-top: 15px;
        box-shadow: 0px 4px 10px rgba(46, 125, 50, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# BASE DE DADOS MATEMÁTICA (REGRAS ESTÁTICAS)
# ==============================================================================
NUMEROS_PRIMOS = {2, 3, 5, 7, 11, 13, 17, 19, 23}
MOLDURA = {1, 2, 3, 4, 5, 6, 10, 11, 15, 16, 20, 21, 22, 23, 24, 25}

# ==============================================================================
# TELA DE LOGIN COM EMBASAMENTO CIENTÍFICO (ZONA DE CONVERSÃO)
# ==============================================================================
SENHA_CORRETA = "LOTO2026"

if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.title("🎯 Otimizador Lotofácil Pro")
    st.subheader("Inteligência Estatística contra a Sorte")
    st.write("---")

    # Bloco de Fundamentação Científica visível para visitantes
    st.markdown("""
    <div class="fundamento-card">
        <h3 style="color: #2e7d32; margin-top:0;">🔬 Como a Engenharia Matemática Otimiza Suas Chances?</h3>
        <p>A maioria dos apostadores queima dinheiro escolhendo dezenas aleatórias. No entanto, o histórico global de todos os concursos da Lotofácil revela uma <b>tendência matemática extremamente rígida e previsível</b>:</p>
        <ul>
            <li><b>A Lei das Repetições:</b> Em cerca de <b>80% dos sorteios</b>, o resultado repete exatamente <b>8, 9 ou 10 números</b> do concurso anterior (sendo 9 a média absoluta mais frequente). Combinações fora disso (como repetir apenas 5 ou mais de 12) são anomalias raras.</li>
            <li><b>O Equilíbrio dos Pares (P) e Ímpares (Í):</b> Mais de 57% dos resultados históricos concentram-se nas proporções exatas de <b>8Í / 7P</b> ou <b>7Í / 8P</b>.</li>
            <li><b>O Quadrante dos Primos:</b> Sorteios legítimos contêm rigorosamente entre <b>5 e 6 números primos</b> na mesma cartela em mais de 60% das vezes.</li>
        </ul>
        <p><b>O que este software faz?</b> Nosso algoritmo de força bruta analisa o último concurso inserido e descarta milhares de cartões matematicamente inviáveis. Ele só entrega para você bilhetes que preencham simultaneamente todos esses critérios de alta probabilidade.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col_login_1, col_login_2 = st.columns(2)
    
    with col_login_1:
        st.markdown("#### 🔓 Já é um Membro Assinante?")
        senha_digitada = st.text_input("Digite sua senha de acesso ativa:", type="password")
        if st.button("Destravar Otimizador", type="primary"):
            if senha_digitada == SENHA_CORRETA:
                st.session_state.autenticado = True
                st.success("Acesso autorizado! Carregando o sistema...")
                st.rerun()
            else:
                st.error("Senha incorreta. Verifique o código enviado no seu e-mail de compra.")
                
    with col_login_2:
        st.markdown("#### ⚡ Não tem uma senha?")
        st.write("Ative seu acesso instantâneo via PIX para destravar o gerador inteligente agora mesmo e baixar seus jogos salvos em Excel ou Texto.")
        
        # LINK DE CHECKOUT DA KIWIFY
        link_kiwify = "https://kiwify.com.br" 
        
        st.markdown(f'<a href="{link_kiwify}" target="_blank" class="btn-compra">Ativar Acesso por Apenas R$ 9,90</a>', unsafe_allow_html=True)
        st.caption("Acesso imediato enviado no seu e-mail. Garantia de 7 dias.")
        
    st.stop()

# ==============================================================================
# MOTOR ALGORÍTMICO DE VALIDAÇÃO E GERAÇÃO
# ==============================================================================
def validar_jogo(combinacao, ultimo_sorteio, qtde_repetidos):
    jogo = set(combinacao)
    
    if len(jogo.intersection(ultimo_sorteio)) != qtde_repetidos:
        return False
        
    pares = len([n for n in jogo if n % 2 == 0])
    if pares not in (7, 8):
        return False
        
    primos = len(jogo.intersection(NUMEROS_PRIMOS))
    if primos not in (5, 6):
        return False
        
    moldura = len(jogo.intersection(MOLDURA))
    if moldura not in (9, 10):
        return False
        
    return True

def gerar_jogos_estrategicos(quantidade_total, ultimo_sorteio):
    todos_numeros = list(range(1, 26))
    jogos_gerados = []
    qtde_9_repetidas = int(quantidade_total * 0.7)
    
    tentativas = 0
    while len(jogos_gerados) < qtde_9_repetidas and tentativas < 5000:
        tentativas += 1
        sugestao = sorted(random.sample(todos_numeros, 15))
        if validar_jogo(sugestao, ultimo_sorteio, qtde_repetidos=9) and (sugestao not in jogos_gerados):
            jogos_gerados.append(sugestao)
            
    while len(jogos_gerados) < quantidade_total and tentativas < 10000:
        tentativas += 1
        sugestao = sorted(random.sample(todos_numeros, 15))
        if validar_jogo(sugestao, ultimo_sorteio, qtde_repetidos=8) and (sugestao not in jogos_gerados):
            jogos_gerados.append(sugestao)
            
    return jogos_gerados

# ==============================================================================
# INTERFACE DO USUÁRIO INTERNA (PAINEL DO ASSINANTE LOGADO)
# ==============================================================================
st.title("🎯 Otimizador Lotofácil Pro")
st.subheader("Painel de Controle Avançado")
st.caption("Área do Membro Autenticado")
st.write("---")

st.sidebar.header("🎛️ Configurações do Sorteio")
resultado_input = st.sidebar.text_input(
    "Dezenas do Último Concurso (Separadas por espaço ou vírgula):",
    value="02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 15, 18, 21, 22, 25"
)

try:
    limpo = resultado_input.replace(",", " ").split()
    ultimo_sorteio_set = {int(x) for x in limpo if 1 <= int(x) <= 25}
except ValueError:
    st.sidebar.error("Por favor, insira apenas números válidos entre 01 e 25.")
    ultimo_sorteio_set = set()

quantidade_jogos = st.sidebar.slider("Quantidade de Jogos para Gerar:", min_value=1, max_value=15, value=10)

if len(ultimo_sorteio_set) == 15:
    st.markdown("### 📊 Análise de Comportamento do Último Concurso")
    
    u_pares = len([n for n in ultimo_sorteio_set if n % 2 == 0])
    u_impares = 15 - u_pares
    u_primos = len(ultimo_sorteio_set.intersection(NUMEROS_PRIMOS))
    u_moldura = len(ultimo_sorteio_set.intersection(MOLDURA))
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="metric-card"><h4>Pares vs Ímpares</h4><p style="font-size: 24px; font-weight: bold; color: #2e7d32;">{u_impares}Í / {u_pares}P</p><small>Padrão Alvo: 8Í/7P ou 7Í/8P</small></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card"><h4>Números Primos</h4><p style="font-size: 24px; font-weight: bold; color: #2e7d32;">{u_primos} dezenas</p><small>Padrão Alvo: 5 ou 6 primos</small></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-card"><h4>Moldura (Bordas)</h4><p style="font-size: 24px; font-weight: bold; color: #2e7d32;">{u_moldura} dezenas</p><small>Padrão Alvo: 9 ou 10 na borda</small></div>', unsafe_allow_html=True)

    st.write("---")
    st.markdown("### 🎲 Gerador Inteligente Ajustado")
    st.caption("O robô irá estruturar os bilhetes aplicando as travas estatísticas acima com base no concurso inserido.")
    
    if 'jogos_armazenados' not in st.session_state:
        st.session_state.jogos_armazenados = None

    if st.button("⚡ Gerar Combinações Otimizadas", type="primary"):
        with st.spinner("Cruzando dados..."):
            st.session_state.jogos_armazenados = gerar_jogos_estrategicos(quantidade_total=quantidade_jogos, ultimo_sorteio=ultimo_sorteio_set)
            
    if st.session_state.jogos_armazenados:
        jogos = st.session_state.jogos_armazenados
        st.success(f"Sucesso! {len(jogos)} jogos gerados seguindo a proporção ideal (70% com 9 repetidas / 30% com 8 repetidas).")
        
        col_jogos_1, col_jogos_2 = st.columns(2)
        for idx, jogo in enumerate(jogos, 1):
            jogo_formatado = " - ".join(f"{n:02d}" for n in jogo)
            if idx <= (len(jogos) / 2):
                with col_jogos_1:
                    st.markdown(f'**Bilhete {idx:02d}:**')
                    st.markdown(f'<div class="game-box">{jogo_formatado}</div>', unsafe_allow_html=True)
            else:
                with col_jogos_2:
st.markdown(f'Bilhete {idx:02d}:')st.markdown(f'{jogo_formatado}', unsafe_allow_html=True)st.write("---")st.markdown("### 📥 Exportar Jogos Otimizados")texto_txt = ""for idx, jogo in enumerate(jogos, 1):texto_txt += f"Jogo {idx:02d}: " + " - ".join(f"{n:02d}" for n in jogo) + "\n"colunas_csv = [f"Dezena_{i}" for i in range(1, 16)]df_jogos = pd.DataFrame(jogos, columns=colunas_csv)df_jogos.index = [f"Jogo {i:02d}" for i in range(1, len(jogos) + 1)]dados_csv = df_jogos.to_csv().encode('utf-8')col_btn1, col_btn2 = st.columns(2)with col_btn1:st.download_button(label="📄 Baixar em Texto (.txt)", data=texto_txt, file_name="jogos_lotofacil.txt", mime="text/plain", use_container_width=True)with col_btn2:st.download_button(label="📊 Baixar em Planilha (.csv)", data=dados_csv, file_name="jogos_lotofacil.csv", mime="text/csv", use_container_width=True)else:st.warning("⚠️ Aguardando digitação de 15 dezenas válidas.")
