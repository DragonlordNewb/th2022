import random

class Quipset:
    def __init__(self, *data):
        self.data = data

    def get(self):
        return self.data[random.randint(0, len(self.data) - 1)]

interesting = Quipset("Interesting.",
    "Hmm.",
    "Alright.",
    "Okay."
)
