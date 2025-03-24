// Setup for my Whack-A-Waste tests

document.body.innerHTML = `
  <div id="score">0</div>
  <div id="level">1</div>
  <div id="mistakes">0</div>
  <div id="game-board"></div>
`;

// Set up game variables
global.score = 0;
global.level = 1;
global.mistakes = 0;
global.activeItems = {};
global.gameRunning = true;

// Set up DOM references
global.gameBoard = document.getElementById('game-board');
global.scoreDisplay = document.getElementById('score');
global.levelDisplay = document.getElementById('level');
global.mistakesDisplay = document.getElementById('mistakes');

// Mock the game functions we need for testing

// Function to calculate how long items stay on screen
global.calculateItemDuration = function() {
  const baseDuration = 3000;
  const decrement = 200 * (global.level - 1);
  return Math.max(1000, baseDuration - decrement);
};

// Function to calculate how fast new items appear
global.calculateSpawnDelay = function() {
  const baseDelay = 2000;
  const decrement = 100 * (global.level - 1);
  return Math.max(500, baseDelay - decrement);
};

// Function to check if player levels up
global.checkLevelUp = function() {
  const newLevel = 1 + Math.floor(global.score / 100);
  if (newLevel > global.level) {
    global.level = newLevel;
    global.levelDisplay.textContent = global.level;
  }
};

// Food types from the game
global.FOOD_TYPES = {
  'fresh': { action: 'none', score: 0, penalty: -10, color: '#81c784' },
  'expiring': { action: 'tap', score: 20, penalty: -15, color: '#fff176' },
  'rotten': { action: 'tap', score: 15, penalty: -20, color: '#e57373' },
  'trash': { action: 'none', score: 0, penalty: -25, color: '#757575' }
};

// Other game constants
global.HOLE_COUNT = 9;
global.MAX_MISTAKES = 5;
global.LEVEL_UP_SCORE = 100;

// Create mock functions that we can check if they were called
global.removeFoodItem = jest.fn();
global.showFeedback = jest.fn();
global.endGame = jest.fn();

// Mock the main interaction function
global.processInteraction = function(holeId, action) {
  if (!global.activeItems[holeId]) return;
  
  const foodType = global.activeItems[holeId].type;
  const correctAction = global.FOOD_TYPES[foodType].action;
  
  // Check if action was correct
  if (action === correctAction) {
    // Correct action
    if (action === 'tap') {
      // Award points for tapping when appropriate
      global.score += global.FOOD_TYPES[foodType].score;
    }
  } else {
    // Incorrect action
    global.score += global.FOOD_TYPES[foodType].penalty;
    global.mistakes++;
    global.mistakesDisplay.textContent = global.mistakes;
    
    if (global.mistakes >= global.MAX_MISTAKES) {
      global.endGame();
    }
  }
  
  // Update score display
  global.scoreDisplay.textContent = global.score;
  
  // Check for level up
  global.checkLevelUp();
  
  // Remove food item
  global.removeFoodItem(holeId);
};
