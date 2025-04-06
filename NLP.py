import nltk
nltk.data.path.append(r"/run/media/panos/SAMSUNG T7/panag/Documents/nltk_data")
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize

words = word_tokenize("Programming Hub provides high quality tutorials")
print(words)

# NLP (Natural Language Processing) is a subfield of computer science that deals with AI which helps computers to understand and process human language.

# NLP is used in applications like chatbots, virtual assistants, and language translation software.

# NLP involves the following components:

# 1. Text planning - This includes retrieving the relevant content from the knowledge base.
# 2. Sentence planning - This involves organizing the content into sentences.
# 3. Translation planning - This involves translating the sentences into the target language.
# 4. Grammar checking - This involves checking the grammatical correctness of the sentences.
# 5. Text Realization - This is mapping sentence pan into sentence structure.
# 6. Speech synthesis - This is the process of converting text into speech.

# NLP Terminology

# 1. NLP - Natural Language Processing
# 2. NLU - Natural Language Understanding
# 3. NLG - Natural Language Generation
# 4. Tokenization - The process of breaking down text into individual words or tokens.
# 5. Stemming - The process of reducing inflected (or sometimes derived) words to their word stem, base or root form.
# 6. Lemmatization - The process of grouping together the different inflected forms of a word so they can be analysed as a single item.

# NLP Libraries
# 1. NLTK
# 2. SpaCy
# 3. Stanford CoreNLP
# 4. Tensorflow
# 5. PyTorch
# 6. scikit-learn
# 7. NLTK
# 8. Apache OpenNLP
# 9. Gate NLP Library
# 10. TextBlob
# 11. CoreNLP
# 12. Gensim
# 13. Polyglot
# 14. Pattern

# Steps:

# The logical steps involved in Natural Language Processing 
# are as follows: 

# Morphological Processing: It is The first phase of NLP which 
# is also known as the lexical analysis phase. 
# The main function is to break the chunks of input into token 
# sets corresponding to sentences and words. 

# In short, breaking the input words by removing all suffixes 
# and prefixes to make it easy. 

#  For example, the word "unsettled" is divided into sub-word 
#  as "un-settled" 


# Syntax Analysis 

# The second phase of NLP mainly checks the syntax. It can be 
# divided into two parts or folds:
 
# To check the formation of the sentence, and to break it up in 
# a structure that shows its syntactic relationships between 
# two or more different words.
 
# It checks the basic grammar rules. For example, 

# Boy the goes to store 

# It is wrong as per the syntax since determiners can't come 
# after a noun. 


# Semantic Analysis 

# It is the third phase of NLP. 

# The main motto of this phase is to extract the dictionary 
# meaning from the text. The text is checked for the meaning. 

# It would be useless if it doesn't have meaning even if it has 
# correct syntax. 

# For example, 

# She is wearing a colorless green dress 

# How colorless can a green dress be? 


# Pragmatic Analysis 

# This is the fourth and final phase of NLP. This phase puts in 
# the events which are present in the given context with the 
# object references obtained during the last phase. 

# For example, "Put the banana in the basket on the shelf" can 
# have two interpretations. 
# It can be interpreted as Banana is on the shelf or the Basket 
# is on the shelf. 


# import nltk

# nltk.download()

from nltk.tokenize import word_tokenize

words=word_tokenize("Programming Hub provides high quality tutorials")

print(words)

# Regular Expressions (RE) are used to find a set of strings,with the help of specialized syntax held in a pattern.

# RE is a language for mentioning text search strings.

# In MS Word,RE is used to search for text in a unique way.

# Many search engines use regular expressions features for searching strings.



# What is a regular expression? 

# "A String that defines a text 
# matching pattern" 


# Some important Characteristics of Regular Expressions: 


# 1. In special language, Regular expression is a formula. 
# It is used for mentioning a sequence of symbols and 
# simple classes of strings. It is also said to be an algebraic 
# notation for characterizing a set of strings. 

