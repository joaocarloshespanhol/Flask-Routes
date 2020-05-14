from flask import Flask, render_template
app = Flask(__name__)

produto = [
    ['Refrigerante', 4.50],
    ['Pizza', 2.50],
    ['Suco', 24.90],
    ['Salgado', 5.50],
    ['Lanche', 18.50]
    ] 

@app.route('/')
def index():  
    return render_template('index.html', titulo = 'Produtos',
    produto = produto)

@app.route('/prod/<int:id>')
def produtos(id):
    prod = produto[id]
    return render_template(
        'produtos.html',
        produto = prod)

if __name__ == '__main__':
    app.run()
