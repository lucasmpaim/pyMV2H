from math import isnan


def f1_score(true_positives, false_positives, false_negatives):
    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)
    f1 = 2.0 * recall * precision / (recall + precision)
    return 0.0 if isnan(f1) else f1
