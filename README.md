# annotations-convertor

script for convert annotations from one format to another format

```bash
python convert.py --input-folder ./data/input \
                  --output-folder ./data/output \
                  --input-format  \
                  --output-format
```

## Dataset types

## Current support format

Currently, the following formats are supported:

|    from    |           to           | implemented |
| :--------: | :--------------------: | ----------- |
| PASCAL VOC |    YOLO(TXT files)     | Yes         |
| PASCAL VOC |   COCO (JSON files)    | No          |
|    COCO    | PASCAL VOC (XML files) | No          |
|    COCO    |    YOLO (TXT files)    | No          |
|    YOLO    |   COCO (JSON files)    | No          |
|    YOLO    | PASCAL VOC (XML files) | Yes         |

## Installation

```bash
git clone https://github.com/codePerfectPlus/dataset-convertor/
```

```bash
cd dataset-convertor
python -m venv venv
```

```bash
source venv/bin/activate
pip install requirements.txt
```

## Usage

convert annotations from one format to another format.

dataset formatting example:

    - data/pascal_voc/JPEGImages/*.jpg
    - data/pascal_voc/Annotations/*.xml

    - data/yolo5/JPEGImages/*.jpg
    - data/yolo5/labels/*.txt

```bash
# example command for pascal-voc(xml) to yolo(txt)
python convert.py --input-folder ./data/pascal_voc \
                  --output-folder ./output/yolo5 \
                  --input-format  voc \
                  --output-format yolo
```

## Reference

- PASCAL VOC - http://host.robots.ox.ac.uk/pascal/VOC/
- COCO - http://cocodataset.org/
- YOLO9000 - https://arxiv.org/abs/1612.08242
- YOLO4 - https://arxiv.org/abs/2004.10934v1

## License

- [MIT License](/LICENSE)

## Authors

- [CodePerfectPlus](https://github/com/CodePerfectPlus)
