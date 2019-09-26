# SAPhackathon2019AIClerk
A trancribing AI that records who said what at business meeting.

# Requirements

```bash
conda create env -n transcriber -c conda-forge speechrecognition tensorflow fastapi
conda activate transcriber
conda install pyaudio
pip install uvicorn
```

# Running

```bash
cd app
uvicorn app:app --reload
```