#  
# 2. The regular expression language was formalized by an 
# American Mathematician named Stephen Cole Kleene. 

# 
# 3. Two main things required for RE. The first one is the 
#  pattern which we need to search and the other is the 
# corpus of text from where we want to search. 



# In Mathematical terms, Regular Expressions is defined as 
# follows: 

# φ denotes that it is an empty language, is also a Regular 
# expression.
 
# ε is said to be a Regular expression, Which states that 
# the language has an Empty string. 

# • If X and Y are Regular expressions, 

# 1.X, Y

# 2. X.Y(Concatenation of XY) 

# 3. X+Y (Union of X and Y) 

# 4.X* Y* (Kleen Closure of X and Y) are also regular 
# expressions. 

# 5.If we obtain a string from the above-mentioned rules, it is 
#  also said to be a regular expression. 



# Syntactic Analysis is a phase of NLP. Its main function is to 
# find the dictionary meaning or the exact meaning of the text. 

# The syntactic analysis compares the text to the rules of 
# formal grammar and checks for the meaning of it. 

# It is defined as the process of analyzing the strings of 
# symbols in natural language according to rules of formal 
# grammar. Also known as Parsing. 


# Let's see the two types of Parsing:

# Top-down Parsing 
 
# It uses a recursive procedure to process the input. The parser 
# starts constructing the parse tree from the starting symbol 
# and tries to transform the start symbol to the input. 
# The only disadvantage of the recursive descent parsing 
# approach is backtracking. 

# Bottom-up Parsing 

# In this kind of parsing the most detailed parts are at the 
# bottom of the upside-down tree, and larger structures 
# composed from them are in successively higher layers until 
# at the top or "root" of the tree a single unit describes the 
# entire input stream. 

# A bottom-up parse discovers and processes that tree 
# starting from the bottom left end, and incrementally works 
# its way upwards and rightwards. 




# Derivation: 

# The derivation is a set of production rules, which can be 
# used sequentially to obtain the input strings. 

# Whenever we are doing parsing, we need to decide the 
# non-terminal, which is to be replaced using the decided set 
# of production rules. 


# Types of Derivation 

# Left-most Derivation: 

# The sentential form of input is scanned from left to right and 
# is replaced. 

# The sentential form, in this case, is known as the 
# left-sentential form. 

# Right-most Derivation 

# In this type of derivation, the sentential form of the input is 
# scanned from right to left and is replaced. 
# The sentential form is known as the right-sentential form.


 

# Grammar 

# Grammar is very essential and important to describe the 
# syntactic structure of well-formed programs. 

# It also denotes syntactical rules for conversation in natural 
# languages. 

# Linguists have attempted to define grammar since the 
# inception of natural languages like English, Hindi, etc. 

# The theory of formal languages is also applicable in 
# the fields of Computer Science mainly in programming 
# languages and data structure. 

# For example, in the 'C' language, the precise grammar rules 
# state how functions are made from lists and statements. 





#  Set of Productions 

# It is denoted by P. The set defines how the terminals and 
# non-terminals can be combined.
 
# Every production(P) consists of non-terminals, an arrow, and 
# terminals (the sequence of terminals). 

# Non-terminals are called the left side of the production and 
# terminals are called the right side of the production. 

# Start Symbol 

# The production begins from the start symbol. It is denoted by 
# the symbol S. 
# Non-terminal symbol is always designated as the start 
# symbol. 



# Semantic Analysis
 
# Semantic analysis is the process of drawing meaning from 
# text. 

# It helps computers to understand and interpret sentences, 
# paragraphs, or whole documents, by analyzing their 
# grammatical structure, and identifying relationships 
# between individual words in a particular context. 

# It's an important sub-task of Natural Language Processing 
# (NLP) and the driving force behind machine learning tools 
# like chatbots, search engines, and text analysis. 

# Semantic analysis-driven tools can help companies 
# automatically extract meaningful information from 
# unstructured data, such as emails, support tickets, and 
# customer feedback. 



