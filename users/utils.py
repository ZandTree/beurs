# urils for user app
from django.utils import timezone


def upload_to(instance, filename):
    """ save uploaded file into media folder
    initial file name changed for the following format: 
    media/user/user_id/year-month-day-hour-seconds-milliseconds.extention
    """
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    timestemp = timezone.now().strftime("%Y-%m-%d-%H%M%S")
    milliseconds = now.microsecond // 1000
    return f"user/{instance.pk}/{timestamp}-{milliseconds}{extension}"
