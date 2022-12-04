
try:
    with open("1file.txt", "w") as file:
        print("Hellomy", file= file)
        print("own world", file= file)
        print("howru", file= file)
        print("Oh sheet", file= file)

    with open("1file.txt", "r") as file1:
        reader = file1.readline()
        kou = reader.count(' ')
        reader1 = file1.readline()
        kou1 = reader1.count(' ')
        reader2 = file1.readline()
        kou2 = reader2.count(' ')
        reader3 = file1.readline()
        kou3 = reader3.count(' ')

        if kou == 0:
            with open("1file.txt", "w") as file:
                print(reader, file=file)
                print("------------", file=file)
                print(reader1, file=file)
                print(reader2, file=file)
                print(reader3, file=file)

        if kou1 == 0:
            with open("1file.txt", "w") as file:
                print(reader, file=file)
                print(reader1, file=file)
                print("------------", file=file)
                print(reader2, file=file)
                print(reader3, file=file)

        if kou2 == 0:
            with open("1file.txt", "w") as file:
                print(reader, file=file)
                print(reader1, file=file)
                print(reader2, file=file)
                print("------------", file=file)
                print(reader3, file=file)

        if kou3 == 0:
            with open("1file.txt", "w") as file:
                print(reader, file=file)
                print(reader1, file=file)
                print(reader2, file=file)
                print(reader3, file=file)
                print("------------", file=file)
        print(reader)
        print(f"**{kou}")
except Exception as ex:
    print(f"Error:{ex}")