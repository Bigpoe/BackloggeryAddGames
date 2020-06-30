# README

This is a `Python` + `SeleniumWebDriver` application that allows you add games to you **Backloggery** profile. This application is a WIP, so you can expect future improvements.

A csv file with the games information is needed inside the **utils** folder. An example is provided inside the aforementioned folder.

## Requirements

* Python 3.7 or later. You can install it from [here](https://www.python.org/downloads/).

## Setup you credentials

In the folder **backloggery_add_games/config** you will see a `config_sample.py` file. Open it using plain text editor. Replace the keys   `your_username` and `your_password` with your Backloggery username and password and save the changes on the document.

Now, rename the file from `config_sample.py` to `config.py`.

## Add your games to a .csv file

There are tow `.csv` fils in **backloggery_add_games/utils** directory, `games_list_detailed.csv` and `games_list_simple.csv`. Depending on the way you want to add your games, open the proper .csv file to prepare your games information following the example in the file.

### Ownership

For the **Ownership** options, make sure to follow these conventions in the `ownership` column of the .csv file:

* Owned - owned
* Household - household
* Subscription - subscription
* Borrowed/Rented - borrowed/rented
* Formerly Owned - formerly owned
* Other - other

Or leave it empty to ignore it.

### Progress status

For the **Progress status** options, make sure to follow these conventions in the `progress_status` column of the .csv file:

* Unfinished - unfinished
* Beaten - beaten
* Completed - completed
* Null
* Mastered - mastered

Or leave it empty to ignore it.

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

- Find a way to create portable version
  

## Version 1.0.0

## Instructions

### Run script from command line

1. Download the repo.
2. Open a terminal.
3. `cd` to the repo folder, for instance `cd Documents/BackloggeryAddGames`
4. `cd` to `backloggery_add_games`folder.
5. (**Optional**) create a python virtual environment:
    1. Run this command to create a virtual environment:
  `python3 -m venv /path/to/new/virtual/environment` , for instance `python3 -m venv my_venv`

    2. Activate your virtual environment: 
`source my_venv/bin/activate`

6. Run `pip install -r requirements.txt`
7. Run `python script_add_game_detailed.py` for **detailed option** or `script_add_game_simple.py` for **simple option**.

### Run script from user interface

1. Download the repo.
2. Open a terminal.
3. `cd` to the repo folder, for instance `cd Documents/BackloggeryAddGames`
4. `cd` to `backloggery_add_games`folder.
5. (**Optional**) create a python virtual environment:
	1. Run this command to create a virtual environment:
  `python3 -m venv /path/to/new/virtual/environment` , for instance `python3 -m venv my_venv`

	2. Activate your virtual environment: 
`source my_venv/bin/activate`

6. Run `pip install -r requirements.txt`
7. Run `python gui_script.py ` for summon the user interface.


## License 

This project is under [MIT license](LICENSE)
