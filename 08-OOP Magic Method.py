class TestObj:

    def __init__(self, number):
        self.number = number
        self.list = []

    def __str__(self):
        return (
            f"TestObj("
                    f"The list: {len(self.list)}, "
                    f"Number: {self.number}"
                    ")"
        )

obj_1 = TestObj(3)
print(obj_1)