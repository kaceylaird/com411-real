import csv

def search(file_path):
    print("Searching...")

    sections = ""
    books = "Books:\n"

    with open(file_path) as file:
        for line in file:
            if line.startswith("Section"):
                sections += line
            else:
                books += line

    print("Done!")

    return f"{sections}\n\n{books}"


def save(file_path, data):
    print("Saving...")
    with open(file_path, "w") as file:
        file.write(data)
    print("Done!")


def run():
    data = search("books.txt")
    save("exported_books.txt", data)


if __name__ == "__main__":
    run()


def read(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file)

        headings = next(csv_reader)
        print(f"Headings:\n{headings}")

        print("Values:")
        for values in csv_reader:
            print(values)


def run_task1():
    read("clothing.csv")


if __name__ == "__main__":
    run_task1()