# Lexical Semantics 

# Studying the meaning of individual words is called lexical 
# semantics. 

# It includes words, sub-words, affixes (sub-units), compound 
# words, and phrases also. All the words, sub-words, etc. are 
# collectively called lexical items. 

# We can also define lexical semantics as the relationship 
# between lexical items, the meaning of sentences, and the 
# syntax of sentences. 




# Working of Semantics Analysis: 

# Lexical semantics plays an important role in semantic 
# analysis, allowing machines to understand relationships 
# between lexical items (words, phrasal verbs, etc.): 

# Hyponyms 
# The specific lexical items of a generic lexical item 
# (hypernym) e.g. orange is a hyponym of fruit (hypernym). 

# Meronomy 
# A logical arrangement of text and words that denotes 
# a constituent part of or member of something e.g., a 
# segment of an orange 

# Polysemy 
# A relationship between the meanings of words or 
# phrases, although slightly different, share a common 
# core meaning e.g. I read a paper, and I wrote a paper) 

# Synonyms 
# Some words that have the same sense or nearly the 
# same meaning as another, e.g., happy, content, ecstatic, 
# overjoyed 

# Antonyms 
# The words that have close to opposite meanings e.g., 
# happy, sad 

# Homonyms 
# Any two words that sound the same and spelled alike 
# but have a different meaning e.g., orange (color), orange 
# (fruit)




# Semantic Analysis Techniques 

# Depending on the type of information one would like to 
# obtain from data, one can use one of two semantic analysis 
# techniques: 

# 1. Text classification model: 
# This type of analysis model assigns predefined 
# categories to text. 

# 2. Text extractor: 
# This type of semantic analysis technique pulls out specific 
# information from the text. 




# Types of Classification Models: 

# Topic classification: In this type of classification method, 
# the text is sorted into predefined categories based on its 
# content. 
# For example, the customer service teams may want to 
# classify support tickets as they drop into their help desk. 
# Through semantic analysis, machine learning tools can 
# recognize if a ticket should be classified as a "Payment 
# issue" or a "Shipping problem." 

# Sentiment analysis: In this type of classification method, 
# it detects positive, negative, or neutral emotions in a text 
# to denote urgency. 
# For example, tagging Twitter mentions by sentiment to 
# get a sense of how customers feel about your brand, 
# and being able to identify disgruntled customers in 
# real-time. 

# Intent classification: The text is classified based on what 
# customers want to do next. 
# You can use this to tag sales emails as "Interested" and 
# "Not Interested" to proactively reach out to those who 
# may want to try your product. 




 
 
#  Types of Extraction Models 

# Keyword extraction: It includes finding relevant words 
# and expressions in a text. This technique is used alone 
# or alongside one of the above methods to gain more 
# granular insights. 
# For instance, one can analyze the keywords in a bunch 
# of tweets that have been categorized as "negative" and 
# detect which words or topics are mentioned most often. 

# Entity extraction: This method identifies the named 
# entities in text, like names of people, companies, places, 
# etc. 
# For example, a customer service team finds it helpful 
# to automatically extract names of products, shipping 
# numbers, emails, and any other relevant data from 
# customer support tickets. 



# Tokenizing is the process of breaking up a part of the text into smaller pieces,such as sentences and words.

# Natural Language toolkit has two importat modules:

# word_tokenize

# sent_tokenize sentence tokenize

words=word_tokenize("Programming Hub provides low quality tutorials")

print(words)

from nltk.tokenize  import sent_tokenize

text="God is Great! I won a lottery."

print(sent_tokenize(text))


# Statistical NLP:

# Large amounts of data are used and conclusions are derived from it.
# It is based on the assumption that the more data you have, the more accurate your results will be.


#Statistical NLP uses machine learning algorithms to train NLP models.

# After successful training on large amounts of data, thetrained model will have positive outcomes with deduction.

# Statistical NLP is easy to scale. They can have faster development.Let's see some of the features.  

