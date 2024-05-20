x = int(input())
y = list(map(int, input().split()))
print(f"Menor valor: {min(y)}\nPosicao: {y.index(min(y))}")