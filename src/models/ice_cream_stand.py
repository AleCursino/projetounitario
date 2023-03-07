from src.models.restaurant import Restaurant

class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        if self.flavors:
            # fiz algumas ateraćões no método para que eu posso imprimir o resultado conforme o método original, mas usando um return (já que o print retorna None)
            texto = "\nNo momento temos os seguintes sabores de sorvete disponíveis:"
            sabores = ""
            for flavor in self.flavors:
                sabores = sabores + "\n\t-" + flavor
            return texto + "\n" + sabores
        else:
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if self.flavors:
            if flavor in self.flavors:
                #estava {self.flavors} no print e dessa maneira mostraria a lista toda.
                # Troquei o print por return e {self.flavors} por {flavor}
                # dessa maneira, vai retornar apenas o sabor que estou pesquisando
                return f"Temos no momento {flavor}!"
            else:
                # mesma coisa do passo anterior, se ficar {self.flavors}, ele vai mostrar a lista de sabores completa
                # também troquei {self.flavors} por {flavor} pra trazer só o sabor q estou buscando
                return f"Não temos no momento {flavor}!"
        else:
           return "Estamos sem estoque atualmente!"

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        #não é preciso validar que tem estoque, por isso retirei um dos if's.
        if flavor in self.flavors:
            return "\nSabor já disponivel!"
        else:
            self.flavors.append(flavor)
            return f"{flavor} adicionado ao estoque!"


