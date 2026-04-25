'''
Lógica de negócio
'''


# UseCases/aplicar_desconto.py

class AplicarDescontoUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.ja_foi_aplicado = False

    def executar(self, percentual):
        if self.ja_foi_aplicado:
            raise Exception("O desconto já foi aplicado nesta sessão!")

        livros = self.repositorio.obter_todos()

        for livro in livros:
            livro.preco *= (1 - percentual / 100)

        self.repositorio.salvar_todos(livros)

        self.ja_foi_aplicado = True

        return [livro.to_dict() for livro in livros]