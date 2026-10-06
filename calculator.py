def add(x: float, y: float) -> float:
    return x + y


def subtract(x: float, y: float) -> float:
    return x - y


def multiply(x: float, y: float) -> float:
    return x * y


def divide(x: float, y: float) -> float:
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


def parse_number(value: str) -> float:
    return float(value)


def calculate(operation: str, x: float, y: float) -> float:
    if operation == "A":
        return add(x, y)
    if operation == "S":
        return subtract(x, y)
    if operation == "M":
        return multiply(x, y)
    if operation == "D":
        return divide(x, y)

    raise ValueError("Invalid operation.")


def test_calculator() -> None:
    assert add(2, 3) == 5
    assert add(2.5, 1.5) == 4.0
    assert add(-2, 3) == 1

    assert subtract(10, 4) == 6
    assert subtract(2.5, 1.0) == 1.5

    assert multiply(3, 4) == 12
    assert multiply(2.5, 2) == 5.0

    assert divide(10, 2) == 5.0
    assert divide(7.5, 2.5) == 3.0

    assert parse_number("2.5") == 2.5

    assert calculate("A", 2, 3) == 5
    assert calculate("S", 5, 2) == 3
    assert calculate("M", 4, 3) == 12
    assert calculate("D", 10, 2) == 5.0

    try:
        parse_number("hello")
    except ValueError:
        pass
    else:
        assert False

    try:
        divide(10, 0)
    except ValueError:
        pass
    else:
        assert False

    try:
        calculate("X", 2, 3)
    except ValueError:
        pass
    else:
        assert False

    print("All tests passed!")


def main() -> None:
    print("Simple Calculator")
    print("A - Add")
    print("S - Subtract")
    print("M - Multiply")
    print("D - Divide")

    operation: str = input("Choose an operation (A/S/M/D): ").upper()

    try:
        x: float = parse_number(input("Enter x: "))
        y: float = parse_number(input("Enter y: "))
        result: float = calculate(operation, x, y)

        print("Result:", result)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    test_calculator()
    main()