import torch
import torchvision.datasets

import numpy as np
from PIL import Image
import dataload.preprocess as preprocess

minist_classes = ('zero', 'one', 'two', 'three',
           'four', 'five', 'six', 'seven', 'eight', 'nine')

fashionminst_classes = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal',
               'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

def mnist_dataset(transform, train=False):
    dataset = torchvision.datasets.MNIST(root='./dataset/mnist',
                                         train=train,
                                         download=False,
                                         transform=transform)

    return dataset

def fashionmnist_dataset(transform, train=False):
    dataset = torchvision.datasets.FashionMNIST(root='./dataset/fashionmnist',
                                         train=train,
                                         download=False,
                                         transform=transform)

    return dataset


if __name__ == "__main__":
    image = (Image.open('../left.png'))
    print(image.size)
    process = preprocess.get_transform((32,32))
    image = process(image)
    print(image.size())