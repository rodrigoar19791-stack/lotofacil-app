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

# Customização visual leve para deixar o app com cara de software SaaS moderno
st.markdown("""
    <style>
    .metric-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        border-left: 5px solid #2e7d32;
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
        padding: 12px 24px;
        text-align: center;
        text-decoration: none;
        font-size: 16px;
        font-weight: bold;
        border-radius: 5px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# SISTEMA DE SEGURANÇA E TELA DE LOGIN (BARREIRA DE MONETIZAÇÃO)
# ==============================================================================
SENHA_CORRETA = "LOTO2026"

if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.markdown("### 🔒 Acesso Restrito — Área Exclusiva de Assinantes")
    st.write("O **Otimizador Lotofácil Pro** é um otimizador estatístico avançado de alta precisão.")
    
    col_login_1, col_login_2 = st.columns(2)
    
    with col_login_1:
        st.markdown("#### Já é um Membro?")
        senha_digitada = st.text_input("Digite sua senha de acesso ativa:", type="password")
        if st.button("Destravar Otimizador", type="primary"):
            if senha_digitada == SENHA_CORRETA:
                st.session_state.autenticado = True
                st.success("Acesso autorizado! Carregando o sistema...")
                st.rerun()
            else:
                st.error("Senha incorreta. Verifique o código enviado no seu e-mail de compra.")
                
    with col_login_2:
        st.markdown("#### Não tem uma senha?")
        st.write("Ative seu acesso instantâneo via PIX para liberar o gerador inteligente agora mesmo por um custo simbólico:")
        
        # ⚠️ SUBSTITUA O LINK ABAIXO PELO SEU LINK DE CHECKOUT COPIADO DA KIWIFY ⚠️
        link_kiwify = "https://kiwify.com.br" 
        
        st.markdown(f'<a href="{link_kiwify}" target="_blank" class="btn-compra">⚡ Quero Acesso por R$ 9,90</a>', unsafe_allow_html=True)
        st.caption("Garantia total de 7 dias protegida por lei.")
        
    st.stop()

# ==============================================================================
# BASE DE DADOS MATEMÁTICA (REGRAS ESTÁTICAS)
# ==============================================================================
NUMEROS_PRIMOS = {2, 3, 5, 7, 11, 13, 17, 19, 23}
MOLDURA = {1, 2, 3, 4, 5, 6, 10, 11, 15, 16, 20, 21, 22, 23, 24, 25}

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
    while len(jogos_gerados) < qtde_9_repetidas and tentatives < 5000:
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
# INTERFACE DO USUÁRIO (FRONT-END)
# ==============================================================================
st.title("🎯 Otimizador Lotofácil Pro")
st.subheader("Análise Estatística Avançada")
st.caption("Acesso Exclusivo de Assinantes")
st.write("---")

st.sidebar.header("🎛️ Painel de Controle")
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
        st.markdown(f'<div class="metric-card"><h4>Pares vs Ímpares</h4><p style="font-size: 24px; font-weight: bold; color: #2e7d32;">{u_impares}Í / {u_pares}P</p><small>Padrão: 8Í/7P ou 7Í/8P</small></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card"><h4>Números Primos</h4><p style="font-size: 24px; font-weight: bold; color: #2e7d32;">{u_primos} dezenas</p><small>Padrão: 5 ou 6 primos</small></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-card"><h4>Moldura (Bordas)</h4><p style="font-size: 24px; font-weight: bold; color: #2e7d32;">{u_moldura} dezenas</p><small>Padrão: 9 ou 10 na borda</small></div>', unsafe_allow_html=True)

    st.write("---")
    st.markdown("### 🎲 Gerador Construtivo de Alta Probabilidade")
    
    if 'jogos_armazenados' not in st.session_state:
        st.session_state.jogos_armazenados = None

    if st.button("⚡ Gerar Combinações Otimizadas", type="primary"):
        with st.spinner("Cruzando dados..."):
            st.session_state.jogos_armazenados = gerar_jogos_estrategicos(quantidade_total=quantidade_jogos, ultimo_sorteio=ultimo_sorteio_set)
            
    if st.session_state.jogos_armazenados:
        jogos = st.session_state.jogos_armazenados
        st.success(f"Sucesso! {len(jogos)} jogos gerados e prontos para exportação.")
        
        col_jogos_1, col_jogos_2 = st.columns(2)
        for idx, jogo in enumerate(jogos, 1):
            jogo_formatado = " - ".join(f"{n:02d}" for n in jogo)
            if idx <= (len(jogos) / 2):
                with col_jogos_1:
                    st.markdown(f'**Bilhete {idx:02d}:**')
                    st.markdown(f'<div class="game-box">{jogo_formatado}</div>', unsafe_allow_html=True)
            else:
                with col_jogos_2:
                    st.markdown(f'**Bilhete {idx:02d}:**')
                    st.markdown(f'<div class="game-box">{jogo_formatado}</div>', unsafe_allow_html=True)
        
        st.write("---")
        st.markdown("### 📥 Baixar Jogos Otimizados")
        
        texto_txt = ""
        for idx, jogo in enumerate(jogos, 1):
            texto_txt += f"Jogo {idx:02d}: " + " - ".join(f"{n:02d}" for n in jogo) + "\n"
            
        colunas_csv = [f"Dezena_{i}" for i in range(1, 16)]
        df_jogos = pd.DataFrame(jogos, columns=colunas_csv)
        df_jogos.index = [f"Jogo {i:02d}" for i in range(1, len(jogos) + 1)]
        dados_csv = df_jogos.to_csv().encode('utf-8')
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            st.download_button(label="📄 Baixar em Texto (.txt)", data=texto_txt, file_name="jogos_lotofacil.txt", mime="text/plain", use_container_width=True)
        with col_btn2:
            st.download_button(label="📊 Baixar em Planilha (.csv)", data=dados_csv, file_name="jogos_lotofacil.csv", mime="text/csv", use_container_width=True)
else:
    st.warning("⚠️ Aguardando digitação de 15 dezenas válidas.")
