
# Returns a greeting message to caller function
# Caller function decides what to do with the response.
def greeter(name: str) -> str:
    """Return a greeting message"""
    # greeter `transforms` original string to something useful
    # and returns it.
    return f"Name {name}!"


def main() -> None:
    friends: list[str] = ["Subham", "Ram", "Shyam", "Monu", "Sonu"]
    # Greet Everyone
    for friend in friends:
        # main acts as the `caller function` for greeter.
        # It can handle response in multiple ways.
        if "Subham" in greeter(friend):
            print(f"{friend} is cute!")
        else:
            print(greeter(friend))


main()
