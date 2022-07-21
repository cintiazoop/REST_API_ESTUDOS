from flask import Flask
from flask_restful import Api
from resource.prontuario_paciente import Pacientes, Paciente
from resource.cadastro_funcionario import Funcionarios, Funcionario

app = Flask(__name__)
api = Api(app)

api.add_resource(Pacientes, '/pacientes')                                         # endpoints
api.add_resource(Paciente, '/pacientes/<string:numero_prontuario>')

api.add_resource(Funcionarios, '/funcionarios')
api.add_resource(Funcionario, '/funcionarios/<string:numero_funcionario>')




if __name__ == '__main__':
    app.run(debug=True)


# http://127.0.0.1:5000/pacientes
# http://127.0.0.1:5000/funcionarios