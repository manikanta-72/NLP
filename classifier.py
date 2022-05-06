from feature_generator import bagOfWords
from tokenizer import tokenize, build_vocab, assign_vocab_index
import numpy as np

def naiveBayesClassifier(X_train, y_train, X_test, C):
    """
    Naive Bayes Classifier for text classification. Naive bayes 
    args:
        X_train: corpus consisting of documents
        y_train: labels to the documents {0,1,2,..., C-1} - a total of C classes
        X_test: documents that need to be labeled
        C: number of classes
    """
    # train data processing
    X_train_tokens = tokenize(X_train)

    # NB_dict is dictionary used to maintain counts
    # NB_dict["class_id"]["word"] = count
    NB_dict = dict()
    for i in range(C):
        NB_dict[i] = dict()
    
    for i, doc in enumerate(X_train_tokens):
        for w in doc:
            if w in NB_dict[y_train[i]]:
                NB_dict[y_train[i]][w] += 1.0
            else:
                NB_dict[y_train[i]][w] = 1.0

    class_word_count = []
    class_prob = []
    for i in range(C):
        total_words = 0
        num_c_instances = np.sum(np.array(y_train) == i)
        print(np.array(y_train) == i)
        class_prob.append(num_c_instances / len(y_train))
        for w in NB_dict[i]:
            total_words += NB_dict[i][w]
        class_word_count.append(total_words)

    # test data processing
    X_test_tokens = tokenize(X_test)
    # X_train_bow = bagOfWords(vocab_index, vocab, X_test_tokens)
    
    prob_mat = np.zeros((len(X_test), C))

    for i, doc_tokens in enumerate(X_test_tokens):
        prob_w_c = 1.0
        for c in range(C):
            prob_w_c = 1.0
            for w in doc_tokens:
                if w in NB_dict[c]:
                    prob_w_c *= (NB_dict[c][w] / class_word_count[c])
                else:
                    # currently neglate all the unknown words in training data
                    continue
            prob_mat[i][c] = class_prob[c] * prob_w_c
    
    # print(NB_dict)
    # print(class_word_count)

    # get labels for probability matrix argmax in each instance
    y_test = np.argmax(prob_mat, axis=1)

    return y_test

if __name__ == "__main__":
    corpus = [
        'I feel great today',
        'It is not a great movie',
        'His love made me feel good',
        'The food in this restraurant is bad'
    ]

    corpus_label = [0,1,0,1]

    test_corpus = ["After eating food I feel great"]
    print(naiveBayesClassifier(corpus, corpus_label, test_corpus, 2))
