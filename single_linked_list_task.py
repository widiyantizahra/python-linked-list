class Node:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_task(self, description, priority):
        new_node = Node(description, priority)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            if new_node.priority > current.priority:
                new_node.next = current
                self.head = new_node
            else:
                while current.next and new_node.priority <= current.next.priority:
                    current = current.next
                new_node.next = current.next
                current.next = new_node

    def remove_task(self, description):
        if self.is_empty():
            print("Daftar tugas kosong.")
            return

        if self.head.description == description:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.description != description:
            current = current.next

        if current.next:
            current.next = current.next.next
        else:
            print("Tugas tidak ditemukan.")

    def print_tasks(self):
        if self.is_empty():
            print("Daftar tugas kosong.")
            return

        current = self.head
        while current:
            print(f"Deskripsi: {current.description} | Prioritas: {current.priority}")
            current = current.next

class Node:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_task(self, description, priority):
        new_node = Node(description, priority)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            if new_node.priority > current.priority:
                new_node.next = current
                self.head = new_node
            else:
                while current.next and new_node.priority <= current.next.priority:
                    current = current.next
                new_node.next = current.next
                current.next = new_node

    def remove_task(self, description):
        if self.is_empty():
            print("Daftar tugas kosong.")
            return

        if self.head.description == description:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.description != description:
            current = current.next

        if current.next:
            current.next = current.next.next
        else:
            print("Tugas tidak ditemukan.")

    def print_tasks(self):
        if self.is_empty():
            print("Daftar tugas kosong.")
            return

        current = self.head
        while current:
            print(f"Deskripsi: {current.description} | Prioritas: {current.priority}")
            current = current.next


# Contoh penggunaan
task_list = LinkedList()

task_list.add_task("les musik", 2)
task_list.add_task("membaca buku", 1)
task_list.add_task("Berolahraga", 3)

task_list.print_tasks()
# Output:
# Deskripsi: Berolahraga | Prioritas: 3
# Deskripsi: Les musik | Prioritas: 2
# Deskripsi: membaca buku | Prioritas: 1

task_list.remove_task("les musik")
task_list.remove_task("sepedaan")

task_list.print_tasks()
# Output:
# Deskripsi: Berolahraga | Prioritas: 3
# Deskripsi: Membaca buku | Prioritas: 1
