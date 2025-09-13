def get_num_words(text):
        return len(text.split())

def count_characters(text):
        counts = {}
        for ch in text:
            ch = ch.lower()
            counts[ch] = counts.get(ch, 0) +1
        return counts

def sort_on(item):
    return item["num"]

def build_sorted_char_list(counts):
        characters = []
        for ch, n in counts.items():
                if not ch.isalpha():
                        continue
                if not ("a" <= ch <= "z"):
                        continue
                characters.append({"char": ch, "num": n})
        characters.sort(reverse=True, key=sort_on)
        return characters
       