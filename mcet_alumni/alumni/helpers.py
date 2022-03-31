from django.core.exceptions import ValidationError

def validate_image_size(file, limit_mb = 10):
    ''' Validate a file's size does not exceed limit size'''

    file_size = file.file.size
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError(f"Max size of file is { limit_mb } MB")