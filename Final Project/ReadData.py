import random
from scipy.spatial import distance
import Image
import numpy as np
import Perceptron
import math
import sys
from random import sample
import time


def read_data(file_name, type):
    if type == "digit":
        image_size = 28
    else:
        image_size = 70

    num_images = 0
    numbers = []
    with open(file_name) as fp:
        line = fp.readline()
        count_rows = 0
        image = []
        while line:
            row = []
            for c in line:
                if c == ' ':
                    row.append('0')
                else:
                    row.append('1')
            row.pop(len(row) - 1)
            image.append(row)

            count_rows += 1
            if count_rows == image_size:
                count_rows = 0
                numbers.append(image)
                num_images += 1
                # print num_images
                image = []
            line = fp.readline()
    return numbers


def read_labels(file_name):
    labels = []
    num_labels = 0
    with open(file_name) as fp:
        line = fp.readline()
        # print(line)
        while line:
            line = line[:-1]
            labels.append(line)
            line = fp.readline()
            num_labels += 1
            # print num_labels
    return labels


def extract_features(data, data_labels):
    image_info = []
    index = 0
    count = 0
    for image in data:
        features = [0] * 100
        for row in range(len(image)):
            r = (len(image) / 10)
            r1 = r
            r2 = 2 * r
            r3 = 3 * r
            r4 = 4 * r
            r5 = 5 * r
            r6 = 6 * r
            r7 = 7 * r
            r8 = 8 * r
            r9 = 9 * r
            r10 = 10 * r

            for col in range(len(image[row])):
                c = (len(image[row]) / 10)
                c1 = c
                c2 = 2 * c
                c3 = 3 * c
                c4 = 4 * c
                c5 = 5 * c
                c6 = 6 * c
                c7 = 7 * c
                c8 = 8 * c
                c9 = 9 * c
                c10 = 10 * c

                if image[row][col] == '1':  # if black pixel
                    if row <= r1 and col <= c1:
                        features[0] += 1
                    elif row <= r1 and col > c1 and col <= c2:
                        features[1] += 1
                    elif row <= r1 and col > c2 and col <= c3:
                        features[2] += 1
                    elif row <= r1 and col > c3 and col <= c4:
                        features[3] += 1
                    elif row <= r1 and col > c4 and col <= c5:
                        features[4] += 1
                    elif row <= r1 and col > c5 and col <= c6:
                        features[5] += 1
                    elif row <= r1 and col > c6 and col <= c7:
                        features[6] += 1
                    elif row <= r1 and col > c7 and col <= c8:
                        features[7] += 1
                    elif row <= r1 and col > c8 and col <= c9:
                        features[8] += 1
                    elif row <= r1 and col > c9 and col <= c10:
                        features[9] += 1

                    elif row > r1 and row <= r2 and col <= c1:
                        features[10] += 1
                    elif row > r1 and row <= r2 and col > c1 and col <= c2:
                        features[11] += 1
                    elif row > r1 and row <= r2 and col > c2 and col <= c3:
                        features[12] += 1
                    elif row > r1 and row <= r2 and col > c3 and col <= c4:
                        features[13] += 1
                    elif row > r1 and row <= r2 and col > c4 and col <= c5:
                        features[14] += 1
                    elif row > r1 and row <= r2 and col > c5 and col <= c6:
                        features[15] += 1
                    elif row > r1 and row <= r2 and col > c6 and col <= c7:
                        features[16] += 1
                    elif row > r1 and row <= r2 and col > c7 and col <= c8:
                        features[17] += 1
                    elif row > r1 and row <= r2 and col > c8 and col <= c9:
                        features[18] += 1
                    elif row > r1 and row <= r2 and col > c9 and col <= c10:
                        features[19] += 1

                    elif row > r2 and row <= r3 and col <= c1:
                        features[20] += 1
                    elif row > r2 and row <= r3 and col > c1 and col <= c2:
                        features[21] += 1
                    elif row > r2 and row <= r3 and col > c2 and col <= c3:
                        features[22] += 1
                    elif row > r2 and row <= r3 and col > c3 and col <= c4:
                        features[23] += 1
                    elif row > r2 and row <= r3 and col > c4 and col <= c5:
                        features[24] += 1
                    elif row > r2 and row <= r3 and col > c5 and col <= c6:
                        features[25] += 1
                    elif row > r2 and row <= r3 and col > c6 and col <= c7:
                        features[26] += 1
                    elif row > r2 and row <= r3 and col > c7 and col <= c8:
                        features[27] += 1
                    elif row > r2 and row <= r3 and col > c8 and col <= c9:
                        features[28] += 1
                    elif row > r2 and row <= r3 and col > c9 and col <= c10:
                        features[29] += 1

                    elif row > r3 and row <= r4 and col <= c1:
                        features[30] += 1
                    elif row > r3 and row <= r4 and col > c1 and col <= c2:
                        features[31] += 1
                    elif row > r3 and row <= r4 and col > c2 and col <= c3:
                        features[32] += 1
                    elif row > r3 and row <= r4 and col > c3 and col <= c4:
                        features[33] += 1
                    elif row > r3 and row <= r4 and col > c4 and col <= c5:
                        features[34] += 1
                    elif row > r3 and row <= r4 and col > c5 and col <= c6:
                        features[35] += 1
                    elif row > r3 and row <= r4 and col > c6 and col <= c7:
                        features[36] += 1
                    elif row > r3 and row <= r4 and col > c7 and col <= c8:
                        features[37] += 1
                    elif row > r3 and row <= r4 and col > c8 and col <= c9:
                        features[38] += 1
                    elif row > r3 and row <= r4 and col > c9 and col <= c10:
                        features[39] += 1

                    elif row > r4 and row <= r5 and col <= c1:
                        features[40] += 1
                    elif row > r4 and row <= r5 and col > c1 and col <= c2:
                        features[41] += 1
                    elif row > r4 and row <= r5 and col > c2 and col <= c3:
                        features[42] += 1
                    elif row > r4 and row <= r5 and col > c3 and col <= c4:
                        features[43] += 1
                    elif row > r4 and row <= r5 and col > c4 and col <= c5:
                        features[44] += 1
                    elif row > r4 and row <= r5 and col > c5 and col <= c6:
                        features[45] += 1
                    elif row > r4 and row <= r5 and col > c6 and col <= c7:
                        features[46] += 1
                    elif row > r4 and row <= r5 and col > c7 and col <= c8:
                        features[47] += 1
                    elif row > r4 and row <= r5 and col > c8 and col <= c9:
                        features[48] += 1
                    elif row > r4 and row <= r5 and col > c9 and col <= c10:
                        features[49] += 1

                    elif row > r5 and row <= r6 and col <= c1:
                        features[50] += 1
                    elif row > r5 and row <= r6 and col > c1 and col <= c2:
                        features[51] += 1
                    elif row > r5 and row <= r6 and col > c2 and col <= c3:
                        features[52] += 1
                    elif row > r5 and row <= r6 and col > c3 and col <= c4:
                        features[53] += 1
                    elif row > r5 and row <= r6 and col > c4 and col <= c5:
                        features[54] += 1
                    elif row > r5 and row <= r6 and col > c5 and col <= c6:
                        features[55] += 1
                    elif row > r5 and row <= r6 and col > c6 and col <= c7:
                        features[56] += 1
                    elif row > r5 and row <= r6 and col > c7 and col <= c8:
                        features[57] += 1
                    elif row > r5 and row <= r6 and col > c8 and col <= c9:
                        features[58] += 1
                    elif row > r5 and row <= r6 and col > c9 and col <= c10:
                        features[59] += 1

                    elif row > r6 and row <= r7 and col <= c1:
                        features[60] += 1
                    elif row > r6 and row <= r7 and col > c1 and col <= c2:
                        features[61] += 1
                    elif row > r6 and row <= r7 and col > c2 and col <= c3:
                        features[62] += 1
                    elif row > r6 and row <= r7 and col > c3 and col <= c4:
                        features[63] += 1
                    elif row > r6 and row <= r7 and col > c4 and col <= c5:
                        features[64] += 1
                    elif row > r6 and row <= r7 and col > c5 and col <= c6:
                        features[65] += 1
                    elif row > r6 and row <= r7 and col > c6 and col <= c7:
                        features[66] += 1
                    elif row > r6 and row <= r7 and col > c7 and col <= c8:
                        features[67] += 1
                    elif row > r6 and row <= r7 and col > c8 and col <= c9:
                        features[68] += 1
                    elif row > r6 and row <= r7 and col > c9 and col <= c10:
                        features[69] += 1

                    elif row > r7 and row <= r8 and col <= c1:
                        features[70] += 1
                    elif row > r7 and row <= r8 and col > c1 and col <= c2:
                        features[71] += 1
                    elif row > r7 and row <= r8 and col > c2 and col <= c3:
                        features[72] += 1
                    elif row > r7 and row <= r8 and col > c3 and col <= c4:
                        features[73] += 1
                    elif row > r7 and row <= r8 and col > c4 and col <= c5:
                        features[74] += 1
                    elif row > r7 and row <= r8 and col > c5 and col <= c6:
                        features[75] += 1
                    elif row > r7 and row <= r8 and col > c6 and col <= c7:
                        features[76] += 1
                    elif row > r7 and row <= r8 and col > c7 and col <= c8:
                        features[77] += 1
                    elif row > r7 and row <= r8 and col > c8 and col <= c9:
                        features[78] += 1
                    elif row > r7 and row <= r8 and col > c9 and col <= c10:
                        features[79] += 1

                    elif row > r8 and row <= r9 and col <= c1:
                        features[80] += 1
                    elif row > r8 and row <= r9 and col > c1 and col <= c2:
                        features[81] += 1
                    elif row > r8 and row <= r9 and col > c2 and col <= c3:
                        features[82] += 1
                    elif row > r8 and row <= r9 and col > c3 and col <= c4:
                        features[83] += 1
                    elif row > r8 and row <= r9 and col > c4 and col <= c5:
                        features[84] += 1
                    elif row > r8 and row <= r9 and col > c5 and col <= c6:
                        features[85] += 1
                    elif row > r8 and row <= r9 and col > c6 and col <= c7:
                        features[86] += 1
                    elif row > r8 and row <= r9 and col > c7 and col <= c8:
                        features[87] += 1
                    elif row > r8 and row <= r9 and col > c8 and col <= c9:
                        features[88] += 1
                    elif row > r8 and row <= r9 and col > c9 and col <= c10:
                        features[89] += 1

                    elif row > r9 and row <= r10 and col <= c1:
                        features[90] += 1
                    elif row > r9 and row <= r10 and col > c1 and col <= c2:
                        features[91] += 1
                    elif row > r9 and row <= r10 and col > c2 and col <= c3:
                        features[92] += 1
                    elif row > r9 and row <= r10 and col > c3 and col <= c4:
                        features[93] += 1
                    elif row > r9 and row <= r10 and col > c4 and col <= c5:
                        features[94] += 1
                    elif row > r9 and row <= r10 and col > c5 and col <= c6:
                        features[95] += 1
                    elif row > r9 and row <= r10 and col > c6 and col <= c7:
                        features[96] += 1
                    elif row > r9 and row <= r10 and col > c7 and col <= c8:
                        features[97] += 1
                    elif row > r9 and row <= r10 and col > c8 and col <= c9:
                        features[98] += 1
                    elif row > r9 and row <= r10 and col > c9 and col <= c10:
                        features[99] += 1

                    else:
                        continue

        image_info.append(Image.Image(data_labels[index], features))
        index = index + 1
    return image_info


