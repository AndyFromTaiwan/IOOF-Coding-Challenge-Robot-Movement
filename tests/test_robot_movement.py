from robotController import Robot

def test_0():
    robot = Robot()
    commands = open('tests/test.0.in').read().splitlines()
    expected_outputs = open('tests/test.0.out').read().splitlines()
    index = 0
    for command in commands:
        if(len(command)>0):
            res = robot.execute(command)
            if(command=='REPORT'):
                assert res == expected_outputs[index]
                index += 1

def test_1():
    robot = Robot()
    commands = open('tests/test.1.in').read().splitlines()
    expected_outputs = open('tests/test.1.out').read().splitlines()
    index = 0
    for command in commands:
        if(len(command)>0):
            res = robot.execute(command)
            if(command=='REPORT'):
                assert res == expected_outputs[index]
                index += 1

def test_2():
    robot = Robot()
    commands = open('tests/test.2.in').read().splitlines()
    expected_outputs = open('tests/test.2.out').read().splitlines()
    index = 0
    for command in commands:
        if(len(command)>0):
            res = robot.execute(command)
            if(command=='REPORT'):
                assert res == expected_outputs[index]
                index += 1
def test_3():
    robot = Robot()
    commands = open('tests/test.3.in').read().splitlines()
    expected_outputs = open('tests/test.3.out').read().splitlines()
    index = 0
    for command in commands:
        if(len(command)>0):
            res = robot.execute(command)
            if(command=='REPORT'):
                assert res == expected_outputs[index]
                index += 1

def test_invalid_0():
    robot = Robot()
    commands = open('tests/test.invalid.0.in').read().splitlines()
    for command in commands:
        if(len(command)>0):
            res = robot.execute(command)
            if(command=='REPORT'):
                assert res == ''

def test_invalid_1():
    robot = Robot()
    robot.execute('PLACE 0,0,NORTH')
    commands = open('tests/test.invalid.1.in').read().splitlines()
    for command in commands:
        if(len(command)>0):
            res = robot.execute(command)
            if(command=='REPORT'):
                assert res == '0,0,NORTH'
