
video_path = "raw_videos\\dt.mp4"
import cv2
cap = cv2.VideoCapture(video_path)
while cap.isOpened():
    ret, frame = cap.read()
    print(ret, frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()