from __future__ import print_function

from xml.dom import minidom
import zipfile, shutil

shutil.copy2('test.odt','test_smaller.odt')

with zipfile.ZipFile('test_smaller.odt', 'r') as odt:

    contentxml = odt.open('content.xml')
    xmldoc = minidom.parse(contentxml)
    contentxml.close()
    
    itemlist = xmldoc.getElementsByTagName('draw:frame') 

    for s in itemlist:
        # skip MathML entries
        if s.hasAttribute('draw:style-name') and 'mml-display' in s.attributes['draw:style-name'].value:
            print('skipping equation')
            continue
        elif s.hasAttribute('svg:width') and s.hasAttribute('svg:height'):
            # It is probably an image
            width = s.attributes['svg:width'].value
            height = s.attributes['svg:height'].value
            if 'pt' in width:
                units = 'pt'
            elif 'px' in width:
                units = 'px'
            else:
                raise ValueError
                
            new_width = str(int(float(width.split(units)[0])*0.32))+units
            new_height = str(int(float(height.split(units)[0])*0.32))+units
            s.setAttribute('svg:width', new_width)
            s.setAttribute('svg:height', new_height)
            print(width, 'x', height, '-->', new_width, 'x', new_height)
        else:
            print(s.attributes['draw:name'].value)
            
with zipfile.ZipFile('test_smaller.odt', 'a') as odt:
    odt.writestr('content.xml', xmldoc.toxml())
        