class TestMethod{
	public static void main(String[] args) {
		TestMethod TestMethod =new TestMethod();
		TestMethod.sample1();
		TestMethod.sample2("Viren More");
		System.out.println(TestMethod.sample3());
		float result=TestMethod.sample4(20,30);
		System.out.println(result);	
		
	}
	// 1)method with no parameters no return value
	public void sample1(){
		System.out.println("this is no paramter and no return");
	}
	//method with paramter and no return value
	public void sample2(String name){
		System.out.println(name);
	}
	//method with no paramters but return value
	public int sample3(){
		int no1=10;int no2=20;
		return no1*no2;
	}
	// 4)method with paramters and return value
	public float sample4(int m,int n){
		return m-n;
	}
}