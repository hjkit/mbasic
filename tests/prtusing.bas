10 PRINT "=== Numeric: # digit placeholders ==="
20 PRINT USING "###"; 1
30 PRINT USING "###"; 12
40 PRINT USING "###"; 123
50 PRINT USING "###"; 1234
60 PRINT USING "#"; 0
70 PRINT ""
80 PRINT "=== Decimal points ==="
90 PRINT USING "##.##"; 12.34
100 PRINT USING "##.##"; 1.5
110 PRINT USING "##.##"; 0.12
120 PRINT USING "##.##"; 100.999
130 PRINT USING ".##"; 0.5
140 PRINT ""
150 PRINT "=== Leading/trailing signs ==="
160 PRINT USING "+###"; 123
170 PRINT USING "+###"; -123
180 PRINT USING "###-"; 123
190 PRINT USING "###-"; -123
200 PRINT ""
210 PRINT "=== Commas ==="
220 PRINT USING "#,###"; 1234
230 PRINT USING "#,###"; 123
240 PRINT USING "##,###.##"; 12345.67
250 PRINT USING "##,###.##"; 123.45
260 PRINT ""
270 PRINT "=== Exponential E ==="
280 PRINT USING "##.##^^^^"; 1234.56
290 PRINT USING "##.##^^^^"; 0.0123
300 PRINT USING "##.##^^^^"; -567.89
310 PRINT ""
320 PRINT "=== Dollar signs ==="
330 PRINT USING "$$###.##"; 123.45
340 PRINT USING "$$###.##"; 12.3
350 PRINT USING "$$###.##"; 1.23
360 PRINT ""
370 PRINT "=== Asterisk fill ==="
380 PRINT USING "**###.##"; 123.45
390 PRINT USING "**###.##"; 12.3
400 PRINT USING "**###.##"; 1.23
410 PRINT ""
420 PRINT "=== Both ** and $$ ==="
430 PRINT USING "**$###.##"; 123.45
440 PRINT USING "**$###.##"; 12.3
450 PRINT ""
460 PRINT "=== String: ! first char ==="
470 PRINT USING "!"; "HELLO"
480 PRINT USING "!"; "A"
490 PRINT USING "!"; ""
500 PRINT ""
510 PRINT "=== String: & variable ==="
520 PRINT USING "&"; "HELLO"
530 PRINT USING "&"; "HELLO WORLD"
540 PRINT USING "&"; ""
550 PRINT ""
560 PRINT "=== String: backslash fixed ==="
570 PRINT USING "\ \"; "HELLO"
580 PRINT USING "\  \"; "HELLO"
590 PRINT USING "\    \"; "HELLO"
600 PRINT USING "\ \"; "AB"
610 PRINT ""
620 PRINT "=== Multiple values ==="
630 PRINT USING "## ##"; 12; 34
640 PRINT USING "## ## ##"; 1; 2; 3
650 PRINT USING "& &"; "AB"; "CD"
660 PRINT ""
670 PRINT "=== Mixed types ==="
680 PRINT USING "& ###"; "NUM"; 123
690 PRINT USING "###.## &"; 45.67; "END"
700 PRINT ""
710 PRINT "=== Edge: negative zero ==="
720 PRINT USING "+###.##"; -0.001
730 PRINT USING "+###.##"; 0.001
740 PRINT ""
750 PRINT "=== Edge: overflow ==="
760 PRINT USING "##"; 999
770 PRINT USING "##"; 1000
780 PRINT ""
790 PRINT "=== Edge: rounding ==="
800 PRINT USING "###.#"; 123.45
810 PRINT USING "###.#"; 123.49
820 PRINT USING "###.#"; 123.5
830 PRINT USING "###.#"; 123.95
840 PRINT ""
850 PRINT "=== Literals in format ==="
860 PRINT USING "Amount: $###.##"; 123.45
870 PRINT USING "(###) ###-####"; 555; 1234
880 PRINT ""
890 PRINT "=== Empty string formats ==="
900 PRINT USING ""; 123
910 END
