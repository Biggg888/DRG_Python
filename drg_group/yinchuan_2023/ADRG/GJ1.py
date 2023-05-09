from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCG_DRG

def group(record):
  adrg_zd=["A18.303+K93.0*","A18.309","A18.313+K93.0*","A18.314+K67.3*","C15.900","C16.000","C16.200","C16.301","C16.500","C16.801","C16.802","C16.804","C16.900","C16.903","C17.000","C18.200","C18.900","C20.x00","C48.000","C76.200","C78.600x004","C78.601","C78.602","C79.809","D13.100","D17.500","D17.702","D18.000x859","D18.100x001","D20.000","D20.100","D20.101","D36.708","D37.200x003","D48.117","D48.121","D48.300x001","D48.301","D48.713","I72.800x063","I74.800x011","I86.800x014","K25.500x001","K26.501","K27.500","K27.503","K29.802","K31.606","K31.814","K35.200","K35.201","K35.300","K35.301","K35.800x001","K36.x02","K40.201","K40.900x002","K40.900x003","K40.901","K43.200","K44.900x001","K44.901","K55.004","K56.100","K56.201","K56.203","K56.500x003","K56.700","K56.701","K57.305","K58.801","K61.001","K63.102","K63.103","K63.105","K63.108","K63.203","K63.216","K64.811","K65.000","K65.003","K65.005","K65.008","K65.012","K65.013","K65.017","K65.806","K65.900","K65.901","K65.902","K65.903","K65.906","K66.800x008","K66.802","K66.805","K66.807","K66.808","K66.812","K66.901","K92.207","K92.208","K92.210","Q43.002","Q43.004","Q79.300","R10.402","R14.x00x006","S30.102","S36.802","S36.812","T18.801"]
  adrg_zd1=[]
  adrg_ss=["34.0401","39.9001","39.9002","40.1100x003","40.2900x017","40.2906","40.2908","41.5x00","53.8000x001","53.8001","53.8301","54.0x00x002","54.0x00x004","54.0x00x018","54.0x00x024","54.0x00x025","54.0x02","54.1100","54.1101","54.1900x006","54.1900x010","54.1903","54.1905","54.1909","54.2100","54.2300x003","54.2302","54.3x00x027","54.3x01","54.3x03","54.3x04","54.4x00x005","54.4x00x006","54.4x00x035","54.4x00x042","54.4x01","54.4x02","54.4x05","54.4x06","54.4x11","54.4x13","54.4x14","54.4x15","54.6101","54.7200x001","54.7402","54.7500x002","54.9100x002","54.9100x009","54.9101","54.9201","54.9900x010","54.9902","96.2900"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合GJ1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCG_DRG.GJ11_group(record):
      return 'GJ11'

    if MDCG_DRG.GJ13_group(record):
      return 'GJ13'

    if MDCG_DRG.GJ15_group(record):
      return 'GJ15'

    return 'GJ1'
  else:
    return ''
