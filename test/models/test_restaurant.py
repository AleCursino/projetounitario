import pytest

from src.models.restaurant import Restaurant


class TestRestaurant:

    #usei fixture para poder usar sempre os mesmos dados nos meus testes
    @pytest.fixture
    def rest_name(self):
        return "DM Doces Saudáveis"

    @pytest.fixture
    def rest_type(self):
        return "Doceria Saudável"

    #teste para o describe_restaurant
    def test_describe_restaurant(self, rest_name, rest_type):
        # setup
        restaurant = Restaurant(rest_name, rest_type)
        expected_result = f"Esse restaurante chama-se {rest_name} e serve {rest_type}.\n O restaturante está servindo {restaurant.number_served} consumidores desde que está aberto."

        #chamada
        result = restaurant.describe_restaurant()

        #avaliacão
        assert result == expected_result

    # testar o open_restaurant quando o restaurante está fechado ainda e a abertura acontecerá com sucesso
    def test_open_restaurant_success(self, rest_name, rest_type):
        # setup
        restaurant = Restaurant(rest_name, rest_type)
        expected_result = f"{rest_name} agora está aberto!"

        #chamada
        result = restaurant.open_restaurant()

        #avaliacão
        assert result == expected_result
        assert restaurant.open is True
        assert restaurant.number_served == 0

    # testar o open_restaurant quando o restaurante já está aberto
    def test_open_restaurant_opened(self, rest_name, rest_type):
        # setup
        restaurant = Restaurant(rest_name, rest_type)
        restaurant.open_restaurant()
        expected_result = f"{rest_name} já está aberto!"

        # chamada
        result = restaurant.open_restaurant()

        # avaliacão
        assert result == expected_result
        assert restaurant.open is True

    # testar o close_restaurant quando o restaurante está aberto e será fechado com sucesso
    def test_close_restaurant_success(self, rest_name, rest_type):
        # setup
        restaurant = Restaurant(rest_name, rest_type)
        restaurant.open_restaurant()
        expected_result = f"{rest_name} agora está fechado!"

        # chamada
        result = restaurant.close_restaurant()

        # avaliacão
        assert result == expected_result
        assert restaurant.open is False
        assert restaurant.number_served == 0

    # testar o close_restaurant quando o restaurante já está fechado
    def test_close_restaurant_closed(self, rest_name, rest_type):
        # setup
        restaurant = Restaurant(rest_name, rest_type)
        expected_result = f"{rest_name} já está fechado!"

        # chamada
        result = restaurant.close_restaurant()

        # avaliacão
        assert result == expected_result
        assert restaurant.open is False

    #testar o método que valida se o número de consumidores é um inteiro maior que zero.
    def test_valid_num_costumers_int(self, rest_name, rest_type):
        # setup
        restaurant = Restaurant(rest_name, rest_type)
        num_customers = 25
        expected_result = True

        # chamada
        result = restaurant.valid_num_costumers(num_customers)

        # avaliacão
        assert result == expected_result

    # testar o método que valida se o número de consumidores é um inteiro maior que zero.
    # porém informando uma string
    def test_valid_num_costumers_str(self, rest_name, rest_type):
        # setup
        restaurant = Restaurant(rest_name, rest_type)
        num_customers = "muitos"
        expected_result = False

        # chamada
        result = restaurant.valid_num_costumers(num_customers)

        # avaliacão
        assert result == expected_result

    # testar o método que valida se o número de consumidores é um inteiro maior que zero.
    # porém informando um inteiro menor que zero
    def test_valid_num_costumers_negative(self, rest_name, rest_type):
        # setup
        restaurant = Restaurant(rest_name, rest_type)
        num_customers = -2
        expected_result = False

        # chamada
        result = restaurant.valid_num_costumers(num_customers)

        # avaliacão
        assert result == expected_result

    # testar o método que valida se o número de consumidores é um inteiro maior que zero.
    # porém informando None no lugar do número válido
    def test_valid_num_costumers_none(self, rest_name, rest_type):
        # setup
        restaurant = Restaurant(rest_name, rest_type)
        num_customers = None
        expected_result = False

        # chamada
        result = restaurant.valid_num_costumers(num_customers)

        # avaliacão
        assert result == expected_result

    # testar o método que define o número total de consumidores atendidos num dia, com o restaurante aberto.
    def test_set_number_served_success(self, rest_name, rest_type):
        # setup
        restaurant = Restaurant(rest_name, rest_type)
        customers = 30
        restaurant.open_restaurant()
        expected_result = f"O número de consumidores agora é {customers}!"

        # chamada
        result = restaurant.set_number_served(customers)

        # avaliacão
        assert result == expected_result
        assert restaurant.number_served == customers

    # testar o método que define o número total de consumidores atendidos num dia, com o restaurante fechado.
    def test_set_number_served_closed(self, rest_name, rest_type):
        # setup
        restaurant = Restaurant(rest_name, rest_type)
        customers = 30
        expected_result = f"{rest_name} está fechado!"

        # chamada
        result = restaurant.set_number_served(customers)

        # avaliacão
        assert result == expected_result
        assert restaurant.number_served == 0

    # testar o método que define o número total de consumidores atendidos num dia, com o restaurante aberto.
    # Porém passando um número num formato incorreto
    # Só vou fazer um teste para isso porque já fiz testes para o método valid_num_costumers(self, num_customers)
    # que é chamado no método a ser testado
    def test_set_number_served_invalid_str(self, rest_name, rest_type):
        # setup
        restaurant = Restaurant(rest_name, rest_type)
        customers = "20"
        restaurant.open_restaurant()
        expected_result = "Total de consumidores inválido"

        # chamada
        result = restaurant.set_number_served(customers)

        # avaliacão
        assert result == expected_result
        assert restaurant.number_served == 0

    # testar o método que incrementa o número de consumidores atendidos, com o restaurante aberto.
    def test_increment_number_served_success(self, rest_name, rest_type):
        # setup
        restaurant = Restaurant(rest_name, rest_type)
        more_customers = 30
        restaurant.open_restaurant()
        total = restaurant.number_served + more_customers
        expected_result = f"O número de consumidores agora é {total}!"

        # chamada
        result = restaurant.increment_number_served(more_customers)

        # avaliacão
        assert result == expected_result
        assert restaurant.number_served == total

    # testar o método que incrementa o número de consumidores atendidos, com o restaurante fechado.
    def test_increment_number_served_closed(self, rest_name, rest_type):
        # setup
        restaurant = Restaurant(rest_name, rest_type)
        more_customers = 30
        total = restaurant.number_served + more_customers
        expected_result = f"{rest_name} está fechado!"

        # chamada
        result = restaurant.increment_number_served(more_customers)

        # avaliacão
        assert result == expected_result
        assert restaurant.number_served == 0

    # testar o método que incrementa o número de consumidores atendidos, com o restaurante aberto.
    # Porém passando um número num formato incorreto
    # Só vou fazer um teste para isso porque já fiz testes para o método valid_num_costumers(self, num_customers)
    # que é chamado no método a ser testado
    def test_increment_number_served_float(self, rest_name, rest_type):
        # setup
        restaurant = Restaurant(rest_name, rest_type)
        more_customers = 2.20
        restaurant.open_restaurant()
        #nao preciso do total pq não entra no primeiro if do método
        #total = restaurant.number_served + more_customers
        expected_result = "Total de consumidores inválido"

        # chamada
        result = restaurant.increment_number_served(more_customers)

        # avaliacão
        assert result == expected_result
        #assert restaurant.number_served == 0
