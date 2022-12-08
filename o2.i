loadI 1024 => r4
loadI 8 => r3
store r3 => r4
loadI 1028 => r2
loadI 16 => r1
store r1 => r2
add r4, r3 => r0
store r1 => r0
mult r1, r3 => r1
loadI 32768 => r4
store r1 => r4
loadI 1032 => r1
loadI 32772 => r4
store r1 => r4
loadI 1036 => r1
loadI 32776 => r4
store r1 => r4
loadI 1040 => r1
store r3 => r1
store r3 => r0
loadI 32768 => r4
load r4 => r1
store r1 => r0
load r4 => r0
loadI 32780 => r4
store r1 => r4
load r2 => r1
mult r0, r1 => r1
loadI 32780 => r4
load r4 => r0
store r0 => r2
store r0 => r4
store r3 => r2
loadI 32772 => r4
load r4 => r2
store r1 => r2
loadI 32776 => r4
load r4 => r4
store r1 => r4
store r3 => r2
store r3 => r4
output 1024
output 1028
output 1036
output 1040
