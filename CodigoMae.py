import streamlit as st
import pandas as pd
import plotly.express as px

#passo 1: # CRIANDO O TÍTULO DO SISTEMA

st.write('# SISTEMA DE VENDAS')
tabela = pd.read_csv('vendas.csv')

# passo 2: CRIAR O FORMULÁRIO DE CADASTRO DAS VENDAS

st.sidebar.write('## CADASTRO DE VENDAS')
data = st.sidebar.date_input('Data')
vendedor =st.sidebar.selectbox('Vendedor',['Ana', 'Bruno', 'Carla'])
produto = st.sidebar.selectbox('Produto', ['Celular', 'Notebbok', 'Fone'])
quantidade = st.sidebar.number_input('Quantidade',step=1)
valor = st.sidebar.number_input('Valor')
botao = st.sidebar.button('Salvar Venda')

# passo 3: SALVANDO A VENDA NO BANCO DE DADOS

if botao:
    nova_venda = [data, vendedor, produto, quantidade, valor]
    tabela.loc[len(tabela)] = nova_venda
    tabela.to_csv('vendas.csv', index=False)
    st.success('Venda cadastrada...')

# passo 4: MOSTRAR A BASE DE DADOS

st.write('## Vendas Cadastradas')
st.dataframe(tabela)

# passo 5: CRIANDO O DASHBOARD

st.write('## DASHBOARD')
soma =  tabela['valor'].sum()
st.metric('Faturamento Total', f"R${soma}")

# CRIAÇÃO DOS GRÁFICOS

# gráfico de barras - VENDAS P/ VENDEDOR
grafico = px.bar(tabela,x='vendedor',y='valor',color='produto')
st.plotly_chart(grafico)

# gráfico de pizza - PARTICIPAÇÃO p/ PRODUTO
grafico2 = px.pie(tabela,names='produto',values='valor')
st.plotly_chart(grafico2)
                          
                             
