from checker import inspect_env

file_path = input("Enter .env file path: ")

results = inspect_env(file_path)

print("\n🔍 EnvPeek Report")
print("=" * 40)

if not results:
    print("No variables found.")
else:
    for name, status in results:
        icon = "✅" if status else "⚠️"
        print(f"{icon} {name}")
