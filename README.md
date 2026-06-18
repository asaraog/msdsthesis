# Neural Decoding of Smell with Artificial Intelligence

**Author:** Apoorv Saraogee, Northwestern University

## Quick Start

```bash
git clone https://github.com/asaraog/msdsthesis.git
cd msdsthesis
pip install zenodo_get
zenodo_get 6387085
unzip Kato_et_al.zip
```

## Contents

| File | Description |
| --- | --- |
| `eeg_decoding_AS.ipynb` | Primary analysis notebook: model training, temporal/spatial/spatiotemporal occlusion analysis, class-specific occlusion, decision-threshold sweep, and paper comparison. |
| `eeg_decoding_AS.html` | Rendered HTML export of the analysis notebook (collapsible sections). |
| `models/fold_1..5.keras` | Trained CNN-LSTM fold models from 5-fold subject-aware cross-validation. |
| `kato_cit_cyc_grid2d_events.pkl` | Pre-processed Cit vs Cyc trial data in 2-D grid format (28 time bins, 10×11 grid, 2 channels). Direct input for model training and evaluation. |
| `compute_kato_baseline.py` | Standalone script that reproduces the 54% Kato et al. (2022) cross-subject ridge-regression baseline. |

## Data

The preprocessed EEG trials and full upstream dataset are available on Zenodo:
[https://zenodo.org/records/6387085](https://zenodo.org/records/6387085) (DOI: 10.5281/zenodo.6387085)
