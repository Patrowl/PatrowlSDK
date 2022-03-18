# Patrowl4py
Python API Client for PatrowlDashboard

# Pypi Deployment commands
```
rm -rf dist/ build/ PatrowlSDK.egg-info
python setup.py sdist bdist_wheel
twine upload dist/*
```

# Tests
- Default: `python3 -m pytest tests/`
- Verbose: `python3 -m pytest tests/ -vv -s`
