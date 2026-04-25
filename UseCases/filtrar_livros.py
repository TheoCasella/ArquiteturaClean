'''
Lógica de negócio
'''

class FiltrarLivroUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def executar(self, termo):
        todos = self.repositorio.obter_todos()
        if not termo:
            return [livro.to_dict() for livro in todos]

        termo_lower = termo.lower()
        return [
            livro.to_dict() for livro in todos
            if termo_lower in livro.titulo.lower() or termo_lower in livro.autor.lower()
        ]