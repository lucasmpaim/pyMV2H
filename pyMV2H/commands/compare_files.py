from .base import Base
from ..metrics import multi_pitch
from ..metrics.harmony import harmony_score
from ..metrics.meter import meter_score
from ..metrics.mv2h import mv2h
from ..metrics.note_value import note_value_score
from ..metrics.voice import voice_score


class CompareFilesCommand(Base):

    def run(self):
        from ..reader.parse_file import Music
        from ..utils.align_files import align_files

        reference_file = Music(self.options['<reference_file>'])
        transcription_file = Music(self.options['<transcription_file>'])
        # align_files(reference_file, transcription_file)
        reference_file.read_if_needed()
        transcription_file.read_if_needed()
        print(
            f'Multi-Pitch: {multi_pitch.multi_pitch_accuracy(reference_file.__notes__, transcription_file.__notes__)}'
        )
        print(f'Voice: {voice_score(reference_file, transcription_file)}')
        print(f'Meter: {meter_score(reference_file, transcription_file)}')
        print(f'Harmony: {harmony_score(reference_file, transcription_file)}')
        print(f'Value: {note_value_score(reference_file, transcription_file)}')
        print(f'MV2H: {mv2h(reference_file, transcription_file)}')
