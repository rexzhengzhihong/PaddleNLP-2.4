from pprint import pprint
from paddlenlp import Taskflow
import sys

def predit_go():
    schema = ['出发地', '目的地', '费用', '时间']
    # 设定抽取目标和定制化模型权重路径
    my_ie = Taskflow("information_extraction", schema=schema,task_path='/home/DiskA/zncsPython/paddlenlp/uie/checkpoint/model_best')
    print(my_ie("城市内交通费7月5日金额114广州至佛山"))

def predit_billvalue():
    schema = ['出发地', '目的地', '费用', '时间']
    # 设定抽取目标和定制化模型权重路径
    my_ie = Taskflow("information_extraction", schema=schema,task_path='/home/DiskA/zncsPython/paddlenlp/uie/billvalue/checkpoint/model_best')
    print(my_ie("城市内交通费7月5日金额114广州至佛山"))


if __name__ == '__main__':
    #print(sys.path)
    predit_go()
