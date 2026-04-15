<h1 align="center">
    MATEC
</h1>

<p align="center">
    <strong>Version: 0.3.0 (Beta)</strong><br>
    MATEC (MathTech) is a high-performance, syntax‑based math tool and Domain Specific Language (DSL) prototype built with Python.
</p>

> MATEC uses **Syntax-like commands** instead of tedious nested menus for a seamless mathematical workflow.

<p align="center">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
    <a href="https://github.com/leverec/MATEC/blob/main/CHANGELOG.md">
        <img src="https://img.shields.io/badge/version%200.3.0-yellow?style=for-the-badge">
    </a>
    <a href="http://www.apache.org/licenses/">
        <img src="https://img.shields.io/badge/Apache--2.0%20License-maroon?style=for-the-badge">
    </a>
    <a href="https://github.com/leverec/MATEC/blob/main/CHANGELOG.md">
        <img src="https://img.shields.io/badge/changelog-darkgreen?style=for-the-badge">
    </a>
    <a href="https://github.com/leverec/MATEC/blob/main/Syntax.md">
        <img src="https://img.shields.io/badge/syntax%20documentation-purple?style=for-the-badge">
    </a>
</p>

## Installation & Usage
**1. Clone This Repository**
```bash
git clone https://github.com/leverec/MATEC.git
cd MATEC
```

**2. Run The Script**
```bash
python main.py
```
*Use `python main.py --debug` or `-d` to enable enhanced error feedback and debug features.*

**3. Enter Commands**

_Example (Geometry):_
```text
$ circle r 7
Radius        : 7
Diameter      : 14
Circumference : 43.98
Area          : 153.94
```

_Example (Advanced Arithmetic):_
```text
$ 21 + 72 : 2 ^ √36 + (76 - 22) * (86 - -19) ÷ π × e
4928.13
```

_Example (Settings Management):_
```text
$ settings set precision 10
[D1] 'precision' has been updated to '10'
$ 21 + 72 : 2 ^ √36 + (76 - 22) * (86 - -19) ÷ π × e
4928.1264033809
```

**4. Exit the program**
Type `exit` or `q` to close the session.

## Roadmap & Goal
**MATEC** is currently in its Beta stage using Python for logic prototyping. The long-term goal is to rewrite the entire engine in **Rust/C++** to transform it into a standalone, low-level compiled language optimized for **AI** and **heavy mathematical computations.**

## Contributing
This is actually a personal project, but ideas and suggestions are welcome. Feel free to open an issue or fork the repo.

## License
[**MATEC**](#matec) is free software licensed under the [**Apache License 2.0**](https://opensource.org/licenses/Apache-2.0) see the [**LICENSE**](https://github.com/leverec/MATEC/blob/main/LICENSE) file for details.

---

> [!NOTE]
> **AI-Assisted:** ALL Markdown files in this repository were written with AI assistance. While I understand English, I find it **difficult** to explain things clearly in it. If any part feels off or confusing, please ask me directly in [**Bahasa Indonesia**](https://en.wikipedia.org/wiki/Indonesian_language) for a better explanation.
>
> **Accuracy:** For highly technical inquiries or if you find any discrepancies, feel free to contact me directly on my social media. I'm more than happy to discuss the project in [**Bahasa Indonesia**.](https://en.wikipedia.org/wiki/Indonesian_language)
