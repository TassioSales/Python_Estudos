with open("adcde.txt", 'a+') as file:
    file.write("Outra Linha\n")
    file.seek(0)
    print(file.read())