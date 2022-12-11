# Term-Project
컴퓨터공학과 21101190 서보성 2학년 2학기 오픈소스소프트웨어 강의의 최종 과제입니다.

# pygame을 활용한 작성 및 참고 코드
 게임 개발을 주제로 선정하여 파이썬으로 게임을 만들때 pygame을 사용하여 만들수 있다는 것을 알게되어 pygame을 활용하여 작성하였고, pygame의 필요한 기능은 인터넷에 작성된 사례를 보거나 따로 사용법을 검색하여 알아낸 후 작성하였습니다.
 특히 가장 많이 참고한 곳(1) : https://github.com/ElenaLim/Pygame/blob/main/minigame.py
 특히 가장 많이 참고한 곳(2) : https://blog.naver.com/scyan2011/222175919461
제가 작성한 코드가 여기 작성된 코드들과 조금 유사한 부분이 있을텐데, 방법은 전혀 다른 게임이지만, 화면 구성 및 플레이어, 적 생성에 많은 참고를 하였습니다
두번째 링크의 경우, 코드 작성에 대한 글이 여러개 있어 처음부터 하나하나 참고하면서 제게 필요한 기능만을 작성하는데 참고하였습니다.

# 게임 방법
 시작화면에서 Esc키를 제외한 아무 키나 누르면 게임이 시작되며, Esc 키를 누르면 그 자리에서 게임이 종료되고 창이 닫힙니다.
 아무 키나 누르고 게임을 시작하면 플레이어와 적 물고기들이 등장하며, 플레이어와 레벨이 갖거나 더 낮은 레벨의 물고기를 먹으면 점수를 획득하며, 높은 레벨의 물고기와 닿을 경우 목숨을 하나 잃게 됩니다. 적 물고기들 끼리도 서로를 잡아먹을 수 있지만, 이는 서로 레벨이 다를 경우에만 일어납니다.
 총 5단계로 진행되며, 레벨이 진행될수록 더 높은 레벨의 물고기가 등장합니다.
 
# 게임 종료
 플레이어의 목숨이 0이 되면 게임 오버가 되며, 5단계까지 클리어할 경우 게임 클리어가 됩니다.
 
# 게임에 사용된 이미지
배경 출처 : https://flickr.com/photos/td246/6405111503/
물고기 그림 : 본인이 3D 그림판을 이용하여 그렸습니다.

# 플레이어 물고기(해당 사진은 레벨 5 기준)
![Level5playerFish](https://user-images.githubusercontent.com/112685218/206908247-ee2823dd-b50e-4096-b79f-19382fd236c9.png)

# 레벨1 물고기
![Level1Fish](https://user-images.githubusercontent.com/112685218/206908190-cccdcd97-7ec5-4a9d-a216-c265cb9db214.png)

# 레벨2 물고기
![Level2Fish](https://user-images.githubusercontent.com/112685218/206908198-95372861-1096-4b97-b11b-89f48c91ad90.png)

# 레벨3 물고기
![Level3Fish](https://user-images.githubusercontent.com/112685218/206908267-fb08dea6-85a8-4d0e-89c1-976e8ae828fa.png)

# 레벨4 물고기
![Level4Fish](https://user-images.githubusercontent.com/112685218/206908284-2c514d6e-144e-4134-bb45-32aa716a96f8.png)

# 레벨5 물고기
![Level5Fish](https://user-images.githubusercontent.com/112685218/206908299-d7304673-d414-41d2-883b-1f1c2614cd11.png)

# 게임 스크린샷
(테스트용 코드(목표 점수가 실제보다 낮음) 상태에서 캡처한점 참고 부탁드립니다.)
![화면 캡처 2022-12-11 223604](https://user-images.githubusercontent.com/112685218/206908355-522f240f-ac17-4033-9bf9-195e3c586de9.png)
![화면 캡처 2022-12-11 223627](https://user-images.githubusercontent.com/112685218/206908357-cf5dd52a-471a-45c5-ba7f-fa1f3b8e6bb2.png)
