# 🚗 Cars

Este projeto foi desenvolvido como parte do curso **PyCode**, com o objetivo de aplicar conceitos aprendidos em **Python** e **Django**.  
A aplicação simula um sistema de gerenciamento de carros, permitindo organizar e visualizar informações de forma prática.

## 📚 Objetivo
O projeto tem caráter **educacional**, servindo como exercício de aprendizado e prática de desenvolvimento web com Django.

## 🛠️ Tecnologias utilizadas
- Python
- Django
- HTML
- CSS

## 📂 Estrutura do projeto
- `accounts/` → Gerenciamento de usuários e autenticação
- `app/` → Configurações principais da aplicação
- `cars/` → Lógica e funcionalidades relacionadas aos carros
- `media/cars/` → Arquivos de mídia (imagens de carros)
- `manage.py` → Script de gerenciamento do Django
+
## 🚀 Como executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/Jullyheder/cars.git
   ```
   ## ⚙️ Configuração do ambiente
   O projeto utiliza variáveis de ambiente para armazenar informações sensíveis (como chaves secretas e configurações).  
   Para configurar corretamente:
   
   1. Faça uma cópia do arquivo `.env-example`:
      ```bash
      cp .env-example .env
      ```
   2. Edite o arquivo .env e adicione suas respectivas chaves e valores, por exemplo:
      ```bash
      SECRET_KEY=sua_chave_secreta
      DEBUG=True
      DATABASE_URL=sqlite:///db.sqlite3
      ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute as migrações:
   ```bash
   python manage.py migrate
   ```
4. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

Acesse em: http://127.0.0.1:8000

🎯 Status
Projeto em desenvolvimento, criado para fins de estudo e prática.

✍️ Desenvolvido por Jullyheder durante o curso PyCode como parte do aprendizado em desenvolvimento web.
