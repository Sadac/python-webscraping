from lxml import etree

# convert the file to a tree element and assign that to the tree variable
tree = etree.parse('fundamentals/src/web_page.html')
# print(etree.tostring(tree)) # print it as a string

# get the title element. The first in tree will be at html tag inside level
# title_element = tree.find("head/title")
# with xpath we dont need to specify the path tag by tag like in the find method
# the xpath returns an array, so we need to access the first item on the list
title_element = tree.xpath("//title/text()")[0]
print(title_element)
# print(title_element.text) # printout the text inside the title tag
# since we are using //title/text() function inside we dont need to use title_element.text


p_element = tree.xpath("//p/text()")[0]
print(p_element)

list_items = tree.xpath("//li")
# print(list_items)

# for li in list_items:
#   a = li.find("a")
#   if a is not None:
#     print(f"{li.text.strip()} {a.text}")
#     # strip to clean withspaces
#   else:
#     print(li.text)

for li in list_items:
  text = ''.join(map(str.strip, li.xpath(".//text()")))
  # add the . to get the text inside an array
  # if we execute xpath against an tag object we need to add the "."
  # if we execute xpath agains a tree object we dont need the "."
  print(text)
  # print(etree.tostring(li))