# The Frequency Distribution

file=open("/run/media/panos/SAMSUNG T7/panag/Documents/ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ/Python tries/text.txt","r")

textf=file.read()

print(textf)

from nltk.probability import FreqDist

import matplotlib.pyplot as plt

fdist=FreqDist(textf)

fdistt=fdist.most_common(10)

print(fdistt)

fdist.plot(10)


# Removing Pnctuation Marks

fdist2=FreqDist(textf)

words_no_punc=[]

for w in textf:
    if w.isalpha():
        words_no_punc.append(w.lower())
        
print(words_no_punc)

print(len(words_no_punc))


#Plotting graph without punctuation marks

fdist3=FreqDist(textf)

words_no_punc2=[]

for w in textf:
    if w.isalpha():
        words_no_punc2.append(w.lower())
        
        

fdist3=FreqDist(words_no_punc2)

fdistt3=fdist3.most_common(10)

fdist3.plot(10)




# Word Cloud is said to be a data visualization technique.
# From the given text, words are displayed on the main chart.

# The size of the word is determined by the frequency of the word in the text.

# The essential words or the frequent ones are displayed in boulder and larger font,and on the opposite,
# the less frequent or the less essential ones are displayed in smaller font.

# In NLP,it is said to be the most useful technique which gives us an idea from the text on how it can be analyzed.

# Some of the properties are as below:

# 1. font_path : It specifies the path for the fonts we want to use

# 2. max_font_size : It specifies the maximum size of the font

# 3. min_font_size : It specifies the minimum size of the font

# 4. background_color : It specifies the color of the background

# 5. max_words : It specifies the maximum number of words to be displayed

# 6. width : It specifies the width of the word cloud

# 7. height : It specifies the height of the word cloud

# 8. contour_width : It specifies the width of the contour

# 9. contour_color : It specifies the color of the contour

# 10. normalize_plurals : It removes the railing "s" from words.

# 11. stopwords : It specifies the words which we want to remove from the word cloud

# 12. font_step : It specifies the step size for the font


from wordcloud import WordCloud


text2="little lazy house built pit lazy enough workeld old upon"

wordcloud=WordCloud().generate(text2)

plt.figure(figsize=(12,12))

plt.imshow(wordcloud)

plt.axis("off")

plt.show()


# Stemming is used to normalize words by truncating the actual word into its base word.

# In simple words,it is a process in which the base word is extracted by removing affixes from the actual content word.

# While tokenizing words, the interpreter counts these words as different words and not asone since their meaning is one.


# According to the steps of NLP, the content meaning is being 
# analyzed. Hence for this purpose, we use Stemming. 

# This process does not give us the exact grammatical or 
# dictionary word for the particular group of words. 

# Stemming is mainly used in Search Engines. It is used to 
# index the words. 

# Hence it stores on the base word or the actual word rather 
# than all of its forms. Thereby, reducing the index size and 
# increasing the retrieval accuracy of the search engines. 




from nltk.stem import PorterStemmer

word_stemmer = PorterStemmer()

print(word_stemmer.stem('writing'))


# The NLTK process has stemmerl, which has the stem() 
# method. This interface has all the stemmers like the 
# porterstemmer, lancasterstem, Regexstemme, and 
# SnowballStemm. 

# The Porter stemming algorithm is known as the most 
# common algorithm. 

# It mainly eliminates and replaces the common suffixes of 
# English words. 



# PorterStemmer class:

# The PorterStemmer class helps to stem the words with the porter stemmer algorithms.

# The class has a wide knowledge about the various word forms and 
# their suffixes which in turn helps it to transform the input word into the final stem word.


# Often, The stem is a shorter word having a similar root meaning.


# Lancaster stemming algorithm:


# LancasterStemmer class:

# LancasterStemmer class helps to implement the Lancaster stemming algorithms for the word we want to stem.

from nltk.stem import LancasterStemmer

Lanc_stemmer = LancasterStemmer()

print(Lanc_stemmer.stem('helps'))


