import spacy
from spacy.tokens import DocBin
from spacy.attrs import ORTH, NORM
from spacy import displacy

from interface.i_nlp_service import INlpService


class NlpService(INlpService):
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        print(self.nlp.get_pipe("ner").labels)

    def get_intent(self, string) -> str:
        doc = self.nlp(string)
        print(displacy.render(doc, style="ent"))
        for token in doc:
            print(token.head.text, token.text, token.pos_, token.dep_)
            print(
                token.text,
                token.lemma_,
                token.pos_,
                token.tag_,
                token.dep_,
                token.shape_,
                token.is_alpha,
                token.is_stop,
            )
        for sent in doc.sents:
            print([w.text for w in sent if w.dep_ == "ROOT" or w.dep_ == "pobj"])
