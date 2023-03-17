#!/usr/bin/env python
# coding: utf-8

import argparse

from utils.data_utils import read_training_data
from utils.pipeline_utils import run_cv
from models.bert_model import BertModel


def main(args):
    df = read_training_data()
    run_cv(model_obj=BertModel,
           model_params={"model_path": args.model_path,
                         "epochs": args.epochs,
                         "batch_size": args.batch_size,
                         "tokenizer_max_len": args.tokenizer_max_len,
                         "learning_rate": args.learning_rate
                         },
           input_df=df,
           fold_col=args.fold_name,
           x_col=args.xcol,
           y_col=args.ycol,
           experiment_name=f"{args.model_path}",
           add_to_zoo=args.add_zoo,
           is_nn=True
           )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-model-path', type=str, default="dbmdz/bert-base-turkish-128k-uncased")
    parser.add_argument('-batch-size', type=int, default=128)
    parser.add_argument('-tokenizer-max-len', type=int, default=32)
    parser.add_argument('-learning-rate', type=float, default=7e-5)
    parser.add_argument('-epochs', type=int, default=3)

    parser.add_argument('-fold-name', type=str, default="public_fold")
    parser.add_argument('-xcol', type=str, default="text")
    parser.add_argument('-ycol', type=str, default="target_label")
    parser.add_argument('--add-zoo', action='store_true')
    args = parser.parse_args()
    main(args)