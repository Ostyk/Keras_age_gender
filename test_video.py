
video_path = "raw_videos\\DT Order Taker_2020102778_20201027070000_20201027080000.mp4"
import cv2
cap = cv2.VideoCapture(video_path)
count=0
while cap.isOpened():
    ret, frame = cap.read()
    #print(ret)
    count += 1
    #cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
print(f"count: {count}")
cap.release()