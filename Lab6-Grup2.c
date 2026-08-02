#include <stdio.h>

void find_min_max(int array[],int size,int *minptr,int *maxptr)
{
	for(int i=0;i<size;++i)
	{
		if (array[i]<*minptr)
		{
			minptr=&array[i];
		}
		if (array[i]>*maxptr)
		{
			maxptr=&array[i];
		}
	}
	printf("%d %d",*minptr,*maxptr);
}

int main() 
{
	int size;
	scanf("%d",&size);
	int array[size];
	int *minptr=array;
	int *maxptr=array;
	int number;
	for(int i=0;i<size;++i)
	{
		scanf("%d",&number);
		array[i]=number;
	}
	find_min_max(array,size,minptr,maxptr);
}

