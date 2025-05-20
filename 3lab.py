class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
            return
        current = self.head
        for _ in range(index - 1):
            if current.next is None:
                break
            current = current.next
        new_node.next = current.next
        current.next = new_node
    
    def delete(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
    
    def find(self, value):
        index = 0
        current = self.head
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1
    
    def print_list(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        print(" -> ".join(values))

def merge_alternate(list1, list2):
    merged = LinkedList()
    current1 = list1.head
    current2 = list2.head
    while current1 or current2:
        if current1:
            merged.append(current1.value)
            current1 = current1.next
        if current2:
            merged.append(current2.value)
            current2 = current2.next
    return merged


if __name__ == "__main__":
    print("Демонстрация работы методов LinkedList:")
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    print("После добавления в начало и конец:")
    ll.print_list()  

    ll.insert(2, 1.5)
    print("После вставки 1.5 по индексу 2:")
    ll.print_list() 

    ll.delete(1.5)
    print("После удаления 1.5:")
    ll.print_list()  

    print("Индекс значения 2:", ll.find(2))  
    print("Индекс несуществующего значения 5:", ll.find(5))  

    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)

    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)

    merged = merge_alternate(list1, list2)
    print("\nРезультат слияния списков list1 и list2:")
    merged.print_list()  # 1 -> 2 -> 3 -> 4 -> 5 -> 6

    list3 = LinkedList()
    list3.append(1)
    list3.append(3)
    list3.append(5)
    list3.append(7)
    list3.append(9)

    list4 = LinkedList()
    list4.append(2)
    list4.append(4)

    merged2 = merge_alternate(list3, list4)
    print("\nРезультат слияния списков разной длины:")
    merged2.print_list()
