## Pré-requisitos
1. Docker instalado

## Para roda a aplicação localmente
1. Ativar o ambiente virtual (conda ou venv)
2. docker-compose up -d (para iniciar o container do banco de dados local)
3. pip install -r requirements/docker.txt (para instalar as dependencias necessarias do flask)
4. flask db upgrade (para atualizar as tabelas do banco de dados)

OBS: É preciso criar no servidor de hospedagem da aplicação os arquivos .env e .env-dados, já que estes 
arquivos não são enviados para o repositório remoto por conter dados sensíveis. Além disso, o docker-compose puxa informações das variáveis de ambiente dos arquivos informados.
