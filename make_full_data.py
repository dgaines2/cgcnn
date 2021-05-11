import sys

sys.path.append("../..")
import os
import pickle
import numpy as np
from contextlib import contextmanager
from megnet_t_funcs import get_selected_temperatures
from pymatgen.io.cif import CifWriter
from alive_progress import alive_bar


@contextmanager
def change_directory(new_dir):
    prev_dir = os.getcwd()
    os.chdir(os.path.expanduser(new_dir))
    try:
        yield
    finally:
        os.chdir(prev_dir)


with open("../data.pickle", "rb") as fr:
    data = pickle.load(fr)

x_train = data["x_train"]
y_train = data["y_train"]
x_val = data["x_val"]
y_val = data["y_val"]
x_test = data["x_test"]
y_test = data["y_test"]
train_mpids = data["train_mpids"]
val_mpids = data["val_mpids"]
test_mpids = data["test_mpids"]

all_x = np.concatenate((x_train, x_val, x_test), axis=0)
all_y = np.concatenate((y_train, y_val, y_test), axis=0)
all_mpids = np.concatenate((train_mpids, val_mpids, test_mpids), axis=0)

id_prop = []
with alive_bar(len(all_x)) as bar:
    for x, y, mp in zip(all_x, all_y, all_mpids):
        if x.state == [[600]]:
            id_prop.append([f"mp-{mp}", y])
            cw = CifWriter(x, symprec=0.001)
            cw.write_file(f"structures/mp-{mp}.cif")
        bar()

np.savetxt("structures/id_prop.csv", id_prop, delimiter=",", fmt="%s")
