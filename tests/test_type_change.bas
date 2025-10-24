100 rem test changing the type of a variable at run time
110 a=1 : b=2
120 gosub 1000
130 print c
140 a=1.1 : b=2.2
150 gosub 1000
155 print c
160 x# = 1.11 : y# = 2.22
170 a=x# : b=y#
180 gosub 1000
190 print c
200 end
1000 rem do some sort of math we dont know precision
1010 c=a+b
1020 return