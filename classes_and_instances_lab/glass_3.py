class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml: int):
        current_content = self.content + ml
        if current_content >= Glass.capacity:
            return f"Cannot add {ml} ml"
        self.content += ml
        return f"Glass filled with {ml} ml"

    def empty(self):
        self.content = 0
        return f"Glass is now empty"

    def info(self):
        current_content = Glass.capacity - self.content
        return f"{current_content} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
