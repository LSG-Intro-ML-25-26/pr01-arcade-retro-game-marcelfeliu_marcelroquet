def on_button_multiplayer_a_pressed():
    global p2, vx, vy, ProjectileP2
    if mp.is_button_pressed(mp.player_selector(mp.PlayerNumber.TWO),
        mp.MultiplayerButton.B):
        pass
    elif mp.is_button_pressed(mp.player_selector(mp.PlayerNumber.TWO),
        mp.MultiplayerButton.A):
        p2 = mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO))
        vx = p2.vx
        vy = p2.vy
        if abs(vx) > abs(vy):
            if vx > 0:
                ProjectileP2 = sprites.create_projectile_from_sprite(img("""
                        . . . . . b b b b b b . . . . .
                        . . . b b 9 9 9 9 9 9 b b . . .
                        . . b b 9 9 9 9 9 9 9 9 b b . .
                        . b b 9 d 9 9 9 9 9 9 9 9 b b .
                        . b 9 d 9 9 9 9 9 1 1 1 9 9 b .
                        b 9 d d 9 9 9 9 9 1 1 1 9 9 9 b
                        b 9 d 9 9 9 9 9 9 1 1 1 9 9 9 b
                        b 9 3 9 9 9 9 9 9 9 9 9 1 9 9 b
                        b 5 3 d 9 9 9 9 9 9 9 9 9 9 9 b
                        b 5 3 3 9 9 9 9 9 9 9 9 9 d 9 b
                        b 5 d 3 3 9 9 9 9 9 9 9 d d 9 b
                        . b 5 3 3 3 d 9 9 9 9 d d 5 b .
                        . b d 5 3 3 3 3 3 3 3 d 5 b b .
                        . . b d 5 d 3 3 3 3 5 5 b b . .
                        . . . b b 5 5 5 5 5 5 b b . . .
                        . . . . . b b b b b b . . . . .
                        """),
                    p2,
                    50,
                    0)
            else:
                ProjectileP2 = sprites.create_projectile_from_sprite(img("""
                        . . . . . b b b b b b . . . . .
                        . . . b b 9 9 9 9 9 9 b b . . .
                        . . b b 9 9 9 9 9 9 9 9 b b . .
                        . b b 9 d 9 9 9 9 9 9 9 9 b b .
                        . b 9 d 9 9 9 9 9 1 1 1 9 9 b .
                        b 9 d d 9 9 9 9 9 1 1 1 9 9 9 b
                        b 9 d 9 9 9 9 9 9 1 1 1 9 9 9 b
                        b 9 3 9 9 9 9 9 9 9 9 9 1 9 9 b
                        b 5 3 d 9 9 9 9 9 9 9 9 9 9 9 b
                        b 5 3 3 9 9 9 9 9 9 9 9 9 d 9 b
                        b 5 d 3 3 9 9 9 9 9 9 9 d d 9 b
                        . b 5 3 3 3 d 9 9 9 9 d d 5 b .
                        . b d 5 3 3 3 3 3 3 3 d 5 b b .
                        . . b d 5 d 3 3 3 3 5 5 b b . .
                        . . . b b 5 5 5 5 5 5 b b . . .
                        . . . . . b b b b b b . . . . .
                        """),
                    p2,
                    -50,
                    0)
        elif vy > 0:
            ProjectileP2 = sprites.create_projectile_from_sprite(img("""
                    . . . . . b b b b b b . . . . .
                    . . . b b 9 9 9 9 9 9 b b . . .
                    . . b b 9 9 9 9 9 9 9 9 b b . .
                    . b b 9 d 9 9 9 9 9 9 9 9 b b .
                    . b 9 d 9 9 9 9 9 1 1 1 9 9 b .
                    b 9 d d 9 9 9 9 9 1 1 1 9 9 9 b
                    b 9 d 9 9 9 9 9 9 1 1 1 9 9 9 b
                    b 9 3 9 9 9 9 9 9 9 9 9 1 9 9 b
                    b 5 3 d 9 9 9 9 9 9 9 9 9 9 9 b
                    b 5 3 3 9 9 9 9 9 9 9 9 9 d 9 b
                    b 5 d 3 3 9 9 9 9 9 9 9 d d 9 b
                    . b 5 3 3 3 d 9 9 9 9 d d 5 b .
                    . b d 5 3 3 3 3 3 3 3 d 5 b b .
                    . . b d 5 d 3 3 3 3 5 5 b b . .
                    . . . b b 5 5 5 5 5 5 b b . . .
                    . . . . . b b b b b b . . . . .
                    """),
                p2,
                0,
                50)
        else:
            ProjectileP2 = sprites.create_projectile_from_sprite(img("""
                    . . . . . b b b b b b . . . . .
                    . . . b b 9 9 9 9 9 9 b b . . .
                    . . b b 9 9 9 9 9 9 9 9 b b . .
                    . b b 9 d 9 9 9 9 9 9 9 9 b b .
                    . b 9 d 9 9 9 9 9 1 1 1 9 9 b .
                    b 9 d d 9 9 9 9 9 1 1 1 9 9 9 b
                    b 9 d 9 9 9 9 9 9 1 1 1 9 9 9 b
                    b 9 3 9 9 9 9 9 9 9 9 9 1 9 9 b
                    b 5 3 d 9 9 9 9 9 9 9 9 9 9 9 b
                    b 5 3 3 9 9 9 9 9 9 9 9 9 d 9 b
                    b 5 d 3 3 9 9 9 9 9 9 9 d d 9 b
                    . b 5 3 3 3 d 9 9 9 9 d d 5 b .
                    . b d 5 3 3 3 3 3 3 3 d 5 b b .
                    . . b d 5 d 3 3 3 3 5 5 b b . .
                    . . . b b 5 5 5 5 5 5 b b . . .
                    . . . . . b b b b b b . . . . .
                    """),
                p2,
                0,
                -50)
