from re import findall


class QuantityErr(Exception):
    pass


class NoneEqErr(Exception):
    pass


class NoneReqErr(Exception):
    pass


class Storage:
    equip_stor = {
        'Printer': 0,
        'Xerox': 0,
        'Fax': 0,
        'Shredder': 0
    }

    def __init__(self, volume):
        self.volume = volume

    @classmethod
    def storage_add(cls, printer=0, xerox=0, fax=0, shredder=0, **kwargs):
        Storage.equip_stor['Printer'] += printer
        Storage.equip_stor['Xerox'] += xerox
        Storage.equip_stor['Fax'] += fax
        Storage.equip_stor['Shredder'] += shredder
        for key, value in kwargs.items():
            Storage.equip_stor[key.title()] = value

    @classmethod
    def storage_add_unit(cls, name_cls):
        name_cls = ''.join(findall("\.(?P<class>\w+)'", str(name_cls.__class__)))
        Storage.equip_stor[name_cls] += 1

    @classmethod
    def pick_up_eq(cls, **kwargs):
        try:
            for key in kwargs:
                if not key.title() in Storage.equip_stor.keys():
                    raise NoneEqErr(f'{key.title()} нет на складе')
                elif not key.title() in cls.requrement.keys():
                    raise NoneReqErr(f'Отделу не требудется - {key.title()}')

        except (NoneEqErr, NoneReqErr) as err:
            print(err)
        else:
            try:
                for key, value in kwargs.items():
                    if Storage.equip_stor.get(key.title()) < value or cls.requrement.get \
                                (key.title()) < value:
                        raise QuantityErr(f'Запросили слишком много {key.title()}')
                    Storage.equip_stor[key.title()] -= value
                    cls.requrement[key.title()] -= value
            except QuantityErr as err:
                print(err)


class Department1(Storage):
    requrement = {  # Что нужно отделу
        'Printer': 7,
        'Xerox': 2,
        'Fax': 4,
    }


class Equipment:
    q_equip = 0

    def __init__(self, speed, format_pap):
        self.speed = speed
        self.format_pap = list(format_pap)

    def __str__(self):
        if 'iscolored' in self.__dir__():
            return f'{self.__class__} с характеристиками: скорость ' \
                   f'{self.speed}, формат бумаги {self.format_pap}, цветной - {self.iscolored}'
        else:
            return f'{self.__class__} с характеристиками: скорость ' \
                   f'{self.speed}, формат бумаги {self.format_pap}'


class Printer(Equipment):
    def __init__(self, speed, format_pap, iscolored=False):
        Equipment.q_equip += 1
        super().__init__(speed, format_pap)
        self.iscolored = iscolored


class Xerox(Equipment):
    def __init__(self, speed, format_pap, iscolored=False):
        Equipment.q_equip += 1
        super().__init__(speed, format_pap)
        self.iscolored = iscolored


class Fax(Equipment):
    def __init__(self, speed, format_pap, iscolored=False):
        Equipment.q_equip += 1
        super().__init__(speed, format_pap)
        self.iscolored = iscolored


class Shredder(Equipment):
    Equipment.q_equip += 1


p1 = Printer(50, ['A4', 'A3'])
x1 = Xerox(60, 'A2', True)
f1 = Fax(5, 'A4')
sh1 = Shredder(100, 'A4')
Storage.storage_add(10, 10, 10, 10)
print(Storage.equip_stor)
Storage.storage_add_unit(p1)
Storage.storage_add_unit(x1)
Storage.storage_add_unit(f1)
Storage.storage_add_unit(sh1)
print(Storage.equip_stor)
print(Department1.requrement)
Department1.pick_up_eq(fax=2, xerox=2)
Department1.pick_up_eq(shredder=5)
print(Storage.equip_stor)
print(Department1.requrement)
