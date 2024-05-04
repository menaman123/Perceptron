import decimal

import random


def perceptron_face_training(face_image_data_training, face_image_data_testing, feature_size):
    weights = []
    num_right = 0
    num_rounds = 0
    percent_accuracy = 0
    for i in range(0, feature_size + 1):
        weights.append(decimal.Decimal(random.randrange(-50, 50)) / 100)
    # print weights
    while percent_accuracy < .85 and num_rounds < 1000:
        for image in face_image_data_training:
            fx = 0
            for j in range(1, feature_size + 1):
                fx += weights[j] * image.class_features[j - 1]
            if fx < 0 and image.class_label == '0':
                num_right += 1
            elif fx >= 0 and image.class_label == '1':
                num_right += 1
            elif fx < 0 and image.class_label == '1':
                for i in range(1, feature_size + 1):
                    weights[i] += image.class_features[i - 1]
                weights[0] += 1
            elif fx >= 0 and image.class_label == '0':
                for i in range(1, feature_size + 1):
                    weights[i] -= image.class_features[i - 1]
                weights[0] -= 1
            num_rounds += 1
        percent_accuracy = float(num_right) / num_rounds


    guess_array = []
    for image in face_image_data_testing:
        fx = 0
        for j in range(1, feature_size + 1):
            fx += weights[j] * image.class_features[j - 1]
        if fx < 0:
            guess_array.append('0')
        else:
            guess_array.append('1')

    return guess_array


def perceptron_digit_training(digit_image_data_training, digit_image_data_testing, feature_size):
    digit_weights = []
    num_right = 0
    num_rounds = 0

    for i in range(10):
        weights_single_digit = []
        for j in range(0, feature_size + 1):
            weights_single_digit.append(decimal.Decimal(random.randrange(-50, 50)) / 100)
        digit_weights.append(weights_single_digit)

    for image in digit_image_data_training:
        fxs = []
        for i in range(10):
            fx = 0
            for j in range(1, feature_size + 1):
                fx += digit_weights[i][j] * image.class_features[j - 1]
            fxs.append(fx)

        max_val = max(fxs)
        predicted_digit = fxs.index(max_val)

        if predicted_digit == int(image.class_label):
            num_right += 1
        else:
            for i in range(1, feature_size + 1):
                digit_weights[int(image.class_label)][i] += image.class_features[i - 1]
            digit_weights[int(image.class_label)][0] += 1

            for i in range(1, feature_size + 1):
                digit_weights[predicted_digit][i] -= image.class_features[i - 1]
            digit_weights[predicted_digit][0] -= 1

        num_rounds += 1
    guess_array = []
    for image in digit_image_data_testing:
        fxs = []
        for i in range(10):
            fx = 0
            for j in range(1, feature_size + 1):
                fx += digit_weights[i][j] * image.class_features[j - 1]
            fxs.append(fx)

        max_val = max(fxs)
        predicted_digit = fxs.index(max_val)
        guess_array.append(str(predicted_digit))

    return guess_array
