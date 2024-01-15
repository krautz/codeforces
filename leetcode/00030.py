# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        word_on_start_index = {}
        for word in set(words):
            start_index = s.find(word)
            while start_index != -1:
                word_on_start_index[start_index] = word
                start_index = s.find(word, start_index + 1)

        result = []
        for start_index in sorted(list(word_on_start_index.keys())):
            word_count_local = {word: 0 for word in words}
            total_words_found = 0
            current_start_index = start_index
            while current_start_index in word_on_start_index and total_words_found != len(words):
                word = word_on_start_index[current_start_index]
                word_count_local[word] += 1
                total_words_found += 1
                current_start_index += len(words[0])

            if word_count_local == word_count:
                result.append(start_index)


        return result
