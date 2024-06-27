# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 14:33:01 2024

@author: rikutotomita
"""

import itertools
import pandas as pd

def word_snake_match(word1,word2,reverse):
    word1_list = list(word1)
    best_word_snake = ""
    for i in range(len(word1_list)):
        if word2[:i] == word1[-1*i:]:
            best_word_snake = word1 + word2[i:]
    if best_word_snake == "":
        best_word_snake = word1 + word2
    if reverse == 0:
        len_word_snake_reverse = word_snake_match(word2, word1, 1)
        if len(best_word_snake) > len(len_word_snake_reverse):
            best_word_snake = len_word_snake_reverse
    return best_word_snake

# word_snake_match('terrible','less',0)

# リストを定義
list_target = ['subway', 'dentist', 'wayward', 'highway', 'terrible', 'english', 'less', 'blessed', 'warden', 'rib', 'stash', 'shunt', 'hunter']

# 全ての組み合わせを取得
combinations = list(itertools.combinations(list_target, 2))

# 結果を保存するリスト
results = []

# 組み合わせに対して word_snake_match 関数を適用して出力
for word1, word2 in combinations:
    snake = word_snake_match(word1, word2, 0)
    original_length = len(word1) + len(word2)
    snake_length = len(snake)
    shortened_length = original_length - snake_length
    results.append([word1, word2, snake, original_length, snake_length, shortened_length])

# pandasのDataFrameに変換
df = pd.DataFrame(results, columns=['Word 1', 'Word 2', 'Word Snake', 'Original Length', 'Snake Length', 'Shortened Length'])

# DataFrameを表示
print(df)
