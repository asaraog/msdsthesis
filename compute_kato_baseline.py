"""Kato et al. (2022) cross-subject pairwise Cit vs Cyc
decoding accuracy directly from the paper's decoding output,
restricted to the post-odor window (t >= 0 ms). 

Each file stores ``MVPA.accs`` as a (1 x nSub)
cell array of per-time-point accuracy vectors (one vector per held-out
subject) and ``MVPA.times`` as the corresponding time axis (35 points
spanning -200 to 1500 ms). 

The reported single number is the mean over
all 22 subjects across the 31 post-odor (t >= 0 ms) time points.
Running this script prints 0.5367 (53.7%, rounded to 54% in the text).
"""
from pathlib import Path

import h5py
import numpy as np

PAIR_FILE = Path(
    'Kato_et_al/Analysis/Decoding/pairwise_crosssubject/4-2vs9-2.mat'
)

with h5py.File(PAIR_FILE, 'r') as f:
    refs = f['MVPA/accs'][()].flatten()
    fold_accs = np.stack([np.asarray(f[r][()]).squeeze() for r in refs])
    times = f['MVPA/times'][()].squeeze()

mask = times >= 0
post_accs = fold_accs[:, mask]
acc = float(post_accs.mean())
print(
    f'cross-subject Cit vs Cyc accuracy (t >= 0 ms) = '
    f'{acc:.4f}  ({acc * 100:.1f}%)  '
    f'[{post_accs.shape[0]} LOSO folds x {post_accs.shape[1]} time points]'
)
