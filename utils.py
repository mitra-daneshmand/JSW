import numpy as np
import cv2


def coordinates(points_file):
    line_count = 0
    x = []
    y = []

    with open(points_file) as fp:
        for line in fp:
            if 3 <= line_count < 151:
                x_temp = line.split(" ")[0]
                y_temp = line.split(" ")[1]
                y_temp = y_temp.replace("\n", "")
                x.append((float(x_temp)))
                y.append((float(y_temp)))
            line_count += 1
    return x, y


def jsw_lm(x, y):
    # Finding the main points of Right knee
    x_l_r_f = x[88]
    y_l_r_f = y[88]
    x_l_r_t = x[123]
    y_l_r_t = y[123]

    x_m_r_f = x[96]
    y_m_r_f = y[96]
    x_m_r_t = x[135]
    y_m_r_t = y[135]

    # Finding the main points of Left knee
    x_l_l_f = x[14]
    y_l_l_f = y[14]
    x_l_l_t = x[49]
    y_l_l_t = y[49]

    x_m_l_f = x[22]
    y_m_l_f = y[22]
    x_m_l_t = x[61]
    y_m_l_t = y[61]

    jsw_l_left = np.linalg.norm([(x_l_l_f - x_l_l_t), (y_l_l_f - y_l_l_t)])
    jsw_m_left = np.linalg.norm([(x_m_l_f - x_m_l_t), (y_m_l_f - y_m_l_t)])
    jsw_l_right = np.linalg.norm([(x_l_r_f - x_l_r_t), (y_l_r_f - y_l_r_t)])
    jsw_m_right = np.linalg.norm([(x_m_r_f - x_m_r_t), (y_m_r_f - y_m_r_t)])

    return jsw_l_left, jsw_m_left, jsw_l_right, jsw_m_right


def visualizing_landmarks(img, xs, ys):

    image = cv2.line(img, (int(xs[14]), int(ys[14])), (int(xs[49]), int(ys[49])), (255, 255, 0), 5)
    image = cv2.line(image, (int(xs[22]), int(ys[22])), (int(xs[61]), int(ys[61])), (0, 144, 245), 5)
    image = cv2.line(image, (int(xs[96]), int(ys[96])), (int(xs[135]), int(ys[135])), (0, 144, 245), 5)
    image = cv2.line(image, (int(xs[88]), int(ys[88])), (int(xs[123]), int(ys[123])), (255, 255, 0), 5)

    for i in range(len(xs)):
        if i == 14 or i == 49 or i == 88 or i == 123:
            image = cv2.circle(image, (int(xs[i]), int(ys[i])), 8, (255, 255, 0), -1)
        elif i == 22 or i == 61 or i == 96 or i == 135:
            image = cv2.circle(image, (int(xs[i]), int(ys[i])), 8, (0, 144, 245), -1)
        else:
            image = cv2.circle(image, (int(xs[i]), int(ys[i])), 7, (255, 0, 144), -1)

    cv2.imwrite("sample/img.png", image)
    return image

