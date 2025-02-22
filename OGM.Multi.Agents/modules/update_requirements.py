import subprocess
import re
import os
file_path = "/Users/manishkumarsaraf/Library/Mobile Documents/com~apple~CloudDocs/OGM/OGM.AGENTS/OGM.Multi.Agents/requirements.txt"
def read_requirements_file(file_path):
    """Reads requirements.txt and returns a dictionary of package:version."""
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return {}
    
    requirements = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            # Ignore empty lines and comments
            if not line or line.startswith('#'):
                continue
            # Try to match package and version specification
            match = re.match(r'([a-zA-Z0-9_-]+)([<>=~]+)(\d+\.\d+(?:\.\d+)*)', line)
            if match:
                package_name = match.group(1)
                version_spec = match.group(2)
                version = match.group(3)
                requirements[package_name] = {'version_spec': version_spec, 'required_version': version}
            else:
                # If no version is specified, assume latest
                package_name = line.split('==')[0]
                requirements[package_name] = {'version_spec': '', 'required_version': None}
    return requirements

def get_installed_package_versions():
    """Gets a dictionary of installed packages and their versions using pip."""
    try:
        process = subprocess.Popen(['pip', 'list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        stdout, stderr = process.communicate()
        if process.returncode!= 0:
            print("Failed to get pip list:", stderr)
            return {}
    except FileNotFoundError:
        print("The pip command is not found. Please check your pip installation.")
        return {}
    
    installed_packages = {}
    for line in stdout.splitlines()[2:]:
        line = line.strip()
        if line:
            package_name, version = line.split()
            installed_packages[package_name] = version
    return installed_packages

def compare_package_versions(requirements, installed_packages):
    """Compares the required package versions with the installed versions."""
    for package_name, req in requirements.items():
        installed_version = installed_packages.get(package_name, 'Not installed')
        if req['version_spec'] and req['required_version']:
            print(f"{package_name}: Installed={installed_version}, Required={req['version_spec']}{req['required_version']}")
        else:
            print(f"{package_name}: Installed={installed_version}, No specific version required")

def main():
    requirements_file_path = input("Enter the path to the requirements.txt file: ")
    requirements = read_requirements_file(requirements_file_path)
    if not requirements:
        return
    
    installed_packages = get_installed_package_versions()
    if not installed_packages:
        return
    
    compare_package_versions(requirements, installed_packages)

if __name__ == '__main__':
    main()
