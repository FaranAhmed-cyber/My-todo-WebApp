FILENAME = "data.txt"


def read_file(filename=FILENAME):
    with open(filename, "r") as file:
        data_read = file.readlines()
    return data_read


def write_file(data_write, filename=FILENAME):
    with open(FILENAME, "w") as file:
        file.writelines(data_write)


# code below it will only execute for this file not for main fie
if __name__ == "__main__":
    print("code below this 'if' statement will execute in this file only.")