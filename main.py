from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', resultado="")

@app.route('/resultado', methods=['POST'])
def resultado():
    fatorial = int(input("Digite um número: "))
    fator = 1
    fatorando = 1

    while fator <= fatorial:
        fatorando = fator * fatorando

        fator = fator + 1
    return render_template('index.html', resultado = f'O numero {numero} é {resultado}')

if __name__ == '__main__':
    app.run(debug=True)