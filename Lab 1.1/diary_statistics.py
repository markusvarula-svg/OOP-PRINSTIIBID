class DiaryStatistics:
    @staticmethod
    def entry_count(diary):
        return len(diary.get_entries())

    @staticmethod
    def average_entry_length(diary):
        entries = diary.get_entries()
        if not entries:
            return 0
        total = sum(len(e) for e in entries)
        return round(total / len(entries), 2)

    @staticmethod
    def longest_entry(diary):
        entries = diary.get_entries()
        if not entries:
            return None
        return max(entries, key=len)

    @staticmethod
    def print_statistics(diary):
        print(f"Sissekannete arv:       {DiaryStatistics.entry_count(diary)}")
        print(f"Keskmine pikkus:        {DiaryStatistics.average_entry_length(diary)} tähemärki")
        longest = DiaryStatistics.longest_entry(diary)
        if longest:
            print(f"Pikim sissekanne:{longest}")