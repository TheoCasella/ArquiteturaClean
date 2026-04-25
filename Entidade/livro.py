'''
Entidades fundamentais
Classes, interfaces, etc
'''

class Livro:
    def __init__(self, id, titular, preco):
        self.id = id
        self.titular = titular
        self.preco = preco

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'autor': self.autor,
            'preco': self.preco
        }