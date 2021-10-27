from keras.models import Sequential
from keras.layers import Dense,Input, Conv1D, LeakyReLU, Flatten, MaxPooling1D
from keras import optimizers


trainset = [("B0018","Battery_Data_Set"), ("B0005","Battery_Data_Set"), ("B0006","Battery_Data_Set")]
testset = [("B0007","Battery_Data_Set")]

min_soc = 0.2
max_soc = 0.6

soc_margin = 0.030 # soc 간격이 1.5%가 아니라 더 높게해야 잘나옴

model_pick = 'cnn'
input_size = 10

epochs = 500
batch_size = 4

def neural_model():
    model = Sequential()

    if model_pick == "cnn":
        model.add(Conv1D(filters = 8, kernel_size = 3,input_shape=(input_size,1))) #input_dim = 1
        model.add(LeakyReLU(alpha=0.1))
        model.add(Conv1D(filters = 32, kernel_size = 3))
        model.add(LeakyReLU(alpha=0.1))
        model.add(Conv1D(filters = 16, kernel_size = 3))
        model.add(LeakyReLU(alpha=0.1))
        model.add(Flatten())
        model.add(Dense(100))
        model.add(Dense(1))
    elif model_pick == "ann":
        model.add(Flatten())
        model.add(Dense(100))
        model.add(Dense(1))

    optimizer = optimizers.Adam()

    model.compile(loss='mae',
                    optimizer = optimizer,
                    #metrics = ["mae", "mse", 'mape', 'msle']
                    )
    #model.summary()
    return model