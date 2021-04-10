## Test task for YouTrack internship

In this test task was implemented AVLTree with next public methods:
- insert: you can put every number value here and tree will balance with your value.❗️You have to put numbers which are not in the tree otherwise an ValueError will be thrown;
- get_node_by_value: you can put number and function will return node with this value if it is exists;
- to_list: you can call it without parameters and function will return list of values of nodes from tree. Order of parameters in list the same as for BFS; 
- print_tree: you can call it without parameters and function will print tree in readable view. Function returns `None`. 

### Simple example of readable tree view
```
        Insert: 5
    ┌8
  ┌7┤
  | └6┐
  |   └5
 4┤
  | ┌3
  └2┤
    └1
AVLNode: self.value=5, self.height=1
4 2 7 1 3 6 8 5
```

### Environment

For checking task you should setup the environment:
- Python version 3.8;
- Libraries: `pptree==3.1`, `pytest==6.2.3`, you can install it in this way `pip install -r requirements.txt`.

For tests checking you can just go to project directory and run in command line this `pytest tests`

[Internship description](https://internship.jetbrains.com/projects/914/)