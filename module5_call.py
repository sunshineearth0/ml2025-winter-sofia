from module5_mod import NumberProcessor

N = int(input("Enter N: "))
processor = NumberProcessor()
for i in range(N):
    entry = int(input(f"Enter entry {i+1}: "))
    processor.add_entry(entry)
target = int(input("Enter X: "))
print(processor.search(target))