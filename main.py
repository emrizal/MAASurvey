
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.widget import Widget
import json
import requests

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols= 1

        self.inside=GridLayout()
        self.inside.cols= 2

        self.inside.add_widget(Label(text="Masukan Kode Toko"))
        self.kode=TextInput(multiline=False)
        self.inside.add_widget(self.kode)

        self.inside.add_widget(Label(text="Apakah ada Power Extension?"))
        self.pwrxt=CheckBox()
        self.inside.add_widget(self.pwrxt)

        self.inside.add_widget(Label(text="Apakah ada Mikrotik?"))
        self.mtik=CheckBox()
        self.inside.add_widget(self.mtik)

        self.add_widget(self.inside)

        self.submit=Button(text="Submit", font_size=40)
        self.submit.bind(on_release=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        kodetoko=self.kode.text
        powerxt=str(int(self.pwrxt.active))
        mikro=str(int(self.mtik.active))
        JSON=('{"'+kodetoko+'":{"Power Extension":"'+powerxt+'","Mikrotik":"'+mikro+'"}}')
        to_database=json.loads(JSON)
        requests.patch(url=MyApp.url,json=to_database)


class MyApp(App):
    url = 'https://surveysample-53422.firebaseio.com/.json'
    auth_key = 'rSimNOe2gR9iz52mEWWLiEQvcYGmEb09EIuPgpwI'
    
#    def patch(self, JSON):
#        to_database = json.loads(JSON)
#        requests.patch(url = self.url, json = to_database)

    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()