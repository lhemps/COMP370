import argparse
import json
from nltk import RegexpTokenizer
from collections import Counter

def term_freq(files, stopwords):
    return 0
    

if __name__ == '__main__':
    def list_str(arg):
        return arg.split(',')

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output_file', required=True)
    parser.add_argument('-s', '--stopwords', required=False)
    parser.add_argument('--input_files', type=list_str, required=True)
    args = parser.parse_args()

    stopwords = []
    if args.stopwords is not None:
        with open(args.stopwords) as f:
            stopwords = [line.strip() for line in f]    

    tfs = term_freq(args.input_files, stopwords)
    
    
    with open(args.output_file,'w') as f:
        json.dump({"sorry I didn't have time to finish": 324}, f)