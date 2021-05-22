# Malaria_detection

 
## **The Goal**
To reduce the burden for microscopists in resource-constrained regions and improve the accuracy of diagnosis of Malaria by applying Deep Learning and utilizing Neural Networks.

 
## **Background**

![image](https://user-images.githubusercontent.com/80243823/119223701-72455180-bb2d-11eb-9fa0-0d7270824d62.png)


![image](https://user-images.githubusercontent.com/80243823/119223573-d582b400-bb2c-11eb-9035-f7a7e2b7b939.png)

Researchers at the Lister Hill National Center for Biomedical Communications (LHNCBC), part of National Library of Medicine (NLM), have developed a mobile application that runs on a standard Android smartphone attached to a conventional light microscope. A repository of segmented cells from the thin blood smear slide images from the Malaria Screener research activity has been established using the smartphone’s built-in camera.

The repository contains 13779 thin blood smear slide images of both infected and uninfected patients, a total of 27558 images which were manually annotated by an expert slide reader at the Mahidol-Oxford Tropical Medicine Research Unit in Bangkok, Thailand.

**Uninfected sample**

![C49P10thinF_IMG_20150724_102951_cell_111](https://user-images.githubusercontent.com/80243823/119223958-c0a72000-bb2e-11eb-9fb7-1c1e8b8d69a6.png)
![C183P144NThinF_IMG_20151201_223357_cell_35](https://user-images.githubusercontent.com/80243823/119223975-d9afd100-bb2e-11eb-9548-6e1282e86468.png)
![C186P147NThinF_IMG_20151203_150557_cell_67](https://user-images.githubusercontent.com/80243823/119223989-ecc2a100-bb2e-11eb-935d-cd0e0c953bc1.png)
![C233ThinF_IMG_20151112_161119_cell_164](https://user-images.githubusercontent.com/80243823/119224013-0b289c80-bb2f-11eb-8b2e-e1b369cab862.png)
![C3thin_original_IMG_20150608_162835_cell_77](https://user-images.githubusercontent.com/80243823/119224032-209dc680-bb2f-11eb-84e5-cec0aed7a738.png)

**Infected sample**

![C39P4thinF_original_IMG_20150622_105102_cell_84](https://user-images.githubusercontent.com/80243823/119224042-37441d80-bb2f-11eb-8a68-a01bfe9c7811.png)
![C39P4thinF_original_IMG_20150622_105102_cell_96](https://user-images.githubusercontent.com/80243823/119224044-39a67780-bb2f-11eb-8f37-d007b7220607.png)
![C39P4thinF_original_IMG_20150622_110115_cell_112](https://user-images.githubusercontent.com/80243823/119224048-3d39fe80-bb2f-11eb-8804-a5e9251653e6.png)
![C176P137NThinF_IMG_20151201_120845_cell_127](https://user-images.githubusercontent.com/80243823/119224056-42974900-bb2f-11eb-99ac-3b2c80ce20df.png)
![C176P137NThinF_IMG_20151201_121808_cell_136](https://user-images.githubusercontent.com/80243823/119224058-46c36680-bb2f-11eb-8ce8-fdfd0a8dab2e.png)


## **The approach**

Unlike general images which have countless unpredictable features, thin blood smear slide images are relatively identical, with the infected images having a few distinctive features. Therefore, extracting useful features out of the images may improve the accuracy by a lot.
Therefore, instead of letting the Neural Networks to learn and classify the raw images, Convolutional Neural Networks (CNN) is first applied to extract important features of the raw images, then the Neural Networks classifies the images based on the extracted features. This approach may increase the accuracy of the model, and is also computationally efficient, thus less time and hardware resources are required.

![image](https://user-images.githubusercontent.com/80243823/119227783-34065d00-bb42-11eb-8058-78817b769a8c.png)


## **Model construction**

**Image loading**

First, all available images have to be processed before feeding them to the model as they have different sizes. Also 27558 images require substantial amount of memory to process, adjusting the resolution of the image is necessary. After multiple testings, 64 x 64 resolution was adopted as it strikes a good balance of having a good model accuracy and not needing too much memory.

The data is then split into training set and testing set under 80:20 ratio respectively.

![image](https://user-images.githubusercontent.com/80243823/119229163-2a342800-bb49-11eb-97e8-88342b251f91.png)


**Convolutional Neural Networks**

For each layer, a 2D-convolution matrix is used to extract features, then MaxPooling is applied so that the most distinctive feature can be used to represent a small area of the image.

![image](https://user-images.githubusercontent.com/80243823/119229756-f9092700-bb4b-11eb-9696-0a2d2ee6f7ae.png)

**Neural Networks for classification (infected or not)**

After extracting the important features of an image, a neuron network for classification is then applied to analyse if the sample is infected with Malaria or not.

![image](https://user-images.githubusercontent.com/80243823/119229991-eb07d600-bb4c-11eb-9008-ff6a40e58af7.png)


**The complete model**

![image](https://user-images.githubusercontent.com/80243823/119230076-43d76e80-bb4d-11eb-8c9c-3cfeadf57690.png)


## **Model performance**

This is the learning progress of the model and its accuracy at different stages. The initial plan is to train the model 20 times (20 epochs). If further training doesn't improve its accuracy by a meaningful amount, the training would stop earlier after a few observations.


First, a simple model is trained and tested.

![image](https://user-images.githubusercontent.com/80243823/119230970-2d331680-bb51-11eb-9a73-6dceff6f4907.png)
![image](https://user-images.githubusercontent.com/80243823/119230994-3f14b980-bb51-11eb-98e7-c9b38e143bb0.png)
![image](https://user-images.githubusercontent.com/80243823/119231014-4dfb6c00-bb51-11eb-85a6-0c42a6c7095c.png)

The accuracy is only about 50%, there is room to improve.


Then a more complex classification neuron network is trained and tested.

![image](https://user-images.githubusercontent.com/80243823/119230860-97978700-bb50-11eb-8e24-134427bcb4ee.png)
![image](https://user-images.githubusercontent.com/80243823/119230850-877fa780-bb50-11eb-862b-017fe9a9ba8f.png)
![image](https://user-images.githubusercontent.com/80243823/119230883-b5fd8280-bb50-11eb-8b54-e7f5960c37be.png)

A substantial improvement over the last model, the accuracy reaches 96%. However, the validation accuracy (testing dataset result) is lower than the training accuracy, which means the model is slightly overfitting, and may not perform as well in real life.


This time, instead of having a more complex classification neuron network, a more complex Convolutional Neural Networks is deployed.
Since the Convolutional Neural Networks is doing the 'heavy lifting' in this case, the neuron network for classification shouldn't require much complexity to do the task. A simple model is applied with low number of neurons.

![image](https://user-images.githubusercontent.com/80243823/119230076-43d76e80-bb4d-11eb-8c9c-3cfeadf57690.png)
![image](https://user-images.githubusercontent.com/80243823/119230283-1808b880-bb4e-11eb-9a69-2d62f081bf6d.png)
![image](https://user-images.githubusercontent.com/80243823/119230302-2e167900-bb4e-11eb-84cf-4341a671df52.png)

This model has 95.98% accuracy in the training dataset, and 95.3% accuracy in the validation dataset (testing set). Having high and close accuracy between training dataset and testing dataset indicates that the model is having optimal complexity, not overfitting, not underfitting. It would most likely perform stably and well in real life.


## **Other possible models and their perforemances**

Using publicly available pre-trained network

There are publicly available pre-trained networks which were trained using millions of images for general image recognition purposes. They usually perform well and require little tuning. To suit the purpose of this project, classification neuron network is added on top of the pre-trained model. In short, use a trained network without tuning for extracting image features, then only train a part of the neuron network for classification.

![image](https://user-images.githubusercontent.com/80243823/119232711-cade1400-bb58-11eb-84b4-d5b554608b10.png)
![image](https://user-images.githubusercontent.com/80243823/119232157-b8fb7180-bb56-11eb-83fd-6565fb74cf4e.png)
![image](https://user-images.githubusercontent.com/80243823/119232172-c7e22400-bb56-11eb-997f-6da72871cffb.png)

The result, however, is not satisfactory as the accuracy is only about 64%. As the pre-trained network is suited for general image recognition, for images like thin blood smear slide images, a specialised new network may perform better.


## **Result**
A neuron network with over 95% accuracy in detecting presence of Malaria in a thin blood smear slide image is trained. As the network can process thousands of images in an instant,  the burden for microscopists in resource-constrained regions is sucessfully reduced and accuracy of diagnosis of Malaria improved by applying Deep Learning and utilizing Neural Networks. 
