<p align="center">
  <a href="https://github.com/codePerfectPlus/dataset-convertor"><img src="https://capsule-render.vercel.app/api?type=rect&color=009ACD&height=100&section=header&text=Dataset%20Convertor&fontSize=90%&fontColor=ffffff" alt="website title image"></a>
  <h2 align="center">👉 Convert object detection dataset format 👈</h2>
</p>

## Dataset types

## Current support format

Currently, the following formats are supported:

|    from    |           to           | implemented |
| :--------: | :--------------------: | ----------- |
| PASCAL VOC |    YOLO(TXT files)     | Yes         |
|    YOLO    | PASCAL VOC (XML files) | Yes         |

## Upcoming support format

|    from    |           to           | Issue/PR(if any) |
| :--------: | :--------------------: | ---------------- |
| PASCAL VOC |   COCO (JSON files)    | No               |
|    COCO    | PASCAL VOC (XML files) | No               |
|    COCO    |    YOLO (TXT files)    | No               |
|    YOLO    |   COCO (JSON files)    | No               |

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

## Contributing

create an issue/PR if any format is missing.Open-source contribution is welcome.check the [contributing guide](/CONTRIBUTING.md) for details. 

## Reference

- PASCAL VOC - http://host.robots.ox.ac.uk/pascal/VOC/
- COCO - http://cocodataset.org/
- YOLO9000 - https://arxiv.org/abs/1612.08242
- YOLO4 - https://arxiv.org/abs/2004.10934v1

## License

- [MIT License](/LICENSE)

## Authors

- [CodePerfectPlus](https://github/com/CodePerfectPlus)
