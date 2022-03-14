if __name__ == '__main__':
    to_address_list = []
    file = open('../resource/address.txt')
    lines = file.readlines()
    for line in lines:
        to_address_list.append(line.strip('\n'))
    print(to_address_list)
