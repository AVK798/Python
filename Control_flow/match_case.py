command = 'quit'

match command:
    case "quit" | "exit":
        print("good bye")
    case "No" | "do":
        print("do not found")
    case "info" | "done":
        print("available are not in done")
    case _:
        print("unknow command")