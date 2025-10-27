import gradio as gr
from transformers import pipeline
import torch
from codigos_traducao import codigos_linguagens


def traduzir_resumir_textos(texto, ling_origem, ling_final):

    nome_modelo_traducao = 'facebook/nllb-200-distilled-600M'
    nome_modelo_resumo = 'facebook/bart-large-cnn'

    idioma_origem = codigos_linguagens[ling_origem]
    idioma_final = codigos_linguagens[ling_final]

    if idioma_origem == "eng_Latn":
        resumidor = pipeline('summarization', model=nome_modelo_resumo)
        resumo = resumidor(texto, max_length=200, min_length=100)[0]['summary_text']
    else:
        tradutor = pipeline('translation', model=nome_modelo_traducao, src_lang=idioma_origem, tgt_lang='eng_Latn')
        texto_traduzido = tradutor(texto, max_length=512)[0]['translation_text']

        resumidor = pipeline('summarization', model=nome_modelo_resumo)
        resumo = resumidor(texto_traduzido, max_length=200, min_length=100)[0]['summary_text']

    tradutor = pipeline('translation', model=nome_modelo_traducao, src_lang='eng_Latn', tgt_lang=idioma_final)
    texto_traduzido = tradutor(texto, max_length=512)[0]['translation_text']

    return texto_traduzido


if __name__ == '__main__':
    codigos_idioma = list(codigos_linguagens.keys())

    theme = gr.themes.Soft(
      primary_hue="fuchsia",
      secondary_hue="blue",
    ).set(
        body_background_fill='*checkbox_background_color',
        body_background_fill_dark='*button_cancel_border_color_hover',
        background_fill_primary='*neutral_900',
        background_fill_primary_dark='*error_icon_color'
    )


    with gr.Blocks(theme=theme) as app:

      gr.Markdown('# Tradução e Resumo')
      gr.Markdown('Esta aplicação traduz texto para português e depois o resume. Modelo de tradução: facebook/nllb-200-distilled-600M. Modelo de sumarização: facebook/bart-large-cnn.')

      with gr.Row():

        with gr.Column():
          texto = gr.Textbox(lines=5, label="Texto de entrada")
          origem = gr.Dropdown(codigos_idioma, value='English', label='Texto original')
          destino = gr.Dropdown(codigos_idioma, value='Portuguese', label='Texto final')
        with gr.Column():
          resumo = gr.Textbox(lines=5, label="Texto resumido")


      botao = gr.Button('Gerar resumo')

      botao.click(
          fn = traduzir_resumir_textos,
          inputs = [texto, origem, destino],
          outputs = resumo
      )

    app.launch()