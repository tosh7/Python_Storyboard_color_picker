import glob
import os
import re
import yaml

def main():
    with open('config/directory.yml') as yml:
        config = yaml.safe_load(yml)['directory']
    storyboard_directories = glob.glob(f"{config}**/*.storyboard", recursive=True)
    dic1 = storyboard_directories[12]
    # search_color(dic1)

    # TODO: 一つで取得できたら、戻す 
    for dic in storyboard_directories:
        search_color(dic)

def search_color(dic):
    print('===============================')
    print(dic)
    xml = open(dic)
    for line in xml.readlines():
        if 'red' in line:
            print(line)

main()