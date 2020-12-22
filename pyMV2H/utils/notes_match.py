from pyMV2H.utils.algorithm_config import ONSET_DELTA
from pyMV2H.utils.pojos import NOTE


def match(note_a: NOTE, note_b: NOTE) -> bool:
    """
    Return if both notes match using ONSET_DELTA tolerance
    :param note_a: first note to check
    :param note_b: second note to check
    :return: a boolean that indicates if both notes are matched
    """
    return (
            note_a.pitch == note_b.pitch and
            abs(note_a.on - note_b.on) < ONSET_DELTA
    )

