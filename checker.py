import os


def inspect_env(file_path):
    if not os.path.exists(file_path):
        print("❌ File not found.")
        return []

    results = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#") or "=" not in line:
                continue

            name, value = line.split("=", 1)

            name = name.strip()
            value = value.strip()

            results.append((name, bool(value)))

    return results
