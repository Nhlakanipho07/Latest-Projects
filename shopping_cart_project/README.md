# Shopping Cart 

## Brief Overview:

This project is a digital shopping cart where each function is a feature of the shopping cart. 

## Setup:

- First clone this repository:

    - run ```git clone git@github.com:Umuzi-org/Nhlakanipho-Ngubo-705-contentitem-python.git``` in git bash or linux terminal

- Then download this [data](http://syllabus.africacode.net/projects/understanding-loops/data.json). 
- Navigate to the shopping cart directory and make sure that the data you have downloaded is in this directory, so that ```data.json``` and ```shopping_cart.py``` are in the same directory.

- Then copy the following code:
```
import json


with open("data.json", "r") as baskets:
    shopping_baskets = json.load(baskets)
```
- Open shopping_cart.py and paste the above code at the top of this file.
- The above code safely opens the data that you have downloaded, so that the contents of that data can be used by any of the functions in the project, whenever that function is called. It then closes that data when it is not in use.

#### ***You should be able to run any function of this project once you have followed all the instructions stated above.*** 