import packages # for the Natural Language Toolkit (NLTK)
from intelligence import data

# Tokenize a string using word parsing as well as a linear perceptron-based
# tagger to identify parts of speech. This perceptron is a form of deep neural
# network that uses a machine learning model to accurately predict the PoS based
# on its previous training, which is done on the spot.

class Tokenization:
    def __init__(self, *args):
        if len(args) == 1:
            tok = _setTokenize(args[0])
            self.sentence = tok[0]
            self.word = tok[1]
            self.pos = tok[2]
            self.partOfSpeech = tok[2]
        elif len(args) == 3:
            self.sentence = args[0]
            self.word = args[1]
            self.pos = args[2]
            self.partOfSpeech = args[2]
        else:
            raise SyntaxError("Invalid number of arguments for a Tokenization.")

def _setTokenize(string):
    # Get a sentence and word tokenization, as well as part of speech analysis
    # by the perceptron

    sentenceTokenization = packages.nltk.sent_tokenize(string)
    wordTokenization = packages.nltk.word_tokenize(string)
    partOfSpeechTagging = packages.nltk.pos_tag(wordTokenization)

    # Return all three for later use

    return (sentenceTokenization, wordTokenization, partOfSpeechTagging)

def tokenize(string):
    # Get a sentence and word tokenization, as well as part of speech analysis
    # by the perceptron

    sentenceTokenization = packages.nltk.sent_tokenize(string)
    wordTokenization = packages.nltk.word_tokenize(string)
    partOfSpeechTagging = packages.nltk.pos_tag(wordTokenization)

    # Return all three for later use

    return Tokenization(sentenceTokenization,
        wordTokenization,
        partOfSpeechTagging
    )

def getNouns(arg):
    if isinstance(arg, Tokenization):
        tok = arg
    else:
        tok = tokenize(arg)

    detectedNouns = list([x for x in tok.pos if x[1] in ["NN", "NNS", "NNP"]])
    selected = []
    for noun in detectedNouns:
        print("checking noun - " + str(noun[0]))
        for nounSynset in packages.nltk.corpus.wordnet.synsets(noun[0]):
            b = False
            for noi in data.nounsOfInterest:
                noiSynset = packages.nltk.corpus.wordnet.synsets(noi[0])[0]
                print("  noi: " + str(noi))
                print("  ps: " + str(nounSynset.path_similarity(noiSynset)))
                if nounSynset.path_similarity(noiSynset) >= 0.5:
                    selected.append(noun)
                    b = True
                    break
            if b:
                break

    for noun in detectedNouns:
        if noun[0] in data.nounsOfInterest:
            selected.append(noun)

    return selected

# The Item object represents an item (like a bottle, box, paper, food, etc.) or
# a set thereof that is important to the Action.

class Item:
    def __init__(self, name, quantity, **properties):
        self.name = name
        self.quantity = quantity
        self.properties = properties
        self.keys = properties.keys()

# The Action object represents the thing that is being analyzed by the AI.

class Action:
    def __init__(self, *items):
        for item in items:
            if isinstance(item, Item):
                raise TypeError("Invalid type for argument of Action - must be \
                an Item.")
                self.items = items
