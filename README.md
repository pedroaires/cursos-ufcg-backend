# cursos-ufcg-backend

Este é o repositório do backend do projeto Cursos UFCG. O objetivo deste projeto é fornecer uma API fornecer informações diversas sobre cursos oferecidos pela Universidade Federal de Campina Grande (UFCG) para o sistema: https://github.com/pedroaires/cursos-ufcg-frontend.

## Localmente
### Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/pedroaires/cursos-ufcg-backend.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd cursos-ufcg-backend/src
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

### Configuração

1. Crie um arquivo `.env` no diretório src e adicione as variáveis
    ```
    DATABASE_URL=...
    ```

### Uso

1. Execute a aplicação
    ```bash
    uvicorn app.main:app --host 127.0.0.1 --port 5000
    ```
2. A API estará disponível em `http://localhost:5000`.


## Via Docker
### Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/pedroaires/cursos-ufcg-backend.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd cursos-ufcg-backend/src
    ```
3. Instale as dependências:
    ```bash
    docker build -t cursos-ufcg-backend .
    ```

### Configuração

1. Crie um arquivo `.env` no diretório src e adicione as variáveis
    ```
    DATABASE_URL=...
    ```

### Uso

1. Execute o container Docker
    ```bash
    docker run -d -p 5000:5000 --name cursos-backend cursos-ufcg-backend
    ```
2. A API estará disponível em `http://localhost:5000`.


