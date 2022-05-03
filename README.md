[![Known Vulnerabilities](https://snyk.io/test/github/Patrowl/PatrowlSDK/badge.svg)](https://snyk.io/test/github/Patrowl/PatrowlSDK)

# Patrowl
Patrowl is an innovative product designed by cybersecurity experts. It automates the detection and remediation of your vulnerabilities to finally be faster and more efficient than cybercriminal organizations.

It is built around 4 main principles:
 - Thanks to Artificial Intelligence coupled with our expertise, Patrowl automates continuous penetration tests. This allows us to identify your assets (known and  shadow-it) and vulnerabilities in real time over a wide area.
 - At a glance, visualize your overall level of security and especially how to improve it.
 - Real adapted solutions appear on the Dashboard. You will be able to act yourself or quickly transmit the solution directly to the teams concerned and follow the remediation.
 - Then Patrowl lets you make sure everything has been fixed with one click, by retesting.

This solution is simple, easy to learn and makes cybersecurity accessible to everyone. Our watchword: **demotivate cybercriminals**

# PatrowlSDK
Python API Client for Patrowl Dashboard Application

# License
PatrowlSDK is an open source and free software released under the [AGPL](https://github.com/Patrowl/PatrowlSDK/blob/master/LICENSE) (Affero General Public License). We are committed to ensure that PatrowlSDK will remain a free and open source project on the long-run.

# Updates
Information, news and updates are regularly posted on [Patrowl.io Twitter account](https://twitter.com/patrowl_io).

# Contributing
Please see our [Code of conduct](https://github.com/Patrowl/PatrowlDocs/blob/master/support/code_of_conduct.md). We welcome your contributions. Please feel free to fork the code, play with it, make some patches and send us pull requests via [issues](https://github.com/Patrowl/PatrowlSDK/issues).

If you need to contact the project team, send an email to <getsupport@patrowl.io>.

# Copyright
Copyright (C) 2021-2022 [Patrowl](https://patrowl.io)

# Pypi Deployment commands
```
rm -rf dist/ build/ PatrowlSDK.egg-info
python setup.py sdist bdist_wheel
twine upload -u Patrowl dist/*
```

# Tests
- Default: `python3 -m pytest tests/`
- Verbose: `python3 -m pytest tests/ -vv -s`
