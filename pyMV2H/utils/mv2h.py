from pyMV2H.utils.pojos import MV2H_WEIGHTS


class MV2H:

    def __init__(self, multi_pitch, voice, harmony, meter, note_value, weights=MV2H_WEIGHTS()):
        self.multi_pitch = multi_pitch
        self.voice = voice
        self.harmony = harmony
        self.meter = meter
        self.note_value = note_value
        self.weights = weights

    def __sum_heights__(self) -> float:
        return (
                self.weights.multi_pitch +
                self.weights.voice +
                self.weights.harmonic +
                self.weights.metrical +
                self.weights.note_value
        )

    def update_heights(self, heights: MV2H_WEIGHTS):
        self.weights = heights

    def __updated__multi_pitch__(self) -> float:
        return self.multi_pitch * self.weights.multi_pitch

    def __updated__voice__(self) -> float:
        return self.voice * self.weights.voice

    def __updated__harmony__(self) -> float:
        return self.harmony * self.weights.harmonic

    def __updated_meter__(self) -> float:
        return self.meter * self.weights.metrical

    def __updated_note_value__(self) -> float:
        return self.note_value * self.weights.note_value

    @property
    def mv2h(self) -> float:
        return (
            self.__updated_meter__() +
            self.__updated__voice__() +
            self.__updated__harmony__() +
            self.__updated_note_value__() +
            self.__updated__multi_pitch__()
        ) / self.__sum_heights__()

    def __repr__(self):
        return f'''
Multi-pitch:    {self.__updated__multi_pitch__()}
Voice:          {self.__updated__voice__()}
Meter:          {self.__updated_meter__()}
Value:          {self.__updated_note_value__()}
Harmony:        {self.__updated__harmony__()}
MV2H:           {self.mv2h}
        '''
