Sea Sweepers Game: Test Plan
Game Overview
Sea Sweepers is an underwater trash collection game where players control a duck to collect floating trash while avoiding marine animals. The game uses HTML5 Canvas and JavaScript.
Main Features to Test
Game Mechanics

 Duck movement (arrow keys)
 Trash collection
 Marine animal collisions
 Timer countdown
 Score tracking
 Game over conditions
 Restart functionality

Visual Elements

 Ocean background with gradient
 Light rays rendering
 Seaweed animation
 Bubble effects
 Trash item floating animation
 Marine animal movement and glow effects
 Ocean floor

Image Loading

 Duck image
 Trash images (bottle, can, trash, paper, milk, banana)
 Marine animal images (dolphin, fish, nemo, turtle, whale)
 Fallback rendering when images fail to load

Edge Cases

 What happens if multiple arrow keys are pressed at once?
 Does the game handle rapid trash collection correctly?
 What if all images fail to load?
 How does the game perform when many marine animals are on screen?
 What happens at the edge of the game area?
 Does tab switching affect the game state?
 How does the game handle very short play sessions?

Browser Testing
Need to check on:

Chrome
Firefox
Safari
Edge
Mobile browsers

Testing Steps
1. Basic Controls

Start the game
Test duck movement with arrow keys:

Up arrow: Duck should move upward
Down arrow: Duck should move downward
Left arrow: Duck should move left
Right arrow: Duck should move right
Multiple arrow keys: Duck should move diagonally


Check that duck doesn't move off-screen

2. Core Gameplay

Approach trash items and verify collection:

Score should increase by 10
Collected count should increment
Trash item should disappear
New trash should spawn in a different location


Avoid marine animals:

Game should end when colliding with any marine animal
Game over screen should appear


Time limit:

Timer should count down from 60 seconds
Game should end when timer reaches 0
Game over screen should appear



3. Visual Elements

Verify background gradient renders correctly
Check that 3 light rays appear and are positioned correctly
Verify seaweed renders at the bottom
Check that bubbles animate upward
Verify trash items have a floating animation
Check that marine animals have proper glow effects
Verify ocean floor renders correctly

4. Game Progression

Play a full game and verify:

Marine animals spawn more frequently as time passes
Score tracking works throughout
Timer correctly counts down


Test restart functionality:

Press SPACE at game over screen
Game should reset all values and start over


Test quit functionality:

Press Q at game over screen
Game should reset



5. Image Loading

Load the game and check if all images load correctly
Test with slow network conditions (throttle connection in dev tools)
Test with images missing/broken:

Verify fallback colored shapes appear instead
Confirm gameplay still works without images



Performance Testing

 Test on low-end devices
 Check performance with many objects on screen
 Monitor for frame rate drops during extended play

Notes for Testing

Focus on checking collision detection between duck and trash/animals
Watch for any visual glitches with animations
Pay attention to image loading issues
Check that restart functionality correctly resets all game state
Test marine animal spawn rate increase as time progresses