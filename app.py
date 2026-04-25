from flask import Flask
from Infraestrutura.livro_repository_txt import LivroRepositoryTXT
from UseCases.filtrar_livros import FiltrarLivroUseCase
from UseCases.aplicar_desconto import AplicarDescontoUseCase
from Controllers.livro_controller import LivroController

app = Flask(__name__)

repositorio = LivroRepositoryTXT()

filtrar_uc = FiltrarLivroUseCase(repositorio)
desconto_uc = AplicarDescontoUseCase(repositorio)

livro_controller = LivroController(filtrar_uc, desconto_uc)

app.register_blueprint(livro_controller.blueprint)

if __name__ == '__main__':
    app.run(debug=True)