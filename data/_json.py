import os
import json
import pandas as pd
from datasets import load_dataset, Features, Value

# 현재 파이썬 파일이 위치한 디렉토리 경로
current_dir = os.path.dirname(os.path.abspath(__file__))


# 허깅페이스 데이터셋 이름 리스트
dataset_names = [
    'crimsonjoo/KBN_ex',
    # 여기에 다른 데이터셋 이름을 추가하세요
]

# dataset_info.json 파일 경로
dataset_info_path = os.path.join(current_dir, 'dataset_info.json')

# 기존 dataset_info.json 파일 로드 또는 빈 딕셔너리 생성
if os.path.exists(dataset_info_path):
    with open(dataset_info_path, 'r', encoding='utf-8-sig') as f:
        dataset_info = json.load(f)
else:
    dataset_info = {}

# 허깅페이스 데이터셋의 열 특징 정의
features = Features({
    'system': Value('string'),
    'instruction': Value('string'),
    'input': Value('string'),
    'chosen': Value('string'),
    'rejected': Value('string'),
    'history': Value('string')
})

# 데이터셋을 순차적으로 처리
for dataset_name in dataset_names:
    # 데이터셋 로드
    dataset = load_dataset(dataset_name, split='train', features=features)
    df = pd.DataFrame(dataset)

    # 데이터프레임의 모든 빈 값을 빈 문자열로 대체
    df = df.fillna('')

    # 원하는 형식으로 데이터 프레임 변환
    json_data = []
    for _, row in df.iterrows():
        json_data.append({
            "system": row['system'],
            "instruction": row['instruction'],
            "input": row['input'],
            "chosen": row['chosen'],
            "rejected": row['rejected'],
            "history": row['history']
        })


    df_name = dataset_name.split('/')[1]
    # JSON 파일로 저장
    dataset_filename = f"{df_name}.json"
    dataset_filepath = os.path.join(current_dir, dataset_filename)
    
    with open(dataset_filepath, 'w', encoding='utf-8-sig') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)

    # dataset_info.json 업데이트
    dataset_info[df_name] = {
        "file_name": dataset_filename,
        "ranking": True,
        "columns": {
            "system": "system",
            "prompt": "instruction",
            "query": "input",
            "chosen": "chosen",
            "rejected": "rejected",
            "history": "history"
        }
    }

# 변경된 dataset_info.json 저장
with open(dataset_info_path, 'w', encoding='utf-8-sig') as f:
    json.dump(dataset_info, f, ensure_ascii=False, indent=4)

print("요청하신 KBN 데이터셋이 성공적으로 json 처리되었습니다.")
