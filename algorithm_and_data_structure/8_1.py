class ArrayList:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return len(self.list) == 0

    def add(self, item):
        self.list.append(item)

    def remove(self, item):
        if item in self.list:
            self.list.remove(item)

    def display(self):
        return self.list

    def clear(self):
        self.list.clear()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, data):
        if self.is_empty():
            return
        if self.head.data == data:
            self.head = self.head.next
        else:
            current = self.head
            while current.next and current.next.data != data:
                current = current.next
            if current.next:
                current.next = current.next.next

    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        return elements

    def clear(self):
        self.head = None

    def search(self, data):
        if self.is_empty():
            return None
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return None
def main():
    list_type = input("Выберите тип списка (1 - массив, 2 - связный список): ")
    if list_type == "1":
        list = ArrayList()
    elif list_type == "2":
        list = LinkedList()
    else:
        print("Неверный выбор.")
        return

    while True:
        print("\n1. Добавить элемент")
        print("2. Удалить элемент")
        print("3. Просмотреть содержимое списка")
        print("4. Очистить список")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            item = input("Введите элемент: ")
            list.add(item)
        elif choice == "2":
            item = input("Введите элемент для удаления: ")
            list.remove(item)
        elif choice == "3":
            print("Содержимое списка:", list.display())
        elif choice == "4":
            list.clear()
            print("Список очищен.")
        elif choice == "5":
            item = input("Введите элемент для поиска: ")
            index = list.search(item)
            if index is not None:
                print(f"Элемент найден на позиции {index}")
            else:
                print("Элемент не найден.")
        elif choice == "6":
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
