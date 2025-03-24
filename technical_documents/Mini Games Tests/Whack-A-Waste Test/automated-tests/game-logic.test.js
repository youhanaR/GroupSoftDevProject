// My test file for Whack-A-Waste game


// Test the game's core functions
describe('Game basics', () => {
    // Reset values before each test
    beforeEach(() => {
      score = 0;
      level = 1;
      mistakes = 0;
      document.getElementById('score').textContent = '0';
      document.getElementById('level').textContent = '1';
      document.getElementById('mistakes').textContent = '0';
    });
  
    // Test the calculateItemDuration function
    test('calculateItemDuration works correctly', () => {
      // Level 1 should be 3000ms
      expect(calculateItemDuration()).toBe(3000);
      
      // Level 5 should be faster
      level = 5;
      expect(calculateItemDuration()).toBe(2200);
      
      // Level 15 should be minimum speed
      level = 15;
      expect(calculateItemDuration()).toBe(1000);
    });
  
    // Test the spawn delay calculation
    test('calculateSpawnDelay works correctly', () => {
      // Level 1 delay
      expect(calculateSpawnDelay()).toBe(2000);
      
      // Level 10 delay
      level = 10;
      expect(calculateSpawnDelay()).toBe(1100);
    });
  
    // Test level up function
    test('checkLevelUp works correctly', () => {
      // Should not level up at 99 points
      score = 99;
      checkLevelUp();
      expect(level).toBe(1);
      
      // Should level up at 100 points
      score = 100;
      checkLevelUp();
      expect(level).toBe(2);
    });
  });
  
  // Test food interactions
  describe('Food interaction tests', () => {
    beforeEach(() => {
      // Reset everything
      score = 0;
      level = 1;
      mistakes = 0;
      activeItems = {};
      
      // Create a test food item
      const foodItem = document.createElement('div');
      foodItem.className = 'food-item';
      document.body.appendChild(foodItem);
      
      // Clear mock function calls
      removeFoodItem.mockClear();
    });
  
    // Test tapping expiring food (should be correct)
    test('Tapping expiring food gives points', () => {
      // Create an expiring food item
      activeItems[1] = {
        type: 'expiring',
        element: document.createElement('div')
      };
      
      // Tap it
      processInteraction(1, 'tap');
      
      // Check results
      expect(score).toBe(20); // Should get 20 points
      expect(mistakes).toBe(0); // No mistakes
      expect(removeFoodItem).toHaveBeenCalledWith(1); // Item should be removed
    });
    
    // Test tapping fresh food (should be wrong)
    test('Tapping fresh food causes mistake', () => {
      // Create a fresh food item
      activeItems[1] = {
        type: 'fresh',
        element: document.createElement('div')
      };
      
      // Tap it (incorrect action)
      processInteraction(1, 'tap');
      
      // Check results
      expect(score).toBe(-10); // Should lose 10 points
      expect(mistakes).toBe(1); // One mistake
      expect(removeFoodItem).toHaveBeenCalledWith(1); // Item should be removed
    });
    
    // Test game over condition
    test('Game ends after 5 mistakes', () => {
      // Start with 4 mistakes
      mistakes = 4;
      
      // Create a fresh food item
      activeItems[1] = {
        type: 'fresh',
        element: document.createElement('div')
      };
      
      // Tap it to cause the 5th mistake
      processInteraction(1, 'tap');
      
      // Check if game over was triggered
      expect(mistakes).toBe(5);
      expect(endGame).toHaveBeenCalled();
    });
  });
  
