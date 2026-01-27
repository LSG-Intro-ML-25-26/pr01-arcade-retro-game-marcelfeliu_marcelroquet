def actualizar_direccion_p1():
    global vx, vy, last_direction_p1
    vx = p1.vx
    vy = p1.vy
    if abs(vx) > abs(vy):
        if vx > 0:
            last_direction_p1 = "right"
        elif vx < 0:
            last_direction_p1 = "left"
    elif abs(vy) > abs(vx):
        if vy > 0:
            last_direction_p1 = "down"
        elif vy < 0:
            last_direction_p1 = "up"

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
            pause(1200)
            game.over(False)
    elif player2 == p2:
        vida_p2 += 0 - 1
        status_p2.value = vida_p2
        player2.start_effect(effects.fire, 200)
        if vida_p2 <= 0:
            p2.destroy(effects.disintegrate, 500)
            pause(1200)
            game.over(False)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap)

def on_up_pressed():
    pass
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_player1_button_up_pressed():
    animation.run_image_animation(p1,
        assets.animation("""
            nena-animation-up
            """),
        200,
        False)
controller.player1.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player1_button_up_pressed)

def on_button_multiplayer_a_pressed(player23):
    global now2, ultimo_disparo_p2, disparo_p23, p2, ProjectileP2
    if mp.is_button_pressed(mp.player_selector(mp.PlayerNumber.TWO),
        mp.MultiplayerButton.B):
        pass
    elif mp.is_button_pressed(mp.player_selector(mp.PlayerNumber.TWO),
        mp.MultiplayerButton.A):
        now2 = game.runtime()
        if now2 - ultimo_disparo_p2 < cooldown_disparo:
            return
        ultimo_disparo_p2 = now2
        disparo_p23 = True
        p2 = mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO))
        actualizar_direccion_p2()
        if last_direction_p2 == "right":
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
        elif last_direction_p2 == "left":
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
        elif last_direction_p2 == "down":
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
        elif last_direction_p2 == "up":
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
    else:
        pass
mp.on_button_event(mp.MultiplayerButton.A,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_a_pressed)

def on_player2_button_down_pressed():
    animation.run_image_animation(p2,
        [img("""
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . . f e 2 f f f f f f 2 e f . .
                . . f f f f e e e e f f f f . .
                . f f e f b f 4 4 f b f e f f .
                . f e e 4 1 f d d f 1 4 e e f .
                . . f e e d d d d d d e e f . .
                . . . f e e 4 4 4 4 e e f . . .
                . . e 4 f 2 2 2 2 2 2 f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . f f e 2 f f f f f f 2 e f f .
                . f f f f f e e e e f f f f f .
                . . f e f b f 4 4 f b f e f . .
                . . f e 4 1 f d d f 1 4 e f . .
                . . . f e 4 d d d d 4 e f e . .
                . . f e f 2 2 2 2 e d d 4 e . .
                . . e 4 f 2 2 2 2 e d d e . . .
                . . . . f 4 4 5 5 f e e . . . .
                . . . . f f f f f f f . . . . .
                . . . . f f f . . . . . . . . .
                """),
            img("""
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . . f e 2 f f f f f f 2 e f . .
                . . f f f f e e e e f f f f . .
                . f f e f b f 4 4 f b f e f f .
                . f e e 4 1 f d d f 1 4 e e f .
                . . f e e d d d d d d e e f . .
                . . . f e e 4 4 4 4 e e f . . .
                . . e 4 f 2 2 2 2 2 2 f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
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
                . . e f e 4 d d d d 4 e f . . .
                . . e 4 d d e 2 2 2 2 f e f . .
                . . . e d d e 2 2 2 2 f 4 e . .
                . . . . e e f 5 5 4 4 f . . . .
                . . . . . f f f f f f f . . . .
                . . . . . . . . . f f f . . . .
                """)],
        200,
        False)
controller.player2.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.PRESSED,
    on_player2_button_down_pressed)

