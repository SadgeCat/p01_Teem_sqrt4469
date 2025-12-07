# Teem_sqrt4469
# Roster
Yuhang Pan (PM), Matthew Ciu, Michelle Chen, Thomas Mackey
# Description
Our website is a local two-player Pokemon showdown game, where we use historical figures and superheroes as the characters using the Pantheon API and the Superheroes API. For the in-game stats, we will get data from those API’s and convert those info into in-game stats. Those stats with be assigned to moves from specific Pokemon and be given to the superheroes and historical figures.
# Install Guide
1. Clone the repository and navigate into the directory
```
git clone git@github.com:SadgeCat/p01_Teem_sqrt4469.git HeroWars
cd HeroWars
```
2. Create and active virtual environment
```
python -m venv venv
. venv/bin/activate
```
3. Install packages
```
pip install -r requirements.txt
```
# Launch Codes
1. Create database and launch app
```
python app/build_db.py
python app/__init__.py
```