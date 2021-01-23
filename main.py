import sys, math, pygame

red = (139,0,0), (139,0,0), (139,0,0), (139,0,0), (139,0,0), (139,0,0)
white = (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)
black  = (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)
beige = (255,224,189), (255,224,189), (255,224,189), (255,224,189), (255,224,189), (255,224,189)
pink = (255, 182, 193), (255, 182, 193), (255, 182, 193), (255, 182, 193), (255, 182, 193), (255, 182, 193)
yellow = (255, 215, 0), (255, 215, 0), (255, 215, 0), (255, 215, 0), (255, 215, 0), (255, 215, 0)

def rotate2d(pos, rad):
    x, y = pos
    s, c = math.sin(rad), math.cos(rad)
    return x*c-y*s, y*c+x*s

class Cam:
    def __init__(self, pos=(0, 0, 0), rot=(0, 0)):
        self.pos = list(pos)
        self.rot = list(rot)

    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            x, y = event.rel
            x /= 200
            y /= 200
            self.rot[0] += y
            self.rot[1] += x

    def update(self, dt, key):
        s = dt*10
        if key[pygame.K_LSHIFT]:
            self.pos[1] += s
        if key[pygame.K_SPACE]:
            self.pos[1] -= s

        x, y = s*math.sin(self.rot[1]), s*math.cos(self.rot[1])

        if key[pygame.K_w]:
            self.pos[0] += x
            self.pos[2] += y
        if key[pygame.K_s]:
            self.pos[0] -= x
            self.pos[2] -= y
        if key[pygame.K_a]:
            self.pos[0] += x
            self.pos[2] -= y
        if key[pygame.K_d]:
            self.pos[0] -= x
            self.pos[2] += y

