# ML Notebooks

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Python](https://img.shields.io/badge/Python-3.11.5-blue?logo=python)](https://python.org/)
[![FastAI](https://img.shields.io/badge/FastAI-2.7.13-blue)](https://fast.ai/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.5.1-blue?logo=pytorch)](https://pytorch.org/)

A collection of machine learning notebooks focused on practical implementation using fastai. These notebooks serve as both learning resources and quick reference guides for various ML tasks.

## Features

- 🖼️ Image Classification with Deep Learning
- 🤖 LLM Vision Integration
- 📊 Probability-based Predictions
- 📓 Interactive Jupyter Notebooks
- 🔄 Quick Reference Examples

## Project Structure

```
notebooks/
├── fastai_course/
│   ├── classifier.ipynb      # Image classification using fastai
│   └── tabular.ipynb        # Tabular data prediction examples
└── custom/
    └── llm_vision.ipynb     # LangChain with vision-based LLMs
```

```
src/
├── utils/
│   ├── search_images.py     # Image search utilities
│   └── exponential_backoff.py  # API retry logic
└── __init__.py
```

```
data/
├── models/                  # Saved model files
├── raw/                    # Raw datasets
└── processed/              # Processed datasets
```

## Notebooks

- `notebooks/fastai_course/classifier.ipynb`: Image classification implementation using fastai (based on fastbook course)
- `notebooks/fastai_course/tabular.ipynb`: Tabular data prediction examples using fastai
- `notebooks/custom/llm_vision.ipynb`: Original implementation integrating LangChain with vision-based LLMs

## Disclaimer

[![Status](https://img.shields.io/badge/Status-Active_Development-success)](https://github.com/pushakargaikwad/ml-notebooks)
[![Purpose](https://img.shields.io/badge/Purpose-Learning_&_Implementation-blue)](https://github.com/pushakargaikwad/ml-notebooks)
[![Code](https://img.shields.io/badge/Code-Updated_&_Working-green)](https://github.com/pushakargaikwad/ml-notebooks)

While some of the code and techniques referenced in this repository may be from materials that are a year or two old, the purpose of this repository is to:
- Consolidate learning materials in one accessible place
- Ensure all code is running with current library versions
- Update implementations as needed
- Demonstrate practical, real-world applications
- Serve as a foundation for more advanced implementations

The focus is on practical implementation and getting things working in real scenarios, rather than just theoretical concepts.
## Prerequisites


Before you begin, ensure you have the following installed:
- Python 3.11.5 or higher
- fastai 2.7.13
- PyTorch 2.5.1
- Jupyter Lab/Notebook

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/pushakargaikwad/ml-notebooks.git
   cd ml-notebooks
   ```

2. Create and activate conda environment:
   ```bash
   conda create -n fastbook python=3.11.5
   conda activate fastbook
   conda install -c fastai fastai
   conda install pytorch torchvision -c pytorch
   conda install jupyter
   ```

## Usage Example

```python
# Load and predict using a trained model
predicted_category, _, probs = learn.predict(PILImage.create('bird.jpg'))
print(f"This is a: {predicted_category}")
print(f"Probability: {probs[0]:.4f}")
```

## License

This project is Free Software, released under the GNU Affero General Public License (AGPL-3.0). This means you have fundamental freedoms to use and enhance this software:

### Your Freedoms
- ✨ You can use these notebooks for any purpose
- 🔄 You can study and modify the code
- 🌍 You can share the notebooks with others
- 🛠️ You can share your modifications

For complete license details, see the [LICENSE](LICENSE) file.

## Credits

This repository contains notebooks and code created while following the [Practical Deep Learning for Coders](https://course.fast.ai/) course and studying the [fastbook](https://github.com/fastai/fastbook). While it serves as learning notes and reference material from the course, it will be expanded with additional content from other sources and original implementations.

The fastai library and course materials have been instrumental in learning deep learning concepts and practical implementations. Special thanks to Jeremy Howard, Sylvain Gugger, and the fastai team for their excellent educational resources.

## Copyright

Copyright © 2025, Pushakar Gaikwad and contributors.