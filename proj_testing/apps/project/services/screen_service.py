from ..models import Screen

class ScreenService:

    @staticmethod
    def get_all_screens():
        return Screen.objects.all()

    @staticmethod
    def create_screen(data):
        return Screen.objects.create(**data)

    @staticmethod
    def update_screen(screen, data):
        for key, value in data.items():
            setattr(screen, key, value)
        screen.save()
        return screen

    @staticmethod
    def delete_screen(screen):
        screen.delete()