from collections import Counter, defaultdict
from machine_learning import split_data
import math, random, re, glob

def tokenize(message):
    message = message.lower()                       #小文字に変換する
    all_words = re.findall("[a-z0-9']+",message)    #単語を識別する
    return set(all_words)                           #重複を取り除く

def count_words(trainingu_set):
    #学習データ（training_set)は、メッセージと、
    #スパムか否かを表すis_spamのペアである
    counts = defaultdict(lambda: [0, 0])
    for message, is_spam in trainingu_set:
        for  word in tokenize(message):
            counts[word][0 if is_spam else 1] += 1
    return counts

def word_prpbabiliies(counts, total_spam, total_non_spam, k=0.5):
    #word_countを、単語、p(単語|スパム) and p(単語|~スパム)の
    #三つ組に変換する
    return [(w,
            (spam + k) / (total_spam + 2 * k),
            (non_spam + k) / (total_non_spam + 2 * k))
            for w, (spam, non_spam) in counts.items()]

def spam_probability(word_probs, message):
    message_words = tokenize(message)
    log_prob_if_spam = log_prob_if_not_spam = 0.0

    #語彙リストの単語を順に適用する
    for word, prob_if_spam, prob_if_not_spam in word_probs:

        #その単語がメッセージ中に現れた場合、
        #その確率の対数を加算する
        if word in message_words:
            log_prob_if_spam += math.log(prob_if_spam)
            log_prob_if_not_spam += math.log(prob_if_not_spam)

        #メッセージに現れなかった場合には、
        #メッセージがその単語を含まない場合の確率の対数、つまり
        #log(1 - 含む場合の確率)を加算する
        else:
            log_prob_if_spam += math.log(1.0 - prob_if_spam)
            log_prob_if_not_spam += math.log(1.0 - prob_if_not_spam)

    prob_if_spam = math.exp(log_prob_if_spam)
    prob_if_not_spam = math.exp(log_prob_if_not_spam)
    return prob_if_spam / (prob_if_spam + prob_if_not_spam)



class NaiveBayesClassifier:
    def __init__(self, k=0.5):
        self.k = k
        self.word_probs = []

    def train(self,training_set):

        #スパムメッセージとスパムではないメッセージの数を数える
        num_spams = len([is_spam
                        for message, is_spam in training_set
                        if is_spam])
        num_non_spams = len(training_set) - num_spams

        #学習データを使って学習する
        word_counts = count_words(training_set)
        self.word_probs = word_prpbabiliies(word_counts,
                                            num_spams,
                                            num_non_spams,
                                            self.k)

    def classify(self, message):
        return spam_probability(self.word_probs, message)

#ファイルを展開した場所に従ってpathを設定する
#元データ：https://spamassassin.apache.org/old/publiccorpus/
#path = r"/Users/saitouyouichirou/python/spam/*/*"
path = r"../spam/*/*"

data = []

#glob.globはワイルドカードに一致するファイル名を返す
for fn in glob.glob(path):
    is_spam = "ham" not in fn

    with open(fn, 'r', encoding="utf-8", errors="ignore") as file:
        for line in file:
            if line.startswith("Subject:"):
                #行頭の"Subject: "を取り除き、残りの部分を保存する
                subject = re.sub(r"^Subject: ", "", line).strip()
                data.append((subject, is_spam))

random.seed(0)
train_data, test_data = split_data(data, 0.75)

classifier = NaiveBayesClassifier()
classifier.train(train_data)

#三つ組（Subject，スパムか否か(is_spam)、予測したスパムである確率）を作る
classified = [(subject, is_spam, classifier.classify(subject))
            for subject, is_spam, in test_data]

#予測確率 >0.5であればスパムであると判断する
#（実際のスパム、予測結果）のペアを作る
counts = Counter((is_spam, spam_probability > 0.5)
                for _, is_spam, spam_probability in classified)

#print(counts)


#spam_probabilityを照準にソートする
classified.sort(key=lambda row: row[2])

#スパムでないメッセージ中、最も高い確率でスパムと判別されたものを取り出す
spammiest_hams = list(filter(lambda row: not row[1], classified))[-5:]

#スパムメッセージの中で、最も低い確率でスパムではないと判別されたものを取り出す
hammiest_spams = list(filter(lambda row: row[1],classified))[5:]

#print(spammiest_hams)
#print(hammiest_spams)

def p_spam_given_word(word_prob):
    #ベイズの定理を用いて、p(スパムである|その単語がメッセージに含まれる)
    #を計算する

    #word_probは、関数word_probabilitiesの返した三つ組の中の1つ
    word, prob_if_spam, prob_if_not_spam = word_prob
    return prob_if_spam / (prob_if_spam + prob_if_not_spam)

words = sorted(classifier.word_probs, key=p_spam_given_word)

spammiest_words = words[-5:]
hammiest_words = words[:5]

print(spammiest_words)
print(hammiest_words)