def on_left_pressed():
    pass
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_player2_button_up_pressed():
    animation.run_image_animation(p2,
        [img("""
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . f f f f f 2 2 f f f f f . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e 2 f 2 f f 2 f 2 e f . .
                . . f f f 2 2 e e 2 2 f f f . .
                . f f e f 2 f e e f 2 f e f f .
                . f e e f f e e e e f e e e f .
                . . f e e e e e e e e e e f . .
                . . . f e e e e e e e e f . . .
                . . e 4 f f f f f f f f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . . f f f f 2 2 f f f f . . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e 2 f 2 f f f 2 f e f . .
                . . f f f 2 f e e 2 2 f f f . .
                . . f e 2 f f e e 2 f e e f . .
                . f f e f f e e e f e e e f f .
                . f f e e e e e e e e e e f f .
                . . . f e e e e e e e e f . . .
                . . . e f f f f f f f f 4 e . .
                . . . 4 f 2 2 2 2 2 e d d 4 . .
                . . . e f f f f f f e e 4 . . .
                . . . . f f f . . . . . . . . .
                """),
            img("""
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . f f f f f 2 2 f f f f f . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e 2 f 2 f f 2 f 2 e f . .
                . . f f f 2 2 e e 2 2 f f f . .
                . f f e f 2 f e e f 2 f e f f .
                . f e e f f e e e e f e e e f .
                . . f e e e e e e e e e e f . .
                . . . f e e e e e e e e f . . .
                . . e 4 f f f f f f f f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . . f f f f 2 2 f f f f . . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e f 2 f f f 2 f 2 e f . .
                . . f f f 2 2 e e f 2 f f f . .
                . . f e e f 2 e e f f 2 e f . .
                . f f e e e f e e e f f e f f .
                . f f e e e e e e e e e e f f .
                . . . f e e e e e e e e f . . .
                . . e 4 f f f f f f f f e . . .
                . . 4 d d e 2 2 2 2 2 f 4 . . .
                . . . 4 e e f f f f f f e . . .
                . . . . . . . . . f f f . . . .
                """)],
        200,
        False)
controller.player2.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player2_button_up_pressed)

def on_right_pressed():
    pass
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_player2_button_right_pressed():
    animation.run_image_animation(p2,
        [img("""
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e 4 d d d d f . . .
                . . . . f f e e 4 4 4 e f . . .
                . . . . . 4 d d e 2 2 2 f . . .
                . . . . . e d d e 2 2 2 f . . .
                . . . . . f e e f 4 5 5 f . . .
                . . . . . . f f f f f f . . . .
                . . . . . . . f f f . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e e e d d d f . . .
                . . . . . f 4 d d e 4 e f . . .
                . . . . . f e d d e 2 2 f . . .
                . . . . f f f e e f 5 5 f f . .
                . . . . f f f f f f f f f f . .
                . . . . . f f . . . f f f . . .
                """),
            img("""
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e 4 d d d d f . . .
                . . . . f f e e 4 4 4 e f . . .
                . . . . . 4 d d e 2 2 2 f . . .
                . . . . . e d d e 2 2 2 f . . .
                . . . . . f e e f 4 5 5 f . . .
                . . . . . . f f f f f f . . . .
                . . . . . . . f f f . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e 4 d d d d f . . .
                . . . . 4 d d e 4 4 4 e f . . .
                . . . . e d d e 2 2 2 2 f . . .
                . . . . f e e f 4 4 5 5 f f . .
                . . . . f f f f f f f f f f . .
                . . . . . f f . . . f f f . . .
                """)],
        200,
        False)
controller.player2.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player2_button_right_pressed)

def mostrar_lore():
    global en_lore
    en_lore = True
    scene.set_background_image(assets.image("""
        
        """))
    story.print_dialog("Durante años el pueblo de Sinfos ha vivido en paz,",
        80,
        90,
        50,
        150)
    scene.set_background_image(assets.image("""
        
        """))
    story.print_dialog("lo que no saben es que ahora el Dios Arnau conocido como el dios bastárdo quiere sus tierras",
        80,
        90,
        50,
        150)
    scene.set_background_image(assets.image("""
        
        """))
    story.print_dialog("Dios Pau, su hermano, heredero legítimo del pueblo deberá defenderlo.",
        80,
        90,
        50,
        150)
    scene.set_background_image(assets.image("""
        
        """))
    story.print_dialog("Los dos hermanos se enfrentarán en una batalla final.",
        80,
        90,
        50,
        150)
    scene.set_background_image(assets.image("""
        
        """))
    story.print_dialog("¿Podrá Dios Pau mantener la paz en Sinfos?",
        80,
        90,
        50,
        150)
    en_lore = False

def on_down_pressed():
    pass
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_player2_button_left_pressed():
    animation.run_image_animation(p2,
        [img("""
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d d 4 e e e f . . .
                . . . f e 4 4 4 e e f f . . . .
                . . . f 2 2 2 e d d 4 . . . . .
                . . . f 2 2 2 e d d e . . . . .
                . . . f 5 5 4 f e e f . . . . .
                . . . . f f f f f f . . . . . .
                . . . . . . f f f . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d e e e e e f . . .
                . . . f e 4 e d d 4 f . . . . .
                . . . f 2 2 e d d e f . . . . .
                . . f f 5 5 f e e f f f . . . .
                . . f f f f f f f f f f . . . .
                . . . f f f . . . f f . . . . .
                """),
            img("""
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d d 4 e e e f . . .
                . . . f e 4 4 4 e e f f . . . .
                . . . f 2 2 2 e d d 4 . . . . .
                . . . f 2 2 2 e d d e . . . . .
                . . . f 5 5 4 f e e f . . . . .
                . . . . f f f f f f . . . . . .
                . . . . . . f f f . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d d 4 e e e f . . .
                . . . f e 4 4 4 e d d 4 . . . .
                . . . f 2 2 2 2 e d d e . . . .
                . . f f 5 5 4 4 f e e f . . . .
                . . f f f f f f f f f f . . . .
                . . . f f f . . . f f . . . . .
                """)],
        200,
        False)
