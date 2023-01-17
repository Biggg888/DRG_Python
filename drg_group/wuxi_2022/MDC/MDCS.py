from drg_group.wuxi_2022.Base import message,intersect,SS_VALID
from drg_group.wuxi_2022.ADRG import SB1,SR1,SS1,ST1,SU1,SV1,SZ1

def group(record):
  mdc_zd=["A20.700","B41.800x003","T80.200","T81.400x006","B65.800x002","B00.900x005","A21.800x001","B39.400","A31.100x002","B69.800x008","A31.100","A31.101","A49.802","B65.000x001","B99.x01","B87.300","A53.000x002","B83.800x009","A01.400","B48.402","B55.200","A97.900","B66.000","A79.801","B49.x00x021","R50.803","T82.700x003","B88.800x002","A41.400x001","A49.901","A51.301","T85.712","T81.400x004","A20.100","B37.808","A93.200","B48.300x001","B46.900x002","A42.100","A19.901","A41.000","B57.200x001","B74.100x002","B74.901","B87.800x001","T85.709","B34.100","A92.300","B48.400","B88.300","B39.900","B74.300","A48.100x003","B65.001","A92.300x001","B42.100","A68.900","A92.300x003","T81.401","A92.500","A93.000","B40.800","A51.000x002","A66.800","A30.900x005","B60.000x001","T82.700x011","B66.900","A42.900","B36.800","B69.800x005","J10.800x002","B76.000","B83.400","A23.200","A24.002","A31.000x005","A41.300","B49.x02+E35.8*","B56.100x001","A49.801","A20.803","A01.000x007","A49.100x005","A59.000","A70.x00","A06.700","A19.200x001","B44.800x005","A24.202","A02.900x002","A51.400x001","A01.000x012","A93.100","A77.900x001","T80.200x004","A51.201","A48.400","A48.800x002","A18.104+N29.1*","B74.400","B78.700","A02.003","A02.901","B37.800x085","B54.x00x008","A77.300","A06.300","B78.000","Z03.000","A01.000x011","A30.200","A41.804","A06.800x001","A40.903+N16.0*","A79.000","A98.300","B69.900x001","B88.900x002","B71.000","A21.100","B49.x18","A49.813","A49.102","B67.401","B80.x00","A01.000x008","A49.817","B01.801","T85.700x104","B58.801+N16.0*","B05.803","B65.900x006","A30.400","B69.805","T81.400x005","B36.801","B83.800x008","A41.500x087","A41.502","A54.900","A30.500","B41.800x001","A32.700","A92.300x004","A06.200","A01.300","B87.900","A42.800x002","A67.100","B65.800x001","T82.700x008","A41.504","A77.200","B45.900","B49.x00x007","A93.802","A28.900","B34.400","A52.101","A31.001","B83.000x001","B81.800x002","A49.800x015","A01.000x006","A22.900","A75.000x004","A18.103+N29.1*","A18.212","A01.000x020","B33.802","A01.000x018","B51.000x001+D77*","A40.100","A50.900","B08.800x006","B65.900x008","B88.800x001","A66.400","B03.x00x003","B43.900","B76.900","B69.803","B03.x00x004","B48.700","A40.000","A02.100","B02.900x001","B88.800x004","B37.800x088","B34.800x003","A06.100x002","T98.200x012","A42.700","A30.400x002","A30.900x003","A18.107+N29.1*","A27.900x002","A06.300x001","A74.900","B65.200x001","B78.901","A06.900","A52.709+N08.0*","A49.806","A50.400","A49.002","B39.500x001","A26.700","A77.100","T81.402","B55.000x001","T80.201","B00.901","A23.900x003","B40.900","B44.800x003","A38.x00x010","B66.300x001","A41.200","A51.000","T84.701","A18.100x021+N37.8*","A21.000","A77.000","A20.300","A18.806+E35.0*","A92.800","A02.000x005","B74.200x002","B67.600x001","A31.800x004","B46.100x001+G99.8*","A01.000x010","B45.100","A19.200","B87.100","T85.711","A38.x00","T81.403","A77.100x001","A92.001","A48.100","B69.804","B34.900","B70.100","B05.900x005","T82.700x010","B76.800","B68.900x004","B00.900x007","A41.505","A49.900","B67.302+E35.0*","A22.100x003","A01.000x019","B88.000x003","B01.800x002+N08.0*","T81.405","B46.800x001","B66.901","B76.100","A40.300","B66.200","A19.902","B67.301","B74.900x003","A58.x01","A30.100x003","A75.900","A75.000x003","B81.100","A24.201","B74.400x002","B47.100","B65.905+N08.0*","A51.300x002","A92.400","A75.100","B99.x00x001","A21.700x002","B08.300","R50.800x002","A02.004","A49.814","B48.300","A98.400","B38.800","B83.300","A28.000","B45.801","A31.102","B83.800x006","A18.209","A63.000","B81.000","B69.800x003","B33.000x001","B01.900x002","A40.200","T85.700x809","A56.300x001","A67.300","T82.700x005","A77.000x001","B04.x00","A02.000","B83.200x001","B66.800x002","B74.100x003","B42.100x001","A41.806","B85.200","B68.901","B33.801","A02.001","A98.500x001+N08.0*","B00.202","B46.400","B02.800x001","A02.000x009","A49.800x023","A24.102","A43.800x001","A98.100","A01.000","A01.003","A01.000x014","A02.900x004","A42.804","A42.805","A50.100","A52.300","B00.001","B48.201","B55.100","B88.900x001","B08.100","A53.000x001","A27.900x005","A28.200","A97.100","B69.802","A21.300","B88.900x003","B71.900","A77.900","A18.106+N29.1*","A21.900x001","A52.100x011","B89.x01","B08.800x004","B66.400x001","B81.200","A50.400x001","B34.400x001","B42.100x003","A19.100","B65.100x001","T85.702","B03.x00","A41.805","A23.903+N16.0*","A51.302","B42.700","A54.602","A30.900x004","B81.802","B81.801","A96.800","A24.400","B57.200x003","B67.600x003","B66.300","B27.100","A27.900x006","A28.001","A98.400x001","A69.900","B48.401","A36.800x005+N33.8*","A30.400x001","A42.200x002","A43.801","A49.803","A25.100x001","T85.708","A28.801","T82.700x007","A06.800x003","A56.800","A54.900x002","T98.200x021","B77.800x004","A02.101","A49.810","B85.100","A52.800","A56.400","T82.700x001","B05.900x002","B46.500","B56.000x001","B71.800","A96.000","B68.000","A41.802","A18.208","A49.200","A99.x00","A21.800","A06.000","B83.800x003","A49.808","A49.003","A56.301","A49.000","A40.800","B49.x00x013","A65.x00","B25.900x001","B68.900x003","A96.100","A63.002","A69.800","A49.301","B67.700x001","B00.700","A23.100x001","A30.300","B67.400x001","B66.800x005","A44.800","B44.801","A01.000x017","A20.101","A41.801","B08.000x002","B77.900","B26.900x001","A49.103","B26.805+N08.0*","B53.100","A49.800x014","A24.300","A20.000","A18.100x031","A18.101","A79.900","B42.100x002","A02.800","A49.812","A21.700","B67.902","R50.900x002","B38.900","A36.900","A41.100x002","A01.000x009","B37.700","B45.700","A41.900x004","B83.800x007","A26.900x002","A19.900x004","A41.500x083","B66.000x001","A48.200","P37.000","B44.802","A18.211","A77.200x001","A02.000x007","A95.900","B68.100","A42.803","A53.900","B38.700","B55.000","A75.001","A40.900","B83.800x002","A51.001","A18.200x010","A49.300","A60.001","A51.300x004","A41.904+N16.0*","B74.400x003","A30.200x001","B50.900x001","B55.200x001","B65.900x007","B83.800x004","B74.000x002","B73.x00","B43.100","A23.000x001","T81.400x001","T81.406","B74.200x003","A06.100","A92.200","A59.800x001","B65.300","A24.000","A23.900x006","A38.x00x013","B83.900","A97.000","B66.800x004","A78.x00","B75.x00","A06.200x001","B85.300","B74.200x001","B03.x00x002","A31.000x004","A20.800x004","B81.300","B83.800x001","A56.000x003","B89.x00","B37.400x001+N37.0*","B64.x00","B08.000x004","A60.002","A43.100","A06.001","B41.700","A06.800x002","A24.100x003","A02.000x006","A41.101","B33.100","A79.800x002","A18.800x001","T85.701","A24.101","B43.801","A77.800","A20.000x001","A51.300x005","B67.904","T79.300x001","B41.900","B33.000","A20.800x005","A31.802","B37.401+N37.0*","B76.901","B44.900x001","B26.804","A49.800x019","A49.804","A27.800x001","A01.000x004","A50.000","A02.900x003","A18.700x002+E35.1*","B05.900x001","B39.400x001","B34.200","A51.300x003","B77.800x002","A18.200x006","B83.201","B05.801","B47.100x001","A92.000","A22.200x001","A20.802","A64.x00","A23.900x001","B25.800x001","A51.500","A31.002","B74.800x001","B45.800x002","B50.800","B90.102+N29.1*","A31.800x006","A32.900","A24.001","T85.700x808","A63.001","B53.800x001","B60.000","A02.000x010","A42.801","A98.000","T82.700x009","A54.600x001","B66.800x006","B49.x11","B55.900","B51.000","A51.900","A41.800x002","B67.907","A36.900x002","A51.100x001","B34.101","B55.100x001","T82.701","T86.807","B83.100","A18.105+N29.1*","B65.800x003","A43.802","A57.x00x002","A26.700x001","B34.000","A59.001+N37.0*","A38.x00x014","A25.000x001","T85.700x103","B34.800x002","A35.x00x001","A19.900","B34.300x002","B27.800","A38.x00x011","B66.902","B83.000x002","B83.200x003","A49.800x020","A01.100","A52.100","A49.100x004","A54.808","T82.700x004","A44.900","B52.900x001","A18.700+E35.1*","A57.x00x003","A32.803","A96.100x001","A18.100x022+N37.8*","B34.300","B34.102","B66.800x003","A06.002","A51.002","B07.x00x009","A31.800x001","A42.000","A50.600","B34.801","B48.000","B37.802","A30.100x001","A31.900x001","B47.000","B02.900x002","B66.500","A60.900","A18.207","A66.600","A49.815","B00.902","B05.800x010","B46.800x002","B33.800","A23.300","B60.800x001","A66.700","B50.000","A30.900x002","B26.800x004","B25.900x002","A92.900","B39.500","B69.800x004","T81.400x002","A49.800x003","A48.801","A31.000x001","B27.900x001","A54.601","T88.000","A32.701","B85.400","A52.200","B08.200","A49.101","A31.801","A31.800x003","A30.800","A18.100x025+N29.1*","A75.200x001","A27.000","A20.801","B74.900x005","A02.100x002","B66.100","A23.100","A52.700x012+N08.0*","B52.000","B48.000x001","B66.101","A42.802","T85.710","A66.300","B48.800x001","A30.900x008","A25.900","B67.601","B83.000","A94.x01","A50.200","A58.x00","A96.200","B42.900","T82.700x002","A52.900","A69.200","A48.300","B01.800x004","B66.800x001","A49.100x006","O98.600x001","B34.800x004","P37.100","A28.100","A49.811","B77.800x005","B67.901","A68.100","B81.400","A54.900x001","A48.100x001","A97.200","A21.300x002","A75.300x001","B08.000x001","P37.300","A66.100","A41.501","A67.900","A54.002","A55.x00","T85.703","B67.903","R50.801","R50.901","A43.900","B74.400x001","B65.101","A18.206","B05.400","A26.000","R68.801","A49.805","B00.204","B54.x00x004","A22.000","A31.800x007","B50.801","A66.900","A30.300x001","A51.303","B33.300x001","A32.000","B51.800","A24.100x002","B52.800","A54.500","B39.300","B05.802","B71.100","A30.000x001","B37.900","A49.201","B52.000x002+N08.0*","A79.100","A67.000","B88.100","A95.100","A79.901","B27.000","A06.000x001","A52.801","A41.506","A50.500","A56.001","B05.800x008","B77.803","A93.801","B79.x00","B69.100","A68.000","B18.103+N08.0*","B05.800x009","A18.813+D77*","A56.302","A92.100","B37.801","A30.900","B42.800","B27.001","B43.800","B68.900x002","A98.200","A23.800","A66.200","T81.404","A49.004","A49.902","B18.205+N08.0*","B76.902","B88.000x002","B83.800x005","A31.800x005","A20.900x002","B54.x00x006","A51.400x010","A41.807","A30.500x001","A44.100","B70.000","R50.900","A18.108+N33.0*","A22.200","A31.901","A48.000","A96.900","A41.900","B85.000","A41.503","A67.200","A54.809","A54.001","B00.205","A50.500x001","A20.200","A63.800","A66.000","A19.900x005","A27.900x004","B67.906","B06.900x001","B74.000x001","A18.210","A75.000x002","B47.900","B44.100x003","A56.200","B08.200x002","A01.200","B02.900x003","B58.900x001","A38.x00x012","B37.700x001","B37.901","A92.300x002","B74.000x003","A50.700","B26.800x010","B05.901","B53.000x001","B51.900","A63.003","B52.001+N08.0*","B57.300","A50.401","A02.002","A54.100x002","B02.700","B88.200x001","B56.900x001","B76.900x003","B48.200","B66.400","B26.800x011","A23.900x004","A77.300x001","B18.904+N08.0*","A24.000x002","B78.902+N08.0*","A59.900","B81.800x001","A41.400","T85.706","A44.000","B74.902","A49.807","B08.400x003","A49.001","A95.000","A48.800","A51.304","B55.000x003","B57.500","A26.900","A51.200","B44.700","B67.905","A31.803","B08.801","A42.200","B00.701","B69.801","B26.800x008+N08.0*","R50.802","A31.800x002","B67.600x002","A26.800x001","A36.804+N16.0*","B57.100","B74.900","A41.803","A22.700","A30.300x002","B40.700","B01.900x001","B08.401","B66.800x007","A18.801+E35.8*","A23.000","A52.700x001","B34.400x002","A27.800","A98.800","B74.100x001","A21.301","A31.000"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd):
    return ''
  
  message('符合MDCS入组条件，匹配规则：主诊断匹配')

  result=SB1.group(record)
  if result:
    return result

  if False and record.ssList and intersect(SS_VALID,record.ssList):
    message('符合SQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'SQY'

  result=SR1.group(record)
  if result:
    return result

  result=SS1.group(record)
  if result:
    return result

  result=ST1.group(record)
  if result:
    return result

  result=SU1.group(record)
  if result:
    return result

  result=SV1.group(record)
  if result:
    return result

  result=SZ1.group(record)
  if result:
    return result

  message('不符合MDCS的ADRG入组条件')
