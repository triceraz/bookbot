# BookBot

BookBot is a simple Python command-line tool for analyzing the text of books. It counts words, character frequency, word length distribution, and can generate visual plots using `matplotlib`.

---

## Features

* Count total words in a book.
* Count the frequency of each character (supports English letters and `æ, ø, å`).
* Count and analyze word lengths.
* Display pretty-printed statistics in the terminal.
* Generate histograms of word lengths using `matplotlib`.

---

## Requirements

* Python 3.7 or higher
* `matplotlib`

Install dependencies with:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
matplotlib==3.9.4
```

---

## Usage

Run the program from the terminal:

```bash
python3 main.py <path_to_book>
```

Example:

```bash
python3 main.py my_book.txt
```

The program will:

1. Print total word count.
2. Print character frequency sorted from most to least frequent.
3. Ask if you want plots of word length distribution.

   * Type `yes` to see a bar chart.
   * Type `no` to skip plotting.

---

## Project Structure

```
BookBot/
│
├─ main.py       # Entry point for the program
├─ stats.py      # Functions to analyze text
├─ plots.py      # Functions to generate matplotlib plots
├─ requirements.txt
└─ README.md
```

---

## Example Output

```
============ BOOKBOT ============
Analyzing book found at my_book.txt
----------- Word Count ----------
Found 5231 total words
--------- Character Count -------
e: 420
t: 380
a: 350
...
============= END ===============
```

If you choose to plot, a bar chart of word length distribution will appear.

---
