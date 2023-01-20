
from lxml import etree 
import pandas as pd

xml_file = '/content/drive/MyDrive/Colab Notebooks/pbs.xml'
tree = etree.parse(xml_file,etree.HTMLParser())

tpplist=tree.xpath("//root/drugs-list/tpp")
tppDF = pd.DataFrame(columns = ['code','name','organisationreference', 'packsize', 'effectivelist', 'brandname'])

for tpp in tpplist:
  subset_effective_list = []
  subset_exmanufacturer_list=[]
  code=tpp.xpath('./code/text()')
  name=tpp.xpath('./preferred-term/text()')
  packsize=tpp.xpath('./pack-size/text()')
  organisationreference=tpp.xpath('./organisation-reference/code/text()')
  brandname = tpp.xpath('./brand-name/value/text()')
  exmanufacturerlist=tpp.xpath('./ex-manufacturer')
  effectivelist=tpp.xpath('./effective')
  
  #tppDF = pd.concat([tppDF, pd.DataFrame(data = [[code, name ,organisationreference, packsize ,effectivelist, brandname, content, exmanufacturerlist]], columns = ['code','name','organisationreference', 'packsize', 'effectivelist', 'brandname','content', 'exmanufacturerlist'])])

  for effective in effectivelist:

    if not effective is None:
       subset_effective_list = []
       for  sub_effective_elem in effective:
            date=sub_effective_elem.xpath('./text()')
            subset_effective_list.append({'effective date':date})

  for exmanufacturer in exmanufacturerlist:
   
   if not exmanufacturer is None:
    
     for  exmanufacturer_list in exmanufacturer:
          amount = exmanufacturer.xpath('./amount/text()')
          effectivedate = exmanufacturer.xpath('./effective/date/text()')
          subset_exmanufacturer_list.append({'amount':amount,"effectivedate":effectivedate})
    
  tppDF = pd.concat([tppDF, pd.DataFrame(data = [[code, name ,organisationreference, packsize , subset_effective_list, brandname, subset_exmanufacturer_list]], columns = ['code','name','organisationreference', 'packsize', 'effectivelist', 'brandname', 'ex-manufacturer'])])
  
  tppDF.to_csv('/content/drive/MyDrive/Colab Notebooks/pbs_drugslist_tpp.csv', index=False)
