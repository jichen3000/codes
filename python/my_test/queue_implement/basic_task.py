import os, json, time, uuid, collections

from nltk.corpus import stopwords

COMMON_WORDS = set(stopwords.words('english'))
DATA_DIRECTORY = os.path.join(os.path.dirname(__file__), 'data')