from Bouqet import Bouquets
from Storage import StorageStream

bouquets = Bouquets()
stream = StorageStream(bouquets)


def start_stream(input_file):

    with open(input_file, 'r') as f:

        while True:

            bouquet = f.readline().replace('\n', '')

            if not bouquet:
                break

            bouquets.add_bouquet(bouquet)

        while True:
            flower = f.readline().replace('\n', '')
            try:
                stream.add_flower(flower[0], flower[1])

            except IndexError:
                break


if __name__ == '__main__':
    start_stream('input')
    print('Done')












