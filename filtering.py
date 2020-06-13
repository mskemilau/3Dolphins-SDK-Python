from builder.builder import Button
import json
from collections import OrderedDict

button = Button(
    picture_link='https://selerasa.com/wp-content/uploads/2015/12/images_daging_ayam-goreng.jpg',
    picture_path='https://selerasa.com/wp-content/uploads/2015/12/images_daging_ayam-goreng.jpg',
    title='Ayam Goreng',
    subtitle='Ini ayam goreng',
    button_values={
        'name': 'Ayam',
        'value': 'Goreng'
    }
)
button.add_button_values('Label', 'Payload')

print (button.build())