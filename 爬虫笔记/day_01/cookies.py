import urllib.request as ur
import urllib.parse as up
headers={
    'Host':'www.icourse163.org',
    'Connection':'keep-alive',
    'edu-script-token':'8e8e8498ac42402fa489879bfd7b8355',
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47',
    'Origin':'https://www.icourse163.org',
    'Cookie':'EDUWEBDEVICE=393fe99ade9f47dd944376bfce7cbdd9; __yadk_uid=KGNdItcq5dy7A4PMxpvkABdIFrQbtDPa; WM_TID=NKmsJ1uVFnxFFQABUVY7JeYa0TIZlwzO; hb_MA-A976-948FFA05E931_source=www.baidu.com; videoVolume=0.8; hasVolume=true; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1605687541,1605688466,1606570472; WM_NI=vyGPiM3TJ5Wj%2F1yhwaiRLBMKeri%2BquQAgMGqOw8OFNp7v3ZydMg9puwicW2HMQiJtbTDq037k9awj%2FAm9GDZHo68V9NwWYFw2HYN3s7QqTG1xXNN9Twmd%2BgsNgy8qts4cHY%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb0f76dae87c094d05c8ea88aa7c54b828e9eafb66a839dfab7e53df5ecb68cf22af0fea7c3b92ab6a789b1ec47f18c86d6d662edefb789f66bab8e84a3d041a7aea7ccf47f939fa9aec67b8da9f8b0c546b4e9bad4d973a893a9daf37fb5b7adb8b1448f8fa7abf76a989cbfd1b23da9e7af98e92583b3f7a8c7528cb1fad9d5338ea999bac57df29897afb279f58fbfb5c63bbc8882afbc60b5b3accce6798eb9b7d9f480b1ecada9dc37e2a3; NTESSTUDYSI=8e8e8498ac42402fa489879bfd7b8355; NTES_YD_SESS=UKtBlGlwgkuT4dkPitQAQswKs2xFROEosYmn_ySB77.915ST1ltocJrMclLBVKY5yR3fnuesX9JFaljIgoEr.9IzJ2.REzrjFRwz_Fc_4GcF.ZDaKESgcQDynm.W0l48Yj0xMJ.6mDkDJw_yOyfCuwIPtA_8Q5YzclAOr4BDIC_84CM1oIi5ihZXlntDsMHoocIx0KPtla9RTYdLcXRMIAHqxyL_q.sMuSs7IdGtADM4r; NTES_YD_PASSPORT=rnePJxwgnghOvmtvO6wACyB9vFvClPG8sCJ53ONJlZS_LRgoLmWedXahdm4MSGuRi9IyN23FZqXSY8FU9ho5VdqnusFHquGc0BgyMNIG7hRnQ6yBB5B95.A5QnkaG1oXA.vrC07r2p7GMXtjypPHW1.ifPmNLVbSWeBDtqmaGKc.dhXiMcqsdG3gOX9G183I8wXMOblz_QDuaPpSSdi6l3OwS; S_INFO=1606570519|0|3&80##|18582699881; P_INFO=18582699881|1606570519|1|imooc|00&99|bej&1605689224&edumooc_client#shh&null#10#0#0|&0|null|18582699881; STUDY_INFO="yd.853d519828d14e57a@163.com|8|1387924997|1606570519907"; STUDY_SESS="rUrmBlNPkwT0tBJvr6TIUNL8ch5C+9YXOzVaiUehOS+9BdtkCYUMK1EZpOEhpaVjLg2gnbJWhJtT/Rxl6ruKzDO26tfihP3LjbciJ3/o33GL7dgNJKz9/fEzcghYMgqWaZZ9tcg/vvlTiuqKxDA7KED/o1X0q876bZpkIbK5X5oLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="KSDC+nvQAF+hEsL+A8IuprwbNtvBFRa5tI+HhtZ2C/v/WzxN4OA5iank0u4Jhq/d4joGNXJpYcGFUesetRa+pIea65hczu6bAKp+6w0nWeHDwvGOWZEkxOZSWM1iVUWCpo+4Z28F3DJkd2Xp3/b47BktB7MlruKP2zH3Q29B2ge20CRxGk6qJL/5TbLxaZujxCmfGzy7kjUyqwRRGhZoYDLWzOozTvlhJMPyFMN+ygLZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1387924997#|#1554200938695; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1606570520'

}

request=ur.Request("https://www.icourse163.org/",headers=headers)

response=ur.urlopen(request)

html=response.read().decode('utf-8')
print(html)
