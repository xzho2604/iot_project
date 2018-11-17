import numpy as np
import sys
import os

debug = 1

def data_clean(input, output='123.txt', write_file=True):

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


        # print(cord_list[i])
    output_lists = []

    if os.path.exists(output):
        os.remove(output)

    with open(output, 'a') as f:
        if write_file:
            f.write('%d,%d,%d,%d,%d,%s,%s,%s,%s,%s,%s,%s\n' % (1,2,3,4,5,'x','y','w1','w2','w3','w4','w5'))

        for i in range(len(group_list)):
            output_list = []
            sum = 0
            for j in range(1, 6):
                if str(j) not in group_list[i]:
                    if write_file:
                        f.write('%.2f,' % 0)
                    output_list.append(0.0)
                else:
                    if write_file:
                        f.write('%.2f,' % group_list[i][str(j)])
                    output_list.append(group_list[i][str(j)])
            if write_file:
                f.write('%s,%s,' % (cord_list[i][0], cord_list[i][1]))
            output_list.append(float(cord_list[i][0]))
            output_list.append(float(cord_list[i][1]))
            for s in range(1, 6):

                if str(s) in count_list[i]:
                    sum += count_list[i][str(s)]

            for k in range(1, 5):
                if str(k) not in count_list[i]:
                    if write_file:
                        f.write('%.2f,' % (0.0))
                    output_list.append(0.0)
                else:
                    if write_file:
                        f.write('%.2f,' % (count_list[i][str(k)]/sum))
                    output_list.append(count_list[i][str(k)]/sum)
            if str('5') not in count_list[i]:
                if write_file:
                    f.write('%.2f' % (0.0))
                output_list.append(0.0)
            else:
                if write_file:
                    f.write('%.2f' % (count_list[i]['5']/sum))
                output_list.append(count_list[i]['5']/sum)

            if write_file:
                f.write('\n')

        output_lists.append(output_list)
    print('File convert done!')

    if not write_file:
        os.remove(output)

    return output_lists


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
            _ = data_clean(args[1], args[2])
    else:
        output_lists =  data_clean('../data02/record04.txt',write_file=False)
        # print(output_lists)



