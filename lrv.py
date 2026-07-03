# Cálculo das linhas de estímulo de redução de velocidade

print("Cálculo das linhas de estímulo de redução de velocidade")

# Entrada de dados
v = float(input("Digite a velocidade inicial [km/h]: ")) / 3.6
print("")
vf = float(input("Digite a velocidade final desejada [km/h]: ")) / 3.6
print("")

# Cálculo do número de linhas
n = (v - vf) / 1.47
tam = round(n)  # arredondamento correto

# Lista de espaços acumulados
lrv = [i * (v - 1.47/2 * i) for i in range(1, tam + 1)]

# Arredondar valores da lista (2 casas decimais)
lrv = [round(valor, 2) for valor in lrv]

# Distâncias entre linhas
res = [round(lrv[a] - lrv[a-1], 2) for a in range(1, len(lrv))]
res.insert(0, lrv[0])

# Velocidade em km/h
l = v * 3.6

# Largura da linha
if l < 60:
    largura = 0.20
elif 60 <= l <= 80:
    largura = 0.30
else:
    largura = 0.40

print(f"A largura da linha deve ser {largura:.2f} m")

# Saída
print("")
print("Espaço Ei até a linha i [m]:", lrv)
print("")
print("Distância até a próxima linha [m]:", res)
print("")
print("Quantidade de linhas:", tam)
print("")
print(f"Espaço total marcado: {lrv[-1]:.2f} m + largura da linha")
