class Item:
    def __init__(self, name, importance):
        self.name = name
        self.importance = importance
        self.next = None


class AdventureBag:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_item(self, name, importance):
        new_item = Item(name, importance)
        if self.is_empty():
            self.head = new_item
        else:
            current = self.head
            if new_item.importance > current.importance:
                new_item.next = current
                self.head = new_item
            else:
                while current.next and new_item.importance <= current.next.importance:
                    current = current.next
                new_item.next = current.next
                current.next = new_item

    def remove_item(self, name):
        if self.is_empty():
            print("Tas kosong.")
            return

        if self.head.name == name:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.name != name:
            current = current.next

        if current.next:
            current.next = current.next.next
        else:
            print("Item tidak ditemukan.")

    def print_items(self):
        if self.is_empty():
            print("Tas kosong.")
            return

        current = self.head
        while current:
            print(f"Nama Item: {current.name} | Tingkat Kepentingan: {current.importance}")
            current = current.next


# Contoh penggunaan
adventure_bag = AdventureBag()

adventure_bag.add_item("BUMI tereliye", 5)
adventure_bag.add_item("Laskar pelangi", 3)
adventure_bag.add_item("Rumah kaca", 4)
adventure_bag.add_item("Panah Sakti", 2)

adventure_bag.print_items()
# Output:
# Nama Item: BUMI tereliye | Tingkat Kepentingan: 5
# Nama Item: Rumah kaca | Tingkat Kepentingan: 4
# Nama Item: Laskar pelangi | Tingkat Kepentingan: 3
# Nama Item: Panah Sakti | Tingkat Kepentingan: 2

adventure_bag.remove_item("Panah Sakti")
adventure_bag.remove_item("Tongkat Ajaib")

adventure_bag.print_items()
# Output:
# Nama Item: BUMI tereliye | Tingkat Kepentingan: 5
# Nama Item: Rumah kaca | Tingkat Kepentingan: 4
# Nama Item: Laskar pelangi | Tingkat Kepentingan: 3
