controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    lookUp = true
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    ProjectileP2 = sprites.createProjectileFromSprite(img`
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
        `, player2, -60, 0)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    checkDirection()
})
controller.down.onEvent(ControllerButtonEvent.Released, function () {
    lookDown = false
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    lookLeft = true
})
controller.right.onEvent(ControllerButtonEvent.Released, function () {
    lookRight = false
})
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    lookLeft = false
})
function checkDirection () {
    speed = 60
    if (lookUp) {
        vy += 0 - speed
    }
    if (lookDown) {
        vy += speed
    }
    if (lookLeft) {
        vx += 0 - speed
    }
    if (lookRight) {
        vx += speed
    }
    if (vx == 0 && vy == 0) {
        return
    }
    ProjectileP1 = sprites.createProjectileFromSprite(img`
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
        `, player1, vx, vy)
}
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    lookRight = true
})
controller.up.onEvent(ControllerButtonEvent.Released, function () {
    lookUp = false
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    lookDown = true
})
let ProjectileP1: Sprite = null
let vx = 0
let vy = 0
let speed = 0
let lookRight = false
let lookLeft = false
let lookDown = false
let ProjectileP2: Sprite = null
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
player1.setStayInScreen(true)
player2.setStayInScreen(true)
scene.cameraFollowSprite(player1)
effects.starField.startScreenEffect()
game.onUpdate(function () {
    scene.centerCameraAt((player1.x + player2.x) / 2, (player1.y + player2.y) / 2)
})
