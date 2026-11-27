from pathlib import Path
from datetime import datetime
import json
import requests

ROOT = Path(__file__).resolve().parents[1]
BRONZE_DIR = ROOT / "data" / "bronze"

ANOS = range(2019, 2027)

BASE_URL = "https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SRAG"


def obter_url(ano):
    if ano <= 2024:
        data = "23-03-2026"
    else:
        data = "23-11-2026"

    ano_curto = str(ano)[-2:]

    nome = f"INFLUD{ano_curto}-{data}.csv"

    return f"{BASE_URL}/{ano}/{nome}"


def baixar_arquivo(url, destino):
    destino.parent.mkdir(parents=True, exist_ok=True)

    resposta = requests.get(
        url,
        stream=True,
        timeout=(30, 300)
    )

    resposta.raise_for_status()

    with open(destino, "wb") as arquivo:
        for bloco in resposta.iter_content(
            chunk_size=1024 * 1024
        ):
            if bloco:
                arquivo.write(bloco)

    resposta.close()


def executar_bronze():
    BRONZE_DIR.mkdir(parents=True, exist_ok=True)

    relatorio = []

    for ano in ANOS:
        url = obter_url(ano)

        nome = url.split("/")[-1]
        destino = BRONZE_DIR / nome

        print(f"Baixando {ano}...")

        try:
            baixar_arquivo(url, destino)

            print(f"[OK] {ano} baixado.")

            relatorio.append({
                "ano": ano,
                "status": "baixado",
                "arquivo": nome,
                "url": url,
                "data_coleta": datetime.now().isoformat(
                    timespec="seconds"
                )
            })

        except requests.exceptions.HTTPError as erro:
            print(f"[ERRO] {ano}: {erro}")

            relatorio.append({
                "ano": ano,
                "status": "erro",
                "detalhe": str(erro)
            })

        except requests.exceptions.RequestException as erro:
            print(f"[ERRO] {ano}: {erro}")

            relatorio.append({
                "ano": ano,
                "status": "erro",
                "detalhe": str(erro)
            })

    metadados = {
        "fonte": "Portal de Dados Abertos do SUS",
        "conjunto": "SRAG 2019 a 2026",
        "url_conjunto": (
            "https://dadosabertos.saude.gov.br/"
            "dataset/srag-2019-a-2026"
        ),
        "arquivos": relatorio
    }

    caminho_metadados = BRONZE_DIR / "metadados_coleta.json"

    caminho_metadados.write_text(
        json.dumps(
            metadados,
            ensure_ascii=False,
            indent=2
        ),
        encoding="utf-8"
    )

    print("\nColeta finalizada!")
    print(f"Arquivos salvos em: {BRONZE_DIR}")


if __name__ == "__main__":
    executar_bronze()
