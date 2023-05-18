import os
import flickr_api

flickr_api.set_keys(api_key = 'be549094e025ae2e545716ade9ef3939', api_secret = '6cfcd06954ef66ea')
os.makedirs(os.path.join(os.getcwd(), "photos"), exist_ok=True)

user = flickr_api.Person.findByUserName("monzonco")
pages_nb = user.getPublicPhotos().info.pages
total = user.getPublicPhotos().info.total
current = 0

for page_nb in range(1, pages_nb+1):
    for index, photo in enumerate(user.getPublicPhotos(page=page_nb)):
        sizes = photo.getSizes()
        biggest_size = list(sizes.keys())[-1]
        filename = photo.title.replace("/", "-") + "_" + photo.id
        current += 1
        try:
            print(f"{current}/{total}", filename)
            photo.save(os.path.join(os.getcwd(), "photos", filename), size_label = biggest_size)
        except Exception as e:
            print(e)