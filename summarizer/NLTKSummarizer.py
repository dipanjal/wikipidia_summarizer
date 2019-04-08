from scrapper.wikipidia import wikipidia
from fileop.FileHelper import FileHelper

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict
import re


class NLTKSummarizer:

    def summarize_wikipidia_article(self, url):
        resp = wikipidia().do_scrap(url)
        if resp['code'] == 200:
            content = resp['body']

            content = self.sanitize_input(content)

            sentence_tokens, word_tokens = self.tokenize_content(content)

            sentence_ranks = self.score_tokens(word_tokens, sentence_tokens)

            return self.summarize(sentence_ranks, sentence_tokens, 4)
        else:
            print(resp['code'], resp['message'])

    def sanitize_input(self, data):
        """
        Currently just a whitespace remover. More thought will have to be given with how
        to handle sanitzation and encoding in a way that most text files can be successfully
        parsed
        """
        replace = {
            ord('\f'): ' ',
            ord('\t'): ' ',
            ord('\n'): ' ',
            ord('\r'): None
        }
        return data.translate(replace)

    def tokenize_content(self, content):
        """
        Accept the content and produce a list of tokenized sentences,
        a list of tokenized words, and then a list of the tokenized words
        with stop words built from NLTK corpus and Python string class filtred out.
        """
        stop_words = set(stopwords.words('english') + list(punctuation))
        words = word_tokenize(content.lower())

        return [
            sent_tokenize(content),
            [word for word in words if word not in stop_words]
        ]

    def tokenize_to_sentence(self, content):
        return sent_tokenize(content)

    def tokenize_single_sentence(self, content, is_trim=False):
        """
        Accept the content and produce a list of tokenized sentences,
        a list of tokenized words, and then a list of the tokenized words
        with stop words built from NLTK corpus and Python string class filtred out.
        """
        stop_words = set(stopwords.words('english') + list(punctuation))
        words = word_tokenize(content.lower())
        if(is_trim):
            return [word for word in words if word not in stop_words]

        return words

    def score_tokens(self, filterd_words, sentence_tokens):
        """
        Builds a frequency map based on the filtered list of words and
        uses this to produce a map of each sentence and its total score
        """
        word_freq = FreqDist(filterd_words)

        ranking = defaultdict(int)

        for i, sentence in enumerate(sentence_tokens):
            for word in word_tokenize(sentence.lower()):
                if word in word_freq:
                    ranking[i] += word_freq[word]

        return ranking

    def summarize(self, ranks, sentences, length):
        """
        Utilizes a ranking map produced by score_token to extract
        the highest ranking sentences in order after converting from
        array to string.
        """
        if int(length) > len(sentences):
            print("Error, more sentences requested than available. Use --l (--length) flag to adjust.")
            exit()

        indexes = nlargest(length, ranks, key=ranks.get)
        final_sentences = [sentences[j] for j in sorted(indexes)]
        final_sentences = ' '.join(final_sentences)
        return final_sentences
        # final_sentences = re.sub(r'[()]*', ' ', final_sentences)
        # replace = {
        #     ord('('): ' ',
        #     ord(')'): ' ',
        #     ord('['): ' ',
        #     ord(']'): ' '
        # }
        #
        # return final_sentences.translate(replace)


    def main(self):
        summery = self.summarize_wikipidia_article("https://en.wikipedia.org/wiki/Artificial_intelligence")
        # summery = self.summarize_wikipidia_article("https://en.wikipedia.org/wiki/Bangladesh")
        saved_file_location = FileHelper().write_in_file(summery, 'what is Bangladesh')
        print("file located at: ", saved_file_location)

        # resp = wikipidia().do_scrap("https://en.wikipedia.org/wiki/Artificial_intelligence")
        # if resp['code'] == 200:
        #     content = resp['body']
        #     saved_file_location = FileHelper().write_in_file(content, 'Artificial intelligence')
        #     print("file located at: ", saved_file_location)



# NLTKSummarizer().main()
