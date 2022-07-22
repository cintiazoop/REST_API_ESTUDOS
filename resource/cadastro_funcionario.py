from flask_restful import Resource, reqparse

funcionarios = [
    {
        'numero_funcionario': '1',
        'nome': 'Maria',
        'funçao': 'atendente'
     },
    {
        'numero_funcionario': '2',
        'nome': 'Pedro',
        'funçao': 'medico'
    }
]


class Funcionarios(Resource):
    def get(self):
        return {'funcionarios': funcionarios}


class Funcionario(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('funçao')

    def encontrar_funcionario(numero_funcionario):
        for funcionario in funcionarios:
            if funcionario['numero_funcionario'] == numero_funcionario:
                return funcionario
        return None

    def get(self, numero_funcionario):                                    # vamos buscar ele pelo numero do prontuario (vamos passar na url)
        funcionario = Funcionario.encontrar_funcionario(numero_funcionario)
        if funcionario:
            return funcionario
        return {'Mensagem': 'Funcionario não existe'}, 404

    def post(self, numero_funcionario):
        dados = Funcionario.argumentos.parse_args()

        novo_funcionario = {
            'numero_funcionario': numero_funcionario,
            'nome': dados['nome'],
            'funçao': dados['funçao']
        }
        funcionarios.append(novo_funcionario)
        return novo_funcionario, 201

    def put(self, numero_funcionario):
        dados = Funcionario.argumentos.parse_args()
        novo_funcionario = {'numero_funcionario': numero_funcionario, **dados}
        funcionario = Funcionario.encontrar_funcionario(numero_funcionario)
        if funcionario:
            funcionario.update(novo_funcionario)
            return novo_funcionario, 200
        funcionarios.append(novo_funcionario)
        return novo_funcionario, 201

    def delete(self, numero_funcionario):
        global funcionarios
        funcionarios = [funcionario for funcionario in funcionarios if funcionario['numero_funcionario'] != numero_funcionario]
        return {'Mensagem': 'Funcionario deletado'}