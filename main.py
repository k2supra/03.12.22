try:
    with open("task.txt", "w") as file:
        file.write("hellomy- world for everyyday on the beach and Mercury`s space potato")

    with open("task.txt", "r") as file:
        for line in file:
            print("Full text: ", line, end=" ")
    print()
    lst = []
    k = line.split(' ')
    for item in k:
        l = len(item)
        #print(l, end=" ")
        if l > 7:
            lst.append(item)
            with open("7+letters.txt", "w") as fle:
                print(f"Words which have 7+ letters: {lst}", file=fle)
                print(f"\033[1;32;40m Words which have 7+ letters:\033[0m {item}")


except Exception as ex:
    print(f"Error: {ex}")