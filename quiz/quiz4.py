"""


I could not finish exercise 1 or 2 (and the rest). I will use this quiz as the one I drop. I'll look into more practice for dictionaries + APIs, not really sure the hw helped as much to prepare for this as I'd like it to.


"""


"""
-------------------------------------------------------------------------------
Q1. There are 351 towns/cities in Massachusetts according to 2020 Census. An API (http://107.173.19.148/mass) provides data of all town names (and other information) in JSON format. Please complete the function below to read the names into a list. Each name will be one item in the list. This list should be sorted alphabetically.

You may create additional helper function(s) if needed, but you are not allowed to change headers of the required functions.
-------------------------------------------------------------------------------
"""

import urllib.request
import json
import pprint

url = "http://107.173.19.148/mass"

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    d = response_data

def get_town_names() -> list:
    """
    Returns a sorted list of town names
    """
    f = []
    for s in d['name']:
        for r in d['towns']:
            f.append(r['name'])
    return sorted(f)

# get_town_names()
# When you've completed your function, uncomment the following lines and run this file to test!
names = get_town_names()
print(type(names), len(names))
print(names)

## Expected output:
## <class 'list'> 351
## ['Abington', 'Acton', 'Acushnet', 'Adams', 'Agawam', 'Alford', 'Amesbury', 'Amherst', ..., 'Yarmouth']


"""
-------------------------------------------------------------------------------
Q2. Please complete the function that takes a town's name as an argugment and returns the population of the town. If the given name is not a valid town in Massachusetts, the function should return 0.

You may create additional helper function(s) or use previous function(s) if needed, but you are not allowed to change headers of the required functions.
-------------------------------------------------------------------------------
"""


def get_population_by_name(town_name: str) -> int:
    """
    Returns the population of the given town, 0 if the town's name is invalid
    """
    print(d.get['towns'][town_name]['population'])

## When you've completed your function, uncomment the following lines and run this file to test!
# print(get_population_by_name('Wellesley'))
# print(get_population_by_name('New York'))


## Expected output:
## 29550
## 0


"""
-------------------------------------------------------------------------------
Q3. Which town/city is the largest by population in Massachusetts? Of course it is Boston. But do you know which town is the smallest? Please complete the function that returns the town's name that has the smallest population in Massachusetts.

Note: 
- You are not allowed to use key=xxx in any of the built-in functions.
- You may create additional helper function(s) or use previous function(s) if needed, but you are not allowed to change headers of the required functions.
-------------------------------------------------------------------------------
"""


def find_smallest_town() -> str:
    """
    Returns the town's name that has the smallest population.

    You are not allowed to use key=xxx in any of the built-in functions.
    """


## When you've completed your function, uncomment the following lines and run this file to test!
# smallest = find_smallest_town()
# print(smallest)

## Expected output:
## Gosnold # There are only 70 people in that town based on 2020 Census.


"""
-------------------------------------------------------------------------------
Q4. You may have noticed you are the mayor of one or several towns in Massachusetts. Please complete the function that returns a dictionary - in this dictionary, key is mayor's name and value is a list of towns that the mayor is managing. You can find example from the expected output below.

You may create additional helper function(s) or use previous function(s) if needed, but you are not allowed to change headers of the required functions.
-------------------------------------------------------------------------------
"""


def get_mayors_dict() -> dict:
    """
    Returns a dictionary that maps mayors to their towns, {str: list}
    """


## When you've completed your function, uncomment the following lines and run this file to test!
# mayors_dict = get_mayors_dict()
# print(mayors_dict['Sabi'])  # you can replace Sabi with your own name

## Expected output - it is ok if the order is different:
## ['Gloucester', 'Huntington', 'New Bedford', 'Richmond', 'Spencer', 'Stoughton', 'Wakefield', 'Wellesley', 'Weymouth', 'Williamsburg', 'Winchendon', 'Winchester', 'Wrentham']


"""
-------------------------------------------------------------------------------
Q5. Have you wondered how many people you are managing? Please complete the function that returns a list of all the mayor names sorted by the total population they manage from most to least. You can find example from the expected output below.

You may create additional helper function(s) or use previous function(s) if needed, but you are not allowed to change headers of the required functions.
-------------------------------------------------------------------------------
"""


def sort_mayors_by_pop() -> list:
    """
    Returns a list that records the mayor names sorted by the total population
    they are managing from most to least.
    """


## When you've completed your function, uncomment the following lines and run this file to test!
# sorted_mayor_list = sort_mayors_by_pop()
# print(sorted_mayor_list) # Ashley is the busiest mayor because she manages almost 800K people, while there are only 1212 people in Stephen's town(s).

## Expected output:
## ['Ashley', 'Ajay', 'Sabi', 'Rohan', 'Olivier', 'Olivia', 'Aryan', 'Andrew', 'Joey', 'Lily', 'Ronald', 'Vicky', 'Juanse', 'Alice', 'Mariale', 'Larry', 'Magnus', 'Ally', 'Michelle', 'Derek', 'Jack', 'Alec', 'Jeffrey', 'Junwei', 'Mark', 'Carina', 'Isaac', 'Shivant', 'Shawn', 'Niusha', 'Nina', 'Natalie', 'Arman', 'Zheng', 'Nan', 'Michael', 'Luna', 'Immanuel', 'Fede', 'Lila', 'Briana', 'Thomas', 'Max', 'Eric', 'Jenny', 'Vincent', 'Hardik', 'Stephen']