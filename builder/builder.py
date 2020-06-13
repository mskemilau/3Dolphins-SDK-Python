from collections import OrderedDict
import json


class Button:
    def __init__(self, picture_link, picture_path, title, subtitle, button_values):
        self.picture_link = picture_link
        self.picture_path = picture_path
        self.title = title
        self.subtitle = subtitle
        self.button_values = [button_values]

    def add_button_values(self, label, payload):
        self.button_values.append({
            'name': label,
            'value': payload
        })

    def build(self):
        result = OrderedDict()
        result['pictureLink'] = self.picture_link
        result['picturePath'] = self.picture_path
        result['title'] = self.title
        result['subTitle'] = self.subtitle
        result['buttonValues'] = []
        for button in self.button_values:
            result['buttonValues'].append(button)
        return '{button:'+json.dumps(result)+'}'
