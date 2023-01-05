cd /home/DiskA/PycharmProjects/PaddleNLP-2.4
cd /home/DiskA/PycharmProjects/PaddleNLP-2.4/model_zoo/uie



python3 doccano.py \
--doccano_file /home/DiskA/zncsPython/paddlenlp/uie/billvalue/bill_doccano.jsonl \
--task_type ext \
--save_dir /home/DiskA/zncsPython/paddlenlp/uie/billvalue/data \
--splits 0.8 0.2 0 


```shell
export train_path=/home/DiskA/zncsPython/paddlenlp/uie/billvalue
python3 finetune.py \
    --train_path $train_path/data/train.txt \
    --dev_path $train_path/data/dev.txt \
    --save_dir $train_path/checkpoint \
    --learning_rate 1e-5 \
    --batch_size 1 \
    --max_seq_len 2048 \
    --num_epochs 1 \
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