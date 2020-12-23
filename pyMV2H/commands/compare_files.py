from .base import Base
from ..metrics import multi_pitch
from ..metrics.mv2h import mv2h
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
        print(f'MV2H: {mv2h(reference_file, transcription_file)}')
