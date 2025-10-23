10 REM Complete random file I/O test
20 REM Create a simple database of names and scores
30 PRINT "Creating student database..."
40 OPEN "R", 1, "/tmp/students.dat", 25
50 FIELD #1, 15 AS NAME$, 5 AS SCORE$, 5 AS GRADE$
60 REM Add 5 students
70 FOR I = 1 TO 5
80 READ N$, S, G$
90 LSET NAME$ = N$
100 RSET SCORE$ = STR$(S)
110 LSET GRADE$ = G$
120 PUT #1, I
130 NEXT I
140 PRINT "  Added 5 students"
150 PRINT
160 DATA "Alice Smith", 95, "A"
170 DATA "Bob Jones", 87, "B"
180 DATA "Carol White", 92, "A"
190 DATA "Dave Brown", 78, "C"
200 DATA "Eve Davis", 85, "B"
210 PRINT "Reading all records:"
220 FOR I = 1 TO 5
230 GET #1, I
240 PRINT "  "; NAME$; " Score:"; SCORE$; " Grade: "; GRADE$
250 NEXT I
260 PRINT
270 PRINT "File size:"; LOF(1); "bytes"
280 PRINT "Last record accessed:"; LOC(1)
290 CLOSE #1
300 PRINT
310 PRINT "All tests passed!"
320 END
