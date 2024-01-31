import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from io import BytesIO


embrapii_logo = "https://embrapii.org.br/wp-content/images/2018/10/logo-embrapii-square.png"
with st.columns(3)[1]:
    st.image(embrapii_logo, use_column_width=True)
st.markdown("""
    <h1 style='text-align: center;'>Redes de inovação EMBRAPII</h1>
""", unsafe_allow_html=True)

dados_unidades ={'Unidade EMBRAPII':['CERTI','SENAI CIMATEC','CEIA-UFG','INATEL','CEEI/UFCG','COPPE','EDGE-UFAL','CPQD','IF-CE','SENAI ISI ELETROQUÍMICA','ELDORADO','SENAI ISI BIOMASSA','SENAI ISI SENSORIAMENTO','SENAI ISI BIOSSINTÉTICOS','SENAI ISI LIGAS ESPECIAIS','SENAI ISI LASER','TECNOGREEN','ESALQ','FEMEC-UFU','INDT','ITEC-FURG','IPT-Materiais','Poli-USP','UFV - Fibras Florestais','SENAI ISI QUÍMICA VERDE','EMBRAPA AGROENERGIA','IF-PB','SENAI SP ISI MATERIAIS AVANÇADOS','USP-IFSC','LAMEF','TECGRAF','CNPEM','CIM-UNIFESP','IF-AM','INT','POLO-UFSC','SENAI ISI EMBARCADOS','Polimeros','CESAR','IF-FLU','IF-Goiano','IF-SC - FLN','MOVE-UFSC','IF-TM','LACTEC','UFSCar - Materiais','CCM-ITA','LESC-UFC','DCC-UFMG','AGROTEC-UFMS','CEINFAR-USP','Escola de Minas - UFOP','CQMED','CEAR-UFPB','VBL IoT E INDÚSTRIA 4,0 - Von Braun','CIEnP','IF-Suldeminas','INRI-UFSM','IF-RN','IF-SP','InovaAgro-UFPel','IF-MG','IPT-Bio','CIn-UFPE','CTIM-UFABC','IF-Goiás','IF-BA','ZETTA-UFLA','FÁRMACOS E VACINAS-UFMG','FMRP-USP','IDOR','METRÓPOLE DIGITAL - UFRN','Graphene-UCS','UFT','Powertrain-USP','BIOTEC-CETENE','CTNano-UFMG','EMBRAPA ITECH-Agro','E-RENOVA - Unicamp','Fitec BH','FITec Campinas','ICMC - USP','INSTITUTO ATLÂNTICO','IQ-USP','ISI TECNOLOGIAS MINERAIS','LITPEG-UFPE','LSI-TEC','NUTES-UEPB','PROMEXBIO-CETEM','SENAI ISI ENGENHARIA DE ESTRUTURAS','SENAI ISI TICS','SIMOB-UFRGS','TECNOLOGIAS 3D - CTI','UFOPA','UFPA'],
'TIPO DE INSTITUIÇÃO':['Instituto Privado','Instituto Privado','Universidade Federal','Universidade Privada','Universidade Federal','Universidade Federal','Universidade Federal','Instituto Privado','Instituto Federal','Instituto Privado','Instituto Privado','Instituto Privado','Instituto Privado','Instituto Privado','Instituto Privado','Instituto Privado','Universidade Estadual','Universidade Estadual','Universidade Federal','Instituto Privado','Universidade Federal','Instituto Público','Universidade Estadual','Universidade Federal','Instituto Privado','Instituto Público','Instituto Federal','Instituto Privado','Universidade Estadual','Universidade Federal','Universidade Privada','Instituto Privado','Universidade Federal','Instituto Federal','Instituto Público','Universidade Federal','Instituto Privado','Instituto Privado','Instituto Privado','Instituto Federal','Instituto Federal','Instituto Federal','Universidade Federal','Instituto Federal','Instituto Privado','Universidade Federal','Universidade Federal','Universidade Federal','Universidade Federal','Universidade Federal','Universidade Estadual','Universidade Federal','Universidade Estadual','Universidade Federal','Instituto Privado','Instituto Privado','Instituto Federal','Universidade Federal','Instituto Federal','Instituto Federal','Universidade Federal','Instituto Federal','Instituto Público','Universidade Federal','Universidade Federal','Instituto Federal','Instituto Federal','Universidade Federal','Universidade Federal','Universidade Estadual','Instituto Privado','Universidade Federal','Universidade Privada','Universidade Federal','Universidade Estadual','Instituto Público','Universidade Federal','Instituto Público','Universidade Estadual','Instituto Privado','Instituto Privado','Universidade Federal','Instituto Privado','Universidade Estadual','Instituto Privado','Universidade Federal','Instituto Privado','Universidade Estadual','Instituto Público','Instituto Privado','Instituto Privado','Universidade Federal','Instituto Público','Universidade Federal','Universidade Federal'],
'CLASSIFICAÇÃO TEMÁTICA EMBRAPII':['Manufatura e Automação','Manufatura e Automação','TICS','TICS','Manufatura e Automação','Mineração, óleo e gás','TICS','TICS','TICS','Química e Materiais','TICS','Química e Materiais','TICS','Química e Materiais','Química e Materiais','Manufatura e Automação','Química e Materiais','Agricultura, Meio ambiente e Sustentabilidade','Química e Materiais','Manufatura e Automação','Manufatura e Automação','Química e Materiais','Química e Materiais','Agricultura, Meio ambiente e Sustentabilidade','Química e Materiais','BIOTECH','Manufatura e Automação','Química e Materiais','Saúde e Fármacos','Química e Materiais','Manufatura e Automação','Saúde e Fármacos','Química e Materiais','Manufatura e Automação','Química e Materiais','Manufatura e Automação','TICS','Química e Materiais','TICS','Energia e Mobilidade','Agricultura, Meio ambiente e Sustentabilidade','Energia e Mobilidade','Energia e Mobilidade','Agricultura, Meio ambiente e Sustentabilidade','TICS','Química e Materiais','Energia e Mobilidade','Manufatura e Automação','TICS','Agricultura, Meio ambiente e Sustentabilidade','Saúde e Fármacos','Mineração, óleo e gás','Saúde e Fármacos','Energia e Mobilidade','TICS','Saúde e Fármacos','Agricultura, Meio ambiente e Sustentabilidade','Energia e Mobilidade','Mineração, óleo e gás','Agricultura, Meio ambiente e Sustentabilidade','Agricultura, Meio ambiente e Sustentabilidade','Energia e Mobilidade','Saúde e Fármacos','Energia e Mobilidade','Química e Materiais','Energia e Mobilidade','Saúde e Fármacos','Agricultura, Meio ambiente e Sustentabilidade','Saúde e Fármacos','Saúde e Fármacos','Saúde e Fármacos','TICS','Química e Materiais','Agricultura, Meio ambiente e Sustentabilidade','Energia e Mobilidade','Agricultura, Meio ambiente e Sustentabilidade','Química e Materiais','Química e Materiais','Agricultura, Meio ambiente e Sustentabilidade','TICS','Manufatura e Automação','TICS','Manufatura e Automação','Química e Materiais','Mineração, óleo e gás','Mineração, óleo e gás','TICS','Saúde e Fármacos','Mineração, óleo e gás','Química e Materiais','TICS','Energia e Mobilidade','Química e Materiais','Agricultura, Meio ambiente e Sustentabilidade','Agricultura, Meio ambiente e Sustentabilidade'],
'Papel de atuação em rede':['DIAMANTE','DIAMANTE','DIAMANTE','DIAMANTE','DIAMANTE','DIAMANTE','DIAMANTE','DIAMANTE','DIAMANTE','DIAMANTE','OURO','OURO','OURO','OURO','OURO','OURO','OURO','OURO','OURO','OURO','OURO','OURO','OURO','OURO','OURO','OURO','OURO','OURO','OURO','OURO','OURO','OURO','PRATA','PRATA','PRATA','PRATA','PRATA','PRATA','PRATA','PRATA','PRATA','PRATA','PRATA','PRATA','PRATA','PRATA','PRATA','PRATA','PRATA','PRATA','PRATA','PRATA','PRATA','PRATA','BRONZE','PRATA','PRATA','PRATA','BRONZE','PRATA','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE','BRONZE'],
'Resultados':[15,15,12,12,13,15,13,13,11,14,15,14,12,12,12,15,13,13,13,13,11,13,15,9,10,10,11,10,10,11,13,12,9,12,12,10,10,9,8,8,8,10,8,6,8,8,7,10,9,7,11,11,7,9,10,7,6,8,9,5,8,6,7,6,6,6,3,7,7,7,7,7,3,5,5,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
'Projetos de PD&I':[10,10,10,10,10,10,10,10,10,10,10,9,10,10,10,7,8,10,9,10,9,10,6,10,7,6,5,5,10,6,6,7,6,6,5,7,4,7,3,7,3,3,4,4,4,4,2,2,3,4,2,2,2,2,2,2,2,2,2,4,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
'Relações com empresas':[5,5,2,3,5,5,5,3,3,4,5,4,2,3,3,5,5,4,5,5,3,3,5,3,2,2,4,3,4,5,5,5,3,5,4,4,3,2,2,2,3,5,1,1,3,4,1,5,5,3,5,5,4,5,4,1,3,5,3,1,4,3,5,2,2,3,1,4,5,5,5,5,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
'Gestão dos KPIs':[5,5,5,5,5,1,5,1,5,5,5,5,5,5,5,1,5,1,1,1,5,1,1,5,5,5,5,5,1,5,1,1,5,1,1,1,5,1,5,1,5,1,5,5,1,5,5,1,1,5,1,1,5,1,1,1,5,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]}
data = pd.DataFrame(dados_unidades)
    
data['Soma das métricas'] = (data['Resultados'] + data['Projetos de PD&I'] + data['Relações com empresas'] + data['Gestão dos KPIs'])/100
# Sidebar with filters
st.sidebar.title('Filtros')
#COLOCAR FILTRO DA DIMENSÃO

selected_category = st.sidebar.multiselect('Papel da Rede', data['Papel de atuação em rede'].dropna().unique())
selected_unity = st.sidebar.selectbox('Unidade', np.insert(data['Unidade EMBRAPII'].dropna().unique(), 0, "Todas", axis=0))
selected_dimension = st.sidebar.selectbox('Dimensão', ['Resultados','Projetos de PD&I','Relações com empresas','Gestão dos KPIs'])

selected_tematicas = st.sidebar.multiselect('Temática', data['CLASSIFICAÇÃO TEMÁTICA EMBRAPII'].dropna().unique())
selected_tipoue = st.sidebar.multiselect('Tipo da UE', data['TIPO DE INSTITUIÇÃO'].dropna().unique())

filtered_data=data

if selected_tematicas:
    filtered_data = filtered_data[filtered_data['CLASSIFICAÇÃO TEMÁTICA EMBRAPII'].isin(selected_tematicas)]
if selected_tipoue:
    filtered_data = filtered_data[filtered_data['TIPO DE INSTITUIÇÃO'].isin(selected_tipoue)]
if selected_category:
    filtered_data = filtered_data[filtered_data['Papel de atuação em rede'].isin(selected_category)]

original_data=filtered_data 

st.markdown("""
<style>
button {
    height: 100px;
    padding-top: 10px !important;
    padding-bottom: 10px !important;
}
</style>
""", unsafe_allow_html=True)

col1,col2,col3= st.columns(3)
if 'Todas' not in selected_unity:
    with col1: #COLOCAR EM NEGRITO
        if st.button('Quero ser **MENTORADO**'):
            dimension_value = data.loc[data['Unidade EMBRAPII'] == selected_unity, selected_dimension].values[0]
            filtered_data = filtered_data[filtered_data[selected_dimension] >= dimension_value]
    with col2:
        if st.button('Quero ser **MENTOR**'):
            dimension_value = data.loc[data['Unidade EMBRAPII'] == selected_unity, selected_dimension].values[0]
            filtered_data = filtered_data[filtered_data[selected_dimension] <= dimension_value]
    with col3:   
        if st.button('Quero ser **PARTICIPANTE** de um projeto'):
            filtered_data = original_data
#Colocar um textinho explicando o que vai aparecer de acordo com o papel da unidade na rede.              

num_unidades=filtered_data['Unidade EMBRAPII'].count()
# Card
st.sidebar.markdown("""
<div style="width: 100%; color: light gray; padding: 20px; border-radius: 5px; font-size: 25px;">
{} <br>
Unidades EMBRAPII
</div>
""".format(num_unidades), unsafe_allow_html=True)


if not filtered_data.empty:
    col1,col2=st.columns(2)
    # Bubble Chart
    color_discrete_map = {'DIAMANTE': 'rgb(185,242,255)', 'OURO': 'rgb(255,215,0)', 'PRATA': 'rgb(192,192,192)', 'BRONZE': 'rgb(184,115,51)'}
    eixox_bubble=st.selectbox('Dimensão EIXO X', ['Resultados','Projetos de PD&I','Relações com empresas','Gestão dos KPIs'])
    eixoy_bubble=st.selectbox('Dimensão EIXO Y', ['Resultados','Projetos de PD&I','Relações com empresas','Gestão dos KPIs'])
    
    fig_bubble = px.scatter(filtered_data, x=eixox_bubble, y=eixoy_bubble,
            size='Soma das métricas', color='Papel de atuação em rede', color_discrete_map=color_discrete_map
                ,hover_name='Unidade EMBRAPII')
    col1.plotly_chart(fig_bubble,use_container_width=True)
    
    #Treemap
    treemap_data = filtered_data.groupby(['Papel de atuação em rede']).size().reset_index(name='Count')
    fig_treemap = px.treemap(treemap_data, path=['Papel de atuação em rede'], values='Count', color='Papel de atuação em rede', color_discrete_map=color_discrete_map)
    fig_treemap.data[0].textinfo = 'label+value'
    fig_treemap.layout.hovermode = False

    col2.plotly_chart(fig_treemap, use_container_width=True)

    #Manipulação de dados para gráfico sunburst
    
    df = filtered_data.loc[:, ['Unidade EMBRAPII', 'CLASSIFICAÇÃO TEMÁTICA EMBRAPII', 'Papel de atuação em rede']]

    novo_df = pd.DataFrame(columns=['Área de Competência', 'DIAMANTE', 'OURO', 'PRATA', 'BRONZE'])

    grupos = df.groupby(['CLASSIFICAÇÃO TEMÁTICA EMBRAPII', 'Papel de atuação em rede'])

    for nome, grupo in grupos:
        area, categoria = nome
        for i, unidade in enumerate(grupo['Unidade EMBRAPII']):
            linha = pd.DataFrame({'Área de Competência': [area], categoria: [unidade]})
            if area not in novo_df['Área de Competência'].values:
                novo_df = pd.concat([novo_df, linha], ignore_index=True)
            else:
                idx = novo_df[(novo_df['Área de Competência'] == area) & (novo_df[categoria].isna())].index
                if len(idx) > 0:
                    novo_df.loc[idx[0], categoria] = unidade
                else:
                    novo_df = pd.concat([novo_df, linha], ignore_index=True)

    novo_df = novo_df.fillna('')

    #Renomear valores em branco
    for col in ['DIAMANTE', 'OURO', 'PRATA']:
        for i in range(len(novo_df[col])):
            if novo_df[col][i] == '':
                novo_df[col][i] = f' '

    for i in range(len(novo_df['BRONZE'])):
        if novo_df['BRONZE'][i] == '':
                novo_df['BRONZE'][i] = None
                
    # Gráfico sunburst
    colormap_sunburst = {'Agricultura, Meio ambiente e Sustentabilidade':'rgb(155, 95, 224)','Energia e Mobilidade':'rgb(22, 164, 216)','TICS':'rgb(96, 219, 232)','Saúde e Fármacos':'rgb(139, 211, 70)','Química e Materiais':'rgb(239, 223, 72)','Mineração, óleo e gás':'rgb(249, 165, 44)','Manufatura e Automação':'rgb(214, 78, 18)'}

    fig = px.sunburst(novo_df, path=['Área de Competência','DIAMANTE', 'OURO', 'PRATA', 'BRONZE'],color='Área de Competência',color_discrete_map=colormap_sunburst)

    fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
    st.plotly_chart(fig)


    
    #Botão para download da tabela

    selected_columns_data = filtered_data[['Unidade EMBRAPII', 'TIPO DE INSTITUIÇÃO', 'CLASSIFICAÇÃO TEMÁTICA EMBRAPII', 'Papel de atuação em rede']]
    def to_excel(df):
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer, index=False, sheet_name='Sheet1')
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']
        format1 = workbook.add_format({'num_format': '0.00'}) 
        worksheet.set_column('A:A', None, format1)  
        writer.close()
        processed_data = output.getvalue()
        return processed_data
    df_xlsx = to_excel(selected_columns_data)
    st.download_button(label='📥 Baixar tabela',
                                    data=df_xlsx ,
                                    file_name= 'df_test.xlsx')
    

    # Display table with selected columns
    st.markdown(selected_columns_data.to_html(index=False, escape=False), unsafe_allow_html=True)
    
else:
    st.warning("Não há registros para os filtros selecionados.")

