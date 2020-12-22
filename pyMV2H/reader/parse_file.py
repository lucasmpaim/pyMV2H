from pyMV2H.utils.pojos import NOTE, TATUM, KEY, HIERARCHY


def need_read(fn):
    def inner(*args, **kwargs):
        music_instance = args[0]
        music_instance.read_if_needed()
        return fn(*args, **kwargs)
    return inner


class Music:

    def __init__(self, file_name):
        self.__file_name__ = file_name
        self.__tatums__ = None
        self.__keys__ = None
        self.__notes__ = None
        self.__hierarchy__ = None
        self.__has_read__ = False

    def read_if_needed(self):
        if not self.__has_read__:
            self.read()

    def read(self):
        self.__tatums__ = list()
        self.__keys__ = list()
        self.__notes__ = list()
        self.__hierarchy__ = list()
        with open(self.__file_name__, 'r') as file:
            all_lines = file.readlines()
            for line in all_lines:
                self.parse_line(line)
        self.__has_read__ = True

    def parse_line(self, line):
        if line.startswith('Note'):
            self.__parse_note__(line)
            self.__notes__.sort(key=lambda a: a.on_val)
        if line.startswith('Key'):
            self.__parse_key__(line)
        if line.startswith('Hierarchy'):
            self.__parse_hierarchy__(line)
        if line.startswith('Tatum'):
            self.__parse_tatum__(line)

    def __parse_note__(self, line):
        # Note 47 46000 46000 46474 1
        args = [int(x) for x in line.split(' ')[1:]]
        self.__notes__.append(NOTE(*args))

    def __parse_tatum__(self, line):
        # Tatum 3750
        args = [int(x) for x in line.split(' ')[1:]]
        self.__tatums__.append(TATUM(*args))

    def __parse_key__(self, line):
        # Key 0 Maj 0
        args = line.split(' ')[1:]
        self.__keys__.append(
            KEY(int(args[0]), args[1].lower() == 'maj', int(args[2]))
        )

    def __parse_hierarchy__(self, line):
        # Hierarchy 3,2 1 a=0 0
        args = [int(x) for x in  line.replace(',', ' ').replace('a=', '').split(' ')[1:]]
        if len(args) == 3:
            # time is optional on original description, set it to zero by default
            args.append(0)
        self.__hierarchy__.append(HIERARCHY(*args))

    @need_read
    def get_notes_grouped_by_onset(self):
        notes = list()

        most_recent_list = list()
        most_recent_value_onset_time = self.__notes__[0].on
        most_recent_list.append(self.__notes__[0])
        notes.append(most_recent_list)

        for note in self.__notes__[1:]:
            if note.on == most_recent_value_onset_time:
                most_recent_list.append(note)
            else:
                notes.append(most_recent_list)
                most_recent_list = list()
                most_recent_value_onset_time = note.on
                most_recent_list.append(note)
        return notes
