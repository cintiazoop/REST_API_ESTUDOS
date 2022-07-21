from flask_restful import Resource


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


class Funcionario(Resource):                                              # essa classe terá as funcionalidades do REST (get, post, put e delete)  -  resource (recursos)
    def get(self, numero_funcionario):                                    # vamos buscar ele pelo numero do prontuario (vamos passar na url)
        for funcionario in funcionarios:
            if funcionario['numero_funcionario'] == numero_funcionario:       # se
                return funcionario

        return {'Message': 'Funcionário not found. '}, 404             # se no for não for encontrado o funcionario, vai devolfer a mensagem de funcionario não encontrado

