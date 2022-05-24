#!/usr/bin/env python
# coding: utf-8

setting = {
 "grant_type": "password",
 "client_id" : "50a4e498-73e0-4e96-8ea2-e19a7a8ad354",
 "client_secret":"3_.w5F8n_Crz84C0ZbCnI_HEec3KJQYP0v",
 "resource": "https://graph.microsoft.com",
 "scope":"https://graph.microsoft.com",
 "username":"alex.lo@wiadvance.com",
 "password":"Alex880824"
}

displayname = {
    "54c994c6-a94f-4811-997c-4cbafdc2c8f2":"Michael Hsia 夏志豪",
    "a4685d0c-4353-43c4-a807-2ebba50b034e":"Pamela Tung 董書芝",
    "97f15e1c-bb98-48e2-a727-02430b2783ad":"Chris Liu 留正格",
    "785ebe6a-44ba-4743-9f2e-c855255b9abe":"Jackal Huang 黃建勳",
    "9bc194f3-cc00-443f-b656-0f8b28757748":"Alex Cho 卓聖恩",
    "677c4158-54ca-44da-8d67-5c86f52ea78f":"Melissa Sung 宋佳玫",
    "c9ebb53b-fbee-4663-a7a0-2af3d7e65683":"EJ Peng 彭怡潔",
    "0dcdb083-a9bd-4adc-bdd2-096d99a0e17c":"Jeff Ma 馬志昇",
    "a6794029-3dd2-4ce9-b09a-3cb8dde5d503":"Jerry Hsieh 謝蒼傑",
    "0d625e3f-4802-42cc-a1c4-061220ed81fa":"Thomas Wu 吳志晏",
    "d29a2a64-7c4b-4c0c-bd88-de9bb18ff904":"Candice Wu 吳鍾淇",
    "6ded4012-f22b-4a44-a09b-874e11a4dabf":"Joeson Chao 趙怡軒",
    "4b690a17-cf71-4f4a-afc1-d09a87c16efc":"Alfie Huang 黃祥瑋",
    "94e944d1-5d8b-4fda-a9b3-393765a357ca":"Alice Lin 林韻涵",
    "223f2935-1191-41b0-ae45-61fca78b340c":"Sam Chao 趙順卿",
    "3795aaba-c314-4915-82bd-ae2f3c87b6c6":"Dean Lee 李冠緯",
    "7db04677-5ed3-470b-b005-33240a0cfc5b":"Jason Shen 沈懷仁",
    "dc741363-e75e-46d5-aaa9-e8153c00c331":"Linus Liu 劉哲榮",
    "a7313047-265e-4f2c-8c4a-41074fbad4db":"Alex Wu 吳建宏",
    "228f88f7-93ef-496a-a00a-fcac3fe31adf":"Oliver Chan 詹新穎",
    "e81ae3b5-d5ed-4cfa-b7e3-6c4a879fffc4":"Jeff Yang 楊上輝",
    "9eac472b-f707-4cca-acb8-03e66cf9459e":"Bob Chao 趙思博",
    "50109c45-26e3-4f07-92d1-7b22d13eb0e4":"Chris Cheng 鄭佳鴻",
    "337cf452-9e95-4d86-9402-b16ba2d38ff1":"Cloud Hsueh 薛毓雲",
    "d7325081-3e12-485e-bd4f-703d4df72d7d":"Ashley Wang 王雅亭",
    "e7cf462b-f08b-4881-ae02-ea4c9ae1b074":"Emily Tsai 蔡瀞儀",
    "d55d4973-2a3a-4099-939f-c08ff61be0b2":"Star Yeh 葉郁馨",
    "8649ebd0-77d6-4ce2-803e-f071f21eec22":"Sean Lin 林昌宗",
    "f03dcd61-01f4-4547-823f-73869c2f00a3":"Zucker Lin 林侑緒",
    "217ab85b-3c23-4d79-811c-5ff7be01db0a":"George Hsiao 蕭友銘",
    "da053672-cf39-46c7-b62b-19bf6fc4bec0":"Eric Chan 詹清舜",
    "5be9ad14-7ed7-4f17-922e-f716a8668790":"Reborn Lee 李昶翰",
    "326bcaf4-582f-483c-ba14-fc7163f289d9":"Sam Wan 萬冠賢",
    "355fc8d4-3a0f-41a5-b23a-fdad95ff1f19":"Lopsa Hung 洪閔翔",
    "6d6ba087-00c2-4356-b197-dd31ac8d2372":"Benjamin Hsu 許鵬馥",
    "1f96292c-2e43-43b3-8627-ca234772fda4":"Cherry Chang 張怡君",
    "bf1ca2da-3e81-44e7-be75-5bd5f70d6d29":"Shante Yu 游三德",
    "9fe44807-88a8-4e68-972f-56886a2ca64f":"Jeff Yeh 葉士豪",
    "ace4ecf9-de76-4b49-8d3d-63f2ae4e9404":"Joey Lai 賴立勤",
    "01a7bd73-b46d-47d0-9539-f4fcb45fe63b":"Peter Chen 陳鈺祺",
    "0d501420-ea2b-40f1-b745-57af3ae92469":"James Huang 黃政傑",
    "98760298-37f0-4176-b650-87e2ad1b06bc":"Raymond Fan 范振煌",
    "1729fc8b-56c8-4f89-a748-3008553911a4":"Steven Tzeng 曾耀虹",
    "715d5ba9-ebc9-43d0-b573-e8ae2babbdb2":"Oscar Chang 張楷翊",
    "fb14c829-f339-4ca8-ad91-6a7d62207c51":"Wanjung Chang 張菀容",
    "25244cbd-c2ee-4620-8bf7-fcd3de73f7e2":"Royce Wang 王柏鈞",
    "7070584a-4de2-424c-bdab-113c9c5b3b2a":"Howard Chou 周昊勳",
    "6645d57d-d7b7-4a2f-9fb2-779ec6aac71e":"Tony Chung 鍾俊芳",
    "ce88140c-5cb5-494c-911a-3115ade06796":"Shengche Chiu 邱晟哲",
    "9c9e382d-1787-443c-b541-3a9301bf6d65":"Jeremy Chen 陳璟星",
    "554a4fcb-43ae-4f83-941c-4afd49e1dc5d":"Sam Hsu 許智淵",
    "9a395fb7-8c39-4814-9fb1-1628a0db5750":"Yueh Tang 唐岳",
    "1e57bdae-b96f-4e4a-9a57-31ff3dae93f7":"Alex Lo 羅哲琛",
    "783a7961-c0ab-4fe3-b6fb-75762cd0a9c9":"Leo Ou 歐先弘",
    "b9dcd5bc-0621-4b35-8c0a-af9cfdc9774c":"Christine Lin 林孟穎",
    "801bd74d-b3fb-4c3d-a3eb-cfcaa1bec7d6":"Yiching Chen 陳怡靜",
    "30eeaf41-e6a9-462f-b47a-3b0559890903":"Howard Yu 游適豪",
    "961c6785-c61f-4ded-9fb7-193d79d7d9ce":"Craig Lo 羅日忠",
    "17ce34ea-5e8c-48f9-a2d9-5c6876129ac6":"Jason Lo 羅傳璽",
    "c306e2ad-d950-4b58-a9d3-a5577a53ad18":"Chloe Shih 施嘉芳",
    "9ad2e56d-1c78-44b4-b3d6-d28f1016fde2":"Yuti Huang 黃郁菂",
    "2c98e4c7-1413-4e74-bb10-efe0780636f0":"Hanson Lin 林承翰",
    "5fed94a7-f12a-4d49-acb3-1a4450098a1a":"Alex Chen 陳毅文"
}



