controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    player1,
    assets.animation`nena-animation-up`,
    500,
    false
    )
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    player1,
    assets.animation`nena-animation-left`,
    500,
    false
    )
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    player1,
    assets.animation`nena-animation-right`,
    500,
    false
    )
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    player1,
    assets.animation`nena-animation-down`,
    500,
    false
    )
})
let player1: Sprite = null
tiles.setCurrentTilemap(tilemap`level1`)
player1 = sprites.create(assets.image`nena-front`, SpriteKind.Player)
let player2 = sprites.create(img`
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
