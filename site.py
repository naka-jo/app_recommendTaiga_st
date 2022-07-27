import streamlit as st

if 'kimi' not in st.session_state:
    st.session_state.kimi = 0
if 'dono' not in st.session_state:
    st.session_state.dono = 0
if 'kiyomori' not in st.session_state:
    st.session_state.kiyomori = 0
if 'maru' not in st.session_state:
    st.session_state.maru = 0
if 'ie' not in st.session_state:
    st.session_state.ie = 0
if 'tora' not in st.session_state:
    st.session_state.tora = 0
if 'kirinn' not in st.session_state:
    st.session_state.kirinn = 0
if 'gumi' not in st.session_state:
    st.session_state.gumi = 0
if 'ryoma' not in st.session_state:
    st.session_state.ryoma = 0
if 'tuke' not in st.session_state:
    st.session_state.tuke = 0
if 'idatenn' not in st.session_state:
    st.session_state.idatenn = 0

def era_choice(a):
    if answer_1_2 == 1:
        st.session_state.kimi += a
        st.text('あなたの回答:平安時代')
    elif answer_1_2 == 2:
        st.session_state.dono += a
        st.session_state.kiyomori += a
        st.text('あなたの回答:平安末期〜鎌倉時代')
    elif answer_1_2 == 3:
        st.session_state.maru += a
        st.session_state.ie += a
        st.session_state.tora += a
        st.session_state.kirinn += a
        st.text('あなたの回答:戦国時代')
    elif answer_1_2 == 4:
        st.session_state.gumi += a
        st.session_state.ryoma += a
        st.session_state.tuke += a
        st.text('あなたの回答:幕末')
    elif answer_1_2 == 5:
        st.session_state.idatenn += a
        st.text('あなたの回答:近現代')


def acter1_list(a):
    global answer_2_1
    answer_2_1 = st.selectbox(
        '''
        選択肢:吉高由里子:1,   小栗旬:2,        中川大志:3,    小池栄子:4,
               山本耕史:5.     大泉洋:6,        堺雅人:7,      草刈正雄:8,
               長澤まさみ:9,   松山ケンイチ:10, 長谷川博己:11, 川口春奈:12,
               染谷将太:13,    松本潤:14,       柴咲コウ:15,   高橋一生:16,
               尾上松也:17,    柳楽優弥:18,     吉沢亮:19,     草なぎ剛:20,
               香取慎吾:21,    福山雅治:22,     役所広司:23,   阿部サダヲ:24,
               中村勘九郎:25   いない:26
        ''',
        (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26))


def acter2_list(a):
    global answer_2_2
    answer_2_2 = st.selectbox(
        '''
        選択肢:吉高由里子:1,   小栗旬:2,        中川大志:3,    小池栄子:4,
               山本耕史:5.     大泉洋:6,        堺雅人:7,      草刈正雄:8,
               長澤まさみ:9,   松山ケンイチ:10, 長谷川博己:11, 川口春奈:12,
               染谷将太:13,    松本潤:14,       柴咲コウ:15,   高橋一生:16,
               尾上松也:17,    柳楽優弥:18,     吉沢亮:19,     草なぎ剛:20,
               香取慎吾:21,    福山雅治:22,     役所広司:23,   阿部サダヲ:24,
               中村勘九郎:25,  いない:26
        ''',
        (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26))

def acter3_list(a):
    global answer_2_3
    answer_2_3 = st.selectbox(
        '''
        選択肢:吉高由里子:1,   小栗旬:2,        中川大志:3,    小池栄子:4,
               山本耕史:5.     大泉洋:6,        堺雅人:7,      草刈正雄:8,
               長澤まさみ:9,   松山ケンイチ:10, 長谷川博己:11, 川口春奈:12,
               染谷将太:13,    松本潤:14,       柴咲コウ:15,   高橋一生:16,
               尾上松也:17,    柳楽優弥:18,     吉沢亮:19,     草なぎ剛:20,
               香取慎吾:21,    福山雅治:22,     役所広司:23,   阿部サダヲ:24,
               中村勘九郎:25,  いない:26
        ''',
        (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26))



