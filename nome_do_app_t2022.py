import streamlit as st
from gsheets import add_contato, listar_contatos

st.set_page_config(page_title="Agenda", layout="centered")
st.title("🏭 Programa mais emprego")

with st.form("form_contato"):
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    trabalho = st.text_input("Qual trabalho você procura ?")
    experiencia = st.text_input("Conte um pouco de você e suas experiencias. (opcional)")
    enviar = st.form_submit_button("Salvar")

    if enviar:
        if nome and email and trabalho and experiencia:
            sucesso = add_contato(nome, email, trabalho, experiencia)
            if sucesso:
                st.success("Contato salvo com sucesso!")
            else:
                st.warning("Contato já existe na lista.")
        else:
            st.warning("Preencha todos os campos.")

st.subheader("📋 Contatos cadastrados")
dados = listar_contatos()

if dados:
    for contato in dados:
        nome = contato.get("nome", "Sem nome")
        email = contato.get("email", "Sem email")
        trabalho = contato.get("trabalho", "Sem trabalho")
        experiencia = contato.get("experiencia", "Sem experiencia")
        st.write(f"**{nome}** - {email} - {trabalho} - {experiencia}")
else:
    st.info("Nenhum contato cadastrado.")
