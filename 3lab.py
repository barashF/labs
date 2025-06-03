class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0  
    
    def custom_append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1  
    
    def custom_prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1  
    
    def custom_insert(self, index, value):
        if index < 0:
            raise IndexError("Индекс не может быть отрицательным")
        
        if index == 0:
            self.custom_prepend(value)
            return
        
        if index > self.size:
            index = self.size  
        
        new_node = Node(value)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1  
    
    def custom_delete(self, value):
        if self.head is None:
            return
        
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1 
            return
        
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next
    
    def custom_find(self, value):
        index = 0
        current = self.head
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1
    
    def custom_print_list(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        print(" -> ".join(values) + f" | Размер: {self.size}")


def merge_alternate(list1, list2):
    merged = LinkedList()
    current1 = list1.head
    current2 = list2.head
    while current1 or current2:
        if current1:
            merged.custom_append(current1.value)
            current1 = current1.next
        if current2:
            merged.custom_append(current2.value)
            current2 = current2.next
    return merged


if __name__ == "__main__":
    print("Демонстрация работы методов LinkedList с учетом размера:")
    ll = LinkedList()
    ll.custom_append(1)
    ll.custom_append(2)
    ll.custom_append(3)
    ll.custom_prepend(0)
    print("После использования custom_prepend и custom_append:")
    ll.custom_print_list()  # Ожидаем: 0 -> 1 -> 2 -> 3 | Размер: 4

    ll.custom_insert(2, 1.5)
    print("После вызова custom_insert с индексом 2:")
    ll.custom_print_list()  # Ожидаем: 0 -> 1 -> 1.5 -> 2 -> 3 | Размер: 5

    ll.custom_delete(1.5)
    print("После вызова custom_delete для значения 1.5:")
    ll.custom_print_list()  # Ожидаем: 0 -> 1 -> 2 -> 3 | Размер: 4

    print("Индекс значения 2:", ll.custom_find(2))  # Ожидаем: 2
    print("Индекс несуществующего значения 5:", ll.custom_find(5))  # Ожидаем: -1

    print("Текущий размер списка:", ll.size)  # Ожидаем: 4

    list1 = LinkedList()
    list1.custom_append(1)
    list1.custom_append(3)
    list1.custom_append(5)

    list2 = LinkedList()
    list2.custom_append(2)
    list2.custom_append(4)
    list2.custom_append(6)

    merged = merge_alternate(list1, list2)
    print("\nРезультат слияния списков list1 и list2:")
    merged.custom_print_list()

    list3 = LinkedList()
    list3.custom_append(1)
    list3.custom_append(3.0)
    list3.custom_append(5)
    list3.custom_append(7)
    list3.custom_append(True)

    list4 = LinkedList()
    list4.custom_append('two')
    list4.custom_append('four')

    merged2 = merge_alternate(list3, list4)
    print("\nРезультат слияния списков разной длины:")
    merged2.custom_print_list() 