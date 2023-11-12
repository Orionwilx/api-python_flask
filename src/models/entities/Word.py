class Word():

    def __init__(self,id,word=None,accept=None) -> None:
        self.id = id
        self.word = word
        self.accept = accept

    def to_JSON(self):
        return {
            "id":self.id,
            "word":self.word,
            "accept":self.accept
        }