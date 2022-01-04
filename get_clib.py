from scipy import signal
import numpy as np
import librosa

def get_loc_clib(full_clib, small_clib, end_search):
    y_full, sr_full = librosa.load(full_clib, sr=None)
    y_small, sr_small = librosa.load(small_clib, sr=sr_full)
    full_Duration = librosa.get_duration(y=y_full, sr=sr_full)
    small_Duration = librosa.get_duration(y=y_small, sr=sr_small)
    if small_Duration > full_Duration:
       print("warning: You are looking for a clip within an audio clip shorter than it!!!")
    print(f"Full  Audio Duration:{full_Duration} | s")
    print(f"Small Audio Duration:{small_Duration} | s")

    end_search = int(full_Duration) if (end_search<=0 or end_search==None) else end_search
    
    correlate = signal.correlate(y_full, y_small[:sr_full*end_search], mode='valid', method='fft')
    start = np.round(np.argmax(correlate) / sr_full, 2)
    end = start+small_Duration
    print("The moment the search stops in seconds: ", end_search)
    print("Start:{} |s".format(start))
    print("End:{:.2f} | s".format(end))

if __name__ == '__main__':
    full_audio  = "Rasha_Rizk.wav"
    small_audio = "target.wav"
    search_pause_time = 0
    get_loc_clib(full_audio, small_audio, search_pause_time)
 
