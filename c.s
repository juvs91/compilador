int a;
int b;
float f;

void uno(int a) {
    a = a + b * a;
    print(a, b, a + b);
}

void dos(int a, int b, float g) {
    int i;
    i = b;
    loop(i > 0) {
        a = a + b * i + b;
        uno(i * 2);
        print(a);
        i = i - 1;
    };
}

main() {
    a = 3;
    b = a + 1;
    print(a, b);
    f = 3.14;
    dos(a + b * 2, b, f * 3); 
	a = uno(1) + uno(1);
    print(a, b, f * 2 + 1);
}