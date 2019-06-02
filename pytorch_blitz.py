#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Macbook Jun 2 09:43:28 2019

@author: zhuzhu
"""

import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3,6,5)
        self.conv2 = nn.Conv2d(6,16,5)
        
        self.fc1 = nn.Linear(16*5*5,120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)
        
    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)),(2,2))
        x = F.max_pool2d(F.relu(self.conv2(x)),(2,2))
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        
        return x
    
    def num_flat_features(self, x):
        size = x.size()[1:]
        num_features = 1
        for i in size:
            num_features *= i
        return num_features
 
net = Net()

criterion = nn.CrossEntropyLoss()

optimizer = optim.SGD(net.parameters(),lr=0.001,momentum=0.9)

transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))
        ])
trainset = torchvision.datasets.CIFAR10(root='./data',train=True,download=True,transform=transform)
trainloader = torch.utils.data.DataLoader(trainset,batch_size=4,shuffle=True,num_workers=2)
testset = torchvision.datasets.CIFAR10(root='./data',train=False,download=True,transform=transform)
testloader = torch.utils.data.DataLoader(testset,batch_size=4,shuffle=False,num_workers=2)

classes = ('plane','car','bird','cat',
           'deer','dog','frog','horse','ship','truck')

def imshow(img):
    img = img/2+0.5
    img = img.numpy()
    plt.imshow(np.transpose(img, (1,2,0)))
    plt.show()

for epoch in range(2):
    running_loss = 0
    for i, data in enumerate(trainloader):
        imgs, labels = data
        optimizer.zero_grad()
        outs = net(imgs)
        loss = criterion(outs, labels)
        loss.backward()
        running_loss += loss
        optimizer.step()
        if i % 2000 == 1999:
            print('[%d,%5d] loss:%.3f'%(epoch+1,i+1,running_loss/2000))
            runing_loss = 0
print('Training finished!')
