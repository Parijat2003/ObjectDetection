from ultralytics import YOLO 

model = YOLO('models/best.pt')
results = model.predict('input_video/test.mp4', save=True) 