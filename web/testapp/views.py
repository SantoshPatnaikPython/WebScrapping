from django.shortcuts import render
from .forms import Web_Form
from bs4 import BeautifulSoup
import requests
import os
import time

def image_download(image,number,loc):
    img_loc = loc
    data = image
    n_images = number
    GOOGLE_IMAGE = \
        'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

    if not os.path.exists(img_loc):
        os.mkdir(img_loc)

    searchurl = GOOGLE_IMAGE + 'q=' + data

    response = requests.get(searchurl)
    time.sleep(10)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    print(soup)

    results = soup.select('img[src^="https://encrypted-tbn0.gstatic.com/images"]', limit=n_images)


    imagelinks = []
    for i in results:
        imagelinks.append(i['src'])


    for i, imagelink in enumerate(imagelinks):
        # open image link and save as file
        response = requests.get(imagelink)

        imagename = img_loc + '/' + data + str(i + 1) + '.jpg'
        with open(imagename, 'wb') as file:
            file.write(response.content)



def details_seek(request):
    form = Web_Form
    if request.method=="POST":
        form = Web_Form(request.POST)
        if form.is_valid():
            to_search = form.cleaned_data['to_search']
            number_of_images = form.cleaned_data['number_of_images']
            destination = form.cleaned_data['destination_folder']
            image_download(to_search, number_of_images, destination)

    return render(request,"testapp/home.html",{"form":form})


