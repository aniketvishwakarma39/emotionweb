from emotionweb import Surprise

s=Surprise(
    type="anniversary",
    name="aniket",
    message ="happy anniversary honey",
    images=[
         "images/avi.jpeg",
        "images/travel.avif",
    ],
    caption=[
        "i love you honey",
        "aniket is aniket",
    ]


)
s.generate()