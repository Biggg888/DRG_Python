from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCO_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["54.1100","54.1101","54.1201","54.1202","54.2100","54.2100x005","54.5100x009","65.0100x002","65.0100x003","65.0101","65.0102","65.0103","65.0104","65.0105","65.0900x005","65.0901","65.0902","65.0905","65.2100","65.2200","65.2400","65.2501","65.2502","65.2503","65.2504","65.2505","65.2900x001","65.2900x007","65.2900x011","65.2901","65.2902","65.2903","65.2904","65.2905","65.2906","65.3100","65.3900x001","65.4100","65.4900x001","65.4901","65.5200","65.5200x001","65.5400","65.6100","65.6200x001","65.7100x001","65.7600","65.7900x010","65.7901","65.7905","65.8101","66.0100x006","66.0101","66.0102","66.0103","66.0200","66.0201","66.0202","66.0203","66.1101","66.2101","66.2200x001","66.2900x003","66.2901","66.2903","66.3100","66.3200x001","66.3201","66.3900x001","66.3900x004","66.3901","66.3902","66.4x00","66.4x01","66.4x02","66.5100","66.5102","66.5200","66.5201","66.6100x006","66.6100x011","66.6100x014","66.6102","66.6104","66.6200","66.6200x003","66.6200x004","66.6201","66.6300","66.6301","66.6901","66.6902","66.7100","66.7100x002","66.7200","66.7300","66.7301","66.7400","66.7401","66.7900x009","66.7901","66.7903","66.7905","66.7906","66.8x02","66.9200x001","66.9201","66.9202","66.9203","66.9204","66.9205","66.9500x001","66.9500x004","66.9600x002","66.9700","66.9900","68.2900x035","68.2900x037","68.2915","68.2917","68.3903","68.3905","74.3x00x006","74.3x00x010","74.3x00x011","74.3x00x012","74.3x00x013","74.3x01","74.3x02","74.3x03","74.3x04","74.3x05","74.3x06","74.3x07","74.3x08","74.3x09"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合OE1入组条件，匹配规则：某一手术匹配')
    
    if MDCO_DRG.OE11_group(record):
      return 'OE11'

    if MDCO_DRG.OE13_group(record):
      return 'OE13'

    if MDCO_DRG.OE15_group(record):
      return 'OE15'

    return 'OE1'
  else:
    return ''
