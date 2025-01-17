# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  # getSuccessors return (successor, action, stepCost)
  
  from util import Stack
  
  stk = Stack()   # 2-tuple
  visit = set()
  #print problem.getStartState()
  #print problem.getSuccessors(problem.getStartState())
  curr = problem.getStartState()
  stk.push((curr, []))
  visit.add(curr)
  
  while stk.isEmpty() is False:
    curr = stk.pop()
    if problem.isGoalState(curr[0]) is True:
      return curr[1]
    for nxt in problem.getSuccessors(curr[0]):
      if nxt[0] not in visit:
        stk.push((nxt[0], curr[1]+[nxt[1]]))
        visit.add(nxt[0])
  print "No Path!"
  exit()    
  util.raiseNotDefined()

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  from util import Queue
  
  que = Queue() # 2-tuple
  visit = set()
  curr = problem.getStartState()
  que.push((curr, []))
  visit.add(curr)
  
  while que.isEmpty() is False:
    curr = que.pop()
    if problem.isGoalState(curr[0]) is True:
      return curr[1]
    for nxt in problem.getSuccessors(curr[0]):
      if nxt[0] not in visit:
        que.push((nxt[0], curr[1]+[nxt[1]]))
        visit.add(nxt[0])
  print "No Path!"
  exit()
  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  from util import PriorityQueue
  
  pque = PriorityQueue()
  visit = set()
  curr = problem.getStartState()
  pque.push((curr, [], 0), 0) # third tuple store cost until it
  
  while pque.isEmpty() is False:
    curr = pque.pop()
    #print 'Start', curr
    if curr[0] in visit:
      continue
    visit.add(curr[0])
    if problem.isGoalState(curr[0]) is True:
      return curr[1]
    for nxt in problem.getSuccessors(curr[0]):
      if nxt[0] in visit:
        continue
      cost = curr[2]+nxt[2]
      pque.push((nxt[0], curr[1]+[nxt[1]], cost), cost)
      #print (nxt[0], curr[1]+[nxt[1]], cost)
                        
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  from util import PriorityQueue
  
  pque = PriorityQueue()
  visit = set()
  curr = problem.getStartState()
  pque.push((curr, [], 0), heuristic(curr, problem))
  
  while pque.isEmpty() is False:
    curr = pque.pop()
    if curr[0] in visit:
      continue
    visit.add(curr[0])
    if problem.isGoalState(curr[0]) is True:
      return curr[1]
    for nxt in problem.getSuccessors(curr[0]):
      if nxt[0] in visit:
        continue
      pque.push((nxt[0], curr[1]+[nxt[1]], curr[2]+nxt[2]), 
                curr[2]+nxt[2]+heuristic(nxt[0], problem)) # f(n) = g(n)+h(n)
  
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch