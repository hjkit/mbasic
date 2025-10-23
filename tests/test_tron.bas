10 REM Test TRON/TROFF trace execution
20 PRINT "Starting program"
30 K = 10
40 PRINT "Before TRON"
50 TRON
60 PRINT "After TRON - trace is now ON"
70 FOR J = 1 TO 2
80 L = K + 10
90 PRINT "J="; J; " K="; K; " L="; L
100 K = K + 10
110 NEXT J
120 PRINT "Before TROFF"
130 TROFF
140 PRINT "After TROFF - trace is now OFF"
150 PRINT "This line should NOT show trace"
160 PRINT "End of program"
170 END
