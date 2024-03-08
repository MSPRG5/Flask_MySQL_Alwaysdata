from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'mysql-etudiant2.alwaysdata.net'
app.config['MYSQL_USER'] = 'etudiant2'
app.config['MYSQL_PASSWORD'] = 'EPSI2024'
app.config['MYSQL_DB'] = 'etudiant2_clients'

mysql = MySQL(app)

@app.route('/')
def accueil():  
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT id, nom, prenom FROM clients')
    data = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    return render_template('lectureBDD.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
