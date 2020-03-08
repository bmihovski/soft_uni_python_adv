class Hero:
    def __init__(self, username: str, level: int):
        self.username = username
        self.level = level

    def __repr__(self):
        return f"{self.username} of type {self.__class__.__name__} has level {self.level}"


class Elf(Hero):
    def __init__(self, username: str, level: int):
        Hero.__init__(self, username, level)


class MuseElf(Elf):
    def __init__(self, username: str, level: int):
        Elf.__init__(self, username, level)


class Wizard(Hero):
    def __init__(self, username: str, level: int):
        Hero.__init__(self, username, level)


class DarkWizard(Wizard):
    def __init__(self, username: str, level: int):
        Wizard.__init__(self, username, level)


class SoulMaster(DarkWizard):
    def __init__(self, username: str, level: int):
        DarkWizard.__init__(self, username, level)


class Knight(Hero):
    pass


class DarkKnight(Knight):
    pass


class BladeKnight(DarkKnight):
    pass

from unittest import TestCase


class HeroTests(TestCase):
    def test_zero(self):
        hero: Hero = Hero("icho", 10)
        self.assertEqual("icho", hero.username)
        self.assertEqual(10, hero.level)
        self.assertEqual("icho of type Hero has level 10", hero.__repr__())


class ElfTests(TestCase):
    def test_zero(self):
        elf: Elf = Elf("do", 13)
        self.assertEqual("do of type Elf has level 13", elf.__repr__())


class MuseElfTests(TestCase):
    def test_zero(self):
        muse_elf: MuseElf = MuseElf("dde", 23)
        self.assertEqual("dde of type MuseElf has level 23", muse_elf.__repr__())


class WizardTests(TestCase):
    def test_zero(self):
        wizard: Wizard = Wizard("ddw", 24)
        self.assertEqual("ddw of type Wizard has level 24", wizard.__repr__())


class DarkWizardTests(TestCase):
    def test_zero(self):
        dark_wizard: DarkWizard = DarkWizard("ddsw", 32)
        self.assertEqual("ddsw of type DarkWizard has level 32", dark_wizard.__repr__())


class SoulMasterTests(TestCase):
    def test_zero(self):
        soul_master: SoulMaster = SoulMaster("sww", 223)
        self.assertEqual("sww of type SoulMaster has level 223", soul_master.__repr__())


class KnightTests(TestCase):
    def test_zero(self):
        knight: Knight = Knight("sdfs", 224)
        self.assertEqual("sdfs of type Knight has level 224", knight.__repr__())


class DarkKnightTests(TestCase):
    def test_zero(self):
        dark_knight: DarkKnight = DarkKnight("eddf", 2342)
        self.assertEqual("eddf of type DarkKnight has level 2342", dark_knight.__repr__())


class BladeKnightTests(TestCase):
    def test_zero(self):
        blade_knight: BladeKnight = BladeKnight("dwww", 2300)
        self.assertEqual("dwww of type BladeKnight has level 2300", blade_knight.__repr__())

if __name__ == '__main__':
    TestCase.main()