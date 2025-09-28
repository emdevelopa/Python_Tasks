model = [
    {"name": "Dog", "features": ["tail wiggles", "barks", 'four legs']},
    {"name": "Cat", "features":["purrs", "meeew",'four legs','proud']},
]


image = ["tail wiggles", "barks",]
# print(model[0]["features"])

def identify_image(image): 
    
    for animal in model:
        if image in animal["features"]:
            print(animal["name"])


 
for image_feature in image:
    # print(image_feature)
    identify_image(image_feature)
