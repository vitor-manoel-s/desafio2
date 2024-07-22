# Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
# depois disso retorne o resultado para uma variável.
def calcularNivel(vitorias, derrotas):

    # o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)  
    saldoVitorias = vitorias - derrotas

    if saldoVitorias < 10:      # Se vitórias for menor do que 10 = Ferro
        ranking = "Ferro"
    elif saldoVitorias <= 20:   # Se vitórias for entre 11 e 20 = Bronze
        ranking = "Bronze"
    elif saldoVitorias <= 50:   # Se vitórias for entre 21 e 50 = Prata
        ranking = "Prata"
    elif saldoVitorias <= 80:   # Se vitórias for entre 51 e 80 = Ouro
        ranking = "Ouro"
    elif saldoVitorias <= 90:   # Se vitórias for entre 81 e 90 = Diamante
        ranking = "Diamante"
    elif saldoVitorias <= 100:  # Se vitórias for entre 91 e 100= Lendário
        ranking = "Lendário"
    else:                       # Se vitórias for maior ou igual a 101 = Imortal
        ranking = "Imortal"
    
    return(saldoVitorias, ranking)


vitorias = int(input("Digite o número de vitórias: "))
derrotas = int(input("Digite o número de derrotas: "))

# Chamada da função
saldoVitorias, nivel = calcularNivel(vitorias, derrotas)

# Ao final deve se exibir a mensagem:"O Herói tem de saldo de {saldoVitorias} está no nível de {nivel}"
print("O Herói tem de saldo de {} está no nível de {}".format(saldoVitorias,nivel))