controller.player2.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player2_button_left_pressed)

def on_player1_button_right_pressed():
    animation.run_image_animation(p1,
        assets.animation("""
            nena-animation-right
            """),
        200,
        False)
controller.player1.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player1_button_right_pressed)

def on_button_multiplayer_b_pressed(player22):
    global now, ultimo_disparo_p1, disparo_p12, p1, ProjectileP1
    if mp.is_button_pressed(mp.player_selector(mp.PlayerNumber.ONE),
        mp.MultiplayerButton.A):
        pass
    elif mp.is_button_pressed(mp.player_selector(mp.PlayerNumber.ONE),
        mp.MultiplayerButton.B):
        now = game.runtime()
        if now - ultimo_disparo_p1 < cooldown_disparo:
            return
        ultimo_disparo_p1 = now
        actualizar_direccion_p1()
        disparo_p12 = True
        p1 = mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE))
        if last_direction_p1 == "right":
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
        elif last_direction_p1 == "left":
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
        elif last_direction_p1 == "down":
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
        elif last_direction_p1 == "up":
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
    else:
        pass
mp.on_button_event(mp.MultiplayerButton.B,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_b_pressed)

def actualizar_direccion_p2():
    global vx2, vy2, last_direction_p2
    vx2 = p2.vx
    vy2 = p2.vy
    if abs(vx2) > abs(vy2):
        if vx2 > 0:
            last_direction_p2 = "right"
        elif vx2 < 0:
            last_direction_p2 = "left"
    elif abs(vy2) > abs(vx2):
        if vy2 > 0:
            last_direction_p2 = "down"
        elif vy2 < 0:
            last_direction_p2 = "up"

def on_player1_button_left_pressed():
    animation.run_image_animation(p1,
        assets.animation("""
            nena-animation-left
            """),
        200,
        False)
controller.player1.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player1_button_left_pressed)

def on_player1_button_down_pressed():
    animation.run_image_animation(p1,
        assets.animation("""
            nena-animation-down
            """),
        200,
        False)
controller.player1.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.PRESSED,
    on_player1_button_down_pressed)

vy2 = 0
vx2 = 0
disparo_p12 = False
ultimo_disparo_p1 = 0
now = 0
disparo_p23 = False
ultimo_disparo_p2 = 0
now2 = 0
ProjectileP2: Sprite = None
ProjectileP1: Sprite = None
vy = 0
vx = 0
status_p2: StatusBarSprite = None
status_p1: StatusBarSprite = None
p2: Sprite = None
p1: Sprite = None
vida_p1 = 0
vida_p2 = 0
velocidad_proyectil = 0
cooldown_disparo = 0
last_direction_p2 = ""
last_direction_p1 = ""
en_lore = False
vy22 = 0
vx22 = 0
vy3 = 0
vx3 = 0
now3 = 0
en_lore = True
mostrar_lore()
last_direction_p1 = "right"
last_direction_p2 = "left"
cooldown_disparo = 500
velocidad_proyectil = 150
vida_p2 = 7
vida_p1 = 7
tiles.set_current_tilemap(tilemap("""
    level1
    """))
p1 = sprites.create(assets.image("""
    nena-front
    """), SpriteKind.player)
p1.set_position(0, 54)
p2 = sprites.create(img("""
        . . . . . . f f f f . . . . . .
        . . . . f f f 2 2 f f f . . . .
        . . . f f f 2 2 2 2 f f f . . .
        . . f f f e e e e e e f f f . .
        . . f f e 2 2 2 2 2 2 e e f . .
        . . f e 2 f f f f f f 2 e f . .
        . . f f f f e e e e f f f f . .
        . f f e f b f 4 4 f b f e f f .
        . f e e 4 1 f d d f 1 4 e e f .
        . . f e e d d d d d d e e f . .
        . . . f e e 4 4 4 4 e e f . . .
        . . e 4 f 2 2 2 2 2 2 f 4 e . .
        . . 4 d f 2 2 2 2 2 2 f d 4 . .
        . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
        . . . . . f f f f f f . . . . .
        . . . . . f f . . f f . . . . .
        """),
    SpriteKind.player)
p2.set_position(160, 54)
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
status_p1.set_bar_border(1, 15)
status_p1.set_color(7, 2)
status_p2.set_color(7, 2)
status_p2.set_bar_border(1, 15)
def mostrar_ganador(ganador: any):
    game.over(False)
    if ganador == 1:
        game.show_long_text("¡Jugador 1 ha ganado!", DialogLayout.BOTTOM)
    else:
        game.show_long_text("¡Jugador 2 ha ganado!", DialogLayout.BOTTOM)

def on_on_update():
    actualizar_direccion_p1()
    actualizar_direccion_p2()
    scene.center_camera_at((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
game.on_update(on_on_update)

def on_forever():
    effects.star_field.start_screen_effect(5000)
forever(on_forever)