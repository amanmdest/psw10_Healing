<div align="center">
  <img src="templates/static/geral/img/logo.png" alt="gerenciar" width="80"/>
  <h1>Healing</h1>
</div>
<p align='center'>Plataforma de telemedicina, agendamento e realização de consultas médicas, desenvolvida durante a décima edição do evento PyStack Week, conduzido pelo professor Caio Sampaio.</p>

<div align='center'>
  <img alt="Django" src="https://img.shields.io/badge/Django-092E20.svg?&logo=django&logoColor=green">
  <img alt="SQLite" src="https://img.shields.io/badge/SQLite-07405E?style=flat&compact=true&logo=sqlite&logoColor=white">
  <img alt="Creative Commons License" src="https://img.shields.io/badge/License-Creative%20Commons-red">
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/amanmdest/psw3_Freelaway?color=purple">
</div>

## Interface da Aplicação
<kbd>
  <img src="media/home.png" alt="home" width="280"/>
</kbd>
<kbd>
  <img src="media/escolher_horario.png" alt="gerenciar" width="280"/>
</kbd>  
</kbd>
<kbd>
  <img src="media/minhas_consultas.png" alt="novo_valor" width="280"/>
</kbd>  
<kbd>
  <img src="media/cadastrar_medico.png" alt="definir_contas" width="280"/>  
</kbd>
<kbd>  
  <img src="media/abrir_horario.png" alt="ver_contas" width="280"/>  
</kbd>
<kbd>
  <img src="media/consultas_medico.png" alt="ver_planejamento" width="280"/>  
</kbd>
<kbd>
  <img src="media/consulta_area_medico.png" alt="dashboard" width="280"/>  
</kbd>
<kbd>
  <img src="media/login.png" alt="login" width="280"/>  
</kbd>  
<kbd>
  <img src="media/cadastro.png" alt="cadastro" width="280"/>  
</kbd>  

## Rode localmente
1. Clone o repositório:
```
  git clone https://github.com/amanmdest/psw10_Healing.git
```
2. Crie e ative um *virtualenv*(Linux):
```
  python -m venv venv
  source venv/bin/activate
```
3. Instale as dependências:
```
  pip install -r requirements.txt
```
4. Migrações Banco de Dados:
```
  python manage.py makemigrations
  python manage.py migrate
```
5. Para poder usar o painel do admin é preciso criar um superuser:
```
  python manage.py createsuperuser
```
6. Rode o projeto localmente:
```
  python manage.py runserver
```
e acesse: http://127.0.0.1:8000/
