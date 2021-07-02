from ginza import *
import spacy

class Processing():
    DEFAULT_LANG = 'ja_ginza'
    def __init__(self, *args, **kwargs):
        """
        
        """
        lang = kwargs['lang'] if 'lang' in kwargs else Processing.DEFAULT_LANG 
        self.nlp = spacy.load(lang) # Japanese lang model named GiNZA.

    def get_pipeline(self):
        pipelines = []
        for task in self.nlp.pipeline:
            pipelines.append(task)
        return pipelines


    def analyze(self, word:str):
        return self.nlp(word)
