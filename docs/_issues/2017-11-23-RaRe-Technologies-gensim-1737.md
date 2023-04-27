---
tags: Hacktoberfest,bug,difficulty-easy,documentation
title: "Confusing \"TypeError: '<' not supported between \u2026 'str' and 'int'\" when doc-tag not present for `most_similar()`"
html_url: "https://github.com/RaRe-Technologies/gensim/issues/1737"
user: souveekbose
repo: RaRe-Technologies/gensim
---

I am facing an issue while using the model.docvecs.most_similar() function.
gensim: 2.3.0
Python 3.6.0
Error message: '<' not supported between instances of 'str' and 'int'

My code follows:
```python
def vectorize_doc2vec():
    sentence1 = 'Dogo is a dog'
    sentence2 = 'dog is a pet'
    sentence3 = 'pets are cool'
    sentence={sentence1:'j1', sentence2:'j2', sentence3:'j3'}
    
    sentences = LabeledLineSentence(sentence)
    
    model = Doc2Vec(min_count=1, window=10, size=100, sample=1e-4, negative=5, workers=8)
    model.build_vocab(sentences.to_array())
    
    model.train(sentences.sentences_perm(), total_examples=model.corpus_count, epochs=10)
    
    print(model.docvecs.most_similar('dog', topn=1))
```

The class LabeledLineSentence is as follows:

```python
class LabeledLineSentence(object):
    def __init__(self, sources):
        self.sources = sources
        
        flipped = {}
        
        # make sure that keys are unique
        for key, value in sources.items():
            if value not in flipped:
                flipped[value] = [key]
            else:
                raise Exception('Non-unique prefix encountered')
    
    def __iter__(self):
        for description, id in self.sources.items():
            yield LabeledSentence(description, id)

    def to_array(self):
        self.sentences = []
        for description, id in self.sources.items():
            self.sentences.append(LabeledSentence(description, id))
        return self.sentences
    
    def sentences_perm(self):
        shuffle(self.sentences)
        return self.sentences
```

Error StackTrace:
```
INFO:gensim.models.doc2vec:collecting all words and their counts
WARNING:gensim.models.doc2vec:Each 'words' should be a list of words (usually unicode strings).First 'words' here is instead plain <class 'str'>.
INFO:gensim.models.doc2vec:PROGRESS: at example #0, processed 0 words (0/s), 0 word types, 0 tags
INFO:gensim.models.doc2vec:collected 14 word types and 4 unique tags from a corpus of 3 examples and 38 words
INFO:gensim.models.word2vec:Loading a fresh vocabulary
INFO:gensim.models.word2vec:min_count=1 retains 14 unique words (100% of original 14, drops 0)
INFO:gensim.models.word2vec:min_count=1 leaves 38 word corpus (100% of original 38, drops 0)
INFO:gensim.models.word2vec:deleting the raw counts dictionary of 14 items
INFO:gensim.models.word2vec:sample=0.0001 downsamples 14 most-common words
INFO:gensim.models.word2vec:downsampling leaves estimated 1 word corpus (3.7% of prior 38)
INFO:gensim.models.word2vec:estimated required memory for 14 words and 100 dimensions: 20600 bytes
INFO:gensim.models.word2vec:resetting layer weights
INFO:gensim.models.word2vec:training model with 8 workers on 14 vocabulary and 100 features, using sg=0 hs=0 sample=0.0001 negative=5 window=10
INFO:gensim.models.word2vec:worker thread finished; awaiting finish of 7 more threads
INFO:gensim.models.word2vec:worker thread finished; awaiting finish of 6 more threads
INFO:gensim.models.word2vec:worker thread finished; awaiting finish of 5 more threads
INFO:gensim.models.word2vec:worker thread finished; awaiting finish of 4 more threads
INFO:gensim.models.word2vec:worker thread finished; awaiting finish of 3 more threads
INFO:gensim.models.word2vec:worker thread finished; awaiting finish of 2 more threads
INFO:gensim.models.word2vec:worker thread finished; awaiting finish of 1 more threads
INFO:gensim.models.word2vec:worker thread finished; awaiting finish of 0 more threads
INFO:gensim.models.word2vec:training on 380 raw words (77 effective words) took 0.0s, 3374 effective words/s
WARNING:gensim.models.word2vec:under 10 jobs per worker: consider setting a smaller `batch_words' for smoother alpha decay
INFO:gensim.models.doc2vec:precomputing L2-norms of doc weight vectors
Traceback (most recent call last):

File "", line 17, in #
 vectorize_doc2vec()
File "", line 14, in vectorize_doc2vec
print(model.docvecs.most_similar('dog', topn=1))

File "C:\Users\humblebee\AppData\Local\Continuum\Anaconda3\lib\site-packages\gensim\models\doc2vec.py", line 461, in most_similar
elif doc in self.doctags or doc < self.count:

TypeError: '<' not supported between instances of 'str' and 'int' # #
```

#1586 