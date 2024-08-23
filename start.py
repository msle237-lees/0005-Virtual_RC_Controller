import subprocess
import argparse
import sys
import os

from modules.DependencyHandler import DependencyHandler

parser = argparse.ArgumentParser(description='Start the application')
parser.add_argument('--ip', type=str, default='localhost', help='IP address to bind to')
parser.add_argument('--port', type=int, default=8080, help='Port to bind to')
parser.add_argument('--debug', action='store_true', help='Enable debug mode')
args = parser.parse_args()

# Using the DependencyHandler class to install dependencies
dependency_handler = DependencyHandler(install=True)
dependency_handler.install_dependencies()

# Start the application
if args.debug:
    subprocess.run(['python', 'src/app.py', '--ip', args.ip, '--port', str(args.port), '--debug'])
else:
    subprocess.run(['python', 'src/app.py', '--ip', args.ip, '--port', str(args.port)])

# Handle subprocess exit code
if subprocess.CompletedProcess.returncode != 0:
    sys.exit(1)
