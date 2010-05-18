# -*- coding:utf-8 -*-
import sys
import xml.etree.cElementTree as ET
from datetime import datetime

import elementflow

def ef_generator(file, count):
    with elementflow.xml(file, 'contacts') as xml:
        for i in range(count):
            with xml.container('person', {'id': unicode(i)}):
                xml.element('name', text='John & Smith')
                xml.element('email', text='john.smith@megacorp.com')
                with xml.container('phones'):
                    xml.element('phone', {'type': 'work'}, text='123456')
                    xml.element('phone', {'type': 'home'}, text='123456')

def et_generator(file, count):
    root = ET.Element('contacts')
    for i in range(count):
        person = ET.SubElement(root, 'person', {'id': unicode(i)})
        ET.SubElement(person, 'name').text = 'John & Smith'
        ET.SubElement(person, 'email').text = 'john.smith@megacorp.com'
        phones = ET.SubElement(person, 'phones')
        ET.SubElement(phones, 'phone', {'type': 'work'}).text = '123456'
        ET.SubElement(phones, 'phone', {'type': 'home'}).text = '123456'
    ET.ElementTree(root).write(file, encoding='utf-8')


if __name__ == '__main__':
    start = datetime.now()
    ef_generator(open('/dev/null', 'w'), 40000)
    print datetime.now() - start
