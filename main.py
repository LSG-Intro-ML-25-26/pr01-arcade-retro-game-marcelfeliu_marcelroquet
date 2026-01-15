
lookUp = False
lookDown = False
lookLeft = False
lookRight = False

ProjectileP1: Sprite = None
ProjectileP2: Sprite = None

player1: Sprite = None
player2: Sprite = None



def on_up_pressed():
    global lookUp
    lookUp = True
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_up_released():
    global lookUp
    lookUp = False
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def on_down_pressed():
    global lookDown
    lookDown = True
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_down_released():
    global lookDown
    lookDown = False
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

def on_left_pressed():
    global lookLeft
    lookLeft = True
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_left_released():
    global lookLeft
    lookLeft = False
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_right_pressed():
    global lookRight
    lookRight = True
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_right_released():
    global lookRight
    lookRight = False
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)



def checkDirection():
    global ProjectileP1

    vx = 0
    vy = 0
    speed = 60

    if lookUp:
        vy -= speed
    if lookDown:
        vy += speed
    if lookLeft:
        vx -= speed
    if lookRight:
        vx += speed

    if vx == 0 and vy == 0:
        return

    ProjectileP1 = sprites.create_projectile_from_sprite(
        img("""
            . . . . . c c 8 8 c c . . . .
            . . . c c f f f f f c c . . .
            . . c f f f a a a f f f c . .
            . c f f a a a a a a f f c . .
            . c f a a a c c c a a f c . .
            c f f a a c c c c a a f f c .
            c f f a a c c c c a a f f c .
            . c f a a a c c c a a f c . .
            . c f f a a a a a a f f c . .
            . . c f f f a a a f f f c . .
            . . . c c f f f f f c c . . .
            . . . . . c c 8 8 c c . . . .
        """),
        player1,
        vx,
        vy
    )

def on_a_pressed():
    checkDirection()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)



def on_b_pressed():
    global ProjectileP2
    ProjectileP2 = sprites.create_projectile_from_sprite(
        img("""
            . . . . . b b b b b . . . . .
            . . . b b 9 9 9 9 9 b b . . .
            . . b 9 9 9 9 9 9 9 9 b . . .
            . b 9 9 9 9 9 9 9 9 9 b . . .
            . b 9 9 9 9 9 9 9 9 9 b . . .
            b 9 9 9 9 9 9 9 9 9 9 b . . .
            . b 9 9 9 9 9 9 9 9 9 b . . .
            . . b 9 9 9 9 9 9 9 9 b . . .
            . . . b b 9 9 9 9 9 b b . . .
            . . . . . b b b b b . . . . .
        """),
        player2,
        -60,
        0
    )
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)



tiles.set_current_tilemap(tilemap("""
    level1
"""))

player1 = sprites.create(
    assets.image("nena-front"),
    SpriteKind.player
)

player2 = sprites.create(
    img("""
        . . . . f f f f . . . .
        . . f f 2 2 2 2 f f . .
        . f f 2 2 2 2 2 2 f f .
        . f e e e e e e e e f .
        f e 2 f f f f f f 2 e f
        f f f f e e e e f f f f
        . f e f b f 4 4 f b f e
        . f e 4 1 f d d f 1 4 e
        . e f f f f d d d 4 e f
        . f d d d d f 2 2 2 f e
        . f b b b b f 2 2 2 f 4
        . . f c c f f f f f f .
    """),
    SpriteKind.player
)

controller.player1.move_sprite(player1)
controller.player2.move_sprite(player2)

player1.set_stay_in_screen(True)
player2.set_stay_in_screen(True)

scene.camera_follow_sprite(player1)



def on_update():
    scene.center_camera_at(
        (player1.x + player2.x) / 2,
        (player1.y + player2.y) / 2
    )
game.on_update(on_update)



effects.star_field.start_screen_effect()
