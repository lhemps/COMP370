import argparse
import json
from nltk.tokenize import RegexpTokenizer
from collections import Counter

def word_count(file, stopwords) :
    with open(file) as f:
        posts = json.load(f)

    titles = []
    for post in posts["data"]["children"]:
        titles.append(post["data"]["title"])

    tokens = []
    tokenizer = RegexpTokenizer(r'\w+')
    for title in titles:
        tokenized = tokenizer.tokenize(title)
        for word in tokenized:
            if word.lower() in stopwords:
                continue
            tokens.append(word.lower())
    
    return Counter(tokens).most_common(10)

if __name__ == "__main__":
    def list_str(arg):
        return arg.split(',')
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--word_counts')
    parser.add_argument('-s', '--stop_words', required=False)
    parser.add_argument('--input_files', type=list_str, required=True)
    args = parser.parse_args()

    stopwords = []
    if args.stop_words is not None:
        with open(args.stop_words) as f:
            stopwords = [line.strip() for line in f]    

    counts = {}
    for file in args.input_files :
        counts[file] = word_count(file, stopwords)
    
    with open(args.word_counts,'w') as f:
        json.dump(counts,f,indent=4)