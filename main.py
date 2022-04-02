import cv2

# функция обработки изображения
def process_img(img, color, name):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_mask = cv2.inRange(hsv_img, color[0], color[1])
    img_mixed = cv2.bitwise_and(img, img, mask=img_mask)
    cv2.imshow('mask' + name, img_mixed)

# выполняемая при изенении ползунка
def update(value = 0):
    color_low = (
        cv2.getTrackbarPos('h_min', 'ui'),
        cv2.getTrackbarPos('s_min', 'ui'),
        cv2.getTrackbarPos('v_min', 'ui')
    )
    color_high = (
        cv2.getTrackbarPos('h_max', 'ui'),
        cv2.getTrackbarPos('s_max', 'ui'),
        cv2.getTrackbarPos('v_max', 'ui')
    )
    
    color = (color_low, color_high)

    process_img(img, color, 'img')
    process_img(rainbow, color, 'rainbow')

img = cv2.imread('img/aquarium.jpg')
rainbow = cv2.imread('img/rainbow.png')

cv2.namedWindow('ui')
cv2.createTrackbar('h_min', 'ui', 0, 180, update)
cv2.createTrackbar('s_min', 'ui', 0, 255, update)
cv2.createTrackbar('v_min', 'ui', 0, 255, update)
cv2.createTrackbar('h_max', 'ui', 180, 180, update)
cv2.createTrackbar('s_max', 'ui', 255, 255, update)
cv2.createTrackbar('v_max', 'ui', 255, 255, update)

cv2.imshow('ui', img)
cv2.waitKey(0)