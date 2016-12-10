from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
from kivy.uix.listview import ListItemButton
from kivy.factory import Factory
import json

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()
    lat = ObjectProperty()
    long = ObjectProperty()
    appidkey = "978031dbd4ea52dc90c8dfc5502d536b"

    def search_location(self):

        if self.search_input.text == "":
            return

        appidkey = "978031dbd4ea52dc90c8dfc5502d536b"
        search_template = "http://api.openweathermap.org/data/2.5/find?q={}&type=like&APPID="+ appidkey
        search_url = search_template.format(self.search_input.text)
        request = UrlRequest(search_url, self.found_location)

        #print ("The user searched for '{}'".format(self.search_input.text))

    '''def get_lat_get_long(self):

        if self.lat == "" or self.long == "":
            return

        appidkey = "978031dbd4ea52dc90c8dfc5502d536b"
        search_template = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&APPID=" + appidkey
        search_url = search_template.format(self.lat.text,self.long.text)
        request = UrlRequest(search_url, self.found_lat_and_long)'''

        #print(search_url)

    def found_location(self, request, data):
        data = json.loads(data.decode()) if not isinstance(data, dict) else data
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        #print(cities)
        self.search_results.item_strings = cities
        del self.search_results.adapter.data[:]
        self.search_results.adapter.data.extend(cities)
        self.search_results._trigger_reset_populate()

    '''def found_lat_and_long(self, request, data):
        arr = []
        data = json.loads(data.decode()) if not isinstance(data, dict) else data
        city = "{} ({})".format(data['name'], data['sys']['country'])
        #city = "{}".format(data['name'])
        arr.append(city)
        print(arr)
        self.search_results.item_strings = arr
        #print data['sys']['country']'''

class LocationButton(ListItemButton):
    pass

class WeatherRoot(BoxLayout):
    def show_current_weather(self, location):
        self.clear_widgets()
        current_weather = Factory.CurrentWeather()
        current_weather.location = location
        self.add_widget(current_weather)

    def show_add_location_form(self):
        self.clear_widgets()
        self.add_widget(AddLocationForm())

class WeatherApp(App):
    pass

if __name__ == '__main__':
    WeatherApp().run()