# =====================================================================================================================
# 1. Import nltk and download the ‘stopwords’ and ‘punkt’ packages
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
# pip install transformers
# pip install textblob
# nltk.download('brown')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# python -m spacy download en_core_web_sm
# python -m spacy download en_core_web_lg
# pip install spacy_langdetect
# pip install textacy
# pip install sumy
# pip install simpletransformers

# !pip install spacy==2.0.12
# pip install https://github.com/huggingface/neuralcoref-models/releases/download/en_coref_md-3.0.0/en_coref_md-3.0.0.tar.gz


# Regex url link
# https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)
# [-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)


# =====================================================================================================================
# 2. Import spacy and load the language model
# import spacy
# # python -m spacy download en_core_web_sm
# nlp = spacy.load("en_core_web_sm")
# print(nlp)


# =====================================================================================================================
# 3. How to tokenize a given text?
# Q. Print the tokens of the given text document
# text = """Last week, the University of Cambridge shared its own research that shows if everyone wears a mask
# outside home,dreaded ‘second wave’ of the pandemic can be avoided."""

# C1: nltk
# import nltk
#
# tokens = nltk.word_tokenize(text)
# for token in tokens:
#     print(token)

# C2: scapy
# import spacy
#
# nlp = spacy.load("en_core_web_sm")
# doc = nlp(text)
# for token in doc:
#   print(token.text)


# =====================================================================================================================
# 4. How to get the sentences of a text document? Q. Print the sentences of the given text document

# text = """The outbreak of coronavirus disease 2019 (COVID-19) has created a global health crisis that has had a deep impact on the way we perceive our world and our everyday lives. Not only the rate of contagion and patterns of transmission threatens our sense of agency, but the safety measures put in place to contain the spread of the virus also require social distancing by refraining from doing what is inherently human, which is to find solace in the company of others. Within this context of physical threat, social and physical distancing, as well as public alarm, what has been (and can be) the role of the different mass media channels in our lives on individual, social and societal levels? Mass media have long been recognized as powerful forces shaping how we experience the world and ourselves. This recognition is accompanied by a growing volume of research, that closely follows the footsteps of technological transformations (e.g. radio, movies, television, the internet, mobiles) and the zeitgeist (e.g. cold war, 9/11, climate change) in an attempt to map mass media major impacts on how we perceive ourselves, both as individuals and citizens. Are media (broadcast and digital) still able to convey a sense of unity reaching large audiences, or are messages lost in the noisy crowd of mass self-communication? """

# C1: spacy
# import spacy
#
# nlp = spacy.load("en_core_web_sm")
# doc = nlp(text)
# for sentence in doc.sents:
#     print(sentence)
#     print(' ')

# C2: nltk
# import nltk
#
# for sentence in nltk.sent_tokenize(text):
#     print(sentence)
#     print(' ')
# import re
# # Tranh truong hop co "e.g. abcd" hoac "no. 1234" ==> chia ra thanh 2 cau: "e.g." va "abcd"
# print(re.sub(r'(no\.)\s+(\d)', r'\1\2', 'no. 5'))

# =====================================================================================================================
# 5. How to tokenize a text using the `transformers` package? Q. Tokenize the given text in encoded form using the tokenizer of Huggingface’s transformer package.
# text = "I love spring season. I go hiking with my friends"
# 
# # pip install transformers
# from transformers import AutoTokenizer
# 
# # Initialize the tokenizer
# tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
# 
# # Encoding with the tokenizer
# inputs = tokenizer.encode(text)
# print(inputs)
# print(tokenizer.decode(inputs))


# =====================================================================================================================
# 6.How to tokenize text with stopwords as delimiters? Tokenize the given text with stop words (“is”,”the”,”was”) as delimiters.
# Tokenizing this way identifies meaningful phrases. Sometimes, useful for topic modeling
# text = "Walter was feeling anxious. He was diagnosed today. He probably is the best person I know."
#
# stop_words_and_delims = ['was', 'is', 'the', '.', ',', '-', '!', '?']
# for r in stop_words_and_delims:
#     text = text.replace(r, 'DELIM')
#
# words = [t.strip() for t in text.split('DELIM')]
# words_filtered = list(filter(lambda a: a not in [''], words))
# print(words_filtered)


# =====================================================================================================================
# 7. How to remove stop words in a text ? Q. Remove all the stopwords ( ‘a’ , ‘the’, ‘was’…) from the text

# text = """the outbreak of coronavirus disease 2019 (COVID-19) has created a global health crisis that has had a deep
# impact on the way we perceive our world and our everyday lives. Not only the rate of contagion and patterns of
# transmission threatens our sense of agency, but the safety measures put in place to contain the spread of the virus
# also require social distancing by refraining from doing what is inherently human, which is to find solace in the
# company of others."""
#
# from nltk.corpus import stopwords
# import nltk
#
# my_stopwords = set(stopwords.words('english'))
# new_tokens = []
#
# # Tokenization using word_tokenize()
# all_tokens = nltk.word_tokenize(text)
#
# for token in all_tokens:
#     if token not in my_stopwords:
#         new_tokens.append(token)
#
# print(" ".join(new_tokens))


# =====================================================================================================================
# 8. How to add custom stop words in spaCy ? Q. Add the custom stopwords “NIL” and “JUNK” in spaCy and remove the stopwords in below text
# text = " Jonas was a JUNK great guy NIL Adam was evil NIL Martha JUNK was more of a fool "
# customize_stop_words = ['NIL', 'JUNK']
#
# import spacy
# nlp = spacy.load('en_core_web_sm')
# # Adding these stop words
# for w in customize_stop_words:
#     nlp.vocab[w].is_stop = True
# doc = nlp(text)
# tokens = [token.text for token in doc if not token.is_stop]
# print(" ".join(tokens))


# =====================================================================================================================
# 9. How to remove punctuations? Q. Remove all the punctuations in the given text
# text = "The match has concluded !!! India has won the match . Will we fin the finals too ? !"

# C1: spacy
# import spacy
#
# nlp = spacy.load('en_core_web_sm')
# doc = nlp(text)
# new_tokens = []
# # Check if a token is a punctuation through is_punct attribute
# for token in doc:
#     if not token.is_punct:
#         new_tokens.append(token.text)
#
# print(" ".join(new_tokens))

# C2: nltk
# from string import punctuation
# import nltk
#
# new_tokens = []
# tokens = nltk.word_tokenize(text)
# for token in tokens:
#     if token not in punctuation:
#         new_tokens.append(token)
# print(' '.join(new_tokens))


# =====================================================================================================================
# 10. How to perform stemming? Q. Perform stemming/ convert each token to it’s root form in the given text
# text = "Dancing is an art. Students should be taught dance as a subject in schools . I danced in many of my school" \
#        " function. Some people are always hesitating to dance."
# from nltk.stem import PorterStemmer
# import nltk
# from string import punctuation
#
# stemmer = PorterStemmer()
# stemmed_tokens = []
# for token in nltk.word_tokenize(text):
#     stemmed_tokens.append(stemmer.stem(token))
#
# new_text = " ".join(stemmed_tokens)
# for char in punctuation:
#     new_text = new_text.replace(' '+char, char)
# print(new_text)


# =====================================================================================================================
# 11. How to lemmatize a given text ? Q. Perform lemmatzation on the given text
# text = "Dancing is an art. Students should be taught dance as a subject in schools . I danced in many of my school" \
#        " function. Some people are always hesitating to dance."

# # C1: spacy
# import spacy
# from string import punctuation
#
# nlp = spacy.load('en_core_web_sm')
# doc = nlp(text)
#
# lemmatized = [token.lemma_ for token in doc]
# new_text = " ".join(lemmatized)
# for char in punctuation:
#     new_text = new_text.replace(' '+char, char)
# print(new_text)

# # C2: nltk
# import nltk
# # nltk.download('wordnet')
# # nltk.download('omw-1.4')
# from nltk.stem import WordNetLemmatizer
# from string import punctuation
#
# lemmar = WordNetLemmatizer()
# stemmed_tokens = []
# for token in nltk.word_tokenize(text):
#     stemmed_tokens.append(lemmar.lemmatize(token))
#
# new_text = " ".join(stemmed_tokens)
# for char in punctuation:
#     new_text = new_text.replace(' '+char, char)
# print(new_text)
# print(text)


# =====================================================================================================================
# 12. How to extract usernames from emails? Q. Extract the usernames from the email addresses present in the text
# text = "The new registrations are potter709@gmail.com , elixir101@gmail.com. If you find any disruptions, kindly" \
#        " contact granger111@gamil.com or severus77@gamil.com "
# import re
#
# usernames = re.findall(r'(\S+)@', text)
# print(usernames)


# =====================================================================================================================
# 13. How to find the most common words in the text excluding stopwords? Q. Extract the top 10 most common words in the given text excluding stopwords.
# text = """Junkfood - Food that do no good to our body. And there's no need of them in our body but still we willingly eat them because they are great in taste and easy to cook or ready to eat. Junk foods have no or very less nutritional value and irrespective of the way they are marketed, they are not healthy to consume.The only reason of their gaining popularity and increased trend of consumption is
# that they are ready to eat or easy to cook foods. People, of all age groups are moving towards Junkfood as it is hassle free and often ready to grab and eat. Cold drinks, chips, noodles, pizza, burgers, French fries etc. are few examples from the great variety of junk food available in the market.
#  Junkfood is the most dangerous food ever but it is pleasure in eating and it gives a great taste in mouth examples of Junkfood are kurkure and chips.. cold rings are also source of junk food... they shud nt be ate in high amounts as it results fatal to our body... it cn be eated in a limited extend ... in research its found tht ths junk foods r very dangerous fr our health
# Junkfood is very harmful that is slowly eating away the health of the present generation. The term itself denotes how dangerous it is for our bodies. Most importantly, it tastes so good that people consume it on a daily basis. However, not much awareness is spread about the harmful effects of Junkfood .
# The problem is more serious than you think. Various studies show that Junkfood impacts our health negatively. They contain higher levels of calories, fats, and sugar. On the contrary, they have very low amounts of healthy nutrients and lack dietary fibers. Parents must discourage their children from consuming junk food because of the ill effects it has on one’s health.
# Junkfood is the easiest way to gain unhealthy weight. The amount of fats and sugar in the food makes you gain weight rapidly. However, this is not a healthy weight. It is more of fats and cholesterol which will have a harmful impact on your health. Junk food is also one of the main reasons for the increase in obesity nowadays.
# This food only looks and tastes good, other than that, it has no positive points. The amount of calorie your body requires to stay fit is not fulfilled by this food. For instance, foods like French fries, burgers, candy, and cookies, all have high amounts of sugar and fats. Therefore, this can result in long-term illnesses like diabetes and high blood pressure. This may also result in kidney failure."""
# import spacy
#
# nlp = spacy.load("en_core_web_sm")
# doc = nlp(text)
#
# # Removal of stop words and punctuations
# words = [token.orth_ for token in doc if token.is_stop == False and token.is_punct == False]
#
# freq_dict = {}
# # Calculating frequency count
# for word in words:
#     if word not in freq_dict:
#         freq_dict[word] = 1
#     else:
#         freq_dict[word] += 1
#
# sort_keys = sorted(freq_dict, key=freq_dict.get, reverse=True)
# print({key: freq_dict[key] for key in sort_keys})


