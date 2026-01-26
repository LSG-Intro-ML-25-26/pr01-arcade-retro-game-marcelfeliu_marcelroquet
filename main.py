def on_on_overlap(projectile, player2):
    global vida_p1, vida_p2
    if projectile == ProjectileP1 and player2 == p1:
        return
    if projectile == ProjectileP2 and player2 == p2:
        return
    projectile.destroy()
    if player2 == p1:
        vida_p1 += 0 - 1
        status_p1.value = vida_p1
        player2.start_effect(effects.fire, 200)
        if vida_p1 <= 0:
            p1.destroy(effects.disintegrate, 500)
            game.over(False)
    elif player2 == p2:
        vida_p2 += 0 - 1
        status_p2.value = vida_p2
        player2.start_effect(effects.fire, 200)
        if vida_p2 <= 0:
            p2.destroy(effects.disintegrate, 500)
            game.over(False)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap)

def on_up_pressed():
    pass
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_button_multiplayer_b_pressed(player23):
    global now, ultimo_disparo_p1, disparo_p12, p1, vx, vy, ProjectileP1
    now = game.runtime()
    if now - ultimo_disparo_p1 < cooldown_disparo:
        return
    ultimo_disparo_p1 = now
    disparo_p12 = True
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
                    velocidad_proyectil,
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
                    0 - velocidad_proyectil,
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
                velocidad_proyectil)
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
                0 - velocidad_proyectil)
mp.on_button_event(mp.MultiplayerButton.B,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_b_pressed)

def on_left_pressed():
    pass
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_button_multiplayer_a_pressed(player22):
    global now2, ultimo_disparo_p2, disparo_p23, p2, vx, vy, ProjectileP2
    now2 = game.runtime()
    if now2 - ultimo_disparo_p2 < cooldown_disparo:
        return
    ultimo_disparo_p2 = now2
    disparo_p23 = True
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
                    velocidad_proyectil,
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
                    0 - velocidad_proyectil,
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
                velocidad_proyectil)
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
                0 - velocidad_proyectil)
mp.on_button_event(mp.MultiplayerButton.A,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_a_pressed)

def on_right_pressed():
    pass
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    pass
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

disparo_p23 = False
ultimo_disparo_p2 = 0
now2 = 0
vy = 0
vx = 0
disparo_p12 = False
ultimo_disparo_p1 = 0
now = 0
ProjectileP2: Sprite = None
ProjectileP1: Sprite = None
status_p2: StatusBarSprite = None
status_p1: StatusBarSprite = None
p2: Sprite = None
p1: Sprite = None
vida_p1 = 0
vida_p2 = 0
velocidad_proyectil = 0
cooldown_disparo = 0
cooldown_disparo = 500
velocidad_proyectil = 150
vida_p2 = 3
vida_p1 = 3
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
mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)).set_stay_in_screen(True)
status_p1 = statusbars.create(20, 4, StatusBarKind.health)
status_p1.attach_to_sprite(p1)
status_p1.value = vida_p1
status_p1.max = vida_p1
status_p2 = statusbars.create(20, 4, StatusBarKind.health)
status_p2.attach_to_sprite(p2)
status_p2.value = vida_p2
status_p2.max = vida_p2
status_p1.set_bar_border(1, 13)
status_p2.set_bar_border(1, 13)
def mostrar_ganador(ganador: any):
    game.over(False)
    if ganador == 1:
        game.show_long_text("¡Jugador 1 ha ganado!", DialogLayout.BOTTOM)
    else:
        game.show_long_text("¡Jugador 2 ha ganado!", DialogLayout.BOTTOM)

def on_on_update():
    scene.center_camera_at((mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)).x + mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)).x) / 2,
        (mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)).y + mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)).y) / 2)
game.on_update(on_on_update)