def extract_features_matrix(data, data_labels):
    image_info = []
    index = 0
    count = 0
    for image in data:
        features = np.empty([10, 10])
        features.fill(0)
        for row in range(len(image)):
            r = (len(image) / 10)
            r1 = r
            r2 = 2 * r
            r3 = 3 * r
            r4 = 4 * r
            r5 = 5 * r
            r6 = 6 * r
            r7 = 7 * r
            r8 = 8 * r
            r9 = 9 * r
            r10 = 10 * r

            for col in range(len(image[row])):
                c = (len(image[row]) / 10)
                c1 = c
                c2 = 2 * c
                c3 = 3 * c
                c4 = 4 * c
                c5 = 5 * c
                c6 = 6 * c
                c7 = 7 * c
                c8 = 8 * c
                c9 = 9 * c
                c10 = 10 * c

                if image[row][col] == '1':  # if black pixel
                    if row <= r1 and col <= c1:
                        features[0][0] += 1
                    elif row <= r1 and col > c1 and col <= c2:
                        features[0][1] += 1
                    elif row <= r1 and col > c2 and col <= c3:
                        features[0][2] += 1
                    elif row <= r1 and col > c3 and col <= c4:
                        features[0][3] += 1
                    elif row <= r1 and col > c4 and col <= c5:
                        features[0][4] += 1
                    elif row <= r1 and col > c5 and col <= c6:
                        features[0][5] += 1
                    elif row <= r1 and col > c6 and col <= c7:
                        features[0][6] += 1
                    elif row <= r1 and col > c7 and col <= c8:
                        features[0][7] += 1
                    elif row <= r1 and col > c8 and col <= c9:
                        features[0][8] += 1
                    elif row <= r1 and col > c9 and col <= c10:
                        features[0][9] += 1

                    elif row > r1 and row <= r2 and col <= c1:
                        features[1][0] += 1
                    elif row > r1 and row <= r2 and col > c1 and col <= c2:
                        features[1][1] += 1
                    elif row > r1 and row <= r2 and col > c2 and col <= c3:
                        features[1][2] += 1
                    elif row > r1 and row <= r2 and col > c3 and col <= c4:
                        features[1][3] += 1
                    elif row > r1 and row <= r2 and col > c4 and col <= c5:
                        features[1][4] += 1
                    elif row > r1 and row <= r2 and col > c5 and col <= c6:
                        features[1][5] += 1
                    elif row > r1 and row <= r2 and col > c6 and col <= c7:
                        features[1][6] += 1
                    elif row > r1 and row <= r2 and col > c7 and col <= c8:
                        features[1][7] += 1
                    elif row > r1 and row <= r2 and col > c8 and col <= c9:
                        features[1][8] += 1
                    elif row > r1 and row <= r2 and col > c9 and col <= c10:
                        features[1][9] += 1

                    elif row > r2 and row <= r3 and col <= c1:
                        features[2][0] += 1
                    elif row > r2 and row <= r3 and col > c1 and col <= c2:
                        features[2][1] += 1
                    elif row > r2 and row <= r3 and col > c2 and col <= c3:
                        features[2][2] += 1
                    elif row > r2 and row <= r3 and col > c3 and col <= c4:
                        features[2][3] += 1
                    elif row > r2 and row <= r3 and col > c4 and col <= c5:
                        features[2][4] += 1
                    elif row > r2 and row <= r3 and col > c5 and col <= c6:
                        features[2][5] += 1
                    elif row > r2 and row <= r3 and col > c6 and col <= c7:
                        features[2][6] += 1
                    elif row > r2 and row <= r3 and col > c7 and col <= c8:
                        features[2][7] += 1
                    elif row > r2 and row <= r3 and col > c8 and col <= c9:
                        features[2][8] += 1
                    elif row > r2 and row <= r3 and col > c9 and col <= c10:
                        features[2][9] += 1

                    elif row > r3 and row <= r4 and col <= c1:
                        features[3][0] += 1
                    elif row > r3 and row <= r4 and col > c1 and col <= c2:
                        features[3][1] += 1
                    elif row > r3 and row <= r4 and col > c2 and col <= c3:
                        features[3][2] += 1
                    elif row > r3 and row <= r4 and col > c3 and col <= c4:
                        features[3][3] += 1
                    elif row > r3 and row <= r4 and col > c4 and col <= c5:
                        features[3][4] += 1
                    elif row > r3 and row <= r4 and col > c5 and col <= c6:
                        features[3][5] += 1
                    elif row > r3 and row <= r4 and col > c6 and col <= c7:
                        features[3][6] += 1
                    elif row > r3 and row <= r4 and col > c7 and col <= c8:
                        features[3][7] += 1
                    elif row > r3 and row <= r4 and col > c8 and col <= c9:
                        features[3][8] += 1
                    elif row > r3 and row <= r4 and col > c9 and col <= c10:
                        features[3][9] += 1

                    elif row > r4 and row <= r5 and col <= c1:
                        features[4][0] += 1
                    elif row > r4 and row <= r5 and col > c1 and col <= c2:
                        features[4][1] += 1
                    elif row > r4 and row <= r5 and col > c2 and col <= c3:
                        features[4][2] += 1
                    elif row > r4 and row <= r5 and col > c3 and col <= c4:
                        features[4][3] += 1
                    elif row > r4 and row <= r5 and col > c4 and col <= c5:
                        features[4][4] += 1
                    elif row > r4 and row <= r5 and col > c5 and col <= c6:
                        features[4][5] += 1
                    elif row > r4 and row <= r5 and col > c6 and col <= c7:
                        features[4][6] += 1
                    elif row > r4 and row <= r5 and col > c7 and col <= c8:
                        features[4][7] += 1
                    elif row > r4 and row <= r5 and col > c8 and col <= c9:
                        features[4][8] += 1
                    elif row > r4 and row <= r5 and col > c9 and col <= c10:
                        features[4][9] += 1

                    elif row > r5 and row <= r6 and col <= c1:
                        features[5][0] += 1
                    elif row > r5 and row <= r6 and col > c1 and col <= c2:
                        features[5][1] += 1
                    elif row > r5 and row <= r6 and col > c2 and col <= c3:
                        features[5][2] += 1
                    elif row > r5 and row <= r6 and col > c3 and col <= c4:
                        features[5][3] += 1
                    elif row > r5 and row <= r6 and col > c4 and col <= c5:
                        features[5][4] += 1
                    elif row > r5 and row <= r6 and col > c5 and col <= c6:
                        features[5][5] += 1
                    elif row > r5 and row <= r6 and col > c6 and col <= c7:
                        features[5][6] += 1
                    elif row > r5 and row <= r6 and col > c7 and col <= c8:
                        features[5][7] += 1
                    elif row > r5 and row <= r6 and col > c8 and col <= c9:
                        features[5][8] += 1
                    elif row > r5 and row <= r6 and col > c9 and col <= c10:
                        features[5][9] += 1

                    elif row > r6 and row <= r7 and col <= c1:
                        features[6][0] += 1
                    elif row > r6 and row <= r7 and col > c1 and col <= c2:
                        features[6][1] += 1
                    elif row > r6 and row <= r7 and col > c2 and col <= c3:
                        features[6][2] += 1
                    elif row > r6 and row <= r7 and col > c3 and col <= c4:
                        features[6][3] += 1
                    elif row > r6 and row <= r7 and col > c4 and col <= c5:
                        features[6][4] += 1
                    elif row > r6 and row <= r7 and col > c5 and col <= c6:
                        features[6][5] += 1
                    elif row > r6 and row <= r7 and col > c6 and col <= c7:
                        features[6][6] += 1
                    elif row > r6 and row <= r7 and col > c7 and col <= c8:
                        features[6][7] += 1
                    elif row > r6 and row <= r7 and col > c8 and col <= c9:
                        features[6][8] += 1
                    elif row > r6 and row <= r7 and col > c9 and col <= c10:
                        features[6][9] += 1

                    elif row > r7 and row <= r8 and col <= c1:
                        features[7][0] += 1
                    elif row > r7 and row <= r8 and col > c1 and col <= c2:
                        features[7][1] += 1
                    elif row > r7 and row <= r8 and col > c2 and col <= c3:
                        features[7][2] += 1
                    elif row > r7 and row <= r8 and col > c3 and col <= c4:
                        features[7][3] += 1
                    elif row > r7 and row <= r8 and col > c4 and col <= c5:
                        features[7][4] += 1
                    elif row > r7 and row <= r8 and col > c5 and col <= c6:
                        features[7][5] += 1
                    elif row > r7 and row <= r8 and col > c6 and col <= c7:
                        features[7][6] += 1
                    elif row > r7 and row <= r8 and col > c7 and col <= c8:
                        features[7][7] += 1
                    elif row > r7 and row <= r8 and col > c8 and col <= c9:
                        features[7][8] += 1
                    elif row > r7 and row <= r8 and col > c9 and col <= c10:
                        features[7][9] += 1

                    elif row > r8 and row <= r9 and col <= c1:
                        features[8][0] += 1
                    elif row > r8 and row <= r9 and col > c1 and col <= c2:
                        features[8][1] += 1
                    elif row > r8 and row <= r9 and col > c2 and col <= c3:
                        features[8][2] += 1
                    elif row > r8 and row <= r9 and col > c3 and col <= c4:
                        features[8][3] += 1
                    elif row > r8 and row <= r9 and col > c4 and col <= c5:
                        features[8][4] += 1
                    elif row > r8 and row <= r9 and col > c5 and col <= c6:
                        features[8][5] += 1
                    elif row > r8 and row <= r9 and col > c6 and col <= c7:
                        features[8][6] += 1
                    elif row > r8 and row <= r9 and col > c7 and col <= c8:
                        features[8][7] += 1
                    elif row > r8 and row <= r9 and col > c8 and col <= c9:
                        features[8][8] += 1
                    elif row > r8 and row <= r9 and col > c9 and col <= c10:
                        features[8][9] += 1

                    elif row > r9 and row <= r10 and col <= c1:
                        features[9][0] += 1
                    elif row > r9 and row <= r10 and col > c1 and col <= c2:
                        features[9][1] += 1
                    elif row > r9 and row <= r10 and col > c2 and col <= c3:
                        features[9][2] += 1
                    elif row > r9 and row <= r10 and col > c3 and col <= c4:
                        features[9][3] += 1
                    elif row > r9 and row <= r10 and col > c4 and col <= c5:
                        features[9][4] += 1
                    elif row > r9 and row <= r10 and col > c5 and col <= c6:
                        features[9][5] += 1
                    elif row > r9 and row <= r10 and col > c6 and col <= c7:
                        features[9][6] += 1
                    elif row > r9 and row <= r10 and col > c7 and col <= c8:
                        features[9][7] += 1
                    elif row > r9 and row <= r10 and col > c8 and col <= c9:
                        features[9][8] += 1
                    elif row > r9 and row <= r10 and col > c9 and col <= c10:
                        features[9][9] += 1
                    else:
                        continue

        image_info.append(Image.Image(data_labels[index], features))
        index = index + 1
    return image_info


