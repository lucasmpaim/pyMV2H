from functools import lru_cache

from .f1 import f1_score
from ..utils.freeze_args import freeze_args
from ..utils.matches import note_match, match_note_list


@freeze_args()
@lru_cache(maxsize=128)
def multi_pitch_accuracy(p_notes: list, t_notes: list, return_match_notes=False):
    match_notes = match_note_list(p_notes, t_notes)
    true_positives = len(match_notes.keys())

    if return_match_notes:
        return f1_score(
            true_positives=true_positives,
            false_positives=abs(true_positives - len(t_notes)),
            false_negatives=abs(true_positives - len(p_notes))
        ), match_notes
    else:
        return f1_score(
            true_positives=true_positives,
            false_positives=abs(true_positives - len(t_notes)),
            false_negatives=abs(true_positives - len(p_notes))
        )