ID = {
    "NT0300":[
        "54c994c6-a94f-4811-997c-4cbafdc2c8f2",
        "a4685d0c-4353-43c4-a807-2ebba50b034e",
        "97f15e1c-bb98-48e2-a727-02430b2783ad",
        "785ebe6a-44ba-4743-9f2e-c855255b9abe",
        "9bc194f3-cc00-443f-b656-0f8b28757748",
        "677c4158-54ca-44da-8d67-5c86f52ea78f",
        "c9ebb53b-fbee-4663-a7a0-2af3d7e65683"
    ],
    "NT0P00":[
        "0dcdb083-a9bd-4adc-bdd2-096d99a0e17c",
        "a6794029-3dd2-4ce9-b09a-3cb8dde5d503",
        "0d625e3f-4802-42cc-a1c4-061220ed81fa",
        "d29a2a64-7c4b-4c0c-bd88-de9bb18ff904",
        "6ded4012-f22b-4a44-a09b-874e11a4dabf",
        "4b690a17-cf71-4f4a-afc1-d09a87c16efc"
    ],
    "NT0100":[
        "94e944d1-5d8b-4fda-a9b3-393765a357ca",
        "223f2935-1191-41b0-ae45-61fca78b340c",
        "3795aaba-c314-4915-82bd-ae2f3c87b6c6",
        "e7cf462b-f08b-4881-ae02-ea4c9ae1b074",
        "7db04677-5ed3-470b-b005-33240a0cfc5b",
        "dc741363-e75e-46d5-aaa9-e8153c00c331"
    ]
    ,
    "NT0M00":[
        "a7313047-265e-4f2c-8c4a-41074fbad4db",
        "228f88f7-93ef-496a-a00a-fcac3fe31adf",
        "e81ae3b5-d5ed-4cfa-b7e3-6c4a879fffc4",
        "9eac472b-f707-4cca-acb8-03e66cf9459e",
        "50109c45-26e3-4f07-92d1-7b22d13eb0e4",
        "337cf452-9e95-4d86-9402-b16ba2d38ff1",
        "d7325081-3e12-485e-bd4f-703d4df72d7d"
    ],
    "NT0000":[
        "e7cf462b-f08b-4881-ae02-ea4c9ae1b074",
        "d55d4973-2a3a-4099-939f-c08ff61be0b2"
    ],
    "NT0C00":[
        "8649ebd0-77d6-4ce2-803e-f071f21eec22",
        "f03dcd61-01f4-4547-823f-73869c2f00a3",
        "217ab85b-3c23-4d79-811c-5ff7be01db0a",
        "da053672-cf39-46c7-b62b-19bf6fc4bec0",
        "5be9ad14-7ed7-4f17-922e-f716a8668790",
        "326bcaf4-582f-483c-ba14-fc7163f289d9",
        "355fc8d4-3a0f-41a5-b23a-fdad95ff1f19",
        "6d6ba087-00c2-4356-b197-dd31ac8d2372",
        "1f96292c-2e43-43b3-8627-ca234772fda4",
        "bf1ca2da-3e81-44e7-be75-5bd5f70d6d29",
        "9fe44807-88a8-4e68-972f-56886a2ca64f",
        "ace4ecf9-de76-4b49-8d3d-63f2ae4e9404",
        "01a7bd73-b46d-47d0-9539-f4fcb45fe63b",
        "0d501420-ea2b-40f1-b745-57af3ae92469"
    ],
    "NT0900":[
        "98760298-37f0-4176-b650-87e2ad1b06bc",
        "1729fc8b-56c8-4f89-a748-3008553911a4",
        "715d5ba9-ebc9-43d0-b573-e8ae2babbdb2",
        "fb14c829-f339-4ca8-ad91-6a7d62207c51",
        "25244cbd-c2ee-4620-8bf7-fcd3de73f7e2",
        "7070584a-4de2-424c-bdab-113c9c5b3b2a",
        "6645d57d-d7b7-4a2f-9fb2-779ec6aac71e",
        "ce88140c-5cb5-494c-911a-3115ade06796",
        "9c9e382d-1787-443c-b541-3a9301bf6d65",
        "554a4fcb-43ae-4f83-941c-4afd49e1dc5d",
        "9a395fb7-8c39-4814-9fb1-1628a0db5750",
        "1e57bdae-b96f-4e4a-9a57-31ff3dae93f7",
        "783a7961-c0ab-4fe3-b6fb-75762cd0a9c9",
        "b9dcd5bc-0621-4b35-8c0a-af9cfdc9774c",
        "801bd74d-b3fb-4c3d-a3eb-cfcaa1bec7d6",
        "30eeaf41-e6a9-462f-b47a-3b0559890903",
        "961c6785-c61f-4ded-9fb7-193d79d7d9ce"
    ],
    "NT0220":[
        "17ce34ea-5e8c-48f9-a2d9-5c6876129ac6",
        "c306e2ad-d950-4b58-a9d3-a5577a53ad18",
        "9ad2e56d-1c78-44b4-b3d6-d28f1016fde2",
        "e81ae3b5-d5ed-4cfa-b7e3-6c4a879fffc4",
        "2c98e4c7-1413-4e74-bb10-efe0780636f0",
        "5fed94a7-f12a-4d49-acb3-1a4450098a1a"
    ]
}

def getSet():
    return setting
def getNames():
    return displayname
def getIDs():
    return ID
