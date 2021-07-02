import os, sys, time, unittest

module_path  = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

class ProcessingTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pipeline(self):
        p = Processing(Processing.DEFAULT_LANG)
        pipelines = p.get_pipeline()
        self.assertEqual('tagger', pipelines[0][0]) # part of speech tagging
        self.assertEqual('parser', pipelines[1][0]) # dependency parsing as sequence labeling
        self.assertEqual('ner', pipelines[2][0])    # Named Entity Recognitio
        self.assertEqual('CompoundSplitter', pipelines[3][0])

    def test_analyze(self):
        p = Processing()
        ret = p.analyze("今日の午後は、突然降り出した雨の影響で、予定が大幅に狂ってしまった。")
        i = 0
        map = {}
        for token in ret:
            tokenset = {'text': token.text, 'pos_': token.pos_, 'dep_':token.dep_ }
            map[str(i)] = tokenset
            i += 1
        return map
        print(ret)
        self.assertEqual(23, len(ret))


if __name__ == '__main__':
    if module_path not in sys.path:
        sys.path.append(module_path)
    from lang.nlp import (
        Processing,
    )
    unittest.main()
