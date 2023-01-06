import os
import time
import argparse
import json
# coding=utf-8
# 将doccano中的标签格式 转换 成数组
# [
#   {
#     "id": 3862,
#     "text": "单据名称",
#     "prefixKey": null,
#     "suffixKey": "0",
#     "backgroundColor": "#73D8FF",
#     "textColor": "#ffffff"
#   }
# ]
# 转换后
# ["单据名称", "企业名称", "企业税号"]
# ["单据名称", "企业名称", "企业税号", "企业地址", "企业电话", "对方企业名称", "对方企业税号", "对方企业地址", "对方企业电话", "日期", "合计金额", "合计税额", "价税合计小写", "价税合计大写", "企业开户行", "企业银行账号", "对方企业开户行", "对方企业银行账号", "项目", "单位", "数量", "单价", "金额", "税率", "税额", "密码", "流水号", "金额大写", "金额小写", "凭证种类", "结算方式", "产品名称", "计税依据", "制表人", "审核人", "医疗保险金额", "养老保险金额", "失业保险金额", "工伤保险金额", "四险合计金额", "退货率", "部门名称", "用途", "材料名称", "工时", "分配率", "原值合计", "折旧额合计", "资产类别", "资产名称", "原值", "投入使用日期", "使用年限", "折旧率", "折旧额", "证券代码", "证券名称", "持有数量", "账面价值", "收盘价", "市值", "公允价值变动", "人员姓名", "出差事由", "地点", "交通工具", "身份信息", "税种", "纳税所属期限", "处理意见", "残值", "净损益", "利率", "本金", "利息", "社保", "盘点原因", "贴现利息", "贴现金额", "短缺原因", "完工率", "期初成本", "本期生产成本", "完工产品成本", "在产品成本", "科目", "破产原因", "摊销额", "处置原因", "销项税额", "进项税额", "进项税额转出", "减免税额", "增值税应纳税额", "应交城市维护建设税", "应交教育费附加", "应交地方教育费附加", "手续费", "印花税", "证券操作"]
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
