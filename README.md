# Deep Learning PyTorch SQL Code Completer

Este repositório contém um projeto de Deep Learning utilizando **PyTorch** para criar um completador de código SQL simples.

## Sobre o Projeto

O objetivo é treinar um modelo de linguagem (Language Model) capaz de prever as próximas palavras de um comando SQL com base no contexto anterior. O modelo utiliza uma arquitetura de Redes Neurais Recorrentes (RNN) com células **LSTM** (Long Short-Term Memory).

### Funcionalidades

*   **Pré-processamento de Texto**: Tokenização e criação de vocabulário a partir de um corpus de comandos SQL.
*   **Modelo LSTM**: Implementação de uma rede neural `SQLLM` com camadas de Embedding, LSTM e Linear.
*   **Dataset Customizado**: Classe `SQLDataset` para preparar sequências de entrada e saída para o treinamento.
*   **Treinamento**: Loop de treinamento utilizando `CrossEntropyLoss` e otimizador `Adam`.
*   **Geração de Texto**: Função `complete_text` para sugerir completamentos de código SQL dado um texto inicial (seed).

## Estrutura do Repositório

*   `completador-de-codigo/`: Contém o Jupyter Notebook (`Completador_de_codigo.ipynb`) com todo o código do projeto, desde o pré-processamento até a inferência.

## Como Usar

1.  Navegue até a pasta `completador-de-codigo`.
2.  Abra o notebook `Completador_de_codigo.ipynb` em um ambiente Jupyter ou Google Colab.
3.  Execute as células para treinar o modelo e testar a geração de código SQL.

## Tecnologias Utilizadas

*   Python
*   PyTorch
*   Jupyter Notebook