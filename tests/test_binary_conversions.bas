10 REM Test binary conversion functions CVI/CVS/CVD and MKI$/MKS$/MKD$
20 PRINT "Testing binary conversion functions"
30 PRINT
40 REM Test 1: Integer conversions (MKI$ and CVI)
50 PRINT "Test 1: Integer conversions"
60 I = 12345
70 S$ = MKI$(I)
80 I2 = CVI(S$)
90 PRINT "  Original:"; I; " Converted back:"; I2
100 IF I = I2 THEN PRINT "  PASS" ELSE PRINT "  FAIL"
110 PRINT
120 REM Test 2: Negative integer
130 PRINT "Test 2: Negative integer"
140 I = -5678
150 S$ = MKI$(I)
160 I2 = CVI(S$)
170 PRINT "  Original:"; I; " Converted back:"; I2
180 IF I = I2 THEN PRINT "  PASS" ELSE PRINT "  FAIL"
190 PRINT
200 REM Test 3: Single-precision float (MKS$ and CVS)
210 PRINT "Test 3: Single-precision float"
220 F! = 3.14159
230 S$ = MKS$(F!)
240 F2! = CVS(S$)
250 PRINT "  Original:"; F!; " Converted back:"; F2!
260 IF ABS(F! - F2!) < 0.0001 THEN PRINT "  PASS" ELSE PRINT "  FAIL"
270 PRINT
280 REM Test 4: Double-precision float (MKD$ and CVD)
290 PRINT "Test 4: Double-precision float"
300 D# = 2.718281828459045
310 S$ = MKD$(D#)
320 D2# = CVD(S$)
330 PRINT "  Original:"; D#; " Converted back:"; D2#
340 IF ABS(D# - D2#) < 0.0000000001 THEN PRINT "  PASS" ELSE PRINT "  FAIL"
350 PRINT
360 REM Test 5: Zero values
370 PRINT "Test 5: Zero values"
380 I = 0
390 F! = 0
400 D# = 0
410 IF CVI(MKI$(I)) = 0 THEN PRINT "  Integer zero: PASS" ELSE PRINT "  Integer zero: FAIL"
420 IF CVS(MKS$(F!)) = 0 THEN PRINT "  Single zero: PASS" ELSE PRINT "  Single zero: FAIL"
430 IF CVD(MKD$(D#)) = 0 THEN PRINT "  Double zero: PASS" ELSE PRINT "  Double zero: FAIL"
440 PRINT
450 REM Test 6: Large values
460 PRINT "Test 6: Large values"
470 I = 32767
480 F! = 12345.6789
490 D# = 9876543210.123456
500 IF CVI(MKI$(I)) = I THEN PRINT "  Max int: PASS" ELSE PRINT "  Max int: FAIL"
510 IF ABS(CVS(MKS$(F!)) - F!) < 0.001 THEN PRINT "  Large single: PASS" ELSE PRINT "  Large single: FAIL"
520 IF ABS(CVD(MKD$(D#)) - D#) < 0.001 THEN PRINT "  Large double: PASS" ELSE PRINT "  Large double: FAIL"
530 PRINT
540 PRINT "All binary conversion tests complete!"
550 END
