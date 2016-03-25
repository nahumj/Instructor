#!/usr/bin/env python3
"""
DO NOT EDIT THIS FILE!
You should only be editing "project0.py"!
"""
from project0 import *
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    args = parser.parse_args()
    convert_to_capitals(args.input_file, args.output_file)

if __name__ == "__main__":
    main()