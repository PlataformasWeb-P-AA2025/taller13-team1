
from flask import Flask, render_template, request, redirect
import requests
import json

app = Flask(__name__)

API_URL = "http://127.0.0.1:8000/api/"
TOKEN = "c77618c0beaece0b61a52db8a3dc16095fdf67b7"
HEADERS = {"Authorization": f"Token {TOKEN}"}

@app.route('/')
def index():
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
    response = requests.get(f"{API_URL}departamentos/", headers=HEADERS)
    data = response.json()
    departamentos = data['results']
    numero_departamentos = data['count']
    return render_template('departamentos.html', departamentos=departamentos, numero_departamentos=numero_departamentos)

@app.route('/crear_edificio', methods=['GET', 'POST'])
def crear_edificio():
    if request.method == 'POST':
        data = {
            'nombre': request.form['nombre'],
            'direccion': request.form['direccion'],
            'ciudad': request.form['ciudad'],
            'tipo': request.form['tipo'],
        }
        r = requests.post(f"{API_URL}edificios/", headers=HEADERS, data=data)
        print("POST /edificios:", r.status_code, r.text)
        return redirect('/edificios')
    return render_template('crear_edificio.html')

@app.route('/crear_departamento', methods=['GET', 'POST'])
def crear_departamento():
    r = requests.get(f"{API_URL}edificios/", headers=HEADERS)
    edificios = r.json()['results']
    if request.method == 'POST':
        data = {
            'nombre_completo': request.form['nombre_completo'],
            'costo_departamento': request.form['costo_departamento'],
            'numero_cuartos': request.form['numero_cuartos'],
            'edificio': request.form['edificio'],  # Debe ser URL completa
        }
        r = requests.post(f"{API_URL}departamentos/", headers=HEADERS, data=data)
        print("POST /departamentos:", r.status_code, r.text)
        return redirect('/departamentos')
    return render_template('crear_departamento.html', edificios=edificios)

if __name__ == '__main__':
    app.run(debug=True)
