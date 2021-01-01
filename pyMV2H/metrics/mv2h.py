from pyMV2H.metrics.harmony import harmony_score
from pyMV2H.metrics.meter import meter_score
from pyMV2H.metrics.multi_pitch import multi_pitch_accuracy
from pyMV2H.metrics.note_value import note_value_score
from pyMV2H.metrics.voice import voice_score
from pyMV2H.utils.music import Music
from pyMV2H.utils.mv2h import MV2H
from pyMV2H.utils.pojos import MV2H_WEIGHTS


def mv2h(
        p_music: Music,
        t_music: Music,
        weights: MV2H_WEIGHTS = MV2H_WEIGHTS()
):
    p_music.read_if_needed()
    t_music.read_if_needed()

    multi_pitch = multi_pitch_accuracy(p_music.__notes__, t_music.__notes__) * weights.multi_pitch
    voice = voice_score(p_music, t_music) * weights.voice
    harmony = harmony_score(p_music, t_music) * weights.harmonic
    meter = meter_score(p_music, t_music) * weights.metrical
    note_value = note_value_score(p_music, t_music) * weights.note_value

    return MV2H(
        multi_pitch, voice, harmony, meter, note_value, weights
    )
