---
title: Project organisation
author: Hans-Martin von Gaudecker
copyright: Creative Commons
theme: dracula
math: mathjax
footer: Hans-Martin von Gaudecker
header: Project organisation
paginate: true
marp: true
size: 4K
---

# Project organisation

Hans-Martin von Gaudecker

---

# Guiding principles

- Clear separation of inputs and outputs
- Group files in directories by step of the analysis

---

# Files / directories

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

---

# src/minimum_wages

_(only Python example)_

- **data**
- **data_management**
- **analysis**
- **final**
- **init**.py
- config.py
- utilities.py

---

# bld/python

_(after running pytask)_

- data
- models
- predictions
- figures
- tables

---

# Additional files in project root directory

_(after running pytask)_

- minimum_wages.pdf
- minimum_wages_pres.pdf
