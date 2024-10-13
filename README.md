# wape-orm-lab

## Setup Instructions

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

1. **Clone the repository & install Poetry**:
   ```bash
   git clone https://github.com/Obscurity-Labs-Training/wape-orm-lab.git
   cd wape-orm-lab
   poetry install --no-root
   poetry  shell
   ```

2. **Create Local DB**:
   ```bash
   python create_db.py
   ```