import cv2

vid_capture = cv2.VideoCapture(0)
if(not(vid_capture.isOpened())):
    print("Error starting webcam")
else:
    fps = vid_capture.get(5)
    print("Frame rate (per second): ", fps, 'FPS')


while(vid_capture.isOpened()):
    ret, frame = vid_capture.read()
    if(ret):
        cv2.imshow('Frame', frame)
        key = cv2.waitKey(100)

        if(key == ord('q')):
            break
    else:
        break
vid_capture.release()
cv2.destroyAllWindows()
