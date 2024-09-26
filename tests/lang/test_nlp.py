import os, sys, unittest

# It is required when you'll run the unittest.
if __name__ == '__main__':
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    if path not in sys.path:
        sys.path.append(path)

from lang.nlp import (
    Processing,
)


class ProcessingTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pipeline(self):
        p = Processing(Processing.DEFAULT_LANG)
        pipelines = p.get_pipeline()
        self.assertEqual('tok2vec', pipelines[0][0]) # part of speech tagging
        self.assertEqual('parser', pipelines[1][0]) # dependency parsing as sequence labeling
        self.assertEqual('ner', pipelines[2][0])    # Named Entity Recognitio
        self.assertEqual('morphologizer', pipelines[3][0]) # Named Entity Recognitio
        self.assertEqual('compound_splitter', pipelines[4][0]) # Named Entity Recognitio
        self.assertEqual('bunsetu_recognizer', pipelines[5][0]) # Named Entity Recognitio


    def test_analyze(self):
        p = Processing()
        ret = p.analyze("今日の午後は、突然降り出した雨の影響で、予定が大幅に狂ってしまった。")
        i = 0
        map = {}
        list = []
        for token in ret:
            list.append(token.text)
            tokenset = {'text': token.text, 'pos_': token.pos_, 'dep_':token.dep_ }
            map[str(i)] = tokenset
            i += 1
        self.assertEqual(23, len(ret))
        self.assertEqual(23, len(list))


if __name__ == '__main__':
    unittest.main()
