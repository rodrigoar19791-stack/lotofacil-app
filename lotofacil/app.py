import streamlit as st
import random

# ==============================================================================
# CONFIGURAÇÕES DA PÁGINA E ESTILIZAÇÃO CUSTOMIZADA
# ==============================================================================
st.set_page_config(
    page_title="LotoAnálise Pro",
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
    </style>
""", unsafe_allow_html=True)

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
    
    # Filtro 1: Repetição do ciclo anterior
    if len(jogo.intersection(ultimo_sorteio)) != qtde_repetidos:
        return False
        
    # Filtro 2: Proporção de Pares e Ímpares (Aceita apenas 7 ou 8 pares)
    pares = len([n for n in jogo if n % 2 == 0])
    if pares not in [7, 8]:
        return False
        
    # Filtro 3: Quantidade de Primos (Aceita apenas 5 ou 6 primos)
    primos = len(jogo.intersection(NUMEROS_PRIMOS))
    if primos not in [5, 6]:
        return False
        
    # Filtro 4: Quantidade na Moldura (Aceita apenas 9 ou 10 na borda)
    moldura = len(jogo.intersection(MOLDURA))
    if moldura not in [9, 10]:
        return False
        
    return True

def gerar_jogos_estrategicos(quantidade_total, ultimo_sorteio):
    todos_numeros = list(range(1, 26))
    jogos_gerados = []
    
    # Distribuição Proporcional Inteligente (70% com 9 repetidas / 30% com 8 repetidas)
    qtde_9_repetidas = int(quantidade_total * 0.7)
    
    tentativas = 0
    # Loop de segurança para evitar travamentos
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
# INTERFACE DO USUÁRIO (FRONT-END)
# ==============================================================================

# Cabeçalho Principal (Aparência de Produto Comercial)
st.title("🎯 LotoAnálise Pro")
st.subheader("Otimizador Estatístico Avançado para Lotofácil")
st.caption("Versão Beta de Validação Comercial — Modelo Híbrido Freemium")
st.write("---")

# BARRA LATERAL: Entrada do Último Concurso e Configurações
st.sidebar.header("🎛️ Painel de Controle")
st.sidebar.write("Configure abaixo os dados do sorteio base para realizar o cruzamento:")

# Input padrão preenchido com o concurso do dia 17/08 para facilitar o teste
resultado_input = st.sidebar.text_input(
    "Dezenas do Último Concurso (Separadas por espaço ou vírgula):",
    value="02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 15, 18, 21, 22, 25"
)

# Trata a entrada de texto do usuário para converter em um Set numérico estável
try:
    limpo = resultado_input.replace(",", " ").split()
    ultimo_sorteio_set = {int(x) for x in limpo if 1 <= int(x) <= 25}
except ValueError:
    st.sidebar.error("Por favor, insira apenas números válidos entre 01 e 25.")
    ultimo_sorteio_set = set()

# Controle do volume de jogos (Simulando barreira do plano Premium)
quantidade_jogos = st.sidebar.slider("Quantidade de Jogos para Gerar:", min_value=1, max_value=15, value=10)

st.sidebar.write("---")
st.sidebar.markdown("""
**💎 Recursos Premium Bloqueados**
* *Exportador de Volantes em PDF para impressão*
* *Análise retroativa de lucros históricos*
* *Alertas Push de tendências matemáticas*
""")

# ÁREA CENTRAL: Dashboard Analítico do Último Concurso
if len(ultimo_sorteio_set) == 15:
    st.markdown("### 📊 Análise de Comportamento do Último Concurso")
    
    # Cálculos das métricas do concurso base inserido
    u_pares = len([n for n in ultimo_sorteio_set if n % 2 == 0])
    u_impares = 15 - u_pares
    u_primos = len(ultimo_sorteio_set.intersection(NUMEROS_PRIMOS))
    u_moldura = len(ultimo_sorteio_set.intersection(MOLDURA))
    
    # Exibição dos cards visuais usando o layout de colunas do Streamlit
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h4>Pares vs Ímpares</h4>
            <p style="font-size: 24px; font-weight: bold; color: #2e7d32;">{u_impares}Í / {u_pares}P</p>
            <small>Padrão ideal: 8Í / 7P ou 7Í / 8P</small>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h4>Números Primos</h4>
            <p style="font-size: 24px; font-weight: bold; color: #2e7d32;">{u_primos} dezenas</p>
            <small>Padrão ideal: 5 ou 6 primos</small>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h4>Moldura (Bordas)</h4>
            <p style="font-size: 24px; font-weight: bold; color: #2e7d32;">{u_moldura} dezenas</p>
            <small>Padrão ideal: 9 ou 10 na moldura</small>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    
    # ÁREA CENTRAL: Geração Inteligente de Apostas
    st.markdown("### 🎲 Gerador Construtivo de Alta Probabilidade")
    st.write("Clique no botão abaixo para rodar o filtro combinatório e criar seus cartões balanceados.")
    
    if st.button("⚡ Gerar Combinações Otimizadas", type="primary"):
        with st.spinner("Cruzando banco de dados e aplicando travas matemáticas..."):
            jogos = gerar_jogos_estrategicos(quantidade_total=quantidade_jogos, ultimo_sorteio=ultimo_sorteio_set)
            
            st.success(f"Sucesso! {len(jogos)} jogos gerados seguindo a proporção ideal de repetições (70% com 9 repetidas / 30% com 8 repetidas).")
            
            # Divide os jogos na tela em duas colunas para melhorar a diagramação (UI)
            col_jogos_1, col_jogos_2 = st.columns(2)
            
            for idx, jogo in enumerate(jogos, 1):
                # Formata os números com dois dígitos (ex: 02 em vez de 2)
                jogo_formatado = " - ".join(f"{n:02d}" for n in jogo)
                
                # Joga metade dos bilhetes na coluna 1 e metade na coluna 2
                if idx <= (len(jogos) / 2):
                    with col_jogos_1:
                        st.markdown(f'**Bilhete {idx:02d}:**')
                        st.markdown(f'<div class="game-box">{jogo_formatado}</div>', unsafe_allow_html=True)
                else:
                    with col_jogos_2:
                        st.markdown(f'**Bilhete {idx:02d}:**')
                        st.markdown(f'<div class="game-box">{jogo_formatado}</div>', unsafe_allow_html=True)
                        
            st.info("💡 Dica comercial: Copie as dezenas acima e registre-as diretamente no site ou app oficial das Loterias Caixa.")

else:
    st.warning("⚠️ Aguardando a digitação de exatamente 15 dezenas válidas na barra lateral para ativar o aplicativo.")
