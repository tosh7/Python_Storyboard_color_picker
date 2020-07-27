import glob
import os
import re
import yaml

def main():
    print("hello world")
    with open('config/directory.yml', 'r') as yml:
        config = yaml.load(yml)['directory']
    print(glob.glob(f"{config}*/*.storyboard"))

main()