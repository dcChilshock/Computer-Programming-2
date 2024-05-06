// See https://aka.ms/new-console-template for more information
Console.Write("Enter Num1: ");
int n1 = int.Parse(Console.ReadLine());
Console.Write("Enter Num2: ");
int n2 = int.Parse(Console.ReadLine());
Console.Write("Choose an option: add, sub, mul, or div: ");
string op = Console.ReadLine().ToLower();
int result = 0;
if (op == "add") result = add(n1, n2);
else if (op == "sub") result = sub(n1, n2);
else if (op == "mul") result = mul(n1, n2);
else if (op == "div") result = div(n1, n2);
Console.WriteLine("Result: " + result);
wait();
// <access level> <static or not> <return type> name(<args) {}
// in console apps, well make all funcations "static"
// not static in forms apps; always "public" though
static void wait()
{
    Console.ReadLine();
    // return;
}
static int add(int x, int y)
{
    return x + y;
}
static int sub(int x, int y)
{
    return x - y;
}
static int mul(int x, int y)
{
    return x * y;
}
static int div(int x, int y)
{
    return x / y;
}

