import cherrypy
import pandas as pd

from OpenSSL import SSL
import xmltodict
import json


def xml_item(row):
    xml = ['<ITEM id="{}">'.format(row.name)]
    for field in row.index:
        xml.append('  <{0}>{1}</{0}>'.format(field, row[field]))
    xml.append('</ITEM>')
    return '\n'.join(xml)

def df_to_xml(df, docid):
    xml = '\n'.join(df.apply(xml_item, axis=1))
    xml = '<?xml version="1.0" encoding="utf-8"?>\n<RESPONSE>\n<ITEMS>\n'+xml+'\n</ITEMS>'
    xml = xml + '\n<DOCUMENT>\n<DOCID>{}</DOCID>\n</DOCUMENT>\n</RESPONSE>'.format(docid)
    return xml


class MyWebService(object):  
    @cherrypy.expose
    def process(self):
        body_xml = cherrypy.request.body.read()
        xmlDict = xmltodict.parse(body_xml)
        json_file = json.dumps(xmlDict["REQUEST"]["ITEMS"]["ITEM"])
        docid = xmlDict["REQUEST"]["DOCUMENT"]["DOCID"]
        if isinstance(json.loads(json_file), dict):
            nrows = 1
        else:    
            nrows = len(json.loads(json_file))
        df = pd.DataFrame.from_records(json.loads(json_file), index=list(range(nrows))).set_index("@id")
        df = df.astype(dtype={'BUKRS': str,
                              'PSWSL': str,
                              'KOSTL': str,
                              'PROJK': str,
                              'NPLNR': str,
                              'AUFNR': str,
                              'LIFNR': str,
                              'VEND_NAME': str,
                              'NET_AMOUNT': float,
                              'GROSS_AMOUNT': float,
                              'F_TAX_AMOUNT': float,
                              'TAXRATE_1': float,
                              'IBAN': str})
   
        files = xmlDict["REQUEST"]["DOCUMENT"]
        p = myprocessor.MyProcessor()
        
        return docid 


if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0', 
             'server.socket_port': 8000}
    cherrypy.config.update(config)
    cherrypy.quickstart(MyWebService())

