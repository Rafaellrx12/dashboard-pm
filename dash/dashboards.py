import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


n_linhas = 1000

posto_graduacao = np.random.choice(['Soldado', 'Cabo', 'Sargento', 'Subtenente', 'Tenente', 'Capitão', 'Major', 'Tenente-Coronel', 'Coronel'], n_linhas)
regime = np.random.choice(['Ativa', 'Reserva', 'Reforma', 'Excluído'], n_linhas)
comportamento = np.random.choice(['Bom', 'Regular', 'Ruim'], n_linhas)
entidade = np.random.choice(['Unidade', 'Batalhão'], n_linhas)
local_do_fato = np.random.choice([ 'Rua X', 'Avenida Y', 'Praça Z'], n_linhas)
registro_desvio = np.random.choice(['Sim', 'Não'], n_linhas)
registro_criminal = np.random.choice(['Sim', 'Não'], n_linhas)

data_registro = pd.date_range(start='2020-01-01', end='2022-12-31', periods=n_linhas)
sexo = np.random.choice(['Masculino', 'Feminino'], n_linhas)


df = pd.DataFrame({
    'Posto/Graduação': posto_graduacao,
    'Regime': regime,
    'Comportamento': comportamento,
    'Entidade': entidade,
    'Local do Fato': local_do_fato,
    'Registro de Desvio de Conduta': registro_desvio,
    'Registro Criminal': registro_criminal,
    'Data Registro': data_registro,
    'Sexo': sexo
})


df.to_excel('dados_pm.xlsx', index=False)


df = pd.read_excel("dados_pm.xlsx");


st.set_page_config(layout="wide");


ano = st.sidebar.selectbox("Ano", df["Data Registro"].dt.year.unique());
df_filtrado = df[df["Data Registro"].dt.year == ano];


filtro_local = st.sidebar.selectbox("Localidade", df["Local do Fato"].unique())
if filtro_local != "":
    df_filtrado = df_filtrado[df_filtrado["Local do Fato"] == filtro_local]




cores = px.colors.qualitative.Set2


with st.container():
    fig_data = px.histogram(df_filtrado, x="Data Registro", title="Histograma da Data de Registro", color_discrete_sequence=[cores]);
    fig_data.update_yaxes(title_text='Quantidade')
    st.plotly_chart(fig_data, use_container_width=True);


with st.container():
    fig_posto_graduacao = px.histogram(df_filtrado, x="Posto/Graduação",title="Contagem de Registros por Posto/Graduação", color_discrete_sequence=cores)
    fig_posto_graduacao.update_yaxes(title_text='Quantidade');
    st.plotly_chart(fig_posto_graduacao, use_container_width=True)


with st.container():
    fig_entidade = px.histogram(df_filtrado, x="Entidade", title="Contagem de Registros por Entidade", color_discrete_sequence=cores)
    fig_entidade.update_yaxes(title_text='Quantidade')
    st.plotly_chart(fig_entidade, use_container_width=True)


with st.container():
    fig_comportamento = px.pie(df_filtrado, names="Comportamento", title="Distribuição do Comportamento", color_discrete_sequence=cores)
    fig_comportamento.update_yaxes(title_text='Quantidade');
    st.plotly_chart(fig_comportamento, use_container_width=True)


with st.container():
    fig_regime_entidade = px.histogram(df_filtrado, x="Regime", color="Entidade", title="Contagem de Registros por Regime e Entidade", color_discrete_sequence=cores)
    fig_regime_entidade.update_yaxes(title_text='Quantidade')
    st.plotly_chart(fig_regime_entidade, use_container_width=True)


with st.container():
    fig_sexo = px.histogram(df_filtrado, x="Sexo", title="Contagem de Registros por Sexo", histfunc='count', color_discrete_sequence=cores)
    fig_sexo.update_yaxes(title_text='Quantidade')
    st.plotly_chart(fig_sexo, use_container_width=True)
