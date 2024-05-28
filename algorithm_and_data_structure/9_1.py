class BSTNode:
    def __init__(self, val=None, color=None):
        self.left = None
        self.right = None
        self.val = val
        self.color = color # Добавлен атрибут цвета

def build_bst(elements):
    if not elements:
        return None
    root = BSTNode(elements[0])
    for element in elements[1:]:
        insert(root, element)
    return root

def insert(node, val):
    if not node:
        return BSTNode(val)
    if val < node.val:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)
    return node
def search(node, val, color=None, comparisons=0):
    if not node:
        return False, comparisons
    comparisons += 1
    if val == node.val and (color is None or color == node.color):
        return True, comparisons
    elif val < node.val:
        return search(node.left, val, color, comparisons)
    else:
        return search(node.right, val, color, comparisons)

def add(node, val, color=None):
    if not node:
        return BSTNode(val, color)
    if val < node.val:
        node.left = add(node.left, val, color)
    else:
        node.right = add(node.right, val, color)
    return node

def delete(node, val):
    if not node:
        return None
    if val < node.val:
        node.left = delete(node.left, val)
    elif val > node.val:
        node.right = delete(node.right, val)
    else:
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        temp = find_min(node.right)
        node.val = temp.val
        node.right = delete(node.right, temp.val)
    return node

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def main():
    elements = [10, 5, 15, 3, 7, 13, 17, 1, 4]
    root = build_bst(elements)

    while True:
        print("\n1. Построить BST")
        print("2. Поиск элемента")
        print("3. Добавление элемента")
        print("4. Удаление элемента")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            root = build_bst(elements)
            print("BST построен.")
        if choice == "2":
            val = int(input("Введите значение для поиска: "))
            color = input("Введите цвет для поиска (оставьте пустым, если не нужен): ")
            found, comparisons = search(root, val, color)
            print(f"Значение найдено: {'Да' if found else 'Нет'}, количество сравнений: {comparisons}")

        if choice == "3":
            val = int(input("Введите значение для добавления: "))
            color = input("Введите цвет для добавления (оставьте пустым, если не нужен): ")
            root = add(root, val, color)
            print("Элемент добавлен.")

        elif choice == "4":
            val = int(input("Введите значение для удаления: "))
            root = delete(root, val)
            print("Элемент удален.")
        elif choice == "5":
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
