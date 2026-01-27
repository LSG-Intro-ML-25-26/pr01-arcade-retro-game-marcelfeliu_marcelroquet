function actualizar_direccion_p1 () {
    vx = p1.vx
    vy = p1.vy
    if (Math.abs(vx) > Math.abs(vy)) {
        if (vx > 0) {
            last_direction_p1 = "right"
        } else if (vx < 0) {
            last_direction_p1 = "left"
        }
    } else if (Math.abs(vy) > Math.abs(vx)) {
        if (vy > 0) {
            last_direction_p1 = "down"
        } else if (vy < 0) {
            last_direction_p1 = "up"
        }
    }
}
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Player, function (projectile, player2) {
    if (projectile == ProjectileP1 && player2 == p1) {
        return
    }
    if (projectile == ProjectileP2 && player2 == p2) {
        return
    }
    projectile.destroy()
    if (player2 == p1) {
        vida_p1 += 0 - 1
        status_p1.value = vida_p1
        player2.startEffect(effects.fire, 200)
        if (vida_p1 <= 0) {
            p1.destroy(effects.disintegrate, 500)
            pause(1200)
            game.over(false)
        }
    } else if (player2 == p2) {
        vida_p2 += 0 - 1
        status_p2.value = vida_p2
        player2.startEffect(effects.fire, 200)
        if (vida_p2 <= 0) {
            p2.destroy(effects.disintegrate, 500)
            pause(1200)
            game.over(false)
        }
    }
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
	
})
controller.player1.onButtonEvent(ControllerButton.Up, ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    p1,
    assets.animation`nena-animation-up`,
    200,
    false
    )
})
mp.onButtonEvent(mp.MultiplayerButton.A, ControllerButtonEvent.Pressed, function (player23) {
    if (mp.isButtonPressed(mp.playerSelector(mp.PlayerNumber.Two), mp.MultiplayerButton.B)) {
    	
    } else if (mp.isButtonPressed(mp.playerSelector(mp.PlayerNumber.Two), mp.MultiplayerButton.A)) {
        now2 = game.runtime()
        if (now2 - ultimo_disparo_p2 < cooldown_disparo) {
            return
        }
        ultimo_disparo_p2 = now2
        disparo_p23 = true
        p2 = mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Two))
        actualizar_direccion_p2()
        if (last_direction_p2 == "right") {
            ProjectileP2 = sprites.createProjectileFromSprite(img`
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
                `, p2, velocidad_proyectil, 0)
        } else if (last_direction_p2 == "left") {
            ProjectileP2 = sprites.createProjectileFromSprite(img`
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
                `, p2, 0 - velocidad_proyectil, 0)
        } else if (last_direction_p2 == "down") {
            ProjectileP2 = sprites.createProjectileFromSprite(img`
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
                `, p2, 0, velocidad_proyectil)
        } else if (last_direction_p2 == "up") {
            ProjectileP2 = sprites.createProjectileFromSprite(img`
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
                `, p2, 0, 0 - velocidad_proyectil)
        }
    } else {
    	
    }
})
controller.player2.onButtonEvent(ControllerButton.Down, ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    p2,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    200,
    false
    )
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
	
})
controller.player2.onButtonEvent(ControllerButton.Up, ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    p2,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    200,
    false
    )
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
	
})
controller.player2.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    p2,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    200,
    false
    )
})
function mostrar_lore () {
    en_lore = true
    scene.setBackgroundImage(assets.image`
                
                `)
    story.printDialog("Durante años el pueblo de Sinfos ha vivido en paz,", 80, 90, 50, 150)
    scene.setBackgroundImage(assets.image`
                
                `)
    story.printDialog("lo que no saben es que ahora el Dios Arnau conocido como el dios bastárdo quiere sus tierras", 80, 90, 50, 150)
    scene.setBackgroundImage(assets.image`
                
                `)
    story.printDialog("Dios Pau, su hermano, heredero legítimo del pueblo deberá defenderlo.", 80, 90, 50, 150)
    scene.setBackgroundImage(assets.image`
                
                `)
    story.printDialog("Los dos hermanos se enfrentarán en una batalla final.", 80, 90, 50, 150)
    scene.setBackgroundImage(assets.image`
                
                `)
    story.printDialog("¿Podrá Dios Pau mantener la paz en Sinfos?", 80, 90, 50, 150)
    en_lore = false
}
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
	
})
controller.player2.onButtonEvent(ControllerButton.Left, ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    p2,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    200,
    false
    )
})
controller.player1.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    p1,
    assets.animation`nena-animation-right`,
    200,
    false
    )
})
mp.onButtonEvent(mp.MultiplayerButton.B, ControllerButtonEvent.Pressed, function (player22) {
    if (mp.isButtonPressed(mp.playerSelector(mp.PlayerNumber.One), mp.MultiplayerButton.A)) {
    	
    } else if (mp.isButtonPressed(mp.playerSelector(mp.PlayerNumber.One), mp.MultiplayerButton.B)) {
        now = game.runtime()
        if (now - ultimo_disparo_p1 < cooldown_disparo) {
            return
        }
        ultimo_disparo_p1 = now
        actualizar_direccion_p1()
        disparo_p12 = true
        p1 = mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.One))
        if (last_direction_p1 == "right") {
            ProjectileP1 = sprites.createProjectileFromSprite(img`
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
                `, p1, velocidad_proyectil, 0)
        } else if (last_direction_p1 == "left") {
            ProjectileP1 = sprites.createProjectileFromSprite(img`
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
                `, p1, 0 - velocidad_proyectil, 0)
        } else if (last_direction_p1 == "down") {
            ProjectileP1 = sprites.createProjectileFromSprite(img`
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
                `, p1, 0, velocidad_proyectil)
        } else if (last_direction_p1 == "up") {
            ProjectileP1 = sprites.createProjectileFromSprite(img`
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
                `, p1, 0, 0 - velocidad_proyectil)
        }
    } else {
    	
    }
})
function actualizar_direccion_p2 () {
    vx2 = p2.vx
    vy2 = p2.vy
    if (Math.abs(vx2) > Math.abs(vy2)) {
        if (vx2 > 0) {
            last_direction_p2 = "right"
        } else if (vx2 < 0) {
            last_direction_p2 = "left"
        }
    } else if (Math.abs(vy2) > Math.abs(vx2)) {
        if (vy2 > 0) {
            last_direction_p2 = "down"
        } else if (vy2 < 0) {
            last_direction_p2 = "up"
        }
    }
}
controller.player1.onButtonEvent(ControllerButton.Left, ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    p1,
    assets.animation`nena-animation-left`,
    200,
    false
    )
})
controller.player1.onButtonEvent(ControllerButton.Down, ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    p1,
    assets.animation`nena-animation-down`,
    200,
    false
    )
})
let vy2 = 0
let vx2 = 0
let disparo_p12 = false
let ultimo_disparo_p1 = 0
let now = 0
let disparo_p23 = false
let ultimo_disparo_p2 = 0
let now2 = 0
let ProjectileP2: Sprite = null
let ProjectileP1: Sprite = null
let vy = 0
let vx = 0
let status_p2: StatusBarSprite = null
let status_p1: StatusBarSprite = null
let p2: Sprite = null
let p1: Sprite = null
let vida_p1 = 0
let vida_p2 = 0
let velocidad_proyectil = 0
let cooldown_disparo = 0
let last_direction_p2 = ""
let last_direction_p1 = ""
let en_lore = false
let now3 = 0
let vx3 = 0
let vy3 = 0
let vx22 = 0
let vy22 = 0
en_lore = true
mostrar_lore()
last_direction_p1 = "right"
last_direction_p2 = "left"
cooldown_disparo = 500
velocidad_proyectil = 150
vida_p2 = 7
vida_p1 = 7
tiles.setCurrentTilemap(tilemap`level1`)
p1 = sprites.create(assets.image`nena-front`, SpriteKind.Player)
p1.setPosition(0, 54)
p2 = sprites.create(img`
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
    `, SpriteKind.Player)
