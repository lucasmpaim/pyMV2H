from fastdtw import fastdtw

from pyMV2H.reader.parse_file import Music


def align_files(provided_file: Music, transcription_file: Music):
    provided_file.read_if_needed()
    transcription_file.read_if_needed()

