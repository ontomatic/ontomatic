# Ontomatic

## Installation

```bash
git clone https://github.com/ontomatic/ontomatic.git
cd ontomatic

uv venv .venv

# Windows
.venv\bin\activate.bat
# macOS
source .venv/script/activate

uv sync --all-package --locked
```

## Run

From project root directory,

### Run API

```bash
# Windows
copy packages/backend/.env.example packages/backend/.env 
# macOS / Linux
cp packages/backend/.env.example packages/backend/.env

# After filling environment variables
dockerc compose up -d

uv run --package backend api
```

### Run Streamlit

```bash
cd packages/frontend
uv run streamlit run app.py
```
