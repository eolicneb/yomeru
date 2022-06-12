from language.kanas import kanas_list
from language.ryuushi import Ryuushi
from text.used_kanjis import iwanai, kanjis


def recursive_kanas(kana_bun):
    try:
        kanas_list(kana_bun)
        return kanas_list.bun_list[:]
    except ValueError:
        done_list = kanas_list.bun_list[:]
        done_position = kanas_list.index
        not_done_yet = recursive_kanas(kana_bun[done_position+1:])
        failed = kana_bun[done_position]
        if failed in iwanai:
            return done_list + [iwanai[failed]] + not_done_yet
        elif failed in kanjis:
            return done_list + [kanjis[failed]()] + not_done_yet
        else:
            patch = Ryuushi()
            patch._kao = failed
            return done_list + [patch] + not_done_yet
