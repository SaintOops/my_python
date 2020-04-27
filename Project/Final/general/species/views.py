from django.shortcuts import render

def index(request):

    species_list = {"info":
    [{"text":"Бинтуронг (Arctictis binturong) - уязвимый вид.","image":"https://s3.nat-geo.ru/images/2019/4/10/6956f2d4d7cf4e9f847605d88c89ce03.max-2000x1000.jpg"},
    {"text":"Выдровая цивета (Cynogale bennettii) - вымирающий вид.","image":"https://cs12.pikabu.ru/post_img/big/2020/04/09/9/1586445439152182825.jpg"},
    {"text":"Галаго Аллена, подвид (Sciurocheirus alleni alleni) - вымирающий вид.","image":"https://www.krasnouhie.ru/wp-content/uploads/2017/12/Galago.jpg"},
    {"text":"Линзанг Литона (Poiana leightoni)) - уязвимый вид","image":"https://avatars.mds.yandex.net/get-pdb/2497678/3eb47648-55f1-4588-82d6-e6dd83b131a5/s1200"},
    {"text":"Малабарская цивета (Viverra civettina)","image":"https://avatars.mds.yandex.net/get-pdb/901820/02c0f590-5436-4eda-92cf-105b47ac5ebd/s1200"},
    {"text":"Сулавесская цивета (Macrogalidia musschenbroekii)","image":"https://zooclub.ru/attach/2335.jpg"},
    {"text":"Цивета Оустона (Chrotogale owstoni)","image":"https://img1.liveinternet.ru/images/attach/c/4/80/408/80408903_chrotogale_owstoni_001.jpg"},
    {"text":"Бандикут Давида (Echymipera davidi) - вымирающий вид","image":"https://simple-fauna.ru/wp-content/uploads/2017/12/bandikuty.jpg"},
    {"text":"Гигантский бандикут (Peroryctes broadbenti) - вымирающий вид","image":"https://simple-fauna.ru/wp-content/uploads/2017/12/korotkonosyj-bandikut.jpg"},
    {"text":"Тасманийский бандикут (Perameles gunnii) - уязвимый вид","image":"https://upload.wikimedia.org/wikipedia/commons/8/8b/Perameles_gunni.jpg"},
    {"text":"Андаманская белозубка (Crocidura andamanensis) - вид на грани исчезновения","image":"https://1vet.by/images/beast/994.jpg"},
    {"text":"Инкский складчатогуб (Mormopterus phrudus) - уязвимый вид","image":"https://lh3.googleusercontent.com/proxy/u3tYmG10I_wOCYOSABfzMIY68j_UygJpcIWZcKSUxBupIC-2m1gzWhQWBaHl7Yt5o3d79IhuB7PnlwFgRPJm2cDbOUKnI-E8KL_DoRQ_xQQdCw"},
    {"text":"Йохорский складчатогуб (Chaerephon johorensis) - уязвимый вид  ","image":"https://zoogalaktika.ru/assets/images/mammalia/chiroptera/pteropus-lylei/pteropus-lylei_01.jpg"},
    {"text":"Кубинский складчатогуб (Mormopterus minutus) - уязвимый вид","image":"https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Artibeus_jamaicensis1.jpg/300px-Artibeus_jamaicensis1.jpg"},
    {"text":"Койбанский агути (Dasyprocta coibae) - уязвимый вид","image":"https://o-prirode.ru/wp-content/uploads/2017/09/osobennosti-pitaniya-aguti-1-e1505593173555.jpg"},
    {"text":"Мексиканский агути (Dasyprocta mexicana) - вид на грани исчезновения","image":"https://o-prirode.ru/wp-content/uploads/2017/09/Dasyprocta-mexicana-e1505591549987.jpg"},
    {"text":"Роатанский агути (Dasyprocta ruatanica) - вымирающий вид","image":"https://upload.wikimedia.org/wikipedia/commons/3/3b/Dasyprocta_leporina_-_Buffalo_Zoo.jpg"},
    {"text":"Галаго Аллена, подвид (Sciurocheirus alleni alleni) - вымирающий вид","image":"https://lh3.googleusercontent.com/proxy/EnCKUjo_UWa4P8vf7_3Qpu5lObHjKgZqKboZMXIxXfaOLEmuntkSA1TRxAHW4w0SK1F_RdC0xKlGXyKg4bbU4UAg-f43yDj0J0u6xzZseUlt"},
    {"text":"Исполинский златокрот (Chrysospalax trevelyani) - вымирающий вид","image":"https://faunist.ru/images/sokolov/Chrysospalax_trevelyani.jpg"},
    {"text":"Рондский галаго (Galagoides rondoensis) - вид на грани исчезновения","image":"https://www.myplanet-ua.com/wp-content/uploads/2017/01/3356780778_2ea2fceca7_b-e1483604549916.jpg"},
    {"text":"Карликовый бегемот (Choeropsis liberiensis) - вымирающий вид","image":"https://web-zoopark.ru/wp-content/uploads/2018/07/1-116.jpg"},
    {"text":"Обыкновенный бегемот (Hippopotamus amphibius) - уязвимый вид","image":"https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Mother_and_very_small_baby_hippo.jpg/240px-Mother_and_very_small_baby_hippo.jpg"},
    {"text":"Горный тенрек (Microgale monticola) - уязвимый вид","image":"https://cs9.pikabu.ru/post_img/2019/04/07/5/1554617314160784275.jpg"},
    {"text":"Гренландский кит (Balaena mysticetus) - вымирающий вид","image":"https://lh3.googleusercontent.com/proxy/VfQ10YcezLiT3sYuC6_7KbjyoU7WCacfcZ7TuQteyzoBLajBBZoTZw4CD1EoDxrdDwgFgocNNcNZ3mpw-qy951YQmeSuFjqoNKwTPeB4JUZf4NZXRA3WNy28xPclFrGohu2K5AlRGgXht8x3SVLs6FIxZP8g_7EKOI3AjPX60oqjPg04S_1h9cKogh2eaImcV903Bd-A9SuvwO5xnwpLFSJwXXHXdEW2sbwC7g"},
    {"text":"Северный гладкий кит (Eubalaena glacialis) - вымирающий вид","image":"https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Eubalaena_glacialis_with_calf.jpg/274px-Eubalaena_glacialis_with_calf.jpg"},
    {"text":"Японский кит (Eubalaena japonica) - вымирающий вид","image":"https://animalreader.ru/wp-content/uploads/2016/07/kit-gladkij-japonskij-naibolee-ujazvimyj-vid-na-zemle-animalreader.-ru-003.jpg"},
    ]}

    return render(request, 'species/index.html', species_list)
