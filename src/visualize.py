#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

#print("print(items)=", items)
items_ten = items[:10]
#print("print(items_ten)=", items_ten)
keys = [item[0] for item in items_ten]
#keys = list(items_ten.keys())
#print("print(keys)=", keys)
values = [item[1] for item in items_ten]
#print("print(values)=", values)
keys = keys[::-1]
values = values[::-1]
plt.bar(range(len(keys)), values)
plt.xticks(range(len(keys)), keys)
plt.xlabel("Language Key", size = 15)
plt.ylabel("Number of Tweets", size = 8)
plt.title("#coronavirus Tweets By Language", size = 18)
plt.savefig("coronavirus_language.png")
