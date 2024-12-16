import argparse
import json
import os
import newsapi as na

def collector(api_key, input, output, days=10):
    with open(input) as f:
        keywords = json.load(f)
        f.close()
    for name,words in keywords.items():
        data = na.fetch_latest_news(api_key, words, days)
        with open(os.path.join(output, name + '.json')) as o:
            o.write(data)
            o.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--api_key', required=True, help="api key")
    parser.add_argument('-b', '--lookback', required=False, help='Number of days to look back')
    parser.add_argument('-i', '--input_file', required=True, help='json input file')
    parser.add_argument('-o', '--output_dir', required=True, help='output directory')
    args = parser.parse_args()

    collector(args.api_key, args.input_file, args.output_dir, args.lookback)