# Projeto 3 — Pipeline de Engenharia de Dados SRAG

Projeto acadêmico de Engenharia de Dados desenvolvido em Python, utilizando a arquitetura Medallion (Bronze, Silver e Gold) para processar dados públicos de Síndrome Respiratória Aguda Grave (SRAG), disponibilizados pelo SUS.

## Objetivo

Desenvolver um pipeline reproduzível de coleta, tratamento e agregação de dados, além de um dashboard interativo para exploração dos resultados.

## Tecnologias utilizadas

- Python
- Pandas
- Requests
- Jupyter Notebook
- Streamlit
- Git e GitHub

## Arquitetura Medallion

- **Bronze:** coleta e armazenamento dos dados originais.
- **Silver:** limpeza, tratamento e padronização dos dados.
- **Gold:** agregação dos dados e geração de indicadores.
- **Dashboard:** visualização interativa utilizando Streamlit, consumindo exclusivamente os dados da camada Gold.

## Estrutura do projeto

```text
projeto3-pipeline-srag/
│
├── notebooks/
│   ├── 01_bronze.ipynb
│   ├── 02_silver.ipynb
│   └── 03_gold.ipynb
│
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Fonte de dados

Portal de Dados Abertos do SUS — Síndrome Respiratória Aguda Grave (SRAG), período de 2019 a 2026.

## Equipe

Projeto desenvolvido por Lucas Flores Corrêa e Vitor Edu Bombassaro do curso de Engenharia de Computação da Universidade Federal do Pampa (UNIPAMPA).

## Projeto Integrador I
