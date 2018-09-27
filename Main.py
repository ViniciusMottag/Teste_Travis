def contalista(lista,x):
    resultado=lista.count(x)
    return resultado
 
def existelista(lista,x):
    for elemento in lista:
         if elemento==x:
               return True
    return False
 
def indicelista(lista,x):
    try:
        resultado = lista.index(x)
    except ValueError:
        resultado = -1
    return resultado
 
def invertelista(lista):
    lista.reverse()
    return lista
 
def inserelista(lista,x,i):
    resultado=lista.insert(x,i)
    return resultado
 
def removelista(lista,x):
    del lista[x]
    return lista

def menu():
    print("------------Menu de opções-----------")
    print("1-Verifica quantas vezes existe um produto digitado")
    print("2-Verifica se existe o valor na lista")
    print("3-Informa o primeiro valor digitado")
    print("4-Inverte a ordem da lista")
    print("5-Insere um novo produto a lista")
    print("6-Remove um produto da lista (O produto deve ser digitado extamente igual na lista)\n")
def main():
    termina=True
    validomenu=True
    sairproduto=True
    continua=True
    lista=[]
    while termina:
        nome=str(input("Digite o nome de um produto ou enter para sair: "))
        if nome=='':
            termina=False
        else:
            lista.append(nome)
        contador_prod_lista = len(lista)
    while continua:
        print("Lista de compras atual:",lista,"\n")
        menu()
        num1=int(input("Digite a opção ou -1 para finalizar: "))
        if num1==-1:
            continua=False
        if num1 not in[1,2,3,4,5,6] and continua==True:
            print (menu())
            num1=(input("Valor invalido,Digite um numero conforme mostrado no Menu de opções: "))
        if num1 ==1:
            produto=str(input("Digite o nome do produto: "))
            lista1 = contalista(lista,produto)
            if lista1>1:
                print("O produto ",produto,"aparece",lista1," vezes na lista\n")
            else:
                print("O produto ",produto,"aparece",lista1," vez na lista\n")
        if num1==2:
            produto=str(input("Digite o nome do produto: "))
            lista2 = contalista(lista,produto)
            if lista2==False:
                print("Não existe este produto -",produto,"na lista\n")
            else:
                print("O produto -",produto,"esta na lista\n")
        if num1==3:
            produto=str(input("Digite o produto: "))
            primeirolista=indicelista(lista,produto)
            print(primeirolista)
        if num1==4:
            lista3= invertelista(lista)
            print(lista3)
        if num1==5:
            produto=str(input("Digite o produto a ser inserido: "))
            print(lista)
            posicao=int(input("Digite a posição a ser inserida: "))
            inserelista(lista,posicao,produto)
            print(lista)
        if num1==6:
            print(lista)
            posicao=int(input("Digite a posição em que o produto deve ser removido: "))
            removelista(lista,posicao)     
main() 
