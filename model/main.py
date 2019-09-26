from aiclerk import AIClerk
import time


def main():
    # Start the microphone
    ai = AIClerk()
    ai.estimate_background_noise()
    ai.start()
    t0 = time.perf_counter()
    t1 = time.perf_counter()
    data_ = []
    while (t1-t0 < 10):
        t1 = time.perf_counter()
        res = ai.get_data()
        if res['audio']:
            data_.append(res)
            print(f'Person talking: {res["person"]}')

    print('Stopping')
    ai.stop()

    '''
    # Write audio files
    for idx, aud in enumerate(data_):
        aud_string = [a[0] for a in aud]
        save_aud(aud_string,f'rec_{idx}.wav', t)
    '''









if __name__ == '__main__':
    main()