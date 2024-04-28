cases = int(input())
for _ in range(cases):
    word = input()
    if len(word) <= 10:
        print(word)
        continue
    print(word[0] + str(len(word[1:-1])) + word[-1])