# Manual Implementation
def sort_dicts_by_key(data_list, sort_key):
    """
    Sorts a list of dictionaries by the specified key.
    Uses .get() for safer access if the key may not exist.
    """
    return sorted(data_list, key=lambda x: x.get(sort_key, None))


# AI-Suggested Version (e.g., Copilot)
def sort_by_key(dicts, key):
    """
    Sorts a list of dictionaries by the specified key.
    Assumes all dictionaries contain the key.
    """
    return sorted(dicts, key=lambda d: d[key])


# Sample data to test both functions
if __name__ == "__main__":
    data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 22},
        {"name": "Charlie", "age": 30}
    ]

    print("Manual version:")
    print(sort_dicts_by_key(data, "age"))

    print("\nAI Copilot version:")
    print(sort_by_key(data, "age"))
