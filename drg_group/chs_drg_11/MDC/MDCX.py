from drg_group.chs_drg_11.Base import message,intersect,SS_VALID
from drg_group.chs_drg_11.ADRG import XJ1,XR1,XR2,XR3,XS1,XS2,XT1,XT2,XT3

def group(record):
  mdc_zd=["Z02.800","Z11.802","Z47.800x005","Z64.400x001","Z12.800","T91.500x001","Q87.800x907","T95.000x010","Z30.102","R44.801","Z72.300","Z72.900","R19.004","T92.500x016","R74.800x006","Z50.700x001","Z13.400x001","Z47.800x030","T95.000x004","Z56.300","Z61.800","Z63.400x001","Z58.100","Z04.900","R47.002","T73.100","T78.900","T92.600","T92.800x002","Z24.600","Z75.800x001","T92.400x005","T93.800x002","T93.801","Q95.400","Z51.901","B90.800x006","Z46.701","Z63.400x002","Z65.300x003","Z71.700","Q99.101","T91.000x003","M23.201","Z47.800x018","T91.000x002","R79.805","R89.900x003","T92.500x015","T95.400","Z58.200","T90.201","T91.501","Z41.900","Q99.000","Z55.000","Z01.800x001","T92.501","Z58.900","Z61.600x001","Z64.100x001","Z65.300x002","M24.805","Q99.102","Z30.302","R62.802","Z20.900","Z28.100","T91.800x003","T95.200x003","B90.800x005","T93.201","M23.211","Q91.400","T92.105","T92.301","T92.500x011","T90.400x004","Z50.900x001","Q97.100","R46.700","Z63.600","T95.101","T70.900","R10.200x001","Z54.800x010","Z74.000","Q92.200","T96.x00x003","Z09.700","B90.802","R53.x00x006","T91.900x003","Z12.500","Z56.500","Z59.500","R64.x00x002","Z20.801","Z75.500","R25.200x004","Q98.500","Z76.500","Z01.503","T86.900","Z65.400x002","Q98.400","R25.200x009","Z12.100","Z51.300","R79.804","Z50.300","R82.500x001","T92.106","Z65.800","Z54.800x002","Z20.702","Z58.400","R93.501","M23.209","R41.100","Q97.000","T90.500x003","T93.300x005","R89.900x002","Z46.700","Z54.100","Z54.800x004","Z03.102","Z57.501","Z63.500x001","B94.802","T95.201","Z75.900x001","Z13.300x003","Z71.200","R76.801","R17.001","R19.000x009","R79.000x001","Z00.401","Z73.900","T92.101","T93.200x013","Z23.400","Z47.800x014","Z30.800x001","Z54.000x005","R77.901","T91.000x004","Z39.100x003","Z45.804","Z01.002","R60.000","Z51.400x003","Z59.000x001","K07.601","Z03.900","Z43.102","Z63.200x001","Q91.100","T92.100x009","R47.001","T92.801","Z31.400x004","Z13.600","M23.202","Z24.500","Z43.300","B90.200","R70.101","T92.300x007","Z43.400x004","B94.200","Z27.000","Z70.000","T92.302","Z04.800","Q87.806","R98.x00x002","Z43.900x001","T87.200","R79.000","T84.400","Z01.502","T93.600x002","T90.200","R13.x00","Z01.800x004","R79.000x006","Z04.300","T98.200x031","Z43.403","R60.900","R93.202","Z51.400x001","R79.800x005","T91.800x007","B90.001","Z29.200x001","Q99.801","Z09.802","Z47.800x022","T92.300","Q92.400","Q93.200","Q92.800","Z12.000","Z54.000x002","Z55.200","Z43.400x003","T92.300x008","Z20.802","T92.300x011","Z30.800x005","Z73.600","Z04.100","T93.800x001","Z71.000","Z54.000x008","Q98.800","R54.x00","Z04.001","Z00.100","T93.200x012","T92.201","Q89.900","T93.204","Z47.800x031","R85.902","Z22.801","Z47.800x011","R52.000","T80.202","T92.303","R25.200x002","Z24.100","R74.800x005","Z65.300x005","Z47.800x020","M24.806","Z43.400x005","Z57.504","T95.300x003","Z61.700x001","Z54.000x009","R76.200","Q87.800x905","T92.503","T95.100x001","Z64.300","T93.102","B90.903","Z30.400x003","Z04.500","Z59.700","Z41.300","R23.200x002","Z09.900x001","Z10.200","Z31.203","T80.203","R18.x00","R53.x00x012","Z47.800x023","R68.800x002","T95.800x006","T91.803","Z01.200","Z22.300","Z54.000x016","Z45.202","Z45.101","Z63.700x001","Z30.800x004","T97.x02","I69.800x002","Q92.700","R11.x01","Z47.800x026","Z60.500","R18.x00x003","R89.000","Z23.100","R54.x01","T93.200x001","Z13.001","R63.601","T92.500x013","R85.901","T92.602","T93.300x003","Z39.100x001","Z39.200x001","Z43.201","Q98.000","Z22.700","B90.100","T95.103","R99.x00x002","Q87.801","T85.806","Z22.000","Z22.400","Z30.503","Z40.900x001","Z54.800x001","R74.801","Z76.201","Z54.300","Z63.700x021","Z01.501","Z43.400x002","Z47.800x034","Z63.800x003","R74.804","Q85.914","T92.402","Z47.800x028","Z54.000x003","Z57.507","Z70.200","Z76.100","Z59.600","M24.808","T91.900x002","Q92.100","Z22.200","Z27.100","T95.002","R19.001","Q95.200","T93.103","R71.x00x004","Z54.700","Z65.300x004","B90.904","R53.x00x002","R63.000","T95.800x002","R63.500","T92.500x006","Z02.100","T92.100","M24.810","Z72.400","T91.800x006","R46.800x001","T90.200x012","R47.004","Z54.000x021","R25.200x007","T93.400x006","Z30.900","R96.100x001","T92.104","R62.801","Z04.002","Z02.500","Z13.801","Z44.300","Z47.800x006","B90.804","B94.801","T90.202","Z13.100","Z11.800x001","R77.803","T95.102","T91.900","Z01.101","Z29.100","Z47.800x019","Z72.800","T93.600","Z24.001","Z29.800","Z47.800x007","T96.x00x001","Q93.100","T93.800","Z30.500x011","T95.202","Z62.800","Z47.800x003","B94.800x001","R23.000","T93.200","Z28.800","T90.100","Z63.700x093","Z73.300","Z13.800x021","Z47.800x015","Z65.400x001","T92.500x004","T90.400x001","Z22.301","T92.500x007","Z45.201","T95.800x007","Z54.900x001","Z13.500","T91.202","Z61.500x001","R77.101","T92.506","R74.900x001","Z02.600","T97.x00x003","R47.100x001","Z58.800","Z12.400","Z03.103","Z27.300","Z43.301","Z71.600","Z13.200","Z13.800x032","Z50.200","Z47.800x035","Z55.900","T91.200","B90.000","Q95.300","T92.300x001","T92.300x012","R89.500","R53.x00x004","R26.100x001","R74.000x001","Z10.800","T73.300","R11.x03","R63.200x002","T81.601","T92.400x002","T92.600x002","Z30.301","Z47.800x012","M24.807","Z63.900","Z63.800x004","Z29.101","T95.200x004","T92.100x008","T92.900","R76.000x001","R87.900x002","T90.205","Z50.101","Z72.200","Z00.800","R46.000","Z23.800x001","Z31.800","T92.000","Q98.900","Z22.102","M24.803","R68.200","Z54.000x004","T85.802","T92.001","Z22.600","R46.500","Z57.400","Z60.900","Z62.100x001","Z62.200x001","Z01.700","Z03.800x731","R68.300x002","T90.000","Z13.300","T95.000x002","T91.200x005","T92.307","I69.400","R89.100","Z22.303","Z61.000x001","R77.800x004","Z47.800x029","T93.400x005","R76.200x002","Z30.000x002","Q95.900","Q96.300","R76.100x001","Z59.200","Z00.600","Z54.000x020","Z47.800x036","Z11.902","Q96.800","Z55.100","Z45.803","R63.300x002","T92.500x014","Z23.000","Z47.800x009","R77.800x003","Z62.900","R60.001","Z57.600","R47.101","R74.001","T92.500x009","T93.600x001","Z13.501","Z73.100x001","Z01.600","Z23.200","T95.000x011","R76.802","Z74.800","R47.000x006","Z03.100","R70.100","Z58.000","R74.800x007","Z57.502","Z52.001","Z63.800x001","Z43.801","T92.500x017","Z55.800","R41.000","T90.800x002","Z25.000","Z45.807","R77.000","Z01.001","Z28.900","Z45.200","B90.201","T90.206","Z51.600","Z54.200x001","Z22.402","R18.x00x001","Z46.900","Q96.400","Z72.500","R10.201","T94.001","Z73.000","R53.x00x008","R93.301","B94.201","Z02.400","Q91.500","T92.100x011","T93.400x004","Z27.900","T93.400x003","R25.200x008","Z65.100x001","Z63.400x003","Z30.202","T95.000x005","T96.x00x002","Z63.700x092","R62.803","Z51.401","T84.901","R79.803","Z46.500x001","Q99.100x003","R70.000","T90.203","T95.300x001","T91.200x002","Z22.101","B94.100","R89.400","Z56.100","Q93.000","Z24.601","R77.200","T93.400","R62.000x002","T92.203","Z57.508","R47.801","T95.001","Z71.100","T92.400x004","Z30.505","T93.000","T92.400","Z73.500","Z02.000","Z13.500x001","R68.800x003","Z73.200","Z10.000","Z52.300x002","T91.002","R11.x02","T88.901","Z65.900","T91.800x005","Z73.400","I69.802","T92.500x001","R19.000x013","Z50.600","Q91.000","B92.x00","R18.x00x005","Z13.700","Z31.500","Z47.800x025","Z30.501","T85.801","R76.800x001","Z65.500x003","Z31.900","Z75.400","Z48.900x001","Q92.900","R53.x00x009","Z31.400x003","Z31.402","E89.900","Q92.500","R58.x00x002","R60.901","T95.801","R41.200","T91.205","Z60.400","Z72.000","Z30.504","Z24.400","R54.x00x003","Z43.302","T93.200x011","T93.200x014","Z48.000x002","R23.100x002","Z74.200","T92.200","T95.000x006","R89.300","T97.x01","T91.500x003","R46.801","Z76.800x001","R52.900","Z09.000x001","Z11.500","Z01.800x002","Z65.200","R41.800x002","T93.208","R93.800x002","M23.203","T91.800x001","R63.100","Z00.500x001","Z56.700","T73.900","T91.001","Z54.000x015","Z64.400x002","R77.800x006","Z20.400","Z26.800","Z47.800x032","Z76.400","Z30.400x004","Z61.900x001","R58.x00x007","Z71.500","Z54.000","Z73.800","T91.800x004","Q96.200","Q99.900","T91.800x008","Z30.103","R53.x00x003","Z43.604","Z61.400x001","T92.202","T95.200x005","Z20.300","B91.x00","T93.300x002","B90.200x003","T98.300x007","Z32.100","Z47.800x021","M23.208","Z50.500","Z45.805","Z60.000x001","Z54.400","Z71.900","R76.100","M23.501","T90.900","Z22.900x001","B90.101","T84.700x001","Z11.200","T92.603","Z04.400","Z27.800","Z11.901","T69.900","Z12.901","T95.000x012","Z31.600x001","Z03.300","R59.901","Z50.800x002","Z31.202","Z54.000x013","Z57.505","B90.902","Z72.600","Z31.401","Z50.501","Z62.600x001","Q96.000","T93.500x002","R47.000x001","Q93.700","Z13.900","Z50.801","Z54.800x006","Q93.300","Z25.100","R61.900","T92.300x006","R77.801","Z13.800x022","T90.500x002","Z11.100","Z30.800x002","T92.304","T93.200x008","Q90.100","Z57.800","T93.300x001","R41.300x001","Z55.400","Z13.800x031","M23.215","Z13.800x011","T93.202","R46.600","Z43.402","R79.000x002","Z59.800","Z03.800x701","R89.800","Z61.200x001","Z03.800","Z63.500x003","T91.201","Z47.800x016","Z47.800x013","T95.800x004","Z45.900","Z29.000","Z09.801","R52.200","R74.802","T93.900","T90.208","Z41.801","Z75.000","R87.900x003","T70.400","Z24.300","Z27.200","Q96.900","T92.100x005","R61.100","R74.800x008","T93.600x003","Z10.300","Z11.000","Z59.900","Z54.800x008","Z58.500","Z03.900x001","T93.203","B94.900","T95.200x006","Z54.800x003","Z70.800","Z12.200","Z12.300","Z43.700","Z60.100x001","T90.401","T93.500x001","T90.200x008","Z60.800","Q99.800","Q93.800","T91.206","B90.801","Z30.101","Q97.200","R49.800x003","T90.102","T95.301","T98.200","Z57.700","Z20.100","Z62.000x001","Z26.900","Z11.300","Z10.100","Z54.000x022","T93.207","T92.504","Z11.600","R46.300","Z47.800x008","Z30.201","R63.200","Z43.200","R19.002","Z60.200x001","Z65.400x003","Z44.200x002","Z60.300x002","T91.802","Z54.000x019","R58.x00x005","Z11.803","Z02.700","Z30.400x001","T92.500x010","Q93.600","Z29.201","R47.003","R72.x00x002","B94.101","R62.000x003","T91.204","T92.400x008","R68.000","T95.800x001","T95.800x005","Z54.000x018","Z64.200","R47.000x005","T92.300x016","Q92.000","T95.900","Z51.800","Z57.503","Z22.302","Z54.000x017","R77.802","Z57.000","R53.x00x005","R19.000x003","T92.300x013","Z20.000","Z26.000","Z43.101","Z02.900","T92.300x005","T93.101","Z09.300","T95.200x001","R69.x00","Z54.800x007","Z70.300","T90.400x003","Z50.000","T93.001","Z40.000x001","R53.x00x010","Z46.501","R62.900","Z13.000x001","T75.200","Z58.600","Z43.603","Z13.800x051","Z65.500x001","Z48.000x001","Z13.800x061","Z74.100x001","Z57.100","Z65.300x001","B94.800x003","T85.800","Z03.600x001","M23.214","Z47.800x027","T90.901","T92.300x002","Z59.400","Z09.804","T92.505","R77.800x001","T90.204","R84.900x004","T92.204","T95.100x002","R77.100","Z20.701","Q98.100","T91.400","T98.200x032","R47.802","R84.901","R84.902","Z12.600","T95.800x003","Q95.000","Z00.300","Z09.803","Z76.300","Z63.500x002","Z74.900","R19.000x008","Z00.200","T93.200x002","Z45.802","R18.x01","Z47.800x017","B90.803","Z40.800","Z58.300","R93.800x003","R77.900","R74.800x003","Z39.100x002","Z59.300","T93.104","Z12.900x001","T92.400x007","Q91.600","Q96.100","Z20.600","I69.801","Z55.300","R68.100x001","T92.400x006","Z62.300x001","Z57.900","R19.003","Q99.100","T93.300x008","T95.000x009","Z61.300x001","Z63.300x001","Z30.000x001","R79.000x004","T92.500x003","R53.x00x011","R61.901","Z00.001","R52.901","Z28.101","T92.100x004","Z22.800","Z63.700x091","Z43.601","Z43.401","M24.100x091","Z20.500","Z54.000x007","Z23.700","T92.502","Z03.802","T95.000x003","Z61.100x001","Q92.300","R89.700","T92.800x001","Z76.000","T91.401","T91.800x010","Z01.102","M24.102","Z24.200","Q99.200","T91.800x002","Z54.000x012","T92.103","R46.100","T92.305","Q98.300","Z70.900","T93.800x003","T82.812","Z01.600x002","Z57.201","Q91.700","T90.400x002","T92.600x003","R79.000x003","T95.800x008","T94.102","T95.802","T92.500x018","Z56.200","Z54.800x005","Z76.900","Z00.300x001","Z32.000x001","Z64.400x003","Q89.700","R25.200x005","T93.300x009","T92.300x015","Q98.200","T93.501","T95.000x001","B90.200x002","T95.803","Z46.503","Z47.900","Q91.200","Z63.100x001","T85.902","T91.502","R71.x00x005","T73.200","Z52.000","Z54.000x006","R99.x01","Z59.100","Z43.600x002","R63.300x003","Z50.400x001","T92.300x017","Q95.800","R58.x00x006","R68.101","T80.800","Z04.200","R89.900x001","T84.700","T93.205","Z11.801","Q97.800","T93.100","Z47.800x033","M23.212","Q92.600","R63.100x002","T73.800","Z62.500x001","Z70.100","T98.000","T94.002","R61.001","Z46.502","T93.200x010","Z03.800x721","Z09.001","Z23.300","T92.400x003","Q90.200","Z27.400x001","B94.000","T94.100","Z43.100","Z71.300","R41.001","T95.200x002","Z71.400","Z22.103","B90.800x004","T95.100x003","Z62.400x001","Z29.900","R47.000x008","Z74.300","Z47.800x024","R19.000x012","Z20.200","Z52.900","R77.800x002","Z65.000","Z72.100","Z56.600","Z57.506","Z56.400","R79.800x003","T93.200x007","Q99.802","Z75.200","Q98.700","R63.400","T93.206","N81.800x006","Q89.901","Z25.800x001","Z63.000","Z02.200","R19.000x016","Z09.400","R23.101","Z23.500","Z42.000","R47.100x002","Z54.000x010","Z63.800x002","Z65.500x002","Z71.800","Z47.800x010","Z28.201","T95.000x008","R26.100","Z28.000","T92.601","T95.300x002","T92.102","T94.000","Z56.000","R58.x00x004","Z03.803","Z11.400","Q95.100","Z20.001","Z30.000x003","R89.200","Z01.900","R79.900","Z02.300","Z03.800x711","R52.100","R23.100","T80.801","Z01.300","Z30.800x003","Z41.800x002","T91.000x001","Z43.602","Z63.700x011","R25.200x006","Z22.401","Z50.100x001","B90.002","T92.500x008","Z75.100","T91.800x009","T84.900","Z03.101","B90.202","R76.900","R71.x00","R87.900x001","T92.500x012","B90.901","Z47.800x004","Q98.600","Z57.300","Q95.500","R68.300","T92.401","R53.x00x001","T93.400x002","Q97.900","T92.500x002","Z22.100","Z23.600","Z13.300x002","Z43.802","R68.100x002","R17.000","T90.207","T95.000x007","T93.301","R77.200x001","R74.803","R60.100","T92.100x010","R49.801","R61.000","Z45.806","M23.204","T98.301","Z58.700","Z04.601","R89.600","Z13.800x041","R82.100","Z54.800x009","Z43.500","R54.x00x002","Z01.600x001","Z54.000x014","Z51.400x002","Z42.900","Z30.203","Q97.300","T92.306","Z75.300"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd):
    return ''
  
  message('符合MDCX入组条件，匹配规则：主诊断匹配')

  result=XJ1.group(record)
  if result:
    return result

  if False and record.ssList and intersect(SS_VALID,record.ssList):
    message('符合XQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'XQY'

  result=XR1.group(record)
  if result:
    return result

  result=XR2.group(record)
  if result:
    return result

  result=XR3.group(record)
  if result:
    return result

  result=XS1.group(record)
  if result:
    return result

  result=XS2.group(record)
  if result:
    return result

  result=XT1.group(record)
  if result:
    return result

  result=XT2.group(record)
  if result:
    return result

  result=XT3.group(record)
  if result:
    return result

  message('不符合MDCX的ADRG入组条件')
