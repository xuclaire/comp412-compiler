//NAME: Claire Xu
//NETID: ccx1
//SIM INPUT:
//OUTPUT: 0 1 1 2 3 5 8 13 21 34 55

//Fibnoacci!

loadI 0 => r0
loadI 1 => r1
add r0, r1 => r2
add r1, r2 => r3
add r2, r3 => r4
add r3, r4 => r5
add r4, r5 => r6
add r5, r6 => r7
add r6, r7 => r8
add r7, r8 => r9
add r8, r9 => r10

//Load addresses
loadI 100 => r9
loadI 104 => r10
loadI 108 => r11
loadI 112 => r12
loadI 116 => r13
loadI 120 => r14
loadI 124 => r15
loadI 128 => r16
loadI 132 => r17
loadI 136 => r18
loadI 140 => r19

store r0 => r9
store r1 => r10
store r2 => r11
store r3 => r12
store r4 => r13
store r5 => r14
store r6 => r15
store r7 => r16
store r8 => r17
store r9 => r18
store r10 => r19

output 100
output 104
output 108
output 112
output 116
output 120
output 124
output 128
output 132
output 136
output 140



