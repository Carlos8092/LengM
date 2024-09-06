from flask import Flask, render_template, request, redirect, url_for, flash
import pyodbc

app = Flask(__name__)

# SQLSERVER CONNECTION
app.config['SQL_SERVER_DRIVER'] = ''
app.config['SQL_SERVER_SERVER'] = ''
app.config['SQL_SERVER_DATABASE'] = ''
app.config['SQL_SERVER_USERNAME'] = ''

connection_string = (
    f"DRIVER={app.config['SQL_SERVER_DRIVER']};"
    f"SERVER={app.config['SQL_SERVER_SERVER']};"
    f"DATABASE={app.config['SQL_SERVER_DATABASE']};"
    "Trusted_Connection=yes;"
)

mysql = pyodbc.connect(connection_string)

# Settings
app.secret_key = 'mysecret'

@app.route('/')
def index():
    cursor = mysql.cursor()
    cursor.execute('SELECT * FROM peliculas')
    data = cursor.fetchall()
    return render_template('INDEX.html', peliculas=data)

@app.route('/add_pelicula', methods=['POST'])
def add_pelicula():
    if request.method == 'POST':
        NOMBRE = request.form['NOMBRE']
        FECHA_SALIDA = request.form['FECHA_SALIDA']
        GENERO = request.form['GENERO']
        cursor = mysql.cursor()
        cursor.execute('INSERT INTO peliculas (NOMBRE, FECHA_SALIDA, GENERO) VALUES (?, ?, ?)', (NOMBRE, FECHA_SALIDA, GENERO))
        mysql.commit()
        flash('Película agregada con éxito')
        return redirect(url_for('index'))

@app.route('/getPelicula/<id>')
def edit_pelicula(id):
    cursor = mysql.cursor()
    cursor.execute('SELECT * FROM peliculas WHERE id = ?', id)
    data = cursor.fetchall()
    return render_template('modifica.html', pelicula=data[0])

@app.route('/update/<id>', methods=['POST'])
def update_pelicula(id):
    if request.method == 'POST':
        NOMBRE = request.form['NOMBRE']
        FECHA_SALIDA = request.form['FECHA_SALIDA']
        GENERO = request.form['GENERO']

        cursor = mysql.cursor()
        cursor.execute("""
            UPDATE peliculas
            SET NOMBRE = ?,
            FECHA_SALIDA = ?,
            GENERO = ?
            WHERE ID = ?
        """, (NOMBRE, FECHA_SALIDA, GENERO, id))
        mysql.commit()
        flash('Película actualizada con éxito')
        return redirect(url_for('INDEX'))

@app.route('/delete/<string:id>')
def delete_pelicula(id):
    cursor = mysql.cursor()
    cursor.execute('DELETE FROM peliculas WHERE ID = ?', id)
    mysql.commit()
    flash('Película eliminada con éxito')
    return redirect(url_for('INDEX'))

if __name__ == '__main__':
    app.run(port=3000, debug=True)
