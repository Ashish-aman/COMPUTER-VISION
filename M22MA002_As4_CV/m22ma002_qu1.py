# -*- coding: utf-8 -*-
"""m22ma002_qu1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zGTmqLmKyAEF_KriYRpGkZ9uPzh5kQFi
"""

# pytorch workflow
import torch
from torch import nn
import numpy as np
import matplotlib.pyplot as plot
import torchvision
from torch import nn
from torch.utils.data import DataLoader
import torch.nn.functional as F
from torchvision import datasets
from torchvision.transforms import ToTensor
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
torch.__version__
from torchvision.datasets import MNIST

# Set device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

train_transform = transforms.Compose(
    [
        
        # torch.tensor(random_noise(img, mode='gaussian', mean=0, var=0.05, clip=True)),
        torchvision.transforms.GaussianBlur(kernel_size=3, sigma=(0.1, 2.0)),
        
        transforms.ToTensor(),
        transforms.Normalize((0.5), ( 0.5)),
    ]
)
test_transform = transforms.Compose(
    [
        transforms.ToTensor(),
        transforms.Normalize((0.5), (0.5)),
    ]
)

# transform = transforms.Compose([transforms.Grayscale(num_output_channels=3),transforms.ToTensor(),])

from torchvision.datasets import MNIST
from torchvision.transforms import transforms
from torch.utils.data import DataLoader, SubsetRandomSampler
import numpy as np
from torch.utils.data import Subset

# Load the MNIST dataset
dataset1 = MNIST(root='./data', train=True, download=True, transform=train_transform)
# dataset1 = MNIST(root='./data', train=True, download=True, transform=transform)
print(type(dataset1))
# Get the total number of samples in the dataset
num_samples = len(dataset1)

# Define the sizes of the two subsets
subset1_size = int(0.8 * num_samples)
subset2_size = num_samples - subset1_size

# Create two subsets of the dataset
subset1 = Subset(dataset1, range(subset1_size))
subset2 = Subset(dataset1, range(subset1_size, num_samples))
print(type(subset1))



batch_size = 64
train_loader = DataLoader(subset1, batch_size=batch_size,shuffle =True)
test_loader = DataLoader(subset2, batch_size=batch_size,shuffle  = False)

# # Load the MNIST dataset
# train_dataset = MNIST(root='./data', train=True, download=True, transform=train_transform)
# # test_dataset = MNIST(root='./data', train=False, download=True, transform=test_transform)

# # Define the data loaders
# batch_size = 64
# train_loader = DataLoader(train_loader, batch_size=batch_size, shuffle=True)
# test_loader = DataLoader(test_loader, batch_size=batch_size, shuffle=True)
print(len(train_loader))
print(len(test_loader))
# print((test_loader.shape))

transform = transforms.Compose([transforms.Grayscale(num_output_channels=3),transforms.ToTensor(),])

subset1 = torchvision.datasets.MNIST(root='data', train=True, download=True, transform=transform)
subset2 = torchvision.datasets.MNIST(root='data', train=False, download=True, transform=transform)

subset1,subset2

train_loader = torch.utils.data.DataLoader(dataset=subset1, batch_size=batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=subset2, batch_size=batch_size, shuffle=False)

for X, y in test_loader:
    print(f"Shape of X [N, C, H, W]: {X.shape}")
    print(f"Shape of y: {y.shape} {y.shape}")
    break

for i in range(6):
  plt.subplot(2,3,i+1)
  plt.imshow(X[i][0])
plt.show()

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline

classes = ('0', '1', '2', '3',
           '4', '5', '6', '7', '8', '9')
# helper function to un-normalize and display an image
def imshow(img):
    img = img / 2 + 0.5 
    img = img / 2 + 0.5  # unnormalize
    plt.imshow(np.transpose(img, (1, 2, 0)))  # convert from Tensor image
# obtain one batch of training images
dataiter = iter(test_loader)
images, labels = next(dataiter)
images = images.numpy() # convert images to numpy for display
# plot the images in the batch, along with the corresponding labels
fig = plt.figure(figsize=(25, 4))
# display 20 images
for idx in range(20):
  ax = fig.add_subplot(2, 20 , idx+1)
  
  imshow(images[idx])
  ax.set_title(classes[labels[idx]])

# Get cpu or gpu device for training.
device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
print(f"Using {device} device")
#hyperparameters
# input_size=1024



