from AudioReader import ThreadMicrophone, save_aud
from sklearn.neighbors import KNeighborsClassifier
import numpy as np



class DummyModel():

    def __init__(self):
        self.names = ['Niels','Prayson','Eskil','Frans','Alex']

    def predict(self, X):
        return np.random.choice(self.names)


class AIClerk():


    def __init__(self):
        self.t = ThreadMicrophone()
        self.model = DummyModel()


    def estimate_background_noise(self):
        self.t.background_noise()

    def start(self):
        self.t.start()

    def stop(self):
        print('Stopping')
        self.t.stop()
        self.t.join()

    def get_data(self):
        data = self.t.get_bytes()
        res = {'person':'','audio':[], 'audio_config':self.t.config}
        if data:
            aud = np.concatenate([d['data'] for d in data])
            pred = self.model.predict(aud)
            res['audio'] = b''.join([d['data_string'] for d in data])
            res['person'] = pred

        return res



    def save_aud(self, data_string, filename):
        save_aud(data_string,filename,self.t)