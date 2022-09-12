import csv

INFILE = "./data/amazon_full.tsv"
OUTFILE = "./data/amazon_full.csv"

with open(INFILE) as fin:
    reader = csv.reader(fin, delimiter="\t")
    content = list(reader)

with open(OUTFILE, "w") as fout:
    writer = csv.writer(fout)
    writer.writerows(content)

