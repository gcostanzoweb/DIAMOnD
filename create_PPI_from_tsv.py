import csv
import sys


inputfile = sys.argv[1]
outfile = sys.argv[2]

sniffer = csv.Sniffer()
line_delimiter = None
for line in open(inputfile,'r'):
    if line[0]=='#':
        continue
    else:
        dialect = sniffer.sniff(line)
        line_delimiter = dialect.delimiter
        break
if line_delimiter == None:
        print('network_file format not correct')
        sys.exit(0)

with open(outfile,'w') as fout:
    for line in open(inputfile,'r'):
            # lines starting with '#' will be ignored
            if line[0]=='#':
                continue
            # The first two columns in the line will be interpreted as an
            # interaction gene1 <=> gene2
            #line_data   = line.strip().split('\t')
            line_data = line.strip().split(line_delimiter)
            print(line_data)
            node1 = line_data[0]
            node2 = line_data[1]

            print(','.join([node1,node2]), file=fout)