acter = ['吉高由里子', '小栗旬', '中川大志', '小池栄子',
         '山本耕史', '大泉洋', '堺雅人', '草刈正雄',
         '長澤まさみ', '松山ケンイチ', '長谷川博己', '川口春奈',
         '染谷将太', '松本潤', '柴咲コウ', '高橋一生',
         '尾上松也', '柳楽優弥', '吉沢亮', '草なぎ剛',
         '香取慎吾', '福山雅治', '役所広司', '阿部サダヲ',
         '中村勘九郎', 'いない']
def acter1_choice(d):
    global answer_2_1
    if 1 <= answer_2_1 <= 1:
        st.session_state.kimi += d
    elif 2 <= answer_2_1 <= 6:
        st.session_state.dono += d
    elif 6 <= answer_2_1 <= 9:
        st.session_state.maru += d
    elif 10 <= answer_2_1 <= 10:
        st.session_state.kiyomori += d
    elif 11 <= answer_2_1 <= 13:
        st.session_state.kirinn += d
    elif 14 <= answer_2_1 <= 14:
        st.session_state.ie += d
    elif 15 <= answer_2_1 <= 18:
        st.session_state.tora += d
    elif 19 <= answer_2_1 <= 20:
        st.session_state.tuke += d
    elif 21 <= answer_2_1 <= 21:
        st.session_state.gumi += d
    elif 22 <= answer_2_1 <= 22:
        st.session_state.ryoma += d
    elif 23 <= answer_2_1 <= 25:
        st.session_state.idatenn += d
    elif 5 <= answer_2_1 <= 5:
        st.session_state.gumi += d

    st.text('あなたの回答:' + acter[answer_2_1-1])

def acter2_choice(d):
    global answer_2_2
    if 1 <= answer_2_2 <= 1:
        st.session_state.kimi += d
    elif 2 <= answer_2_2 <= 6:
        st.session_state.dono += d
    elif 6 <= answer_2_2 <= 9:
        st.session_state.maru += d
    elif 10 <= answer_2_2 <= 10:
        st.session_state.kiyomori += d
    elif 11 <= answer_2_2 <= 13:
        st.session_state.kirinn += d
    elif 14 <= answer_2_2 <= 14:
        st.session_state.ie += d
    elif 15 <= answer_2_2 <= 18:
        st.session_state.tora += d
    elif 19 <= answer_2_2 <= 20:
        st.session_state.tuke += d
    elif 21 <= answer_2_2 <= 21:
        st.session_state.gumi += d
    elif 22 <= answer_2_2 <= 22:
        st.session_state.ryoma += d
    elif 23 <= answer_2_2 <= 25:
        st.session_state.idatenn += d
    elif 5 <= answer_2_2 <= 5:
        st.session_state.gumi += d

    st.text('あなたの回答:' + acter[answer_2_2-1])

def acter3_choice(d):
    global answer_2_3
    if 1 <= answer_2_3 <= 1:
        st.session_state.kimi += d
    elif 2 <= answer_2_3 <= 6:
        st.session_state.dono += d
    elif 6 <= answer_2_3 <= 9:
        st.session_state.maru += d
    elif 10 <= answer_2_3 <= 10:
        st.session_state.kiyomori += d
    elif 11 <= answer_2_3 <= 13:
        st.session_state.kirinn += d
    elif 14 <= answer_2_3 <= 14:
        st.session_state.ie += d
    elif 15 <= answer_2_3 <= 18:
        st.session_state.tora += d
    elif 19 <= answer_2_3 <= 20:
        st.session_state.tuke += d
    elif 21 <= answer_2_3 <= 21:
        st.session_state.gumi += d
    elif 22 <= answer_2_3 <= 22:
        st.session_state.ryoma += d
    elif 23 <= answer_2_3 <= 25:
        st.session_state.idatenn += d
    elif 5 <= answer_2_3 <= 5:
        st.session_state.gumi += d

    st.text('あなたの回答:' + acter[answer_2_3-1])


