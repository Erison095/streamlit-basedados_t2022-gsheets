import streamlit as st
from gsheets import add_contato, listar_contatos

st.set_page_config(page_title="Agenda", layout="centered")
st.title("📇 Exemplo de Agenda de Contatos (Google Sheets)")

with st.form("form_contato"):
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    trab = st.text_input("Qual trabalho você procura ?")
    enviar = st.form_submit_button("Salvar")

    if enviar:
        if nome and (email,trab):
            sucesso = add_contato(nome, email, trab)
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
        trab = contato.get("trab", "Sem trabalho")
        st.write(f"**{nome}** - {email} - {trab}")
else:
    st.info("Nenhum contato cadastrado.")
