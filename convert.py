''' 
# Python script to convert objects detection dataset from 
# one format to another format

'''

import argparse
import logging
from src.utils import Convertor

logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',
					datefmt='%d/%m/%Y %I:%M:%S %p',
					level=logging.INFO,
					handlers=[
        				logging.FileHandler('debug.log'),
        				logging.StreamHandler()])
    
parser = argparse.ArgumentParser(description='convert object detection format to another format')
parser.add_argument('--input-folder', '-i', type=str, required=True, help='input folder')
parser.add_argument('--output-folder', '-o', type=str, required=True, help='output folder')
parser.add_argument('--input-format', '-if', type=str, required=True, help='input format')
parser.add_argument('--output-format', '-of', type=str, required=True, help='output format')
args = parser.parse_args()


if __name__ == '__main__':

    convertor = Convertor(args.input_folder, args.output_folder, args.input_format, args.output_format)

    if args.input_format == 'yolo' and args.output_format == 'voc':
        logging.info('Starting conversion from yolo to voc format')
        convertor.yolo2voc()
        logging.info('Conversion Completed. Check {} folder'.format(args.output_folder))
    
    elif args.input_format == 'voc' and args.output_format == 'yolo':
        logging.info('Starting conversion from voc to yolo format')
        convertor.voc2yolo()
        logging.info('Conversion Completed. Check {} folder'.format(args.output_folder))
    
    else:
        print('Conversion not supported yet, please check https://github.com/codePerfectPlus/dataset-convertor and create an issue.')
