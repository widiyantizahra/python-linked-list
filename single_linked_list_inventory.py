class Product:
    def __init__(self, name, code, stock):
        self.name = name
        self.code = code
        self.stock = stock
        self.next = None


class InventoryManagement:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_product(self, name, code, stock):
        new_product = Product(name, code, stock)
        if self.is_empty():
            self.head = new_product
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_product

    def remove_product(self, code):
        if self.is_empty():
            print("Inventaris kosong.")
            return

        if self.head.code == code:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.code != code:
            current = current.next

        if current.next:
            current.next = current.next.next
        else:
            print("Produk tidak ditemukan.")

    def print_inventory(self):
        if self.is_empty():
            print("Inventaris kosong.")
            return

        current = self.head
        while current:
            print(f"Nama Produk: {current.name} | Kode Produk: {current.code} | Jumlah Stok: {current.stock}")
            current = current.next


# Contoh penggunaan
inventory = InventoryManagement()

inventory.add_product("kerudung", "B001", 15)
inventory.add_product("gamis", "C001", 10)
inventory.add_product("rok", "S001", 6)

inventory.print_inventory()
# Output:
# Nama Produk: kerudung | Kode Produk: B001 | Jumlah Stok: 15
# Nama Produk: gamis | Kode Produk: C001 | Jumlah Stok: 10
# Nama Produk: rok | Kode Produk: S001 | Jumlah Stok: 6

inventory.remove_product("C001")
inventory.remove_product("S002")

inventory.print_inventory()
# Output:
# Nama Produk: kerudung | Kode Produk: B001 | Jumlah Stok: 15
# Nama Produk: rok | Kode Produk: S001 | Jumlah Stok: 6
