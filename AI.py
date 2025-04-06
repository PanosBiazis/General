# Artificial Intelligence(AI) is a way to make machines think and behave intelligently.

# AI is used in many fields such as Healthcare, Finance, Banking, Robotics, Transport, Internet, and many more.
# AI has three stages:

# 1. Narrow AI
# 2. General AI 
# 3. Super AI

# Applications of AI:

# 1. Computer Vision
# 2. Natural Language Processing
# 3. Speech Recognition
# 4. Speech Synthesis
# 5. Robotics
# 6. Games
# 7. Internet of Things
# 8. Internet of People

# Fraud detection is a problem under AI domain whereas rule-based methods and machine  learning are solution techniques in the AI domain.

import sklearn
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
label_names=data['target_names']
labels=data['target']
feature_names=data['feature_names']
features=data['data']
print(label_names)#class names
print(labels[0])# binary value 0
#finding the radius
print(feature_names[0])
# mean radius
print(features[0])
# Naive Bayes is a technique used to build classifiers using Bayes theorem.
# Naive Bayes is a family of probabilistic machine learning models based on Bayes' theorem
# There are three types of Naive Bayes models using scikit learn package:

# 1. Gaussian Naive Bayes
# 2. Multinomial Naive Bayes
# 3. Bernoulli Naive Bayes

# we are going to use the Gaussian Naive Bayes Model.
from sklearn.model_selection import train_test_split

# Splitting the data
train,test,train_labels,test_labels=train_test_split(features,labels,test_size=0.40,random_state=42)

from sklearn.naive_bayes import GaussianNB

gnb=GaussianNB()
model=gnb.fit(train,train_labels)# fitting the data 

# It's time for prediction
preds=gnb.predict(test)
print(preds)

#last stage Accuracy
from sklearn.metrics import accuracy_score
print(accuracy_score(test_labels,preds))#95.17% accurate

# Regression is the process of estimating the relationship between input and output variables.
#Input variables are called independent variables known as predictors and 
# output variables are called dependent variables, also known as criterion variables.

# Buiding Regressors
import pickle
import numpy as np
from sklearn import linear_model
import sklearn.metrics as sm
import matplotlib.pyplot as plt
import os

# input='F:\panag\Documents\ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ\Python tries\ex1data1.txt'
# input = r"/run/media/panos/SAMSUNGT7/panag/Documents/ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ/Python tries/ex1data1.txt"
# input = "./Python tries/ex1data1.txt"
# Get the current working directory
current_directory = os.getcwd()

# Construct the path to the file dynamically
input = os.path.join(current_directory,"Documents","ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ" ,"Python tries", "ex1data1.txt")

# load the file
data = np.loadtxt(input, delimiter=',')

# load the file
# data=np.loadtxt(input,delimiter=',')
X,y=data[:,:-1],data[:,-1]

# Split it into training and testing
num_training=int(0.8*len(X))
num_test=len(X)- num_training
#Training data
X_train,y_train=X[:num_training],y[:num_training]
#Test data
X_test,y_test=X[num_training:],y[num_training:]

#linear regressor object and train it using the training data
regressor=linear_model.LinearRegression()
regressor.fit(X_train,y_train)

#the prediction
y_test_pred=regressor.predict(X_test)

# plot the output
plt.scatter(X_test,y_test,color='green')
plt.plot(X_test,y_test_pred,color='black',linewidth=4)
plt.xticks(())
plt.yticks(())
plt.show()

# Unsupervised learning refers to the process of building machine learning models without using labeled training data
# Unsupervised learning algorithms attempt to build learning models that can find subgroups within the given dataset using some similarity metric.

# Clustering is a technique that groups together objects that are close to each other in the feature space.
# types of clustering:

# 1 Based on Goals
# 1.1. Monothetic
# 1.2. Polythetic

# 2 Based on Overlaps
# 2.1. Hard Clustering
# 2.2. Soft Clustering

#Implementing K-means clustering algorithm
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans

# Two-dimensional data
from sklearn.datasets._samples_generator import make_blobs

X, y_true = make_blobs(n_samples=500, centers=4,cluster_std=0.40,random_state=0)
plt.scatter(X[:,0],X[:,1],s=50)
plt.show()
# Initializing kmeans
kmeans=KMeans(n_clusters=4)

# Training the data
kmeans.fit(X)
y_kmeans=kmeans.predict(X)
plt.scatter(X[:,0],X[:,1],c=y_kmeans,s=50,cmap='viridis')
centers=kmeans.cluster_centers_
plt.scatter(centers[:,0],centers[:,1],c='black',s=200,alpha=0.5)
plt.show()

# Mean shift is a powerful algorithm used unsupervised learning. 
# It is a non-parametric algorithm used frequently for clustering.
# It is a centroid-based algorithm, which means that it updates the location of centroids iteratively based 
# on the density of the data points in each cluster.
# It is also called hierarchical clustering or mean shift cluster analysis.

from sklearn.cluster import MeanShift
from matplotlib import style
style.use("ggplot")

# Two-dimensional dataset
from sklearn.datasets._samples_generator import make_blobs

