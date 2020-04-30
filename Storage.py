from collections import defaultdict


class StorageStream:

    def __init__(self, bouquets):
        self.available_flowers = {
            "S": defaultdict(int),
            "L": defaultdict(int)
        }
        self.bouquets = bouquets

    def add_flower(self, flower, size):
        try:
            self.available_flowers[size][flower] += 1
        except KeyError:
            print(f"Size {size} is wrong")

        else:
            completed_bouquet = self.check_complete(size)

            if completed_bouquet:
                self.bouquets.complete(completed_bouquet)
                self.del_flowers(completed_bouquet)

    def check_complete(self, size):

        for bouquet in self.bouquets.waiting_bouquets[size]:
            result = True
            for key, value in bouquet.items():
                if key not in ['id', 'name', 'size']:
                    if self.available_flowers[bouquet['size']][key] < value:
                        result = False
                        break

            if result:
                return bouquet
        return False

    def del_flowers(self, bouquet):

        for key, value in bouquet.items():
            if key not in ['id', 'name', 'size']:
                self.available_flowers[bouquet['size']][key] -= value

