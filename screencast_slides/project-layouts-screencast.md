---
title: Project organisation
author: Hans-Martin von Gaudecker
organization: Department of Economics, Universität Bonn
course: Effective Programming Practices for Economists
copyright: Creative Commons
---

### Guiding principles

- Clear separation of inputs and outputs
- Group files in directories by step of the analysis

### Files / directories

- **.git**
- **src**
- **tests**
- **paper**
- README.md
- .gitignore
- environment.yml
- .pre-commit-config.yaml
- MANIFEST.in
- pyproject.toml
- setup.cfg

### src/minimum_wages

*(only Python example)*

- **data**
- **data_management**
- **analysis**
- **final**
- __init__.py
- config.py
- utilities.py

### bld/python

*(after running pytask)*

- data
- models
- predictions
- figures
- tables

### Additional files in project root directory

*(after running pytask)*

- minimum_wages.pdf
- minimum_wages_pres.pdf