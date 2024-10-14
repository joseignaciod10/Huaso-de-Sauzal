from flask import Flask, render_template
from flask_sitemap import Sitemap

app = Flask(__name__)
ext = Sitemap(app=app)

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

@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    """Genera el sitemap en formato XML."""
    pages = []
    ten_days_ago = (datetime.datetime.now() - datetime.timedelta(days=10)).date().isoformat()

    # Itera sobre todas las rutas de la aplicación
    for rule in app.url_map.iter_rules():
        # Ignora las rutas que tienen parámetros dinámicos
        if "GET" in rule.methods and len(rule.defaults) >= len(rule.arguments):
            url = url_for(rule.endpoint, **(rule.defaults or {}), _external=True)
            pages.append([url, ten_days_ago])

    sitemap_xml = render_template('sitemap_template.xml', pages=pages)
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"

    return response

if __name__ == '__main__':
    app.run(debug=True)
