import pyap
from commonregex import CommonRegex
import re
class Parser:
    address_keywords = ('address','tx', 'texas', 'rd', 'road')

    def parse_line(self,sentence,work_token):

        # if address
        for keyword in self.address_keywords:
            if keyword in sentence:
                pattarn = r'\d+( \w+){1,5},( \w+){1,5}, (AZ|CA|CO|NH|TX) [0-9]+(-[0-9]{4})?\s?'
                address_group = re.search(pattarn,sentence,re.IGNORECASE)
                print(address_group.group(0))
