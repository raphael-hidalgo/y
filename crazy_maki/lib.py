def try_me():

    from PIL import Image
    import requests
    from io import BytesIO

    response = requests.get('https://thumbs.dreamstime.com/b/funny-maki-sushi-character-eating-sticks-silly-childish-drawing-isolated-white-background-creature-colorful-vector-78986858.jpg')
    img = Image.open(BytesIO(response.content))
    return img
