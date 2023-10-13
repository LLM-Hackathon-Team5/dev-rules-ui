# 必要なライブラリをインポート
import streamlit as st
import json

# タイトルの表示
st.title('開発ルール設定アンケート')

# 項目と選択肢を辞書として定義
questions = {
    "コメントの詳細度": ["詳細", "普通", "簡潔"],
    # 他の項目も同様に追加してください
}

# ユーザーの回答を保存する辞書
answers = {}

# 各質問に対して選択肢を表示し、ユーザーの選択を保存
for question, options in questions.items():
    answer = st.selectbox(question, options)
    answers[question] = answer

# 「結果を表示」ボタンがクリックされたら、選択された回答を表示
if st.button('結果を表示'):
    st.write(answers)

    # 回答をJSON形式でテキストファイルとしてダウンロード可能にする
    st.download_button(
        label="結果をダウンロード",
        data=json.dumps(answers, indent=4).encode(),
        file_name="development_rules.json",
