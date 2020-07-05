"""
Imagine you are creating a Super Mario game. You need to define
a class to represent Mario. What would it look like? If you aren't
familiar with SuperMario, use your own favorite video or board game
to model a player.
"""


class Mario:
    """
    class of Mario that has power and coin to collect
    """
    def __init__(self, color):
        """initializing mario"""
        self.color = color
        self.power = 0
        self.coin = 0
        self.level = 1

    def get_power(self):
        """updating power of mario"""
        self.power += 5
        return self.power

    def collect_coin(self):
        """updating the collection of coins"""
        self.coin += 1
        return self.coin

    def update_level(self):
        """increasing the level"""
        if self.level == "success":
            self.level += 1

