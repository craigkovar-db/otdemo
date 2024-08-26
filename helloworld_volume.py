import argparse
parser=argparse.ArgumentParser(description="sample argument parser")
parser.add_argument('-f', '--file')
args=parser.parse_args()

filename = args.file
with open(filename) as f:
    content = f.readline().strip()
    print(f"Hello World from Volumes to {content}")
