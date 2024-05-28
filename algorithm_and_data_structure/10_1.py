def hash_function(text):
    if len(text) <= 10:
        return -1 # Специальное значение для строк меньше или равной 10 символов
    return sum(ord(character) for character in text)

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key):
        hash_value = hash_function(key)
        if hash_value == -1:
            print(f"Строка '{key}' не хешируется.")
            return
        self.table[hash_value % self.size].append(key)

    def search(self, key):
        hash_value = hash_function(key)
        if hash_value == -1:
            print(f"Строка '{key}' не хешируется.")
            return []
        return self.table[hash_value % self.size]

    def delete(self, key):
        hash_value = hash_function(key)
        if hash_value == -1:
            print(f"Строка '{key}' не хешируется.")
            return
        if key in self.table[hash_value % self.size]:
            self.table[hash_value % self.size].remove(key)


def main():
    # Создание хеш-таблицы
    hash_table = HashTable(11)

    # Ввод данных
    data = ["apple", "banannnnnnnnn", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "iceberg", "jackfruit","ГЕРЫ_ДОЛЖНЫ_ГОРЕТЬ"]
    for item in data:
        hash_table.insert(item)



if __name__ == "__main__":
    main()
