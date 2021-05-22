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

Instead of letting the Neural Networks to learn and classify the raw images, Convolutional Neural Networks (CNN) is first applied to extract important features of the raw images, then the Neural Networks classifies the images based on the extracted features. This approach may increase the accuracy of the model, and is also computationally efficient, thus less time and hardware resources are required.

![fullconvlayervisual](https://user-images.githubusercontent.com/80243823/119224275-44154100-bb30-11eb-8c58-30cda360d672.jpeg)



