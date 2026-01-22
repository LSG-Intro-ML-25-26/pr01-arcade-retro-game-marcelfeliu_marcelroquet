mp.onButtonEvent(mp.MultiplayerButton.A, ControllerButtonEvent.Pressed, function on_button_multiplayer_a_pressed() {
    
    if (mp.isButtonPressed(mp.playerSelector(mp.PlayerNumber.Two), mp.MultiplayerButton.B)) {
        
    } else if (mp.isButtonPressed(mp.playerSelector(mp.PlayerNumber.Two), mp.MultiplayerButton.A)) {
        p2 = mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Two))
        vx = p2.vx
        vy = p2.vy
        if (Math.abs(vx) > Math.abs(vy)) {
            if (vx > 0) {
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
                        `, p2, 50, 0)
            } else {
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
                        `, p2, -50, 0)
            }
            
        } else if (vy > 0) {
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
                    `, p2, 0, 50)
        } else {
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
                    `, p2, 0, -50)
        }
        
    }
    
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left_pressed() {
    
})
mp.onButtonEvent(mp.MultiplayerButton.B, ControllerButtonEvent.Pressed, function on_button_multiplayer_b_pressed() {
    
    if (mp.isButtonPressed(mp.playerSelector(mp.PlayerNumber.One), mp.MultiplayerButton.A)) {
        
    } else if (mp.isButtonPressed(mp.playerSelector(mp.PlayerNumber.One), mp.MultiplayerButton.B)) {
        p1 = mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.One))
        vx = p1.vx
        vy = p1.vy
        if (Math.abs(vx) > Math.abs(vy)) {
            if (vx > 0) {
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
                        `, p1, 50, 0)
            } else {
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
                        `, p1, -50, 0)
            }
            
        } else if (vy > 0) {
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
                    `, p1, 0, 50)
        } else {
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
                    `, p1, 0, -50)
        }
        
    }
    
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function on_right_pressed() {
    
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down_pressed() {
    
})
let ProjectileP1 : Sprite = null
let ProjectileP2 : Sprite = null
let vy = 0
let vx = 0
let p2 : Sprite = null
let p1 : Sprite = null
let p22 = null
let vx2 = 0
let vy2 = 0
tiles.setCurrentTilemap(tilemap`
    level1
    `)
p1 = sprites.create(assets.image`
    nena-front
    `, SpriteKind.Player)
p2 = sprites.create(img`
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
        `, SpriteKind.Player)
mp.setPlayerSprite(mp.playerSelector(mp.PlayerNumber.One), p1)
mp.setPlayerSprite(mp.playerSelector(mp.PlayerNumber.Two), p2)
mp.moveWithButtons(mp.playerSelector(mp.PlayerNumber.One), 100, 100)
mp.moveWithButtons(mp.playerSelector(mp.PlayerNumber.Two), 100, 100)
scene.cameraFollowSprite(mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.One)))
scene.cameraFollowSprite(mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Two)))
mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.One)).setStayInScreen(true)
mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.One)).setStayInScreen(true)
game.onUpdate(function on_on_update() {
    scene.centerCameraAt((mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.One)).x + mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Two)).x) / 2, (mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.One)).y + mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.Two)).y) / 2)
})
