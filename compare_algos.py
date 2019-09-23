import csv
import sys
from collections import defaultdict

def calcscore(inputfile, dictionary):
    score = 0
    rank = 0
    for line in open(inputfile, 'r'):
        if line[0]=='#':
            continue
        else:
            rank+=1
    
    for line in open(inputfile,'r'):
        if line[0]=='#':
            continue
        else:
            line_data = line.strip().split()         
            node = line_data[1]
            if node in dictionary:
                score += rank*dictionary[node]
            else:
                score += rank*min(dictionary.values())
            rank-=1
    
    return score

def compare(res, dictfile):
    dictionary = defaultdict(dict)

    sniffer = csv.Sniffer()
    line_delimiter = None
    for line in open(dictfile,'r'):
        if line[0]=='#':
            continue
        else:
            dialect = sniffer.sniff(line)
            line_delimiter = dialect.delimiter
            break
    if line_delimiter == None:
            print('network_file format not correct')
            sys.exit(0)

    for line in open(dictfile,'r'):
            # lines starting with '#' will be ignored
            if line[0]=='#':
                continue
            # The first two columns in the line will be interpreted as an
            # interaction gene1 <=> gene2
            #line_data   = line.strip().split('\t')
            line_data = line.strip().split(line_delimiter)
            
            node = line_data[0]
            score = line_data[1]

            dictionary[node] = float(score)

    return calcscore(res, dictionary)

if __name__ == '__main__':
    oldres = sys.argv[1]
    newres = sys.argv[2]
    dictfile = sys.argv[3]

    (oldscore, newscore) = (compare(oldres, dictfile), compare(newres, dictfile))

    print(oldscore)
    print(newscore)