# Visualizing
centers=[[2,2],[4,5],[3,10]]
X,_=make_blobs(n_samples=500,centers=centers,cluster_std=1)
plt.scatter(X[:,0],X[:,1])
plt.show()

# Natural Language Processing is casually dubbed NLP.
# It is a subfield of artificial intelligence and linguistics.
# NLP is used in a wide variety of applications, from text classification to speech recognition.
# It is used to analyze and understand human language.
# NLP is used in many applications such as sentiment analysis, named entity recognition, topic modeling and machine translation.
# While Learning NLP,WE come across two main Components of NLP:

# 1. Natural Language Understanding (NLU)
# Natural Language Understanding revolves around machine reading comprehension.This is an AI-hard problem.
# An NLU system needs the following components:

# 1. Lexical Analysis
# 2. Syntactic Analysis
# 3. Parsing
# 4. Entity Resolution
# 5. Named Entity Recognition
# 6. Sentiment Analysis
# 7. Topic Modeling
# 8. Question Answering
# 9. Machine Translation
# 10. Grammar rules

# 2. Natural Language Generation (NLG)
# It is the process of producing meaninful phrases and sentences in the form of natural language from a representation system like a knowledge base or a logical form.
# NLG is used in applications like chatbots, virtual assistants, and language translation software.
# NLG involves the following components:

# 1. Text planning - This includes retrieving the relevant content from the knowledge base.
# 2. Sentence planning - This involves organizing the content into sentences.
# 3. Translation planning - This involves translating the sentences into the target language.
# 4. Grammar checking - This involves checking the grammatical correctness of the sentences.
# 5. Text Realization - This is mapping sentence pan into sentence structure.

# Open-Source Libraries
# 1. NLTK (Natural Language Toolkit)
# 2. SpaCy
# 3. Stanford CoreNLP
# 4. Tensorflow
# 5. PyTorch
# 6. scikit-learn
# 7. NLTK
# 8. Apache OpenNLP
# 9. Gate NLP Library

# NLP Terminology
# 1. NLP - Natural Language Processing
# 2. NLU - Natural Language Understanding
# 3. NLG - Natural Language Generation
# 4. Tokenization - The process of breaking down text into individual words or tokens.
# 5. Stemming - The process of reducing inflected (or sometimes derived) words to their word stem, base or root form.
# 6. Lemmatization - The process of grouping together the different inflected forms of a word so they can be analysed as a single item.
# 7. Named Entity Recognition - The process of identifying and classifying named entities in text.
# 8. Sentiment Analysis - The process of determining the sentiment of a text, whether it is positive, negative, or neutral.
# 9. Topic Modeling - The process of discovering the main topics in a text.
# 10. Question Answering - The process of answering questions based on the context of a text.
# 11. Morpheme - It is a primitive unit of meaning in a language.
# 12. Discourse - Understanding how a sentence can affect the next.
# 13. Pragmatics - Understanding how language is used in context to convey meaning.
# 14. Semantics - Understanding the meaning of words and phrases.
# 15. Word Sense Disambiguation - The process of identifying the correct sense of a word based on its context.
# 16. Word Sense Merging - The process of merging words with the same meaning.
# 17. Morphology - Study of constructing words from primitive meaningful units.
# 18. Phonology - It is the study of organizing sound systematically.
# 19. Speech Processing - It is the study of processing speech.
# 20. Speech Synthesis - It is the study of synthesizing speech.
# 21. Syntax - Arranging words to form a sentence determining the structural role of words in sentences and phrases.
# 22. Word Sense Disambiguation - The process of identifying the correct sense of a word based on its context.
# 23. Word Sense Merging - The process of merging words with the same meaning.
# 24. World Knowledge - It includes the general knowledge about the world.
# 25. Language Model - It is a probability distribution over a sequence of words.


# NLTK
# NLTK is a popular open-source NLP library used for tasks such as tokenization, stemming
import nltk
nltk.download()
# Tokenization - Spliting part into smaller parts, paragraphs to sentences,sentences to words.
from nltk.tokenize import word_tokenize
text="One day or day one! It's your choice."
print(word_tokenize(text))
# Sent_tokenize package
from nltk.tokenize import sent_tokenize
text="One day or day one! It's your choice."
print(sent_tokenize(text))
# Stemming is the process of cutting off the prefixes and 
# subffixes of the word and taking into account only the root word.
from nltk.stem.porter import PorterStemmer
# Lemmatization is similar to stemming however 
# it is more effective because it takes into consideration the morphological analysis of the word.
# We can also extract the base form of words byy lemmatization.
# This kind of base form of any word is called lemma.
# Lemmatization is the process of grouping together the different inflected forms of a word so they can be analysed as a single item.
from nltk.stem import WordNetLemmatizer
# Bag of Words model
# Bag of words is a method of representing text data in a numerical form 
# where the number of occurrences of each word is represented as a feature.
# It is used in Natural Language Processing.
# Document-term matrix is the matrix of various word counts that occur in the document.
# By setting the threshold and choosing the words that are more meaningful,we can build a histogram of all the words.
# It is used in Natural Language Processing.
# Topic modeling is the process of identifying patterns in text data that correspond to a topic.
# If the text contains multiple topics, then this technique can be used to identify and separate those themes witin the input text.
# Latent Dirichlet Allocation (LDA) is a popular topic modeling technique where the underlying intuition is that a given piece of text is a combination of multiple topics.
# It is used in Natural Language Processing.
# We need to import the gensim package in python using the LDA algorithm.
# Named Entity Recognition (NER) is a process of identifying named entities in unstructured text into predefined categories.
# Named entities are proper nouns that refer to specific objects, concepts, or entities in the real world
# Named entities can be people, places, organizations, dates, times, etc.
# Named entity recognition is used in Natural Language Processing.


