import numpy as np
import sys
import os


def main(input, output):

    group_list = []
    data_dict = {}
    cord_list = []
    count = 0

    with open(input, 'r') as f:
        for l in f.readlines():
            tag, _, rssi = l.strip('\n').split(' ')
            if tag != '-----End':
                if tag not in data_dict:
                    data_dict[tag] = [int(rssi)]
                else:
                    data_dict[tag].append(int(rssi))
            else:
                count += 1
                if count == 2:
                    _, position = rssi.split('-----')
                    x, y = position.split(',')
                    cord_list.append((x, y))
                    group_list.append(data_dict)
                    data_dict = {}
                    count = 0



    for i in range(len(group_list)):
        for key, value in group_list[i].items():
            group_list[i][key] = np.mean(value)

        # print(group_list[i])
        # print(cord_list[i])

    if os.path.exists(output):
        os.remove(output)

    with open(output, 'a') as f:
        f.write('%d,%d,%d,%d,%d,%s,%s\n' % (1,2,3,4,5,'x','y'))

        for i in range(len(group_list)):
            for j in range(1, 6):
                if str(j) not in group_list[i]:
                    f.write('%.2f,' % 0)
                else:
                    f.write('%.2f,' % group_list[i][str(j)])
            f.write('%s,%s\n' % (cord_list[i][0], cord_list[i][1]))


    print('File convert done!')


if __name__ == "__main__":

    args = sys.argv
    if len(args) != 3:
        print("Please input openfile_name and savefile_name\n")
        exit(0)
    else:
        main(args[1], args[2])


