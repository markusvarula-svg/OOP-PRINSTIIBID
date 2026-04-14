import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from diary import Diary


class DiaryPersistence:
    @staticmethod
    def save_to_file(diary, filename):
        entries = diary.get_entries()
        with open(filename, "w", encoding="utf-8") as f:
            for entry in entries:
                f.write(entry + "\n")

    @staticmethod
    def load_from_file(filename):
        diary = Diary()
        entries = []
        max_number = 0

        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if line:
                    entries.append(line)
                    try:
                        number = int(line.split(".")[0])
                        if number > max_number:
                            max_number = number
                    except ValueError:
                        pass

        diary.set_entries(entries, max_number + 1)
        return diary