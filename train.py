import comet_ml
import datetime
# comet_ml.config.save(api_key = 'Qn88wPyWB3PmP0hTUAwhg1h9u')
experiment = comet_ml.Experiment(
        project_name= "Rebar_Segmentation"
)
experiment.set_name(f"trial{datetime.datetime.now().date().strftime('%Y%m%d')}")
# import os 
# os.environ["OMP_NUM_THREADS"] = '8'

import ultralytics
from ultralytics import YOLO
ultralytics.checks()

#Train a model
LOCAL_PATH = 'datasets\constructive_seg\dataset.yaml'
SERVER_PATH = 'datasets/panel/YOLODataset/data_dayhoff.yaml'

model = YOLO(model='yolov8n-seg.pt')
result = model.train(data=SERVER_PATH,
                     epochs = 300,
                     lr0 = 1E-3,
                     lrf = 1E-6,
                     optimiser = 'AdamW',
                     save = True,
                     plots = True,
                     val = True,
                     cache = True,
                     augment = False,
                     project = f'run/seg_train_{datetime.date.today().isoformat()}'
                     )
