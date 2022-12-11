
# Olá pessoa curiosa.

Esse projeto foi desenvolvido numa máquina que usa como sistema operativo o Windows 10. Por este motivo, todos os comandos do terminal e/ou o powershell são os usados pelo sistema operativo. Caso uses outro sistema, pesquise pelos comandos equivalentes para o seu caso (uma pessoa desenvolvedora precisa de cultivar o hábito da pesquisa, não é mesmo?).

***Nota, todos os comandos usam o terminal do windows, com os perfis powershell ou git bash. Por uma questão de conveniência e para que a aplicação "automagicamente" funcione em qualquer sistema operativo, toda a aplicação foi desenvolvida em docker, desse modo, basta criar as imagens e containers para que a mesma funcione independentemente do sistema operativo utilizado.***

## Pré-requisitos:
* Tests: [PyTest](https://docs.pytest.org)
* Framework: [FastAPI](https://fastapi.tiangolo.com)
* Code Formatter: [Black](https://pypi.org/project/black)
* Version Control: [GitHub](https://github.com/AladinoBorges/lessery_project)
* Code Runner: [CodeRunner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)
* Virtual Environment: [Pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today)
* Task | Job Queue Manager: [Celery](https://docs.celeryq.dev/en/stable)
* Package Manager | Installer: [Pip](https://pypi.org/project/pip)
* Database Image: [Imagem Docker MySQL](https://hub.docker.com/_/mysql)
* Code Style Guide Enforcement: [Flake8](https://pypi.org/project/flake8)
* Programming Language: [Python (>=3.11.1)](https://www.python.org/downloads/release/python-3111)
* ORM (Object Relational Mapper): [SQLAlchemy](https://www.sqlalchemy.org)
* Environment Variables File Reader: [python-dotenv](https://pypi.org/project/python-dotenv)
* Database Design and Management: [MySQL Workbench](https://dev.mysql.com/doc/workbench/en)
* Development Environment: [Docker](https://www.docker.com/get-started) e [Docker Compose](https://docs.docker.com/get-started/08_using_compose)
  
## Instruções para rodar a aplicação backend.

***Atenção: toda a estrutura do backend está contentorizada no Docker, por isso será necessário instalá-lo juntamente com todos os pré-requisitos antes de clonar esse repositório. O MySQL Workbench é usado apenas para ter uma interface visual para a gestão e modelagem do banco de dados. Poderão ser usadas alternativas como [DBeaver](https://dbeaver.io/) por exemplo.***

1. Cole e execute no terminal o seguinte comando para clonar o repositório que contém o código (git bash):
  * ```git clone https://gitlab.com/hh_engineering/backend.git```

2. Execute os seguintes comandos pela ordem que aparecem para instalar todas as dependências do projeto presentes no arquivo Pipfile e inicializar o ambiente de dependências isolado (git bash):
  * ```py -m pip install pipenv```;
  * ```py -m pipenv shell```;
  * ```pipenv install --dev```

3. Iniciar o docker digitando o seguinte comando no terminal (powershell):
  * ```Start-service docker```

4. Execute o seguinte comando para configurar todo o docker (aplicação contentorizada, banco de dados mysql e rodar todos os containers necessários automaticamente) (git bash):
  * ```pipenv run composer:build```

5. Caso a aplicação contentorizada não rode automaticamente na porta 8004, execute o seguinte comando (git bash):
  * ```pipenv run composer:up``` 


***Nota: não é necessário rodar a aplicação backend pois a mesma é instanciada no docker, e todas as alterações efetuadas no código são automaticamente atualizados na aplicação contentorizada.***
