from collections import namedtuple

NOTE = namedtuple('NOTE', 'pitch on on_val off_val voice')

TATUM = namedtuple('TATUM', 'time')

HIERARCHY = namedtuple('HIERARCHY', 'bpb sbpb tpsb al time')

KEY = namedtuple('KEY', 'tonic is_major time')

CHORD = namedtuple('CHORD', 'time chord')


MIDI_TIME_SIGNATURE = namedtuple('TIME_SIGNATURE', 'numerator denominator')
