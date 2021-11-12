"""
Define a function diamond that takes a single integer input size. The function then prints (doesn't have to return) a hollow diamond made of asterisks.

Hint: <string>.center(2*size - 1) may be helpful in your code (for center aligning)

Examples of what should appear:

diamond(4) -->
   *   
  * *  
 *   * 
*     *
 *   * 
  * *  
   * 

diamond(5) -->
      *      
     * *     
    *   *    
   *     *   
  *       *  
 *         * 
*           *
 *         * 
  *       *  
   *     *   
    *   *    
     * *     
      * 
"""

def diamond(size):
  star="*"
  print(star.center(2*size-1))
  for i in range(1, size+1):
    for j in range(1,size-i+1):
      print('',end='')
    for j in range(1,2*i):
      if j==1 or j==2*i-1:
        print('*', end='')
      else:
        print('', end='')
  for i in range(size-1,0,-1):
    for j in range (1,size-i+1):
      print('',end="")
    for j in range(1,2*i):
      if j==1 or j==2*i:
        print('*',end='')
      else:
        print('',end='')
  print(star.center(2*size-1))

      