# =====================================================================================================================
# 14. How to do spell correction in a given text? Q. Correct the spelling errors in the following text
# text = "He is a gret person. He beleives in bod"
# from textblob import TextBlob
# # pip install textblob
# text = TextBlob(text)
# print(text.correct())


# =====================================================================================================================
# 15. How to tokenize tweets? Q. Clean the following tweet and tokenize them
# text = " Having lots of fun #goa #vaction #summervacation. Fancy dinner @Beachbay restro :) "
# import re
# import nltk
# from nltk.tokenize import TweetTokenizer
#
# # Cleaning the tweets
# text = re.sub(r'\W', ' ', text)
#
# # Using nltk's TweetTokenizer
#
# tokenizer = TweetTokenizer()
# print(tokenizer.tokenize(text))
# print(nltk.word_tokenize(text))


# =====================================================================================================================
# 101. Write a program to find all words that occur at least three times in the Brown Corpus.
# from nltk.corpus import brown
#
# # nltk.download('brown')
# all_unique_words_brown = set(brown.words())
# brown_fd = nltk.FreqDist(brown.words())
# atleast_3times = [word for word in all_unique_words_brown if brown_fd[word] > 2]
# print(atleast_3times)


# =====================================================================================================================
# 36. How to merge two tokens as one? Q. Merge the first name and last name as single token in the given sentence
# import spacy
# import nltk
# nlp = spacy.load('en_core_web_sm')
# text = "Robert Langdon is a famous character in various books and movies"
# # document = nlp(text)
# # tokens = nltk.word_tokenize(text)
# # person = []
# # for ent in document.ents:
# #     print(ent.label_, ent.text)
# #     if ent.label_ == 'PERSON':
# #         person.append(ent)
# # print(person)
#
# doc = nlp(text)
#
# with doc.retokenize() as retokenizer:
#     start = 0
#     for idx, token in enumerate(doc):
#         if token.ent_type_ == 'PERSON':
#             continue
#         else:
#             if start == idx:
#                 start = idx + 1
#                 continue
#             retokenizer.merge(doc[start:idx])
#             start = idx+1
#     if start != len(doc):
#         retokenizer.merge(doc[start:])
#
# for token in doc:
#     print(token.text)


# =====================================================================================================================
# 16. How to extract all the nouns in a text? Q. Extract and print all the nouns present in the below text
import spacy

# text = "James works at Microsoft. She lives in manchester and likes to play the flute"

# C1: spacy
# nlp = spacy.load("en_core_web_sm")
# doc = nlp(text)
#
# for token in doc:
#     if token.pos_ == 'NOUN' or token.pos_ == 'PROPN':
#         print(token.text)


# =====================================================================================================================
# 17. How to extract all the pronouns in a text? Q. Extract and print all the pronouns in the text
# text = "John is happy finally. He had landed his dream job finally. He told his mom. She was elated "
# nlp = spacy.load("en_core_web_sm")
# doc = nlp(text)
#
# for token in doc:
#     if token.pos_ == 'PRON':
#         print(token.text)

# =====================================================================================================================
# 18. How to find similarity between two words/text documents? Find the similarity between any two words/text documents
import spacy  # spacy == 3.2.5

word1 = "John lives in Canada"
word2 = "James lives in America, though he's not from there"
word3 = "excellent"
nlp = spacy.load('en_core_web_lg')
token1 = nlp(word1)
token2 = nlp(word2)
token3 = nlp(word3)

# Use similarity() function of tokens
print(token1.similarity(token2))
print(token1.similarity(token3))

# =====================================================================================================================
# 20. How to find the cosine similarity of two documents? Q. Find the cosine similarity between two given documents
# text1 = 'Taj Mahal is a tourist place in India'
# text2 = 'Great Wall of China is a tourist place in china'
# documents = [text1, text2]
# # pip install scikit-learn
# # pip install pandas
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import pandas as pd
#
# vectorizer = CountVectorizer()
# matrix = vectorizer.fit_transform(documents)
#
# # Obtaining the document-word matrix
# doc_term_matrix = matrix.todense()
#
# # Computing cosine similarity
# df = pd.DataFrame(doc_term_matrix)
# print(cosine_similarity(df, df))


# =====================================================================================================================
# 21. How to find soft cosine similarity of documents? Q. Compute the soft cosine similarity of the given documents
# doc_soup = "Soup is a primarily liquid food, generally served warm or hot (but may be cool or cold), that is made by combining ingredients of meat or vegetables with stock, juice, water, or another liquid. "
#
# doc_noodles = "Noodles are a staple food in many cultures. They are made from unleavened dough which is stretched, extruded, or rolled flat and cut into one of a variety of shapes."
#
# doc_dosa = "Dosa is a type of pancake from the Indian subcontinent, made from a fermented batter. It is somewhat similar to a crepe in appearance. Its main ingredients are rice and black gram."
#
# doc_trump = "Mr. Trump became president after winning the political election. Though he lost the support of some republican friends, Trump is friends with President Putin"
#
# doc_election = "President Trump says Putin had no political interference is the election outcome. He says it was a witchhunt by political parties. He claimed President Putin is a friend who had nothing to do with the election"
#
# doc_putin = "Post elections, Vladimir Putin became President of Russia. President Putin had served as the Prime Minister earlier in his political career"
#
# from gensim import corpora
# from gensim.utils import simple_preprocess
# from gensim.models import Word2Vec
# from gensim.similarities import SoftCosineSimilarity, SparseTermSimilarityMatrix, WordEmbeddingSimilarityIndex
#
# documents = [doc_soup, doc_noodles, doc_dosa, doc_trump, doc_election, doc_putin]
#
# model = Word2Vec(documents)
# termsim_index = WordEmbeddingSimilarityIndex(model.wv)
# dictionary = corpora.Dictionary([simple_preprocess(doc) for doc in documents])
#
# # Prepare the similarity matrix
# similarity_matrix = SparseTermSimilarityMatrix(termsim_index, dictionary)
#
# # Convert the sentences into bag-of-words vectors.
# sent_1 = dictionary.doc2bow(simple_preprocess(doc_trump))
# sent_2 = dictionary.doc2bow(simple_preprocess(doc_election))
# sent_3 = dictionary.doc2bow(simple_preprocess(doc_putin))
# sent_4 = dictionary.doc2bow(simple_preprocess(doc_soup))
# sent_5 = dictionary.doc2bow(simple_preprocess(doc_noodles))
# sent_6 = dictionary.doc2bow(simple_preprocess(doc_dosa))
#
# sentences = [sent_1, sent_2, sent_3, sent_4, sent_5, sent_6]
#
# # Compute soft cosine similarity
# docsim_index = SoftCosineSimilarity(sentences, similarity_matrix, num_best=10)
# print([i for i in docsim_index[sent_1] if i[0] == 1][0][1])


# =====================================================================================================================
# 22. How to find similar words using pre-trained Word2Vec? Q. Find all similiar words to “amazing” using Google news Word2Vec.
# import gensim.downloader as api
#
# # Load the pretrained google news word2vec model
# word2vec_model300 = api.load('word2vec-google-news-300')
#
# # Using most_similar() function
# print(word2vec_model300.most_similar('amazing'))


# =====================================================================================================================
# 23. How to compute Word mover distance? Q. Compute the word mover distance between given two texts
# sentence_orange = 'Oranges are my favorite fruit'
# sent = "apples are not my favorite"

# # C1:
# import gensim.downloader as api
#
# model = api.load('word2vec-google-news-300')
# # Computing the word mover distance
# print(model.wmdistance(sentence_orange, sent))

# # C2:
# import gensim.downloader as api
# from gensim.models.word2vec import Word2Vec
#
# corpus = api.load('text8')
# model = Word2Vec(corpus, vector_size=300, min_count=1)
# print(model.wv.wmdistance(sentence_orange, sent, norm=False))
# print(model.wv.wmdistance(sent, sentence_orange, norm=False))


# =====================================================================================================================
# 24. How to replace all the pronouns in a text with their respective object names? Q. Replace the pronouns in below text by the respective object nmaes
# text = " My sister has a dog and she loves him"
# # !pip install spacy==2.0.12
# # !pip install https://github.com/huggingface/neuralcoref-models/releases/download/en_coref_md-3.0.0/en_coref_md-3.0.0.tar.gz
# import en_coref_md
#
# # Add it to the pipeline
# nlp = en_coref_md.load()
# # nlp = spacy.load('en_core_web_sm')
#
# # Printing the coreferences
# doc1 = nlp('My sister has a dog. She loves him.')
# for cluster in doc1._.coref_clusters:
#     print(cluster.mentions)


