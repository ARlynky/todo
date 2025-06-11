import argparse
import json


def add(item, data, data_path):
    data.append(item)
    with open(data_path, "w") as f:
        json.dump(data, f, indent=4)

    print("Added", item, "to TODO list")


def list(data):
    if data == []:
        print("list already empty")
    else:
        for index, value in enumerate(data):
            print(index, " ", value)


def empty(data_path):
    with open(data_path, "w") as f:
        f.write("[]")
    print("TODO list has been cleared")


def remove(data, data_path, arg):
    if data == []:
        print("No items in TODO list")

    elif arg not in data:
        print("Item not in TODO list")

    else:
        data.remove(arg)

        with open(data_path, "w") as f:
            json.dump(data, f, indent=4)
        print("Removed", arg, "from TODO list")


def main():
    parser = argparse.ArgumentParser(description="TODO list")
    parser.add_argument("--add", help="the item to add to the list")
    parser.add_argument("--list", help="list the TODO list", action="store_true")
    parser.add_argument("--empty", help="empty TODO list", action="store_true")
    parser.add_argument("--remove", help="remove a value in TODO list via name")

    args = parser.parse_args()

    data_path = "data.json"

    with open(data_path, "r") as f:
        todos = json.load(f)

    if args.add:
        add(args.add, todos, data_path)

    if args.list:
        list(todos)

    if args.empty:
        empty(data_path)

    if args.remove:
        remove(todos, data_path, str(args.remove))


if __name__ == "__main__":
    main()
