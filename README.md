# Sistema de Cadastramento e Visualização de Dados

Este projeto é um sistema desenvolvido em Django para realizar o cadastro e visualização de dados via interface web e API.

## ⚙ Configurações

| Configuração      | Especificações              |
|-------------------|-----------------------------|
| Linguagem         | Python                      |
| Framework         | Django                      |
| Banco de Dados    | SQLite                      |
| Repositório       | Git                         |
| Ambiente Local    | Porta padrão: 8000          |
| Integrações       | Templates, API              |

---

## 🚀 Iniciando o Projeto SRH

### 1. Clone o repositório

bash
git clone https://github.com/CarlosVLemos/projeto-semana-ubiqua 



#### 1. Crie o arquivo crie um ambiente virtual antes de baixar as dependencias do projeto, no terminal digite
bash
python -m venv env




#### 1. Ainda no terminal, ative o ambiente virtual

linux:

bash
source env/bin/activate



windows:
bash
env\Scripts\activate


#### 2. Baixe as dependencias do arquivo requirements.txt
bash
pip install -r requirements.txt


#### 3. Fazer as migrações do sistema
bash
Python manage.py migrate



#### 4. Crie um super usuario 
bash
python manage.py createsuperuser


irá pedir para criar: nome,email,senha

lembre deles para fazer login na aplicação, e pode forçar a senha caso ela seja curta


#### 5. Rodar o Sistema
bash
Python manage.py runserver





#### 6. acesse o sistema pelo navegador
bash
http://localhost:8000
