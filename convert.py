""" 
# Python script to convert objects detection dataset from 
# one format to another format

"""

import argparse


parser = argparse.ArgumentParser(description='convert object detection format to another format')
parser.add_argument('--input-folder', '-i', type=str, required=True, help='input folder')
parser.add_argument('--output-folder', '-o', type=str, required=True, help='output folder')
parser.add_argument('--input-format', '-if', type=str, required=True, help='input format')
parser.add_argument('--output-format', '-of', type=str, required=True, help='output format')
args = parser.parse_args()


