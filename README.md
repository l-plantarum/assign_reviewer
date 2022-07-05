学生と教員を，同程度の人数にD-Waveを使ってグループわけします．
ただし，学生は指導教員と別のグループになるものとします．
グループの数はソースコード中のNROOMを書き換えてください．

入力: テキストファイル list.csv に，以下の形式で学生名と教員名を指定してください．
このファイルの一行目は，必ず「学生名,ゼミ教員」でなければなりません．
二行目以降は，学生名と学生の指導教員名を半角コンマで区切って書き込みます．
学生を複数指導している指導教員の場合，指導教員名は厳密に同じにしてください．
例えば佐藤花子先生が田中一郎と山本陽子を指導している場合，田中一郎の行に「佐藤花子」山本陽子の行に「佐藤」と書いた場合，両者は別の教員と認識されます．
サンプルをlist.txtに格納します．

```
学生名,ゼミ教員
学生1,教員1
学生2,教員5

```