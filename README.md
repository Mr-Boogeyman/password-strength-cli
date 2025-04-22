# AI Password Strength Checker (Linux CLI Tool)

This is a Python-based command-line tool that evaluates the strength of a password and checks if it has been compromised in known data breaches using the [Have I Been Pwned API](https://haveibeenpwned.com/API/v3).

---

## Features

- **Password Strength Scoring** — Based on length, complexity, and common password patterns.
- **Breach Check** — Uses the Have I Been Pwned k-anonymity API.
- **Lightweight CLI Tool** — Runs directly from the terminal on Linux.
- **Global Installation (Optional)** — Run as a global command (`password-strength`).

---

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/password-strength-cli.git
cd password-strength-cli
pip install .
