'''
Entidades fundamentais
Classes, interfaces, etc
'''

class Livro:
    def __init__(self, id, titulo, autor, preco):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'autor': self.autor,
            'preco': self.preco
        }