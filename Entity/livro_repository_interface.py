'''
Entidades fundamentais
Classes, interfaces, etc
'''
from abc import ABC, abstractmethod

class ILivroRepository(ABC):
    @abstractmethod
    def obter_todos(self):
        """Deve retornar uma lista de objetos Livro"""
        pass

    @abstractmethod
    def salvar_todos(self, livros):
        """Deve receber uma lista de objetos Livro e persistir"""
        pass