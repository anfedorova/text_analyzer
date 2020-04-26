from collections import Counter
from operator import itemgetter


class AnalyzeText:

    def __init__(self, file_name):
        self.text_len = 0
        self.CHARS = " ,?’–.!/;:̈"
        self.counter = Counter()
        with open(file_name) as file:
            self.text = file.read().replace('\n', '')

    def _clear_text(self):
        for char in self.text:
            if char in self.CHARS:
                self.text = self.text.replace(char, '').lower()

        self.text_len = len(self.text)

    def _string_division(self):
        combination_array = [self.text[i: i + 3] for i in range(self.text_len)]

        for word in combination_array:
            self.counter[word] += 1

    def generate_result(self):
        self._clear_text()
        self._string_division()
        for i in self.counter.keys():
            self.counter[i] = self.counter[i] / self.text_len

        list_d = list(self.counter.items())
        list_c = sorted(list_d, key=itemgetter(1), reverse=True)
        result = {}
        for i in list_c:
            result[i[0]] = round(i[1], 4)

        return result

