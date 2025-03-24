Whack-A-Waste Test Results
Tested by: Jood
Date: March 20-22, 2025
Overall Results
I found a few issues but the game works pretty well overall!
Test TypeTests DonePassedFailedNotesBasic Features12102Game mechanics work but found scoring issueEdge Cases633Tab switching and mobile have problemsPerformance211Works fine on desktop but slow on older phonesBrowsers431Safari has animation glitchesUser Testing321My roommate found it confusing at first
Specific Test Results
Basic Game Features
✅ Game starts correctly - Score, level, mistakes all initialize at correct values
✅ Food items spawn randomly from holes
✅ Clicking expiring food (yellow) gives 20 points
✅ Clicking rotten food (red) gives 15 points
✅ NOT clicking fresh food works correctly
✅ NOT clicking trash works correctly
✅ Mistake counter increases for wrong actions
❌ ISSUE: Sometimes score doesn't update right away when tapping multiple items quickly
✅ Game ends after 5 mistakes
✅ Play again button works correctly
✅ Animations work for food items
❌ ISSUE: Sometimes feedback text like "Repurposed!" stays on screen too long
Edge Cases
❌ ISSUE: Game continues running when switching tabs
❌ ISSUE: Rapid clicking on multiple food items can cause visual glitches
✅ Negative scores display correctly
✅ Window resizing works OK on desktop
❌ ISSUE: Game is hard to play on very small mobile screens
✅ No memory leaks found during 15-minute play session
Browser Testing
✅ Chrome - Works perfectly
✅ Firefox - Works with minor animation differences
❌ ISSUE: Safari - Particle effects sometimes don't appear
✅ Mobile Chrome - Works but buttons are a bit small
User Testing Feedback
I had 3 friends test the game:
Alex (plays a lot of games):

Figured out the mechanics quickly
Got to level 4
Suggested adding sound effects
Said the game was fun but got repetitive

Sam (doesn't play many games):

Took about 1 minute to understand what to do
Found the yellow/green colors a bit confusing
Liked the educational aspect
Thought level progression was too slow

Jamie (on mobile):
❌ ISSUE: Had trouble with touch accuracy on small screen

Suggested making tap areas larger
Liked the animations
Learned about food waste concepts

To Fix

Fix the tab switching issue - game should pause when tab is not active
Fix the visual glitches with rapid clicking
Improve mobile experience with larger tap areas
Fix Safari particle effect issue
Make sure score updates immediately
Consider adding sound effects (Alex's suggestion)
Maybe make yellow/green colors more distinct (Sam's feedback)

Notes for Next Time
Testing on mobile was really important - found issues I wouldn't have caught otherwise. Should test on more devices next time.
The game is actually pretty fun once you get the hang of it! I got to level 6 during testing.