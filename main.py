from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    nombre = None
    edad = None
    cantidad_tarros = None
    total_sin_descuento = None
    total_con_descuento = None
    descuento = None

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])

        total_sin_descuento = cantidad_tarros * 9000

        if edad >= 18 and edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento * (1 - descuento)
        descuento = total_sin_descuento - total_con_descuento

    return render_template('ejercicio1.html', nombre=nombre, edad=edad, cantidad_tarros=cantidad_tarros,
                           total_sin_descuento=total_sin_descuento, total_con_descuento=total_con_descuento, descuento=descuento)

users = {
    "juan": {"password": "admin", "message": "Bienvenido Administrador juan"},
    "pepe": {"password": "user", "message": "Bienvenido Usuario pepe"}
    }

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    error_message = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username]['password'] == password:
            message = users[username]['message']
            return render_template('ejercicio2.html', message=message)
        else:
            error_message = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)