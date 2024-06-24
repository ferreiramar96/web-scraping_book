class Content:
    """
    Classe-base comum para todos os artigos/páginas
    """
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body
        
    def print(self):
        """
        Uma função flexível de exibição controla a saída
        """
        print("URL: {}".format(self.url))
        print("TITLE: {}".format(self.title))
        print("BODY:\n{}".format(self.body))


"""a classe Website não armazena informações coletadas das
páginas individuais, mas instruções sobre como coletar esses dados."""
'''Ao usar as classes Content e Website, podemos então escrever um Crawler para
coletar o título e o conteúdo de qualquer URL fornecido para uma dada
página web de um dado site'''


class Website:
    """
    Contém informações sobre a estrutura do site
    """
    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag

teste = Content('1', '2', '3')
print(teste.print())