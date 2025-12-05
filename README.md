# Runtime 2025-12-05-a

A Jupyter notebook environment for AI engineering and prototyping.

## Setup

### Prerequisites
- Python 3.12+
- uv package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/PhonxayMax/9781633434615.git
cd 9781633434615
```

2. Create virtual environment:
```bash
uv venv
```

3. Install dependencies:
```bash
uv pip install -r requirements.txt
```

4. Open in VS Code:
```bash
code .
```

## Project Structure

```
9781633434615/
├── .gitignore          # Git ignore rules (excludes .env, .venv, etc.)
├── .vscode/
│   └── settings.json   # VS Code Python & Jupyter configuration
├── requirements.txt    # Python dependencies
├── index.ipynb         # Main Jupyter notebook
└── README.md          # This file
```

## Dependencies

- **jupyter** - Interactive notebook environment
- **notebook** - Jupyter Notebook interface
- **ipykernel** - Python kernel for Jupyter
