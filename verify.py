from mechanize import Browser
from lxml import html
import requests

def findName(house_number, street_name, city):
  br = Browser()
  br.open("http://propertytax.peoriacounty.org/")
  response = br.response()

  def select_form(form):
    return form.attrs.get('action', None) == '/Search/ExecuteSearch'

  br.select_form(predicate=select_form)
  br['house_number'] = house_number
  br['street_name'] = street_name
  br['community_name'] = city

  br.submit()
  newUrl = br.geturl()
  page = requests.get(newUrl)
  tree = html.fromstring(page.content)
  owners = '';
  owner1 = tree.xpath('/html/body/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[1]')
  if not len(owner1) == 0:
    owners = (owner1[0].text)
  owner2 = tree.xpath('/html/body/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[1]')
  if not len(owner2) == 0:
    owners = owners + " " + (owner2[0].text)
  return owners

owners = findName("7007", "Stratton", "peoria")
print owners