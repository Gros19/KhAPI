import shutil
import os
from pathlib import Path

#프로젝트 경로 반환
def get_project_root() -> Path:
    return Path(__file__).parent.parent.parent

print(get_project_root())


#디렉토리 이하까지 삭제하는 함수
def remove_folder(path):
    try:
        if os.path.exists(path):
            shutil.rmtree(path)
            print(path," 삭제 성공")
        else:
             raise Exception("폴더를 찾을 수 없습니다.")
    except Exception as e:
        print("예외 발생.", e)
        
