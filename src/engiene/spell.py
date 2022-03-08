class Spelling():
    def __init__(self):
        self.lower_vowel = {'a', 'â', 'e', 'ê', 'ı', 'î', 'i', 'o', 'ô', 'ö', 'u', 'û', 'ü'}
        self.SPELL_SLICER = (('001000', 5), ('000100', 5), ('01000', 4), ('00100', 4), ('00010', 4), ('1000', 3), ('0100', 3),
                    ('0011', 3), ('0010', 3), ('011', 2), ('010', 2), ('100', 2), ('10', 1), ('11', 1))


    def to_lower(self,word):
        tolower_text = (word.replace('İ', 'i'))
        tolower_text = (tolower_text.replace('I', 'ı'))
        return tolower_text.lower()


    def wordtoten(self,word: str):
        """    Gelen kelimeyi, sesli harfler "1", sessiz harfler "0" olmak üzere sayıya çevirir.    :param word: str    :return: str    """
        wtt = ''

        for ch in word:
            if ch in self.lower_vowel:
                wtt += '1'
            else:
                wtt += '0'
        return wtt

    def spellword(self,word: str):
        word = self.to_lower(word)
        syllable_list = []
        tenword = self.wordtoten(word)
        len_spell = tenword.count('1')

        for i in range(tenword.count('1')):
            for x, y in self.SPELL_SLICER:
                if tenword.startswith(x):
                    syllable_list.append(word[:y])
                    word = word[y:]
                    tenword = tenword[y:]
                    break

        if tenword == '0':
            syllable_list[-1] = syllable_list[-1] + word
        elif word:
            syllable_list.append(word)

        if len(syllable_list) != len_spell:
            return False

        return syllable_list