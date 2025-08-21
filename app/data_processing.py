import pandas as pd
from collections import Counter


class DataProcessing:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    # apply the find_rate_word function on every line in the df
    def create_rate_word(self):
        self.df["rate_word"] = self.df["Text"].apply(self.find_rate_word)

    def create_weapon(self):
        self.df["weapon"] = self.df["Text"].apply(self.find_weapon)

    # function that return the rate word in the df
    @staticmethod
    def find_rate_word(text):
        words = text.split()
        if not words:
            return None
        word_counts = Counter(words)
        rare_word = min(word_counts, key=word_counts.get)
        return rare_word

#funcsion that return the black_list(list of str)
    @staticmethod
    def get_black_list():
        with open("data/weapon_list.txt", "r", encoding="utf-8") as f:
            black_list = [line.strip() for line in f.readlines()]
            return black_list


    def find_weapon(self):
        black_list = self.get_black_list()
        



