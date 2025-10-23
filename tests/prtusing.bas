10 PRINT "=== Basic # digit placeholders ==="
20 PRINT USING "#"; 0
30 PRINT USING "#"; 5
40 PRINT USING "#"; 9
50 PRINT USING "##"; 0
60 PRINT USING "##"; 7
70 PRINT USING "##"; 42
80 PRINT USING "##"; 99
90 PRINT USING "###"; 1
100 PRINT USING "###"; 12
110 PRINT USING "###"; 123
120 PRINT USING "###"; 1234
130 PRINT USING "####"; 9999
140 PRINT USING "#####"; 12345
150 PRINT ""
160 PRINT "=== Decimal formats ==="
170 PRINT USING "#.#"; 1.2
180 PRINT USING "#.#"; 9.9
190 PRINT USING "#.##"; 1.23
200 PRINT USING "#.##"; 9.87
210 PRINT USING "##.#"; 12.5
220 PRINT USING "##.##"; 12.34
230 PRINT USING "##.##"; 1.5
240 PRINT USING "##.##"; 0.12
250 PRINT USING "##.##"; 100.999
260 PRINT USING "###.##"; 456.78
270 PRINT USING "###.###"; 12.345
280 PRINT ""
290 PRINT "=== Leading decimal formats ==="
300 PRINT USING ".#"; 0.5
310 PRINT USING ".#"; 0.9
320 PRINT USING ".##"; 0.5
330 PRINT USING ".##"; 0.99
340 PRINT USING ".##"; 0.01
350 PRINT USING ".###"; 0.123
360 PRINT USING ".###"; 0.999
370 PRINT ""
380 PRINT "=== Leading + sign ==="
390 PRINT USING "+#"; 0
400 PRINT USING "+#"; 5
410 PRINT USING "+#"; -3
420 PRINT USING "+##"; 12
430 PRINT USING "+##"; -45
440 PRINT USING "+###"; 123
450 PRINT USING "+###"; -456
460 PRINT USING "+###.##"; 12.34
470 PRINT USING "+###.##"; -56.78
480 PRINT ""
490 PRINT "=== Trailing + sign ==="
500 PRINT USING "####+"; 123
510 PRINT USING "####+"; -456
520 PRINT USING "###+"; 12
530 PRINT USING "###+"; -34
540 PRINT USING "##.##+"; 12.5
550 PRINT USING "##.##+"; -34.7
560 PRINT ""
570 PRINT "=== Trailing - sign ==="
580 PRINT USING "###-"; 0
590 PRINT USING "###-"; 123
600 PRINT USING "###-"; -456
610 PRINT USING "##-"; 12
620 PRINT USING "##-"; -34
630 PRINT USING "#-"; 5
640 PRINT USING "#-"; -7
650 PRINT USING "##.##-"; 12.34
660 PRINT USING "##.##-"; -56.78
670 PRINT ""
680 PRINT "=== Comma separators ==="
690 PRINT USING "#,###"; 1
700 PRINT USING "#,###"; 12
710 PRINT USING "#,###"; 123
720 PRINT USING "#,###"; 1234
730 PRINT USING "#,###"; 12345
740 PRINT USING "##,###"; 1234
750 PRINT USING "##,###"; 12345
760 PRINT USING "##,###.##"; 1234.56
770 PRINT USING "##,###.##"; 123.45
780 PRINT USING "###,###"; 123456
790 PRINT USING "###,###.##"; 123456.78
800 PRINT ""
810 PRINT "=== Exponential format ==="
820 PRINT USING "##.##^^^^"; 0
830 PRINT USING "##.##^^^^"; 1
840 PRINT USING "##.##^^^^"; 12.34
850 PRINT USING "##.##^^^^"; 123.45
860 PRINT USING "##.##^^^^"; 1234.56
870 PRINT USING "##.##^^^^"; 0.0123
880 PRINT USING "##.##^^^^"; 0.001
890 PRINT USING "##.##^^^^"; -567.89
900 PRINT USING "##.##^^^^"; -0.0045
910 PRINT USING "#.#^^^^"; 99.9
920 PRINT ""
930 PRINT "=== Dollar sign $$ ==="
940 PRINT USING "$$#"; 1
950 PRINT USING "$$#"; 9
960 PRINT USING "$$##"; 12
970 PRINT USING "$$##"; 5
980 PRINT USING "$$###.##"; 123.45
990 PRINT USING "$$###.##"; 12.3
1000 PRINT USING "$$###.##"; 1.23
1010 PRINT USING "$$###.##"; 0.5
1020 PRINT USING "$$#.##"; 5.67
1030 PRINT ""
1040 PRINT "=== Asterisk fill ** ==="
1050 PRINT USING "**#"; 1
1060 PRINT USING "**#"; 9
1070 PRINT USING "**##"; 12
1080 PRINT USING "**##"; 5
1090 PRINT USING "**###.##"; 123.45
1100 PRINT USING "**###.##"; 12.3
1110 PRINT USING "**###.##"; 1.23
1120 PRINT USING "**###.##"; 0.99
1130 PRINT ""
1140 PRINT "=== Combined **$ ==="
1150 PRINT USING "**$#"; 5
1160 PRINT USING "**$##"; 12
1170 PRINT USING "**$###.##"; 123.45
1180 PRINT USING "**$###.##"; 12.3
1190 PRINT USING "**$###.##"; 1.23
1200 PRINT USING "**$#.##"; 5.67
1210 PRINT ""
1220 PRINT "=== String ! format ==="
1230 PRINT USING "!"; ""
1240 PRINT USING "!"; "A"
1250 PRINT USING "!"; "AB"
1260 PRINT USING "!"; "HELLO"
1270 PRINT USING "!"; "XYZ"
1280 PRINT USING "!"; "1"
1290 PRINT ""
1300 PRINT "=== String & format ==="
1310 PRINT USING "&"; ""
1320 PRINT USING "&"; "A"
1330 PRINT USING "&"; "AB"
1340 PRINT USING "&"; "HELLO"
1350 PRINT USING "&"; "WORLD"
1360 PRINT USING "&"; "HELLO WORLD"
1370 PRINT USING "&"; "BASIC"
1380 PRINT ""
1390 PRINT "=== String backslash format ==="
1400 PRINT USING "\ \"; "A"
1410 PRINT USING "\ \"; "AB"
1420 PRINT USING "\ \"; "ABC"
1430 PRINT USING "\ \"; "ABCD"
1440 PRINT USING "\  \"; "A"
1450 PRINT USING "\  \"; "ABC"
1460 PRINT USING "\  \"; "ABCD"
1470 PRINT USING "\   \"; "HELLO"
1480 PRINT USING "\    \"; "HELLO"
1490 PRINT USING "\     \"; "HELLO"
1500 PRINT ""
1510 PRINT "=== Multiple values ==="
1520 PRINT USING "# #"; 1; 2
1530 PRINT USING "# #"; 5; 9
1540 PRINT USING "## ##"; 12; 34
1550 PRINT USING "## ##"; 56; 78
1560 PRINT USING "## ## ##"; 1; 2; 3
1570 PRINT USING "### ### ###"; 100; 200; 300
1580 PRINT USING "& &"; "AB"; "CD"
1590 PRINT USING "& &"; "HI"; "BYE"
1600 PRINT USING "! !"; "HELLO"; "WORLD"
1610 PRINT ""
1620 PRINT "=== Mixed string and number ==="
1630 PRINT USING "& ##"; "A"; 12
1640 PRINT USING "& ###"; "NUM"; 123
1650 PRINT USING "### &"; 456; "END"
1660 PRINT USING "! ##.#"; "X"; 12.5
1670 PRINT USING "##.## &"; 45.67; "END"
1680 PRINT ""
1690 PRINT "=== Literals in format ==="
1700 PRINT USING "X=#"; 5
1710 PRINT USING "Y=##"; 42
1720 PRINT USING "Total: ###"; 100
1730 PRINT USING "Amount: $###.##"; 123.45
1740 PRINT USING "(###)"; 555
1750 PRINT USING "[##]"; 99
1760 PRINT USING "Cost=$##.##"; 45.99
1770 PRINT ""
1780 PRINT "=== Overflow tests ==="
1790 PRINT USING "#"; 10
1800 PRINT USING "#"; 99
1810 PRINT USING "##"; 100
1820 PRINT USING "##"; 999
1830 PRINT USING "##"; 1000
1840 PRINT USING "###"; 1234
1850 PRINT USING "###"; 9999
1860 PRINT USING "#.#"; 10.5
1870 PRINT USING "#.##"; 99.99
1880 PRINT USING "##.#"; 100.5
1890 PRINT ""
1900 PRINT "=== Negative zero edge cases ==="
1910 PRINT USING "+#.##"; -0.001
1920 PRINT USING "+#.##"; 0.001
1930 PRINT USING "+##.#"; -0.01
1940 PRINT USING "+##.#"; 0.01
1950 PRINT USING "#.##-"; -0.001
1960 PRINT USING "#.##-"; 0.001
1970 PRINT ""
1980 PRINT "=== Rounding edge cases ==="
1990 PRINT USING "#.#"; 1.45
2000 PRINT USING "#.#"; 1.49
2010 PRINT USING "#.#"; 1.5
2020 PRINT USING "#.#"; 1.55
2030 PRINT USING "##.#"; 12.45
2040 PRINT USING "##.#"; 12.49
2050 PRINT USING "##.#"; 12.5
2060 PRINT USING "##.#"; 12.95
2070 PRINT USING "##.##"; 1.995
2080 PRINT USING "##.##"; 1.999
2090 PRINT ""
2100 PRINT "=== Zero handling ==="
2110 PRINT USING "#"; 0
2120 PRINT USING "##"; 0
2130 PRINT USING "###"; 0
2140 PRINT USING "#.#"; 0
2150 PRINT USING "##.##"; 0
2160 PRINT USING "+#"; 0
2170 PRINT USING "#-"; 0
2180 PRINT USING "$$##"; 0
2190 PRINT USING "**##"; 0
2200 PRINT ""
2210 PRINT "=== Random test data ==="
2220 PRINT USING "###"; 7
2230 PRINT USING "###"; 89
2240 PRINT USING "###"; 456
2250 PRINT USING "##.##"; 3.14
2260 PRINT USING "##.##"; 2.71
2270 PRINT USING "##.##"; 98.6
2280 PRINT USING "+###"; 42
2290 PRINT USING "+###"; -17
2300 PRINT USING "###-"; 88
2310 PRINT USING "###-"; -99
2320 PRINT USING "$$###.##"; 99.99
2330 PRINT USING "$$###.##"; 0.99
2340 PRINT USING "**###.##"; 77.77
2350 PRINT USING "#,###"; 5678
2360 PRINT USING "##,###.##"; 9876.54
2370 PRINT ""
2380 PRINT "=== More random numbers ==="
2390 PRINT USING "###"; 234
2400 PRINT USING "###"; 567
2410 PRINT USING "###"; 890
2420 PRINT USING "##.#"; 11.1
2430 PRINT USING "##.#"; 22.2
2440 PRINT USING "##.#"; 33.3
2450 PRINT USING "##.#"; 44.4
2460 PRINT USING "##.#"; 55.5
2470 PRINT USING "##.#"; 66.6
2480 PRINT USING "##.#"; 77.7
2490 PRINT USING "##.#"; 88.8
2500 PRINT USING "##.#"; 99.9
2510 PRINT ""
2520 PRINT "=== Sign and decimal combos ==="
2530 PRINT USING "+#.#"; 1.1
2540 PRINT USING "+#.#"; -2.2
2550 PRINT USING "#.#+"; 3.3
2560 PRINT USING "#.#+"; -4.4
2570 PRINT USING "#.#-"; 5.5
2580 PRINT USING "#.#-"; -6.6
2590 PRINT USING "+##.##"; 12.12
2600 PRINT USING "+##.##"; -34.34
2610 PRINT USING "##.##+"; 56.56
2620 PRINT USING "##.##-"; -78.78
2630 PRINT ""
2640 PRINT "=== Edge: very small decimals ==="
2650 PRINT USING ".#"; 0.1
2660 PRINT USING ".#"; 0.5
2670 PRINT USING ".#"; 0.9
2680 PRINT USING ".##"; 0.01
2690 PRINT USING ".##"; 0.05
2700 PRINT USING ".##"; 0.09
2710 PRINT USING ".##"; 0.99
2720 PRINT USING ".###"; 0.001
2730 PRINT USING ".###"; 0.555
2740 PRINT USING ".###"; 0.999
2750 PRINT ""
2760 PRINT "=== Dollar with different widths ==="
2770 PRINT USING "$$#.#"; 1.2
2780 PRINT USING "$$##.#"; 12.3
2790 PRINT USING "$$###.#"; 123.4
2800 PRINT USING "$$####.##"; 1234.56
2810 PRINT USING "$$#####.##"; 12345.67
2820 PRINT ""
2830 PRINT "=== Asterisk with different widths ==="
2840 PRINT USING "**#.#"; 1.2
2850 PRINT USING "**##.#"; 12.3
2860 PRINT USING "**###.#"; 123.4
2870 PRINT USING "**####.##"; 1234.56
2880 PRINT ""
2890 PRINT "=== Combo **$ different widths ==="
2900 PRINT USING "**$#.#"; 1.2
2910 PRINT USING "**$##.#"; 12.3
2920 PRINT USING "**$###.#"; 123.4
2930 PRINT USING "**$####.##"; 1234.56
2940 PRINT ""
2950 PRINT "=== Exp with different precisions ==="
2960 PRINT USING "#.#^^^^"; 123.4
2970 PRINT USING "#.##^^^^"; 123.45
2980 PRINT USING "#.###^^^^"; 123.456
2990 PRINT USING "##.#^^^^"; 1234.5
3000 PRINT USING "###.#^^^^"; 12345.6
3010 PRINT ""
3020 PRINT "=== Exp with small numbers ==="
3030 PRINT USING "##.##^^^^"; 0.00012
3040 PRINT USING "##.##^^^^"; 0.00034
3050 PRINT USING "##.##^^^^"; 0.00056
3060 PRINT USING "##.##^^^^"; 0.00789
3070 PRINT ""
3080 PRINT "=== Exp with negatives ==="
3090 PRINT USING "##.##^^^^"; -123.45
3100 PRINT USING "##.##^^^^"; -0.0123
3110 PRINT USING "+##.##^^^^"; 456.78
3120 PRINT USING "+##.##^^^^"; -789.01
3130 PRINT ""
3140 PRINT "=== String variations ==="
3150 PRINT USING "&"; "MBASIC"
3160 PRINT USING "&"; "PRINT"
3170 PRINT USING "&"; "USING"
3180 PRINT USING "&"; "FORMAT"
3190 PRINT USING "&"; "TEST"
3200 PRINT USING "!"; "FIRST"
3210 PRINT USING "!"; "SECOND"
3220 PRINT USING "!"; "THIRD"
3230 PRINT ""
3240 PRINT "=== Fixed width strings ==="
3250 PRINT USING "\  \"; "AB"
3260 PRINT USING "\  \"; "ABC"
3270 PRINT USING "\  \"; "ABCD"
3280 PRINT USING "\   \"; "TEST"
3290 PRINT USING "\   \"; "TESTS"
3300 PRINT USING "\    \"; "SHORT"
3310 PRINT USING "\    \"; "LONGER"
3320 PRINT ""
3330 PRINT "=== More overflow cases ==="
3340 PRINT USING "#"; 12
3350 PRINT USING "#"; 123
3360 PRINT USING "##"; 123
3370 PRINT USING "##"; 1234
3380 PRINT USING ".#"; 1.2
3390 PRINT USING ".##"; 1.23
3400 PRINT USING "$$#"; 12
3410 PRINT USING "**#"; 12
3420 PRINT ""
3430 PRINT "=== Test complete ==="
3440 END
