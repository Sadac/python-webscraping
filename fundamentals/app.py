from lxml import etree

# convert the file to a tree element and assign that to the tree variable
tree = etree.parse('fundamentals/src/web_page.html')
# print(etree.tostring(tree)) # print it as a string

# get the title element. The first in tree will be at html tag inside level
title_element = tree.find("head/title")
# print(title_element)
print(title_element.text) # printout the text inside the title tag

p_element = tree.find("body/p")
print(p_element.text)

list_items = tree.findall("body/ul/li")
# print(list_items)
for li in list_items:
  a = li.find("a")
  if a is not None:
    print(f"{li.text.strip()} {a.text}")
    # strip to clean withspaces
  else:
    print(li.text)
