from emotionweb import Surprise

s=Surprise(
    type="birthday",
    name="Unknown",
    message="happy birthday sir",
    images=[
        "images/avi.jpeg",
        "images/travel.avif",
    ],
    caption=[
        "hello",
        "work on you",
    ]
    
)
s.generate()
