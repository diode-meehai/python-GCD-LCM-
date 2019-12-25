#https://gist.github.com/endolith/114336/eff2dc13535f139d0d6a2db68597fad2826b53c3
#gcd = 1
lcm = []

l = []
# ตัวแปร gcd ใช้เก็บค่า หรม. , lcm ใช้เก็บค่า ครน.
# gcd กำหนดค่าเริ่มต้นเป็น 1 เพราะเป็นตัวแปรที่เกี่ยวข้องกับการ
# คูณหรือหาร

a = int(input("Please input first number : "))
b = int(input("Please input second number : "))
c = int(input("Please Third second number : "))

l.append(a)
l.append(b)
l.append(c)
print(l)

# GCD of more than two (or array) numbers 
# This function implements the Euclidian  
# algorithm to find H.C.F. of two number 
  
def find_gcd(x, y): # หรม.
    while(y): 
        x, y = y, x % y #Modulo ได้ตัวเศษ
        print("y = " + str(y))
    return x 


def find_lcm(a, b): #ครน
    """Compute the lowest common multiple of a and b"""
    return a * b / find_gcd(a, b)
      
      
#l = [2, 4, 6, 8, 16] 
  
num1=l[0] 
num2=l[1] 
gcd = find_gcd(num1,num2) 
print("หรม 2 ตัวแรก: " + str(gcd)  )

lcm_C = find_lcm(num1,num2) # สูตรการหา ครน. เมื่อได้ หรม.แล้ว
lcm.append(lcm_C)
print("ครน 2 ตัวแรก: " + str(lcm))
print("======================")
  
#for i in range(2,len(l)):  #ไล่ทุกตัว
for i in range(2):  #คิดร่วมตัวที่ 3
    print(i)
    print("i: " + str(l[i]))
    print("i1 คู่ถัดไป: " + str(l[i+1]))
    
    gcd=find_gcd(gcd,l[i]) 
    print("หรม. gcd: " + str(gcd))
    
    
    lcm_CC = find_lcm(lcm[i] , l[i+1])
    #lcm_CC = find_lcm(l[i] , l[i+1])
    lcm.append(lcm_CC)
    print("ครน. lcm: " + str(lcm[i]))
    
    print("------------")

print("ครน 3 ตัว: " + str((lcm))) #ครน. คู่แรก บวก กับ คู่สอง
print("ครน 3 ตัว: " + str((lcm[-1])))
print("หรม 3 ตัว: " + str(gcd)) 

    
# Code contributed by Mohit Gupta_OMG 
