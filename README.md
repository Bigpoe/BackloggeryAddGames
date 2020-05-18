# README

This is a Python application that allows you add games to you **Backloggery** profile. This application is a WIP, so you can expect future improvements.

A csv file with the games information is needed inside the **utils** folder. An example is provided inside the aforementioned folder.

### Requirements

* Python 3.7 or later. You can install it from [here](https://www.python.org/downloads/).

### Progress status

For the **Progress status** options, make sure follow these conventions in the `progress_status` column of the .csv file:

* Unfinished/unfinished
* Beaten/beaten
* Completed/completed
* Null
* Mastered/mastered

### Wishlist

If you want to add a game to your wishlist, write `1` in the **wishlist** column, otherwise the wishlist checkbox will be ignored.

### Instructions for Mac/Unix/Linux

1. Download the repo.
2. Open a terminal.
3. `cd` to the repo folder, for instance `cd Documents/BackloggeryAddGames`
4. (**Optional**) create a python virtual environment:
	1. Run this command to create a virtual environment:
  `python3 -m venv /path/to/new/virtual/environment` , for instance `python3 -m venv my_venv`

	2. Activate your virtual environment: 
`source venv/bin/activate`

5. Run `pip install -r requirements.txt`
6. Run `python -m pytest ./scripts/add_games/add_games_script.py --show-capture=stdout -v -s`

### Instructions for Windows

**Work in progress**
