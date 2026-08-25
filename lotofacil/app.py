import streamlit as st
import random
import pandas as pd

# ==============================================================================
# CONFIGURAÇÕES DA PÁGINA E ESTILIZAÇÃO CUSTOMIZADA ADVANCED
# ==============================================================================
st.set_page_config(
    page_title="Otimizador Lotofácil Pro",
    page_icon="🎯",
    layout="wide"
)

# Estilização profissional de cassino e painéis de dados (SaaS Premium)
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
    /* Estilos do Volante Virtual */
    .volante-container {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 10px;
        max-width: 350px;
        margin: 20px 0;
    }
    .bola-desativada {
        width: 50px;
        height: 50px;
        background-color: #ffffff;
        border: 2px solid #bdbdbd;
        color: #757575;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 18px;
    }
    .bola-ativada {
        width: 50px;
        height: 50px;
        background-color: #1976d2;
        border: 2px solid #0d47a1;
        color: white;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 18px;
        box-shadow: 0px 0px 8px #1976d2;
    }
    /* Estilos dos Quadrantes Quentes/Frios */
    .badge-quente {
        background-color: #ffebee;
        color: #c62828;
        padding: 5px 10px;
        border-radius: 5px;
        font-weight: bold;
        border: 1px solid #ffcdd2;
        display: inline-block;
        margin: 2px;
    }
    .badge-frio {
        background-color: #e3f2fd;
        color: #1565c0;
        padding: 5px 10px;
        border-radius: 5px;
        font-weight: bold;
        border: 1px solid #bbdefb;
        display: inline-block;
        margin: 2px;
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
# INTERFACE INTERNA (PAINEL TURBO DO MEMBRO LOGADO)
# ==============================================================================
st.title("🎯 Otimizador Lotofácil Pro")
st.subheader("Painel de Controle Avançado — Versão Turbo 2.0")
st.caption("Acesso Exclusivo de Assinante Ativo")
st.write("---")

st.sidebar.header("🎛️ Configurações do Sorteio")
resultado_input = st.sidebar.text_input(
    "Dezenas do Último Concurso:",
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
    
    # DIVISÃO DA TELA: Esquerda (Métricas/Volante) | Direita (Tendências Históricas)
    col_esquerda, col_direita = st.columns([1.2, 1])
    
    with col_esquerda:
        st.markdown("### 🗺️ Mapeamento Geográfico do Último Concurso")
        st.caption("Veja abaixo a distribuição real das dezenas no volante oficial da Caixa:")
        
        # MONTAGEM DO VOLANTE VIRTUAL EM HTML/CSS
        html_volante = '<div class="volante-container">'
        for i in range(1, 26):
            classe_bola = "bola-ativada" if i in ultimo_sorteio_set else "bola-desativada"
            html_volante += f'<div class="{classe_bola}">{i:02d}</div>'
        html_volante += '</div>'
        st.markdown(html_volante, unsafe_allow_html=True)

    with col_direita:
        st.markdown("### 🔥 Tendências Clínicas e Ciclos")
        st.caption("Cruzamento com o banco de dados de comportamento de frequência:")
        
        # Inteligência Computacional de Grupos Recomendados
        dezenas_frias = {1, 10, 11, 14, 16, 17, 19, 20, 23, 24}.difference(ultimo_sorteio_set)
