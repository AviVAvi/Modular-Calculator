def save(result):
    with open("texts.txt", "w") as file:
        file.write(str(result))