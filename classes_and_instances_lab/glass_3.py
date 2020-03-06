class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def glass_content(self):
        return Glass.capacity - self.content

    def fill(self, ml: int):
        if self.glass_content() <= ml:
            return f"Cannot add {ml} ml"
        self.content += ml
        return f"Glass filled with {ml} ml"

    def empty(self):
        self.content = 0
        return f"Glass is now empty"

    def info(self):
        return f"{self.glass_content()} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
