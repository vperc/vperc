import tensorflow as tf
import numpy as np #Numpy 是一个最优的数学处理函数库
import matplotlib.pyplot as plt
import math
from tensorflow.keras import layers
model_1 = tf.keras.Sequential()

#sin函数产生一系列的标准化数据
SAMPLES = 1000
np.random.seed(1337)
x_values = np.random.uniform(low=0,high=2*math.pi,size=SAMPLES) # 用来产生特定范围内的一系列随机数。
np.random.shuffle(x_values)#当原始数据产生之后，我们要接着做的事情，便是数据清洗。我们要确保数据以真正的随机的方式反馈,radom.shuffle()提供了方法
y_values = np.sin(x_values)
#Add a small random number to each y value
y_values += 0.1* np.random.randn(*y_values.shape)

plt.plot(x_values,y_values,'b.')
plt.show()

model_1.add(layers.Dense(16,activation='relu',input_shape=(1,)))
model_1.add(layers.Dense(1))

model_1.compile(optimizer='rmsprop',loss='mse',metrics=['mae'])
model_1.summary()

#分成训练集和测试集
TRAIN_SPLIT = int(0.6 * SAMPLES)
TEST_SPLIT = int(0.2* SAMPLES + TRAIN_SPLIT)
#整个数据集包括三个部分，训练集，测试集，验证集。示例中用了 60% 的数据当训练集，20% 的数据当测试集，20% 的数据当验证集。这个比例不是恒定的，可以按需求调整。

x_train,x_test,x_validate = np.split(x_values,[TRAIN_SPLIT,TEST_SPLIT])
y_train,y_test,y_validate = np.split(y_values,[TRAIN_SPLIT,TEST_SPLIT])

assert (x_train.size + x_validate.size + x_test.size) == SAMPLES

# Plot our data
plt.plot(x_train,y_train,'b.',label="Train")
plt.plot(x_test,y_test,'r.',label="Test")
plt.plot(x_validate,y_validate,'y.',label="Validate")
plt.legend() #最后再把数据以二维坐标的方式画在图片上。
plt.show()

#训练模型
history_1 =model_1.fit(x_train,y_train,epochs=1000,batch_size=16,validation_data=(x_validate,y_validate))
#训练结果
loss = history_1.history['loss']
val_loss = history_1.history['val_loss']

epochs = range(1,len(loss) +1)

plt.plot(epochs,loss,'g.',label='Training loss')
plt.plot(epochs,val_loss,'b',label='Validation loss')
plt.title('Teaining and Validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
#该图显示了每个时期的损失（或模型的预测与实际数据之间的差异）。有几种计算损失的方法，我们使用的方法是均方误差。对于训练和验证数据有明显的损失值。

SKIP = 50

plt.plot(epochs[SKIP:],loss[SKIP:],'g.',label='Training loss')
plt.plot(epochs[SKIP:],val_loss[SKIP:],'b.',label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('loss')
plt.legend()
plt.show()
#从图中可以分析出，大概 epochs 到了 600 左右，训练开始趋于稳定。意味着我们的 epochs 应该不需要超过 600。

plt.clf()

mae = history_1.history['mae']
val_mae = history_1.history['val_mae']

plt.plot(epochs[SKIP:],mae[SKIP:],'g.',label='Training MAE')
plt.plot(epochs[SKIP:],val_mae[SKIP:],'b.',label='Validation MAE')
plt.title('Training and validation mean absolute error')
plt.xlabel('Epochs')
plt.ylabel('MAE')
plt.legend()
plt.show()
#从平均绝对误差图可以看到，训练数据显示出的错误始终比验证数据低，这意味着网络可能存在过拟合 (Overfit)，或者过分地学习了训练数据，从而无法对新数据做出有效的预测。

predictions = model_1.predict(x_train)

plt.clf()
plt.title('Training data predicted vs actual values')
plt.plot(x_test,y_test,'b.',label = 'Actual')
plt.plot(x_train,predictions,'r',label='Predicted')
plt.legend()
plt.show()

#优化模型
#优化的关键是增加全连接层，这一层包含了16个神经元
model_2 = tf.kreas.Squential()

model_2.add(layers.Dense(16,activation='relu',input_shape=(1,)))

model_2.add(layers.Dense(16,activation='relu'))

model_2.add(layers.Dense(1))

model_2.compile(optimizer = 'rmsprop',loss='mse',metrics =['mae'])

history_2 = model_2.fit(x_train,y_train,epochs=600,batch_size=16,validate_data=(x_validate,y_validate))