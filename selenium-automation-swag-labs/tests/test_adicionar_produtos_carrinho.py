import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
                                                                                                                    

@pytest.mark.usefixtures("setup_teardown")
class TestAdicionarProdutosCarrinho:
    def test_adicionar_produtos_carrinho(self):
        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()

        produto_1 = "Sauce Labs Backpack"
        produto_2 = "Sauce Labs Bike Light"
        
        # Dado que o login é feito com sucesso
        login_page.fazer_login("standard_user", "secret_sauce")
        home_page.verificar_login_com_sucesso()

        # Quando adiciona itens ao carrinho
        home_page.adicionar_item_ao_carrinho(produto_1)
        home_page.acessar_carrinho()
        cart_page.click_continue_shopping() 
        home_page.adicionar_item_ao_carrinho(produto_2)
        
        home_page.acessar_carrinho()
        # Então os itens adiconados devem estar visivéis no carrinho
        cart_page.verificar_produto_carrinho_existe(produto_1)
        cart_page.verificar_produto_carrinho_existe(produto_2)
        