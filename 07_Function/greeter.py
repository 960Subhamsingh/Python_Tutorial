
def greeter(name: str) -> None:
    """Greets Zortan"""
    print(f"Subham {name}!")


def main() -> None:
    friends: list[str] = ["Subham", "Mohan", "Richa", "Gita", "Shyam"]
    # Greet Everyone
    for friend in friends:
        greeter(friend)


# Invoke the `main` function
main()
