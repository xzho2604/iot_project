import numpy as np
import sys
import os

debug = 1

def main(input, output):

    group_list = []
    data_dict = {}
    cord_list = []
    tag_list = []
    count_dict = {}
    count_list = []

    with open(input, 'r') as f:
        for l in f.readlines():

            tag, _, rssi = l.strip('\n').split(' ')
            if tag != '-----End':
                tag_list.append(tag)
                if tag not in data_dict:
                    data_dict[tag] = [int(rssi)]
                else:
                    data_dict[tag].append(int(rssi))
            elif tag == '-----End':
                for i in set(tag_list):
                    count_dict[i] = tag_list.count(i)

                # print(count_dict)
                count_list.append(count_dict)
                # print(collections.Counter(tag_list))
                _, position = rssi.split('-----')
                x, y = position.split(',')
                cord_list.append((x, y))
                group_list.append(data_dict)
                data_dict = {}
                tag_list = []
                count_dict = {}


    for i in range(len(group_list)):
        for key, value in group_list[i].items():
            # print(value)
            group_list[i][key] = np.mean(value)

        # print(group_list[i])
        # print(cord_list[i])

    if os.path.exists(output):
        os.remove(output)

    with open(output, 'a') as f:
        f.write('%d,%d,%d,%d,%d,%s,%s,%s,%s,%s,%s,%s\n' % (1,2,3,4,5,'x','y','w1','w2','w3','w4','w5'))

        for i in range(len(group_list)):
            sum = 0
            for j in range(1, 6):
                if str(j) not in group_list[i]:
                    f.write('%.2f,' % 0)
                else:
                    f.write('%.2f,' % group_list[i][str(j)])
            f.write('%s,%s,' % (cord_list[i][0], cord_list[i][1]))
            for s in range(1, 6):

                if str(s) in count_list[i]:
                    sum += count_list[i][str(s)]

            for k in range(1, 5):
                if str(k) not in count_list[i]:
                    f.write('%.2f,' % (0.0))
                else:
                    f.write('%.2f,' % (count_list[i][str(k)]/sum))
            if str('5') not in count_list[i]:
                f.write('%.2f' % (0.0))
            else:
                f.write('%.2f' % (count_list[i]['5']/sum))
            f.write('\n')
    print('File convert done!')


if __name__ == "__main__":
    args = sys.argv


    if len(args) == 1:
        debug = 1
    else:
        debug = 0

    if not debug:
        args = sys.argv
        if len(args) != 3:
            print("Please input openfile_name and savefile_name\n")
            exit(0)
        else:
            main(args[1], args[2])
    else:
        main('../data02/record04.txt', 'update_clean_test.txt')



