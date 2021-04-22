import eel
import desktop
import search

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def kimetsu_search(word):
    '''
    if word == "":
        msgbox("検索単語を入力して下さい")
        exit()
    '''
    return search.kimetsu_search(word)
    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)