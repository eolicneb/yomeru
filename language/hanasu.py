from .tsubu import Tsubu
from .kanas import kanas, kanas_list
from language.dispatcher import ryuushi_dispatcher as ryuushi_dict


class Honbun:
    class_dipatcher = {('imi', 'uchiryuu'): "tsubu",
                       ('imi', 'kao', 'onsei'): "ryuushi"}

    def __init__(self):
        self.honbun_list = []

    def make_ryuushi(self, imi, kao, onsei):
        shi = ryuushi_dict[kao]
        if onsei or imi:
            shi.onsei = onsei
            shi.imi = imi
        return shi

    def make_tsubu(self, imi, uchiryuu):
        def select(object):
            if self.class_dipatcher[tuple(object.keys())] == "ryuushi":
                return self.make_ryuushi(**object)
            else:
                return self.make_tsubu(**object)
        ryuu = [select(obj) for obj in uchiryuu]
        return Tsubu(imi=imi, uchiryuu=ryuu)

    def from_dict(self, dict_data):
        self.honbun_list = [self.make_tsubu(**obj) for obj in dict_data]

    def to_dict(self, tsubu):
        return [self.bun_to_dict(bun) for bun in self.honbun_list]

    def bun_to_dict(self, tsubu):
        if hasattr(tsubu, '_uchiryuu'):
            return {'imi': tsubu.imi,
                    'uchiryuu': [self.bun_to_dict(shi) for shi in tsubu.uchiryuu]}
        else:
            return {'imi': tsubu.imi, 'kao': tsubu.kao, 'onsei': tsubu.onsei}
