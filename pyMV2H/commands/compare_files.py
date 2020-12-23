from .base import Base
from ..metrics.mv2h import mv2h


class CompareFilesCommand(Base):

    def run(self):
        from ..reader.parse_file import Music

        reference_file = Music(self.options['<reference_file>'])
        transcription_file = Music(self.options['<transcription_file>'])
        # align_files(reference_file, transcription_file)
        reference_file.read_if_needed()
        transcription_file.read_if_needed()
        print(mv2h(reference_file, transcription_file))
