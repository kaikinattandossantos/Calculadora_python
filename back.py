from flask import Flask, request, render_template #baixar os pacotes
#render template faz a conexão com outros documentos
app = Flask(__name__)

# Função para realizar operações matemáticas
def calcular_operacao(num1, num2, operacao):
    try:
        if operacao == "+":
            return num1 + num2
        elif operacao == "-":
            return num1 - num2
        elif operacao == "*":
            return num1 * num2
        elif operacao == "/":
            return "Erro: divisão por zero" if num2 == 0 else num1 / num2
        else:
            return "Operação inválida"
    except Exception:
        return "Erro: Entrada inválida"

@app.route('/') #página inicial
def index(): #função atribuida ao caminho
    return render_template('index.html', result="---")

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operacao = request.form['operacao']
        result = calcular_operacao(num1, num2, operacao)
    except Exception:
        result = "Erro: Entrada inválida"
    return render_template('index.html', result=result)

if __name__ == "__main__": #Executa o código abaixo quando rodar o arquivo, a menos que seja importado para outro arquivo (deploy)
    app.run(debug=True) #para atualizar o código em tempo real
