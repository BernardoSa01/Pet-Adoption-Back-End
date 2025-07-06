<h1 align="center">🐾 Pet Adoption - API</h1>

<p align="center"> Este repositório contém a API desenvolvida para o projeto Pet Adoption, que faz parte do Projeto MVP do sprint 1 da pós-graduação em Desenvolvimento Full Stack pela PUC-Rio. </p>

<p align="center">A aplicação tem como objetivo gerenciar um sistema de cadastro de animais disponíveis para adoção, permitindo operações como cadastro, listagem, busca e remoção de pets.</p>

> 🎯 Público-alvo: ONGs, abrigos de animais, clínicas veterinárias e iniciativas independentes de adoção.
---

## 🚀 Tecnologias utilizadas

- **Python 3.11**
- **Flask**
- **SQLite**
- **Swagger (Documentação)**
---

## 📂 Estrutura do projeto
```
pet-adoption-api
├── app.py
├── model/
├── schemas
├── requirements.txt
└── README.md
```
---


## 🎯 Funcionalidades 

- Cadastrar novos pets
- Listar todos os pets cadastrados
- Buscar pet por nome 
- Remover pets
---

## ⚙️ Instalação e execução 

Siga os passos abaixo para executar o projeto localmente.

### 1. Clone o repositório

```bash
git clone https://github.com/BernardoSa01/Pet-Adoption-Back-End.git
cd Pet-Adoption-Back-End
```

### 2. Crie e ative um ambiente virtual
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o servidor
```bash
python app.py
```

O servidor estará disponível em:
```bash
http://localhost:5001
```

### 📘 Documentação da API (Swagger)
A documentação interativa pode ser acessada após iniciar o servidor:
```bash
http://localhost:5001/openapi/swagger
```
---

## 📄 Licença
Este projeto é de uso acadêmico, criado para fins de avaliação no curso de pós-graduação da PUC-Rio




