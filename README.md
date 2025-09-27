# gdoc-text-extractor

<p align="left">
  <img alt="python" src="https://img.shields.io/badge/python-3.8%2B-blue" />
  <img alt="tests" src="https://img.shields.io/badge/tests-pytest-green" />
  <img alt="license" src="https://img.shields.io/badge/license-MIT-lightgrey" />
</p>

> **A small Python CLI that downloads a published Google Doc, parses `(x-coordinate, character, y-coordinate)` triples from its visible text, and reconstructs the original text layout for analysis or display.**

---

## 🚀 Quick overview

`gdoc-text-extractor` reads the visible text from a *published* Google Doc (HTML), detects groups of three lines as the coordinates `(x, char, y)`, and rebuilds each output row by placing characters at their X positions for every Y row (rendering from top `max(Y)` down to `min(Y)`). It supports block characters such as `█` and `░` and can print to stdout or write to a file.

---

## 🔗 Official input (assessment)

This repository references the official assessment table (the canonical input dataset).  
**Published table (input data for assessment):**  
https://docs.google.com/document/d/e/2PACX-1vSZ9d7OCd4QMsjJi2VFQmPYLebG2sGqI879_bSPugwOo_fgRcZLAFyfajPWU91UDiLg-RxRD41lVYRA/pub

> The table contains rows with three ordered columns — `x-coordinate`, `Character`, `y-coordinate` — which encode each character's grid position. The repo uses this document as the sample/test data.

---

## 🖨️ Sample output (from the assessment table)


```text
   ███████░  ██████████░ ██████░ ██░    ███░   ████████░   ██░           ███░ ████████░
 ███░    ██░ ██░           ██░   ██░  ███░   ███░     ███░ ███░   ███░   ██░  ██░     ██░
███░         ██░           ██░   ██░███░     ██░       ██░  ██░  █████░ ███░  ██░      ██░
██░          ████████░     ██░   ████░       ██░       ██░  ███░ ██░██░ ██░   ██░      ██░
███░         ██░           ██░   ██░███░     ██░       ██░   ██░██░ ██░██░    ██░      ██░
 ███░    ██░ ██░           ██░   ██░  ███░   ███░     ███░   ████░   ████░    ██░     ██░
   ███████░  ██████████░ ██████░ ██░    ███░   ████████░      ██░     ██░     ████████░
