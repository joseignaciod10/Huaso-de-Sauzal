from flask import Flask, render_template, url_for, make_response
import datetime

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



@app.route('/routes')
def list_routes():
    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        try:
            # Excluir rutas que necesitan parámetros dinámicos
            if len(rule.arguments) == 0:
                url = url_for(rule.endpoint, **(rule.defaults or {}), _external=True)
                output.append(f"{url} ({methods}) -> {rule.endpoint}")
        except Exception as e:
            print(f"Error generating URL for {rule.endpoint}: {e}")
    return "<br>".join(output)

# Ruta para generar el sitemap.xml
@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    """Genera el sitemap en formato XML."""
    pages = []
    ten_days_ago = (datetime.datetime.now() - datetime.timedelta(days=10)).date().isoformat()

    # Itera sobre todas las rutas de la aplicación
    for rule in app.url_map.iter_rules():
        # Ignora las rutas con parámetros dinámicos
        if "GET" in rule.methods and len(rule.arguments) == 0:
            url = url_for(rule.endpoint, _external=True)
            pages.append([url, ten_days_ago])

    # Renderiza el archivo sitemap_template.xml
    sitemap_xml = render_template('sitemap_template.xml', pages=pages)
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"

    return response



if __name__ == '__main__':
    app.run(debug=True)