mp.on_button_event(mp.MultiplayerButton.A,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_a_pressed)

def on_up_pressed():
    pass
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_left_pressed():
    pass
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_button_multiplayer_b_pressed():
    global p1, vx, vy, ProjectileP1
    if mp.is_button_pressed(mp.player_selector(mp.PlayerNumber.ONE),
        mp.MultiplayerButton.A):
        pass
    elif mp.is_button_pressed(mp.player_selector(mp.PlayerNumber.ONE),
        mp.MultiplayerButton.B):
        p1 = mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE))
        vx = p1.vx
        vy = p1.vy
        if abs(vx) > abs(vy):
            if vx > 0:
                ProjectileP1 = sprites.create_projectile_from_sprite(img("""
                        . . . . . . . c c c a c . . . .
                        . . c c b b b a c a a a c . . .
                        . c c a b a c b a a a b c c . .
                        . c a b c f f f b a b b b a . .
                        . c a c f f f 8 a b b b b b a .
                        . c a 8 f f 8 c a b b b b b a .
                        c c c a c c c c a b c f a b c c
                        c c a a a c c c a c f f c b b a
                        c c a b 6 a c c a f f c c b b a
                        c a b c 8 6 c c a a a b b c b c
                        c a c f f a c c a f a c c c b .
                        c a 8 f c c b a f f c b c c c .
                        . c b c c c c b f c a b b a c .
                        . . a b b b b b b b b b b b c .
                        . . . c c c c b b b b b c c . .
                        . . . . . . . . c b b c . . . .
                        """),
                    p1,
                    50,
                    0)
            else:
                ProjectileP1 = sprites.create_projectile_from_sprite(img("""
                        . . . . . . . c c c a c . . . .
                        . . c c b b b a c a a a c . . .
                        . c c a b a c b a a a b c c . .
                        . c a b c f f f b a b b b a . .
                        . c a c f f f 8 a b b b b b a .
                        . c a 8 f f 8 c a b b b b b a .
                        c c c a c c c c a b c f a b c c
                        c c a a a c c c a c f f c b b a
                        c c a b 6 a c c a f f c c b b a
                        c a b c 8 6 c c a a a b b c b c
                        c a c f f a c c a f a c c c b .
                        c a 8 f c c b a f f c b c c c .
                        . c b c c c c b f c a b b a c .
                        . . a b b b b b b b b b b b c .
                        . . . c c c c b b b b b c c . .
                        . . . . . . . . c b b c . . . .
                        """),
                    p1,
                    -50,
                    0)
        elif vy > 0:
            ProjectileP1 = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . c c c a c . . . .
                    . . c c b b b a c a a a c . . .
                    . c c a b a c b a a a b c c . .
                    . c a b c f f f b a b b b a . .
                    . c a c f f f 8 a b b b b b a .
                    . c a 8 f f 8 c a b b b b b a .
                    c c c a c c c c a b c f a b c c
                    c c a a a c c c a c f f c b b a
                    c c a b 6 a c c a f f c c b b a
                    c a b c 8 6 c c a a a b b c b c
                    c a c f f a c c a f a c c c b .
                    c a 8 f c c b a f f c b c c c .
                    . c b c c c c b f c a b b a c .
                    . . a b b b b b b b b b b b c .
                    . . . c c c c b b b b b c c . .
                    . . . . . . . . c b b c . . . .
                    """),
                p1,
                0,
                50)
        else:
            ProjectileP1 = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . c c c a c . . . .
                    . . c c b b b a c a a a c . . .
                    . c c a b a c b a a a b c c . .
                    . c a b c f f f b a b b b a . .
                    . c a c f f f 8 a b b b b b a .
                    . c a 8 f f 8 c a b b b b b a .
                    c c c a c c c c a b c f a b c c
                    c c a a a c c c a c f f c b b a
                    c c a b 6 a c c a f f c c b b a
                    c a b c 8 6 c c a a a b b c b c
                    c a c f f a c c a f a c c c b .
                    c a 8 f c c b a f f c b c c c .
                    . c b c c c c b f c a b b a c .
                    . . a b b b b b b b b b b b c .
                    . . . c c c c b b b b b c c . .
                    . . . . . . . . c b b c . . . .
                    """),
                p1,
                0,
                -50)
