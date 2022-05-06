from tokenizer import tokenize, build_vocab, assign_vocab_index

def bagOfWords(vocab_index, vocab, tokens):
    """
    This uses summation not or operator.
    ToDo: handler for tokens not found in vocab
    """
    bow = []
    for doc in tokens:
        doc_rep = [0]*len(vocab)
        for token in doc:
            doc_rep[vocab_index[token]] += 1
        bow.append(doc_rep)
    return bow

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
    print("Bag of words representation of corpus: ", bagOfWords(vocab_index, vocab, tokens))