# Regular Expression stemming algorithm:

# This stemming algorithm helps us to customize and create our stemmer.

# RegexpStemmer class:

# RegexpStemmer class help us to implement Regular Expression Stemmer Algorithms.

# Firstly it selects a regular expression and removes a prefix or suffix that matches the expression.

from nltk.stem import RegexpStemmer

pattern = r'(?<!ing)(?<=\w)(ing|ly|ed|ing|es|s|t|ment)$'

Reg_stemmer = RegexpStemmer(pattern)

print(Reg_stemmer.stem('ingeat'))


# Snowball stemming algorithm 

# Snowball stemming algorithm is one of the very useful 
# stemming algorithms. 

# SnowballStemmer class 

# Snowball stemming algorithms are implemented using 
# SnowballStemmer class. 

# This class supports 15 non-English Languages. 

# To use this class, we need to create the instance with the 
# language name we want to use and later call the stem() 
# method. 


from nltk.stem import SnowballStemmer
 
French_stemmer = SnowballStemmer('french') 

print(French_stemmer.stem ('Bonjoura'))


# The Lemmatization technique is similar to stemming. The 
# output is called a ‘lemma’.Lemma is said to be the root word. 

# It finds the dictionary word and does not truncate the 
# original word. 

# NLTK has a WordNetLemmatizer class which acts as a thin 
# coating around the wordnet corpus. 

# NLTK has a WordNetLemmatizer class which acts as a thin 
# coating around the wordnet corpus. 

# To find the lemma it uses morphy() function to the WordNet 
# CorpusReader class.


from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize('books'))

# Stemming:

stemmer = PorterStemmer()

print(stemmer.stem('studies'))


# Lemmatization:


lemmatizer2 = WordNetLemmatizer()

print(lemmatizer2.lemmatize('studies'))


# PorterStemmer class cuts off the ‘es’ from the word. 

# On the other side, WordNetLemmatizer class finds the 
# dictionary word. 

# Talking in simple terms, stemming only looks at the form 
# of the word whereas lemmatization finds out the meaning 
# of the word. We will always get a valid word, after 
# lemmatization.



# Parts-of-Speech(POS)


# Sopwords like 'the' and 'a'


from nltk.corpus import stopwords

english_stops = set(stopwords.words('english'))

words =  ['I','am','a','writer'] # Create the original list

# Filter out stop words using list comprehension
filtered_words = [word for word in words if word not in english_stops]

# Now you have the filtered list in 'filtered_words'
print(filtered_words)


# POS Tagging:

# Tagging can be defined as a kind of classification, wherein 
# the description of tokens is automatically assigned. 

# The parts of speech like nouns, verbs, adjectives, and 
# conjunctions are known as descriptors ‘tag’. 

# Talking about Parts-of-Speech(POS) tagging, we define it 
# as a process of converting a sentence in the form of a list of 
# words, into a list of tuples. Tuples are in the form of tags. 

# POS tagging is also known as a process of assigning one of 
# the parts of speech to the given word.


sentence = "I am going to College"

print(sentence)

update_sent = nltk.pos_tag(word_tokenize(sentence))

print(update_sent)


# Chunking:


# Chunking is one of the most important processes in Natural 
# language Processing. 

# Chunking is a process where we have unstructured text from 
# which we extract meaningful phrases. 

# It is a process that splits simple text into phrases that are 
# more meaningful than individual words. 

# It's hard to infer meaningful information by tokenizing a 
# bunch of words. Chunking works on the top of Parts of 
# Speech tagging. 

# The input which we provide are the POS tags and the output 
# is the chunks.


# Phrases can be defined as a meaningful group of words. 

# There are 5 kinds of phrases: 

# ¢ Noun Phrases (NP) 

# ¢ Verb Phrases (VP) 

# ¢ Adjective Phrases (ADJP) 

# ¢ Adverb Phrases (ADVP) 

# ¢ Prepositional Phrases (PP)


