from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Bienvenue sur l’espace organisateur de votre séminaire</h1>"

@app.route('/ajouter-referent', methods=['GET', 'POST'])
def ajouter_referent():
    if request.method == 'POST':
        nom = request.form['nom']
        email = request.form['email']
        role = request.form['role']
        # Simuler un enregistrement
        return f"Référent ajouté : {nom} ({role}) - {email}"
    return '''
        <form method="post">
            Nom: <input type="text" name="nom"><br>
            Email: <input type="email" name="email"><br>
            Rôle: <input type="text" name="role"><br>
            <input type="submit" value="Ajouter">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
