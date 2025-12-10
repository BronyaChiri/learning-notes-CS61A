#include<stdio.h>
double sumn(int n);
double cache[10000000] = {};
int main()
{int i=1;
double t=0, num = 0;
scanf("%lf",&num);
for(i=1;t<=num;i++)
{t = sumn(i);

}
printf("%d",i-1);


    return 0;
}
double sumn(int n)
{if(n==1) return 1;
 else if (cache[n]!=0) return cache[n];
 else {cache[n]=(1/((double)(n))+sumn(n-1));
 return cache[n];}
}