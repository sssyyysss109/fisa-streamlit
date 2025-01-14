import streamlit as st

#text를 입력하는 검색창
#ani_list에 있는 글자가 일부라도 들어가면 img_list에 있는 그림이 출력되는 검색창 만들기
ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

ans=st.text_input("검색하실 애니메이션을 입력해주세요.")

for ani in ani_list:
    if ans in ani:
        img_idx=ani_list.index(ans)

if ans != '': #초기상태
    st.image(img_list[img_idx])

