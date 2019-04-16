import cv2

cap = cv2.VideoCapture(0)

def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480():
    cap.set(3, 640)
    cap.set(4, 480)

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

def rescale_frame(frame, percent):
    scale_percent = percent
    width = int(frame.shape[1] * scale_percent/100)
    height = int(frame.shape[0] * scale_percent/100)
    dim = (width,height)
    return cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)



#change_res(6464, 4864)
#make_720p()
#make_480()
make_1080p()

while True:
    ret, frame = cap.read()

    """frame = rescale_frame(frame, 30)

    cv2.imshow('frame', frame)"""

    frame2 = rescale_frame(frame, 145)

    cv2.imshow('Fullscreen', frame2)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
