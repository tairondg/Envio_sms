import streamlit as st
import pandas as pd
from twilio.rest import Client
import sendmsg as sd
import services.bd_contato as db


st.set_page_config(
     page_title="Envio de mensagem",
     page_icon="📱",
     layout="centered",
     initial_sidebar_state="expanded",
    )

col1, col2 = st.columns(2)
with col1:
    st.image('GU_logo-branco.png')

# retirar o menu do Streamlit da tela
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# st.write(contatos)
st.title("Enviar mensagem")

cpf = st.text_input(str("Digite o CPF"))
# pesq_cpf = contatos.loc[contatos["CPF"] == cpf]


# for i, num_cpf in enumerate(contatos["CPF"]):
#     nome = contatos.loc[i, 'Nome']
#     celular = contatos.loc[i, 'Celular']


# def enviar_msg():
#     # Your Account SID from twilio.com/console
#     account_sid = "AC67186a420be226f63da0c02a8497ede3"
#     # Your Auth Token from twilio.com/console
#     auth_token  = "d804cda4a4f574748702111c677bf189"
#     client = Client(account_sid, auth_token)
#     client.messages.create(
#     to=f"+55{celular}", 
#     from_="+19704998790",
#     body=f"Olá, {nome}! Carregamento liberado!")

try:
    def enviar_carregamento():
        # Your Account SID from twilio.com/console
        account_sid = "AC67186a420be226f63da0c02a8497ede3"
        # Your Auth Token from twilio.com/console
        auth_token  = "d804cda4a4f574748702111c677bf189"
        client = Client(account_sid, auth_token)
        client.messages.create(
        to=f"+55{row[3]}", 
        from_="+19704998790",
        body=f"GRUPO UNIMETAL - UNIDADE COSMOPOLIS Informa: {row[1]}, Entrada liberada!")
    
    def enviar_faturamento():
        # Your Account SID from twilio.com/console
        account_sid = "AC67186a420be226f63da0c02a8497ede3"
        # Your Auth Token from twilio.com/console
        auth_token  = "d804cda4a4f574748702111c677bf189"
        client = Client(account_sid, auth_token)
        client.messages.create(
        to=f"+55{row[3]}", 
        from_="+19704998790",
        body=f"GRUPO UNIMETAL - UNIDADE COSMOPOLIS Informa: {row[1]}, retirar NF na portaria.")

    if st.button("BUSCAR 🔎"):
        db.cursor.execute(f"SELECT * from contato_msg WHERE cpf_motorista = '{cpf}'") 
        row = db.cursor.fetchone() 
        st.header(f'Sua mensagem será enviada para o {row[1]}! \n Escolha abaixo a forma de envio:')
        
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                if st.button("AUTORIZAR CARREGAMENTO", on_click=enviar_carregamento):
                    st.success("Autorização de carregameto enviada com sucesso!")
                # contatos['CPF'] = contatos['CPF'].astype(str)
                # contatos['Celular'] = contatos['Celular'].astype(str)
                # pesq_cpf = contatos.loc[contatos["CPF"] == cpf]
                # nome = pesq_cpf.iloc[0, 2]
                # celular = pesq_cpf.iloc[0, 1]
                # st.write(f'Meu nome é {nome} e meu celular é {celular}')    
                    # if st.button("Carregamento", on_click=enviar_msg):
                    #     st.write("Mensagem enviada")
            
            with col2:
                if st.button("NOTA FISCAL LIBERADA", on_click=enviar_faturamento):
                    st.success("Mensagem enviada com sucesso!")


except:
    st.success("CPF não cadastrado!")




# if st.button("AUTORIZAR CARREGAMENTO"):
#     # contatos['CPF'] = contatos['CPF'].astype(str)
#     # contatos['Celular'] = contatos['Celular'].astype(str)
#     # pesq_cpf = contatos.loc[contatos["CPF"] == cpf]
#     # nome = pesq_cpf.iloc[0, 2]
#     # celular = pesq_cpf.iloc[0, 1]
#     # st.write(f'Meu nome é {nome} e meu celular é {celular}')    
#     if st.button("Carregamento", on_click=enviar_msg):
#         st.write("Mensagem enviada")
    
        
        





    
    
# for i, pesq_cpf in enumerate(contatos["CPF"]):        
#     nome = contatos.loc[i, 'Nome']
#     celular = contatos.loc[i, 'Celular']
# st.text(f'{nome} e {celular}')
# st.write(f"Oi {teste[1]}, esse é o seu celular {teste[2]}!!")
#     for i, cpf in enumerate(contatos["CPF"]):
#         nome = contatos.loc[i, 'Nome']
#         celular = contatos.loc[i, 'Celular']
    