import json
import sys

MINIMUM_ACCURACY = 1.01


def main():
    try:
        with open("metrics.json", "r") as file:
            metrics = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f"ERROR: Could not read metrics.json: {error}")
        sys.exit(1)

    accuracy = metrics.get("accuracy")

    if not isinstance(accuracy, (int, float)):
        print("ERROR: Accuracy is missing or invalid.")
        sys.exit(1)

    print(f"Model accuracy: {accuracy:.4f}")
    print(f"Minimum required accuracy: {MINIMUM_ACCURACY:.2f}")

    if accuracy < MINIMUM_ACCURACY:
        print("QUALITY GATE FAILED")
        sys.exit(1)

    print("QUALITY GATE PASSED")


if __name__ == "__main__":
    main()

