import os


def cwd():
    path = os.getcwd()
    print(f"The current working directory is {path}")
    print(f"The directory contains the following:")
    for file in os.listdir(path):
        print(file)


def run():
    print("Processing...")
    cwd()


if __name__ == "__main__":
    run()


def display_chars(file_path, num_chars):
    with open(file_path) as file:
        data = file.read(num_chars)
        print(data)


def display_line(file_path):
    with open(file_path) as file:
        data = file.readline().strip()
        print(data)


def display_text(file_path):
    with open(file_path) as file:
        data = file.read()
        print(data)


def run_task2():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")


if __name__ == "__main__":
    run_task2()