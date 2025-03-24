Sea Sweepers Bug Tracker
Detailed Bug Reports
BUG-01: Diagonal movement speed
Status: Fixed
Description:
When pressing two arrow keys simultaneously (e.g., up and right), the duck moves approximately 1.4x faster than when moving in a single direction. This creates an unintended advantage when moving diagonally.
Steps to Reproduce:

Start the game
Press and hold the Up arrow key - note the duck's speed
Release and press diagonal keys (Up + Right) - notice faster movement

Expected Behavior:
Duck should move at consistent speed regardless of direction.
Actual Behavior:
Duck moves about 40% faster when moving diagonally.
Root Cause:
The movement code applies full speed in both horizontal and vertical directions simultaneously, without normalizing the resulting vector.
Fix:
Fixed movement code
let dx = 0;
let dy = 0;

if (keys.ArrowUp) dy -= 1;
if (keys.ArrowDown) dy += 1;
if (keys.ArrowLeft) dx -= 1;
if (keys.ArrowRight) dx += 1;

// Normalize diagonal movement
if (dx !== 0 && dy !== 0) {
    const length = Math.sqrt(dx * dx + dy * dy);
    dx = dx / length;
    dy = dy / length;
}

// Apply speed
duck.x += dx * duck.speed;
duck.y += dy * duck.speed;

BUG-02: Missing image files
Status: Fixed
Description:
Several game images fail to load, causing the game to fall back to simple colored shapes. Specifically, 'milk.png' and 'whale.png' were not found.
Steps to Reproduce:

Load the game
Check browser console for 404 errors
Observe that some objects appear as colored rectangles instead of images

Expected Behavior:
All images should load correctly.
Actual Behavior:
Error 404 for some image files, falling back to colored rectangles.
Root Cause:
Incorrect file paths or missing images in the /images directory.
Fix:

Added missing files to the images directory
Corrected file paths in the code:
Fixed image paths
milkImage.src = 'images/milk_bottle.png'; // Changed from milk.png
whaleImage.src = 'images/blue_whale.png'; // Changed from whale.png

BUG-03: Marine animal glow effect flickering
Status: In Progress
Description:
The glow effect around marine animals sometimes flickers, especially on lower-end devices and mobile browsers.
Steps to Reproduce:

Run the game on a mid-range mobile device or throttle CPU in browser dev tools
Observe marine animals as they swim around
Notice flickering of the glow effect, especially when multiple animals are on screen

Expected Behavior:
Glow effect should appear smooth and consistent.
Actual Behavior:
Glow effect flickers and causes frame rate drops.
Root Cause:
The pulsing effect created by adjusting global alpha in combination with the radial gradient is performance-intensive.
Potential Fix (in progress):
Simplified glow effect
// Instead of using sin function for pulsing, use simpler approach
const glowSize = 15;
const glowX = animal.x + animal.width/2;
const glowY = animal.y + animal.height/2;

// Create a radial gradient for the glow
const gradient = ctx.createRadialGradient(
    glowX, glowY, animal.width/2,
    glowX, glowY, animal.width/2 + glowSize
);

// Use static opacity instead of pulsing
ctx.globalAlpha = 0.6;

BUG-04: Trash spawning too close to duck
Status: Fixed
Description:
When collecting trash, new trash sometimes spawns too close to the duck, making it too easy to collect multiple items in rapid succession.
Steps to Reproduce:

Start a new game
Collect a trash item
Observe that a new trash item sometimes spawns within immediate reach

Expected Behavior:
New trash should spawn away from the duck's current position.
Actual Behavior:
New trash sometimes spawns too close to the duck, allowing for chain collection.
Root Cause:
The distance check for new trash positioning isn't strict enough, and the quadrant-based positioning doesn't guarantee enough distance.
Fix:
Improved trash spawn logic
// Increased minimum distance from duck
const MIN_DUCK_DISTANCE = 200; // Increased from 150

// In the while loop for finding a valid position:
if (duckDistance > MIN_DUCK_DISTANCE) {
    validPosition = true;
}

BUG-05: No mobile controls
Status: Open
Description:
The game has no touch controls for mobile devices, making it unplayable on tablets and phones without a physical keyboard.
Steps to Reproduce:

Load the game on a mobile device
Try to play the game
Notice there's no way to control the duck

Expected Behavior:
Mobile devices should have touch-based controls.
Actual Behavior:
No controls available on touch devices.
Proposed Solution:
Add on-screen directional buttons for mobile or implement touch/drag controls.

BUG-06: Imprecise collision detection
Status: Open
Description:
Collision detection using bounding rectangles sometimes feels imprecise, especially with irregularly shaped marine animals.
Steps to Reproduce:

Play the game
Approach a marine animal carefully
Notice that collisions sometimes register when visually the duck and animal don't appear to touch

Expected Behavior:
Collisions should match the visible shapes of objects.
Actual Behavior:
Collisions use rectangular bounding boxes that don't match the visual shapes.
Proposed Solution:
Implement more precise collision detection, possibly using circular hitboxes or adjusting the rectangle sizes to better match the visual elements.

BUG-07: Performance issues on mobile
Status: In Progress
Description:
Frame rate drops significantly on mobile devices when multiple marine animals are on screen with glow effects active.
Steps to Reproduce:

Play the game on a mobile device
Continue playing until several marine animals appear on screen
Observe the frame rate drop

Expected Behavior:
Game should maintain smooth performance on most devices.
Actual Behavior:
Noticeable performance degradation on mobile devices.
Root Cause:
Multiple factors:

Complex drawing operations for glow effects
No frame rate limiting or throttling
Multiple gradient operations per frame

Potential Fix (in progress):

Simplify glow effects
Add frame rate limiting option
Reduce the number of marine animals on mobile devices
Optimize drawing operations


BUG-08: No pause when tab loses focus
Status: Open
Description:
When switching to another browser tab or window, the game continues running in the background, which can result in unintended game overs.
Steps to Reproduce:

Start a game
Switch to another browser tab
Return after a few seconds
Game has continued running and may be in game over state

Expected Behavior:
Game should pause when tab loses focus.
Actual Behavior:
Game continues running in background.
Proposed Solution:
Add visibility change listener
document.addEventListener('visibilitychange', function() {
    if (document.hidden) {
        // Pause game
        gameActive = false;
    } else {
        // Resume if not in game over state
        if (!gameOver) {
            gameActive = true;
            // Reset lastTime to prevent huge time jump
            lastTime = 0;
            requestAnimationFrame(gameLoop);
        }
    }
});