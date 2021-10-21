with open("adcde.txt", "w+") as file:
    for c in range(1,4):
        file.write(f"Linha {c}\n")
    file.seek(0)
    print(file.read())