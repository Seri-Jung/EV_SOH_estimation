import matplotlib.pyplot as plt
from config import *
from method import *
from dataset import *
from vsei_feature import get_vsei_feature
import tensorflow as tf
from sklearn.metrics import accuracy_score
from numpy import argmax
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt
import pandas as pd


    
def mean_squared_error(y,t):
    return 0.5 * np.sum((y-t)**2)


if __name__ =="__main__":

    # train dataset 생성
    train_data = {}
    train_data['charge'] = []
    train_data['discharge'] = []

    for td in trainset:
        charge_data, discharge_data = get_matData(td)  # 4개 데이터셋
        train_data['charge'].append(charge_data)
        train_data['discharge'].append(discharge_data)

    # test dataset 생성
    test_data = {}
    test_data['charge'] = []
    test_data['discharge'] = []
    for td in testset:
        charge_data, discharge_data = get_matData(td) 
        test_data['charge'].append(charge_data)
        test_data['discharge'].append(discharge_data)

    '''
    ex ) train_data['charge'][0][120]['Voltage_measured'] // state = charge ; 0 = dataset ; 120 = cycle ; Voltage_measured = feature ;
    charging feature is Voltage_measured ; Current_measured ; Temperature_measured ; Current_charge ; Voltage_charge ; Time ;
    discharging feature is Voltage_measured ; Current_measured ; Temperature_measured ; Current_load ; Voltage_load ; Time ; Capacity ;
    '''
    
    trainX, trainY = get_vsei_feature(train_data,trainset)
    testX, testY, testCycles = get_vsei_feature(test_data,testset, is_testset= True)

    trainX = np.array(trainX)
    trainY = np.array(trainY)
    testX = np.array(testX); testY = np.array(testY)
    
    trainX = np.expand_dims(trainX,axis=2)
    testX = np.expand_dims(testX,axis=2)

    # print(trainX)
    print('\ntrainX shape:', trainX.shape)

    print("\n---\n")
    # print(trainY)
    print('\ntrainX shape:', trainY.shape)

    # 모델 CNN
    print("CNN\n")
    model1 = neural_model("cnn")

    history1 = model1.fit(trainX,trainY, epochs=epochs, batch_size= batch_size, validation_data = (testX,testY))

    predict_result1 = model1.predict(testX)
    #loss, mae, mse = model.evaluate(testX, testY)
    testCycles = np.array(testCycles)

    Xpred1 = predict_result1.argmax(axis=-1)
    Ytest= testY.argmax(axis=-1)

    # # 모델 LSTM
    # print("LSTM\n")
    # model2 = neural_model('LSTM')
    # history2 = model2.fit(trainX,trainY, epochs=epochs, batch_size= batch_size, validation_data = (testX,testY))

    # predict_result2 = model2.predict(testX)
    # #loss, mae, mse = model.evaluate(testX, testY)
    # testCycles = np.array(testCycles)

    # Xpred2 = predict_result2.argmax(axis=-1)
    # Ytest= testY.argmax(axis=-1)
    

    # # # 정확도
    # # print("정확도: ", accuracy_score(Xpred, Ytest))

    # # 모델 비교 그래프
    # plt.figure()
    # plt.plot(testCycles,testY, label = "original")
    # plt.plot(testCycles,predict_result1, label = "Convolution Neural Networks")
    # plt.plot(testCycles,predict_result2, label = "LSTM")
    # plt.ylabel('State Of Health(SOH)')
    # plt.xlabel('Cycle')
    # plt.legend()
    # plt.savefig("./result.jpg")
    # plt.show()

    # # 손실도
    # plt.figure()
    # plt.plot(history1.history['loss'][20:], label = 'original_loss')  # 매 epoch 마다의 훈련 손실 값 
    # plt.plot(history1.history['val_loss'][20:], label = 'validation_loss') # 매 epoch 마다의 검증 손실 값 
    # plt.title('Convolution Neural Networks loss')
    # plt.ylabel('loss')
    # plt.xlabel('epoch')
    # plt.legend()
    # plt.savefig("./result_CNN_loss.jpg")
    # plt.show()

    # plt.figure()
    # plt.plot(history2.history['loss'][20:], label = 'original_loss')  # 매 epoch 마다의 훈련 손실 값 
    # plt.plot(history2.history['val_loss'][20:], label = 'validation_loss') # 매 epoch 마다의 검증 손실 값 
    # plt.title('LSTM loss')
    # plt.ylabel('loss')
    # plt.xlabel('epoch')
    # plt.legend()
    # plt.savefig("./result_LSTM_loss.jpg")
    # plt.show()

    # rmse1 = sqrt(mean_squared_error(testY, predict_result1))
    # print("CNN RMSE: %s" %rmse1)

    # rmse2 = sqrt(mean_squared_error(testY, predict_result2))
    # print(" LSTM RMSE: %s" %rmse2)