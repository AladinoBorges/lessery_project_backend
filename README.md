
# Olá pessoa curiosa.

Esse projeto foi desenvolvido numa máquina que usa como sistema operativo o Windows 10. Por este motivo, todos os comandos do terminal e/ou o powershell são os usados pelo sistema operativo. Caso uses outro sistema, pesquise pelos comandos equivalente para o seu caso (uma pessoa desenvolvedora precisa de cultivar o hábito da pesquisa, não é mesmo?).

***Nota, todos os comandos usam o terminal do windows, com os perfis powershell ou git bash.***

## Pré-requisitos:
* Tests: [PyTest](https://docs.pytest.org)
* Framework: [FastAPI](https://fastapi.tiangolo.com)
* Code Runner: [CodeRunner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)
* Database Image: [Imagem Docker MySQL](https://hub.docker.com/_/mysql)
* Code Formatter: [Black](https://pypi.org/project/black)
* Version Control: [GitHub](https://github.com/AladinoBorges/lessery_project)
* Virtual Environment: [Pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today)
* Programming Language: [Python (>=3.11.1)](https://www.python.org/downloads/release/python-3111)
* Development Environment: [Docker](https://www.docker.com/get-started)
* Task | Job Queue Manager: [Celery](https://docs.celeryq.dev/en/stable)
* Package Manager | Installer: [Pip](https://pypi.org/project/pip)
* Code Style Guide Enforcement: [Flake8](https://pypi.org/project/flake8)
* ORM (Object Relational Mapper): [SQLAlchemy](https://www.sqlalchemy.org)
* Database Design and Management: [MySQL Workbench](https://dev.mysql.com/doc/workbench/en)
* Environment Variables File Reader: [python-dotenv](https://pypi.org/project/python-dotenv)
  
## Instruções para rodar a aplicação backend.

### ***Atenção: toda a estrutura do backend está contentorizada no Docker, por isso será necessário instalá-lo juntamente com todos os pré-requisitos antes de clonar esse repositório. O MySQL Workbench é usado apenas para ter uma interface visual para a gestão e modelagem do banco de dados. Poderão ser usadas alternativas como [DBeaver](https://dbeaver.io/) por exemplo.***

1. Cole e execute no terminal o seguinte comando para clonar o repositório que contém o código (git bash):
```git clone https://gitlab.com/hh_engineering/backend.git```

2. Execute o comando para instalar todas as dependências do projeto presentes no arquivo Pipfile (git bash):
```pipenv install```

3. Execute o comando para ativar o virtual env do projeto (git bash):
```pipenv shell```

3. Iniciar o docker digitando o seguinte comando no terminal (powershell):
```Start-service docker```

4. No repositório clonado, baixar a imagem MySQL (git bash):
```docker pull mysql```

5. Executar o container Docker para a conexão com o banco de dados (git bash): 
```docker run -p 8080:8080 -e MYSQL_PASSWORD=a_sua_senha_do_banco_de_dados mysql```

6. Utilizando um terminal a parte (ainda no repositório clonado) solicitar a conexão do banco de dados ao docker:
 ```pipenv run dev```
