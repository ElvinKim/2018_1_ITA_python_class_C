from bs4 import BeautifulSoup

html_code ="""
<html>

 <head>

  <title>

   The Dormouse's story

  </title>

 </head>

 <body>

  <p class="title">

   <b id="story">

    The Dormouse's story

   </b>

  </p>

  <p class="story">

   Once upon a time there were three little sisters; and their names were

   <a class="sister" href="http://example.com/elsie" id="link1">

    Elsie

   </a>

   ,

   <a class="sister" href="http://example.com/lacie" id="link2">

    Lacie

   </a>

   and

   <a class="sister" href="http://example.com/tillie" id="link2">

    Tillie

   </a>

   ; and they lived at the bottom of a well.

  </p>

  <p class="story">

   ...

  </p>

  <table>

  <tr class="tr_1">

   <td class="element1"> one </td>

   <td class="element2"> two </td>

   <td class="element3"> three </td>

  </tr>



  <tr class="tr_2">

   <td class="element1"> one </td>

   <td class="element2"> two </td>

   <td class="element3"> three </td>

  </tr>



  <tr class="tr_3">

   <td class="element1"> one </td>

   <td class="element2"> two </td>

   <td class="element3"> three </td>

  </tr>



  </table>

 </body>

</html>
"""

soup = BeautifulSoup(html_code, "html.parser")

print(soup.title)
print(soup.title.name)
print(soup.title.text)

print(soup.find_all("td"))
print(soup.find_all("td")[0].text)
print(soup.find_all("td", {"class": "element1"}))


print(soup.find("tr", {"class": "tr_1"}).find_all("td"))