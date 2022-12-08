// COMP 412 Reference Allocator (2022-1-0), k = 7
loadI  2000 => r0             // rematerialize vr14 => pr0
load   r0 => r0               // Mem[vr14] => vr6
loadI  2000 => r1             // rematerialize vr13 => pr1
load   r1 => r1               // Mem[vr13] => vr10
add    r0, r0  => r2          // vr6, vr6 => vr11
loadI  1 => r3                // rematerialize vr12 => pr3
add    r1, r3  => r3          // vr10, vr12 => vr8
loadI  2004 => r4             // rematerialize vr2 => pr4
store  r2 => r4               // vr11 => Mem[vr2]
loadI  2008 => r5             // rematerialize vr0 => pr5
store  r3 => r5               // vr8 => Mem[vr0]
add    r0, r2  => r2          // vr6, vr11 => vr9
add    r1, r3  => r1          // vr10, vr8 => vr4
store  r2 => r4               // vr9 => Mem[vr2]
store  r1 => r5               // vr4 => Mem[vr0]
add    r0, r2  => r2          // vr6, vr9 => vr7
add    r3, r1  => r3          // vr8, vr4 => vr5
store  r2 => r4               // vr7 => Mem[vr2]
store  r3 => r5               // vr5 => Mem[vr0]
add    r0, r2  => r2          // vr6, vr7 => vr3
add    r1, r3  => r3          // vr4, vr5 => vr1
store  r2 => r4               // vr3 => Mem[vr2]
store  r3 => r5               // vr1 => Mem[vr0]
output 2004                   // as in the input
output 2008                   // as in the input
