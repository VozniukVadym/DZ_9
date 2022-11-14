import string
class TextProcessor():
    def __init__(self, stroka, znak):
        self.stroka=stroka
        self._znak=znak
    def get_clean_string(self):
        for i in string.punctuation:
            if i in self.stroka:
                self.stroka = self.stroka.replace(i, '')
        return self.stroka
    def _is_punktiantian(self):
        if self._znak in string.punctuation:
            return True
        else:
            return False

strok=TextProcessor('A ja, pokazhu, otkuda na  Belaruss - napadenie','a')
print(strok.get_clean_string())
print(strok._is_punktiantian())

class TextLoader():
    def __init__(self):
        self._textprocessor = TextProcessor('jhjhb','n')
    def set_clean_text(self):
        self.clean_string=TextProcessor.get_clean_string(self._textprocessor)
        print(self.clean_string)
        return self.clean_string
    @property
    def clean_text(self):
        print('clean text'+self.clean_string)
        return self.clean_string
TextLoader.set_clean_text('sdfs')

'''Далі не розібрався.'''