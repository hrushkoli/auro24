## sync py and ipynb files example.sync.py and example.sync.ipynb.

python -m jupyter_ascending.scripts.make_pair --base example

## Start jupyter and open the notebook:

python -m jupyter notebook example.sync.ipynb

## Add some code to the .sync.py file, e.g.

echo 'print("Hello World!")' >> example.sync.py

## Sync the code into the jupyter notebook:

python -m jupyter_ascending.requests.sync --filename example.sync.py

## Run that cell of code

python -m jupyter_ascending.requests.execute --filename example.sync.py --line 16

