#

Every C programs has 4 components.
* Heap
* Stack
* Registers
* Instructions

There are two main archecture which dictates how a program is run and executed.
1- 32-bit
2- 64-bit

## The Heap
The heap is an area in memory designed for the purpose of manual memory allocation.
memory is allocated on the heap when ever functions like:
malloc - calloc - global - static 

## Registers
registers are small storage area in the processors, they can be used to store memory addresses, values or anythings that can be represented in 8 bytes or less

## The Stack
the stack is a data structure comprised of elements which can be added or removed with only two operations, "push" or "pop"
- Push adds an element to the top of the stack
- Pop removes the top element from stack
each element on the stack is assigned a stack address.
elements that are higher on the stack have lower address than those at the bottom of the stack. 
The stack grows towards lower address memory

## Instructions
The instruction has two parts.
* Operations
* Arguments 
Every operations can take two arguments which is seperated with a comma.
The move operations takes arg2 and moves it to arg1
[ mov arg1, arg2 ]

The add opeerations takes the two arguments and stores it in the first arg1.
[ add arg1, arg2 ]

The sub operations acts in the same way but this time arg2 is subtracted from arg1.
[ sub arg1, arg2 ]

The compared
[ cmp arg1, arg2 ]

Push

Pop

Lea
