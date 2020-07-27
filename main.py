import glob
import os
import re
import yaml
import rgb_to_hex as rh

def main():
    with open('config/directory.yml') as yml:
        config = yaml.safe_load(yml)['directory']
    storyboard_directories = glob.glob(f"{config}**/*.storyboard", recursive=True)
    xib_dictionaries = glob.glob(f"{config}**/*.xib", recursive=True)

    for dic in storyboard_directories:
        search_color(dic)
    
    for xib in xib_dictionaries:
        search_color(xib)

def search_color(dic):
    with open('file.txt', 'a') as f:
        print('===============================', file=f)
        print(dic, file=f)
        xml = open(dic)
        for line in xml.readlines():
            if 'red=' in line:
                print(line.strip(), file=f)
                red_line = re.findall('red(.*)green', line)
                red = re.findall('"(.*)"', red_line[0])[0]
                green_line = re.findall('green(.*)blue', line)
                green = re.findall('"(.*)"', green_line[0])[0]
                blue_line = re.findall('blue(.*)alpha', line)
                blue = re.findall('"(.*)"', blue_line[0])[0]
                print(f'{rh.rgb_to_hex(float(red), float(green), float(blue))}\n', file=f)

main()