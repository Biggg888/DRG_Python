from drg_group.hefei_2023.Base import message,intersect,SS_VALID
from drg_group.hefei_2023.DRG import MDCK_DRG
from drg_group.hefei_2023.DRG_EX import KD2X

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["06.0100x001","06.0200x001","06.0201","06.0900x004","06.0900x005","06.0900x006","06.0901","06.0902","06.0903","06.1200","06.3100","06.3101","06.3102","06.5100x001","06.5100x002","06.7x00","06.7x00x003","06.7x01","06.7x02","06.8100","06.8100x002","06.8900x005","06.8900x006","06.8900x007","06.8901","06.8902","06.8903","06.8904","06.8905","06.9100x001","06.9200","06.9300","06.9501","06.9502","06.9800","06.9900x002","40.1900x002","40.4000x003"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合KD2入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if KD2X.group(record):
      return 'KD2X'

    
    if MDCK_DRG.KD21_group(record):
      return 'KD21'

    if MDCK_DRG.KD23_group(record):
      return 'KD23'

    if MDCK_DRG.KD25_group(record):
      return 'KD25'

    return ''
  else:
    return ''
