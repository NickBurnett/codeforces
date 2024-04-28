lines = int(input())
x = 0
for _ in range(lines):
    l = input()
    if "+" in l: x += 1
    else: x -= 1
print(x)