#BIBLIOTECAS DE GRAFICOS E MATEMÁTICA, RESPECTIVAMENTE#
import matplotlib.pyplot as plt
import numpy as np
import math as mt

ano = "2025"
trimestre = "3° Trimestre"
exp1 = 20
exp2 = 15
exp3 = 10
exp4 = 25
exp5 = 2
quantidade_de_dados = exp1 + exp2 + exp3 + exp4 + exp5 #ESPECIFICAÇÃO DE VARIÁVEIS E APLICAÇÃO DELAS --> SOMA#
print(f"{ano}, {trimestre} Primeiro teste")
print(f"O total de amostras utilizadas nos experimentos foram: {quantidade_de_dados}")
print("Os gráficos de cada experimento, respectivamente são:")

#ESPECIFICANDO AS VARIÁVEIS QUE VOU USAR#
x1 = [0, 1, 2, 3, 4, 5, 6]
y1 = [i**2 for i in x1]

x2 = [0, 1, 2, 3, 4, 5]
y2 = [i*2 for i in x2]

x3 = [0, 1, 2, 3, 4, 5]
k = 5
y3 = [(k*i**2)/2 for i in x3]

x4 = [0, 1, 2, 3, 4, 5]
y4 = [(mt.exp(i))/2 for i in x4]

x5 = np.linspace(0, 2*np.pi, 100)
y_seno = np.sin(x5)
y_cosseno = np.cos(x5)

plt.plot(x1, y1, label='linha y=x²', color='black', marker='*')
plt.plot(x2, y2, label='linha y=2x', color='green', marker='^')
plt.plot(x3, y3, label='linha y=(k*x^2)/2', color='red', marker='o')
plt.plot(x4, y4, label='linha y=e^x/2', color='orange', marker='s') #s de square#
plt.plot(x5, y_seno, label='Seno')
plt.plot(x5, y_cosseno, label='Cos')

plt.title("exemplo de gráfico")
plt.xlabel("eixo x")
plt.ylabel("eixo y")
plt.legend()
plt.grid(True, color='blue', linestyle='--')

plt.show()
