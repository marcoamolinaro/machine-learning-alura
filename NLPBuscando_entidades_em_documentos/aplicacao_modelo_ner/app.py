import streamlit as st
import spacy 

st.title("Reconhecimento de Entidades Nomeadas (NER)")

caminho_modelo = "D:/Desenvolvedor/Alura/FormacaoMachineLearning/NLPBuscando_entidades_em_documentos/aplicacao_modelo_ner/modelo/content/modelo"

modelo = spacy.load(caminho_modelo)

texto = ''

arquivo = st.file_uploader("Carregar arquivo de texto (somente .txt)", type=["txt"])

if arquivo is not None:
    texto = arquivo.read().decode("utf-8")

if texto:
    doc = modelo(texto)
    st.subheader('Entidades Reconhecidas:')
    for entidade in doc.ents:
        st.text(f'{entidade.text} -> {entidade.label_}') 