# =====================================================================================================================
# 25. How to extract topic keywords using LSA? Q. Extract the topic keywords from the given texts using LSA(Latent Semantic Analysis )
# texts = [
#     """It's all about travel. I travel a lot.  those who do not travel read only a page.” – said Saint Augustine. He was a great travel person. Travelling can teach you more than any university course. You learn about the culture of the country you visit. If you talk to locals, you will likely learn about their thinking, habits, traditions and history as well.If you travel, you will not only learn about foreign cultures, but about your own as well. You will notice the cultural differences, and will find out what makes your culture unique. After retrurning from a long journey, you will see your country with new eyes.""",
#     """ You can learn a lot about yourself through travelling. You can observe how you feel beeing far from your country. You will find out how you feel about your homeland.You should travel You will realise how you really feel about foreign people. You will find out how much you know/do not know about the world. You will be able to observe how you react in completely new situations. You will test your language, orientational and social skills. You will not be the same person after returning home.During travelling you will meet people that are very different from you. If you travel enough, you will learn to accept and appreciate these differences. Traveling makes you more open and accepting.""",
#     """Some of my most cherished memories are from the times when I was travelling. If you travel, you can experience things that you could never experience at home. You may see beautiful places and landscapes that do not exist where you live. You may meet people that will change your life, and your thingking. You may try activities that you have never tried before.Travelling will inevitably make you more independent and confident. You will realise that you can cope with a lot of unexpected situations. You will realise that you can survive without all that help that is always available for you at home. You will likely find out that you are much stronger and braver than you have expected.""",
#     """If you travel, you may learn a lot of useful things. These things can be anything from a new recepie, to a new, more effective solution to an ordinary problem or a new way of creating something.Even if you go to a country where they speak the same language as you, you may still learn some new words and expressions that are only used there. If you go to a country where they speak a different language, you will learn even more.""",
#     """After arriving home from a long journey, a lot of travellers experience that they are much more motivated than they were before they left. During your trip you may learn things that you will want to try at home as well. You may want to test your new skills and knowledge. Your experiences will give you a lot of energy.During travelling you may experience the craziest, most exciting things, that will eventually become great stories that you can tell others. When you grow old and look back at your life and all your travel experiences, you will realise how much you have done in your life and your life was not in vain. It can provide you with happiness and satisfaction for the rest of your life.""",
#     """The benefits of travel are not just a one-time thing: travel changes you physically and psychologically. Having little time or money isn't a valid excuse. You can travel for cheap very easily. If you have a full-time job and a family, you can still travel on the weekends or holidays, even with a baby. travel  more is likely to have a tremendous impact on your mental well-being, especially if you're no used to going out of your comfort zone. Trust me: travel more and your doctor will be happy. Be sure to get in touch with your physician, they might recommend some medication to accompany you in your travels, especially if you're heading to regions of the globe with potentially dangerous diseases.""",
#     """Sure, you probably feel comfortable where you are, but that is just a fraction of the world! If you are a student, take advantage of programs such as Erasmus to get to know more people, experience and understand their culture. Dare traveling to regions you have a skeptical opinion about. I bet that you will change your mind and realize that everything is not so bad abroad.""",
#     """ So, travel makes you cherish life. Let's travel more . Share your travel diaries with us too"""
# ]
# from sklearn.feature_extraction.text import TfidfVectorizer
#
# # Defining the vectorizer
# vectorizer = TfidfVectorizer(stop_words='english', max_features=1000, max_df=0.5, smooth_idf=True)
#
# # Transforming the tokens into the matrix form through .fit_transform()
# matrix = vectorizer.fit_transform(texts)
#
# # SVD represent documents and terms in vectors
# from sklearn.decomposition import TruncatedSVD
#
# SVD_model = TruncatedSVD(n_components=10, algorithm='randomized', n_iter=100, random_state=122)
# SVD_model.fit(matrix)
#
# # Getting the terms
# terms = vectorizer.get_feature_names()
#
# # Iterating through each topic
# for i, comp in enumerate(SVD_model.components_):
#     terms_comp = zip(terms, comp)
#     # sorting the 7 most important terms
#     sorted_terms = sorted(terms_comp, key=lambda x: x[1], reverse=True)[:7]
#     print("Topic " + str(i) + ": ")
#     # printing the terms of a topic
#     for t in sorted_terms:
#         print(t[0], end=' ')
#     print(' ')


# =====================================================================================================================
# 26. How to extract topic Keywords using LDA? Q. Extract the the topics from the given texts with the help of LDA(Latent dirichlet algorith
# from gensim import corpora
# import nltk
# from nltk.corpus import stopwords
#
# # Before topic extraction, we remove punctuations and stopwords.
# my_stopwords = set(stopwords.words('english'))
# punctuations = ['.', '!', ',', "You", "I"]
#
# # We prepare a list containing lists of tokens of each text
# all_tokens = []
# for text in texts:
#     tokens = []
#     raw = nltk.wordpunct_tokenize(text)
#     for token in raw:
#         if token not in my_stopwords:
#             if token not in punctuations:
#                 tokens.append(token)
#                 all_tokens.append(tokens)
#
# # Creating a gensim dictionary and the matrix
# dictionary = corpora.Dictionary(all_tokens)
# doc_term_matrix = [dictionary.doc2bow(doc) for doc in all_tokens]
#
# # Building the model and training it with the matrix
# from gensim.models.ldamodel import LdaModel
#
# model = LdaModel(doc_term_matrix, num_topics=5, id2word=dictionary, passes=40)
#
# print(model.print_topics(num_topics=6, num_words=5))


# =====================================================================================================================
# 27. How to extract topic keywords using NMF? Q. Extract the the topics from the given texts with the help of NMF(Non-negative Matrix Factorization method)
# from sklearn.feature_extraction.text import TfidfVectorizer
#
# # Defining the vectorizer
# vectorizer = TfidfVectorizer(stop_words='english', max_features=1000, max_df=0.5, smooth_idf=True)
#
# # Transforming the tokens into the matrix form through .fit_transform()
# nmf_matrix = vectorizer.fit_transform(texts)
# from sklearn.decomposition import NMF
#
# nmf_model = NMF(n_components=6)
# nmf_model.fit(nmf_matrix)
#
#
# # Function to print topics
# def print_topics_nmf(model, vectorizer, top_n=6):
#     for idx, topic in enumerate(model.components_):
#         print("Topic %d:" % (idx))
#         print([(vectorizer.get_feature_names()[i], topic[i])
#                for i in topic.argsort()[:-top_n - 1:-1]])
#
# print_topics_nmf(nmf_model, vectorizer)


# =====================================================================================================================
# 28. How to classify a text as positive/negative sentiment? Q. Detect if a text is positive or negative sentiment
# text = "It was a very pleasant day"
# from textblob import TextBlob
# blob = TextBlob(text)
#
# # Using the sentiment attribute
# print(blob.sentiment)
# if (blob.sentiment.polarity > 0):
#     print("Positive")


# =====================================================================================================================
# 29. How to use the Word2Vec model for representing words? Q. Extract the word vector representation of the word using word2vec model
# texts = [" Photography is an excellent hobby to pursue ",
#          " Photographers usually develop patience, calmnesss"
#          " You can try Photography with any good mobile too"]
# all_tokens = []
# for text in texts:
#     tokens = []
#     raw = nltk.wordpunct_tokenize(text)
#     for token in raw:
#         tokens.append(token)
#     all_tokens.append(tokens)
#
# # Import and fit the model with data
# from gensim.models import Word2Vec
#
# model = Word2Vec(all_tokens, min_count=1)
#
# # Getting the vector representation of a word
# print(model.wv['Photography'])


# =====================================================================================================================
# 30. How to visualize the word embedding obtained from word2Vec model? Q. Implement Word embedding on the given texts and visualize it
# texts = [" Photography is an excellent hobby to pursue ",
#          " Photographers usually develop patience, calmnesss"
#          " You can try Photography with any good mobile too"]
# all_tokens = []
# for text in texts:
#     tokens = []
#     raw = nltk.wordpunct_tokenize(text)
#     for token in raw:
#         tokens.append(token)
#         all_tokens.append(tokens)
#
# # Import and fit the model with data
# import gensim
# from gensim.models import Word2Vec
#
# model = Word2Vec(all_tokens)
#
# # Visualizing the word embedding
# from sklearn.decomposition import PCA
# from matplotlib import pyplot
#
# X = model.wv[list(model.wv.index_to_key)]
# pca = PCA(n_components=2)
# result = pca.fit_transform(X)
# # create a scatter plot of the projection
# pyplot.scatter(result[:, 0], result[:, 1])
# words = list(model.wv.index_to_key)
# for i, word in enumerate(words):
#     pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
# pyplot.show()


# =====================================================================================================================
# 31. How to represent the document using Doc2Vec model? Q. Represent a text document in the form a vector
# texts = [" Photography is an excellent hobby to pursue ",
#          " Photographers usually develop patience, calmnesss"
#          " You can try Photography with any good mobile too"]
# from gensim.models import Doc2Vec
# import gensim
#
# all_tokens = []
# for text in texts:
#     tokens = []
#     raw = nltk.wordpunct_tokenize(text)
#     for token in raw:
#         tokens.append(token)
#         all_tokens.append(tokens)
#
# # Preparing data in the format and fitting to the model
# def tagged_document(list_of_list_of_words):
#     for i, list_of_words in enumerate(list_of_list_of_words):
#         yield gensim.models.doc2vec.TaggedDocument(list_of_words, [i])
#
#
# my_data = list(tagged_document(all_tokens))
# model = Doc2Vec(my_data)
#
# print(model.infer_vector(['photography', 'is', 'an', ' excellent ', 'hobby ', 'to', ' pursue ']))


# =====================================================================================================================
# 32. How to extract the TF-IDF Matrix? Q. Extract the TF-IDF (Term Frequency -Inverse Document Frequency) Matrix for the given list of text documents
# text_documents = ['Painting is a hobby for many , passion for some',
#                   'My hobby is coin collection'
#                   'I do some Painting every now and then']
# from gensim import corpora
# from gensim.utils import simple_preprocess
# from gensim import models

# # C1: gensim
# doc_tokenized = [simple_preprocess(text) for text in text_documents]
# dictionary = corpora.Dictionary()
#
# # Creating the Bag of Words from the docs
# BoW_corpus = [dictionary.doc2bow(doc, allow_update=True) for doc in doc_tokenized]
# for doc in BoW_corpus:
#     print([[dictionary[id], freq] for id, freq in doc])
# import numpy as np
# tfidf = models.TfidfModel(BoW_corpus)

