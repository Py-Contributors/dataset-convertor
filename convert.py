""" 
# Python script to convert objects detection dataset from 
# one format to another format

"""

import argparse
from src.utils import Convertor

parser = argparse.ArgumentParser(description='convert object detection format to another format')
parser.add_argument('--input-folder', '-i', type=str, required=True, help='input folder')
parser.add_argument('--output-folder', '-o', type=str, required=True, help='output folder')
parser.add_argument('--input-format', '-if', type=str, required=True, help='input format')
parser.add_argument('--output-format', '-of', type=str, required=True, help='output format')
args = parser.parse_args()


if __name__ == '__main__':

    convertor = Convertor(args.input_folder, args.output_folder, args.input_format, args.output_format)
    if args.input_format == 'yolo' and args.output_format == "voc":
        convertor.yolo2voc()
    elif args.input_format == 'voc' and args.output_format == "yolo":
        convertor.voc2yolo()
    else:
        print('Conversion not supported yet, please check https://github.com/codePerfectPlus/dataset-convertor/blob/main/README.md for upcoming supported formats')