# Define model
# Define the network architecture
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # self.flat = nn.Flatten()
        self.conv1 = nn.Conv2d(3, 5, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(5, 5, kernel_size=3, stride=1, padding=1)
        self.conv3 = nn.Conv2d(5, 5, kernel_size=3, stride=1, padding=1)
        self.conv4 = nn.Conv2d(5, 5, kernel_size=3, stride=1, padding=1)
        self.conv5 = nn.Conv2d(5, 5, kernel_size=3, stride=1, padding=1)
        self.conv6 = nn.Conv2d(5, 5, kernel_size=3, stride=1, padding=1)
        self.conv7 = nn.Conv2d(5, 5, kernel_size=3, stride=1, padding=1)
        self.conv8 = nn.Conv2d(5, 5, kernel_size=3, stride=1, padding=1)        
        self.maxpool = nn.MaxPool2d(kernel_size=2, stride=2)
        # self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.flat = nn.Flatten()
        self.fc = nn.Linear(45, 10)
        # self.fc1 = nn.Linear(520, 10)

    def forward(self, x):
        # x = self.flat(x)
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        # x = self.pool(x)
        x = F.relu(self.conv3(x))
        x = self.maxpool(x)
        x = F.relu(self.conv4(x))
        x = F.relu(self.conv5(x))
        x = F.relu(self.conv6(x))
        x = self.maxpool(x)
        x = F.relu(self.conv7(x))
        x = F.relu(self.conv8(x))
        x = self.maxpool(x)
        # print(x.shape)
        # print(x.shape)
        # x = x.view(-1, 256 * 8 * 8)
        x = self.flat(x)
        # x = F.relu(self.fc(x))
        # x = self.fc1(x)
        # x=  F.softmax(x, dim=1)
        x = self.fc(x)
        x=  F.softmax(x, dim=1)
        # print(x.shape)
        return x


device = ("cuda" if torch.cuda.is_available() else "cpu")
print(device)
model = Net().to(device)

# # net

net = Net().to(device)
optimizer = torch.optim.Adam(net.parameters(), lr=0.001)
# optimizer = torch.optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
# Define the loss function
criterion = nn.CrossEntropyLoss()

train_loss = []
def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    model.train()
    # print(model)
    #batch = enumerate(dataloader)
    # print(batch)
    tt_loss = 0
    for batch, (X, y) in enumerate(dataloader):
        #print(batch)
        # print(y)
        # Y = []
        # for i in y:
        #   if i.item() % 2 == 0:
        #     Y.append((i.item()//2)+1)
        #   else:
        #     Y.append(i.item()//2)
        
        # y = torch.tensor(Y)
        # print(y)
        X, y = X.to(device), y.to(device)
        # print(type(X))
        # X=torchvision.transforms.functional.rgb_to_grayscale(X,1)
        # X=X.reshape(-1,32*32).to(device)

        # Compute prediction error
        # print("Images: ",X.shape)
        pred = model(X)
        # print(pred)
        loss = loss_fn(pred, y)
        tt_loss += loss
        #loss = (pred - y)
        # Backpropagation
        optimizer.zero_grad()
        # print(type(loss))
        # print(f"gradient of loss:-{loss}")
        loss.backward()
        # for i in model.parameters():
        #  print(f" i is {i}, value is {i.grad}")
        #print(f"gradient of loss:-{loss.grad}")
        optimizer.step()
        #print(optimizer)
        #print(f"gradient of loss:-{loss.grad.data}")
        #print(f"gradient of loss:-{.grad}")

        if batch % 100 == 0:
            #print(f"batch is {batch} , len(X) is : {len(X)}")
            loss, current = loss.item(), batch*len(X)
            print(f"loss: {loss:>3f}  [{current:>5d}/{size:>5d}]")
    train_loss.append(tt_loss.item() / len(dataloader))
#train(train_dataloader, model, loss_fn, optimizer)

num_classes = 10
matrix = [[0 for _ in range(num_classes)] for _ in range(num_classes)]
def confusion_matrix(actual, predicted,matrix):
    
    for a, p in zip(actual, predicted):
        matrix[a][p] += 1
    return matrix

a,b=1,2
a,b

test_l = []
def test(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    print(f"size :{size}, num_batches : {num_batches} ")
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for X, y in dataloader:
            # print(y)
            # Y = []
            # for i in y:
            #   if i.item() % 2 == 0:
            #     Y.append((i.item()//2)+1)
            #   else:
            #     Y.append(i.item()//2)
            
            # y = torch.tensor(Y)
            # print(y)
            X, y = X.to(device), y.to(device)

            
            # X=torchvision.transforms.functional.rgb_to_grayscale(X,1)
            # X=X.reshape(-1,32*32).to(device)
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            # print(pred)
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
    test_loss /= num_batches
    correct /= size
    test_l.append(test_loss)
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")



epochs = 10

for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train(train_loader,net, criterion, optimizer)
    test(test_loader, net, criterion)
print("Done!")

print(train_loss)
print(test_l)

# Plot loss
plt.figure(figsize = (10,7))
plt.plot(range(len(train_loss)), train_loss, label="train_loss")
plt.plot(range(len(test_l)), test_l, label="test_loss")
plt.title("Loss")
plt.xlabel("Epochs")
plt.legend()
plt.show()

import torch
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Prepare confusion matrix
conf_matrix = torch.zeros(10, 10)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Iterate over test dataset
# for X, y in test_loader:
#     X, y = X.to(device), y.to(device)
#     y_preds = net(X)  # Assuming model is your trained model

#     # Update confusion matrix
#     predicted_labels = torch.argmax(y_preds, dim=-1)

#     for p, l in zip(predicted_labels, y):
#       # print(p,l)
#       conf_matrix[p, l] += 1
# calculating confusion matrix
conf_matrix = torch.zeros(10,10)
for X,y in test_loader:
    X,y = X.to(device=device), y.to(device=device)
    y_preds = net(X)
    # populating the confusion matrix
    for p,l in zip(y_preds.argmax(dim=1),y):
        conf_matrix[p,l] += 1
print(f"confusion matrix:\n{conf_matrix}")
# Convert confusion matrix to NumPy array
conf_matrix = conf_matrix.numpy()

# Visualize confusion matrix
plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, fmt=".0f", cmap="Blues")
plt.xlabel("True Label")
plt.ylabel("Predicted Label")
plt.title("Confusion Matrix")
plt.show()



# Calculate overall and class-wise accuracy
print("Overall and class-wise accuracy:")
class_acc = []
for i in range(10):
    class_acc.append(conf_matrix[i, i] / conf_matrix[i].sum())

overall_acc = conf_matrix.diagonal().sum() / conf_matrix.sum()
print(f"Overall accuracy: {overall_acc}")

for i in range(10):
    print(f"Class {i} accuracy: {class_acc[i]}")

import matplotlib.pyplot as plt

# Plotting the ROC curve
plt.figure(figsize=(10, 10))
plt.title("ROC Curve --- Test Dataset")
recalls = []
precisions = []

for i in range(10):
    tp = conf_matrix[i, i]
    fn = conf_matrix[i].sum() - tp
    fp = conf_matrix[:, i].sum() - tp
    tn = conf_matrix.sum() - tp - fn - fp
    precisions.append(tp / (tp + fp))
    recalls.append(tp / (tp + fn))
    plt.plot(fp / (fp + tn), tp / (tp + fn), "o", label=f"Class {i}")

plt.legend()
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.plot([0, 1], [0, 1], color="black")
plt.show()

from torchvision.models import resnet18
# Model with pretrained weights Architecture - Resnet18resnet18
def model():
    mod_resnet = resnet18()
    mod_resnet.conv1=nn.Conv2d(3,64,kernel_size=(7,7),stride=(2,2),padding=(3,3),bias=False)
    mod_resnet.fc.in_features = 512
    
    mod_resnet.layer4[1].conv2 = nn.Conv2d(512,512,kernel_size=(3,3),stride=(1,1),padding=(1,1),bias=False)
    mod_resnet.layer4[1].bn2 = nn.BatchNorm2d(512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    mod_resnet.fc = nn.Linear(512, 10)
    
    return mod_resnet

model_resnet = model().to(device=device)
model_resnet

optimizer = torch.optim.Adam(model_resnet.parameters(), lr=0.001)
# optimizer = torch.optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
# Define the loss function
criterion = nn.CrossEntropyLoss()

epochs = 10
train_loss = []
test_l = []
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train(train_loader,model_resnet, criterion, optimizer)
    test(test_loader, model_resnet, criterion)
print("Done!")

# Plot loss
plt.figure(figsize = (10,7))
plt.plot(range(len(train_loss)), train_loss, label="train_loss")
plt.plot(range(len(test_l)), test_l, label="test_loss")
plt.title("Loss")
plt.xlabel("Epochs")
plt.legend()
plt.show()

# calculating confusion matrix
conf_matrix_resnet = torch.zeros(10,10)
for X,y in test_loader:
    X,y = X.to(device=device), y.to(device=device)
    y_preds = model_resnet(X)
    # populating the confusion matrix
    for p,l in zip(y_preds.argmax(dim=1),y):
        conf_matrix_resnet[p,l] += 1
print(f"confusion matrix:\n{conf_matrix_resnet}")

# Visualize confusion matrix
plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix_resnet, annot=True, fmt=".0f", cmap="Blues")
plt.xlabel("True Label")
plt.ylabel("Predicted Label")
plt.title("Confusion Matrix")
plt.show()

# Calculate overall and class-wise accuracy
print("Overall and class-wise accuracy:")
class_acc = []
for i in range(10):
    class_acc.append(conf_matrix_resnet[i, i] / conf_matrix_resnet[i].sum())

overall_acc = conf_matrix_resnet.diagonal().sum() / conf_matrix_resnet.sum()
print(f"Overall accuracy: {overall_acc}")

for i in range(10):
    print(f"Class {i} accuracy: {class_acc[i]}")

import matplotlib.pyplot as plt

# Plotting the ROC curve
plt.figure(figsize=(10, 10))
plt.title("ROC Curve --- Test Dataset for RESNET 18 model")
recalls = []
precisions = []

for i in range(10):
    tp = conf_matrix_resnet[i, i]
    fn = conf_matrix_resnet[i].sum() - tp
    fp = conf_matrix_resnet[:, i].sum() - tp
    tn = conf_matrix_resnet.sum() - tp - fn - fp
    precisions.append(tp / (tp + fp))
    recalls.append(tp / (tp + fn))
    plt.plot(fp / (fp + tn), tp / (tp + fn), "o", label=f"Class {i}")

plt.legend()
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.plot([0, 1], [0, 1], color="black")
plt.show()

