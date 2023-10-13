import json

# ファイルからデータを読み込む
with open('development_rules.md', 'r') as file:
    lines = file.readlines()

# 質問と回答を抽出
rules = {}
current_question = None
for line in lines:
    if line.startswith("##"):
        current_question = line.strip("# ").strip()
    elif line.startswith("-"):
        rules[current_question] = line.strip("- ").strip()

# JSONに変換して表示
rules_json = json.dumps(rules, indent=4, ensure_ascii=False)
print(rules_json)

# JSONファイルに保存
with open('development_rules.json', 'w') as json_file:
    json_file.write(rules_json)
