from flask import Flask, render_template, request, redirect
import requests
import json

app = Flask(__name__)
API_URL = "http://127.0.0.1:8000/api/"
TOKEN = "75fb6a21ae8e4795ccc3c3f502eebc2731337de7"
HEADERS = {"Authorization": f"Token {TOKEN}"}

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/edificios')
def listar_edificios():
    response = requests.get(f"{API_URL}edificios/", headers=HEADERS)
    data = response.json()
    edificios = data['results']
    numero_edificios = data['count']
    return render_template('edificios.html', edificios=edificios, numero_edificios=numero_edificios)

@app.route('/departamentos')
def listar_departamentos():
    r = requests.get(f"{API_URL}departamentos/", headers=HEADERS)
    departamentos = json.loads(r.content)['results']
    numero_departamentos = json.loads(r.content)['count']
    return render_template('departamentos.html', departamentos=departamentos, numero_departamentos=numero_departamentos)

@app.route('/crear-edificio', methods=['POST'])
def crear_edificio():
    data = {
        "nombre": request.form['nombre'],
        "direccion": request.form['direccion'],
        "ciudad": request.form['ciudad'],
        "tipo": request.form['tipo']
    }
    requests.post(f"{API_URL}edificios/", headers=HEADERS, data=data)
    return redirect('/edificios')

@app.route('/crear-departamento', methods=['POST'])
def crear_departamento():
    data = {
        "nombre_completo": request.form['nombre_completo'],
        "costo_departamento": request.form['costo'],
        "numero_cuartos": request.form['cuartos'],
        "edificio": request.form['edificio_url']  # Debe ser la URL completa
    }
    requests.post(f"{API_URL}departamentos/", headers=HEADERS, data=data)
    return redirect('/departamentos')

if __name__ == '__main__':
    app.run(debug=True)
