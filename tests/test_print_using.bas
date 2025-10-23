10 REM Test PRINT USING - comprehensive format testing
20 PRINT "=== String Field Tests ==="
30 A$ = "HELLO": B$ = "WORLD"
40 PRINT "Test 1: First character only (!)"
50 PRINT USING "!"; A$
60 PRINT "Expected: H"
70 PRINT
80 PRINT "Test 2: Fixed width (\ \)"
90 PRINT USING "\ \"; A$
100 PRINT "Expected: HEL (3 chars: 2+1 space)"
110 PRINT
120 PRINT "Test 3: Fixed width with spaces (\   \)"
130 PRINT USING "\   \"; A$
140 PRINT "Expected: HELLO"
150 PRINT
160 PRINT "Test 4: Variable length (&)"
170 PRINT USING "&"; A$
180 PRINT "Expected: HELLO"
190 PRINT
200 PRINT "=== Numeric Field Tests - Basic ==="
210 PRINT "Test 5: Basic digit positions (###)"
220 PRINT USING "###"; 123
230 PRINT "Expected: 123"
240 PRINT
250 PRINT "Test 6: Decimal point (#.##)"
260 PRINT USING "#.##"; 1.23
270 PRINT "Expected: 1.23"
280 PRINT
290 PRINT "Test 7: Rounding (##.##)"
300 PRINT USING "##.##"; 12.678
310 PRINT "Expected: 12.68"
320 PRINT
330 PRINT "Test 8: Right justify (####)"
340 PRINT USING "####"; 42
350 PRINT "Expected:   42"
360 PRINT
370 PRINT "=== Sign Tests ==="
380 PRINT "Test 9: Leading sign (+###)"
390 PRINT USING "+###"; 123
400 PRINT "Expected: +123"
410 PRINT
420 PRINT "Test 10: Leading sign negative (+###)"
430 PRINT USING "+###"; -45
440 PRINT "Expected:  -45 (4 chars: 3 digits + 1 sign)"
450 PRINT
460 PRINT "Test 11: Trailing sign (###-)"
470 PRINT USING "###-"; -67
480 PRINT "Expected:  67- (4 chars: 3 digits + 1 sign)"
490 PRINT
500 PRINT "=== Dollar Sign Tests ==="
510 PRINT "Test 12: Dollar sign ($$###.##)"
520 PRINT USING "$$###.##"; 123.45
530 PRINT "Expected:  $123.45 ($$ + 3 digits + . + 2 digits = 8 chars)"
540 PRINT
550 PRINT "=== Asterisk Fill Tests ==="
560 PRINT "Test 13: Asterisk fill (**###.##)"
570 PRINT USING "**###.##"; 12.34
580 PRINT "Expected: ***12.34 (** + 3 digits + . + 2 digits = 8 chars)"
590 PRINT
600 PRINT "Test 14: Asterisk + dollar (**$###.##)"
610 PRINT USING "**$###.##"; 5.67
620 PRINT "Expected: ****$5.67 (**$ + 3 digits + . + 2 digits = 10 chars)"
630 PRINT
640 PRINT "=== Comma Separator Tests ==="
650 PRINT "Test 15: Thousand separators (##,###.##)"
660 PRINT USING "##,###.##"; 1234.56
670 PRINT "Expected:  1,234.56 (comma counts as position)"
680 PRINT
690 PRINT "=== Overflow Test ==="
700 PRINT "Test 16: Number too large (##.##)"
710 PRINT USING "##.##"; 123.45
720 PRINT "Expected: %123.45"
730 PRINT
740 PRINT "=== Literal Characters Test ==="
750 PRINT "Test 17: Literal with underscore (_!##)"
760 PRINT USING "_!##"; 42
770 PRINT "Expected: !42"
780 PRINT
790 PRINT "=== Multiple Values Test ==="
800 PRINT "Test 18: Multiple values (## ## ##)"
810 PRINT USING "## ## ##"; 10; 20; 30
820 PRINT "Expected: 10 20 30"
830 PRINT
840 PRINT "All PRINT USING tests complete!"
850 END
