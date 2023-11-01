# from app import app, db
# from flask import request, jsonify
# from app.models import Riesgo

# # Crear un riesgo
# @app.route('/crear_riesgo', methods=['POST'])
# def crear_riesgo():
#     data = request.get_json()

#     nuevo_riesgo = Riesgo(
#         titulo=data['titulo'],
#         descripcion=data['descripcion'],
#         impacto=data['impacto'],
#         probabilidad=data['probabilidad'],
#         proveedor=data['proveedor'],
#         user_id=data['user_id']
#     )

#     db.session.add(nuevo_riesgo)
#     db.session.commit()

#     return jsonify({"mensaje": "Riesgo creado exitosamente"}), 201

# # Leer un riesgo
# @app.route('/riesgo/<int:riesgo_id>', methods=['GET'])
# def obtener_riesgo(riesgo_id):
#     riesgo = Riesgo.query.get(riesgo_id)

#     if riesgo is None:
#         return jsonify({"mensaje": "Riesgo no encontrado"}), 404

#     return jsonify({
#         "id": riesgo.id,
#         "titulo": riesgo.titulo,
#         "descripcion": riesgo.descripcion,
#         "impacto": riesgo.impacto,
#         "probabilidad": riesgo.probabilidad,
#         "proveedor": riesgo.proveedor,
#         "user_id": riesgo.user_id
#     }), 200

# # Actualizar un riesgo
# @app.route('/riesgo/<int:riesgo_id>', methods=['PUT'])
# def actualizar_riesgo(riesgo_id):
#     data = request.get_json()
#     riesgo = Riesgo.query.get(riesgo_id)

#     if riesgo is None:
#         return jsonify({"mensaje": "Riesgo no encontrado"}), 404

#     riesgo.titulo = data['titulo']
#     riesgo.descripcion = data['descripcion']
#     riesgo.impacto = data['impacto']
#     riesgo.probabilidad = data['probabilidad']
#     riesgo.proveedor = data['proveedor']
#     riesgo.user_id = data['user_id']

#     db.session.commit()

#     return jsonify({"mensaje": "Riesgo actualizado exitosamente"}), 200


# # Eliminar un riesgo
# @app.route('/riesgo/<int:riesgo_id>', methods=['DELETE'])
# def eliminar_riesgo(riesgo_id):
#     riesgo = Riesgo.query.get(riesgo_id)

#     if riesgo is None:
#         return jsonify({"mensaje": "Riesgo no encontrado"}), 404

#     db.session.delete(riesgo)
#     db.session.commit()

#     return jsonify({"mensaje": "Riesgo eliminado exitosamente"}), 200

from app import app, db
from models.riesgos import Riesgo, riesgo_schema, riesgos_schema
from flask import request, jsonify
from services.jwt import auth_required
from utils.utils import success_response, error_response

# Crear un riesgo
@app.route('/crear_riesgo', methods=['POST'])
@auth_required
def crear_riesgo():
    data = request.get_json()

    nuevo_riesgo = Riesgo(
        titulo=data['titulo'],
        descripcion=data['descripcion'],
        impacto=data['impacto'],
        probabilidad=data['probabilidad'],
        proveedor=data['proveedor'],
        user_id=data['user_id']
    )

    db.session.add(nuevo_riesgo)
    db.session.commit()

    return jsonify({"mensaje": "Riesgo creado exitosamente"}), 201

# Leer todos los riesgos
@app.route('/riesgo', methods=['GET'])
@auth_required
def get_all_riesgos():
    riesgos = Riesgo.query.all()
    return riesgos_schema.jsonify(riesgos), 200


# Leer un riesgo
@app.route('/riesgo/<id>', methods=['GET'])
# @auth_required
def get_riesgo(id):
    riesgo = Riesgo.query.get(id)

    if riesgo is None:
        return jsonify({"mensaje": "Riesgo no encontrado"}), 404

    return jsonify({
        "id": riesgo.id,
        "titulo": riesgo.titulo,
        "descripcion": riesgo.descripcion,
        "impacto": riesgo.impacto,
        "probabilidad": riesgo.probabilidad,
        "proveedor": riesgo.proveedor,
        "user_id": riesgo.user_id
    }), 200

# Actualizar un riesgo
@app.route('/riesgo/<id>', methods=['PUT'])
@auth_required
def actualizar_riesgo(id):
    data = request.get_json()
    riesgo = Riesgo.query.get(id)

    if riesgo is None:
        return jsonify({"mensaje": "Riesgo no encontrado"}), 404

    riesgo.titulo = data['titulo']
    riesgo.descripcion = data['descripcion']
    riesgo.impacto = data['impacto']
    riesgo.probabilidad = data['probabilidad']
    riesgo.proveedor = data['proveedor']
    riesgo.user_id = data['user_id']

    db.session.commit()

    return riesgo_schema.jsonify(riesgo)

# Eliminar un riesgo
@app.route('/riesgo/<id>', methods=['DELETE'])
@auth_required
def eliminar_riesgo(id):
    riesgo = Riesgo.query.get(id)

    if riesgo is None:
        return jsonify({"mensaje": "Riesgo no encontrado"}), 404

    db.session.delete(riesgo)
    db.session.commit()

    return jsonify({"mensaje": "Riesgo eliminado exitosamente"}), 200

@app.route('/')
def hello():
    return 'hola mundo'