def tri(tableau:list):
   
   listBase = tableau
   list0 = []
   list1 = []
   len_tab = len(tableau)
   
   i = 0
   
   while i < len_tab:
          
       popped = listBase.pop(i)
       len_tab -= 1
          
       if popped == 0:

           list0.append(0) 
           
       elif popped == 1:

           list1.append(1)
           
       i += 1
       
   listBase.extend(list0)
   listBase.extend(list1)
   
   return listBase[::-1]
        
              
print(tri([0,1,0,1,0,1,0,1,0]))