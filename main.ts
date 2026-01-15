controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    lookUp = true
    lookDown = false
    lookLeft = false
    lookRight = false
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    ProjectileP2 = sprites.createProjectileFromSprite(img`
        . . . . . b b b b b b . . . . . . 
        . . . . b b 9 9 9 9 9 9 b b . . . 
        . . . . b b 9 9 9 9 9 9 9 9 b b . 
        . . . b b 9 d 9 9 9 9 9 9 9 9 b b 
        . . b 9 d 9 9 9 9 9 1 1 1 9 9 b . 
        b 9 d d 9 9 9 9 9 1 1 1 9 9 9 b . 
        b 9 d 9 9 9 9 9 9 1 1 1 9 9 9 b . 
        b 9 3 9 9 9 9 9 9 9 9 1 9 9 b . . 
        b 5 3 d 9 9 9 9 9 9 9 9 9 9 9 b . 
        b 5 3 3 9 9 9 9 9 9 9 9 9 d 9 b . 
        b 5 d 3 3 9 9 9 9 9 9 9 d d 9 b . 
        . b 5 3 3 3 d 9 9 9 9 d d 5 b . . 
        . . b d 5 3 3 3 3 3 3 3 d 5 b b . 
        . . . b d 5 d 3 3 3 3 5 5 b b . . 
        . . . . b b 5 5 5 5 5 5 b b . . . 
        . . . . . . b b b b b b . . . . . 
        `, player2, -60, 50)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (lookDown) {
        ProjectileP1 = sprites.createProjectileFromSprite(img`
            . . . . . . . . . c c 8 . . . . 
            . . . . . . 8 c c c f 8 c c . . 
            . . . c c 8 8 f c a f f f c c . 
            . . c c c f f f c a a f f c c c 
            8 c c c f f f f c c a a c 8 c c 
            c c c b f f f 8 a c c a a a c c 
            c a a b b 8 a b c c c c c c c c 
            a f c a a b b a c c c c c f f c 
            a 8 f c a a c c a c a c f f f c 
            c a 8 a a c c c c a a f f f 8 a 
            . a c a a c f f a a b 8 f f c a 
            . . c c b a f f f a b b c c 6 c 
            . . . c b b a f f 6 6 a b 6 c . 
            . . . c c b b b 6 6 a c c c c . 
            . . . . c c a b b c c c . . . . 
            . . . . . c c c c c c . . . . . 
            `, player1, 0, 50)
    } else if (lookUp) {
        ProjectileP1 = sprites.createProjectileFromSprite(img`
            . . . . . . . . . c c 8 . . . . 
            . . . . . . 8 c c c f 8 c c . . 
            . . . c c 8 8 f c a f f f c c . 
            . . c c c f f f c a a f f c c c 
            8 c c c f f f f c c a a c 8 c c 
            c c c b f f f 8 a c c a a a c c 
            c a a b b 8 a b c c c c c c c c 
            a f c a a b b a c c c c c f f c 
            a 8 f c a a c c a c a c f f f c 
            c a 8 a a c c c c a a f f f 8 a 
            . a c a a c f f a a b 8 f f c a 
            . . c c b a f f f a b b c c 6 c 
            . . . c b b a f f 6 6 a b 6 c . 
            . . . c c b b b 6 6 a c c c c . 
            . . . . c c a b b c c c . . . . 
            . . . . . c c c c c c . . . . . 
            `, player1, 0, -50)
    } else if (lookLeft) {
        ProjectileP1 = sprites.createProjectileFromSprite(img`
            . . . . . . . . . c c 8 . . . . 
            . . . . . . 8 c c c f 8 c c . . 
            . . . c c 8 8 f c a f f f c c . 
            . . c c c f f f c a a f f c c c 
            8 c c c f f f f c c a a c 8 c c 
            c c c b f f f 8 a c c a a a c c 
            c a a b b 8 a b c c c c c c c c 
            a f c a a b b a c c c c c f f c 
            a 8 f c a a c c a c a c f f f c 
            c a 8 a a c c c c a a f f f 8 a 
            . a c a a c f f a a b 8 f f c a 
            . . c c b a f f f a b b c c 6 c 
            . . . c b b a f f 6 6 a b 6 c . 
            . . . c c b b b 6 6 a c c c c . 
            . . . . c c a b b c c c . . . . 
            . . . . . c c c c c c . . . . . 
            `, player1, -50, 0)
    } else if (lookRight) {
        ProjectileP1 = sprites.createProjectileFromSprite(img`
            . . . . . . . . . c c 8 . . . . 
            . . . . . . 8 c c c f 8 c c . . 
            . . . c c 8 8 f c a f f f c c . 
            . . c c c f f f c a a f f c c c 
            8 c c c f f f f c c a a c 8 c c 
            c c c b f f f 8 a c c a a a c c 
            c a a b b 8 a b c c c c c c c c 
            a f c a a b b a c c c c c f f c 
            a 8 f c a a c c a c a c f f f c 
            c a 8 a a c c c c a a f f f 8 a 
            . a c a a c f f a a b 8 f f c a 
            . . c c b a f f f a b b c c 6 c 
            . . . c b b a f f 6 6 a b 6 c . 
            . . . c c b b b 6 6 a c c c c . 
            . . . . c c a b b c c c . . . . 
            . . . . . c c c c c c . . . . . 
            `, player1, 50, 0)
    }
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    lookUp = false
    lookDown = false
    lookLeft = true
    lookRight = false
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    lookUp = false
    lookDown = false
    lookLeft = false
    lookRight = true
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    lookUp = false
    lookDown = true
    lookLeft = false
    lookRight = false
})
let ProjectileP1: Sprite = null
let ProjectileP2: Sprite = null
let lookRight = false
let lookLeft = false
let lookDown = false
let lookUp = false
let player2: Sprite = null
let player1: Sprite = null
tiles.setCurrentTilemap(tilemap`level1`)
player1 = sprites.create(assets.image`nena-front`, SpriteKind.Player)
player2 = sprites.create(img`
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
controller.player1.moveSprite(player1)
controller.player2.moveSprite(player2)
scene.cameraFollowSprite(player1)
scene.cameraFollowSprite(player2)
player1.setStayInScreen(true)
player2.setStayInScreen(true)
game.onUpdate(function () {
    scene.centerCameraAt((player1.x + player2.x) / 2, (player1.y + player2.y) / 2)
})
