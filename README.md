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

## Notebooks

- `classifier.ipynb`: Image classification implementation using fastai (based on fastbook course)
- `llm_vision.ipynb`: Original implementation integrating LangChain with vision-based LLMs for advanced image understanding and processing

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