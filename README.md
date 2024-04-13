# Projeto de Automação de Testes com Selenium e Python para o Site Saucedemo


## Objetivo

<details>

<summary> Clique para expandir o menu sobre o objetivo do projeto </summary>

Esse projeto inicia com o curso de [Automação de Testes Web com Selenium Webdriver e Python](https://www.udemy.com/course/automacao-de-testes-selenium-webdriver-python/?couponCode=KEEPLEARNING) onde usamos o site [Swag Labs](https://www.saucedemo.com/). Como o curso aborda apenas ensinar os principais básicos e alguns poucos conceitos avançados do Selenium Webdriver com Python, devido a isso poucos fluxos são feitos e automatizados, então decidi expandir e torna-lo em um projeto de automação mais completo, onde irei automatizar os fluxos do site todo, juntamente com um Test Map onde estarão todos os casos de teste.

</details>

## Instalando o Framework

<details>

<summary> Clique para expandir o menu sobre a instalação do framework </summary>

### Python

1. Baixe  e instale o Python no site oficial,([baixe a última versão disponivél](https://www.python.org/downloads/))
2. Para IDE eu usei o [VS Code](https://code.visualstudio.com/), mas voce também pode usar o [PyCharm](https://www.jetbrains.com/pt-br/pycharm/)

### Criar Ambiente Virtual Python

1. Abra o VS Code na pasta do projeto.
2. No Terminal do VS Code rode o comando; `python -m venv venv`. Esse segundo venv é o nome do ambiente que você pode colocar qualquer nome. Note que uma pasta com o nome do ambiente será criada.
3. Para utilizarmos o ambiente do projeto precisar ativar o ambiente virtual com o comando `venv\Scripts\Activate.ps1`. Você precisará ativar sempre que abrir o projeto.

### Configurar o Selenium Webdriver

1. Acesse o site oficial e escolha o Selenium para o [Python](https://pypi.org/project/selenium/). Copie o comando e use no terminal.
   1. lembre-se de estar com o ambiente virtual ativado.
   2. Para ver se o Selenium foi instalado `pip show selenium`.

</details>

## Estrutura das Pastas

<details>

<summary> Clique para expandir o menu sobre a estrutura das pastas </summary>

1. Algumas pastas serão criadas as quais não serão e não recomando enviar para seu projeto no Github. Então você pode criar um arquivo `.gitignore` e adicionar essas pastas, são elas: pycache, .pytest_cache, venv(no caso a pasta do seu ambiente virtual).
2. Voce só precisará criar as seguintes pastas; __tests__ - Dentro dessa pasta estarão os arquivos de testes. __pages__ - Nesta pasta estarão seus arquivos de page objects.


</details>

## Test Map

<details>

<summary> Clique para expandir o menu sobre o test map </summary>


| Descrição de Teste  | Testcase | Status |
| ------------- | ------------- | ------------- |
| Verifique que é possivél efetuar login                              | test_login_valido                 | Automated |
| Verifique a mensagem de erro ao efetuar o login com a senha errada  | test_login_invalido               | Automated |
| Verifique que é possivél adicionar itens ao carrinho                | test_adicionar_produtos_carrinho  | Automated |
| Verifique que é possivél concluir uma compra                        | test_efetuar_compra               | Needs Automation |


</details>