class Cube:
    vertices = (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
    edges = (0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)
    faces = (0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4), (2, 3, 7, 6), (0, 3, 7, 4), (1, 2, 6, 5)

    def __init__(self, pos=(0, 0, 0)):
        x, y, z = pos
        self.verts = [(x+X/2, y+Y/2, z+Z/2) for X, Y, Z in self.vertices]



pygame.init()
w, h = 800, 800
cx, cy = w//2, h//2
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
cam = Cam((0, 0, -5))
pygame.event.get()
pygame.mouse.get_rel()
pygame.mouse.set_visible(0)
pygame.event.set_grab(1)

red_cubes = [
    #right leg
    Cube((0, -1, 1)), Cube((0, -1, 2)), Cube((0, -1, 3)), Cube((1, -1, 1)), Cube((1, -1, 2)), Cube((1, -1, 3)),

    #left leg
    Cube((4, -1, 1)), Cube((4, -1, 2)), Cube((4, -1, 3)), Cube((5, -1, 1)), Cube((5, -1, 2)), Cube((5, -1, 3)),

    #belly bottom layer
    Cube((0, -2, 0)), Cube((1, -2, 0)), Cube((2, -2, 0)), Cube((3, -2, 0)), Cube((4, -2, 0)), Cube((5, -2, 0)),
    Cube((0, -2, -1)), Cube((1, -2, -1)), Cube((2, -2, -1)), Cube((3, -2, -1)), Cube((4, -2, -1)), Cube((5, -2, -1)),
    Cube((0, -2, 5)), Cube((1, -2, 5)), Cube((2, -2, 5)), Cube((3, -2, 5)), Cube((4, -2, 5)), Cube((5, -2, 5)),
    Cube((0, -2, 4)), Cube((1, -2, 4)), Cube((2, -2, 4)), Cube((3, -2, 4)), Cube((4, -2, 4)), Cube((5, -2, 4)),
    Cube((-1, -2, -1)), Cube((-1, -2, 0)), Cube((-1, -2, 1)), Cube((-1, -2, 2)), Cube((-1, -2, 3)), Cube((-1, -2, 4)),
    Cube((6, -2, -1)), Cube((6, -2, 0)), Cube((6, -2, 1)), Cube((6, -2, 2)), Cube((6, -2, 3)), Cube((6, -2, 4)),

    #belly layer above belt
    Cube((-1, -4, -1)), Cube((-1, -4, 0)), Cube((-1, -4, 1)), Cube((-1, -4, 2)), Cube((-1, -4, 3)), Cube((-1, -4, 4)),
    Cube((6, -4, -1)), Cube((6, -4, 0)), Cube((6, -4, 1)), Cube((6, -4, 2)), Cube((6, -4, 3)), Cube((6, -4, 4)),
    Cube((0, -4, -1)), Cube((1, -4, -1)), Cube((2, -4, -1)), Cube((3, -4, -1)), Cube((4, -4, -1)), Cube((5, -4, -1)),
    Cube((0, -4, 5)), Cube((1, -4, 5)), Cube((2, -4, 5)), Cube((3, -4, 5)), Cube((4, -4, 5)), Cube((5, -4, 5)),
    Cube((7, -4, 0)), Cube((7, -4, 3)), Cube((8, -4, 1)), Cube((8, -4, 2)), Cube((9, -4, 1)), Cube((9, -4, 2)),
    Cube((-3, -4, 1)), Cube((-3, -4, 2)), Cube((-4, -4, 1)), Cube((-4, -4, 2)),
    Cube((-2, -4, 0)), Cube((-2, -4, 3)),

    #belly layer 2 rows above belt
    Cube((0, -5, -1)), Cube((1, -5, -1)), Cube((4, -5, -1)), Cube((5, -5, -1)), Cube((-1, -5, -1)), Cube((6, -5, -1)),
    Cube((-1, -5, 0)), Cube((6, -5, 0)), Cube((0, -5, 5)), Cube((1, -5, 5)), Cube((4, -5, 5)), Cube((5, -5, 5)),
    Cube((2, -5, 5)), Cube((3, -5, 5)), Cube((-1, -5, 4)), Cube((6, -5, 4)),
    Cube((6, -5, 3)), Cube((6, -5, 2)), Cube((6, -5, 1)), Cube((7, -5, 0)), Cube((7, -5, 3)),
    Cube((8, -5, 1)), Cube((8, -5, 2)), Cube((9, -5, 1)), Cube((9, -5, 2)),
    Cube((-3, -5, 1)), Cube((-3, -5, 2)), Cube((-4, -5, 1)), Cube((-4, -5, 2)),
    Cube((-2, -5, 0)), Cube((-2, -5, 3)),


    #belly layer 3 rows above belt
    Cube((-1, -6, 0)), Cube((6, -6, 0)), Cube((6, -6, 0)), Cube((0, -6, 5)), Cube((1, -6, 5)), Cube((4, -6, 5)),
    Cube((5, -6, 5)), Cube((2, -6, 5)), Cube((3, -6, 5)), Cube((-1, -6, 4)), Cube((6, -6, 4)),
    Cube((6, -6, 3)), Cube((6, -6, 2)), Cube((6, -6, 1)), Cube((7, -6, 0)), Cube((7, -6, 3)),
    Cube((8, -6, 1)), Cube((8, -6, 2)),
    Cube((-3, -6, 1)), Cube((-3, -6, 2)),
    Cube((-2, -6, 0)), Cube((-2, -6, 3)),

    #red hat bottom layer
    Cube((1, -13, -1)), Cube((2, -13, -1)), Cube((3, -13, -1)), Cube((4, -13, -1)), Cube((5, -13, 0)),
    Cube((1, -13, 5)), Cube((2, -13, 5)), Cube((3, -13, 5)), Cube((4, -13, 5)), Cube((5, -13, 4)),
    Cube((5, -13, 3)), Cube((5, -13, 2)), Cube((5, -13, 1)),
    Cube((0, -13, 0)), Cube((0, -13, 1)), Cube((0, -13, 2)), Cube((0, -13, 3)), Cube((0, -13, 4)),
    Cube((6, -13, 1)), Cube((6, -13, 2)),

    #red hat 2nd bottom layer
    Cube((1, -14, 0)), Cube((2, -14, 0)), Cube((3, -14, 0)), Cube((4, -14, 0)),
    Cube((1, -14, 4)), Cube((2, -14, 4)), Cube((3, -14, 4)), Cube((4, -14, 4)),
    Cube((1, -14, 1)), Cube((1, -14, 2)), Cube((1, -14, 3)),
    Cube((5, -14, 1)), Cube((5, -14, 2)), Cube((4, -14, 3)),
    Cube((6, -14, 1)), Cube((6, -14, 2)),

    #red hat 3rd layer
    Cube((2, -15, 1)), Cube((2, -15, 2)), Cube((2, -15, 3)),
    Cube((3, -15, 1)), Cube((3, -15, 2)), Cube((3, -15, 3)),
    Cube((4, -15, 1)), Cube((4, -15, 2)), Cube((4, -15, 3)),
    Cube((5, -15, 1)), Cube((5, -15, 2)),

    #4th row above belt
    Cube((-1, -7, 4)), Cube((0, -7, 4)), Cube((6, -7, 4)), Cube((5, -7, 4)),
    Cube((6, -7, 3)), Cube((6, -7, 2)), Cube((6, -7, 1)),
    Cube((7, -7, 3)), Cube((7, -7, 2)), Cube((7, -7, 1)),
    Cube((-2, -7, 1)), Cube((-2, -7, 2)), Cube((-2, -7, 3)),

    Cube((-2, -6, 0)), Cube((-2, -6, 1)), Cube((-2, -6, 2)),

]
black_cubes = [
    #right foot
    Cube((0, 0, 0)), Cube((0, 0, 1)), Cube((0, 0, 2)), Cube((0, 0, 3)), Cube((1, 0, 0)), Cube((1, 0, 1)),
    Cube((1, 0, 2)), Cube((1, 0, 3)),

    #left foot
    Cube((4, 0, 0)), Cube((4, 0, 1)), Cube((4, 0, 2)), Cube((4, 0, 3)), Cube((5, 0, 0)), Cube((5, 0, 1)),
    Cube((5, 0, 2)), Cube((5, 0, 3)),

    #belt
    Cube((-1, -3, -1)), Cube((-1, -3, 0)), Cube((-1, -3, 1)), Cube((-1, -3, 2)), Cube((-1, -3, 3)), Cube((-1, -3, 4)),
    Cube((6, -3, -1)), Cube((6, -3, 0)), Cube((6, -3, 1)), Cube((6, -3, 2)), Cube((6, -3, 3)), Cube((6, -3, 4)),
    Cube((0, -3, -1)), Cube((1, -3, -1)), Cube((2, -3, -1)), Cube((3, -3, -1)), Cube((4, -3, -1)), Cube((5, -3, -1)),
    Cube((0, -3, 5)), Cube((1, -3, 5)), Cube((2, -3, 5)), Cube((3, -3, 5)), Cube((4, -3, 5)), Cube((5, -3, 5)),

    #eyes
    Cube((1, -10, 0)), Cube((4, -10, 0))
]
white_cubes = [
    #bottom layer beard
    Cube((2, -5, -1)), Cube((3, -5, -1)),

    #second bottom layer beard
    Cube((2, -6, -1)), Cube((3, -6, -1)), Cube((0, -6, -1)), Cube((1, -6, -1)), Cube((4, -6, -1)), Cube((5, -6, -1)),

    #third bottom layer beard
    Cube((1, -7, -1)), Cube((4, -7, -1)), Cube((-1, -7, -1)), Cube((6, -7, -1)), Cube((0, -7, 0)), Cube((5, -7, 0)),
    Cube((1, -7, 5)), Cube((2, -7, 5)), Cube((3, -7, 5)), Cube((4, -7, 5)), Cube((6, -7, 0)), Cube((-1, -7, 0)),

    #forth bottom layer beard
    Cube((4, -8, -1)), Cube((1, -8, -1)), Cube((0, -8, -1)), Cube((5, -8, -1)), Cube((2, -8, -1)), Cube((3, -8, -1)),
    Cube((0, -8, 0)), Cube((5, -8, 0)), Cube((1, -8, 5)), Cube((2, -8, 5)), Cube((3, -8, 5)), Cube((4, -8, 5)),
    Cube((0, -8, 5)), Cube((5, -8, 5)), Cube((6, -8, 4)), Cube((6, -8, 3)), Cube((6, -8, 2)), Cube((6, -8, 1)),
    Cube((-1, -8, 1)), Cube((-1, -8, 2)), Cube((-1, -8, 3)), Cube((-1, -8, 4)),

    #fifth bottom layer beard
    Cube((0, -9, -1)), Cube((5, -9, -1)), Cube((0, -9, 5)), Cube((5, -9, 5)), Cube((-1, -9, 5)), Cube((6, -9, 5)),
    Cube((1, -9, 6)), Cube((2, -9, 6)), Cube((3, -9, 6)), Cube((4, -9, 6)),
    Cube((7, -9, 4)), Cube((7, -9, 3)), Cube((7, -9, 2)), Cube((7, -9, 1)), Cube((6, -9, 0)),
    Cube((-2, -9, 1)), Cube((-2, -9, 2)), Cube((-2, -9, 3)), Cube((-2, -9, 4)), Cube((-1, -9, 0)),

    #sixth bottom layer beard
    Cube((0, -10, 5)), Cube((5, -10, 5)), Cube((-1, -10, 5)), Cube((6, -10, 5)),
    Cube((1, -10, 6)), Cube((2, -10, 6)), Cube((3, -10, 6)), Cube((4, -10, 6)),
    Cube((7, -10, 4)), Cube((7, -10, 3)), Cube((7, -10, 2)), Cube((7, -10, 1)), Cube((6, -10, 0)),
    Cube((6, -10, 4)), Cube((6, -10, 3)), Cube((6, -10, 2)), Cube((6, -10, 1)),
    Cube((-2, -10, 1)), Cube((-2, -10, 2)), Cube((-2, -10, 3)), Cube((-2, -10, 4)), Cube((-1, -10, 0)),

    #seventh bottom layer beard
    Cube((0, -11, 5)), Cube((5, -11, 5)), Cube((1, -11, 6)), Cube((2, -11, 6)), Cube((3, -11, 6)), Cube((4, -11, 6)),
    Cube((5, -11, 0)), Cube((0, -11, 0)), Cube((5, -11, 4)), Cube((5, -11, 3)), Cube((5, -11, 2)), Cube((5, -11, 1)),
    Cube((6, -11, 3)), Cube((6, -11, 2)), Cube((6, -11, 1)), Cube((6, -11, 4)),
    Cube((-1, -11, 1)), Cube((-1, -11, 2)), Cube((-1, -11, 3)), Cube((-1, -11, 4)),

    #eighth bottom layer beard
    Cube((1, -12, 5)), Cube((2, -12, 5)), Cube((3, -12, 5)), Cube((4, -12, 5)),
    Cube((5, -12, 4)), Cube((5, -12, 3)), Cube((5, -12, 2)), Cube((5, -12, 1)),
    Cube((0, -12, 0)), Cube((0, -12, 1)), Cube((0, -12, 2)), Cube((0, -12, 3)), Cube((0, -12, 4)),

    #white ball above hat
    Cube((7, -13, 1)), Cube((7, -13, 2)), Cube((8, -13, 1)), Cube((8, -13, 2)),
    Cube((7, -12, 1)), Cube((7, -12, 2)), Cube((8, -12, 1)), Cube((8, -12, 2)),


    #Santa hat bottom layer
    Cube((0, -11, -1)), Cube((5, -11, -1)),

    #Santa hat 2nd bottom layer
    Cube((1, -12, -1)), Cube((2, -12, -1)), Cube((3, -12, -1)), Cube((4, -12, -1)), Cube((5, -12, 0)),

    #belt layer
    Cube((7, -3, 1)), Cube((7, -3, 2)), Cube((10, -3, 1)), Cube((10, -3, 2)), Cube((8, -3, 3)), Cube((9, -3, 3)),
    Cube((8, -3, 0)), Cube((9, -3, 0)),
    Cube((-2, -3, 1)), Cube((-2, -3, 2)), Cube((-5, -3, 1)), Cube((-5, -3, 2)), Cube((-4, -3, 3)), Cube((-3, -3, 3)),
    Cube((-4, -3, 0)), Cube((-3, -3, 0)),

]
pink_cubes = [
    #Lips
    Cube((2, -7, -1)), Cube((3, -7, -1))
]
beige_cubes = [
    #nose layer
    Cube((2, -9, -1)), Cube((3, -9, -1)), Cube((2, -9, -2)), Cube((3, -9, -2)), Cube((2, -9, 0)), Cube((3, -9, 0)),
    Cube((1, -9, 0)), Cube((4, -9, 0)),

    #Skin layer between eyes
    Cube((2, -10, 0)), Cube((3, -10, 0)), Cube((0, -10, 0)), Cube((5, -10, 0)),

    #Skin layer above eyes
    Cube((1, -11, 0)), Cube((2, -11, 0)), Cube((3, -11, 0)), Cube((4, -11, 0)),

    #left hand
    Cube((8, -2, 1)), Cube((8, -2, 2)), Cube((9, -2, 1)), Cube((9, -2, 2)),

    #right hand
    Cube((-3, -2, 1)), Cube((-3, -2, 2)), Cube((-4, -2, 1)), Cube((-4, -2, 2)),
]
yellow_cubes = [Cube((2, -3, -2)), Cube((3, -3, -2))]

while True:
    dt = clock.tick()/1000

    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        cam.events(event)

    screen.fill((211, 211, 211))

    face_list = []
    face_color = []
    depth = []

    for obj in red_cubes:
        for edge in obj.edges:
            points = []
            for x, y, z in (obj.verts[edge[0]], obj.verts[edge[1]]):
                x -= cam.pos[0]
                y -= cam.pos[1]
                z -= cam.pos[2]

                x, z = rotate2d((x, z), cam.rot[1])
                y, z = rotate2d((y, z), cam.rot[0])

                f = 400/z
                x, y = x*f, y*f
                points += [(cx + int(x), cy + int(y))]
            pygame.draw.line(screen, (0, 0, 0), points[0], points[1], 5)

        screen_coords= []
        vert_list = []
        for x, y, z in obj.verts:
            x -= cam.pos[0]
            y -= cam.pos[1]
            z -= cam.pos[2]
            x, z = rotate2d((x, z), cam.rot[1])
            y, z = rotate2d((y, z), cam.rot[0])
            vert_list += [(x, y, z)]

            f = 400 / z
            x, y = x * f, y * f
            screen_coords += [(cx + int(x), cy + int(y))]

        for f in range(len(obj.faces)):
            face = obj.faces[f]
            on_screen = False
            for i in face:
                x, y = screen_coords[i]
                if vert_list[i][2] > 0 and x > 0 and x < w and y > 0 and y < h:
                    on_screen = True
                    break
            if on_screen:
                coords = [screen_coords[i] for i in face]
                face_list += [coords]
                face_color += [red[f]]

                depth += [sum(sum(vert_list[j][i] for j in face)**2 for i in range(3))]

    for obj in black_cubes:
        for edge in obj.edges:
            points = []
            for x, y, z in (obj.verts[edge[0]], obj.verts[edge[1]]):
                x -= cam.pos[0]
                y -= cam.pos[1]
                z -= cam.pos[2]

                x, z = rotate2d((x, z), cam.rot[1])
                y, z = rotate2d((y, z), cam.rot[0])

                f = 400/z
                x, y = x*f, y*f
                points += [(cx + int(x), cy + int(y))]
            pygame.draw.line(screen, (0, 0, 0), points[0], points[1], 5)

        screen_coords= []
        vert_list = []
        for x, y, z in obj.verts:
            x -= cam.pos[0]
            y -= cam.pos[1]
            z -= cam.pos[2]
            x, z = rotate2d((x, z), cam.rot[1])
            y, z = rotate2d((y, z), cam.rot[0])
            vert_list += [(x, y, z)]

            f = 400 / z
            x, y = x * f, y * f
            screen_coords += [(cx + int(x), cy + int(y))]

        for f in range(len(obj.faces)):
            face = obj.faces[f]
            on_screen = False
            for i in face:
                x, y = screen_coords[i]
                if vert_list[i][2] > 0 and x > 0 and x < w and y > 0 and y < h:
                    on_screen = True
                    break
            if on_screen:
                coords = [screen_coords[i] for i in face]
                face_list += [coords]
                face_color += [black[f]]

                depth += [sum(sum(vert_list[j][i] for j in face)**2 for i in range(3))]

    for obj in white_cubes:
        for edge in obj.edges:
            points = []
            for x, y, z in (obj.verts[edge[0]], obj.verts[edge[1]]):
                x -= cam.pos[0]
                y -= cam.pos[1]
                z -= cam.pos[2]

                x, z = rotate2d((x, z), cam.rot[1])
                y, z = rotate2d((y, z), cam.rot[0])

                f = 400/z
                x, y = x*f, y*f
                points += [(cx + int(x), cy + int(y))]
            pygame.draw.line(screen, (0, 0, 0), points[0], points[1], 5)

        screen_coords= []
        vert_list = []
        for x, y, z in obj.verts:
            x -= cam.pos[0]
            y -= cam.pos[1]
            z -= cam.pos[2]
            x, z = rotate2d((x, z), cam.rot[1])
            y, z = rotate2d((y, z), cam.rot[0])
            vert_list += [(x, y, z)]

            f = 400 / z
            x, y = x * f, y * f
            screen_coords += [(cx + int(x), cy + int(y))]

        for f in range(len(obj.faces)):
            face = obj.faces[f]
            on_screen = False
            for i in face:
                x, y = screen_coords[i]
                if vert_list[i][2] > 0 and x > 0 and x < w and y > 0 and y < h:
                    on_screen = True
                    break
            if on_screen:
                coords = [screen_coords[i] for i in face]
                face_list += [coords]
                face_color += [white[f]]

                depth += [sum(sum(vert_list[j][i] for j in face)**2 for i in range(3))]

    for obj in beige_cubes:
        for edge in obj.edges:
            points = []
            for x, y, z in (obj.verts[edge[0]], obj.verts[edge[1]]):
                x -= cam.pos[0]
                y -= cam.pos[1]
                z -= cam.pos[2]

                x, z = rotate2d((x, z), cam.rot[1])
                y, z = rotate2d((y, z), cam.rot[0])

                f = 400/z
                x, y = x*f, y*f
                points += [(cx + int(x), cy + int(y))]
            pygame.draw.line(screen, (0, 0, 0), points[0], points[1], 5)

        screen_coords= []
        vert_list = []
        for x, y, z in obj.verts:
            x -= cam.pos[0]
            y -= cam.pos[1]
            z -= cam.pos[2]
            x, z = rotate2d((x, z), cam.rot[1])
            y, z = rotate2d((y, z), cam.rot[0])
            vert_list += [(x, y, z)]

            f = 400 / z
            x, y = x * f, y * f
            screen_coords += [(cx + int(x), cy + int(y))]

        for f in range(len(obj.faces)):
            face = obj.faces[f]
            on_screen = False
            for i in face:
                x, y = screen_coords[i]
                if vert_list[i][2] > 0 and x > 0 and x < w and y > 0 and y < h:
                    on_screen = True
                    break
            if on_screen:
                coords = [screen_coords[i] for i in face]
                face_list += [coords]
                face_color += [beige[f]]

                depth += [sum(sum(vert_list[j][i] for j in face)**2 for i in range(3))]

    for obj in pink_cubes:
        for edge in obj.edges:
            points = []
            for x, y, z in (obj.verts[edge[0]], obj.verts[edge[1]]):
                x -= cam.pos[0]
                y -= cam.pos[1]
                z -= cam.pos[2]

                x, z = rotate2d((x, z), cam.rot[1])
                y, z = rotate2d((y, z), cam.rot[0])

                f = 400/z
                x, y = x*f, y*f
                points += [(cx + int(x), cy + int(y))]
            pygame.draw.line(screen, (0, 0, 0), points[0], points[1], 5)

        screen_coords= []
        vert_list = []
        for x, y, z in obj.verts:
            x -= cam.pos[0]
            y -= cam.pos[1]
            z -= cam.pos[2]
            x, z = rotate2d((x, z), cam.rot[1])
            y, z = rotate2d((y, z), cam.rot[0])
            vert_list += [(x, y, z)]

            f = 400 / z
            x, y = x * f, y * f
            screen_coords += [(cx + int(x), cy + int(y))]

        for f in range(len(obj.faces)):
            face = obj.faces[f]
            on_screen = False
            for i in face:
                x, y = screen_coords[i]
                if vert_list[i][2] > 0 and x > 0 and x < w and y > 0 and y < h:
                    on_screen = True
                    break
            if on_screen:
                coords = [screen_coords[i] for i in face]
                face_list += [coords]
                face_color += [pink[f]]

                depth += [sum(sum(vert_list[j][i] for j in face)**2 for i in range(3))]

    for obj in yellow_cubes:
        for edge in obj.edges:
            points = []
            for x, y, z in (obj.verts[edge[0]], obj.verts[edge[1]]):
                x -= cam.pos[0]
                y -= cam.pos[1]
                z -= cam.pos[2]

                x, z = rotate2d((x, z), cam.rot[1])
                y, z = rotate2d((y, z), cam.rot[0])

                f = 400/z
                x, y = x*f, y*f
                points += [(cx + int(x), cy + int(y))]
            pygame.draw.line(screen, (0, 0, 0), points[0], points[1], 5)

        screen_coords= []
        vert_list = []
        for x, y, z in obj.verts:
            x -= cam.pos[0]
            y -= cam.pos[1]
            z -= cam.pos[2]
            x, z = rotate2d((x, z), cam.rot[1])
            y, z = rotate2d((y, z), cam.rot[0])
            vert_list += [(x, y, z)]

            f = 400 / z
            x, y = x * f, y * f
            screen_coords += [(cx + int(x), cy + int(y))]

        for f in range(len(obj.faces)):
            face = obj.faces[f]
            on_screen = False
            for i in face:
                x, y = screen_coords[i]
                if vert_list[i][2] > 0 and x > 0 and x < w and y > 0 and y < h:
                    on_screen = True
                    break
            if on_screen:
                coords = [screen_coords[i] for i in face]
                face_list += [coords]
                face_color += [yellow[f]]

                depth += [sum(sum(vert_list[j][i] for j in face)**2 for i in range(3))]




    order = sorted(range(len(face_list)), key=lambda i: depth[i], reverse = 1)

    for i in order:
        try:
            pygame.draw.polygon(screen, face_color[i], face_list[i])
        except:
            pass

    pygame.display.flip()

    key = pygame.key.get_pressed()
    cam.update(dt, key)
