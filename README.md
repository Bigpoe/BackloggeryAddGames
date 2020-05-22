# README

This is a `Python` + `SeleniumWebDriver` application that allows you add games to you **Backloggery** profile. This application is a WIP, so you can expect future improvements.

A csv file with the games information is needed inside the **utils** folder. An example is provided inside the aforementioned folder.

### Requirements

* Python 3.7 or later. You can install it from [here](https://www.python.org/downloads/).

### Add your games to a .csv file

In order to use this application, you need to add your games details to a csv file named **games_list_detailed.csv** located in **utils** folder. There is an example in the file, so you can follow it to add your game's information.

### Ownership

For the **Ownership** options, make sure to follow these conventions in the `ownership` column of the .csv file:

* Owned - owned
* Household - household
* Subscription - subscription
* Borrowed/Rented - borrowed/rented
* Formerly Owned - formerly owned
* Other - other

Or it in empty to ignore it.

### Progress status

For the **Progress status** options, make sure to follow these conventions in the `progress_status` column of the .csv file:

* Unfinished - unfinished
* Beaten - beaten
* Completed - completed
* Null
* Mastered - mastered

Or it in empty to ignore it.

### Rating level

For the **Rating** options, make sure to follow these conventions in the `rating` column of the .csv file:

* 5
* 4
* 3
* 2
* 1
* 0

### Now Playing

If you want to mark a game as `Now Playing`, write `1` in the **now_playing** column in the csv file, otherwise the `Now Playing` checkbox will be ignored.

### Wishlist

If you want to add a game to your `Wishlist`, write `1` in the **wishlist** column in the csv file, otherwise the `Wishlist` checkbox will be ignored.

## To do

- Re-factor the method for adding games in 'simple mode'.
- Enable option to choose between simple and detailed method.

## Version 1.0.0

### Instructions for Mac

### Run from GUI

1. Download the repo.
2. Open a terminal.
3. `cd` to the repo folder, for instance `cd Documents/BackloggeryAddGames`
4. (**Optional**) create a python virtual environment:
	1. Run this command to create a virtual environment:
  `python3 -m venv /path/to/new/virtual/environment` , for instance `python3 -m venv my_venv`

	2. Activate your virtual environment: 
`source my_venv/bin/activate`

5. Run `pip install -r requirements.txt`
6. Run `python ./gui/gui_script.py` to generate the GUI.
7. Click on the option you wish to use.

### Run from pyTest

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
