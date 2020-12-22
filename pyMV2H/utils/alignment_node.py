# ALIGNMENT_NODE = namedtuple('ALIGNMENT_NODE', 'prev_list value')

class AlignmentNode:
    def __init__(self, prev_list, value):
        self.prev_list = prev_list
        self.value = value
        count = 0
        if prev_list is not None:
            for prev in prev_list:
                count += prev.count
        self.count = max(count, 1)

    def get_alignment(self, index):
        if self.prev_list is None:
            return list()
        if len(self.prev_list) == 0:
            return list()

        alignment = list()
        current_search_index = index
        for node in self.prev_list:
            if current_search_index < self.count:
                alignment = node.get_aligment(current_search_index)
                break
            else:
                current_search_index -= node.count
        alignment.append(self.value)
        return alignment
