from ginza import *
import spacy

class Processing():

    def __init__(self, *args, **kwargs):
        """
        
        """
        pass

    def example(self):
        nlp = spacy.load("ja_ginza") # Japanese lang model named GiNZA.
        doc = nlp("今日の午後は、突然降り出した雨の影響で、予定が大幅に狂ってしまった。")
        print(doc.text)
        for token in doc:
            print(token.text, token.pos_, token.dep_)
        return ''