# Some rules are being defines for the phrase structure: 

# + S(Sentence) — NPVP 

# * NP - {Determiner, Noun, Pronoun, Proper name} 

# * VP - V (NP)(PP)(Adverb) 

# * PP - Pronoun (NP) 

# * AP - Adjective (PP) 

# Let us look at an Example, 

grammar= "NP : {<DT>?<]]>*<NN>}" 
parser = nltk.RegexpParser(grammar) 
tagged_words = [("The", "DT"), ("quick", "JJ"), ("brown", "JJ"), ("fox", "NN")]
output = parser.parse(tagged_words) 
print (output) 
output.draw()


# We need to Extract Noun Phrases from the text. 

# We will define ‘?’ as an optional character And ‘*’ for o or 
# more repetitions. 

# We will first create a parser. Then we will start by parsing 
# the text. At last, we need to get an output. 

# We have successfully extracted noun phrases from the text.


# Chinking- 
# Chinking is a small part of the chunk. 

# In many scenarios, we need only a part of the text from the 
# whole chunk. 

# In complicated situations, chunking may result in unuseful 
# data. In such situations, chinking comes into the picture 
# which excludes some part of the chunked text. 

# Let's check out an example. We will be taking the whole 
# string as a chunk, and with the help of the chinking process, 
# we will eliminate the adjectives from it. 

# Chinking is most commonly used when a lot of unuseful data 
# is left even after the chunking procedure. We will be writing 
# the chinking grammar in the inverted curly braces ie. } 
# Grammar {
    
    
    


# Example 

# -O or more repetations 

# grammar = "7"" NP: {<.*>+}}<]]J>+"

grammar = "NP: {<DT>?<JJ>*<NN>}"

parser = nltk.RegexpParser(grammar)
 
output = parser.parse(tagged_words) 

print (output) 

output.draw() 

# In the above Chinking example, we will be taking the whole 
# string and then excluding adjectives from that chunk. 

# Then we create a parser and later parse the string and 
# finally display the output.


# Wordnet was created by Princeton, it is a huge lexical 

# database for the English language. It is said to be part of the 
# NLTK corpus. 

# A set of synsets is defined as a group of nouns, verbs, 
# adjectives, and adverbs. Every set of synsets has a distinct 
# meaning. 

# Some of its uses are as follows: 

# ¢ It helps find the meaning of a word. 
# ¢ Also helps us find synonyms and antonyms of a word. 

# « Words that have multiple uses and definitions, helps in 
# word sense disambiguation 

# Using wordnet, word similarities and relations can also 
# be explored.     

from nltk.corpus import wordnet as wn

# Synset instances 

# The cluster of all the synonym words having the same idea 
# is called synset instances. 

# Using Wordnet, we get a list of Synset instances. 

# The ‘wordnet.synsets(word)’ provides us the list of Synsets.

syn=wn.synsets('dog')[0]

names=syn.name()

print(names)

definitions=syn.definition()

print(definitions)

examples=syn.examples()

print(examples)


# Pros of NLP Systems:

# We as a User can ask a question about any topic and 
# get an answer within seconds. 

# NLP system provides us the answers in natural 
# language 

# The NLP system does not provide us with unwanted and 
# unnecessary answers; it gives us exact answers to our 
# questions. 

# The NLP system helps us to communicate with the 
# computer in our natural language. 

# The more information provided in the question, the more 
# accuracy we get in the answers. 

# NLP systems are very time efficient. 

# NLP is also used to improve the efficiency of 
# documentation processes. 

# NLP helps in structuring a highly unstructured data 
# source.


# Cons of NLP Systems 

# NLP systems cannot adapt to new domains and have 
# limited functions only. That is why they are built for 
# single and specific tasks only. 

# NLP systems lack a User interface which makes it 
# difficult for users to communicate with the system. 

# Complex Query Language- The NLP system will not be 
# able to provide us the correct answer if the question is 
# poorly worded or unclear. 

# NLP systems may not show us context.