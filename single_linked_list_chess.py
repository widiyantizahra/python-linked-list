class Player:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
        self.next = None


class ChessTournament:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_player(self, name, rank):
        new_player = Player(name, rank)
        if self.is_empty():
            self.head = new_player
        else:
            current = self.head
            if new_player.rank < current.rank:
                new_player.next = current
                self.head = new_player
            else:
                while current.next and new_player.rank >= current.next.rank:
                    current = current.next
                new_player.next = current.next
                current.next = new_player

    def eliminate_player(self, name):
        if self.is_empty():
            print("Tidak ada peserta terdaftar.")
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
            print("Peserta tidak ditemukan.")

    def print_players(self):
        if self.is_empty():
            print("Tidak ada peserta terdaftar.")
            return

        current = self.head
        while current:
            print(f"Nama: {current.name} | Peringkat: {current.rank}")
            current = current.next


# Contoh penggunaan
tournament = ChessTournament()

tournament.add_player("ratna", 1500)
tournament.add_player("haikal", 1200)
tournament.add_player("ridho", 1800)
tournament.add_player("zuliana", 1600)

tournament.print_players()
# Output:
# Nama: ridho | Peringkat: 1800
# Nama: zuliana | Peringkat: 1600
# Nama: ratna | Peringkat: 1500
# Nama:  | Peringkat: 1200

tournament.eliminate_player("haikal")
tournament.eliminate_player("Mila")

tournament.print_players()
# Output:
# Nama: Budi | Peringkat: 1800
# Nama: Rina | Peringkat: 1600
# Nama: Siti | Peringkat: 1200
