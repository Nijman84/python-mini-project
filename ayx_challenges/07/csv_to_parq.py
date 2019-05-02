#!/usr/bin/python3
import pandas as pd
import sys

if len(sys.argv) <= 1:
    print('Please specify a CSV you want to convert to Parquet')
    exit(1)

csvFile = sys.argv[1]

# splitted = csvFile.split('.')
# print(splitted)
# outputNameElements = splitted[:-1]
# print(outputNameElements)
# outputName = '.'.join(outputNameElements)
# print(outputName)
outputParq = '.'.join(csvFile.split('.')[:-1]) + '.parq'

white = '\033[1;37;40m'
blue = '\033[1;34;40m'
green = '\033[1;32;40m'

print(white, 'Converting', blue, csvFile, white, 'to', green, outputParq, white)

df = pd.read_csv(csvFile)
df.to_parquet(outputParq)