p2.setPosition(160, 54)
mp.setPlayerSprite(mp.playerSelector(mp.PlayerNumber.One), p1)
mp.setPlayerSprite(mp.playerSelector(mp.PlayerNumber.Two), p2)
mp.moveWithButtons(mp.playerSelector(mp.PlayerNumber.One), 100, 100)
mp.moveWithButtons(mp.playerSelector(mp.PlayerNumber.Two), 100, 100)
scene.cameraFollowSprite(mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.One)))
scene.cameraFollowSprite(mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Two)))
mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.One)).setStayInScreen(true)
mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Two)).setStayInScreen(true)
status_p1 = statusbars.create(20, 4, StatusBarKind.Health)
status_p1.attachToSprite(p1)
status_p1.value = vida_p1
status_p1.max = vida_p1
status_p2 = statusbars.create(20, 4, StatusBarKind.Health)
status_p2.attachToSprite(p2)
status_p2.value = vida_p2
status_p2.max = vida_p2
status_p1.setBarBorder(1, 15)
status_p1.setColor(7, 2)
status_p2.setColor(7, 2)
status_p2.setBarBorder(1, 15)
function mostrar_ganador(ganador: any) {
    game.over(false)
    if (ganador == 1) {
        game.showLongText("¡Jugador 1 ha ganado!", DialogLayout.Bottom)
    } else {
        game.showLongText("¡Jugador 2 ha ganado!", DialogLayout.Bottom)
    }
    
}
game.onUpdate(function () {
    actualizar_direccion_p1()
    actualizar_direccion_p2()
    scene.centerCameraAt((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
})
forever(function () {
    effects.starField.startScreenEffect(5000)
})
