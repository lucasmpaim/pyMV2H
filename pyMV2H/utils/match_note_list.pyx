from pyMV2H.utils.matches import note_match

cpdef dict match_note_list(p_notes: list, t_notes: list):
    cpdef dict match_notes = dict()
    cdef list t_notes_copy = list(t_notes)
    cdef list p_notes_copy = list(p_notes)

    cdef int t_index = 0
    while t_index < len(t_notes_copy):
        t_note = t_notes_copy[t_index]
        p_index = 0
        while p_index < len(p_notes_copy):
            p_note = p_notes_copy[p_index]
            if note_match(t_note, p_note):
                # Found a match
                match_notes[t_note] = p_note
                t_notes_copy.pop(t_index)
                p_notes_copy.pop(p_index)
                t_index -= 1
                break
            p_index += 1
        t_index += 1
    return match_notes
