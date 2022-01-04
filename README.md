# Search-within-an-audio-clip
Searching for an audio clip inside another clip using librosa &amp; scipy


You can replace the files here and run the function

```python
    full_audio  = "Rasha_Rizk.wav"
    small_audio = "target.wav"
    search_pause_time = 0
    get_loc_clib(full_audio, small_audio, search_pause_time)
```

If you want to search inside a video, you can use the following command to convert the video to a wav
Then search inside the resulting file
```
ffmpeg -i wissal_idbella.mp4 -vn -acodec pcm_s16le -ar 44100 -ac 2 out_ws.wav
```
# Output
```
    Full  Audio Duration:595.32 | s
    Small Audio Duration:15.104 | s
    The moment the search stops in seconds:  595
    Start:200.0 |s
    End:215.10 | s
```
