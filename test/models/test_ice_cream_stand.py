import pytest

from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    # usei fixture para poder usar sempre os mesmos dados nos meus testes
    @pytest.fixture
    def rest_name(self):
        return "DM Sorvetes Artesanais"

    @pytest.fixture
    def rest_type(self):
        return "Sorveteria"

    @pytest.fixture
    def list_flavors(self):
        return ["Chocolate", "Creme", "Doce de leite", "Leite ninho"]

    @pytest.fixture
    def list_flavors_empty(self):
        return []

    #testar o método que informa quais os sabores disponíveis na minha sorveteria
    def test_flavors_available_success(self,rest_name, rest_type, list_flavors):
        # setup
        icecream = IceCreamStand(rest_name, rest_type, list_flavors)
        texto = "\nNo momento temos os seguintes sabores de sorvete disponíveis:"
        sabores = ""
        for flavor in list_flavors:
            sabores = sabores + "\n\t-" + flavor

        expected_result = texto + "\n" + sabores

        # chamada
        result = icecream.flavors_available()

        # avaliacão
        assert result == expected_result

    #testar o método que informa quais os sabores disponíveis na minha sorveteria, mas a mesma está sem estoque
    def test_flavors_available_list_empty(self, rest_name, rest_type, list_flavors_empty):
        # setup
        icecream = IceCreamStand(rest_name, rest_type, list_flavors_empty)

        expected_result = "Estamos sem estoque atualmente!"

        # chamada
        result = icecream.flavors_available()

        # avaliacão
        assert result == expected_result

    #testar o método que verificar se o sabor que p cliente deseja está disponível.
    def test_find_flavor_success(self,rest_name, rest_type, list_flavors):
        # setup
        icecream = IceCreamStand(rest_name, rest_type, list_flavors)
        flavor = "Leite ninho"

        expected_result = f"Temos no momento {flavor}!"

        # chamada
        result = icecream.find_flavor(flavor)

        # avaliacão
        assert result == expected_result

    #testar o método que verificar se o sabor que p cliente deseja está disponível.
    # mas o sabor está em falta.
    def test_find_flavor_not_available(self,rest_name, rest_type, list_flavors):
        # setup
        icecream = IceCreamStand(rest_name, rest_type, list_flavors)
        flavor = "Graviola"

        expected_result = f"Não temos no momento {flavor}!"

        # chamada
        result = icecream.find_flavor(flavor)

        # avaliacão
        assert result == expected_result

    #testar o método que verificar se o sabor que p cliente deseja está disponível.
    # mas estamos sem estoque
    def test_find_flavor_list_empty(self,rest_name, rest_type, list_flavors_empty):
        # setup
        icecream = IceCreamStand(rest_name, rest_type, list_flavors_empty)
        flavor = "Mangaba"

        expected_result = "Estamos sem estoque atualmente!"

        # chamada
        result = icecream.find_flavor(flavor)

        # avaliacão
        assert result == expected_result

    #testar o método que adiciona um novo sabor ao nosso estoque.
    # Porém esse sabor já está disponível
    def test_add_flavor_already_available(self,rest_name, rest_type, list_flavors):
        # setup
        icecream = IceCreamStand(rest_name, rest_type, list_flavors)
        new_flavor = "Creme"

        expected_result = "\nSabor já disponivel!"

        # chamada
        result = icecream.add_flavor(new_flavor)

        # avaliacão
        assert result == expected_result

    #testar o método que adiciona um novo sabor ao nosso estoque.
    def test_add_flavor_new_flavor(self,rest_name, rest_type, list_flavors):
        # setup
        icecream = IceCreamStand(rest_name, rest_type, list_flavors)
        new_flavor = "Café"
        new_list_flavors = list_flavors.copy()
        new_list_flavors.append(new_flavor)

        expected_result = f"{new_flavor} adicionado ao estoque!"

        # chamada
        result = icecream.add_flavor(new_flavor)

        # avaliacão
        assert result == expected_result
        assert new_list_flavors == list_flavors
        #assert new_list_flavors == icecream.flavors
