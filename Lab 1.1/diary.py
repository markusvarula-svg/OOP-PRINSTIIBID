class Diary:
    def __init__(self):
        self._entries = []
        self._counter = 1

    def add_entry(self, text):
        entry = f"{self._counter}. {text}"
        self._entries.append(entry)
        self._counter += 1

    def remove_entry(self, index):
        if 0 <= index < len(self._entries):
            self._entries.pop(index)
        else:
            raise IndexError("Sissekanne ei eksisteeri.")

    def get_entries(self):
        return list(self._entries)

    def set_entries(self, entries, start_counter):
        self._entries = list(entries)
        self._counter = start_counter

    def __str__(self):
        if not self._entries:
            return "(Päevik on tühi)"
        return "\n".join(self._entries)