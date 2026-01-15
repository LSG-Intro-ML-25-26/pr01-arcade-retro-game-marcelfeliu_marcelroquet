def on_up_pressed():
    global lookUp, lookDown, lookLeft, lookRight
    lookUp = True
    lookDown = False
    lookLeft = False
    lookRight = False
    animation.run_image_animation(
        player1,
        assets.animation("""nena-animation-up"""),
        500,
        False
    )

controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)


def on_b_pressed():
    global ProjectileP2
    ProjectileP2 = sprites.create_projectile_from_sprite(
        img("""
        . . . . . b b b b b b . . . . .
        . . . . b b 9 9 9 9 9 9 b b . .
        . . . . b b 9 9 9 9 9 9 9 9 b b
        . . . b b 9 d 9 9 9 9 9 9 9 9 b b
        . . b 9 d 9 9 9 9 9 1 1 1 9 9 b .
        b 9 d d 9 9 9 9 9 1 1 1 9 9 9 b
        b 9 d 9 9 9 9 9 9 1 1 1 9 9 9 b
        b 9 3 9 9 9 9 9 9 9 9 1 9 9 b
        b 5 3 d 9 9 9 9 9 9 9 9 9 9 9 b
        b 5 3 3 9 9 9 9 9 9 9 9 9 d 9 b
        b 5 d 3 3 9 9 9 9 9 9 9 d d 9 b
        . b 5 3 3 3 d 9 9 9 9 d d 5 b .
        . . b d 5 3 3 3 3 3 3 3 d 5 b b
        . . . b d 5 d 3 3 3 3 5 5 b b
        . . . . b b 5 5 5 5 5 5 b b
        . . . . . . b b b b b b . .
        """),
        player2,
        -60,
        50
    )

controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)


def on_a_pressed():
    checkDirection()

controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)


def on_left_pressed():
    global lookUp, lookDown, lookLeft, lookRight
    lookUp = False
    lookDown = False
    lookLeft = True
    lookRight = False
    animation.run_image_animation(
        player1,
        assets.animation("""nena-animation-left"""),
        500,
        False
    )

controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)


def checkDirection():
    global ProjectileP1

    if lookDown:
        ProjectileP1 = sprites.create_projectile_from_sprite(img("""..."""), player1, 0, 50)
    elif lookUp:
        ProjectileP1 = sprites.create_projectile_from_sprite(img("""..."""), player1, 0, -50)
    elif lookLeft:
        ProjectileP1 = sprites.create_projectile_from_sprite(img("""..."""), player1, -50, 0)
    elif lookRight:
        ProjectileP1 = sprites.create_projectile_from_sprite(img("""..."""), player1, 50, 0)
    else:
        pass


def on_right_pressed():
    global lookUp, lookDown, lookLeft, lookRight
    lookUp = False
    lookDown = False
    lookLeft = False
    lookRight = True
    animation.run_image_animation(
        player1,
        assets.animation("""nena-animation-right"""),
        500,
        False
    )

controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)


def on_down_pressed():
    global lookUp, lookDown, lookLeft, lookRight
    lookUp = False
    lookDown = True
    lookLeft = False
    lookRight = False
    animation.run_image_animation(
        player1,
        assets.animation("""nena-animation-down"""),
        500,
        False
    )

controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)


ProjectileP1: Sprite = None
ProjectileP2: Sprite = None

lookRight = False
lookLeft = False
lookDown = False
lookUp = False

player2: Sprite = None
player1: Sprite = None


tiles.set_current_tilemap(tilemap("""level1"""))

player1 = sprites.create(assets.image("""nena-front"""), SpriteKind.player)
player2 = sprites.create(img("""..."""), SpriteKind.player)

controller.player1.move_sprite(player1)
controller.player2.move_sprite(player2)

scene.camera_follow_sprite(player1)
scene.camera_follow_sprite(player2)

player1.set_stay_in_screen(True)
player2.set_stay_in_screen(True)


def on_on_update():
    scene.center_camera_at(
        (player1.x + player2.x) / 2,
        (player1.y + player2.y) / 2
    )

game.on_update(on_on_update)


def on_forever():
    effects.star_field.start_screen_effect()

forever(on_forever)