# # C2: sklearn
# from sklearn.feature_extraction.text import TfidfVectorizer
#
# # Fit the vectorizer to our text documents
# vectorizer = TfidfVectorizer()
# matrix = vectorizer.fit_transform(text_documents)
# print(matrix)


# =====================================================================================================================
# 33. How to create bigrams using Gensim’s Phraser? Q. Create bigrams from the given texts using Gensim library’s Phrases
# documents = ["the mayor of new york was there", "new york mayor was present"]
# # Import Phraser from gensim
# from gensim.models import Phrases
# from gensim.models.phrases import Phraser
#
# sentence_stream = [doc.split(" ") for doc in documents]
#
# # Creating bigram phraser
# bigram = Phrases(sentence_stream, min_count=1, threshold=2, delimiter=' ')
# bigram_phraser = Phraser(bigram)
#
# for sent in sentence_stream:
#     tokens_ = bigram_phraser[sent]
#     print(tokens_)


# =====================================================================================================================
# 34. How to create bigrams, trigrams using ngrams? Q. Extract all bigrams , trigrams using ngrams of nltk library
# Sentences = "Machine learning is a neccessary field in today's world. Data science can do wonders . Natural Language Processing is how machines understand text "
# from nltk import ngrams
#
# bigram = list(ngrams(Sentences.lower().split(), 2))
# trigram = list(ngrams(Sentences.lower().split(), 3))
#
# print(" Bigrams are", bigram)
# print(" Trigrams are", trigram)


# =====================================================================================================================
# 35. How to detect the language of entered text? Q. Find out the language of the given text
# text = "El agente imprime su pase de abordaje. Los oficiales de seguridad del aeropuerto pasan junto a él con un perro grande. El perro está olfateando alrededor del equipaje de las personas tratando de detectar drogas o explosivos."
# import spacy
# # !pip install spacy_langdetect
# from spacy_langdetect import LanguageDetector
# from spacy.language import Language
#
# nlp = spacy.load('en_core_web_sm')
#
# # Add the language detector to the processing pipeline
# @Language.factory('language_detector')
# def language_detector(nlp, name):
#     return LanguageDetector()
#
# nlp.add_pipe('language_detector', last=True)
#
# doc = nlp(text)
# # document level language detection. Think of it like average language of the document!
# print(doc._.language)
# # sentence level language detection
# for sent in doc.sents:
#     print(sent, sent._.language)


# =====================================================================================================================
# 37. How to extract Noun phrases from a text ? Q. Extract and print the noun phrases in given text document
# text = "There is a empty house on the Elm Street"
# import spacy
#
# nlp = spacy.load('en_core_web_sm')
# doc = nlp(text)
#
# # Use `noun_chunks` attribute to extract the Noun phrases
# chunks = list(doc.noun_chunks)
# print(chunks)


# =====================================================================================================================
# 38. How to extract Verb phrases from the text ? Q. Extract the Verb Phrases from the given text
# text = "I may bake a cake for my birthday. The talk will introduce reader about Use of baking"
# # Regex pattern to identify verb phrase
# # !pip install textacy
# import spacy
# import textacy
# from spacy.util import filter_spans
#
# # Regex pattern to identify verb phrase
# verb_pattern = [{"POS": "AUX", "OP": "*"}, {"POS": "VERB", "OP": "*"}, {"POS": "ADV", "OP": "*"}, {"POS": "VERB", "OP": "+"}]
# doc = textacy.make_spacy_doc(text, lang='en_core_web_lg')
#
# # Finding matches
# verb_phrases = textacy.extract.token_matches(doc, verb_pattern)
# verb_phrases = filter_spans(verb_phrases)
# # Print all Verb Phrase
# for chunk in verb_phrases:
#     print(chunk.text)


# =====================================================================================================================
# 39. How to extract first name and last names present in the document ? Q. Extract any two consecutive Proper Nouns that occour in the text document
# text = "Sherlock Holmes and Clint Thomas were good friends. I am a fan of John Mark"
# from spacy.matcher import Matcher
#
# nlp = spacy.load("en_core_web_sm")
# matcher = Matcher(nlp.vocab)
# doc = nlp(text)
#
#
# # Function that adds patterns to the matcher and finds the respective matches
# def extract_matches(doc):
#     pattern = [[{'POS': 'PROPN'}, {'POS': 'PROPN', "OP": "+"}]]
#     matcher.add('FULL_NAME', pattern)
#     matches = matcher(doc)
#
#     for match_id, start, end in matches:
#         span = doc[start:end]
#         print(span.text)
#
#
# extract_matches(doc)


# =====================================================================================================================
# 40. How to identify named entities in the given text? Q. Identify and print all the named entities with their labels in the below text
# text = " Walter works at Google. He lives in London."
# import spacy
#
# nlp = spacy.load("en_core_web_sm")
#
# doc = nlp(text)
# for ent in doc.ents:
#     print(ent.orth_, ent.label_)


# =====================================================================================================================
# 41. How to identify all the names of Organizations present in the text with NER? Q. Identify and extract a list of all organizations/Companies mentioned in the given news article
# text =" Google has released it's new model which has got attention of everyone. Amazon is planning to expand into Food delivery, thereby giving competition . Apple is coming up with new iphone model. Flipkart will have to catch up soon."
# import spacy
#
# nlp = spacy.load("en_core_web_sm")
#
# output = []
# doc = nlp(text)
# for ent in doc.ents:
#     if ent.label_ == 'ORG':
#         output.append(ent.orth_)
# print(output)


# =====================================================================================================================
# 42. How to replace all names of people in the text with ‘UNKNOWN’? Q. Identify and replace all the person names in the news article with UNKNOWN to keep privacy
# news = " Walter was arrested yesterday at Brooklyn for murder. The suspicions and fingerprints pointed to Walter and his friend Pinkman. The arrest was made by inspector Hank"
# import spacy
# from string import punctuation
#
# nlp = spacy.load('en_core_web_sm')
# doc = nlp(news)
#
# # Identifying the entities of category 'PERSON'
# entities = [entity.text for entity in doc.ents if entity.label_ == 'PERSON']
# updated_text = []
#
# for token in doc:
#     if token.text in entities:
#         updated_text.append("UNKNOWN")
#     else:
#         updated_text.append(token.text)
#
# new_text = " ".join(updated_text)
# for char in punctuation:
#     new_text = new_text.replace(' '+char, char)
# print(new_text)


# =====================================================================================================================
# 43. How to visualize the named entities using spaCy? Q. Display the named entities prsent in the given document along with their categories using spacy
# text = " Walter was arrested yesterday at Brooklyn for murder. The suspicions and fingerprints pointed to Walter  and his friend  Pinkman . He is from Paris "
# from spacy import displacy
#
# nlp = spacy.load('en_core_web_sm')
# doc = nlp(text)
# displacy.serve(doc, style='ent', host='localhost')


# =====================================================================================================================
# 44. How to implement dependency parsing ? Q. Find the dependencies of all the words in the given text
# text = "Mark plays volleyball every evening."
#
# nlp = spacy.load('en_core_web_sm')
# doc = nlp(text)
#
# for token in doc:
#     print(token.text, token.dep_)


# =====================================================================================================================
# 45. How to find the ROOT word of any word in a sentence? Q. Find and print the root word / headword of any word in the given sentence
# text = "Mark plays volleyball. Sam is not into sports, he paints a lot"
#
# nlp = spacy.load('en_core_web_sm')
# doc = nlp(text)
#
# for token in doc:
#     print(token.text, token.head)


# =====================================================================================================================
# 46. How to visualize the dependency tree in spaCy? Q. Visualize the dependencies of various tokens of the given text using spaCy
# text = "Mark plays volleyball. Sam is not into sports, he paints a lot"
# from spacy import displacy
#
# nlp = spacy.load('en_core_web_sm')
# doc = nlp(text)
# displacy.serve(doc, style='dep', host='localhost')


# =====================================================================================================================
# 47. How to detect all the Laptop names present in the text? Q.Detect all the Laptop names present in the given  document.
# text = "For my offical use, I prefer lenova. For gaming purposes, I love asus"
# import spacy
#
# nlp = spacy.load("en_core_web_sm")
# from spacy.pipeline import EntityRuler
# from spacy.language import Language
#
#
# # Functions to create patterns of laptop name to match
# def create_versioned(name):
#     return [
#         [{'LOWER': name}],
#         [{'LOWER': {'REGEX': f'({name}\d+\.?\d*.?\d*)'}}],
#         [{'LOWER': name}, {'TEXT': {'REGEX': '(\d+\.?\d*.?\d*)'}}]]
#
#
# def create_patterns():
#     versioned_languages = ['dell', 'HP', 'asus', 'msi', 'Apple', 'HCL', 'sony', 'samsung', 'lenova', 'acer']
#     flatten = lambda l: [item for sublist in l for item in sublist]
#     versioned_patterns = flatten([create_versioned(lang) for lang in versioned_languages])
#
#     lang_patterns = [
#         [{'LOWER': 'dell'}, {'LIKE_NUM': True}],
#         [{'LOWER': 'HP'}],
#         [{'LOWER': 'asus'}, {'LOWER': '#'}],
#         [{'LOWER': 'msi'}, {'LOWER': 'sharp'}],
#         [{'LOWER': 'Apple'}],
#         [{'LOWER': 'HCL'}, {'LOWER': '#'}],
#         [{'LOWER': 'sony'}],
#         [{'LOWER': 'samsung'}],
#         [{'LOWER': 'toshiba'}],
#         [{'LOWER': 'dell'}, {'LOWER': 'inspiron'}],
#         [{'LOWER': 'acer'}, {'IS_PUNCT': True, 'OP': '?'}, {'LOWER': 'c'}],
#         [{'LOWER': 'golang'}],
#         [{'LOWER': 'lenova'}],
#         [{'LOWER': 'HP'}, {'LOWER': 'gaming'}],
#         [{'LOWER': 'Fujitsu'}],
#         [{'LOWER': 'micromax'}],
#     ]
#
#     return versioned_patterns + lang_patterns
#
# @Language.factory('ruler')
# def language_detector(nlp, name):
#     return EntityRuler(nlp)
#
# # Add the Entity Ruler to the pipeline
# ruler = nlp.add_pipe("ruler")
# ruler.add_patterns([{'label': 'laptop', 'pattern': p} for p in create_patterns()])
#
# # Identify the car names now
# doc = nlp(text)
# for ent in doc.ents:
#     print(ent.text, ent.label_)


