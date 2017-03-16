#include <stdio.h>

void main()
{
	char pass[128];
	
	do {
	printf("Enter your password: ");
	scanf("%s", pass);

	if(strcmp(pass, "iduas3a99321*a2"))
	{
		printf("Error!!.\n");
	}
	else
	{
		printf("Ok!!.\n");
	}
	}while(1);
}
