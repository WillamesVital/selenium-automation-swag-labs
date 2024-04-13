import conftest
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
                                               
                                                 
@pytest.mark.usefixtures("setup_teardown")
class TestLoginValido:
    def test_login_valido(self):
        # Instancia os objetos a serem usados
        self.driver= conftest.driver
        login_page = LoginPage()
        home_page = HomePage()
        
        login_page.fazer_login("standard_user", "secret_sauce")
        
        home_page.verificar_login_com_sucesso()
