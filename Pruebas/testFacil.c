program alone;
var int a, b, c; 

function int add(int op1, op2)
var int res;
{
	res = op1 + op2;
	return res;
}

function void subs(int op1, op2)
var int res;
{
	res = op1 - op2;
	print(res);
}

main()
var int j, k, l, iterator;
{
	k = 25;
	l = 12;
	read(j);
	subs(k, l);
	add(10, 1);
	if(j > k || k < l) then{
		print("True");
	} else {
		print("False");
		j = l + k;
	}
		
	while(iterator < 10){
		iterator = iterator + 1;
	}
	print("thanks");
}
end