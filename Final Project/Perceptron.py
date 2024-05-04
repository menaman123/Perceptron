#Authors: Anna Godin & Kimberly Wolak


import decimal

import random


def perceptron_face_training(face_image_data_training, face_image_data_testing, feature_size):
    weights = []  # 0....100, weight[0] is the bias
    num_right = 0
    num_rounds = 0
    percent_accuracy = 0
    for i in range(0, feature_size + 1):  # assigning random weights
        weights.append(decimal.Decimal(random.randrange(-50, 50)) / 100)
    # print weights
    while percent_accuracy < .85 and num_rounds < 1000:
        for image in face_image_data_training:
            # image = face_image_data_training[0]
            fx = 0
            for j in range(1, feature_size + 1):  # 1-100
                # print str(image.class_features[j - 1]) + ", " + str(weights[j]),
                fx += weights[j] * image.class_features[j - 1]  # calculate f(x)

            # print "\n"
            # print fx
            # print image.class_label
            if fx < 0 and image.class_label == '0':
                # print "correct!"
                num_right += 1
            elif fx >= 0 and image.class_label == '1':
                # print "correct!"
                num_right += 1
            elif fx < 0 and image.class_label == '1':
                # print "wrong prediction"
                for i in range(1, feature_size + 1):
                    weights[i] += image.class_features[i - 1]
                weights[0] += 1
                # print weights
            elif fx >= 0 and image.class_label == '0':
                # print "wrong prediction"
                for i in range(1, feature_size + 1):
                    weights[i] -= image.class_features[i - 1]
                weights[0] -= 1
                # print weights
            num_rounds += 1
        percent_accuracy = float(num_right) / num_rounds
        # print "percent accuracy: " + str(float(num_right) / num_rounds)
    # print num_rounds
    # print num_right

    # -----------------------------------------------------------------------------------------#
    # TESTING TIME
    # -----------------------------------------------------------------------------------------#

    guess_array = []
    for image in face_image_data_testing:
        fx = 0
        for j in range(1, feature_size + 1):  # 1-100
            # print str(image.class_features[j - 1]) + ", " + str(weights[j]),
            fx += weights[j] * image.class_features[j - 1]  # calculate f(x)
        if fx < 0:
            guess_array.append('0')
        else:
            guess_array.append('1')

    return guess_array


def perceptron_digit_training(digit_image_data_training, digit_image_data_testing, feature_size):
    # 2D array containing weights for each number, ex digit_weights[0] contains the 100 weights for the digit 0
    digit_weights = []
    num_right = 0
    num_rounds = 0
    percent_accuracy = 0

    for i in range(10):
        weights_single_digit = []
        for j in range(0, feature_size + 1):  # assigning random weights
            weights_single_digit.append(decimal.Decimal(random.randrange(-50, 50)) / 100)
        digit_weights.append(weights_single_digit)
        # print digit_weights[i]
        # print "\n"
    # print digit_weights

    # while percent_accuracy < .85 and num_rounds < 1000:

    for image in digit_image_data_training:
        fxs = []
        # image = digit_image_data_training[0]
        # print image.class_features
        # print image.class_label
        for i in range(10):
            fx = 0
            for j in range(1, feature_size + 1):  # 1-100, going through each feature
                # print str(image.class_features[j - 1]) + ", " + str(digit_weights[i][j]) + ". ", #print the feature count and the weight for digit i, weight j
                fx += digit_weights[i][j] * image.class_features[j - 1]  # calculate f(x) for digit i
            fxs.append(fx)

        max_val = max(fxs)
        predicted_digit = fxs.index(max_val)
        # print max_val
        # print "predicted digit " + str(predicted_digit)
        # print "actual digit " + image.class_label

        if predicted_digit == int(image.class_label):
            # print "correct!"
            num_right += 1
        else:
            # print "wrong prediction"
            # add to actual digit weight
            for i in range(1, feature_size + 1):
                digit_weights[int(image.class_label)][i] += image.class_features[i - 1]
            digit_weights[int(image.class_label)][0] += 1

            # subtract from predicted weight
            for i in range(1, feature_size + 1):
                digit_weights[predicted_digit][i] -= image.class_features[i - 1]
            digit_weights[predicted_digit][0] -= 1

        num_rounds += 1
        # percent_accuracy = float(num_right) / num_rounds
        # print "num right: " + str(num_right)
        # print "num rounds: " + str(num_rounds)
        # print percent_accuracy

    # -----------------------------------------------------------------------------------------#
    # TESTING TIME
    # -----------------------------------------------------------------------------------------#
    guess_array = []
    for image in digit_image_data_testing:
        fxs = []
        for i in range(10):
            fx = 0
            for j in range(1, feature_size + 1):  # 1-100, going through each feature
                fx += digit_weights[i][j] * image.class_features[j - 1]  # calculate f(x) for digit i
            fxs.append(fx)

        max_val = max(fxs)
        predicted_digit = fxs.index(max_val)
        guess_array.append(str(predicted_digit))

    return guess_array