# =====================================================================================================================
# 48. How to summarize text using gensim ? Q. Extract the summary of the given text based using gensim package based on the TextRank Algorithm.
# original_text = """Studies show that exercise can treat mild to moderate depression as effectively as antidepressant medication—but without the side-effects, of course. As one example, a recent study done by the Harvard T.H. Chan School of Public Health found that running for 15 minutes a day or walking for an hour reduces the risk of major depression by 26%. In addition to relieving depression symptoms, research also shows that maintaining an exercise schedule can prevent you from relapsing.
# Exercise is a powerful depression fighter for several reasons. Most importantly, it promotes all kinds of changes in the brain, including neural growth, reduced inflammation, and new activity patterns that promote feelings of calm and well-being. It also releases endorphins, powerful chemicals in your brain that energize your spirits and make you feel good. Finally, exercise can also serve as a distraction, allowing you to find some quiet time to break out of the cycle of negative thoughts that feed depression.
# Exercise is not just about aerobic capacity and muscle size. Sure, exercise can improve your physical health and your physique, trim your waistline, improve your sex life, and even add years to your life. But that’s not what motivates most people to stay active.
# People who exercise regularly tend to do so because it gives them an enormous sense of well-being. They feel more energetic throughout the day, sleep better at night, have sharper memories, and feel more relaxed and positive about themselves and their lives. And it’s also powerful medicine for many common mental health challenges.
# Regular exercise can have a profoundly positive impact on depression, anxiety, ADHD, and more. It also relieves stress, improves memory, helps you sleep better, and boosts your overall mood. And you don’t have to be a fitness fanatic to reap the benefits. Research indicates that modest amounts of exercise can make a difference. No matter your age or fitness level, you can learn to use exercise as a powerful tool to feel better.
# Ever noticed how your body feels when you’re under stress? Your muscles may be tense, especially in your face, neck, and shoulders, leaving you with back or neck pain, or painful headaches. You may feel a tightness in your chest, a pounding pulse, or muscle cramps. You may also experience problems such as insomnia, heartburn, stomachache, diarrhea, or frequent urination. The worry and discomfort of all these physical symptoms can in turn lead to even more stress, creating a vicious cycle between your mind and body.
# Exercising is an effective way to break this cycle. As well as releasing endorphins in the brain, physical activity helps to relax the muscles and relieve tension in the body. Since the body and mind are so closely linked, when your body feels better so, too, will your mind.Evidence suggests that by really focusing on your body and how it feels as you exercise, you can actually help your nervous system become “unstuck” and begin to move out of the immobilization stress response that characterizes PTSD or trauma.
# Instead of allowing your mind to wander, pay close attention to the physical sensations in your joints and muscles, even your insides as your body moves. Exercises that involve cross movement and that engage both arms and legs—such as walking (especially in sand), running, swimming, weight training, or dancing—are some of your best choices.
# Outdoor activities like hiking, sailing, mountain biking, rock climbing, whitewater rafting, and skiing (downhill and cross-country) have also been shown to reduce the symptoms of PTSD."""
# # !pip install gensim==3.8.3
# from gensim.summarization.summarizer import summarize
#
# # Pass the document along with desired word count to get the summary
# my_summary = summarize(original_text, word_count=100)
# print(my_summary)


# =====================================================================================================================
# 49. How to summarize text based on the LexRank algorithm ? Q. Extract the summary of the given text based on the TextRank Algorithm.
# pip install sumy
# from sumy.summarizers.lex_rank import LexRankSummarizer
#
# # Plain text parsers since we are parsing through text
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
#
# parser = PlaintextParser.from_string(original_text, Tokenizer("english"))
#
# summarizer = LexRankSummarizer()
# my_summary = summarizer(parser.document, 2)
# print(*my_summary)


# =====================================================================================================================
# 50. How to summarize text using Luhn algorithm? Q. Extract the summary of the given text based on the Luhn Algorithm.
# pip install sumy
# from sumy.summarizers.luhn import LuhnSummarizer
#
# # Plain text parsers since we are parsing through text
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
#
# parser = PlaintextParser.from_string(original_text, Tokenizer("english"))
#
# summarizer = LuhnSummarizer()
# my_summary = summarizer(parser.document, 2)
# print(*my_summary)


# =====================================================================================================================
# 51. How to summarize text based on LSA algorithm? Q. Extract the summary of the given text based on the LSA Algorithm.
# import sumy
# from sumy.summarizers.lsa import LsaSummarizer
#
# # Plain text parsers since we are parsing through text
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
#
# parser = PlaintextParser.from_string(original_text, Tokenizer("english"))
#
# summarizer = LsaSummarizer()
# my_summary = summarizer(parser.document, 2)
# print(*my_summary)


# =====================================================================================================================
# 52. How to convert documents into json format ? Q. Covert the given text documents into json format for spacy usage
# text1 = "Netflix has released a new series"
# text2 = "It was shot in London"
# text3 = "It is called Dark and the main character is Jonas"
# text4 = "Adam is the evil character"
#
# import spacy
# import json
#
# nlp = spacy.load("en_core_web_sm")
# doc1 = nlp(text1)
# doc2 = nlp(text2)
# doc3 = nlp(text3)
# doc4 = nlp(text4)
#
# # Import docs_to_json
# from spacy.training import docs_to_json
#
# # Converting into json format
# json_data = docs_to_json([doc1, doc2, doc3, doc4])
# print(json.dumps(json_data, indent=2))


# =====================================================================================================================
# 53. How to build a text classifier with TextBlob ? Q Build a text classifier with available train data using textblob library
# train = [
#     ('I love eating sushi','food-review'),
#     ('This is an amazing place!', 'Tourist-review'),
#     ('Pizza is my all time favorite food','food-review'),
#     ('I baked a cake yesterday, it was tasty', 'food-review'),
#     ("What an awesome taste this sushi has", 'food-review'),
#     ('It is a perfect place for outing', 'Tourist-review'),
#     ('This is a nice picnic spot', 'Tourist-review'),
#     ("Families come out on tours here", 'Tourist-review'),
#     ('It is a beautiful place !', 'Tourist-review'),
#     ('The place was warm and nice', 'Tourist-review')
# ]
# test = [
#     ('The sushi was good', 'food-review'),
#     ('The place was perfect for picnics ', 'Tourist-review'),
#     ("Burgers are my favorite food", 'food-review'),
#     ("I feel amazing!", 'food-review'),
#     ('It is an amazing place', 'Tourist-review'),
#     ("This isn't a very good place", 'Tourist-review')
# ]
#
# from textblob.classifiers import NaiveBayesClassifier
#
# # Training
# cl = NaiveBayesClassifier(train)
#
# # Classify some text
# print(cl.classify("My favorite food is spring rolls"))
# print(cl.classify("It was a cold place for picnic"))
#
# # Printing accuracy of classifier
# print("Accuracy: {0}".format(cl.accuracy(test)))


# =====================================================================================================================
# 54. How to train a text classifier using Simple transformers ? Q. Build and train a text classifier for the given data using simpletransformers library
# train_data = [
#     ["The movie was amazing", 1],
#     ["It was a boring movie", 0],
#     ["I had a great experience", 1],
#     ["I was bored during the movie", 0],
#     ["The movie was great", 1],
#     ["The movie was bad", 0],
#     ["The movie was good", 1]
# ]
# pip install simpletransformers

# from simpletransformers.classification import ClassificationModel, ClassificationArgs
# import pandas as pd
# import logging
# import warnings
#
# warnings.filterwarnings('ignore')
#
# logging.basicConfig(level=logging.INFO)
# transformers_logger = logging.getLogger("transformers")
# transformers_logger.setLevel(logging.WARNING)
#
# # Preparing train data
#
# train_df = pd.DataFrame(train_data)
# train_df.columns = ["text", "labels"]
#
# # Optional model configuration
# model_args = ClassificationArgs(num_train_epochs=1, use_multiprocessing=False)
#
# # Create a ClassificationModel
# model = ClassificationModel("bert", "bert-base-uncased", args=model_args, use_cuda=False)
#
# # Train the model
# model.train_model(train_df)
#
# # Make predictions with the model
# model.args.use_multiprocessing_for_evaluation = False
# model.args.multiprocessing_chunksize = 1
# model.args.dataloader_num_workers = 1
# model.args.process_count = 1
# predictions, raw_outputs = model.predict(["The titanic was a good movie"])
#
# print(predictions)


# =====================================================================================================================
# 55. How to perform text classification using spaCy ? Q. Build a text classifier using spacy that can classify IMDB reviews as positive or negative
# import spacy
#
# nlp = spacy.load("en_core_web_sm")
#
# textcat = nlp.create_pipe("textcat", config={"exclusive_classes": True, "architecture": "simple_cnn"})
# nlp.add_pipe(textcat, last=True)
# textcat = nlp.get_pipe("textcat")
#
# # add label to text classifier
# textcat.add_label("POSITIVE")
# textcat.add_label("NEGATIVE")
#
#
# def load_data(limit=0, split=0.8):
#     """Load data from the IMDB dataset."""
#     # Partition off part of the train data for evaluation
#     train_data, _ = thinc.extra.datasets.imdb()
#     random.shuffle(train_data)
#     train_data = train_data[-limit:]
#     texts, labels = zip(*train_data)
#     cats = [{"POSITIVE": bool(y), "NEGATIVE": not bool(y)} for y in labels]
#     split = int(len(train_data) * split)
#     return (texts[:split], cats[:split]), (texts[split:], cats[split:])
#
#
# # load the IMDB dataset
# print("Loading IMDB data...")
# (train_texts, train_cats), (dev_texts, dev_cats) = load_data()
# train_texts = train_texts[:n_texts]
# train_cats = train_cats[:n_texts]
#
# train_data = list(zip(train_texts, [{"cats": cats} for cats in train_cats]))
#
# # get names of other pipes to disable them during training
# pipe_exceptions = ["textcat", "trf_wordpiecer", "trf_tok2vec"]
# other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]
#
# # Training the text classifier
# with nlp.disable_pipes(*other_pipes):  # only train textcat
#     optimizer = nlp.begin_training()
#     if init_tok2vec is not None:
#         with init_tok2vec.open("rb") as file_:
#             textcat.model.tok2vec.from_bytes(file_.read())
#             print("Training the model...")
#             print("{:^5}\t{:^5}\t{:^5}\t{:^5}".format("LOSS", "P", "R", "F"))
#             batch_sizes = compounding(4.0, 32.0, 1.001)
#             for i in range(n_iter):
#                 losses = {}
#                 # batch up the examples using spaCy's minibatch
#                 random.shuffle(train_data)
#                 batches = minibatch(train_data, size=batch_sizes)
#                 for batch in batches:
#                     texts, annotations = zip(*batch)
#                     nlp.update(texts, annotations, sgd=optimizer, drop=0.2, losses=losses)


