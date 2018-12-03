from flask import Flask, render_template
import requests
import json

app = Flask(__name__)



@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/pokemon/<query>', methods=['GET'])
def display(query):
    r = requests.get('https://pokeapi.co/api/v2/pokemon/' + query)
    data = r.json()
    for key, value in data.items():
        if key == 'name':
            name = value
        if key == 'id':
            identify = value
    if query.isdigit():
        return render_template('name.html', name=name, identify=identify)
    return render_template('id.html', name=name.capitalize(), identify=identify)

 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
