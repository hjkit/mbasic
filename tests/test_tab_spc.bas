10 REM Test TAB and SPC functions
20 PRINT "Test 1: TAB function"
30 PRINT "A"; TAB(10); "B"; TAB(20); "C"
40 PRINT "Should show: A at 1, B at 10, C at 20"
50 PRINT
60 PRINT "Test 2: SPC function"
70 PRINT "X"; SPC(5); "Y"; SPC(10); "Z"
80 PRINT "Should show: X, 5 spaces, Y, 10 spaces, Z"
90 PRINT
100 PRINT "Test 3: Combined TAB and SPC"
110 PRINT TAB(5); "Start"; SPC(3); "Middle"; TAB(30); "End"
120 PRINT
130 PRINT "Test 4: TAB with numbers"
140 PRINT TAB(10); 123; TAB(20); 456; TAB(30); 789
150 PRINT
160 PRINT "Test 5: Multiple lines with TAB"
170 FOR I = 1 TO 3
180 PRINT "Line"; I; TAB(15); "Col 15"; TAB(30); "Col 30"
190 NEXT I
200 PRINT
210 PRINT "All TAB/SPC tests complete!"
220 END
