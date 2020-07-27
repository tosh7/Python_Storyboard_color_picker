import glob
import os
import re
import yaml

def main():
    with open('config/directory.yml') as yml:
        config = yaml.safe_load(yml)['directory']
    print(glob.glob(f"{config}**/*.storyboard", recursive=True))

main()