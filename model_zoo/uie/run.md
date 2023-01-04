cd /home/DiskA/PycharmProjects/PaddleNLP-2.4
cd /home/DiskA/PycharmProjects/PaddleNLP-2.4/model_zoo/uie

#### idea中运行环境已经改成/usr/local/bin/python3了。但还是会报错：
ImportError: libcudart.so.10.1: cannot open shared object file: No such file or directory
解决：
sudo ldconfig /usr/local/cuda-10.0/lib64

```shell
python3 -m pip install paddlenlp.trainer

```

python3 doccano.py \
--doccano_file /home/DiskA/zncsPython/paddlenlp/uie/data/doccano_ext.jsonl \
--task_type ext \
--save_dir /home/DiskA/zncsPython/paddlenlp/uie/data \
--splits 0.8 0.2 0 \
--schema_lang ch


```shell
export train_path=/home/DiskA/zncsPython/paddlenlp/uie
python3 finetune.py \
    --train_path $train_path/data/train.txt \
    --dev_path $train_path/data/dev.txt \
    --save_dir $train_path/checkpoint \
    --learning_rate 1e-5 \
    --batch_size 8 \
    --max_seq_len 512 \
    --num_epochs 100 \
    --model uie-base \
    --seed 1000 \
    --logging_steps 10 \
    --valid_steps 100 \
    --device gpu
```

```shell
python3 evaluate.py \
    --model_path /home/DiskA/zncsPython/paddlenlp/uie/checkpoint/model_best \
    --test_path /home/DiskA/zncsPython/paddlenlp/uie/data/dev.txt \
    --batch_size 8 \
    --max_seq_len 512 
```
- 评估
python3 evaluate.py \
    --model_path /home/DiskA/zncsPython/paddlenlp/uie/checkpoint/model_best \
    --test_path /home/DiskA/zncsPython/paddlenlp/uie/data/dev.txt \
    --debug