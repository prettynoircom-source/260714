import streamlit as st

st.set_page_config(page_title="MBTI 직업 & 포켓몬 추천", page_icon="🎮", layout="centered")

# MBTI별 추천 직업 + 어울리는 포켓몬 (이름, 도감번호, 한줄 설명)
MBTI_DATA = {
    "INTJ": {"job": "전략 컨설턴트", "pokemon": "뮤츠", "dex": 150,
             "desc": "치밀한 계획과 압도적인 능력으로 목표를 달성하는 전략가 타입이에요."},
    "INTP": {"job": "연구원", "pokemon": "메타그로스", "dex": 376,
             "desc": "논리적 사고와 분석력이 뛰어난 지적 탐구자 타입이에요."},
    "ENTJ": {"job": "경영자(CEO)", "pokemon": "리자몽", "dex": 6,
             "desc": "강한 리더십과 추진력으로 조직을 이끄는 타입이에요."},
    "ENTP": {"job": "스타트업 창업가", "pokemon": "팬텀", "dex": 94,
             "desc": "기발한 아이디어와 임기응변이 뛰어난 혁신가 타입이에요."},
    "INFJ": {"job": "심리상담가", "pokemon": "뮤", "dex": 151,
             "desc": "타인의 마음을 깊이 이해하는 신비로운 통찰가 타입이에요."},
    "INFP": {"job": "작가 · 일러스트레이터", "pokemon": "이브이", "dex": 133,
             "desc": "무한한 가능성과 감성을 지닌 순수한 몽상가 타입이에요."},
    "ENFJ": {"job": "교사 · 코치", "pokemon": "루카리오", "dex": 448,
             "desc": "타인의 성장을 돕고 이끄는 따뜻한 지도자 타입이에요."},
    "ENFP": {"job": "마케터 · PD", "pokemon": "피카츄", "dex": 25,
             "desc": "밝은 에너지와 창의력으로 사람들을 사로잡는 타입이에요."},
    "ISTJ": {"job": "회계사 · 공무원", "pokemon": "강철톤", "dex": 208,
             "desc": "원칙을 지키고 꾸준히 성실하게 임무를 완수하는 타입이에요."},
    "ISFJ": {"job": "간호사 · 사회복지사", "pokemon": "라프라스", "dex": 131,
             "desc": "따뜻한 마음으로 남을 보살피는 헌신적인 타입이에요."},
    "ESTJ": {"job": "경영관리자", "pokemon": "갸라도스", "dex": 130,
             "desc": "강력한 실행력으로 조직을 통솔하는 타입이에요."},
    "ESFJ": {"job": "이벤트 기획자 · HR", "pokemon": "폴리곤", "dex": 137,
             "desc": "사람들을 잘 챙기고 조율하는 사교적인 타입이에요."},
    "ISTP": {"job": "엔지니어 · 정비사", "pokemon": "강챙이", "dex": 212,
             "desc": "손재주가 좋고 문제 해결에 능한 실용주의자 타입이에요."},
    "ISFP": {"job": "디자이너 · 플로리스트", "pokemon": "세레비", "dex": 251,
             "desc": "섬세한 감각과 예술적 감성을 지닌 자유로운 타입이에요."},
    "ESTP": {"job": "파일럿 · 프로선수", "pokemon": "개굴닌자", "dex": 658,
             "desc": "빠른 판단력과 순발력이 뛰어난 모험가 타입이에요."},
    "ESFP": {"job": "배우 · 엔터테이너", "pokemon": "픽시", "dex": 35,
             "desc": "무대를 사랑하고 사람들을 즐겁게 하는 타입이에요."},
}

IMAGE_URL_TEMPLATE = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/"
    "sprites/pokemon/official-artwork/{dex}.png"
)

st.title("🔮 MBTI 직업 & 포켓몬 추천기")
st.write("당신의 MBTI를 선택하면 어울리는 직업과 포켓몬을 추천해드려요!")

mbti = st.selectbox("MBTI를 선택하세요", list(MBTI_DATA.keys()))

if st.button("결과 보기"):
    result = MBTI_DATA[mbti]
    st.subheader(f"✨ {mbti} 유형 결과")
    st.markdown(f"**추천 직업:** {result['job']}")
    st.markdown(f"**어울리는 포켓몬:** {result['pokemon']}")
    st.write(result["desc"])
    st.image(IMAGE_URL_TEMPLATE.format(dex=result["dex"]), caption=result["pokemon"], width=300)
