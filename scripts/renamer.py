#!/usr/local/bin/python3

import os

def main():
    i = 0
#   Insert the path to the source folder here.
    path = "~/source/folder/for/the/files/"
    for filename in os.listdir(path):
        destination = "image" + str(i) + ".jpg"
        source = path + filename
        destination = path + destination
        os.rename(source, destination)
        i += 1

if __name__ == '__main__':
    main()