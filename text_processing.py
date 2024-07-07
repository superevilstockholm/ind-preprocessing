# Ini adalah library untuk mengolah teks agar dapat di baca oleh mesin
import re
import pandas as pd

class PreProcessing:
    @staticmethod
    def clean_string(string):
        pattern = r"[^A-Za-z\s]"
        clean_string = re.sub(pattern, "", string.lower())
        return clean_string

    @staticmethod
    def tokenize_string(string):
        tokens = string.split(" ")
        return tokens

    @staticmethod
    def remove_stopwords(tokens):
        with open("data/ind_stopwords.txt", "r", encoding="utf-8") as file:
            stopwords = file.read().splitlines()
        clean_tokens = [token for token in tokens if token.lower() not in stopwords]
        return clean_tokens

    @staticmethod
    def lematization_tokens(tokens):
        dictionary = pd.read_csv("data/dict_lematization.csv")
        changed_tokens = []
        for token in tokens:
            if token in dictionary["kata_turunan"].values:
                changed_tokens.append(dictionary[dictionary["kata_turunan"] == token]["kata_dasar"].values[0])
            else:
                changed_tokens.append(token)
        return changed_tokens

    @staticmethod
    def padding_tokens(tokens, max_length):
        if len(tokens) >= max_length:
            return tokens[:max_length]
        else:
            pad_tokens = tokens + ["[PAD]"] * (max_length - len(tokens))
            return pad_tokens

    def process_text(self, string, max_length):
        cleaned_string = self.clean_string(string)
        tokens = self.tokenize_string(cleaned_string)
        tokens_without_stopwords = self.remove_stopwords(tokens)
        base_tokens = self.lematization_tokens(tokens_without_stopwords)
        padded_tokens = self.padding_tokens(base_tokens, max_length)
        return padded_tokens