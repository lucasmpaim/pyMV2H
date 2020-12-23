from pyMV2H.metrics.multi_pitch import multi_pitch_accuracy
from pyMV2H.metrics.voice import voice_score
from pyMV2H.reader.parse_file import Music
from pyMV2H.utils.pojos import MV2H_WEIGHTS


def mv2h(
        p_music: Music,
        t_music: Music,
        weights: MV2H_WEIGHTS = MV2H_WEIGHTS()
):
    p_music.read_if_needed()
    t_music.read_if_needed()

    weight_sum = (
            weights.multi_pitch +
            weights.voice +
            weights.harmonic +
            weights.metrical +
            weights.value_detection
    )
    multi_pitch = multi_pitch_accuracy(p_music.__notes__, t_music.__notes__) * weights.multi_pitch
    voice = voice_score(p_music, t_music) * weights.voice

    return (
            (
                    multi_pitch +
                    voice +
                    1 +
                    1 +
                    1
            ) / weight_sum
    )

    # return (
    #     multi_pitch_accuracy(p_music.__notes__, t_music.__notes__),
    #     voice_score(p_music, t_music),
    #     0,
    #     0,
    #     0
    # )
