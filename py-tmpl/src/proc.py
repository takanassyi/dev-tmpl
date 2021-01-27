class Hello:
    def make_lemonade(self, count):
        print(count)

    def out_of_stock(self):
        print("out_of_stock")

    def print(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        fresh_fruit = {
            'apple': 10,
            'banana': 8,
            'lemon': 5,
        }
        print("****************************")

        count = fresh_fruit.get('lemon', 0)
        print(count)
        if count:
            self.make_lemonade(count)
        else:
            self.out_of_stock()

        return 'Hello World!!'
