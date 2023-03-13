kata = (19,42,21)
length = len(kata)
aux = str(kata[0])
for i in kata[1:]:
    aux = aux + " " + str(i)
print("The " + str(length) + " numbers are: " + aux)