def get_accuracy(guess, test_labels_list):
    count = 0
    for i in range(len(guess)):
        if guess[i] == test_labels_list[i]:
            count += 1
    print(str(count) + "/" + str(len(guess)))
    return float(count) / len(guess)


def write_to_file(file_name, contents):
    f = open(file_name, "a")
    f.write(str(contents) + "\n")
    f.close()


# Main - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# -f = faces
# -d = digits

# -p = perceptron

# sample call for digits, running bayes and percent data 50%: ReadData.py -d -b 5
start_time = time.time()

if len(sys.argv) != 4:
    print( "Incorrect number of arguments")
    print("Example: % ReadData.py -b -d 5")
    exit()

num_digits = 5000
num_faces = 451
amount_testing_data_digits = []  # stores the number of data points that should be read
amount_testing_data_faces = []  # stores the number of data points that should be read

amount_testing_data_digits.append(0)  # index 0 not used
amount_testing_data_faces.append(0)  # same as above
count = .1
for i in range(10):
    amount_testing_data_digits.append(int(math.ceil(num_digits * count)))
    amount_testing_data_faces.append(int(math.ceil(num_faces * count)))
    count += .1

percentage = int(sys.argv[3])  # 1 = 10% of data, 2 = 20%, 3 = 30% etc
print (str(percentage) + "0% of data")
guess = []
algo = ""
if sys.argv[1] == "-d":  # digits
    print ("digits")
    train_digit_image = "classification/data/digitdata/trainingimages"
    train_digit_label = "classification/data/digitdata/traininglabels"
    train_digit_image_list = read_data(train_digit_image, "digit")
    train_digit_labels_list = read_labels(train_digit_label)

    test_digit_image = "classification/data/digitdata/testimages"
    test_digit_label = "classification/data/digitdata/testlabels"
    test_digit_image_list = read_data(test_digit_image, "digit")
    test_digit_labels_list = read_labels(test_digit_label)
    # training
    training_digit_info_list = extract_features(train_digit_image_list, train_digit_labels_list)
    training_digit_info_list = sample(training_digit_info_list, amount_testing_data_digits[percentage])

    training_digit_info_list_KN = extract_features_matrix(train_digit_image_list, train_digit_labels_list)
    training_digit_info_list_KN = sample(training_digit_info_list_KN, amount_testing_data_digits[percentage])
    # testing
    testing_digit_info_list = extract_features(test_digit_image_list, test_digit_labels_list)
    testing_digit_info_list_KN = extract_features_matrix(test_digit_image_list, test_digit_labels_list)

    if sys.argv[2] == "-p":
        algo = "perceptron"
        guess = Perceptron.perceptron_digit_training(training_digit_info_list, testing_digit_info_list, 100)


    end_time = time.time() - start_time
    write_to_file("time-to-train.txt", end_time)
    print(algo)
    #exit() # to delete - time training


    accuracy = get_accuracy(guess, test_digit_labels_list)
    print(accuracy)
    write_to_file("results.txt", accuracy)
