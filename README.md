# Neural EEG Decoding of Smell

Download or git clone this project onto local machine into folder on local machine.

```
git clone https://github.com/asaraog/msdsthesis.git

cd msdsthesis
pip install zenodo_get
zenodo_get 6387085
unzip Kato_et_al.zip
ls
```

## Contents

| File                               | Description                                                                                                                                                                                                                                    |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `eeg_decoding_citcyc.ipynb`      | Primary analysis notebook: model training, temporal/spatial/spatiotemporal occlusion analysis, class-specific occlusion, decision-threshold sweep, and paper comparison.                                                                       |
| `eeg_decoding_citcyc.html`       | Rendered HTML export of the analysis notebook (collapsible sections).                                                                                                                                                                          |
| `citcyc_cnn_lstm_model.keras`    | Final saved Keras model used for Cit vs Cyc evaluation and thesis figure generation. Includes the trained network architecture and weights.                                                                                                    |
| `compute_kato_baseline.py`       | Standalone script that reproduces the 54% Kato et al. (2022) cross-subject ridge-regression baseline by loading `4-2vs9-2.mat` and averaging `MVPA.accs` over the 22 LOSO subject folds and 31 post-odor decoding time points (t ≥ 0 ms). |
| `kato_cit_cyc_grid2d_events.pkl` | Pre-processed Cit vs Cyc trial data in 2-D grid format (28 time bins, 10×11 grid, 2 channels). Direct input for model training and evaluation.*Tracked via Git LFS.*                                                                        |

## External data

The full upstream dataset is available at
[https://zenodo.org/records/6387085](https://zenodo.org/records/6387085) under `Kato_et_al/`.
