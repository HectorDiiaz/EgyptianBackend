from flask import Blueprint, jsonify, request
from flaskext.mysql import MySQL
from config import config
from models.usuario import Usuario
from flask_cors import CORS
from flask import Flask



# Crear el blueprint para el controlador de login
usuario_app = Blueprint('registrarUsuario', __name__)
CORS(usuario_app)
# Método: POST
# Datos de entrada: Se espera un JSON en el cuerpo de la solicitud que contenga el campo
# Datos de salida: Devuelve un JSON con un mensaje indicando que se registró correctamente usuario. En caso de error, devuelve un mensaje de error.
@usuario_app.route('/registrar_usuario', methods=['POST'])
def registrar_usuario():
    try:
        usuario = request.get_json()  # Obtener los datos enviados desde el frontend
        resultado = Usuario.guardar_usuario(usuario)  # Guardar los datos en la base de datos

        return jsonify(resultado)
    except Exception as ex:
        print(f"Error en registrar_usuario: {str(ex)}")
        return jsonify({"mensaje": "Error"})



@usuario_app.route('/modificar_usuario', methods=['PUT'])
def modificar_usuario():
    try:
        usuario = request.get_json()  # Obtener los datos enviados desde el frontend
        resultado = Usuario.actualizar_usuario(usuario)  # Actualizar los datos en la base de datos

        return jsonify(resultado)
    except Exception as ex:
        print(f"Error en modificar_usuario: {str(ex)}")
        return jsonify({"mensaje": "Error"})
    
@usuario_app.route('/eliminar_usuario', methods=['PUT'])
def eliminar_usuario():
        id = request.get_json()  # Obtener los datos enviados desde el frontend
        resultado = Usuario.eliminarUsuario(id)  # Actualizar los datos en la base de datos
        return jsonify(resultado)

@usuario_app.route('/listar_usuarios', methods=['GET'])
def listar_usuarios():
    try:
        usuarios = Usuario.listar_usuarios()

        if usuarios is not None:
            return jsonify({'usuarios': usuarios, 'mensaje': "Lista de usuarios satisfactoria"})
        else:
            return jsonify({"mensaje": "Error"})
    except Exception as ex:
        print(f"Error en listar_usuarios: {str(ex)}")
        return jsonify({"mensaje": "Error"})
    
    
@usuario_app.route('/upload', methods=['POST'])
def upload():
    try:
        imagen = Usuario.upload()
        
        if imagen is not None:
            return jsonify({'usuarios': imagen, 'mensaje': "imagen recibida de manera satisfactoria"})
        else:
            return jsonify({"mensaje": "Error, imagen no recibida o proccesada"})
    except Exception as ex:
        print(f"Error upload: {str(ex)}")
        return jsonify({"mensaje": "Error"})