if sys.argv[1] == "-f":  # faces
    print("faces")
    train_face_image = "classification/data/facedata/facedatatrain"
    train_face_label = "classification/data/facedata/facedatatrainlabels"
    train_face_image_list = read_data(train_face_image, "face")
    train_face_labels_list = read_labels(train_face_label)

    test_face_image = "classification/data/facedata/facedatatest"
    test_face_label = "classification/data/facedata/facedatatestlabels"
    test_face_image_list = read_data(test_face_image, "face")
    test_face_labels_list = read_labels(test_face_label)
    # training
    training_face_info_list = extract_features(train_face_image_list, train_face_labels_list)
    training_face_info_list = sample(training_face_info_list, amount_testing_data_faces[percentage])

    training_face_info_list_KN = extract_features_matrix(train_face_image_list, train_face_labels_list)
    training_face_info_list_KN = sample(training_face_info_list_KN, amount_testing_data_faces[percentage])

    # testing
    testing_face_info_list = extract_features(test_face_image_list, test_face_labels_list)
    testing_face_info_list_KN = extract_features_matrix(test_face_image_list, test_face_labels_list)

    if sys.argv[2] == "-p":
        algo = "perceptron"
        guess = Perceptron.perceptron_face_training(training_face_info_list, testing_face_info_list, 100)

    end_time = time.time() - start_time
    write_to_file("time-to-train.txt", end_time)
    print(algo)
    #exit()  # to delete - time training



    accuracy = get_accuracy(guess, test_face_labels_list)
    print(accuracy)
    write_to_file("results.txt", accuracy)

print("\n")
