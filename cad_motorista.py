import streamlit as st
import Controllers.MotoristaController as MotoristaController
import models.Motorista as motorista

col1, col2 = st.columns(2)
with col1:
    st.image('GU_logo-branco.png')
    
st.title("Incluir Motorista")

with st.form(key="incluir_motorista"):
    input_nome = st.text_input(label="Nome motorista")
    input_cpf = st.text_input(label="CPF")    
    input_cel = st.text_input(label="Celular")
    input_button_submit = st.form_submit_button("Salvar")


if input_button_submit:
    motorista.cpf_motorista = input_cpf
    motorista.nome_motorista = input_nome
    motorista.cel_motorista = input_cel

    MotoristaController.incluir(motorista)
    st.success("Motorista cadastrado com sucesso")

    