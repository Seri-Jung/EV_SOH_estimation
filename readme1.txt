데이터셋 구성:
  B0005.mat Data for Battery #5
  B0006.mat Data for Battery #6
  B0007.mat Data for Battery #7
  B0018.mat Data for Battery #18

설명:
  - 4개의 리튬 이온 배터리 세트(5, 6, 7, 18)가 있음.

  - 실온에서 3개의 다른 충방전 및 임피던스 실험을 통해 저장된 데이터

  - 충전 조건: 
    - 약 2-3초 간격으로 저장
    - 배터리 전압이 4.2V에 도달할 때까지 1.5A에서 정전류(CC) 모드로 충전한 다음, 충전 전류가 20mA로 떨어질 때까지 정전압(CV) 모드로 계속 충전함.

  - 방전 조건: 
    - 약 10초 간격으로 저장
    - 배터리 5, 6, 7, 18에 대해 배터리 전압이 각각 2.7V, 2.5V, 2.2V 및 2.5V로 떨어질 때까지 2A 정전류(CC) 레벨에서 방전 수행.

  - 임피던스 측정: 0.1Hz에서 5kHz까지 *전기화학적 임피던스 분광법(EIS) 주파수 스위프를 통해 수행됨.
    * 전기화학적 임피던스 분광법(EIS)에 관한 설명: http://www.wizmac.com/2015/lecture/board01_view.htm?No=172&Sub_No=8

  - 배터리 수명 종료(EOL) 기준에 도달했을 때 중단되었으며, 이 는 정격용량이 30% 감소(2Ahr에서 1.4Ahr로) 되었을 때 중단됨. 
  - 이 데이터셋은 남은 충전량(주어진 방전 주기 동안)과 잔여 유효 수명(RUL)을 예측하는데 사용할 수 있음. 
               
 
데이터셋 구조:
- cycle: 충전, 방전 및 임피던스 작업을 포함하는 최상위 구조 배열

   -- type: 작동 유형, 충전, 방전, 임피던스일 수 있음

   -- ambient_temperature: 주변온도(섭씨)

  -- time: 주기 시작 날짜 및 시간(MATLAB 날짜 벡터 형식)

  -- data: 측정값을 포함하는 데이터 구조
         - 충전 데이터 필드:
            Voltage_measured: Battery terminal voltage (Volts)
            Current_measured: Battery output current (Amps)
            Temperature_measured: Battery temperature (degree C)
            Current_charge: Current measured at charger (Amps)
            Voltage_charge: Voltage measured at charger (Volts)
            Time: Time vector for the cycle (secs)


          - 방전 데이터 필드:
            Voltage_measured: Battery terminal voltage (Volts)
            Current_measured: Battery output current (Amps)
            Temperature_measured: Battery temperature (degree C)
            Current_charge: Current measured at load (Amps)
            Voltage_charge: Voltage measured at load (Volts)
            Time: Time vector for the cycle (secs)
            Capacity: Battery capacity (Ahr) for discharge till 2.7V 
 
          - 임피던스 데이터 필드:
            Sense_current: Current in sense branch (Amps)
            Battery_current: Current in battery branch (Amps)
            Current_ratio: Ratio of the above currents
            Battery_impedance: Battery impedance (Ohms) computed from raw data
            Rectified_impedance: Calibrated and smoothed battery impedance (Ohms)
            Re: Estimated electrolyte resistance (Ohms)
            Rct: Estimated charge transfer resistance (Ohms)
