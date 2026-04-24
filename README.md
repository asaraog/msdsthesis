# MSDS Thesis – Supplementary Files

Supplementary files accompanying the MSDS thesis "Neural Decoding of Smell"
(Apoorv Saraogee, Northwestern University SPS).

## Contents

| File | Description |
| --- | --- |
| `eeg_decoding_saraogee.ipynb` | Primary analysis notebook: model training, temporal/spatial/spatiotemporal occlusion analysis, class-specific occlusion, decision-threshold sweep, and paper comparison. |
| `citcyc_cnn_lstm_model.keras` | Final saved Keras model used for Cit vs Cyc evaluation and thesis figure generation. Includes the trained network architecture and weights. |
| `compute_kato_baseline.py` | Standalone script that reproduces the 54% Kato et al. (2022) cross-subject ridge-regression baseline by loading `4-2vs9-2.mat` and averaging `MVPA.accs` over the 22 LOSO subject folds and 31 post-odor decoding time points (t ≥ 0 ms). |
| `kato_cit_cyc_grid2d_events.pkl` | Pre-processed Cit vs Cyc trial data in 2-D grid format (28 time bins, 10×11 grid, 2 channels). Direct input for model training and evaluation. *Tracked via Git LFS.* |

## External data

The full upstream dataset is available at
<https://zenodo.org/records/6387085> under `Kato_et_al/`.

## Companion repository

Full development history, exploratory notebooks, and figure-generation
scripts live in the [`mridecoder`](https://github.com/asaraog/mridecoder)
repository.
