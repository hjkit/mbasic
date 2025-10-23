10 REM Test binary data in random files using MKI$/MKS$/MKD$ and CVI/CVS/CVD
20 PRINT "Testing binary random file I/O"
30 PRINT
40 REM Open random file with 14-byte records (2+4+8 bytes)
50 OPEN "R", 1, "/tmp/binary_test.dat", 14
60 FIELD #1, 2 AS I$, 4 AS F$, 8 AS D$
70 PRINT "Writing binary data to file..."
80 REM Write 3 records with binary numeric data
90 FOR N = 1 TO 3
100 LSET I$ = MKI$(N * 100)
110 LSET F$ = MKS$(N * 3.14159)
120 LSET D$ = MKD$(N * 2.718281828)
130 PUT #1, N
140 NEXT N
150 PRINT "  Wrote 3 records"
160 PRINT
170 REM Read back the binary data
180 PRINT "Reading binary data from file:"
190 FOR N = 1 TO 3
200 GET #1, N
210 IV = CVI(I$)
220 FV = CVS(F$)
230 DV = CVD(D$)
240 PRINT "  Record"; N; ": Int="; IV; " Single="; FV; " Double="; DV
250 NEXT N
260 PRINT
270 REM Verify the data
280 PRINT "Verification:"
290 GET #1, 1
300 IF CVI(I$) = 100 THEN PRINT "  Record 1 int: PASS" ELSE PRINT "  Record 1 int: FAIL"
310 GET #1, 2
320 IF CVI(I$) = 200 THEN PRINT "  Record 2 int: PASS" ELSE PRINT "  Record 2 int: FAIL"
330 GET #1, 3
340 IF CVI(I$) = 300 THEN PRINT "  Record 3 int: PASS" ELSE PRINT "  Record 3 int: FAIL"
350 PRINT
360 CLOSE #1
370 PRINT "Binary file I/O test complete!"
380 END
