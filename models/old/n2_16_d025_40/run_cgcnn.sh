python -u main.py --train-ratio 0.4 --val-ratio 0.2 --test-ratio 0.4 --epochs 600 --optim 'SGD' --n-conv 2 --h-fea-len 16 --dropout-rate 0.25 ../../../structures | tee main.out
