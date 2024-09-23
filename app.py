from flask import Flask, render_template
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Función para conectar a la base de datos y obtener los datos
def get_data():
    db_connection = mysql.connector.connect(
        host="localhost", # Cambia si estás usando un servidor MySQL remoto
        user="root", # Cambiar por el usuario de la base de datos
        password="admin", # Cambiar por la contraseña de la base de datos
        database="prueba_dashboard" # Cambiar por el nombre de la base de datos
    )
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM empleados")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=['id', 'nombre', 'edad', 'ciudad', 'salario'])
    cursor.close()
    db_connection.close()
    return df

# Función para generar el gráfico de barras
def plot_bar(df):
    fig, ax = plt.subplots()
    ax.bar(df['edad'], df['salario'])
    ax.set_title('Relación entre Edad y Salario')
    ax.set_xlabel('Edad')
    ax.set_ylabel('Salario')

    # Convertir la imagen a base64 para insertar en HTML
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

# Función para generar el gráfico circular
def plot_pie(df):
    fig, ax = plt.subplots()
    ciudad_count = df['ciudad'].value_counts()
    ax.pie(ciudad_count, labels=ciudad_count.index, autopct='%1.1f%%')
    ax.set_title('Cantidad de personas por ciudad')

    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

@app.route('/')
def index():
    df = get_data()  # Obtener los datos de la base de datos
    table_html = df.to_html(classes='table table-bordered table-hover table-striped text-center', index=False)  # Alinear texto y agregar estilos de Bootstrap
    bar_chart = plot_bar(df)  # Gráfico de barras
    pie_chart = plot_pie(df)  # Gráfico circular
    return render_template('index.html', tables=table_html, bar_chart=bar_chart, pie_chart=pie_chart)



if __name__ == '__main__':
    app.run(debug=True)
