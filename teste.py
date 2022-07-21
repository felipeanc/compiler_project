def lex(w):
    for i in range(8):
        char = w.read(1)
        print(char, end="")
    print()
f = open("source.txt", "r")
lex(f)
lex(f)
lex(f)