// Setup file for Sea Sweepers tests


// Create mock canvas environment
document.body.innerHTML = `
  <div id="title">Sea Sweepers</div>
  <canvas id="gameCanvas" width="800" height="600"></canvas>
`;

// Mock canvas and context for testing
const mockContext = {
  clearRect: jest.fn(),
  fillRect: jest.fn(),
  beginPath: jest.fn(),
  moveTo: jest.fn(),
  lineTo: jest.fn(),
  fill: jest.fn(),
  stroke: jest.fn(),
  arc: jest.fn(),
  ellipse: jest.fn(),
  closePath: jest.fn(),
  createLinearGradient: jest.fn().mockReturnValue({
    addColorStop: jest.fn()
  }),
  createRadialGradient: jest.fn().mockReturnValue({
    addColorStop: jest.fn()
  }),
  drawImage: jest.fn(),
  fillText: jest.fn(),
  save: jest.fn(),
  restore: jest.fn(),
  translate: jest.fn(),
  scale: jest.fn()
};

// Mock canvas element and getContext method
const mockCanvas = document.getElementById('gameCanvas');
mockCanvas.getContext = jest.fn().mockReturnValue(mockContext);

// Mock global variables
global.gameActive = true;
global.gameOver = false;
global.score = 0;
global.collectedItems = 0;
global.timer = 60;

// Mock game objects
global.duck = {
  x: 400,
  y: 300,
  width: 60,
  height: 40,
  speed: 5
};

global.trashItems = [];
global.marineAnimals = [];
global.bubbles = [];
global.seaweeds = [];

// Mock key states
global.keys = {
  ArrowUp: false,
  ArrowDown: false,
  ArrowLeft: false,
  ArrowRight: false,
  Space: false,
  KeyQ: false
};

// Mock image objects
global.duckImage = new Image();
global.bottleImage = new Image();
global.canImage = new Image();
global.trashImage = new Image();
global.paperImage = new Image();
global.milkImage = new Image();
global.bananaImage = new Image();
global.dolphinImage = new Image();
global.fishImage = new Image();
global.nemoImage = new Image();
global.turtleImage = new Image();
global.whaleImage = new Image();

// Mock image loaded state
global.duckImageLoaded = true;
global.bottleImageLoaded = true;
global.canImageLoaded = true;
global.trashImageLoaded = true;
global.paperImageLoaded = true;
global.milkImageLoaded = false; // Simulate one failing image
global.bananaImageLoaded = true;
global.dolphinImageLoaded = true;
global.fishImageLoaded = true;
global.nemoImageLoaded = true;
global.turtleImageLoaded = true;
global.whaleImageLoaded = false; // Simulate one failing image

// Mock light rays
global.lightRays = [
  {x: 200, width: 160},
  {x: 400, width: 160},
  {x: 600, width: 160}
];

// Mock requestAnimationFrame
global.requestAnimationFrame = jest.fn();

// Mock functions to test
global.checkCollision = function(rect1, rect2) {
  return (
    rect1.x < rect2.x + rect2.width &&
    rect1.x + rect1.width > rect2.x &&
    rect1.y < rect2.y + rect2.height &&
    rect1.y + rect1.height > rect2.y
  );
};

