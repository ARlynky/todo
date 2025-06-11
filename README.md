
# TODO

This repo is for **personal use** and not intended for public consumption (yet!)
I’m using it to learn how to share CLI tools and packages like a real developer.

if you saw my first repo [https://github.com/ARlynky/fortune] you will se a lot of
similarities in the readme just because the nature of this project is the same.

A simple script that prints a random "todo list"

---

## 🛠 Installation

> ⚠️ Only works on **Linux-based systems** (for now)

To install this package, run the following command in your terminal:

```sh
curl -sSL https://raw.githubusercontent.com/ARlynky/todo/main/install.sh | bash
```

This will:

* Clone the repo into `~/.local/share/todo`
* Add a launcher to `~/.local/bin/todo`
* Let you run `todo` from anywhere (if `~/.local/bin` is in your `PATH`)

## 🛠 Updating

You can update it via running the install script again either from the
repo (.local/share/install.sh) or from the web like before
note this will reset your fortunes.txt file if you edited it
although this project is still a work in progress and small
so i don't think you should care to update

---

## 📂 Project Structure

todo/
├── todo.py          # The main script
├── data.json        # your todo(s)
├── install.sh       # Install script for quick setup
└── README.md

---

## Notes

* This is a learning repo, so stuff might break or change often.
* Feel free to fork or copy if you're also learning how to share CLI tools!

---

## Why This Exists

I'm experimenting with lightweight ways to share personal tools — using
Git, Bash, Python, and curl — without needing to dive into full
package managers like `apt`, `pacman`, or PyPI (yet).
