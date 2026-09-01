from emotionweb import Surprise

s=Surprise(
    type="anniversary",
    name="unknown",
    message ="happy anniversary honey",
    images=[
         "images/avi.jpeg",
        "images/travel.avif",
    ],
    caption=[
        "dumn for you",
        "i dont know",
    ]


)
s.generate()