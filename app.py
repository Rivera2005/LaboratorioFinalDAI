"""API REST del catálogo de libros."""
from flask import Flask, jsonify, request
from database import (
    obtener_libros, obtener_libro_por_id, insertar_libro,
    actualizar_libro, eliminar_libro
)

app = Flask(__name__)

@app.get("/")
def inicio():
    return jsonify({"mensaje": "API de libros en funcionamiento"}), 200

@app.get("/libros")
def listar_libros():
    return jsonify(obtener_libros()), 200

@app.get("/libros/<int:libro_id>")
def consultar_libro(libro_id):
    libro = obtener_libro_por_id(libro_id)
    if libro is None:
        return jsonify({"error": "Libro no encontrado"}), 404
    return jsonify(libro), 200

@app.post("/libros")
def insertar():
    libro = request.json
    resultado = insertar_libro(libro)
    return jsonify(resultado), 201

@app.put("/libros/<int:id>")
def actualizar(id):
    libro = request.json
    resultado = actualizar_libro(id, libro)
    return jsonify(resultado), 200

@app.delete("/libros/<int:id>")
def eliminar(id):
    resultado = eliminar_libro(id)
    return jsonify(resultado), 200

@app.errorhandler(Exception)
def manejar_error(error):
    # Durante el laboratorio permite observar errores sin ocultarlos completamente.
    return jsonify({"error": str(error)}), 500

if __name__ == "__main__":
    app.run(debug=True)
