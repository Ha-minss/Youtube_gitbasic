# === 단축키 연습용 파이썬 스크립트 ===

# 1. 라이브러리 임포트 (Ctrl + / 로 주석 연습)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 2. 샘플 데이터 생성 함수 정의
def create_sample_data(num_rows=100):
    """
    (연습용: 함수 뼈대를 만듭니다)
    이 부분은 여러 줄 주석(Docstring)입니다.
    """
    print(f"총 {num_rows}개의 랜덤 샘플 데이터를 생성합니다...")
    # 딕셔너리 형태로 데이터 구성
    
    data = {
        'Student_ID': [f'S{1001 + i}' for i in range(num_rows)],
        'Math_Score': np.random.randint(40, 101, size=num_rows),
        'English_Score': np.random.randint(30, 101, size=num_rows),
        'Study_Hours': np.random.uniform(1.0, 10.0, size=num_rows).round(1)
    }
    
    # 데이터프레임으로 변환
    df = pd.DataFrame(data)
    return df

# 3. 데이터 처리 및 분석 함수 정의
def analyze_scores(dataframe):
    """
    학생 데이터를 분석하고 새로운 컬럼을 추가합니다.
    """
    
    # 3-1. 총점 및 평균 계산
    dataframe['Total_Score'] = dataframe['Math_Score'] + dataframe['English_Score']
    dataframe['Average_Score'] = dataframe['Total_Score'] / 2
    
    # 3-2. 합격/불합격 (Pass/Fail) 처리 (조건문 연습)
    # 평균 60점 이상, 모든 과목 40점 이상일 때 'Pass'
    pass_condition = (dataframe['Average_Score'] >= 60) & \
                     (dataframe['Math_Score'] > 40) & \
                     (dataframe['English_Score'] > 40)
    
    dataframe['Result'] = np.where(pass_condition, 'Pass', 'Fail')
    
    print("\n[데이터 처리 완료]")
    return dataframe

# 4. 메인(Main) 실행 블록: 여기가 스크립트의 시작점입니다.
if __name__ == "__main__":
    
    print("--- 데이터 분석 스크립트 시작 ---")
    
    # 1단계: 데이터 생성
    student_data = create_sample_data(num_rows=50)
    
    # 2단계: 데이터 분석
    analyzed_data = analyze_scores(student_data)
    
    # 3단계: 결과 출력 (반복문 연습)
    print("\n[결과 리포트 (Fail 학생만 출력)]")
    fail_students = analyzed_data[analyzed_data['Result'] == 'Fail']
    
    for index, row in fail_students.iterrows():
        print(f"ID: {row['Student_ID']}, 평균: {row['Average_Score']}, 결과: {row['Result']}")
        
    print(f"\n--- 총 {len(fail_students)}명의 학생이 'Fail' ---")
    # print("--- 스크립트 종료 ---")


print("나는 지금 깃허브 두번쨰수정중인레후44")
print("나는 세번쨰수정이야")
1+1 = 3
444 + 333 = 4444
print("이건브렌치전용인레후")
print("이건 진짜 DEVELOP 버전")
