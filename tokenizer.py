import re

def tokenize(corpus):
    """
    Intial version 0.1: split each document in the corpus and return fragments as list.
    0.2 : use of re module -- regex(regular expression) --- . \ + * ? [ ^ ] $ ( ) { } = !  | : -
    To Fix:
        special characters need to be tokenized as separate words.
    """
    token = [doc.split() for doc in corpus]
    # token = [list(filter("",re.split(' |\?|!|$', doc))) for doc in corpus]
    return token

def build_vocab(corpus_tokens):
    """
    return a list of unique tokens in tokenized corpus
    args:
        corpus_tokens: tokenized corpus
    """
    vocab = []
    for doc in corpus_tokens:
        for token in doc:
            if token not in vocab:
                vocab.append(token)

    return vocab

def assign_vocab_index(vocab):
    vocab_index = {}
    for i,token in enumerate(vocab):
        vocab_index[token] = i
    return vocab_index

if __name__ == "__main__":
    corpus = [
        'he is a king!',
        'she is a queen and she is beautiful',
        'is he a man?',
        'she is a woman',
        'warsaw is poland capital',
        'berlin is germany capital',
        'paris is france capital',
        'he paid 100$'
    ]
    tokens = tokenize(corpus)
    vocab = build_vocab(tokens)
    vocab_index = assign_vocab_index(vocab)
