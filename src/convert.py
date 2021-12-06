import os
from glob import glob
from turtle import width
from xml.etree import ElementTree as ET
import shutil
# Pascal Voc - XML
# Pascal VOC format is a XML file format for images and annotations.
# Yolo5 - TXT
# Yolo5 format is a text file format for images and annotations.
# COCO - JSON
# COCO format is a JSON file format for images and annotations.

class Convertor:
    def __init__(self, input_folder, outout_folder, input_format, output_format):
        self.input_folder = input_folder
        self.output_folder = outout_folder
        self.input_image_folder = os.path.join(self.input_folder, 'JPEGImages')
        self.input_annotation_folder = os.path.join(self.input_folder, 'Annotations')
        self.output_image_folder = os.path.join(self.output_folder, 'JPEGImages')
        self.output_annotation_folder = os.path.join(self.output_folder, 'Annotations')
        self.input_format = input_format
        self.output_format = output_format
    
    def voc2yolo(self):
        """ Pascal Voc format to yolo txt format conversion """
        if self.input_format == 'voc' and self.output_format == 'yolo':
            for xml_file in glob(os.path.join(self.input_annotation_folder, '*.xml')):
                tree = ET.parse(xml_file)
                root = tree.getroot()
                
                file_name = root.find('filename').text
                width = int(root.find('size').find('width').text)
                height = int(root.find('size').find('height').text)

                for obj in root.iter('object'):
                    xmin = int(obj.find('bndbox').find('xmin').text)
                    ymin = int(obj.find('bndbox').find('ymin').text)
                    xmax = int(obj.find('bndbox').find('xmax').text)
                    ymax = int(obj.find('bndbox').find('ymax').text)
                    label = obj.find('name').text

                    # conver xmin ymin xmax ymax to x y w h
                    x = (xmin + xmax) / width
                    y = (ymin + ymax) / height
                    w = (xmax - xmin) / width
                    h = (ymax - ymin) / height


                    if not os.path.exists(self.output_annotation_folder):
                        os.makedirs(self.output_annotation_folder)

                    # FIXME: conver label to id
                    with open(os.path.join(self.output_annotation_folder, file_name[:-4] + '.txt'), 'a') as f:
                        f.write(label + ' ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h) + '\n')

                if not os.path.exists(self.output_image_folder):
                    os.makedirs(self.output_image_folder)
                
                shutil.copy(os.path.join(self.input_image_folder, file_name), os.path.join(self.output_image_folder, file_name))

        else:
            print('Not support')

    def yolo2voc(self):
        """ yolo txt format to pascal voc xml format """
        # TODO: write yolo2Voc conversion script    

""" if __name__ == '__main__':
    input_folder = 'data/yolo'
    output_folder = 'output/voc'
    input_format = 'yolo'
    output_format = 'voc'
    convertor = Convertor(input_folder, output_folder, input_format, output_format)
    convertor.pascal2voc() """

