def find_zohan(name: str) -> None:
    friends = ["Subam", "Kumar", "Singh", "Mohsn", "sita", "Ram"]

    try:
        assert name in friends
    except AssertionError:
        print(f"{name} not found!")
    else:
        print(f"Found {name}")
    finally:
        print("Goodbye")


find_zohan("subam")
find_zohan("Kumar")

