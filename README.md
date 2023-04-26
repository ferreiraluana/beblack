# Reuso de Software
## _Projeto BeBlack_

O software desenvolvido é um site de vendas de maquiagens da marca BeBlack, criado em Python utilizando o framework Django, com a arquitetura MVC, banco de dados SQL, API request e microsserviços. O objetivo principal é oferecer uma experiência 
de compra agradável e eficiente para os clientes, seguindo as práticas de reuso de software e suas aplicações, bem como a metodologia ágil Scrum.
--
[![](https://github.com/ferreiraluana/beblack/blob/main/be_black-removebg-preview.png)](https://github.com/ferreiraluana/beblack/blob/main/be_black-removebg-preview.png)
--
>> Antes de rodar a aplicação, verifique se todas as bibliotecas necessárias estão instaladas na sua máquina!
```sh
pip install -r requirements.txt
```

### Instruções para rodar o projeto
Na pasta raiz, ative o ambiente virtual:
```sh
activate
```
Retorne para a pasta principal digitando o comando a seguir duas vezes:
```sh
cd ..
```
Entre na pasta API:
```sh
cd API
```
Configure o Flask para rodar aplicação:
```sh
set FLASK_APP=app.py
```
Run Flask:
```sh
flask run
```
Em outro terminal, entre na pasta `FrontEnd`:
```sh
cd FrontEND
```
Rode o servidor:
```sh
python manage.py runserver
```
Siga o endereço da aplicação:
```sh
http://127.0.0.1:8000/
```




