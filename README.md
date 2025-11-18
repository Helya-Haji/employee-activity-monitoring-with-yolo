# employee activity monitoring with yolo11n

This repository contains a project for detecting employee activities in office environments using YOLOv11n. The model identifies different states of employees based on images from a publicly available office dataset, which have been manually re-annotated for this project.

## Features

The model can detect and classify employees into four states:
* Sitting
* Standing
* Working
* Unavailable

The output can be applied to video streams, allowing real-time visualization and saving of detected employee activities.

## Dataset

We used the "Edinburgh office monitoring video dataset" Dataset as the base. For this project, all images were manually annotated to create custom labels for the employee states mentioned above. These custom annotations were used for training and evaluating the YOLOv11n model.
dataset citation: T. Qasim, R. B. Fisher, N. Bhatti; Ground-truthing Large Human Behavior Monitoring Datasets, Proc. 2020 Int. Conf on Pattern Recognition, online, 2021


## Summery

Architecture: YOLOv11n
Task: Object Detection
Classes: 4 (Sitting, Standing, Working, Unavailable)
Training: On the manually annotated dataset derived from the Edinburgh office monitoring video dataset
