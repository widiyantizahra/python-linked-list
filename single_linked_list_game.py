class Item:
    def __init__(self, nama, kepentingan):
        self.nama = nama
        self.kepentingan = kepentingan
        self.next = None

class Tas:
    def __init__(self):
        self.head = None

    def tambah_item(self, nama, kepentingan):
        item_baru = Item(nama, kepentingan)
        
        if self.head is None:
            self.head = item_baru
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = item_baru

    def hapus_item(self, nama):
        if self.head is None:
            return
        
        if self.head.nama == nama:
            self.head = self.head.next
        else:
            curr = self.head
            prev = None
            while curr is not None and curr.nama != nama:
                prev = curr
                curr = curr.next
            if curr is None:
                return
            prev.next = curr.next

    def cetak_daftar_item(self):
        if self.head is None:
            print("Tas kosong.")
        else:
            curr = self.head
            print("Daftar item dalam tas:")
            while curr is not None:
                print(f"Nama: {curr.nama}, Kepentingan: {curr.kepentingan}")
                curr = curr.next


# Contoh penggunaan program

# Membuat objek tas
tas = Tas()

# Menambahkan beberapa item ke dalam tas
tas.tambah_item("Potion", 5)
tas.tambah_item("Pedang Emas", 10)
tas.tambah_item("Kunci Ajaib", 8)
tas.tambah_item("Armor Kuat", 9)

# Mencetak daftar item dalam tas
tas.cetak_daftar_item()
# Output:
# Daftar item dalam tas:
# Nama: Potion, Kepentingan: 5
# Nama: Pedang Emas, Kepentingan: 10
# Nama: Kunci Ajaib, Kepentingan: 8
# Nama: Armor Kuat, Kepentingan: 9

# Menghapus item "Kunci Ajaib" dari tas
tas.hapus_item("Kunci Ajaib")

# Mencetak daftar item setelah penghapusan
tas.cetak_daftar_item()
# Output:
# Daftar item dalam tas:
# Nama: Potion, Kepentingan: 5
# Nama: Pedang Emas, Kepentingan: 10
# Nama: Armor Kuat, Kepentingan: 9
