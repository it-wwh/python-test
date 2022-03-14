#!/usr/bin/python3
# -*- coding: UTF-8 -*-


# brownie run --network bsc-test ./scripts/file_test.py
def main():
    to_address_list = []
    file = open('../resource/address.txt')
    lines = file.readlines()
    for line in lines:
        to_address_list.append(line.strip('\n'))
    print(to_address_list)

