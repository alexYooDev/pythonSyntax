treeHit = 0
while treeHit < 10:
  treeHit += 1
  if treeHit == 1:
    print("%dst hit" %treeHit)
  elif treeHit == 2:
    print("%dnd hit" %treeHit)
  elif treeHit == 3:
    print("%drd hit" %treeHit)
  else: print("%dth hit" %treeHit)
  if(treeHit==10): print('The tree is falling down')