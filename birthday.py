from emotionweb import Surprise

s=Surprise(
    type="birthday",
    name="Aniket Vishwakarma",
    message="hey honey i love u i will always take stand for you",
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
