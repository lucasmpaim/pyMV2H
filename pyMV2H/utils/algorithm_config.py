"""
The penalty assigned for insertion and deletion errors when performing alignment.
The default value of 1 leads to a reasonably fast, but not exhaustive
search through alignments.
"""
NON_ALIGNMENT_PENALTY = 1.

"""
The difference in onset time between two {@link mv2h.objects.Note}s for them to be
counted as a match.
Measured in milliseconds.
"""
ONSET_DELTA = 50
