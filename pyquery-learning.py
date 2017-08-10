from pyquery import PyQuery as pq;
from lxml import etree;

html = '''
  <div>
    <p id="id">id</p>
  </div>
''';

doc = pq(etree.fromstring(html));

print doc.text();

doc.append(pq('<p>233</p>'));

doc('#id').css({'background-color': 'yellow'});

doc('#id').attr('id', 'asd');

p_list = doc('p');

for item in p_list.items():
  print item.html();

print doc.html();

