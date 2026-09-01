from emotionweb import Surprise

s=Surprise(
    type="loveletter",
    name="Unknown",
    message="its just a dummy msg",
    images=[],
    caption=["hello",
             "aket",
             "ani",
             "ket",],
)
s.generate()