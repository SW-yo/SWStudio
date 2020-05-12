tp = 70
fp = 4930
fn = 13930
tn = 891070

def accuracy(tp, fp, fn, tn):
    correct = tp + tn
    total = tp + fp + fn + tn
    return correct / total

print(accuracy(tp, fp, fn, tn))

def precision(tp, fp, fn, tn):
    return tp / (tp + fp)

print(precision(tp, fp, fn, tn))

def recall(tp, fp, fn, tn):
    return tp / (tp + fn)

print(recall(tp, fp, fn, tn))

def f1_score(tp, fp, fn, tn):
    p = precision(tp, fp, fn, tn)
    r = recall(tp, fp, fn, tn)
    return 2 * p * r / (p + r)

print(f1_score(tp, fp, fn, tn))
