import magic

def is_video(file):
    mime = magic.Magic(mime=True)
    file_type = mime.from_buffer(file.read(1024))
    return file_type.startswith('video/')