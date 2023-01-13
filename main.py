
from lxml import etree
import pandas as pd


xml_file = '/content/drive/MyDrive/Colab Notebooks/pbs.xml'
tree = etree.parse(xml_file, etree.HTMLParser())

tpplist = tree.xpath("//root/drugs-list/tpp")
tppDF = pd.DataFrame(columns=['code', 'name', 'organisationreference',
                     'packsize', 'effectivelist', 'brandname', 'content', 'exmanufacturerlist'])

for tpp in tpplist:
    code = tpp.xpath('./code/text()')
    name = tpp.xpath('./preferred-term/text()')
    packsize = tpp.xpath('./pack-size/text()')
    organisationreference = tpp.xpath('./organisation-reference/code/text()')
    brandname = tpp.xpath('./brand-name/value/text()')
    content = tree.xpath('./content/text()')
    exmanufacturerlist = tpp.xpath('./ex-manufacturer/text()')
    effectivelist = tpp.xpath('./effective')

    tppDF = pd.concat([tppDF, pd.DataFrame(data=[[code, name, organisationreference, packsize, effectivelist, brandname, content, exmanufacturerlist]], columns=[
                      'code', 'name', 'organisationreference', 'packsize', 'effectivelist', 'brandname', 'content', 'exmanufacturerlist'])])

    # for effective in effectivelist:
    #   subset_effective_list = []
    #   for sub_effective_elem in effective.iter():
    #        subset_effective_list.append({'text':sub_effective_elem.text})

    # for exmanufacturer in exmanufacturerlist:
    #   subset_exmanufacturer_list = []
    #   for sub_exmanufacturer_elem in exmanufacturer.iter():
    #        subset_exmanufacturer_list.append({'text':sub_exmanufacturer_elem.text})

    # print(code,",",name,",",organisationreference,",",packsize,",",effective,",",subset_effective_list, ",",brandname,",",content, ",",subset_exmanufacturer_list)

    # tppDF.append(pd.DataFrame([code, name ,organisationreference, packsize ,effectivelist, brandname, content, exmanufacturerlist]))
