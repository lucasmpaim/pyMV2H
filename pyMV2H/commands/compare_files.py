from .base import Base


class CompareFilesCommand(Base):

    def run(self):
        from ..reader.parse_file import Music
        from ..utils.align_files import align_files

        reference_file = Music(self.options['<reference_file>'])
        transcription_file = Music(self.options['<transcription_file>'])
        align_files(reference_file, transcription_file)
