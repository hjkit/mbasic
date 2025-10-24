10 REM Math Comparison Test
20 REM Float vs Double Precision
30 PRINT "Math Precision Comparison Test"
40 PRINT "==============================="
50 PRINT
100 REM Test ATN at key points
110 PRINT "ATN (Arctangent) Test Points:"
120 PRINT "X", "ATN(X)"
130 PRINT "---", "------"
140 X = 0: PRINT X, ATN(X)
150 X = 0.1: PRINT X, ATN(X)
160 X = 0.5: PRINT X, ATN(X)
170 X = 0.7071068: PRINT X, ATN(X)
180 X = 1: PRINT X, ATN(X)
190 X = 1.5: PRINT X, ATN(X)
200 X = 2: PRINT X, ATN(X)
210 X = 10: PRINT X, ATN(X)
220 X = 100: PRINT X, ATN(X)
230 PRINT
300 REM Test SIN at key points
310 PRINT "SIN Test Points:"
320 PRINT "X (radians)", "SIN(X)"
330 PRINT "-----------", "------"
340 X = 0: PRINT X, SIN(X)
350 X = 0.5236: PRINT X, SIN(X)
360 X = 0.7854: PRINT X, SIN(X)
370 X = 1.0472: PRINT X, SIN(X)
380 X = 1.5708: PRINT X, SIN(X)
390 X = 3.1416: PRINT X, SIN(X)
400 X = 6.2832: PRINT X, SIN(X)
410 PRINT
500 REM Test COS at key points
510 PRINT "COS Test Points:"
520 PRINT "X (radians)", "COS(X)"
530 PRINT "-----------", "------"
540 X = 0: PRINT X, COS(X)
550 X = 0.5236: PRINT X, COS(X)
560 X = 0.7854: PRINT X, COS(X)
570 X = 1.5708: PRINT X, COS(X)
580 X = 3.1416: PRINT X, COS(X)
590 PRINT
700 REM Test ATN identity
710 PRINT "ATN Identity: ATN(1/X)+ATN(X) = PI/2"
720 PRINT "X", "Result", "Error"
730 PRINT "-", "------", "-----"
740 FOR I = 1 TO 5
750   READ X
760   R = ATN(1/X) + ATN(X)
770   E = ABS(R - 1.5708)
780   PRINT X, R, E
790 NEXT I
800 DATA 0.5, 1.0, 2.0, 5.0, 10.0
810 PRINT
900 REM Test Pythagorean identity
910 PRINT "Pythagorean: SIN^2+COS^2 = 1"
920 PRINT "X", "Result", "Error"
930 PRINT "-", "------", "-----"
940 FOR I = 1 TO 5
950   READ X
960   S = SIN(X): C = COS(X)
970   R = S*S + C*C
980   E = ABS(R - 1)
990   PRINT X, R, E
1000 NEXT I
1010 DATA 0, 0.7854, 1.5708, 3.1416, 6.2832
1020 PRINT
1100 REM Division precision
1110 PRINT "Division Tests:"
1120 R = (1/3) * 3
1130 PRINT "1/3 * 3 =", R, "Error=", ABS(R-1)
1140 R = (1/7) * 7
1150 PRINT "1/7 * 7 =", R, "Error=", ABS(R-1)
1160 R = (1/49) * 49
1170 PRINT "1/49*49 =", R, "Error=", ABS(R-1)
1180 PRINT
1200 PRINT "Test Complete"
9999 SYSTEM