st.title("オススメ大河ドラマ診断")
st.caption("質問に答えるだけでオススメの大河ドラマが見つかります！")

with st.form(key='like_form'):
    st.text('質問1')
    answer_1 = st.radio(
        '''
        時代にこだわりますか？

        選択肢:強くこだわる:1, ややこだわる:2, こだわらない:3 →質問2へ
        ''',
        (1, 2, 3))
    submit_btn = st.form_submit_button('回答')
    if submit_btn:
        if answer_1 == 1:
            st.text('あなたの回答:強くこだわる')
        elif answer_1 == 2:
            st.text('あなたの回答:ややこだわる')
        elif answer_1 == 3:
            st.text('あなたの回答:こだわらない')

with st.form(key='era_form'):
    st.text('質問1_2')
    answer_1_2 = st.selectbox(
        '''
        強くこだわる、ややこだわると回答された方
        好きな時代を選んでください
        選択肢:平安:1, 平安末期〜鎌倉時代:2,
        戦国時代:3, 幕末:4, 近現代:5
        ''',
        (1,2,3,4,5))
    era_btn = st.form_submit_button('回答')
    if era_btn:
        if answer_1 == 1:
            era_choice(20)
        if answer_1 == 2:
            era_choice(10)
        st.text('質問2へ')

with st.form(key='acter1_form'):
    st.text('質問2_1:この中で1番好きな役者さんを選んでください')
    acter1_list(1)
    acter1_btn = st.form_submit_button('回答')
    if acter1_btn:
        acter1_choice(20)
with st.form(key='acter2_form'):
    st.text('質問2_2:この中で2番目に好きな役者さんを選んでください')
    acter2_list(2)
    acter2_btn = st.form_submit_button('回答')
    if acter2_btn:
        acter2_choice(10)

with st.form(key='acter3_form'):
    st.text('質問2_3:この中で3番目に好きな役者さんを選んでください')
    acter3_list(3)
    acter3_btn = st.form_submit_button('回答')
    if acter3_btn:
        acter3_choice(5)

with st.form(key='writer_form'):
    st.text('質問3:この中に好きな脚本家はいますか？')
    answer_4 = st.selectbox(
        '''
        三谷幸喜:1, 宮藤官九郎:2, 古沢良太:3,
        福田靖:4, 大森美香:5, いない:6
        ''',
        (1,2,3,4,5,6))
    writer_btn = st.form_submit_button('回答')
    if writer_btn:
        if answer_4 == 1:
            st.session_state.dono += 15
            st.session_state.maru += 15
            st.session_state.gumi += 15
            st.text('あなたの回答:三谷幸喜')
        elif answer_4 == 2:
            st.session_state.idatenn += 15
            st.text('あなたの回答:宮藤官九郎')
        elif answer_4 == 3:
            st.session_state.ie += 15
            st.text('あなたの回答:古沢良太')
        elif answer_4 == 4:
            st.session_state.ryoma += 15
            st.text('あなたの回答:福田靖')
        elif answer_4 == 5:
            st.session_state.tuke += 15
            st.text('あなたの回答:大森美香')


point = {"光る君へ":st.session_state.kimi, "鎌倉殿の13人":st.session_state.dono,
         "平清盛":st.session_state.kiyomori,"真田丸":st.session_state.maru,
         "どうする家康":st.session_state.ie ,"おんな城主直虎":st.session_state.tora,
         "麒麟がくる":st.session_state.kirinn, "新選組！":st.session_state.gumi,
         "龍馬伝":st.session_state.ryoma,"青天を衝け":st.session_state.tuke,
         "いだてん":st.session_state.idatenn}

point2 = sorted(point.items(), key = lambda x:x[1], reverse = True)
final_rank = []
for i in range(10):
    title = point2[i][0]
    final_rank.append(title)
print(final_rank)

st.subheader('あなたにオススメの大河ドラマは')
st.header('1位')
st.header(final_rank[0])
st.header('2位')
st.header(final_rank[1])
st.header('3位')
st.header(final_rank[2])
st.subheader('大河ドラマ見てね！！！！！！')
