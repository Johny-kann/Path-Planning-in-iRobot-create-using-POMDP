# Path Planning in iRobot create using POMDP

[Click here for the project link](http://my.fit.edu/~jsankaranara2015/AIproj3//)

The goal of the project is to make a robot plan its path from a source to the destination and reach the destination only by evidence and its previous transition.

The methodology involved
- creating a graph of nodes connected to each other based on the arena
- assigning an equal belief for all the states
- computing policies using value iteration based on MDP and POMDP
- Issuing actions to the robot to move (Up,Down,Left,Right)
- Getting evidence from the robot if it hits anywhere
- updating the belief based on the evidence and actions
- Repeat the last 4 actions till it reaches the destination

The utilities for the actions are computed based on the formula
![Capture](https://github.com/Johny-kann/Path-Planning-in-iRobot-create-using-POMDP/blob/master/formula.PNG)

A sample graph depicting the arena, where the blue color represents the states which are all blocked
![Capture](https://github.com/Johny-kann/Path-Planning-in-iRobot-create-using-POMDP/blob/master/graph.PNG)


Technical Features: Python, Multi-Threading, POMDP, MDP, PyCreate lib
