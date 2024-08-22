import argparse
import sys
import os
import time


parser = argparse.ArgumentParser(description='Start the program')
parser.add_argument('-ip', '--ip', type=str, help='IP address of the server')
parser.add_argument('-p', '--port', type=int, help='Port number of the server')
parser.add_argument('-v', '--virtual', action='store_true', help='Use the Virtual Controller')
parser.add_argument('-d', '--debug', action='store_true', help='Enable debug mode')

args = parser.parse_args()

if args.ip is None:
    print('IP address is required')
    sys.exit(1)
elif args.port is None:
    print('Port number is required')
    sys.exit(1)
    
if args.virtual:
    os.system(f'python3 virtual_controller.py {"--d" if args.debug else ""} -ip {args.ip} -p {args.port}')
    time.sleep(1)
else:
    os.system(f'python3 controller.py {"--d" if args.debug else ""} -ip {args.ip} -p {args.port}')
    time.sleep(1)
    