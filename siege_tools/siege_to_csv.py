import csv
import argparse

def process(infilename, outfilename):
    """
    Take an input file and create from it an output file in csv. This can
    later be used to load into R or another program of similar ability.

    """

    with open(infilename, 'r') as infile, open(outfilename, 'wb') as outfile:
        writer = csv.writer(outfile, delimiter=' ')
        writer.writerow(['url', 'status', 'time', 'size'])
        for line in infile:
            if not 'HTTP' in line:
                # A hack to avoid non-informative lines
                continue
            raw_data = line.split()
            status = raw_data[1]
            time = float(raw_data[2])
            url = raw_data[7]
            size = float(raw_data[4])
            writer.writerow([url, status, time, size])


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Process siege files')
    parser.add_argument('-i', '--infile', type=str,
                        help='Input file with siege output')
    parser.add_argument('-o', '--outfile', type=str,
                        help='Output file to write')

    args = parser.parse_args()
    process(infilename=args.infile, outfilename=args.outfile)
