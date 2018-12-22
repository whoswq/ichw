# -*- coding: utf-8 -*-
"""wcount.py: count words from an Internet file.

__name__: wangchongbin
__pkuid__: 1800011716
__email__: 1800011716@pku.edu.cn
"""

import sys
from urllib.request import urlopen
from urllib import error


def wcount(lines, topn = 10):
    '''this module is used to count words in a list
    lines is a list contains all line in the web
    '''
    
    str_letter = 'abcdefghijklmnopqrstuvwxyz'
    for line in lines:
        l = line.decode()
        list_line = l.split()
        for word in list_line:
            new = word.lower()
            word_new = ''
            for item in new:
                if item in str_letter:
                    word_new += item
                else:
                    word_new += ' '
            
            list_word_new = word_new.split()
            for new_word in list_word_new:
                if new_word in dict_words and new_word != '':
                    dict_words[new_word] += 1
                else:
                    dict_words[new_word] = 1

    list_words = list(dict_words.items())
    list_sorted = sorted(list_words, key = lambda x: x[1], reverse = True)

    if topn <= len(list_sorted):
        list_display = list_sorted[:topn]
        for i in list_display:
            print(i[0].ljust(20, ' '), i[1])
        return True
    else:
        print('sorry topn is out of index')
        return False

def main():
    '''main module
    '''
    global dict_words
    dict_words = {}
    url = sys.argv[1]
    success = False
    
    try:
        doc = urlopen(url)
        doc_lines = doc.readlines()
        doc.close()
        success = True
    except ValueError as e:
        print('valueError')
        print(e)
    except error.HTTPError as e:
        print('HTTPError')
        print(e.code)
    except error.URLError as e:
        print('URLError')
        print(e.reason)

    if success == False:
        print('please try again')
    else:
        if len(sys.argv) == 3:
            try:
                topn = int(sys.argv[2])
                wcount(doc_lines, topn)
            except ValueError:
                print('invalid literal for int()')
                print('please try again')
        if len(sys.argv) == 2:
            wcount(doc_lines)


if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    elif len(sys.argv) > 3:
        print('invalid input')
    else:
        main()
