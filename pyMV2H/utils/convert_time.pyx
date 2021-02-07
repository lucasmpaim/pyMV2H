cimport cython
from cpython cimport array
import array

@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
cpdef int convert_time(int time, object p_music, object t_music, list py_alignment, dict alignment_times):
    cdef array.array alignment = array.array('i', py_alignment)


    alignment_time = alignment_times.get(time, None)
    if alignment_time is not None:
        return alignment_time

    cdef float t_index = -1
    cdef list t_notes = t_music.get_notes_grouped_by_onset()

    cdef int index

    # Find the correct transcription anchor index to start with
    for index, t_note in enumerate(t_notes):
        if t_note[0].on == time:
            # Time matches an anchor exactly
            t_index = index
            break

        if t_note[0].on > time:
            # This anchor is past the time
            t_index = index - 0.5
            break

    cdef list p_notes = p_music.get_notes_grouped_by_onset()
    cdef int p_previous_anchor = -1
    cdef int p_previous_previous_anchor = -1
    cdef int p_next_anchor = len(p_notes)
    cdef int p_next_next_anchor = len(p_notes)

    cdef int alignment_length = len(alignment)
    for index in range(alignment_length):
        if alignment.data.as_ints[index] != -1:
            if alignment.data.as_ints[index] == t_index:
                # This is the correct time, exactly on the index
                return p_notes[index][0].on
            elif alignment.data.as_ints[index] < t_index:
                # The time is past this anchor
                p_previous_previous_anchor = p_previous_anchor
                p_previous_anchor = index
            else:
                #  We are past the time
                if p_next_anchor == len(p_notes):
                    # This is the first anchor for which we are past the time
                    p_next_anchor = index
                else:
                    # This is the 2nd anchor for which we are past the time
                    p_next_next_anchor = index

    if p_previous_anchor == -1 and p_next_anchor == len(p_notes):
        # Nothing was aligned
        alignment_times[time] = time
        return time

    if p_previous_anchor == -1:
        if p_next_anchor != len(p_notes):
            alignment_time = _convert_time(
                time,
                p_next_anchor,
                p_next_next_anchor,
                p_notes,
                t_notes,
                alignment
            )
        else:
            # Only 1 anchor. Just linear shift.
            alignment_time = (
                    time -
                    t_notes[alignment.data.as_ints[p_next_anchor]][0].on +
                    p_notes[alignment.data.as_ints[p_next_anchor]][0].on
            )
    elif p_next_anchor == len(p_notes):
        # Time is after the last anchor. Use the previous rate.
        if p_next_anchor == len(p_notes):
            alignment_time = _convert_time(
                time,
                p_previous_previous_anchor,
                p_previous_anchor,
                p_notes,
                t_notes,
                alignment
            )
        else:
            # Only 1 anchor. Just linear shift.
            alignment_time = (
                    time -
                    t_notes[alignment[p_previous_anchor]][0].on +
                    p_notes[alignment[p_previous_anchor]][0].on
            )
    else:
        # Time is between anchor points
        alignment_time = _convert_time(
                time,
                p_previous_anchor,
                p_next_anchor,
                p_notes,
                t_notes,
                alignment
        )

    alignment_times[time] = alignment_time
    return int(alignment_time)


cdef int _convert_time(int time, int previous_anchor, int next_anchor, list p_notes, list t_notes, array.array alignment):
    cdef int p_previous_time = p_notes[previous_anchor][0].on
    cdef int p_next_time = p_notes[next_anchor][0].on

    cdef int t_previous_time = t_notes[alignment.data.as_ints[previous_anchor]][0].on
    cdef int t_next_time = t_notes[alignment.data.as_ints[next_anchor]][0].on

    cdef int rate = ((p_next_time - p_previous_time) / (t_next_time - t_previous_time))
    return round(rate * (time - t_previous_time) + p_previous_time)

