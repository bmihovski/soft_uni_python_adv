class Smartphone:
    def __init__(self, memory: int, apps=list(), is_on=False):
        self.memory = memory
        self.apps = apps
        self.is_on = is_on

    def power(self):
        self.is_on = not self.is_on

    def install(self, app: str, needed_memory: int):
        if self.memory - needed_memory <= 0:
            return f"Not enough memory to install {app}"
        if not self.is_on:
            return f"Turn on your phone to install {app}"
        self.memory -= needed_memory
        self.apps.append(app)
        return f"Installing {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


smartphone: Smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
