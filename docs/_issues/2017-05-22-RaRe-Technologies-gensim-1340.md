---
tags: Hacktoberfest,bug,difficulty-easy
title: " 'ConcatenatedDoc2Vec' object has no attribute 'corpus_count'"
html_url: "https://github.com/RaRe-Technologies/gensim/issues/1340"
user: jasminezz
repo: RaRe-Technologies/gensim
---


#### Description
study "doc2vec-IMDB.ipynb" step by step ,but when train the model, got the following error:

100000 docs: 25000 train-sentiment, 25000 test-sentiment
Doc2Vec(dm/c,d100,n5,w5,mc2,s0.001,t8)
Doc2Vec(dbow,d100,n5,mc2,s0.001,t8)
Doc2Vec(dm/m,d100,n5,w10,mc2,s0.001,t8)
START 2017-05-22 17:11:40.993000
*0.248200 : 1 passes : Doc2Vec(dm/c,d100,n5,w5,mc2,s0.001,t8) 257.3s 1.1s
*0.240400 : 1 passes : Doc2Vec(dm/c,d100,n5,w5,mc2,s0.001,t8)_inferred 257.3s 5.7s
*0.113640 : 1 passes : Doc2Vec(dbow,d100,n5,mc2,s0.001,t8) 54.2s 0.8s
*0.101200 : 1 passes : Doc2Vec(dbow,d100,n5,mc2,s0.001,t8)_inferred 54.2s 2.6s
*0.176480 : 1 passes : Doc2Vec(dm/m,d100,n5,w10,mc2,s0.001,t8) 75.1s 0.8s
Traceback (most recent call last):
  File "D:/PycharmProjects/NLP_demo/doc2vec_train_test.py", line 142, in <module>
    train(doc_list, models_by_name, train_docs, test_docs)
  File "D:/PycharmProjects/NLP_demo/doc2vec_train_test.py", line 105, in train
    train_model.train(doc_list, total_examples=train_model.corpus_count, epochs=train_model.iter)
AttributeError: 'ConcatenatedDoc2Vec' object has no attribute 'corpus_count'
*0.194800 : 1 passes : Doc2Vec(dm/m,d100,n5,w10,mc2,s0.001,t8)_inferred 75.1s 3.3s

Environment:
python3
windows 7
