import cs50


def main():
    height = get_height()
    for i in range(height):
        k = (height - i) - 1
        while True:
            if k == 0:
                break
            print(" ", end='')
            k -= 1
            j = i
        while True:
            if j < 0:
                break
            print("#", end='')
            j -= 1
            print("  ", end='')
            z = i
        while True:
            if z < 0:
                break
            print("#", end='')
            z -= 1
            print()


def get_height():
    while True:
        try:
            height = cs50.get_int("Height: ")
            if (height > 0 and height < 9):
                break
            except ValueError:
                None
    return height


main()