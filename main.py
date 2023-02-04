#exceptions - ислкючения - ayriqsha jagdaylar
'''try:
    x = int(input("Please enter a number: "))
except ValueError:
    print("Oops!  That was no valid number.  Try again...")
finally:
	print('complete')

try:
	print(a)
except NameError:
	print('joq ozgeriwshini jazip ketkensen')
finally:
	print('completed')'''

'''try:
	print(2/0)
except Exception:
	print('Chto-to poshle ne tak')
finally:
	print('compeled')'''

#files #'r' - read, 'w' - write , 'a' - append
'''file = open('file.txt','r')
text_copy = file.read()
print(text_copy)
file.close()'''

file = open('file.txt','w')
file.write(   '''     
          |\_|\
          | a_a\
          | | "]
      ____| '-\___
     /.----.___.-'\
    //        _    \
   //   .-. (~v~) /|
  |'|  /\:  .--  / \
 // |-/  \_/____/\/~|
|/  \ |  []_|_|_] \ |
| \  | \ |___   _\ ]_}
| |  '-' /   '.'  |
| |     /    /|:  | 
| |     |   / |:  /\
| |     /  /  |  /  \
| |    |  /  /  |    \
\ |    |/\/  |/|/\    \
 \|\ |\|  |  | / /\/\__\
  \ \| | /   | |__
       / |   |____)
       |_/
       ''')
file.close()


file = open('file.txt','w')

for i in range(1,30):
	file.write(str(i))
	file.write('\n')
file.close()