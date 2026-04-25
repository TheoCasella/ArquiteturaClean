'''
Armazenamento e recuperação de dados
'''
from Entidade.livro_repository_interface import ILivroRepository
import os

class LivroRepositoryTXT(ILivroRepository):
    def __init__(self, arquivo="database.txt"):
        self.arquivo = arquivo
        #Caso o arquivo database.txt nao exista, ele cria
        if not os.path.exists(self,arquivo):
            with open(self.arquivo,"r") as f:
                pass
    #arquivo .txt --> lista de objetos 'livros'
    def obter_todos(self):
        livros = []
        with open(self.arquivo,"r") as f:
            for linha in f:
                partes = linha.strip().split(";")
                if len(partes) == 4:
                    livros.append(Livro(partes[0], partes[1], partes[2], float(partes[3])))
        return livros
    #lista de objetos 'livros' --> arquivo .txt
    def salvar_todos(self, livros):
        with open(self.arquivo,"w") as f:
            for livro in livros:
                f.write(f"{livro.id};{livro.titulo};{livro.autor};{livro.preco}\n")