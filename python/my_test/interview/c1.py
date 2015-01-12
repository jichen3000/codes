text = """
Early sales of Apple's new iPhones have lived up to high expectations.

The strong sales mirror growing consumer demand for smartphones with bigger
screens. IDC, a research firm, estimated that at least 20 percent of all
smartphones shipped last year in China, the largest smartphone market in
the world, were five inches or larger. It also predicted that manufacturers
this year would ship more "phablets," or smartphones with screens measuring
at least 5-point-5 diagonal inches, than laptops.

The company on Monday said it sold more than 10 million of the iPhone 6 and
6 Plus models in the first three days they were available in stores. That
is higher than the nine million new iPhones it sold last year in their
first weekend on sale. But some analysts, like Gene Munster of Piper
Jaffray, wondered whether first-weekend sales were still a reliable measure
for consumer demand.

The iPhone sales were on the upper end of financial analysts' expectations,
which ranged from 6 million to the "low teens" of millions of sales.
"""
    
def search_text(text, keyword):
    def check_keyword(setence, keyword):
        words = setence.split(" ")
        return keyword in words
    return [line for line in text.split(".") if check_keyword(line, keyword)]

if __name__ == '__main__':
    from minitest import *

    with test(search_text):
        search_text(text, 'iPhone').must_equal(['\n\nThe company on Monday said it sold more than 10 million of the iPhone 6 and\n6 Plus models in the first three days they were available in stores',
 '\n\nThe iPhone sales were on the upper end of financial analysts\' expectations,\nwhich ranged from 6 million to the "low teens" of millions of sales'])