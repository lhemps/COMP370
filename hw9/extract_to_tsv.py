import argparse
import json
import random

def extract_to_tsv(output, input, number):
    with open(input, 'r') as f:
        file = json.load(f)
    
    with open(output, 'w') as o:
        o.write("Name\tTitle\tcoding\n")
        posts = file["data"]["children"]
        if number > len(posts):
            number = len(posts)
        for post in random.sample(posts, number):
            post = post["data"]
            o.write(post["name"]+ '\t' + post["title"] + '\t \n')
    

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output_file", required=True)
    parser.add_argument("json_file")
    parser.add_argument("num_posts",type=int)

    args = parser.parse_args()

    extract_to_tsv(args.output_file, args.json_file, args.num_posts)
