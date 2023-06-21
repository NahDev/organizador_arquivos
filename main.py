import os
import shutil
from datetime import datetime


def organizar_pastas_arquivos(
    pasta_raiz, pasta_destino, pastas_excluidas=[], arquivos_excluidos=[]
):
    for caminho_atual, subpastas, arquivos in os.walk(pasta_raiz):
        for subpasta in subpastas:
            if subpasta in pastas_excluidas:
                continue  # Pula a pasta se estiver na lista de pastas excluídas
            print("""""")

            caminho_completo = os.path.join(caminho_atual, subpasta)
            print(caminho_completo)

            print(f"lendo a subpasta {subpasta}")
            data_modificacao = datetime.fromtimestamp(
                os.path.getmtime(caminho_completo)
            )
            ano = str(data_modificacao.year)
            mes = str(data_modificacao.month).zfill(2)
            nova_pasta = os.path.join(pasta_destino, ano, mes, subpasta)

            if not os.path.exists(os.path.dirname(nova_pasta)):
                os.makedirs(os.path.dirname(nova_pasta))

            if not os.path.exists(nova_pasta):
                shutil.copytree(caminho_completo, nova_pasta)
                print(f"movendo a subpasta {subpasta} para a nova pasta {nova_pasta}")
            else:
                print(
                    f"O arquivo {subpasta} já existe na pasta {nova_pasta}. Não será movido."
                )

        for arquivo in arquivos:
            if arquivo in arquivos_excluidos:
                continue  # Pula o arquivo se estiver na lista de arquivos excluídos

            print(f"lendo o arquivo {arquivo}")

            caminho_completo = os.path.join(caminho_atual, arquivo)
            data_modificacao = datetime.fromtimestamp(
                os.path.getmtime(caminho_completo)
            )
            ano = str(data_modificacao.year)
            mes = str(data_modificacao.month).zfill(2)
            nova_pasta = os.path.join(pasta_destino, ano, mes)

            if not os.path.exists(nova_pasta):
                os.makedirs(nova_pasta)

            novo_caminho = os.path.join(nova_pasta, arquivo)

            if not os.path.exists(novo_caminho):
                shutil.copy(caminho_completo, novo_caminho)
                print(f"movendo o arquivo {arquivo} para a nova pasta {nova_pasta}")
            else:
                print(
                    f"O arquivo {arquivo} já existe na pasta {nova_pasta}. Não será movido."
                )


pasta_raiz = "/home/pmaubouro/Downloads"
pasta_destino = (
    "/home/pmaubouro/Downloads/Resultados"  # Defina o caminho para a nova pasta aqui
)
pastas_excluidas = [
    "go",
    "Resultados",
    "bin",
    "lib",
    "doc",
    "api",
    "src",
    "pkg",
    "test"
]  # Lista de pastas a serem excluídas
arquivos_excluidos = [
    "Win10_22H2_BrazilianPortuguese_x64.iso",
    "Anaconda3-2023.03-Linux-x86_64.sh",
    "RoboVivo.zip",
]  # Lista de arquivos a serem excluídos

organizar_pastas_arquivos(
    pasta_raiz, pasta_destino, pastas_excluidas, arquivos_excluidos
)
