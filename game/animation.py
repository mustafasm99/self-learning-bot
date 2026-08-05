from PIL import Image
import pygame


class Animation:

    def __init__(self, gif_path, size=(48, 48), animation_speed=0.15):

        self.frames = []
        self.current_frame = 0
        self.timer = 0
        self.animation_speed = animation_speed

        gif = Image.open(gif_path)

        try:
            while True:

                frame = gif.copy().convert("RGBA")

                mode = frame.mode
                size_original = frame.size
                data = frame.tobytes()

                image = pygame.image.fromstring(
                    data,
                    size_original,
                    mode
                )

                image = pygame.transform.scale(
                    image,
                    size
                )

                self.frames.append(image)

                gif.seek(gif.tell() + 1)

        except EOFError:
            pass

    def update(self):

        self.timer += self.animation_speed

        if self.timer >= 1:

            self.timer = 0

            self.current_frame += 1

            if self.current_frame >= len(self.frames):
                self.current_frame = 0

    def get_frame(self):

        return self.frames[self.current_frame]