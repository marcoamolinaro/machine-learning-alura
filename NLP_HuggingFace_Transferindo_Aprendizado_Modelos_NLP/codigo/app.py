from transformers import pipeline
from transformers import AutoTokenizer
from transformers import TFAutoModelForSequenceClassification
from transformers import create_optimizer
import gradio as gr
from datasets import load_dataset, DatasetDict, ClassLabel
from huggingface_hub import notebook_login
import numpy as np
import torch
import os
from huggingface_hub import login

print("Hello, world!")

token_write = os.getenv("HF_TOKEN_WRITE")
#login(token=token_write)

print("Logged in to Hugging Face Hub")

classificador = pipeline(
    "zero-shot-classification", 
    model="Mel-Iza0/zero-shot", 
    tokenizer="Mel-Iza0/zero-shot"
)

texto = 'Com o início da era digital, a capacidade de transmissão de informações cresceu apressuradamente, o que facilitou o contato com diversos assuntos, dentre eles a educação sexual . Entretanto, surgiram paralelamente algumas questões, das quais se destacam a preocupação com o momento adequado do ingresso do tema a vida do estudante, assim como de maneira antagônica, o aumento de casos de DST´S\\xa0\\xa0e gravidez indesejada nesse período, a qual leva a um maior questionamento sobre o começo desta pauta., A falta de comunicação sobre a sexualidade entre jovens no Brasil acarreta muitas das vezes\\xa0na inserção desses em um meio repleto de dúvidas, gerando a ocorrência de doenças sexualmente transmissíveis e de gravidez precoce. Com base nisso, muitos adolescentes buscam compreender melhor essas questões na internet, local onde se podem encontrar notícias falsas ou inadequadas para seu desenvolvimento, impedindo assim a correta compreensão do assunto, assim como a responsabilidade imposta por ele., Por outro lado, o diálogo em relação à sexualidade e seus tópicos é um tabu para pais e professores, que se sentem desorientados sobre a devida hora e os devidos critérios a serem tratados com os filhos e alunos, dificultando com que esses esclareçam suas dúvidas e entenda de maneira correta, o que levaria a conscientização da seriedade dessa discussão., Em virtude do que foi mencionado, as indagações a respeito divide várias opiniões e reflexões acima do que deve ser feito. É de extrema importância o Ministério da Educação, em parceria com o Ministério da Cidadania, implantar a educação sexual na matriz curricular estudantil dos jovens, através de aulas elaboradas e destinadas ao esclarecimento de perguntas, assim como palestras e programas com a intenção de propagar o conteúdo aos estudantes, contando com o suporte dos pais, funcionários e encarregados da rede de ensino no país, para que seja realizado constantemente.'

classificador(texto, candidate_labels=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

def mostrar_resultado(texto):
    return classificador(texto, candidate_labels=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])['labels'][0]

# app = gr.Interface(
#     fn=mostrar_resultado,
#     inputs=["text"],
#     outputs=["text"]
# )

# app.launch()
dados_redacoes = load_dataset("csv", data_files='./redacoes.csv')

treino_teste = dados_redacoes['train'].train_test_split(test_size=0.2, shuffle=False)
treino_teste

dados_redacoes = DatasetDict({
    'treino': treino_teste['train'],
    'teste': treino_teste['test']
})

modelo = TFAutoModelForSequenceClassification.from_pretrained("mam1963/distilbert-essays-scores-pt-cased")
tokenizador = AutoTokenizer.from_pretrained("mam1963/distilbert-essays-scores-pt-cased")

dados_redacoes['teste'].to_pandas()

textos = [dados_redacoes['teste']['essay'][2],
          dados_redacoes['teste']['essay'][909]]