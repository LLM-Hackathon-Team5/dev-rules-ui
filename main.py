# 必要なライブラリをインポート
import streamlit as st
import json

# タイトルの表示
st.title('開発ルール設定アンケート')

# dev-rules-qa.jsonからNo、質問、回答選択肢の3つを抽出し、その内容でquesionsを修正
with open('dev-rules-qa.json', 'r') as f:
    dev_rules = json.load(f)
    questions = {}
    for rule in dev_rules:
        questions[rule['question']] = rule['answer_options']
# ユーザーの回答を保存する辞書
answers = {}

# 各質問に対して選択肢を表示し、ユーザーの選択を保存
for question, options in questions.items():
    answer = st.selectbox(question, options)
    answers[question] = answer.split('. ', 1)[-1]  # 番号を除去


def to_markdown(answers):
    markdown_text = "# 開発ルール\n"
    for question, answer in answers.items():
        markdown_text += f"## {question}\n- {answer}\n\n"
    return markdown_text


# 「結果を表示」ボタンがクリックされたら、選択された回答を表示
if st.button('結果を表示'):
    st.write(answers)

    # 回答をTXT形式でテキストファイルとしてダウンロード可能にする
    markdown_data = to_markdown(answers)
    st.download_button(
        label="結果を「.txt」ファイルでダウンロード",
        data=markdown_data.encode(),
        file_name="development_rules.md",
        mime="text/markdown",
    )
    # 回答をJSONL形式でファイルとしてダウンロード可能にする
    jsonl_data = "\n".join([json.dumps({"input_text": question, "output_text": answer}, ensure_ascii=False) for question, answer in answers.items()])
    st.download_button(
        label="結果を「.jsonl」ファイルでダウンロード",
        data=jsonl_data.encode(),
        file_name="development_rules.jsonl",
        mime="application/json",
    )
    # 回答をJSON形式でファイルとしてダウンロード可能にする
    json_data = json.dumps(answers, ensure_ascii=False, indent=4)
    st.download_button(
        label="結果を「.json」ファイルでダウンロード",
        data=json_data.encode(),
        file_name="development_rules.json",
        mime="application/json",
    )

