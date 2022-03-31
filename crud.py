from this import d
import streamlit as st;

with st.form(key="include_cliente"):
    input_name = st.text_input(label="Insira o seu nome")
    input_age = st.number_input(label="Insira a sua idade",format="%d",step=1)
    input_occupation = st.selectbox("Selecione sua profissão",["Agronomo", "Arquiteto", "Bombeiro", "Barbeiro", "Cozinheiro", "Contador", "Dentista", "Desempregado", "Engenheiro", "Encanador", "Farmaceutico", "Frentista", "Garimpeiro", "Goleiro", "Jornalista", "Jardineiro", "Neurocirurgião", "Narrador", "Oculista", "Ourives", "Palhaço", "Programador", "Quiroprata", "Queijeiro", "Redator", "Recepcionista", "Secretário", "Somelier", "Tecnico", "Tabeliao", "Urologista", "Vaqueiro", "Vendedor", "Zelador"])
    input_button_submit = st.form_submit_button("Enviar")
    
if input_button_submit:
    st.write(f'Nome: {input_name}') 
    st.write(f'Idade: {input_age}')  
    st.write(f'Profissão: {input_occupation}')  
     