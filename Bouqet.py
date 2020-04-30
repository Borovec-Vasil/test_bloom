import re

OUTPUT_FILE = 'output'


class Bouquets:

    def __init__(self):
        self.waiting_bouquets = {
            "L": [],
            "S": []
        }

    @staticmethod
    def parse_name(bouquet_name):

        list_of_flowers = re.findall('\d*\D+', bouquet_name[2:])

        numbers = [int(i) for i in re.findall('\d+', bouquet_name[2:])]

        if sum(numbers[:-1]) != numbers[-1]: # !!! Just log, Don't know what to do
            print(f"Total quantity not equal to sum of flowers --- {bouquet_name} !!!!")
            #TODO something

        list_of_flowers = {
            flower[-1]: int(flower[:-1]) for flower in list_of_flowers
        }

        list_of_flowers.update({
            "name": bouquet_name[0],
            "size": bouquet_name[1],
            "id": bouquet_name
        })

        return list_of_flowers

    def add_bouquet(self, bouquet_name):
        try:

            parsed_name = self.parse_name(bouquet_name)
            self.waiting_bouquets[parsed_name['size']].append(parsed_name)

        except (IndexError, ValueError, KeyError) as e:
            print(f"Name {bouquet_name} is wrong !!!")

    def complete(self, item):

        with open(OUTPUT_FILE, 'a') as f:
            f.write(item['id'] + '\n')

        self.waiting_bouquets[item['size']].remove(item)