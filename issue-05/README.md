pip install -U pytest
pip install -U pytest-cov
python -m pytest --cov .\ -v .\issue-05.py
python -m pytest --cov .\ --cov-report html .\issue-05.py

