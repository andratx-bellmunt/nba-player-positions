# 🏀 NBA Player Position Classification & Inference

Proof of concept of machine learning project leveraging official NBA player statistics to optimize positional classification, map hybrid styles of play, and infer missing historical labels.

## 🔗 Live Report
The full interactive data storytelling report—complete with narrative analysis and dynamic visualizations—is hosted live on my portfolio:
👉 **[View the Interactive Portfolio Report](https://andratx-bellmunt.github.io/portfolio/projects/nba.html)**

---

## 🛠️ Project Architecture

This repository is engineered using modular, industry-standard Python data pipelines. Heavy plotting logic and helper functions are isolated from the core narrative to keep code execution clean and readable.

```text
.
├── data/                  # Source CSV datasets
├── docs/                  # Clean production artifacts (rendered HTML)
├── src/
│   ├── notebooks/         # Narrative-driven analysis and modeling notebooks
│   └── utils/             # Modular Python utility scripts (e.g., plots.py)
├── templates/             # HTML injection fragments (analytics & tracking tokens)
├── _quarto.yml            # Automated Quarto build configurations
├── pyproject.toml         # Fast, reproducible dependency configurations (via uv)
└── uv.lock                # Deterministic lockfile for exact environment state
```


## 🚀 Quick Start & Reproducibility

This project utilizes `uv` for Python dependency management. Follow these steps to clone the repo and run the environment locally:

### Clone the Repository

```bash
git clone https://github.com/andratx-bellmunt/nba-player-positions.git
cd nba-player-positions
```

### Set Up the Environment

Ensure you have `uv` installed, then synchronize the environment (this will automatically create a virtual environment and install all pinned versions):
```bash
uv sync
```

### Explore the Code

To run the notebook with your active `uv` environment:

```bash
uv run jupyter notebook src/notebooks/nba.ipynb
```

## 📊 Methodology & Key Findings

* **Supervised Learning:** Built a classification model to systematically map hybrid/fluid modern player styles back to core labels and infer non-listed positional attributes.
* **Unsupervised Clustering:** Analyzed statistical playstyles rather than traditional court labels to identify emerging "shadow positions" in the modern NBA.


## 🗃️ Data Sources

Official NBA data has been retrieved via the API Python package available at PyPI: [nba_api](https://pypi.org/project/nba_api/).


## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