# =====================================================================================================================
# 56. How to translate the text (using simpletransformers) ? Q. Translate the given list of texts from English to Dutch using simpletransformers package
# text = [
#     'Our experienced writers travel the world to bring you informative and inspirational features, destination roundups, travel ideas, tips and beautiful photos in order to help you plan your next holiday',
#     'Each part of Germany is different, and there are thousands of memorable places to visit.',
#     "Christmas Markets originated in Germany, and the tradition dates to the Late Middle Ages.",
#     "Garmisch-Partenkirchen is a small town in Bavaria, near Germany’s highest mountain Zugspitze, which rises to 9,718 feet (2,962 meters)",
#     "It’s one of the country’s top alpine destinations, extremely popular during the winter",
#     "In spring, take a road trip through Bavaria and enjoy the view of the dark green Alps and the first alpine wildflowers. "]
#
# # !pip install simpletransformers
#
# # Import the model
# from simpletransformers.seq2seq import Seq2SeqModel
#
# # Setting desired arguments
# my_args = {"train_batch_size": 2,
#            "num_train_epochs": 10,
#            "save_eval_checkpoints": False,
#            "save_model_every_epoch": False,
#            "evaluate_during_training": True,
#            "evaluate_generated_text": True}
#
# # Instantiating the model
# my_model = Seq2SeqModel(encoder_decoder_name="Helsinki-NLP/opus-mt-en-de", encoder_decoder_type="marian", args=my_args,
#                         use_cuda=False)
#
# # translating the text
#
# print(my_model.predict(text))


# =====================================================================================================================
# 57. How to create a Question-Answering system from given context? Q. Build a Question Answering model that answers questions from the given context using transformers package
# context = """ Harry Potter is the best book series according to many people. Harry Potter was written by JK.Rowling .
# It is afantasy based novel that provides a thrilling experience to readers."""
#
# question = "What is Harry Potter ?"
#
# # !pip install transformers
# from transformers import pipeline
#
# # Get thetask-specific pipeline
# my_model = pipeline(task="question-answering")
#
# context = r""" Harry Potter is the best book series according to many people. Harry Potter was written by JK.Rowling .
# It is afantasy based novel that provides a thrilling experience to readers."""
#
# # Pass the question and context to the model to obtain answer
# print(my_model(question="What is Harry Potter ?", context=context))
# print(my_model(question="Who wrote Harry Potter ?", context=context))


# =====================================================================================================================
# 58. How to do text generation starting from a given piece of text? Q. Generate text based on the the starting provided.
# starting = "It was a bright"
#
# from transformers import pipeline
#
# # Get the task-specific pipeline
# my_model = pipeline(task="text-generation")
#
# # Pass the starting sequence as input to generate text
# print(my_model(starting)[0]['generated_text'])


# =====================================================================================================================
# 59. How to classify a text as positive or negative sentiment with transformers? Q. Find out whether a given text is postive or negative sentiment along with score for predictions
# text1 = "It is a pleasant day, I am going for a walk"
# text2 = "I have a terrible headache"
# from transformers import pipeline
#
# # Get the task specific pipeline
# my_model = pipeline("sentiment-analysis")
#
# # Predicting the sentiment with score
# print(my_model(text1))
# print(my_model(text2))


# =========================================== PRIVIOUS EXAM ===========================================================
# =====================================================================================================================
# =====================================================================================================================


# =====================================================================================================================
# sm22_1.1. Define s as a text. Write expressions for finding all words in s that contain the sequence of letters pt.
# The result should be in the form of a list of words: ['word1', 'word2',...]

# from nltk.book import text2
# print([w for w in text2 if 'pt' in w])


# =====================================================================================================================
# sm22_1.2. Define a function percent(word, text) that calculates how often a given word occurs in a text and expresses
# the result as a percentage

# from nltk.book import FreqDist, text1
#
#
# # C1: ignore punctuation
# # Remove Enclitics word like I'm, I'll, you're, It's, I've,... ==> only 1 word
# def vocab_size(text):
#     return len([w for w in text if w.isalpha() and w.lower not in ("d", "ll", "m", "re", "s", "t", "ve")])
#
#
# def percent(word, text):
#     """
#     Returns the percentage that a given word comprises in a text.
#     """
#     word_count = len([w for w in text if w.lower() == word.lower()])
#     total_words = vocab_size(text)
#     return 100 * word_count / total_words
#
#
# print(f"\nIf ignore punctuation: {percent('whale', text1):.4f}%")
#
#
# # C2: include all
# def percent(word, text):
#     return FreqDist(text)[word] / float(len(text)) * 100
#
#
# print(f"If include all: {percent('whale', text1):.4f}%")


# =====================================================================================================================
# sm22_1.3. Write a python NLTK program to split the text sentence/paragraph into a list of words.

# import nltk
#
# text = '''Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station.'''
#
# print("\nOriginal string:")
# print(text)
# token_text = nltk.sent_tokenize(text)
# print("\nSentence-tokenized copy in a list:")
# print(token_text)
# print("\nRead the list:")
# for s in token_text:
#     print(s)

# =====================================================================================================================
# sm22_1.4. Extract the Verb Phrases from the given text

# text = "I may bake a cake for my birthday. The talk will introduce reader about Use of baking"
# # Regex pattern to identify verb phrase
# # !pip install textacy
# import textacy
# from spacy.util import filter_spans
#
# # Regex pattern to identify verb phrase
# verb_pattern = [{"POS": "AUX", "OP": "*"}, {"POS": "VERB", "OP": "*"}, {"POS": "ADV", "OP": "*"},
#                 {"POS": "VERB", "OP": "+"}]
# doc = textacy.make_spacy_doc(text, lang='en_core_web_lg')
#
# # Finding matches
# verb_phrases = textacy.extract.token_matches(doc, verb_pattern)
# # Avoid repetition
# verb_phrases = filter_spans(verb_phrases)
#
# # Print all Verb Phrase
# for chunk in verb_phrases:
#     print(chunk.text)


# =====================================================================================================================
# sm22_2.1. Define s as a text. Write expressions for finding all words in s that all lowercase letters.
# # The result should be in the form of a list of words: ['word1', 'word2',...]
# from nltk.book import text6
#
# # Having all lowercase letters except for an initial capital (i.e., titlecase)
# print([w for w in text6 if w.istitle()])
# # print([w for w in text6 if w.islower()])


# =====================================================================================================================
# sm22_2.2. Find all the four-letter words in the Chat Corpus (text5). With the help of a frequency
# distribution (FreqDist), show these words in decreasing order of frequency.

# from nltk.book import FreqDist, text5
#
# four_letter_fd = FreqDist([w for w in text5 if len(w) == 4])
# print(four_letter_fd.most_common())


# =====================================================================================================================
# sm22_2.3. Write a Python nktl program to create a list of words from a given string

# from nltk.tokenize import word_tokenize
# text = "Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station."
# print("\nOriginal string:")
# print(text)
# print("\nList of words:")
# print(word_tokenize(text))


# =====================================================================================================================
# sm22_2.4. Merge the first name and last name as single token in the given sentence.

# import spacy
# import nltk
# nlp = spacy.load('en_core_web_sm')
# text = "Robert Langdon is a famous character in various books and movies"
# # document = nlp(text)
# # tokens = nltk.word_tokenize(text)
# # person = []
# # for ent in document.ents:
# #     print(ent.label_, ent.text)
# #     if ent.label_ == 'PERSON':
# #         person.append(ent)
# # print(person)
#
# doc = nlp(text)
#
# with doc.retokenize() as retokenizer:
#     start = 0
#     for idx, token in enumerate(doc):
#         if token.ent_type_ == 'PERSON':
#             continue
#         else:
#             if start == idx:
#                 start = idx + 1
#                 continue
#             retokenizer.merge(doc[start:idx])
#             start = idx+1
#     if start != len(doc):
#         retokenizer.merge(doc[start:])
#
# for token in doc:
#     print(token.text)


# =====================================================================================================================
# sm22_re1.1. Define s as a text. Write expressions for finding all words in s that ending in "ize".
# The result should be in the form of a list of words: ['word1', 'word2',...]

# from nltk.book import text2
# print([w for w in text2 if w.endswith('ize')])


# =====================================================================================================================
# sm22_re1.2. Write a function that finds the 50 most frequently occurring words of a text that are not stopwords

# from nltk.corpus import stopwords
# from nltk.corpus import brown
#
#
# def flatten_to_list(text):
#     # if list ==> flatten to 1d
#     if type(text[0]) == list:
#         text = [i for s in text for i in s]
#     # if string ==> convert to list of word
#     elif type(text) == str:
#         text = text.split()
#     return list(text)
#
#
# def find_most_frequent_non_stopwords(text, n=50, lang='english'):
#     text = flatten_to_list(text)
#
#     fd = nltk.FreqDist(w.lower() for w in text if w.lower().isalpha() and w.lower() not in stopwords.words('english'))
#     return fd.most_common(n)
#
#
# print(find_most_frequent_non_stopwords(brown.words(), 50), end='')


