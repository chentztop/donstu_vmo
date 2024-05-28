import math
class QueueArray:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.head = self.tail = -1
        self.max_size = max_size

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.tail + 1) % self.max_size == self.head

    def enqueue(self, data):
        if self.is_full():
            print("Очередь полна")
            return
        if self.is_empty():
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.max_size
        self.queue[self.tail] = data

    def dequeue(self):
        if self.is_empty():
            print("Очередь пуста")
            return
        temp = self.queue[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.max_size
        return temp

    def display(self):
        if self.is_empty():
            print("Очередь пуста")
            return
        if self.tail >= self.head:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.head, self.max_size):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
        print()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Очередь пуста")
            return
        temp = self.front
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        return temp.data

    def display(self):
        if self.is_empty():
            print("Очередь пуста")
            return
        current_node = self.front
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    def average_negative(self):
        if self.is_empty():
            return None
        count = 0
        sum = 0
        current_node = self.front
        while current_node is not None:
            if float(current_node.data) < 0:  # Преобразование в float для поддержки чисел с плавающей точкой
                count += 1
                sum += float(current_node.data)
            current_node = current_node.next
        if count == 0:
            return None
        return sum / count

    def geometric_negative(self):
        if self.is_empty():
            return None
        count = 0
        product = 1
        current_node = self.front
        while current_node is not None:
            try:
                data = float(current_node.data)  # Преобразование в float для поддержки чисел с плавающей точкой
                if data < 0:
                    count += 1
                    product *= data
            except ValueError:
                print("Ошибка: данные не могут быть преобразованы в число.")
            current_node = current_node.next
        if count == 0:
            return None
        return math.pow(abs(product), 1 / count)
def main():
    queue_type = input("Выберите тип очереди (1 - массив, 2 - связный список): ")
    if queue_type == "1":
        max_size = int(input("Введите максимальный размер очереди: "))
        queue = QueueArray(max_size)
    elif queue_type == "2":
        queue = QueueLinkedList()
    else:
        print("Неверный выбор.")
        return

    while True:
        print("\n1. Добавить элемент")
        print("2. Удалить элемент")
        print("3. Просмотреть содержимое очереди")
        print("4. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            item = input("Введите элемент: ")
            queue.enqueue(item)
        elif choice == "2":
            print("Удален элемент:", queue.dequeue())
        elif choice == "3":
            print("Содержимое очереди:")
            queue.display()
        elif choice == "4":
            print("Среднее арифметическое отрицательных чисел:", queue.average_negative())
        elif choice == "5":
            print("Геометрическое среднее отрицательных чисел:", queue.geometric_negative())
        elif choice == "6":
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
