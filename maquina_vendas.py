import time

matriz = [
    [1, "coca-cola", 3.75, 2],
    [2, "pepsi", 3.67, 5],
    [3, "monster", 9.96, 1],
    [4, "café", 1.25, 100],
    [5, "redbull", 13.99, 2]
]

dinheiro = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]

def CalcularTroco(valorProduto, valorPago):
    troco = valorPago - valorProduto
    time.sleep(3)
    print("seu troco será de:", troco, "!")
    for valor in dinheiro:
        qtd = troco // valor
        if qtd >= 1:
            if valor > 1:
                print(qtd, " nota(s) de ", [valor])
                print('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*')
            elif valor == 1:
                print(qtd, " moeda(s) de ", [valor], "Real")
                print('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*')
            elif valor < 1:
                print(qtd, " moeda(s) de ", [valor], "centavos")
                print('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*')
            troco = troco - (valor * qtd)

def SelecionarProduto():
    compra = int(input("qual produto você quer? "))
    while compra <= 0 or compra > 5:
        print("insira um valor valído")
        compra = int(input("qual produto você quer? "))
    return compra

while True:
    print('''
    -------------------------------------------
    Produtos | Preço | Estoque
    -------------------------------------------
    | 1 | Coca-Cola | 3,75 |''', (matriz[0][3]), '''
    --------------------------------------------
    | 2 | Pepsi | 3,67 |''', (matriz[1][3]), '''
    -------------------------------------------
    | 3 | Monster | 9,96 |''', (matriz[2][3]), '''
    -------------------------------------------
    | 4 | Café | 1,25 |''', (matriz[3][3]), '''
    -------------------------------------------
    | 5 | RedBull | 13,99 |''', (matriz[4][3]), '''
    -------------------------------------------''')
    
    compra = SelecionarProduto()
    print("você escolheu, " + str(matriz[compra - 1][1]) + " !")
    
    if (matriz[compra - 1][3]) > 0:
        print("temos o total de " + str(matriz[compra - 1][3]) + " no estoque!")
        (matriz[compra - 1][3]) = (matriz[compra - 1][3]) - 1
        print("o valor que será pago é de R$" + str(matriz[compra - 1][2]) + ":)")
        time.sleep(3)
        valorDoProduto = matriz[compra - 1][2]
        valorPago = float(input("qual o valor será insirido? "))
        
        while valorPago < valorDoProduto:
            print("insira um valor maior ou igual ao preço do produto")
            valorPago = float(input("qual o valor será insirido? "))
        
        CalcularTroco(valorDoProduto, valorPago)
        time.sleep(3)
    else:
        print("sinto muito, estamos sem estoque desse produto :(")
