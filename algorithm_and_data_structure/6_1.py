class StackArray:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def pop_first(self):
        if self.is_empty():
            return None
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        return popped_node.data

    def pop_last(self):
        if self.is_empty():
            return None
        if self.head.next is None:  # Если в списке только один элемент
            popped_node = self.head
            self.head = None
            return popped_node.data
        current_node = self.head
        while current_node.next.next is not None:  # Находим предпоследний элемент
            current_node = current_node.next
        popped_node = current_node.next  # Последний элемент
        current_node.next = None  # Удаляем ссылку на последний элемент
        popped_node.next = None  # Освобождаем память
        return popped_node.data

    def display(self):
        return self.stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def pop_first(self):
        if self.is_empty():
            return None
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        return popped_node.data

    def pop_last(self):
        if self.is_empty():
            return None
        if self.head.next is None:  # Если в списке только один элемент
            popped_node = self.head
            self.head = None
            return popped_node.data
        current_node = self.head
        while current_node.next.next is not None:  # Находим предпоследний элемент
            current_node = current_node.next
        popped_node = current_node.next  # Последний элемент
        current_node.next = None  # Удаляем ссылку на последний элемент
        popped_node.next = None  # Освобождаем память
        return popped_node.data





    def display(self):
        elements = []
        current_node = self.head
        while current_node is not None:
            elements.append(current_node.data)
            current_node = current_node.next
        return elements
def main():
    stack_type = input("Выберите тип стека (1 - массив, 2 - связный список): ")
    if stack_type == "1":
        stack = StackArray()
    elif stack_type == "2":
        stack = StackLinkedList()
    else:
        print("Неверный выбор.")
        return

    while True:
        print("\n1. Добавить элемент")
        print("2. Удалить элемент")
        print("3. Просмотреть верхний элемент")
        print("4. Просмотреть содержимое стека")
        print("5. Выход")
        print("6. Удаление первого элемента")
        print("7. Удален последний элемент")
        choice = input("Выберите действие: ")

        if choice == "1":
            item = input("Введите элемент: ")
            stack.push(item)
        elif choice == "2":
            print("Удален элемент:", stack.pop())
        elif choice == "3":
            print("Верхний элемент:", stack.peek())
        elif choice == "4":
            print("Содержимое стека:", stack.display())
        elif choice == "5":
            break
        elif choice == "6":
            print("Удален первый элемент:", stack.pop_first())
        elif choice == "7":
            print("Удален последний элемент:", stack.pop_last())
        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    main()
