import sys

def generator(text, sep=" ", option=None):
    """"Divide el texto de acuerdo al valor de sep y producirá las sub-strings. option especifica si una acción se realizará sobre las sub-strings antes de ser producidas."""
    if type(text) != str:
        sys.exit("ERROR!")
    aux = text.split(sep)
    if type(text) != str:
        sys.exit("ERROR!")
    if option == "ordered":
        aux = aux.sort()
        # print(aux)
        # for i in aux:
        #     print(i)
    if option == "unique":
        aux = list(set(aux))
        for i in aux:
            print(i)
    # if option == "shuffle":
    else:
        sys.exit("ERROR!")


generator("Hola/caracola/Hola", '/', 'unique')