# =====================================================================================================================
# sm22_re1.3. Write a Python NLTK program to split all punctuation into separate tokens.

# from nltk.tokenize import WordPunctTokenizer
# import nltk
# text = "Reset your password if you just can't remember your old one."
# print("\nOriginal string:")
# print(text)
# result = WordPunctTokenizer().tokenize(text)
# print("\nSplit all punctuation into separate tokens:")
# print(result)
# print(nltk.wordpunct_tokenize(text))


# =====================================================================================================================
# sm22_re1.4. Find the similarity between any two text documents.

# word1 = "John lives in Canada"
# word2 = "James lives in America, though he's not from there"
# nlp = spacy.load('en_core_web_lg')
# token1 = nlp(word1)
# token2 = nlp(word2)
#
# # Use similarity() function of tokens
# print(f"Similarity between text 1 and text 2 is {token1.similarity(token2)}")


# =====================================================================================================================
# sm22_re2.1. Define s as a text. Write expressions for finding all words in s that contain the letter z.
# The result should be in the form of a list of words: ['word1', 'word2',...]

# nltk.download('inaugural')
# nltk.download('nps_chat')
# nltk.download('gutenberg')
# nltk.download('genesis')
# nltk.download('webtext')
# nltk.download('treebank')

# from nltk.book import text6
# print([w for w in text6 if 'z' in w])

# =====================================================================================================================
# sm22_re2.2. Write a function to find all words that occur at least three times in the Brown Corpus

# from nltk.corpus import brown
#
#
# def find_words_occurring_thrice_or_more():
#     cfd = nltk.FreqDist(w.lower() for w in brown.words())
#     wordtypes = set(w.lower() for w in brown.words())
#     return [w for w in wordtypes if cfd[w] >= 3]
#
#
# three_or_more = find_words_occurring_thrice_or_more()
# print(three_or_more[:10])


# =====================================================================================================================
# sm22_re2.3. Write a Python NLTK program to tokenize words, sentence wise.

# from nltk.tokenize import sent_tokenize, word_tokenize
# text = "Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station."
# print("\nOriginal string:")
# print(text)
# print("\nTokenize words sentence wise:")
# result = [word_tokenize(t) for t in sent_tokenize(text)]
# print(result)
# print("\nRead the list:")
# for s in result:
#     print(s)


# =====================================================================================================================
# sm22_re2.4. Replace the pronouns in below text by the respective object names.

# text = " My sister has a dog and she loves him"
# # !pip install spacy==2.0.12
# # !pip install https://github.com/huggingface/neuralcoref-models/releases/download/en_coref_md-3.0.0/en_coref_md-3.0.0.tar.gz
# import en_coref_md
#
# # Add it to the pipeline
# nlp = en_coref_md.load()
# # nlp = spacy.load('en_core_web_sm')
#
# # Printing the coreferences
# doc1 = nlp('My sister has a dog. She loves him.')
# for cluster in doc1._.coref_clusters:
#     print(cluster.mentions)


# =====================================================================================================================
# sp22_1.1. Define a function percent(word, text) that calculates how often a given word occurs in a text and expresses
# the result as a percentage.

# from nltk.book import FreqDist, text1
#
#
# # C1: ignore punctuation
# # Remove Enclitics word like I'm, I'll, you're, It's, I've,... ==> only 1 word
# def vocab_size(text):
#     return len([w for w in text if w.isalpha() and w.lower not in ("d", "ll", "m", "re", "s", "t", "ve")])
#
#
# def percent(word, text):
#     """
#     Returns the percentage that a given word comprises in a text.
#     """
#     word_count = len([w for w in text if w.lower() == word.lower()])
#     total_words = vocab_size(text)
#     return 100 * word_count / total_words
#
#
# print(f"\nIf ignore punctuation: {percent('whale', text1):.4f}%")
#
#
# # C2: include all
# def percent(word, text):
#     return FreqDist(text)[word] / float(len(text)) * 100
#
#
# print(f"If include all: {percent('whale', text1):.4f}%")


# =====================================================================================================================
# sp22_1.2. Write a function that takes a text and a vocabulary as its arguments and returns the set of words that
# appear in the text but not in the vocabulary. Both arguments can be represented as a lists of strings.

# from nltk import word_tokenize
#
#
# def return_vocab_not_in_text(text, vocab):
#     if type(text) == str:
#         text = word_tokenize(text)
#     else:
#         assert isinstance(text,
#                           list), "Argument `text` must be a list or a string"
#
#         # if vocab is a str
#     if type(vocab) == str:
#         vocab = word_tokenize(vocab)
#     else:
#         assert isinstance(vocab,
#                           list), "Argument `vocab` must be a list or a string"
#
#     return set(text).difference(set(vocab))
#
#
# deep_thought = ("When I was a kid my favorite relative was Uncle Caveman. "
#                 "After school we'd all go play in his cave, "
#                 "and every once in a while he would eat one of us. "
#                 "It wasn't until later that I found out that Uncle Caveman "
#                 "was a bear.")
# vocab = ["'d", 'was', '.', 'play', 'school', 'favorite', 'found',
#          'kid', 'all', 'once', 'Caveman', 'Uncle', 'cave',
#          'while', 'relative', "n't", 'until', 'out', 'we', 'a', 'my',
#          'After', 'that', 'every', 'later', 'and', 'go', 'in', 'of',
#          'one', 'bear', 'When', 'would', 'eat']
# dt_words = word_tokenize(deep_thought)
#
# print(return_vocab_not_in_text(dt_words, vocab))


# =====================================================================================================================
# sp22_1.3. Write a Python NLTK program to split all punctuation into separate tokens.

# from nltk.tokenize import WordPunctTokenizer
# import nltk
# text = "Reset your password if you just can't remember your old one."
# print("\nOriginal string:")
# print(text)
# result = WordPunctTokenizer().tokenize(text)
# print("\nSplit all punctuation into separate tokens:")
# print(result)
# print(nltk.wordpunct_tokenize(text))


# =====================================================================================================================
# sp22_1.4. Find the similarity between any two text documents.

# word1 = "John lives in Canada"
# word2 = "James lives in America, though he's not from there"
# nlp = spacy.load('en_core_web_lg')
# token1 = nlp(word1)
# token2 = nlp(word2)
#
# # Use similarity() function of tokens
# print(f"Similarity between text 1 and text 2 is {token1.similarity(token2)}")


# =====================================================================================================================
# sp22_2.1. Find all the four-letter words in the Chat Corpus (text5). With the help of a frequency distribution
# (FreqDist), show these words in decreasing order of frequency.

# from nltk.book import FreqDist, text5
#
# four_letter_fd = FreqDist([w for w in text5 if len(w) == 4])
# print(four_letter_fd.most_common())


# =====================================================================================================================
# sp22_2.2. Write code to print out an index for a lexicon, allowing someone to look up words according to their
# meanings (or their pronunciations; whateven properties are contained in the lexical entries).

# def insert(trie, key, value):
#     if key:
#         first, rest = key[0], key[1:]
#         if first not in trie:
#             trie[first] = {}
#         insert(trie[first], rest, value)
#     else:
#         trie['value'] = value
#
#
# def lookup(trie, key):
#     if key:
#         first, rest = key[0], key[1:]
#         if first not in trie:
#             return 'no result'
#         return lookup(trie[first], rest)
#     else:
#         return trie['value']
#
#
# trie = {}
# insert(trie, 'abcd', 'Definition for abcd')
# insert(trie, 'efgh', 'Definition for efgh')
# insert(trie, 'abcdefgh', 'Definition for abcdefgh')
#
# import json
#
# trie = dict(trie)
# print(json.dumps(trie, indent=2))
# search_key = 'abcdefgh'
# print('Definition of "{}": {}'.format(search_key, lookup(trie, search_key)))


# =====================================================================================================================
# sp22_2.3. Write a Python NLTK program to tokenize words, sentence wise.

# from nltk.tokenize import sent_tokenize, word_tokenize
# text = "Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station."
# print("\nOriginal string:")
# print(text)
# print("\nTokenize words sentence wise:")
# result = [word_tokenize(t) for t in sent_tokenize(text)]
# print(result)
# print("\nRead the list:")
# for s in result:
#     print(s)


# =====================================================================================================================
# sp22_2.4. Replace the pronouns in the below text by the respective object names.

# text = " My sister has a dog and she loves him"
# # !pip install spacy==2.0.12
# # !pip install https://github.com/huggingface/neuralcoref-models/releases/download/en_coref_md-3.0.0/en_coref_md-3.0.0.tar.gz
# import en_coref_md
#
# # Add it to the pipeline
# nlp = en_coref_md.load()
# # nlp = spacy.load('en_core_web_sm')
#
# # Printing the coreferences
# doc1 = nlp('My sister has a dog. She loves him.')
# for cluster in doc1._.coref_clusters:
#     print(cluster.mentions)


# =====================================================================================================================
# Write a Python NLTK program to tokenize sentences in languages other than English.

# text = '''NLTK ist Open Source Software. Der Quellcode wird unter den Bedingungen der Apache License Version 2.0 vertrieben.
# Die Dokumentation wird unter den Bedingungen der Creative Commons-Lizenz Namensnennung - Nicht kommerziell - Keine
# abgeleiteten Werke 3.0 in den Vereinigten Staaten verteilt.
# '''
# print("\nOriginal string:")
# print(text)
# from nltk.tokenize import sent_tokenize
#
# token_text = sent_tokenize(text, language='german')
# print("\nSentence-tokenized copy in a list:")
# print(token_text)
# print("\nRead the list:")
# for s in token_text:
#     print(s)

# =====================================================================================================================
# Write a Python NLTK program to tokenize a twitter text.

# from nltk.tokenize import TweetTokenizer
# tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)
# tweet_text = "NoSQL introduction - w3resource http://bit.ly/1ngHC5F  #nosql #database #webdev"
# print("\nOriginal Tweet:")
# print(tweet_text)
# result = tknzr.tokenize(tweet_text)
# print("\nTokenize a twitter text:")
# print(result)


# =====================================================================================================================
# Write a Python NLTK program to remove Twitter username handles from a given twitter text.

