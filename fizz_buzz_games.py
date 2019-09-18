#-*-coding:utf-8-*-
import torch
import torch.nn as nn
def fizz_buzz_encode(i):
    if i % 15 == 0:
        return 3
    elif i % 5 == 0:
        return 2
    elif i % 3 == 0:
        return 1
    else:
        return 0
def fizz_buzz_decode(i, prediction):
    return [str(i), 'fizz', 'buzz', 'fizz_buzz'][prediction]

def binary_encode(i, num_digits):
    return [i >> d & 1for d in range(num_digits)][::-1]

NUM_DIGITS = 10
trX = torch.Tensor([binary_encode(i, NUM_DIGITS) for i in range(101, 2**NUM_DIGITS)])
trY = torch.LongTensor([fizz_buzz_encode(i) for i in range(101, 2 ** NUM_DIGITS)])
teX = torch.Tensor([binary_encode(i, NUM_DIGITS) for i in range(1, 101)])
teY = torch.LongTensor([fizz_buzz_encode(i) for i in range(1, 101)])

NUM_HIDDEN = 100
model = nn.Sequential(
    nn.Linear(NUM_DIGITS, NUM_HIDDEN),
    nn.ReLU(),
    nn.Linear(NUM_HIDDEN, 4)
)

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
NUM_EPOCHS = 10000
BATCH_SIZE = 128
for epoch in range(NUM_EPOCHS):
    for start in range(0, trX.size(0), BATCH_SIZE):
        end = start + BATCH_SIZE
        batch_x = trX[start: end]
        batch_y = trY[start: end]
        y = model(batch_x)
        loss = loss_fn(y, batch_y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(loss.item())
for start in range(0, teX.size(0), BATCH_SIZE):
    end = start + BATCH_SIZE
    with torch.no_grad():
        predictions = model(teX)
    predictions = zip(range(1, 101), predictions.max(1)[1].data.numpy().tolist())
    for i, x in predictions:
        print(fizz_buzz_decode(i, x))
