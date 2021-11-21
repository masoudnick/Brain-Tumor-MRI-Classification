# Brain Tumor MRI Classification Using Pre-trained Models

## What is a brain tumor?

A brain tumor is a collection, or mass, of abnormal cells in your brain. Your skull, which encloses your brain, is very rigid. Any growth inside such a restricted space can cause problems. Brain tumors can be cancerous (malignant) or noncancerous (benign). When benign or malignant tumors grow, they can cause the pressure inside your skull to increase. This can cause brain damage, and it can be life-threatening.

## The importance of the subject

Early detection and classification of brain tumors is an important research domain in the field of medical imaging and accordingly helps in selecting the most convenient treatment method to save patients life therefore.

## Basic Requirements

| **Package Name**      | **Version** |
| --------------------- | ----------- |
| `python`              | 3.7.12      |
| `tensorflow`          | 2.6.0       |
| `keras`               | 2.6.0       |
| `keras-preprocessing` | 1.1.2       |
| `matplotlib`          | 3.0.2       |
| `opencv`              | 4.1.2       |
| `scikit-learn`        | 0.22.2      |

## Dataset

The dataset was taken from [here](https://www.kaggle.com/masoudnickparvar/brain-tumor-mri-dataset).

### Dataset Details

This dataset contains **7022** images of human brain MRI images which are classified into 4 classes:

- glioma
- meningioma
- no tumor
- pituitary

About 22% of the images are intended for model testing and the rest for model training.
Pay attention that The size of the images in this dataset is different. You can resize images to the desired size after pre-processing and removing the extra margins.

### Data Pre-processing

Crop the part of the image that contains only the brain (which is the most important part of the image): The cropping technique is used to find the extreme top, bottom, left and right points of the brain using OpenCV. You can do this with [Preprocessing.py](https://github.com/masoudnick/Brain-Tumor-MRI-Classification/blob/main/Preprocessing.py)

![preprocessing result](https://github.com/masoudnick/Brain-Tumor-MRI-Classification/blob/main/preprocess.jpg)

## Pre-trained Model

A pre-trained model is a model that was trained on a large benchmark dataset to solve a problem similar to the one that we want to solve. Accordingly, due to the computational cost of training such models, it is common practice to import and use models from published literature (e.g. VGG, Inception, ResNet50). For this project, I decided to use **ResNet50** model to perform image classification for brain tumor MRI images.[Resnet50 Article](https://arxiv.org/abs/1512.03385)

## Note
You can see more details about training steps and testing results inside [Brain_Tumor_Classification.ipynb](https://github.com/masoudnick/Brain-Tumor-MRI-Classification/blob/main/Brain_Tumor_Classification.ipynb)

