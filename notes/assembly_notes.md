#

Every C programs has 4 components.
1- Heap
2- Stack
3- Registers
4- Instructions

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
>>> Push adds an element to the top of the stack
>>> Pop removes the top element from stack
each element on the stack is assigned a stack address.
elements that are higher on the stack have lower address than those at the bottom of the stack. 
The stack grows towards lower address memory 
