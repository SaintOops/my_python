#include <math.h>
#include <stdio.h>


int Catalan_numbers(int n) {
	if (n != 0)
		return  Catalan_numbers(n - 1) * 2 * (2 * n - 1) / (n + 1);
	else
		return 1;
}

int fibonacci(int n) {
	if (n == 0) {
		return 0;
	}
	else if (n == 1) {
		return 1;
	}
	else {
		return fibonacci(n - 1) + fibonacci(n - 2);
	}
}

int factorial(int n) {
	return (n < 2) ? 1 : n * factorial(n - 1);
}

int binomial(int n, int k ){
	if (n>0 && k>=0 && n>k){return factorial(n)/(factorial(n-k)* factorial(k));}
	else {return 0;}
}

double n_length(int n, double r, double a){
	if (n<3){return 0;}
	else {return sqrt(2*r*r-2*r*sqrt(r*r-a*a/4));}
}

double binom(double a, double b, int n)
{
	double sum=0;
	for(int i=0; i<n+1; i=i+1){sum+=binomial(n,i)*pow(a,n-i)*pow(b,i);}
	return sum;
} 


int subfactorial(int n) {
	double a = 0;
	for (int k = 0; k <n+1; k=k+1) {
	a+=(pow(-1,k)/factorial(k));
	}
	return a*factorial(n);
}

int doubfactorial(int n) {
	if(n%2==0){return pow(2,n/2)*factorial(n/2);}
	else {return factorial(n)/(pow(2,(n-1)/2)*factorial((n-1)/2));}
}
