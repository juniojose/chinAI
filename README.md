# chinAI - Bot de Automação para Instagram

Um bot de automação desenvolvido em Python para interagir com o Instagram, focado em executar tarefas repetitivas como "curtir" posts na timeline.

## Funcionalidades

-   **Captura de Coordenadas:** Uma interface de linha de comando (CLI) interativa para mapear e salvar as coordenadas de elementos da interface gráfica.
-   **Automação de Cliques:** Executa uma sequência de cliques baseada nas coordenadas salvas.
-   **Reconhecimento de Imagem:** Utiliza reconhecimento de imagem para localizar e interagir com elementos dinâmicos, como o botão "curtir".
-   **Operação em Múltiplas Instâncias:** Projetado para operar em um ciclo, passando por múltiplas instâncias (ex: "telefones").

## Pré-requisitos

-   Python 3.x
-   Pip

## Instalação

1.  Clone este repositório:
    ```sh
    git clone https://github.com/juniojose/chinAI.git
    cd chinAI
    ```

2.  Crie e ative um ambiente virtual (recomendado):
    ```sh
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Como Usar

A aplicação funciona em duas etapas principais:

### 1. Configuração (Captura de Coordenadas)

Antes de rodar o bot, você precisa ensiná-lo onde clicar. Execute o script de configuração:

```sh
python cli.py
```

O script pedirá que você clique em diferentes locais na tela. Para cada clique, você deverá fornecer um nome para essa coordenada no terminal (por exemplo, `instagramIcon`, `likeButton`, etc.). Pressione `ESC` quando terminar. Isso criará o arquivo `coordenadas.json`.

### 2. Execução do Bot

Com o arquivo `coordenadas.json` criado, você pode iniciar o bot de automação:

```sh
python src/automacao.py
```

O bot começará a executar o ciclo de ações pré-definido, utilizando as coordenadas que você salvou.
