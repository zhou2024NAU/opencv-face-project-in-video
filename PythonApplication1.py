import os
import cv2
from PIL import Image
import numpy as np
def getImageAndLabels(path):
    
if-_name_-==__main_-:
#ͼƬ·��
path='./data/jm/
#��ȡͼ�������1d��ǩ���������
faces,ids=getImageAndLabels(path)
#����ʶ����
recognizer=cv2.face.LBPHFaceRecognizer_create()
#ѵ��
recognizer.train(faces,np.array(ids))
#�����ļ�
recognizer.write('trainer/trainer.yml')
