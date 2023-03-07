import cv2

'''
    @func: 
        cvAlgorithm: video(image) process;
    @para:
        cap: video;
'''

def cvAlgorithm(cap):
    ret, frame = cap.read()

    # Converting to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Otsu method binarization
    retval, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

    # Expansion, white area becomes larger
    dst = cv2.dilate(dst, None, iterations=2)
    dst = cv2.erode(dst, None, iterations=6)
    dst = cv2.dilate(dst, None, iterations=2)
    dst = cv2.erode(dst, None, iterations=6)
    dst = cv2.dilate(dst, None, iterations=2)
    dst = cv2.erode(dst, None, iterations=6)

    return dst