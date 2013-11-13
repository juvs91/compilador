int fact(int n) {
    if(n == 1) {
        return n;
    } else {
        return n * fact(n - 1);
    };
}

main() {
    int a;
    a = fact(12);  
	rt(30+5);
	fw(a);
    print(a);
}