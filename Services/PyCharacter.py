from typing import Any

class MissingElixir(Exception):
    def __init__(self, message, value = None):
        if not value:
            super().__init__(message)
        else:
            super().__init__(message, value)

class Character:
    plist = False
    atk = 1
    defs = 1
    hp = 100
    elx = 0
    full_list = {
        "atk": atk,
        "def": defs,
        "hp": hp,
        "elx": elx,
        "powers": plist
    }

    def __init__(self, name, charClass):
        self.name = name
        self.charClass = charClass

    def __str__(self):
        if not self.plist:
            return f"Character {self.name} created with class {self.charClass}"
        return f"Character {self.name} created with class {self.charClass} and powers: {str(self.plist)}"

    def __getitem__(self, item):
        return self.full_list[item]

    def __setitem__(self, key, value):
        self[key] = value
        return self[key]

    def __iter__(self):
        self.full_iter = []
        self.full_iter.append("atk")
        self.full_iter.append(self["atk"])
        self.full_iter.append("def")
        self.full_iter.append(self["def"])
        self.full_iter.append("elx")
        self.full_iter.append(self["elx"])
        self.full_iter.append("powers")
        self.full_iter.append(self["powers"])
        return iter(self.full_iter)

    def powers(self, plist: dict[Any, Any]):
        self.plist = plist
        self.full_list["powers"] = self.plist

    def stats(self, atk, defs, hp, elx):
        self.atk = atk
        self.defs = defs
        self.hp = hp
        self.elx = elx
        self.full_list = {
            "atk": atk,
            "def": defs,
            "hp": hp,
            "elx": elx,
            "powers": self.plist
        }

    def attack(self, power = None):
        if power is None:
            return self.atk
        if self.elx >= self.plist[power]["elx"]:
            self.elx -= self.plist[power]["elx"]
            return self.plist[power]["atk"] * self.atk
        raise MissingElixir(f"Not enough elixir to use power {power} for defense!")

    def rest(self, times: int, multiplier = 1):
        x = 0
        while x < times:
            self.elx += 1 * multiplier
            x += 1
        return self.elx

    def defend(self, power = None):
        if power is None:
            return self.defs
        if self.elx >= self.plist[power]["elx"]:
            self.elx -= self.plist[power]["elx"]
            return self.plist[power]['def'] + self.defs
        raise MissingElixir(f"Not enough elixir to use power {power} for defense!")

    def add_power(self, power_name, power_stats: dict[Any, Any]):
        self.plist[power_name] = power_stats
        self.full_list["powers"] = self.plist

class Fight:
    char_1: Character = Character("", "")
    char_2: Character = Character("", "")
    def __enter__(self):
        print("Starting fight!")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return f"Battle finished!"

    def __init__(self, char_1: Character, char_2: Character):
        self.char_1 = char_1
        self.char_2 = char_2

    def attack(self, char, power, power2):
        if char == "char_1":
            self.char_2.hp -= (self.char_1.attack(power) - self.char_2.defend(power2))
        elif char == "char_2":
            self.char_1.hp -= (self.char_2.attack(power) - self.char_1.defend(power2))
        if self.char_1.hp <= 0:
            print(f"The fight ended! {self.char_2.name} wins!")
            self.close()
            return self.char_2
        elif self.char_2.hp <= 0:
            print(f"The fight ended! {self.char_1.name} wins!")
            self.close()
            return self.char_1
        return f"{self.char_1.name} hp: {str(self.char_1.hp)}\n{self.char_2.name} hp: {str(self.char_2.hp)}"


    def rest(self, char, times: int, multiplier = 1):
        if char == "char_1":
            self.char_1.rest(times, multiplier)
            return self.char_1.elx
        elif char == "char_2":
            self.char_2.rest(times, multiplier)
            return self.char_2.elx


    def close(self):
        del self

