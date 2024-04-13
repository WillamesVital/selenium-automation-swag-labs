from selenium.webdriver.common.by import By
import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class TestLoginInvalido:
    def test_login_invalido(self):
        
        mensagem_erro_esperada = "Epic sadface: Username and password do not match any user in this service"
        login_page = LoginPage()
        login_page.fazer_login("standard_user", "password_invalid")
        
        login_page.verificar_messagem_erro_login_existe()
        login_page.verificar_texto_mensagem_erro_login(mensagem_erro_esperada)
        