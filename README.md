# dev-rules-ui
## 概要
- 開発チームのコーディングルールを設定するUIを開発。
- ユーザーは、コーディングルールに関する選択式のQAに回答
- 回答内容に基づき、開発ルールがMarkdown言語で開発ルール.txtファイルとして出力

## 1. 目次


## 2. Outputイメージ


## 3. システム構成の概要


## 4. 使用技術について
- UI：Streamlit
- 開発言語：Python 3.10.1

## 5. QA項目
| No | 項目                                       | 詳細                                                                                             |
|----|-------------------------------------------|--------------------------------------------------------------------------------------------------|
| 1  | コメントの詳細度                          | コメントがコードの意図や動作をどの程度詳細に記述するかを選択                                     |
| 2  | コメントに開発者の意思を記載するか        | コード内に開発者の意図やTODO、HACKなどを記載するかどうか                                         |
| 3  | 関数の説明を行うdocstringの記載項目、詳細度 | 関数の動作、入力パラメータ、変数の型、戻り値など、どの程度詳細にdocstringを記載するか           |
| 4  | 変数の型を動的に設定するか、静的に設定するか | 変数の型を動的に決定するか、静的に型を宣言するかを選択                                           |
| 5  | 変数・関数名は英語中心にするか日本語中心にするか | コード内の識別子の命名を英語または日本語で行うかを選択                                           |
| 6  | コメントすべきでないことのルール           | コード内で避けるべきコメントのタイプを複数選択                                                   |
| 7  | 関数・クラス分割の詳細度                    | コードの機能ごとに関数やクラスをどの程度分割するか、その基準を設定                               |
| 8  | 変数・関数名は短縮系を許容するか許容しないか | 識別子の命名で短縮形を許容するかどうかを選択                                                     |
| 9  | 望ましいデザインパターン（生成パターン）    | Singleton, Factory Methodなど、プロジェクトで推奨する生成パターンを選択                         |
| 10 | 望ましいデザインパターン（構造パターン）    | Adapter, Bridgeなど、プロジェクトで推奨する構造パターンを選択                                   |
| 11 | 望ましいデザインパターン（振る舞いパターン） | Command, Iteratorなど、プロジェクトで推奨する振る舞いパターンを選択                             |
| 12 | コードのリファクタリング頻度                | コードのリファクタリングをどの程度の頻度で行うかを設定                                           |
| 13 | テストカバレッジの目標値                   | プロジェクトのテストカバレッジの目標値を設定                                                     |
| 14 | エラーハンドリングの方針                   | エラーハンドリングの方法や方針を設定                                                             |
| 15 | コードのインデントスタイル                 | インデントのスタイル（スペース、タブ、その数）を設定                                             |
| 16 | コードレビューの基準                       | コードレビューで注目するポイントや基準を設定                                                     |
| 17 | ユニットテストの記述基準                   | ユニットテストをどの程度詳細に記述するかの基準を設定                                             |
| 18 | コードの最大行数                           | 関数やファイルの最大行数を設定                                                                   |
| 19 | ブランチングストラテジー                   | Gitのブランチの作成と管理のストラテジーを設定                                                     |
| 20 | CI/CDの導入                                | 連続的インテグレーションとデリバリーのツールや方針を設定                                         |



## 6. 環境構築の手順


## 7. ディレクトリ構造


## 8. Gitの運用ルール


## 参考記事
- Readme書き方: https://speakerdeck.com/knr109/xin-ren-enziniagakai-fa-siyasuireadmenoshu-kifang?slide=12
- StreamlitでのQA＋Submit：https://blog.streamlit.io/build-a-streamlit-form-generator-app-to-avoid-writing-code-by-hand/
