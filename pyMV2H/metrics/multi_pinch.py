from .f1 import f1_score
from ..utils.notes_match import match


def multi_pinch_accuracy(p_notes: list, t_notes: list):
    true_positives = 0

    for t_note in t_notes:
        for p_note in p_notes:
            if match(t_note, p_note):
                # Found a match
                true_positives += 1
                break

    return f1_score(
        true_positives=true_positives,
        false_positives=len(t_notes) - true_positives,
        false_negatives=len(p_notes) - true_positives
    )
