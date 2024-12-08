#%%
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 데이터 생성
np.random.seed(42)

n_coils = 2000  # 생성할 코일 데이터 수
start_time = datetime(2024, 1, 1, 8, 0, 0)  # 임의의 시작 시간 설정
#%%
data = {
    "Coil_ID": [f"COIL_{i+1:04d}" for i in range(n_coils)],  # 코일 식별 ID
    "Material_Code": np.random.choice(["SPCC", "SPCD", "SPCE", "SGCC"], size=n_coils),  # 철강 소재 재질 코드
    "Thickness_mm": np.round(np.random.uniform(0.4, 2.0, n_coils), 2),  # 코일 두께 (단위: mm)
    "Width_mm": np.random.randint(800, 1601, n_coils),  # 코일 폭 (단위: mm)
    "Raw_Weight_ton": np.round(np.random.uniform(5, 25, n_coils), 2),  # 원소재 중량 (단위: 톤)
    "Heating_Zone_Temperature_C": np.random.randint(750, 851, n_coils),  # 가열대 온도 (단위: ℃)
    "Heating_Zone_Target_C": np.random.randint(780, 830, n_coils),  # 가열대 목표 온도 (단위: ℃)
    "Soaking_Zone_Temperature_C": np.random.randint(850, 951, n_coils),  # 균열대 온도 (단위: ℃)
    "Soaking_Zone_Target_C": np.random.randint(880, 940, n_coils),  # 균열대 목표 온도 (단위: ℃)
    "Cooling_Zone_Temperature_C": np.random.randint(450, 601, n_coils),  # 냉각대 온도 (단위: ℃)
    "Cooling_Zone_Target_C": np.random.randint(470, 570, n_coils),  # 냉각대 목표 온도 (단위: ℃)
    "Line_Speed_m_min": np.round(np.random.uniform(50, 200, n_coils), 1),  # 라인 속도 (단위: m/min)
    "Pot_Temperature_C": np.random.randint(450, 471, n_coils),  # Pot 온도 (단위: ℃)
    "Pot_Temperature_Target_C": np.random.randint(455, 465, n_coils),  # Pot 온도 목표 (단위: ℃)
    "Line_Speed_Target_m_min": np.round(np.random.uniform(60, 150, n_coils), 1),  # 라인 속도 목표 (단위: m/min)
    "Coating_Weight_g_m2": np.random.randint(40, 276, n_coils),  # 도금량 (단위: g/m²)
    "Coating_Target_g_m2": np.random.randint(50, 270, n_coils),  # 도금량 목표값 (단위: g/m²)
    "Cooling_Tower_Tension_kN": np.round(np.random.uniform(5, 25, n_coils), 1),  # 냉각타워 장력 (단위: kN)
    "Skin_Pass_Mill_Tension_kN": np.round(np.random.uniform(3, 15, n_coils), 1),  # Skin Pass Mill 장력 (단위: kN)
    "Skin_Pass_Mill_Roll_Force_kN": np.round(np.random.uniform(50, 200, n_coils), 1),  # Skin Pass Mill 롤 압력 (단위: kN)
    "Post_Treatment_Coating_Weight_ug_m2": np.random.randint(100, 1000, n_coils),  # 후처리 부착량 (단위: g/m²)
    "Post_Treatment_Target_ug_m2": np.random.randint(300, 700, n_coils),  # 후처리 부착량 목표값 (단위: ug/m²)
    "Oiling_Weight_mg_m2": np.random.randint(400, 4000, n_coils),  # 도유량 (단위: mg/m²)
    "Oiling_Target_mg_m2": np.random.randint(1000, 3000, n_coils),  # 도유량 목표값 (단위: g/m²)
    "Trimming_Loss_Percentage": np.round(np.random.uniform(1, 5, n_coils), 1),  # 절사량 비율 (%)
    "Defect_Info": np.random.choice(["None", "Surface Crack", "Pinholes", "Wrinkles", "Edge Waves"], size=n_coils, p=[0.8, 0.05, 0.05, 0.05, 0.05]),  # 결함 정보
}

# DataFrame 생성
df = pd.DataFrame(data)


# 상한과 하한 계산
df["Coating_Lower_Bound_g_m2"] = df["Coating_Target_g_m2"] * 0.9 # 도금량 하한
df["Post_Treatment_Upper_Bound_ug_m2"] = df["Post_Treatment_Target_ug_m2"] * 1.2 # 후처리 상한
df["Post_Treatment_Lower_Bound_ug_m2"] = df["Post_Treatment_Target_ug_m2"] * 0.8 # 후처리 하한
df["Oiling_Upper_Bound_mg_m2"] = df["Oiling_Target_mg_m2"] * 1.5  # 도유량 상한
df["Oiling_Lower_Bound_mg_m2"] = df["Oiling_Target_mg_m2"] * 0.9  # 도유량 하한
df["Heating_Zone_Upper_Bound_C"] = df["Heating_Zone_Target_C"] * 1.05
df["Heating_Zone_Lower_Bound_C"] = df["Heating_Zone_Target_C"] * 0.95
df["Soaking_Zone_Upper_Bound_C"] = df["Soaking_Zone_Target_C"] * 1.05
df["Soaking_Zone_Lower_Bound_C"] = df["Soaking_Zone_Target_C"] * 0.95
df["Cooling_Zone_Upper_Bound_C"] = df["Cooling_Zone_Target_C"] * 1.05
df["Cooling_Zone_Lower_Bound_C"] = df["Cooling_Zone_Target_C"] * 0.95
df["Pot_Temperature_Upper_Bound_C"] = df["Pot_Temperature_Target_C"] * 1.05
df["Pot_Temperature_Lower_Bound_C"] = df["Pot_Temperature_Target_C"] * 0.95

# 생성 시간과 완료 시간 계산
creation_times = [start_time]  # 첫 번째 코일의 생성 시간
completion_times = []

# 첫 번째 코일의 완료 시간 계산
completion_time = creation_times[0] + timedelta(minutes=10 + df.loc[0, "Thickness_mm"] * 5 + df.loc[0, "Width_mm"] / 400)
completion_times.append(completion_time)

# 이후 코일의 생성/완료 시간 계산
for i in range(1, n_coils):
    creation_time = completion_times[i - 1]  # 이전 코일의 완료 시간이 현재 코일의 생성 시간
    creation_times.append(creation_time)
    completion_time = creation_time + timedelta(minutes=10 + df.loc[i, "Thickness_mm"] * 5 + df.loc[i, "Width_mm"] / 400)
    completion_times.append(completion_time)

# DataFrame에 추가
df["Creation_Time"] = creation_times
df["Completion_Time"] = completion_times[:n_coils]  # 각 코일의 완료 시간

# 제품 중량 계산: 절사량 반영 및 도금량 추가
df["Measured_Finished_Weight_ton"] = (
    df["Raw_Weight_ton"] * (1 - df["Trimming_Loss_Percentage"] / 100)
    + df["Coating_Weight_g_m2"] * 1e-6 * df["Width_mm"] * 1e-3
)

print(df)

output_file = 'output.csv'
df.to_csv(output_file, index=False, encoding='utf-8')

# %%