# from nltk.tokenize import TweetTokenizer
# tknzr = TweetTokenizer(strip_handles=True)
# tweet_text = "@abcd @pqrs NoSQL introduction - w3resource http://bit.ly/1ngHC5F  #nosql #database #webdev"
# print("\nOriginal Tweet:")
# print(tweet_text)
# result = tknzr.tokenize(tweet_text)
# print("\nTokenize a twitter text:")
# print(result)


# =====================================================================================================================
# Write a Python NLTK program that will read a given text through each line and look for sentences. Print each sentence and divide two sentences with "=============="

# import nltk.data
# text = '''
# Mr. Smith waited for the train. The train was late.
# Mary and Samantha took the bus. I looked for Mary and
# Samantha at the bus station.
# '''
# print("\nOriginal Tweet:")
# print(text)
# sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
# print('\n==============\n'.join(sent_detector.tokenize(text.strip())))


# =====================================================================================================================
# Write a Python NLTK program to find parenthesized expressions in a given string and divides the string into a sequence of substrings.

# from nltk.tokenize import SExprTokenizer
# text = '(a b (c d)) e f (g)'
# print("\nOriginal Tweet:")
# print(text)
# print(SExprTokenizer().tokenize(text))
# text = '(a b) (c d) e (f g)'
# print("\nOriginal Tweet:")
# print(text)
# print(SExprTokenizer().tokenize(text))
# text = '[(a b (c d)) e f (g)]'
# print("\nOriginal Tweet:")
# print(text)
# print(SExprTokenizer().tokenize(text))
# print(text)
# print(SExprTokenizer().tokenize(text))
# text = '{a b {c d}} e f {g}'
# print("\nOriginal Tweet:")
# print(text)
# print(SExprTokenizer().tokenize(text))


# =====================================================================================================================
# Write a Python NLTK program to list down all the corpus names.

# import nltk.corpus
# dir(nltk.corpus)
# print("\nAvailable corpus names:")
# print(dir(nltk.corpus))


# =====================================================================================================================
# Write a Python NLTK program to get a list of common stop words in various languages in Python.

# from nltk.corpus import stopwords
# print(stopwords.fileids())


# =====================================================================================================================
# Write a Python NLTK program to check the list of stopwords in various languages.

# import nltk
# from nltk.corpus import stopwords
# result = set(stopwords.words('english'))
# print("List of stopwords in English:")
# print(result)
# print("\nList of stopwords in Arabic:")
# result = set(stopwords.words('arabic'))
# print(result)
# print("\nList of stopwords in Azerbaijani:")
# result = set(stopwords.words('azerbaijani'))
# print(result)
# print("\nList of stopwords in Danish:")
# result = set(stopwords.words('danish'))
# print(result)
# print("\nList of stopwords in Dutch:")
# result = set(stopwords.words('dutch'))
# print(result)
# print("\nList of stopwords in Finnish:")
# result = set(stopwords.words('finnish'))
# print(result)
# print("\nList of stopwords in French:")
# result = set(stopwords.words('french'))
# print(result)
# print("\nList of stopwords in German:")
# result = set(stopwords.words('german'))
# print(result)
# print("\nList of stopwords in Greek:")
# result = set(stopwords.words('greek'))
# print(result)
# print("\nList of stopwords in Hungarian:")
# result = set(stopwords.words('hungarian'))
# print(result)
# print("\nList of stopwords in Indonesian:")
# result = set(stopwords.words('indonesian'))
# print(result)
# print("\nList of stopwords in Italian:")
# result = set(stopwords.words('italian'))
# print(result)
# print("\nList of stopwords in Kazakh:")
# result = set(stopwords.words('kazakh'))
# print(result)
# print("\nList of stopwords in Nepali:")
# result = set(stopwords.words('nepali'))
# print(result)
# print("\nList of stopwords in Norwegian:")
# result = set(stopwords.words('norwegian'))
# print(result)
# print("\nList of stopwords in Portuguese:")
# result = set(stopwords.words('portuguese'))
# print(result)
# print("\nList of stopwords in Romanian:")
# result = set(stopwords.words('romanian'))
# print(result)
# print("\nList of stopwords in Russian:")
# result = set(stopwords.words('russian'))
# print(result)
# print("\nList of stopwords in Spanish:")
# result = set(stopwords.words('spanish'))
# print(result)
# print("\nList of stopwords in Swedish:")
# result = set(stopwords.words('swedish'))
# print(result)
# print("\nList of stopwords in Turkish:")
# result = set(stopwords.words('turkish'))
# print(result)


# =====================================================================================================================
# Write a Python NLTK program to remove stop words from a given text.

# from nltk.corpus import stopwords
# stoplist = stopwords.words('english')
# text = '''
# In computing, stop words are words which are filtered out before or after
# processing of natural language data (text). Though "stop words" usually
# refers to the most common words in a language, there is no single universal
# list of stop words used by all natural language processing tools, and
# indeed not all tools even use such a list. Some tools specifically avoid
# removing these stop words to support phrase search.
# '''
# print("\nOriginal string:")
# print(text)
# clean_word_list = [word for word in text.split() if word not in stoplist]
# print("\nAfter removing stop words from the said text:")
# print(clean_word_list)

# =====================================================================================================================
# Write a Python NLTK program to omit some given stop words from the stopwords list.

# import nltk
# from nltk.corpus import stopwords
# result = set(stopwords.words('english'))
# print("List of stopwords in English:")
# print(result)
# print("\nOmit - 'again', 'once' and 'from':")
# stop_words = set(stopwords.words('english')) - {'again', 'once', 'from'}
# print("\nList of fresh stopwords in English:")
# print (stop_words)

# =====================================================================================================================
# Write a Python NLTK program to find the definition and examples of a given word using WordNet.

# from nltk.corpus import wordnet
# syns = wordnet.synsets("fight")
# print("Defination of the said word:")
# print(syns[0].definition())
# print("\nExamples of the word in use::")
# print(syns[0].examples())


# =====================================================================================================================
# Write a Python NLTK program to find the sets of synonyms and antonyms of a given word.

# from nltk.corpus import wordnet
# synonyms = []
# antonyms = []
#
# for syn in wordnet.synsets("end"):
#     for l in syn.lemmas():
#         synonyms.append(l.name())
#         if l.antonyms():
#             antonyms.append(l.antonyms()[0].name())
# print("\nSet of synonyms of the said word:")
# print(set(synonyms))
# print("\nSet of antonyms of the said word:")
# print(set(antonyms))


# =====================================================================================================================
# Write a Python NLTK program to get the overview of the tagset, details of a specific tag in the tagset and details on several related tagsets, using regular expression.

# import nltk
# print("Overview of the tagset:")
# print(nltk.help.brown_tagset())
# print("\nDetails of a specific tag :")
# print(nltk.help.brown_tagset(r'NNS'))
# print("\nDetails on several related tagsets, using regular expression:")
# nltk.help.brown_tagset(r'WP*')


# =====================================================================================================================
# Write a Python NLTK program to compare the similarity of two given nouns.

# from nltk.corpus import wordnet
# print("\nComparing ship anb boat:")
# n1 = wordnet.synset('ship.n.01')
# n2 = wordnet.synset('boat.n.01')
# print(n1.wup_similarity(n2))
# print("\nComparing bus anb boat:")
# n1 = wordnet.synset('bus.n.01')
# n2 = wordnet.synset('boat.n.01')
# print(n1.wup_similarity(n2))
# print("\nComparing red anb greed:")
# n1 = wordnet.synset('red.n.01')
# n2 = wordnet.synset('green.n.01')
# print(n1.wup_similarity(n2))


# =====================================================================================================================
# Write a Python NLTK program to compare the similarity of two given verbs.

# from nltk.corpus import wordnet
# print("\nComparing go anb return:")
# v1 = wordnet.synset('go.v.01')
# v2 = wordnet.synset('return.v.01')
# print(v1.wup_similarity(v2))
#
# print("\nComparing buy anb sell:")
# v1 = wordnet.synset('buy.v.01')
# v2 = wordnet.synset('sell.v.01')
# print(v1.wup_similarity(v2))
#
# print("\nComparing begin anb start:")
# v1 = wordnet.synset('begin.v.01')
# v2 = wordnet.synset('start.v.01')
# print(v1.wup_similarity(v2))


# =====================================================================================================================
# Write a Python NLTK program to find the number of male and female names in the names corpus. Print the first 10 male and female names.

# from nltk.corpus import names
# print("\nNumber of male names:")
# print (len(names.words('male.txt')))
# print("\nNumber of female names:")
# print (len(names.words('female.txt')))
# male_names = names.words('male.txt')
# female_names = names.words('female.txt')
# print("\nFirst 10 male names:")
# print (male_names[0:15])
# print("\nFirst 10 female names:")
# print (female_names[0:15])


# =====================================================================================================================
# Write a Python NLTK program to print the first 15 random combine labeled male and labeled female names from names corpus.

# from nltk.corpus import names
# import random
#
# male_names = names.words('male.txt')
# female_names = names.words('female.txt')
#
# labeled_male_names = [(str(name), 'male') for name in male_names]
# labeled_female_names = [(str(name), 'female') for name in female_names]
#
# # combine labeled male and labeled female names
# labeled_all_names = labeled_male_names + labeled_female_names
#
# # shuffle the labeled names array
# random.shuffle(labeled_all_names)
#
# print("First 15 random labeled combined names:")
# print(labeled_all_names[:15])


# =====================================================================================================================
# Write a Python NLTK program to extract the last letter of all the labeled names and create a new array with the last letter of each name and the associated label.

# from nltk.corpus import names
# import random
# male_names = names.words('male.txt')
# female_names = names.words('female.txt')
# labeled_male_names = [(str(name), 'male') for name in male_names]
# labeled_female_names = [(str(name), 'female') for name in female_names]
# # combine labeled male and labeled female names
# all_labeled_names = labeled_male_names + labeled_female_names
# feature_set = [(name[-1], gender) for (name, gender) in all_labeled_names]
# print("\nFirst 15 labeled names:")
# print((all_labeled_names[:15]))
# print("\nLast letter of all the labeled names with the associated label:")
# print((feature_set[:15]))
