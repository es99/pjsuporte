## Pré-requisitos
1. Docker instalado
2. Python version >= 3.10.0, recomendo utilizar o [pyenv](https://github.com/pyenv/pyenv)

## Para roda a aplicação localmente
1. Com o _pyenv_ instalado
    1. ```pyenv versions``` (para listar as versões instalados no diretório)
    2. ```pyenv install 3.10.0``` (para instalar a versão 3.10 no _workdir_)
    3. ```pyenv local 3.10.0``` (para utilizar a versão 3.10 no _workdir_)
    4. ```pyenv virtualenv myenv``` (para criar um ambiente virtual utilizando a versão instalado no _workdir_, ou seja, 3.10)
    5. ```pyenv activate myenv``` (para ativar o ambiente virtual)
    obs.: Não esquecer de adicionar o arquivo oculto _.python-version_ no _.gitignore_
2. ```pip install -r requirements/docker.txt``` (para instalar as dependencias necessarias do flask)
3. Ativar as variáveis de ambientes do flask e do smtp, contidas nos respectivos arquivos _env-flask.sh_ e _env-smtp.sh_
    1. ```source ./env-flask.sh```
    2. ```source ./env-smtp.sh```
4. ```docker-compose up -d``` (para iniciar o container do banco de dados local)
5. ```flask db upgrade``` (para atualizar as tabelas do banco de dados)
6. ```flask run --host 0.0.0.0 --port 8000``` para iniciar o servidor flask na porta 8000 rodando a aplicação no ambiente de desenvolvimento

##### v1.3.6
- Inserido a opção _checkbox_ "Farmácia" na solicitação de cadastro de usuários
- Na mesma página de solicitação de cadastro (/solicita_cadastro) alterado Entidade -> Município, a localização do campo _field_ também foi alterada para sair de baixo do campo _RG_ pois os usuários estavam confundindo _Entidade_ com _orgão expedidor_.

OBS: É preciso criar no servidor de hospedagem da aplicação os arquivos .env e .env-dados, já que estes 
arquivos não são enviados para o repositório remoto por conter dados sensíveis. Além disso, o docker-compose puxa informações das variáveis de ambiente dos arquivos informados.
