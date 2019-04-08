from fileop.FileHelper import FileHelper
from summarizer.NLTKSummarizer import NLTKSummarizer
from emailsummarizer.Parser import Parser
import re


class EmailSummarizer:

    def sanitinze(self,content):
        val = re.sub(r'\s{2,}', ' ', content)
        replace = {
            ord('\f'): ' ',
            ord('\t'): ' ',
            ord('\n'): ' ',
            ord('\r'): None
        }
        return val.translate(replace)

    def main(self):
        paragraph = FileHelper().read_from_file("paragraph.txt")
        print(paragraph)

        print("---------- LEVEL 1 ------------")
        paragraph = self.sanitinze(paragraph)
        # print(paragraph)

        sentence_tokens = NLTKSummarizer().tokenize_to_sentence(paragraph)
        #
        # print("---------- SENTENCES ------------")
        # # print(sentence_tokens)
        for sentence in sentence_tokens:
            # print(sentence)
            word_tokens = NLTKSummarizer().tokenize_single_sentence(sentence)

            Parser().parse_line(sentence, word_tokens)

            # word_tokens_trimmed = NLTKSummarizer().tokenize_single_sentence(sentence,True)
            # print("---------- WORDS ------------")
            # print(word_tokens)
            # print("---------- WORDS TRIMMED------------")
            # print(word_tokens_trimmed)


        # sentence_tokens = NLTKSummarizer().tokenize_to_sentence(paragraph)
        # word_token = NLTKSummarizer().tokenize_single_sentence(paragraph)
        # print(word_token)


EmailSummarizer().main()
