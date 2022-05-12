#!pip install flair
import os
import torch 
import numpy as np
import torch.nn.functional as F
import sklearn
from sklearn.cluster import KMeans

from flair.embeddings import TransformerWordEmbeddings
from flair.data import Sentence

'''
Set Params Here
'''
infilename = 'News/news_iter1_self'
n_clusters = 6
outputdir = './output/'
outfilename = outputdir + infilename + '-out-'
data = open(infilename, 'r').readlines()

# init embedding
embedding_model = 'bert-base-uncased'
embedding_file = "./embeddings/" + embedding_model
if os.path.exists(embedding_file):
      print("Using embedding file : %s"%embedding_file)
      embedding = torch.load('./embeddings/bert-base-uncased')
else:
      print("Downloading %s model"%embedding_model)
      embedding = TransformerWordEmbeddings(embedding_model)
      torch.save(embedding, embedding_file)

print("Embeddings loaded")

# create a sentence
# sentence = Sentence('The grass is green .')

# embed words in sentence
# embedding.embed(sentence)

# print(sentence[0].embedding.size(), sentence[0].embedding)

sentences = [] 
for line in data:
  sentence = Sentence(line)
  embedding.embed(sentence)
  sentences.append(sentence[0].embedding)
# print(sentences[0].size(), len(sentences))

t = torch.stack(sentences)
# F.cosine_similarity(t[0], t[1], dim=0, eps=1e-08)

'''
Kmeans Clustering
'''
# n_clusters = 2
kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(t) # verbose = 1
# print(kmeans.labels_)
#print(kmeans.cluster_centers_)

final_sets = {}
for i in range(0, n_clusters):
  final_sets[i] = []
for idx in range(0, len(data)):
  final_sets[kmeans.labels_[idx]].append(data[idx])


def show_sets(final_sets):
  pairs = [v for (k,v) in final_sets.items()]
  for i in range(0, len(pairs)):
    # print("Set {} utterances:".format(i))
    utts = pairs[i]
    with open(outfilename+str(i), 'w') as f:
      for line in utts:
            f.write(line)

show_sets(final_sets)      
