from argparse import ArgumentParser, ArgumentTypeError
import re
from robotModel import RobotModel

class Robot(object):
    def __init__(self):
        self.robotModel = RobotModel()
        self.handlers = dict()
        self.handlers['PLACE'] = self.robotModel.place
        self.handlers['MOVE'] = self.robotModel.move
        self.handlers['LEFT'] = self.robotModel.turnLeft
        self.handlers['RIGHT'] = self.robotModel.turnRight
        self.handlers['REPORT'] = self.report

    def execute(self, command):
        try:
            if re.match(r'PLACE\s\d,\d,\w+', command):
                args = command.split()[1].split(',')
                handler = self.handlers.get('PLACE')
                handler(int(args[0]), int(args[1]), args[2])
            elif command != 'PLACE':
                handler = self.handlers.get(command)
                if handler is not None:
                    return handler()
        except Exception as e:
            print(e)
        
    def report(self):
        message = ''
        status = self.robotModel.report()
        if status is not None:
            message = f'{status[0]},{status[1]},{status[2]}'
            print(message)
        return message


def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in {'yes', 'true', 't', 'y', '1'}:
        return True
    elif v.lower() in {'no', 'false', 'f', 'n', '0'}:
        return False
    else:
        raise ArgumentTypeError('Boolean value expected.')

if __name__ == '__main__':
    robot = Robot()
    parser = ArgumentParser()
    parser.add_argument('-f', '--file', type=str, help='The robot will execute commands from a input file')
    parser.add_argument('-i', '--input', default=False, type=str2bool, help='The robot will execute commands from user inputs')
    args = parser.parse_args()
    if args.input:
        while(True):
            command = input("Place enter the next command: ")
            if len(command)>0:
                robot.execute(command)
            else:
                break
    elif args.file is not None:
        commands = open(args.file).read().splitlines()
        for command in commands:
            if(len(command)>0):
                robot.execute(command)
