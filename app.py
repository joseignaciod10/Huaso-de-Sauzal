from flask import Flask, render_template

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para la página de la historia del vino
@app.route('/history')
def history():
    return render_template('history.html')

# Ruta para la página Quiénes somos
@app.route('/quienes-somos')
def quienes_somos():
    return render_template('quienes_somos.html')
@app.route('/galeria')
def galeria():
    return render_template('galeria.html') 

# Ruta para la página Nuestros vinos
@app.route('/nuestros-vinos')
def nuestros_vinos():
    return render_template('nuestros_vinos.html')

# Ruta para la página Contacto
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

# Ruta para la historia de Cariñena
@app.route('/historia_carinena')
def historia_carinena():
    return render_template('historia_carinena.html')

# Ruta para la historia de Chilena
@app.route('/historia_chilena')
def historia_chilena():
    return render_template('historia_chilena.html')

# Ruta para la historia de Garnacha
@app.route('/historia_garnacha')
def historia_garnacha():
    return render_template('historia_garnacha.html')

if __name__ == '__main__':
    app.run(debug=True)
