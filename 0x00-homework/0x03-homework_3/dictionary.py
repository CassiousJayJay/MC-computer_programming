
def main():
    my_class()
    fruits()
    details()
    results()


def my_class():
    student = {"name": "John",  "age": 20, "grade": "A"}
    print(student.get("age"))

    student.update({"city": "New York"})

    if "grade" in student:
            print("Exist")
    else:
        print("Does not exist")

    del student["age"]
    print(student.keys())


def fruits():
    inventory = {"apples": 10, "bananas": 15, "oranges": 5}
    print(inventory.get("bananas"))

    inventory.update({"oranges":8})

    if "grapes" in inventory:
        print("Grapes exist")
    else:
        print("Grapes does not exist")
    del inventory["apples"]

    print(inventory.values())


def details():  
    contacts = {"John": "john@example.com", "Jane": "jane@example.com",  "Bob": "bob@example.com"}
    print(contacts.get("Jane"))

    contacts.update({"John":"john.doe@example.com"})

    if "Alice" in contacts:
        print("Alice is present")
    else:
        print("Alice is absent")

    del contacts["Bob"]
    print(contacts.items())


def results():
    scores = {"Alice": 85, "Bob": 92,  "Charlie": 78}
    print(scores.get("Bob"))

    scores.update({"David": 95})

    if "Eve" in scores:
        print("Eve is present")
    else:
        print("Eve is absent")

    del scores[ "Charlie"]

    print(scores.items())

if __name__=="__main__":
    main()





