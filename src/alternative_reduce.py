#!/usr/bin/env python3
import matplotlib
import numpy as np
import json
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import argparse
from collections import Counter, defaultdict
from glob import glob

parser = argparse.ArgumentParser()
parser.add_argument('--input_dir', required=True)
parser.add_argument('--keys', nargs='+', required=True)
args = parser.parse_args()

input_files = glob(args.input_dir + '/*')

for key in args.keys:
    yaxis = []
    total = defaultdict(lambda: Counter())
    
    for path in sorted(input_files):
        with open(path) as f:
            tmp = json.load(f) 
            sumofnum = 0 
            try:
                for k in tmp[key]:
                    sumofnum += tmp[key][k]
            except:
                pass
            yaxis.append(sumofnum)
    
    plt.plot(np.arange(len(yaxis)), yaxis, label=key)

plt.xlabel("2020 Date Month")
plt.ylabel("Number of Tweets")
plt.title("Tweets Per Hashtag 2020")
plt.legend()
plt.xticks([0, 60, 121, 182, 244, 305], ["Jan", "Mar", "May", "Jul", "Sep", "Nov"]) 
plt.savefig("lineplot7.png", bbox_inches="tight")
