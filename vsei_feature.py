from method import get_Rf, get_Vsei

def get_vsei_feature(data, dataset_name, is_testset = False): # 10개 추출
    dataX = []
    dataY = []
    save_cycle = []
    for i in range(len(dataset_name)): # 데이터셋 개수별로 for문 돌기
        cycles = len(data['charge'][i])  # 사이클 수 
        cmax = data['discharge'][i][0]['Capacity']  # 쵀대정격용량
        rf = get_Rf(data['charge'][i][0])  # 배터리의 고정 내부 저항(첫 사이클에서 추출)
        for cycle, charge_data, discharge_data in zip(range(cycles),data['charge'][i],data['discharge'][i]):
            vsei_feature = get_Vsei(charge_data, rf)
            dataX.append(vsei_feature)
            dataY.append(discharge_data['Capacity']/cmax * 100)
            save_cycle.append(cycle)

    if is_testset:
        return dataX, dataY, save_cycle
        
    return dataX, dataY