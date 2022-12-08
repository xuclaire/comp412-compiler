loadI 2000 => r5
loadI 2000 => r4
load r5 => r5
load r4 => r4
loadI 2004 => r3
loadI 2008 => r2
loadI 1 => r1
add r5, r5 => r0
add r4, r1 => r1
store r0 => r3
store r1 => r2
add r5, r0 => r0
add r4, r1 => r4
store r0 => r3
store r4 => r2
add r5, r0 => r0
add r1, r4 => r1
store r0 => r3
store r1 => r2
add r5, r0 => r0
add r4, r1 => r1
store r0 => r3
store r1 => r2
output 2004
output 2008
