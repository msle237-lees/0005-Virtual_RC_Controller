import os
import sys
import argparse

class DependencyHandler:
    def __init__(self, install: bool = False):
        self.install = install

        # Ensure the script is being run from the project root directory
        self.ensure_root_directory()

        # Get requirements.txt file location
        self.path = os.path.join(os.getcwd(), 'requirements.txt')

        # Check if requirements.txt exists
        if not os.path.exists(self.path):
            print('requirements.txt not found')
            sys.exit(1)

    def ensure_root_directory(self):
        """
        Ensure that the current working directory is the root directory of the project.
        The root directory is assumed to contain the 'requirements.txt' file.
        If the script is not in the root directory, it will attempt to change to the correct directory.
        """
        current_dir = os.getcwd()
        root_dir = self.find_project_root(current_dir)

        if root_dir:
            os.chdir(root_dir)
            print(f"Changed directory to project root: {root_dir}")
        else:
            print("Project root not found. This script must be run from within the project's directory.")
            sys.exit(1)

    def find_project_root(self, start_dir):
        """
        Recursively search for the project root directory by looking for 'requirements.txt'.
        """
        if os.path.exists(os.path.join(start_dir, 'requirements.txt')):
            return start_dir
        else:
            parent_dir = os.path.dirname(start_dir)
            if parent_dir == start_dir:  # Reached the root of the filesystem
                return None
            return self.find_project_root(parent_dir)

    def install_dependencies(self):
        """
        Install dependencies from the requirements.txt file within a virtual environment.
        """
        if self.install:
            os.system('python -m venv venv')
            os.system('source venv/bin/activate')
            os.system('pip install -r requirements.txt')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage Python project dependencies.")
    parser.add_argument('--install', action='store_true', help='Install dependencies from requirements.txt')
    args = parser.parse_args()

    handler = DependencyHandler(install=args.install)
    handler.install_dependencies()
