N = int(input("Enter N: "))
entries = []
for i in range(N):
    entry = int(input(f"Enter entry {i+1}: "))
    entries.append(entry)

target = int(input("Enter X: "))

if target in entries:
    print(entries.index(target) + 1)  # Return 1-based index
else:
    print(-1)
