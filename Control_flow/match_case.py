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

        # Match with data structures
point = (1, 0)
match point:
 case (0, 0): print("Origin")
 case (x, 0): print(f"On X-axis at {x}")
 case (0, y): print(f"On Y-axis at {y}")
 case (x, y): print(f"Point at ({x}, {y})")