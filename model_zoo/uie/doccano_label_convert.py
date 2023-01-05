import os
import time
import argparse
import json
# coding=utf-8
# ½«doccanoÖÐµÄ±êÇ©Êý¾Ý ×ª³ÉÊý×é
# [
#   {
#     "id": 3862,
#     "text": "µ¥¾ÝÃû³Æ",
#     "prefixKey": null,
#     "suffixKey": "0",
#     "backgroundColor": "#73D8FF",
#     "textColor": "#ffffff"
#   }
# ]
# ×ª³É
# ["µ¥¾ÝÃû³Æ", "ÆóÒµÃû³Æ", "ÆóÒµË°ºÅ"]
#
#


def do_convert():
    tic_time = time.time()
    if not os.path.exists(args.doccano_label_file):
        raise ValueError("Please input the correct path of doccano file.")

    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir)

    # file = open(args.doccano_label_file, "rb", encoding="utf-8")
    # fileJson = json.loads(file)
    # print(fileJson)
    raw_examples=""
    with open(args.doccano_label_file, "r", encoding="utf-8") as f:
        raw_examples=f.read()

    json2 = json.loads(raw_examples)
    lable=[]
    for i in range(len(json2)):
        lable.append(json2[i]['text'])
        #print(json2[i]['text'])

    print(lable)
    with open(args.save_dir+"/label_config_list.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(lable, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    # yapf: disable
    parser = argparse.ArgumentParser()

    parser.add_argument("--doccano_label_file", default="C:\\Users\\rex\\Downloads\\label_config.json", type=str, help="The doccano file exported from doccano platform.")
    parser.add_argument("--save_dir", default="C:\\Users\\rex\\Downloads\\", type=str, help="The path of data that you wanna save.")
    args = parser.parse_args()
    # yapf: enable

    do_convert()
