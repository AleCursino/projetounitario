class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        # retirei .title() para colocar letras maiúsculas e minúsculas sem problemas no nome do meu restaurante
        #self.restaurant_name = restaurant_name.title()
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    #troquei TODOS os prints por return em cada método, já que os prints não retornam nada.

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        #Uma mensagem está fazendo referência incorreta, imprimindo o tipo no lugar do nome. Foi corrigido
        #corrigi a palavra restaurante e troquei o and pelo e.
        # troquei os prints pelo return pq os prints retornam None.
        # juntei as duas frases numa só
        return f"Esse restaurante chama-se {self.restaurant_name} e serve {self.cuisine_type}.\n O restaturante está servindo {self.number_served} consumidores desde que está aberto."

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        #alterei os prints pelo return
        if not self.open:
            #considerei aberto como True
            self.open = True
            #troquei o number_served de -2 para 0 consumidores
            self.number_served = 0
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        # alterei os prints pelo return
        if self.open:
            self.open = False
            self.number_served = 0 #é reduntante??
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"

    #novo método para fazer validacoes necessarias no número de consumidores
    #servirá para uso nos métodos set_number_served e increment_number_served
    def valid_num_costumers(self, num_customers):
        if type(num_customers) is int and num_customers >= 0:
            return True
        else:
            return False

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        #considerei que o método vai contar o número de pessoas atendidas durante o dia!!!
        # alterei os prints pelo return
        # acrescentei o metodo para verificar se o valor  inserido é um inteiro
        if self.valid_num_costumers(total_customers):
            if self.open:
                self.number_served = total_customers
                return f"O número de consumidores agora é {self.number_served}!"
            else:
                return f"{self.restaurant_name} está fechado!"
        else:
            return "Total de consumidores inválido"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        # do jeito que estava, estava igual ao método anterior, para incremetar, eu coloquei self.number_served += more_customers
        # alterei os prints pelo return
        # acrescentei o metodo para verificar se o valor  inserido é um inteiro
        if self.valid_num_costumers(more_customers):
            if self.open:
                self.number_served += more_customers
                return f"O número de consumidores agora é {self.number_served}!"
            else:
                return f"{self.restaurant_name} está fechado!"
        else:
            return "Total de consumidores inválido"