# Deep Learning
# Deep learning is a subset of machine learning that is used for training deep neural networks
# We would feed the machine (training) with a lot of images of cats and dogs.
# The machine would learn to identify the images as cats or dogs.
# Convolutional Neural Networks (CNNs) are used for image recognition tasks.
# CNNs are made up of neurons consisting of weights and biases.
# CNNs are used for image recognition tasks.
# These neurons accept input data, process it, and then output something.
# The output of one neuron becomes the input of another neuron.
# The goal of the network is to go from the raw image data in the input layer to the correct class in the output layer.
# When we are working with ordinary neural networks, we need to convert the input data into a single layer.
# This layer acts as the input to the neural network,which then passes through the layers of the neural network.
# In these layers, each neuron is connected to all the neurons in the previous layer.
# The main disadvantage of ordinary neural networks is that they do not scale well to full images.
# CNNs are used for image recognition tasks.
# CNNs explicitly consider the structure of images when processing the data.
# The neurons in CNNs are arranged in 3 dimensions - width,height, and depth.
# Each neuron in the current layer is connected to a small patch of the output from the previous layer.
# It's like overlaying an NxN filter on the input image. It uses M filters to be sure about getting all the details.
# These M filters act as feature extractors. If you look at the outputs of these filters,
# we can see that they extract features like edges,corners, and so on.
# Types of layers in a CNN
# CNN consists of different layers. They are input layer and output layer.
# Between these layers there are some multiple hidden layers.There is no limitation for hidden layers present in the network.
# Types of layers:

# Input layer - This layer takes the row image data as it is.

# Convolutional layer - This layer is responsible for feature extraction.
# This layer computes the convolutions between the neurons and the various patches in the input.

# Pooling - It is responsible for reducing the spatial size of the convoluted feature.
# Pooling combines the output of a neuron cluster at one layer into a single neuron in the next layer.It uses the MAX function

# Flatten - This layer is used to flatten the output of the pooling layer.

# Dense layer - This layer is used to create the output layer.

# Fully Connected Layer - This layer computes the output scores in the last layer.

# The output of the fully connected layer is passed through a softmax function to get the probabilities of the output classes.
# The resulting output is the size 1x1xL where L is the number of classes in the training dataset.

# Artificial Neural Network (ANN) is a model designed to simulate the learning process of the human brain.
# ANNs are designed such that they can identify the underlying patterns in a data and learn from them.
# The data is fed into the network in batches.
# The network is trained using backpropagation.
# The network can be trained to recognize patterns in data and can be used for image recognition.
# ANN can learn to perform tasks by observing examples, we do not need to program them with task-specific rules.
# Such a network is a colection of Artificial neurons connected nodes.
# Aplications of ANN:

# 1. Computer Vision
# 2. Natural Language Processing
# 3. Speech Recognition
# 4. Speech Synthesis
# 5. Robotics
# 6. Games
# 7. Internet of Things
# 8. Internet of People

# Artificial Neurons are also called perceptrons.This consist of the following basic terms:

# 1. Input
# 2. Output
# 3. Bias
# 4. Weight
# 5. Activation Function
# 6. Threshold
# 7. Activation
# 8. Learning
# 9. Learning Rate
# 10. Learning Algorithm
# 11. Learning Process
# 12. Learning Rules
# 13. Learning Technique
# 14. Learning Model

# A perceptron is an artificial neuron unit in a neuron network.
# It is an element of the artificial neural network.
# It is an algorithm or a single-layered neural network that works as a binary classifier for supervised learning.
# It is linear in nature and can take mutiple inputs to give out a single binary output,thereby being able to classify the data sets available.
# It is a supervised learning algorithm, which means it requires a labeled dataset to train the model.
# Types of perceptrons:

# 1. Single Perceptron - Single layer Perceptrons is the simplest type of artificial neural network that can learn only linearly separable patterns.
# 2. Multilayer Perceptron - Multilayer Perceptron is a type of artificial neural network that can learn non-linearly separable patterns.

# In this ,the algorithm consists of two phases:
# 1. Forward Propagation - In this phase, the input is propagated through the network to the output layer
# 2. Backward Propagation - In this phase, the error is propagated back through the network to update the weights and bias values.

# The weights and bias values are updated using the learning algorithm.