import pandas as pd
from collections import Counter
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer



class DataProcessing:

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.sid = SentimentIntensityAnalyzer()

    # apply the find_rate_word function on every line in the df
    def create_rate_word(self):
        self.df["rate_word"] = self.df["Text"].apply(self.find_rate_word)

    def create_weapon(self):
        self.df["weapon"] = self.df["Text"].apply(self.find_weapon)

    def create_sentiment(self):
        self.df["sentiment"] = self.df["Text"].apply(self.get_sentiment)

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

#funcsion that check if is word from the black_list if true return the weapon
    def find_weapon(self,text):
        black_list = self.get_black_list()
        weapon = None
        for w in text:
            if w in black_list:
                weapon = w

        return weapon

#funcsion that return the sentiment from the text
    @staticmethod
    def get_sentiment(self, text):
        score = self.sid.polarity_scores(text)["compound"]
        if score >= 0.5:
            return "positive"
        elif score <= -0.5:
            return "negative"
        else:
            return "neutral"












