from flask_restful import Resource, reqparse

pacientes = [
    {
        'numero_prontuario': '1',
        'nome': 'Maria',
        'idade': '30'
     },
    {
        'numero_prontuario': '2',
        'nome': 'Pedro',
        'idade': '15'
    }
]


class Pacientes(Resource):                                               # lista todos pacientes
    def get(self):
        return {'pacientes': pacientes}


class Paciente(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('idade')


    def encontrar_paciente(numero_prontuario):
        for paciente in pacientes:
            if paciente['numero_prontuario'] == numero_prontuario:
                return paciente
        return None

    def get(self, numero_prontuario):                                    # vamos buscar ele pelo numero do prontuario (vamos passar na url)
        paciente = Paciente.encontrar_paciente(numero_prontuario)
        if paciente:
            return paciente
        return {'Mensagem': 'Paciente não existe'}, 404


    def post(self, numero_prontuario):
        dados = Paciente.argumentos.parse_args()

        novo_paciente = {
            'numero_prontuario': numero_prontuario,
            'nome': dados['nome'],
            'idade': dados['idade']
        }
        pacientes.append(novo_paciente)
        return novo_paciente, 200


    def put(self, numero_prontuario):
        dados = Paciente.argumentos.parse_args()
        novo_paciente = {'numero_prontuario': numero_prontuario, **dados}
        paciente = Paciente.encontrar_paciente(numero_prontuario)
        if paciente:
            paciente.update(novo_paciente)
            return novo_paciente, 200
        pacientes.append(novo_paciente)
        return novo_paciente, 201

    def delete(self, numero_prontuario):
        global pacientes
        pacientes = [paciente for paciente in pacientes if paciente['numero_prontuario'] != numero_prontuario]
        return {'message': 'Paciente deletado'}



