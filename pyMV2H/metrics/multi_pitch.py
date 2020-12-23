from .f1 import f1_score
from ..utils.matches import note_match


def multi_pitch_accuracy(p_notes: list, t_notes: list, return_match_notes=False):
    true_positives = 0
    match_notes = dict()

    for t_note in t_notes:
        for p_note in p_notes:
            if note_match(t_note, p_note):
                # Found a match
                true_positives += 1
                match_notes[t_note] = p_note
                break

    if return_match_notes:
        return f1_score(
            true_positives=true_positives,
            false_positives=len(t_notes) - true_positives,
            false_negatives=len(p_notes) - true_positives
        ), match_notes
    else:
        return f1_score(
            true_positives=true_positives,
            false_positives=len(t_notes) - true_positives,
            false_negatives=len(p_notes) - true_positives
        )
