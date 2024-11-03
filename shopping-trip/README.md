# **Shopping Trip** 

The environment is a 20x20 grid with 10 items randomly scattered across.
The goal is to traverse the grid picking up items (or food if you prefer) along the way, and then returning to the starting position of (0, 0)
(0, 0) is the top left corner of the with a Domain of 0-19 and a Range of 0-19
The location of the 10 items are randomly generated each time a new instance is created. No two items can ever be in the same position.

## **Action Space** 

- 0: Move agent up one position

- 1: Move agent right one position

- 2: Move agent down one position

- 3: Move agent left one position

- 4: Pickup item

## **Observation Space**

The observation is going to return a dictionary of the agents location, and the locations of all the food scattered about.
Locations are given in the form of (x, y) coordinates
The name that will access the agent location is 

- "agent"

The names of the different food items are as follows

- "apples"
- "banana"
- "yogurt"
- "pizza"
- "noodles"
- "chicken"
- "soda"
- "candy"
- "chips"
- "cereal"

## **Rewards**

Each time the agent takes a step a -1 reward is given
If the agent attempts an illegal action (i.e. attempting to move up when agent is already at the top row) a -5 reward is given
If the agent picks an item up a reward of +5 is given
If the agent attemps to pickup an item, and does not share the same current location as an item a -10 reward is given
When all items are collected and the agent has succesfully returned to the starting position (0, 0) a +100 reward is given

