import pandas as pd
import eel

### デスクトップアプリ作成課題
def kimetsu_search(word):
    # 検索対象取得
    val = eel.js_function('file')()
    df=pd.read_csv("./" + val)
    source=list(df["name"])

    # 検索
    if word in source:
        # print("『{}』はあります".format(word))
        txt = "『{}』はあります".format(word)

    else:
        # print("『{}』はありません".format(word))
        txt = "『{}』はありません".format(word)
        # 追加
        '''
        add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        if add_flg=="1":
        '''
        source.append(word)
    return txt

    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    df.to_csv("./" + val, encoding="utf_8-sig")
    print(source)
