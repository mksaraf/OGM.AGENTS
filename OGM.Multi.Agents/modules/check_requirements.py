import subprocess
import sys

def get_installed_packages():
    result = subprocess.run(['pip3', 'freeze'], capture_output=True, text=True)
    return set(result.stdout.splitlines())

def install_packages(requirements_file):
    with open(requirements_file) as f:
        packages = f.read().splitlines()

    pre_installed_packages = get_installed_packages()
    installed_packages = []
    failed_packages = []

    for package in packages:
        try:
            subprocess.check_call(['pip3', 'install', package])
            installed_packages.append(package)
        except subprocess.CalledProcessError:
            failed_packages.append(package)

    post_installed_packages = get_installed_packages()
    newly_installed_packages = post_installed_packages - pre_installed_packages

    return newly_installed_packages, failed_packages

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 check_requirements.py <path_to_requirements.txt>")
        sys.exit(1)

    requirements_file = sys.argv[1]
    newly_installed, failed = install_packages(requirements_file)

    print("\nSummary of installations:")
    print("Newly installed packages:")
    for package in newly_installed:
        print(f"  - {package}")

    print("Failed packages:")
    for package in failed:
        print(f"  - {package}")
