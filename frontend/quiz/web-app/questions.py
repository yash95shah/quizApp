from quiz.gcp import storage, datastore

def upload_file(image_file, public):
    if not image_file:
        return None
    public_url = storage.upload_file(
        image_file,
        public
    )
    return public_url

def save_question(data, image_file):
    if image_file:
        data['imageUrl'] =  unicode(upload_file(image_file, True))
    else:
        data['imageUrl'] = u ''
    data['correctAnswer']= int (data['correctAnswer'])
    datastore.save_question(data)
    return