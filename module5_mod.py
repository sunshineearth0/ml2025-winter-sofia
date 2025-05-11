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