mp.on_button_event(mp.MultiplayerButton.B,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_b_pressed)

def on_right_pressed():
    pass
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    pass
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

ProjectileP1: Sprite = None
ProjectileP2: Sprite = None
vy = 0
vx = 0
p2: Sprite = None
p1: Sprite = None
p22 = None
vx2 = 0
vy2 = 0
tiles.set_current_tilemap(tilemap("""
    level1
    """))
p1 = sprites.create(assets.image("""
    nena-front
    """), SpriteKind.player)
p2 = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . f f f f . . . . . .
        . . . . f f f 2 2 f f f . . . .
        . . . f f f 2 2 2 2 f f f . . .
        . . f f f e e e e e e f f f . .
        . . f e e 2 2 2 2 2 2 e f f . .
        . f f e 2 f f f f f f 2 e f f .
        . f f f f f e e e e f f f f f .
        . . f e f b f 4 4 f b f e f . .
        . . f e 4 1 f d d f 1 4 e f . .
        . . e f f f f d d d 4 e f . . .
        . . f d d d d f 2 2 2 f e f . .
        . . f b b b b f 2 2 2 f 4 e . .
        . . f b b b b f 5 4 4 f . . . .
        . . . f c c f f f f f f . . . .
        . . . . f f . . . f f f . . . .
        """),
    SpriteKind.player)
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.ONE), p1)
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.TWO), p2)
mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.ONE), 100, 100)
mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.TWO), 100, 100)
scene.camera_follow_sprite(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)))
scene.camera_follow_sprite(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)))
mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)).set_stay_in_screen(True)
mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)).set_stay_in_screen(True)

def on_on_update():
    scene.center_camera_at((mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)).x + mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)).x) / 2,
        (mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)).y + mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)).y) / 2)
game.on_update(on_on_update)
