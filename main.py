from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
import json

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()

    def search_location(self):

        appidkey = "978031dbd4ea52dc90c8dfc5502d536b"
        search_template = "http://api.openweathermap.org/data/2.5/find?q={}&type=like&APPID="+ appidkey
        search_url = search_template.format(self.search_input.text)
        request = UrlRequest(search_url, self.found_location)

        print ("The user searched for '{}'".format(self.search_input.text))

    def found_location(self, request, data):
        data = json.loads(data.decode()) if not isinstance(data, dict) else data
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        self.search_results.item_strings = cities

class WeatherApp(App):
    pass

if __name__ == '__main__':
    WeatherApp().run()