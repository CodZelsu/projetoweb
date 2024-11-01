class numeroquarto:
    def __init__ (self, numeroquarto, ativo):
        self.numeroquarto = numeroquarto

    def desativar (self):
        self.ativo = False
        print ("O quarto foi desativado com sucesso")
                
if __name__ == "__main__":
            numeroquarto2=numeroquarto ("numero", True)
            numeroquarto2.desativar ()