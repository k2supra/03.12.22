try:
    with open("task.txt", "w") as file:
        file.write("hellomy- world for everyyday on the beach and Mercury`s space potato")

    with open("task.txt", "r") as file:
        for line in file:
            print(line, end="")
except Exception as ex:
    print(f"Error: {ex}")