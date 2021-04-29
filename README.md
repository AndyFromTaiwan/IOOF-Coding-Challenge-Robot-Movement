# IOOF Coding Challenge: Robot Movement

IOOF-Coding-Challenge-Robot-Movement   
├── tests                # pytest test cases   
├── .gitignore           
├── README.md            
├── conftest.py          # for pytest   
├── robotController.py   # robot control interface, it accepts input commands and controls robot to execute    
├── robotModel.py        # robot internal state model, wrapped by the robot controller    
├── robot_movement.txt   # program spec   
└── sample.in            # pytest test cases   

## Usage
This program supports two modes

1) Input commands from a file:    
   $ python3 robotController.py -f sample.in
2) Input commands from standard input:    
   $ python3 robotController.py -i true
   Enter a return to exit the program
3) Help messages:    
   $ python3 robotController.py -h
   
## Testing
$ pytest tests   
Contains 6 test cases to cover all scenarios in the spec:    
1) test_0: robot basic function test   
2) test_1: robot executes all valid PLACE (including replace) and MOVE at all directions without falling   
3) test_2: robot MOVE, LEFT, RIGHT functions test   
4) test_3: robot can circle around 4 boundaries clockwise and counterclockwise without falling   
5) test_invalid_0: robot discards all invald commands (e.g. 'PLACE 0,-1,EAST' 'PLACE 4,4,E' 'PLACE ONE,1,WEST') before a valid PLACE command   
6) test_invalid_1: robot discards all invald commands (e.g. 'MOV' 'SLEEP' 'PLACE 5,0,NORTH') after a valid PLACE command   

## Design Overview
1) Contains model and controller, can be easily extended to the MVC architecture   
2) Use regular expression and exception handling to prevent invalid command execution    
3) CLI argument parsing    
