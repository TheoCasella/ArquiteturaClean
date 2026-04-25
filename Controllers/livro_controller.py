'''
Gerencia o fluxo das requisições
'''

from flask import Blueprint, request, jsonify, render_template

class LivroController:
    def __init__(self, filtrar_use_case, desconto_use_case):
        self.filtrar_use_case = filtrar_use_case
        self.desconto_use_case = desconto_use_case
        self.blueprint = Blueprint('livro', __name__)
        self._configurar_rotas()

    def _configurar_rotas(self):
        @self.blueprint.route('/')
        def index():
            return render_template('index.html')

        @self.blueprint.route('/api/buscar')
        def buscar():
            termo = request.args.get('q', '')
            resultado = self.filtrar_use_case.executar(termo)
            return jsonify(resultado)

        @self.blueprint.route('/api/promocao', methods=['POST'])
        def promocao():
            try:
                resultado = self.desconto_use_case.executar(10)
                return jsonify(resultado)
            except Exception as e:
                return jsonify({"status": "erro", "mensagem": str(e)}), 400