# SOH 추청방법 구현

 - 삼성 네이처 논문 참고: [An Incremental Voltage Difference Basedd Technique for Online State of Health Estimation of Li-ion Batteries](https://www.nature.com/articles/s41598-020-66424-9.pdf)
 - 사용한 데이터: NASA battery dataset(public) 
   - [데이터셋에 대한 설명(영문)](https://github.com/Seri-Jung/EV_vsei/blob/main/readme.txt)
   - [데이터셋에 대한 설명(국문)](https://github.com/Seri-Jung/EV_vsei/blob/main/readme1.txt)

### ❤ 설명
삼성 네이처에 실린 An Incremental Voltage Difference Basedd Technique for Online State of Health Estimation of Li-ion Batteries 논문의 V_sei를 활용한 SOC와 SOH추정 방법을 익히고 이를 나사 데이터셋에 적용시켜보기
- 논문 분석 자료: [삼성논문분석자료.pptx](https://github.com/Seri-Jung/EV_vsei/files/8314149/default.pptx)

#### NASA 데이터 SOH 추정 모델을 SK 렌터카에 적용시키기 어려운 이유
- 데이터가 10초 주기임(정상/비정상 경계를 나누는 데이터가 필요함)
  - SK 데이터를 0.1초 주기의 시간간격으로 생성한다면 학습모델을 동작할 수는 있음.
- 이상 데이터를 찾아 볼 수 없음 (정상&비정상을 나누는 데이터 X) 즉, 매우 좋은 상태의 데이터만 존재
- 데이터 구성의 단순함
- NASA 데이터는 충전조건이 일정하지만, SK 데이터는 충전 패턴이 일정하지 않음
- NASA의 충전은 일정(linear)하고 방전은 랜덤해서 SOH를 추정할 수 있지만, SK 데이터에 적용한다면 SOH 100%만 나올 것.
- SOH 결과값은 100% 만 나옴 (신품으로만 구성)
- 노후 데이터가 존재하지 않음
