# program template for Spaceship
import math
import random
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# globals for user interface
WIDTH = 800
HEIGHT = 600

score = 0
lives = 3
time = 0


class KeyScheme:
    def __init__(self, thrust, turn_left, turn_right, shoot):
        self.thrust = simplegui.KEY_MAP[thrust]
        self.turn_left = simplegui.KEY_MAP[turn_left]
        self.turn_right = simplegui.KEY_MAP[turn_right]
        self.shoot = simplegui.KEY_MAP[shoot]


class ImageInfo:
    def __init__(self, center, size, radius=0, lifespan=None, animated=False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated


# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim

# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5, 5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot3.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")


# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
# soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]


def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info, thrust_sound=None):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.thrust_sound = thrust_sound

    def draw(self, canvas):
        if self.thrust:
            center = (self.image_center[0] + self.image_size[0], self.image_center[1])
        else:
            center = self.image_center

        canvas.draw_image(self.image, center, self.image_size, self.pos, self.image_size, self.angle)

    def wrap_pos(self):
        self.pos[0] = self.pos[0] % WIDTH
        self.pos[1] = self.pos[1] % HEIGHT

    def accelerate(self):
        c = 0.05
        acc = 0.5
        self.vel[0] *= (1 - c)
        self.vel[1] *= (1 - c)
        if self.thrust:
            forward = angle_to_vector(self.angle)
            self.vel[0] += forward[0] * acc
            self.vel[1] += forward[1] * acc

    def update(self):
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        self.accelerate()
        self.wrap_pos()

    def shoot(self):
        global a_missile
        forward = angle_to_vector(self.angle)
        pos = [self.pos[0] + forward[0] * self.radius, self.pos[1] + forward[1] * self.radius]
        vel = [self.vel[0] + forward[0] * 6, self.vel[1] + forward[1] * 6]
        a_missile = Sprite(pos, vel, self.angle, 0, missile_image, missile_info, missile_sound)

    def turn(self, dir):
        turn_speed = 0.05
        dir = dir.upper()
        if dir == "LEFT":
            my_ship.angle_vel -= turn_speed
        elif dir == "RIGHT":
            my_ship.angle_vel += turn_speed
        elif "dir == NONE":
            my_ship.angle_vel = 0

    def thrusters(self, on):
        self.thrust = on
        if self.thrust_sound:
            if self.thrust:
                self.thrust_sound.rewind()
                self.thrust_sound.play()
            else:
                self.thrust_sound.pause()


# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound=None):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()

    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def wrap_pos(self):
        self.pos[0] = self.pos[0] % WIDTH
        self.pos[1] = self.pos[1] % HEIGHT

    def update(self):
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.wrap_pos()


def draw(canvas):
    global time, score, lives

    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2],
                      [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    if a_missile:
        a_missile.draw(canvas)

    # update ship and sprites
    my_ship.update()
    a_rock.update()
    if a_missile:
        a_missile.update()

    canvas.draw_text("Lives: " + str(lives), (20, 50), 32, "white")
    canvas.draw_text("Score: " + str(score), (WIDTH - 130, 50), 32, "white")


def rand(min, max, neg=False):
    if neg:
        return random.choice([
            random.randrange(min, max),
            random.randrange(-max, -min)
        ])

    return random.randrange(min, max)


# timer handler that spawns a rock
def rock_spawner():
    global a_rock

    pos = (random.randrange(WIDTH), random.randrange(HEIGHT))
    vel = (rand(2, 4, True), rand(2, 4, True))
    ang_vel = rand(4, 6, True) / 100.0
    a_rock = Sprite(pos, vel, 0, ang_vel, asteroid_image, asteroid_info)


def keydown(key):
    global my_ship
    if key == key_scheme.turn_left:
        my_ship.turn("left")
    if key == key_scheme.turn_right:
        my_ship.turn("right")
    if key == key_scheme.thrust:
        my_ship.thrusters(True)
    if key == key_scheme.shoot:
        my_ship.shoot()


def keyup(key):
    global my_ship
    if key in (key_scheme.turn_left, key_scheme.turn_right):
        my_ship.turn("none")
    if key == key_scheme.thrust:
        my_ship.thrusters(False)


# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info, ship_thrust_sound)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0.03, asteroid_image, asteroid_info)
a_missile = None
key_scheme = KeyScheme("up", "left", "right", "space")

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()