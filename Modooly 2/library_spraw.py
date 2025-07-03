def pokazatu_wmist():
    with open("sprawu", "r", encoding="UTF-8") as fp:
        info = fp.readlines()
        x = 1
        for i in info:
            print(f"{x}) {i}")
            x += 1

        return info