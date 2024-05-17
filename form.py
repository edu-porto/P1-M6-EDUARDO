from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator


def main() -> None:
    float_val1 = inquirer.number(
        message="Enter float:",
        float_allowed=True,
        validate=EmptyInputValidator(),
    ).execute()
    float_val2 = inquirer.number(
        message="Enter float:",
        float_allowed=True,
        validate=EmptyInputValidator(),
    ).execute()

    float_val3 = inquirer.number(
        message="Enter float:",
        float_allowed=True,
        validate=EmptyInputValidator(),
    ).execute()

    float_val4 = inquirer.number(
        message="Enter float:",
        float_allowed=True,
        validate=EmptyInputValidator(),
    ).execute()


    print(f"float_val1: {float_val1},float_val2: {float_val2}, float_val3: {float_val3}, float_val4: {float_val4} ")

if __name__ == "__main__":
    main()