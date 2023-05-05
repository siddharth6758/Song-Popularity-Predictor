from csv import DictWriter


def appendFunc(dictionary):
    fields = ['duration_ms','explicit','danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','time_signature']
    with open('test.csv', 'a',newline = "") as f_object:
        dictwriter = DictWriter(f_object, fieldnames=fields)
        # dictwriter.writeheader()
        dictwriter.writerow(dictionary)
        f_object.close()