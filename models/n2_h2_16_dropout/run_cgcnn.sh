python -u main.py --train-ratio 0.8 --val-ratio 0.1 --test-ratio 0.1 --epochs 600 --optim 'SGD' --n-conv 2 --n-h 2 --h-fea-len 16 --dropout ../structures | tee main.out
