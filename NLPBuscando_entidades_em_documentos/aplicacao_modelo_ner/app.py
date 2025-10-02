import streamlit as st
import spacy 
from spacy_streamlit import visualize_ner


st.title("Reconhecimento de Entidades Nomeadas (NER)")

caminho_modelo = "D:/Desenvolvedor/Alura/FormacaoMachineLearning/NLPBuscando_entidades_em_documentos/aplicacao_modelo_ner/modelo/content/modelo"

modelo = spacy.load(caminho_modelo)

rotulos = list(modelo.get_pipe('ner').labels)

cores = {
  'B-JURISPRUDENCIA': '#F0F8FF',
  'B-LEGISLACAO': '#FA8072',
  'B-LOCAL': '#F98FB98',
  'B-ORGANIZACAO': '#DDA0DD',
  'B-PESSOA': '#F0E68C',
  'B-TEMPO': '#FFB6C1',
  'I-JURISPRUDENCIA': '#F0F8FF',
  'I-LEGISLACAO': '#FA8072',
  'I-LOCAL': '#F98FB98',
  'I-ORGANIZACAO': '#DDA0DD',
  'I-PESSOA': '#F0E68C',
  'I-TEMPO': '#FFB6C1',
  'LOC': '#D3D3D3',
  'MISC': '#D3D3D3',
  'ORG': '#D3D3D3',
  'PER': '#D3D3D3'
}

opcoes = {'ents': rotulos, 'colors': cores}

escolha = st.radio(label= "Escolha uma opção para fornecer o texto:", options=['Inserir texto manualmente', 'Carregar arquivo de texto'])

texto = ''

if escolha == 'Inserir texto manualmente':
    texto = st.text_area("Insira o texto aqui:")
elif escolha == 'Carregar arquivo de texto':
    arquivo = st.file_uploader("Carregar arquivo de texto (somente .txt)", type=["txt"])
    if arquivo is not None:
        texto = arquivo.read().decode("utf-8")

doc = modelo(texto)
    
visualize_ner(doc, 
              labels=rotulos, 
              displacy_options=opcoes,
              colors=cores,
              title="Entidades Nomeadas Reconhecidas"
            )

