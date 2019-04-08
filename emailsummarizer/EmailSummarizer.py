from fileop.FileHelper import FileHelper
from summarizer.NLTKSummarizer import NLTKSummarizer
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
        paragraph = FileHelper().read_from_file("/home/mrd/projects/python/wikipidia_summarizer/emailsummarizer/paragraph.txt")
        print(paragraph)

        print("---------- LEVEL 1 ------------")
        paragraph = self.sanitinze(paragraph)
        print(paragraph)

        sentence_tokens, word_tokens = NLTKSummarizer().tokenize_content(paragraph)
        print("---------- SENTENCES ------------")
        # print(sentence_tokens)
        for sentence_token in sentence_tokens:
            print(sentence_token)
        print("---------- WORDS ------------")
        print(word_tokens)

EmailSummarizer().main()
