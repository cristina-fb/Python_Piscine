import sys, random

def generator(text, sep=" ", option=None):
    """"Divide el texto de acuerdo al valor de sep y producirá las sub-strings. option especifica si una acción se realizará sobre las sub-strings antes de ser producidas."""
    if (type(text) != str) or (type(sep) != str):
        print("ERROR!")
        return
    aux = text.split(sep)
    if (type(option) != str) and (option != None):
        print("ERROR!")
        return
    if option == "ordered":
        aux.sort()
        for i in aux:
            print(i)
    elif option == "unique":
        aux = list(set(aux))
        for i in aux:
            print(i)
    elif option == "shuffle":
        lst = []
        for i in range(len(aux)):
            r = random.randint(0, len(aux) - 1)
            while r in lst:
                r = random.randint(0, len(aux) - 1)
            lst.append(r)
            print(aux[r])
    elif option == None:
        for i in aux:
            print(i)
    else:
        print("ERROR")
        return

text = "Le Lorem Ipsum est simplement du faux texte."
generator(text, sep=" ")
print()
generator(text, sep=" ", option="shuffle")
print()
generator(text, sep=" ", option="ordered")
print()
generator(text, sep=" ", option="unique")
print()
generator(1.0, sep=" ", option="unique")
print()
generator(text, sep=2, option="unique")
print()
generator(text, sep=" ", option="uniqueee")
print()
generator(1.0, sep=" ", option=34.7)