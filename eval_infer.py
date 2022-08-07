import cv2
import numpy as np
import tools.infer.utility as utility
import tools.infer.predict_rec as predict_rec

args = utility.parse_args()
#args.rec_model_dir = './inference/ch_PP-OCRv3_rec_infer'
args.rec_model_dir = './inference/en_PP-OCRv3_rec_infer/'
text_recognizer = predict_rec.TextRecognizer(args)

data_label = './train_data/rec/train.txt'
with open(data_label, 'r') as f:
    annotations = f.readlines()

    correct = 0
    for item in annotations:
        path, label = item.split("\t")
        image = cv2.imread(path)
        label = label.replace(" ", "").replace("\n", "")
        h,w,c = image.shape
        image = image.reshape(1,h,w,c)
        rec_res, elapse = text_recognizer(image)
        result = rec_res[0][0].replace(" ", "")
        if result == label:
            correct += 1

    print('acc', correct / len(annotations))
