class NumberProcessor:
    def __init__(self):
        self.entries = []
    
    def add_entry(self, entry):
        self.entries.append(entry)
    
    def search(self, target):
        if target in self.entries:
            return self.entries.index(target) + 1  # 1-based index
        else:
            return -1

if __name__ == "__main__":
    N = int(input("Enter N: "))
    processor = NumberProcessor()
    for i in range(N):
        entry = int(input(f"Enter entry {i+1}: "))
        processor.add_entry(entry)
    target = int(input("Enter X: "))
    print(processor.search(target))