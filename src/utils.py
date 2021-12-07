import os
from PIL import Image
from glob import glob
from xml.etree import ElementTree as ET
import shutil
from datetime import datetime


class Convertor:
    ''' 
    Convertor class is a class for converting images and annotations from one format to another.

    Parameters
    ----------
    input_folder : str
        Path to the input folder.
    output_folder : str
        Path to the output folder.
    input_format : str
        Input format of the images and annotations.
    output_format : str
        Output format of the images and annotations.

    Methods
    -------
    voc2yolo()
        Convert Pascal VOC format to Yolo5 format.
    
    yolo2voc()
        Convert Yolo5 format to Pascal VOC format.

    # Pascal Voc - XML
    # Pascal VOC format is a XML file format for images and annotations.
    # Yolo5 - TXT
    # Yolo5 format is a text file format for images and annotations.
    # COCO - JSON
    # COCO format is a JSON file format for images and annotations.
    
    '''
    def __init__(self, input_folder, outout_folder, input_format, output_format):
        self.input_folder = input_folder
        self.input_image_folder = os.path.join(self.input_folder, 'JPEGImages')
        self.input_annotation_folder = os.path.join(self.input_folder, 'Annotations')
        self.output_folder = outout_folder
        self.output_image_folder = os.path.join(self.output_folder, 'JPEGImages')
        self.output_annotation_folder = os.path.join(self.output_folder, 'Annotations')
        self.input_format = input_format
        self.output_format = output_format
    
    def voc2yolo(self):
        ''' Pascal Voc format to yolo txt format conversion '''
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
        ''' yolo txt format to pascal voc xml format '''
        if self.input_format == 'yolo' and self.output_format == 'voc':
            
            # create output Annotations folder if not exists
            if not os.path.exists(self.output_annotation_folder):
                    os.makedirs(self.output_annotation_folder)
            
            for txt_file in glob(os.path.join(self.input_annotation_folder, '*.txt')):
                image_file_name = os.path.basename(txt_file)[:-4] + '.jpg'
                
                # create output image file directory if not exists
                if not os.path.exists(self.output_image_folder):
                    os.makedirs(self.output_image_folder)
                
                # copy image file to output image file directory
                shutil.copy(os.path.join(self.input_image_folder, image_file_name), 
                            os.path.join(self.output_image_folder, image_file_name))
                
                # read txt file
                with open(txt_file, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        line = line.strip()
                        label, x, y, w, h = line.split(' ')
                        img = Image.open(os.path.join(self.input_image_folder, image_file_name))

                        img_width, img_height = img.size

                        xmin = int(float(x) * img_width)
                        ymin = int(float(y) * img_height)
                        xmax = int(float(x) * img_width + float(w) * img_width)
                        ymax = int(float(y) * img_height + float(h) * img_height)

                        # create xml file
                        # REVIEW: need to REVIEW the xml file formation
                        root = ET.Element('annotation')
                        ET.SubElement(root, 'folder').text = 'VOC'
                        ET.SubElement(root, 'filename').text = image_file_name
                        ET.SubElement(root, 'source').text = 'https://github.com/codePerfectPlus/dataset-convertor'
                        ET.SubElement(root, 'database').text = 'VOC Format'
                        ET.SubElement(root, 'date').text = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        root2 = ET.SubElement(root, 'size')
                        ET.SubElement(root2, 'width').text = str(img_width)
                        ET.SubElement(root2, 'height').text = str(img_height)
                        ET.SubElement(root2, 'depth').text = '3'
                        root3 = ET.SubElement(root, 'object')
                        ET.SubElement(root3, 'name').text = label
                        ET.SubElement(root3, 'pose').text = 'Unspecified'
                        ET.SubElement(root3, 'truncated').text = '0'
                        ET.SubElement(root3, 'difficult').text = '0'
                        root4 = ET.SubElement(root3, 'bndbox')
                        ET.SubElement(root4, 'xmin').text = str(xmin)
                        ET.SubElement(root4, 'ymin').text = str(ymin)
                        ET.SubElement(root4, 'xmax').text = str(xmax)
                        ET.SubElement(root4, 'ymax').text = str(ymax)

                        # write xml file
                        tree = ET.ElementTree(root)
                        tree.write(os.path.join(self.output_annotation_folder, image_file_name[:-4] + '.xml'))
        else:
            print('Not support')

    def yolo2coco(self):
        ''' yolo txt format to coco json format '''
        pass
    
    def coco2yolo(self):
        ''' coco json format to yolo txt format '''
        pass

    def voc2coco(self):
        ''' voc xml format to coco json format '''
        pass

    def coco2voc(self):
        ''' coco json format to voc xml format '''
        pass
