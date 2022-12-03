try:
    with open("1stfile.txt", "w") as file1:
        print("Hello", file= file1)
        print("my", file= file1)
        print("own", file= file1)
        print("world!", file= file1)

    with open("1stfile.txt", "r") as file3:
        con = file3.readlines()


    with open("2ndfile.txt", "w") as file2:
        for item in con:
            print(item.replace("\n", ""), file=file2)

    print("****DONE****")
except Exception as ex:
    print(f"Error: {ex}")