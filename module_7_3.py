# Домашнее задание по теме "Оператор "with".
# Задача "Найдёт везде":

class WordsFinder:
    file_names = []
    def __init__(self, *names):
        self.file_names += names

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            with open(file, 'r', encoding='utf-8') as f:
                strings = f.read().lower()
                punctuation_to_remove = "',.!?;:-"
                translator = str.maketrans('', '', punctuation_to_remove)
                strings = strings.translate(translator)
                words = strings.split()
                all_words[file] = words
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word in words:
                result[name] = words.index(word) + 1
        return result

    def count(self,word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file, words in all_words.items():
            count = words.count(word)
            if count > 0:
                result[file] = count
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
