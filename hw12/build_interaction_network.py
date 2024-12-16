import pandas
import argparse
import json

def build_network(df, ponylist):
    network = dict.fromkeys(ponylist, {})
    speakers = df['pony'].tolist()
    for i, pony in enumerate(speakers):
        if i+1 == len(speakers): continue
        pony2 = speakers[i+1]
        if pony.strip() == pony2.strip(): continue
        try:
            network[pony][pony2] += 1 
            network[pony2][pony] += 1
        except KeyError:
            network[pony][pony2] = 1
            network[pony2][pony] = 1
    return network

def preprocess(f):
    df = pandas.read_csv(f,header=0,encoding='utf-8')
    df = df.map(lambda x: x.lower() if type(x) == str else x)
    df = df[~df['pony'].str.contains('others|ponies|and|all', regex=True)]
    ponylist = df.groupby(['pony'])['pony'].count().sort_values(ascending=False).head(101)
    df = df[df['pony'].isin(ponylist.keys())]
    return df, ponylist.keys()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--script_input')
    parser.add_argument('-o', '--network_file')
    args = parser.parse_args()

    df, ponylist = preprocess(args.script_input)
    network = build_network(df, ponylist)

    with open(args.network_file, 'w') as f:
        json.dump(network, f, indent=4)
    