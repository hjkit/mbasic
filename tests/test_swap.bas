10 REM Test SWAP statement
20 PRINT "=== Simple Variable SWAP Tests ==="
30 PRINT
40 REM Test 1: Integer variables
50 A% = 10
60 B% = 20
70 PRINT "Before SWAP: A%="; A%; ", B%="; B%
80 SWAP A%, B%
90 PRINT "After SWAP:  A%="; A%; ", B%="; B%
100 IF A% = 20 AND B% = 10 THEN PRINT "Test 1: PASS" ELSE PRINT "Test 1: FAIL"
110 PRINT
120 REM Test 2: String variables
130 X$ = "HELLO"
140 Y$ = "WORLD"
150 PRINT "Before SWAP: X$="; X$; ", Y$="; Y$
160 SWAP X$, Y$
170 PRINT "After SWAP:  X$="; X$; ", Y$="; Y$
180 IF X$ = "WORLD" AND Y$ = "HELLO" THEN PRINT "Test 2: PASS" ELSE PRINT "Test 2: FAIL"
190 PRINT
200 REM Test 3: Float variables
210 C! = 3.14
220 D! = 2.71
230 PRINT "Before SWAP: C!="; C!; ", D!="; D!
240 SWAP C!, D!
250 PRINT "After SWAP:  C!="; C!; ", D!="; D!
260 IF C! = 2.71 AND D! = 3.14 THEN PRINT "Test 3: PASS" ELSE PRINT "Test 3: FAIL"
270 PRINT
280 PRINT "=== Array Element SWAP Tests ==="
290 PRINT
300 REM Test 4: Array elements
310 DIM ARR(5)
320 ARR(1) = 100
330 ARR(2) = 200
340 PRINT "Before SWAP: ARR(1)="; ARR(1); ", ARR(2)="; ARR(2)
350 SWAP ARR(1), ARR(2)
360 PRINT "After SWAP:  ARR(1)="; ARR(1); ", ARR(2)="; ARR(2)
370 IF ARR(1) = 200 AND ARR(2) = 100 THEN PRINT "Test 4: PASS" ELSE PRINT "Test 4: FAIL"
380 PRINT
390 REM Test 5: Variable with array element
400 E% = 50
410 ARR(3) = 60
420 PRINT "Before SWAP: E%="; E%; ", ARR(3)="; ARR(3)
430 SWAP E%, ARR(3)
440 PRINT "After SWAP:  E%="; E%; ", ARR(3)="; ARR(3)
450 IF E% = 60 AND ARR(3) = 50 THEN PRINT "Test 5: PASS" ELSE PRINT "Test 5: FAIL"
460 PRINT
470 PRINT "=== Mixed Type SWAP Tests ==="
480 PRINT
490 REM Test 6: Default type variables (implicitly single precision)
500 F = 99
510 G = 88
520 PRINT "Before SWAP: F="; F; ", G="; G
530 SWAP F, G
540 PRINT "After SWAP:  F="; F; ", G="; G
550 IF F = 88 AND G = 99 THEN PRINT "Test 6: PASS" ELSE PRINT "Test 6: FAIL"
560 PRINT
570 PRINT "All SWAP tests complete!"
580 END
