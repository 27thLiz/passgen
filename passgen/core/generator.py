"""the password generator"""

import random
from pathlib import Path

class generator:
    def generate_password(self, filename, min_len, max_len, count, seperator):
        path = Path(filename)
        if not path.exists():
            print("error: file does not exist") #TODO log error
            return
        words = path.open()

        matched_words = []

        for word in words:
            word_len = len(word)
            if word_len >= min_len and word_len <= max_len and word.find("'") == -1:
                matched_words.append(word)

        password = ""
        for i in range(0, count):
            index = random.randint(0, len(matched_words))
            word = matched_words[index].strip('\n')
            word = word.upper() if random.randint(0, 1) == 0 else word.lower()
            password += word
            if i != count - 1:
                password += seperator

        return password
