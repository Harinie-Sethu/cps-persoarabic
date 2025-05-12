from globals import GLOBALS
from helpers import load_common_map

class UnifiedParser:
    def __init__(self, lang):
        GLOBALS.currLang = lang
        self.mappings = load_common_map("common.map")
        self.inverse_map = {v[lang]: k for k, v in self.mappings.items() if v[lang] != "-"}

    def parse_word(self, word):
        phonemes = []
        for char in word:
            cps = self.inverse_map.get(char, None)
            if cps:
                phonemes.append(cps)
            else:
                phonemes.append('UNK')  # Handle unknown characters explicitly
        return phonemes

    def parse_words_from_file(self, filepath):
        word_phoneme_dict = {}
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                word = line.strip()
                if word:
                    word_phoneme_dict[word] = self.parse_word(word)
        return word_phoneme_dict
