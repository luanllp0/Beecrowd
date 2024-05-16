# cont = int(input())
# for i in range (0, cont):
#     a =int(input())
#     lis = [0, 1]
#     for j in range (0, a):
#         x = lis[-1] + lis[-2]
#         lis.append(x)
#     print(f"Fib({a}) = {lis[-2]}")

# x = int(input())
# y = list(map(int, input().split()))
# print(f"Menor valor: {min(y)}\nPosicao: {y.index(min(y))}")

# x = int(input())
# soma = x
# cont = 1
# while True:
#     z = int(input())
#     if z > x:
#         break
# while soma < z:
#     x = x+1
#     soma = soma +x
#     cont += 1
# print(cont)

# n = int(input())
# ho = str("Ho")
# for i in range (1, n):
#     ho += " Ho"
# ho += "!"
# print(ho)

# bin = 0
# x = 0
# while True:
#     piscada = str(input())
#     if piscada == "--*":
#         bin += 1
#     elif piscada == "-*-":
#         bin += 2
#     elif piscada == "-**":
#         bin += 3
#     elif piscada == "*--":
#         bin += 4
#     elif piscada == "*-*":
#         bin += 5
#     elif piscada == "**-":
#         bin += 6
#     elif piscada == "***":
#         bin += 7
#     elif piscada == "caw caw":
#         print(bin)
#         x += 1
#         bin = 0
#     if x == 3:
#         break

# a = int(input())
# for i in range (0, a):
#     x = int(input())
#     if x % 2 == 0:
#         print("0")
#     else:
#         print("1")
    

# cont=int(input())
# for i in range (0, cont):
#     nome1, num1, nome2, num2 = map(str, input().split())
#     n, m = map(int, input().split())
#     soma = n + m
#     if soma % 2 == 0:
#         if num1 == "PAR":
#             print(nome1)
#         else:
#             print(nome2)
#     elif soma % 2 != 0:
#         if num1 == "IMPAR":
#             print(nome1)
#         else:
#             print(nome2)

# a, b, c, d = map(int,input().split())
# x = a+b+c+d -3
# print(x)

# a, b = map(int, input().split())
# if a > b:
#     print(a)
# elif b >= a:
#     print (b)