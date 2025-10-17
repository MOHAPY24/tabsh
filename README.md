

# tabsh

**tabsh** — The Arabic BASH Shell
*A BASH superset integrating Arabic syntax for shell usage*

---

## Table of Contents

1. [Introduction](#introduction)
2. [Goals & Motivation](#goals--motivation)
3. [Features](#features)
4. [Current Limitations & Known Issues](#current-limitations--known-issues)
5. [Architecture & Design](#architecture--design)
6. [Installation & Usage](#installation--usage)

   * [Prerequisites](#prerequisites)
   * [Installation Steps](#installation-steps)
   * [Using tabsh](#using-tabsh)
   * [Configuration Files](#configuration-files)
   * [Examples](#examples)
7. [Testing](#testing)
8. [Contributing](#contributing)
9. [Roadmap & Future Work](#roadmap--future-work)
10. [License](#license)
11. [Acknowledgments](#acknowledgments)
12. [Contact / Support](#contact--support)

---

## 1. Introduction

`tabsh` is a shell extension / superset built on top of BASH that allows users to write shell commands using **Arabic syntax**. It’s designed to reduce the language barrier for Arabic-speaking users while keeping compatibility with standard BASH features.

With `tabsh`, you can write basic shell commands in Arabic directly in your terminal. The system translates the Arabic syntax into equivalent BASH commands under the hood and executes them transparently.

---

## 2. Goals & Motivation

* **Accessibility**: Help Arabic-speaking users who may not be familiar with English syntax use the command line more easily.
* **Integration**: Preserve compatibility with BASH to avoid breaking traditional workflows.
* **Customization**: Allow users to extend the Arabic command mappings based on their preferences or dialects.
* **Community-driven**: Encourage collaborative development of command translations and tooling.
* **Bridge to learning**: Help beginners understand shell scripting concepts by seeing them in their native language.

---

## 3. Features

* **Arabic command translation**: Translate supported Arabic commands to their BASH equivalents.
* **Interactive Arabic shell**: Use Arabic commands directly in the terminal.
* **Command history**: Maintains `.tabshhistory` for previously run commands.
* **Configuration support**: Custom user-defined settings via `.tabshrc`.
* **Fallback compatibility**: Falls back to BASH if a command isn’t translated.
* **Cross-platform**: Works on most UNIX-based systems (Linux, macOS, WSL).

---

## 4. Current Limitations & Known Issues

⚠️ Please note that `tabsh` is in early development, and not all shell syntax or constructs are yet supported:

1. The `.tabshrc` file **does not yet support** environment variables, functions, or aliases fully.
2. Control flow commands such as conditionals (e.g. `if`, `else`) or loops are **not yet supported** in Arabic.
3. Do **not** attempt to set `tabsh` as your default login shell via `chsh`—this can break your environment.
4. Use `tabsh` through the provided wrapper script (`tabsh.sh`) for now.
5. Only a limited set of basic commands are translated—full language coverage is still in progress.
6. Translating complex pipelines or redirections is not fully supported yet.

---

## 5. Architecture & Design

### Core Components

* **`tabsh.py`** — The main Python script that handles Arabic-to-BASH translation.
* **`tabsh.sh`** — The shell wrapper that invokes the translator and passes output to BASH.
* **`translations.py`** — Contains all Arabic-to-English keyword mappings.
* **`utils.py`** — Helper utilities for parsing, tokenizing, and transforming commands.
* **`.tabshrc`** — User config file.
* **`.tabshhistory`** — Arabic command history file.

### How It Works

1. You type a command in Arabic.
2. `tabsh.sh` intercepts the command and calls `tabsh.py`.
3. The Python script translates Arabic keywords into standard BASH.
4. The translated command is passed to BASH for execution.
5. Output is displayed as normal.

---

## 6. Installation & Usage

### Prerequisites

* Python 3.x
* Bash shell (or compatible)
* UNIX-like system (Linux, macOS, WSL)

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/MOHAPY24/tabsh.git
   cd tabsh
   ```

2. Make the main scripts executable:

   ```bash
   chmod +x tabsh.sh tabsh.py
   ```

3. Optionally, install any required Python packages:

   ```bash
   pip install -r requirements.txt  # if this file exists
   ```

4. Source the shell wrapper in your session (don’t use `chsh`):

   ```bash
   source /full/path/to/tabsh.sh
   ```

   Or run it directly:

   ```bash
   ./tabsh.sh
   ```

> ⚠️ Do not make `tabsh` your default shell. Use it as a command or via `source`.

---

### Using tabsh

Once `tabsh.sh` is sourced or run, you can enter supported Arabic commands directly into your terminal, and they will be translated and executed.

For example:

```bash
اطبع "مرحبا"
```

This will be translated and executed as:

```bash
echo "مرحبا"
```

You can also mix Arabic commands with regular BASH:

```bash
ls -l
اطبع "تم عرض الملفات"
```

If a command is not recognized in Arabic, `tabsh` will pass it directly to BASH without translation.

---

### Configuration Files

* **`.tabshrc`**: Optional user config file for defining custom behavior (in progress).
* **`.tabshhistory`**: Stores a history of Arabic commands used in the shell.

---

### Examples

Here are some example commands that work with `tabsh`:

```bash
اطبع "مرحباً بالعالم"
```

```bash
انشئ_مجلد test_folder
```

```bash
اذهب test_folder
```

```bash
انشئ_ملف ملف.txt
```

These will be translated to standard shell equivalents like `echo`, `mkdir`, `cd`, and `touch`.

---

## 7. Testing

To test `tabsh`, run the shell and enter some of the supported Arabic commands. Verify that:

* The command is executed as expected
* The translation is correct
* The command is saved in `.tabshhistory`

More formal testing (unit tests) is planned for future releases.

---

## 8. Contributing

We welcome contributions of all kinds! You can:

* Add new Arabic command mappings
* Improve the translation engine
* Submit bug fixes
* Propose or help implement new features
* Expand documentation and examples

Before submitting pull requests, please:

* Follow consistent coding style
* Document any new features clearly
* Test your changes
* Avoid breaking existing functionality

You can start by checking open issues or suggesting improvements.

---

## 9. Roadmap & Future Work

| Feature / Enhancement                | Status   | Notes                                     |
| ------------------------------------ | -------- | ----------------------------------------- |
| Support for `.tabshrc` (full syntax) | Planned  | Environment variables, functions, aliases |
| Add more Arabic command mappings     | Ongoing  | Core focus                                |
| Improve fallback behavior            | Ongoing  | Handle unsupported syntax better          |
| Script (.tabsh) support              | Future   | Requires syntax coverage                  |
| Conditional/loop support in Arabic   | Future   | Not yet implemented                       |
| Plugin system for dialects           | Proposed | User-definable extensions                 |
| CLI installer                        | Proposed | Easier setup process                      |

---

## 10. License

This project is licensed under the **GNU GPL v3.0**. See the [LICENSE](LICENSE) file for full details.

---

## 11. Acknowledgments

* To the Arabic-speaking development community for inspiration.
* Open source shell tools that laid the groundwork.
* Early users and testers providing feedback and ideas.

---

## 12. Contact / Support

* GitHub Issues: [Submit here](https://github.com/MOHAPY24/tabsh/issues)
* Pull Requests: Always welcome
* Maintainer: [MOHAPY24](https://github.com/MOHAPY24)

---

Let me know if you’d like this delivered as a `.md` file or want a shorter version for display on the GitHub repo page.
