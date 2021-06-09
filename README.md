# Homework6
 efficientdet for target detection

How to train:
1. First please download the released dataset in https://drive.google.com/file/d/1YkH4nmZxhZ-b3cFztre8cWcUJJfE-GcP/view?usp=sharing
2. Unzip the dataset, there are three folder. 
      Copy the test_images to the floder of data.
      Copy the JPEGImages and Annotations to the floder of VOCdevkit\VOC2007.
3. Run voc2efficientdet.py to generate txt files.
4. Run voc_annotation.py to input classes. (You can modify the new_classes.txt to change classes.)
5. Run train.py for training.

How to predict:
1. Run predict.py

How to test:
1. Run test.py to generate test.csv (Please make sure that the test data is placed in the test/test_images)
