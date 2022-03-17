"""SRP SOC
Принцип единственной ответственности
Single Responsibility Principle

Если у вас есть класс, у этого класса дожна быть основаня отвественность. Он НЕ ДОЛЖЕН брать на себя другие ответственности!
"""


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # Нарушаем SRP
    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def load_from_web(self, uri):
    #     pass


class PersistenceManager:
    @staticmethod
    def save_to_file(filename, journal: Journal):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry('Why me?')
j.add_entry('Love u')

print(j)

file = 'journal.txt'
PersistenceManager.save_to_file(file, j)

with open(file, 'r') as fh:
    print(fh.read())

'''
ВЫВОД: не стоит перегружать свои обьекты слишком большим количеством обязанностей.
Антипаттерн - GodObject(Всемогущий объект)
'''