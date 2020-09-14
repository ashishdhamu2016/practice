import argparse


parser = argparse.ArgumentParser()

parser.add_argument("--input",help("define input argument"))

args = parser.parse_args()

print(f"these are your arguments:{args}")