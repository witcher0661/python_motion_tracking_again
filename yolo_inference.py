from ultralytics import YOLO 

model = YOLO(r"C:\Users\44780\Documents\python_motion_tracking_again\models\best.pt")

results = model.predict(r"C:\Users\44780\Documents\python_motion_tracking_again\input_videos\08fd33_4.mp4",save=True)
print(results[0])
print('=====================================')
for box in results[0].boxes:
    print(box)