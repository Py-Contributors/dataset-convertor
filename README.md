# annotations-convertor

script for convert annotations from one format to another format

```bash
python convert.py --input-folder ./data/input \
                  --output-folder ./data/output \
                  --input-format  \
                  --output-format
```

## Current support format

Currently, the following formats are supported:

- pascal_voc - XML files
- yolo5 - txt files
- coco - json files

## Upcoming support format

the following formats are planned to be supported in the future:


## Installation

```bash
python -m venv venv
source venv/bin/activate
pip install requirements.txt
```

## Usage

convert annotations from one format to another format.

```bash
# example command for pascal-voc(xml) to yolo(txt)
python convert.py --input-folder ./data/pascal_voc \
                  --output-folder ./output/yolo5 \
                  --input-format  voc \
                  --output-format yolo
```

## License

- [MIT License](/LICENSE)

## Authors

- [CodePerfectPlus](https://github/com/CodePerfectPlus)