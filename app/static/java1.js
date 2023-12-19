function ffname(){
    var f=document.frm.fname.value;
    var reg=/^[A-Za-z]+$/;
    if(f=="")
    {
        document.getElementById("fname").innerHTML="Please Enter First Name"
    }
    else if(!reg.test(f))
    {
        document.getElementById("fname").innerHTML="Use only Alphabets"
    }
    else{
        document.getElementById("fname").innerHTML=""
    }
}
function lname(){
    var f=document.frm.lastname.value;
    var reg=/^[A-Za-z]+$/;
    if(f=="")
    {
        document.getElementById("lastname").innerHTML="Please Enter Last Name"
    }
    else if(!reg.test(f))
    {
        document.getElementById("lastname").innerHTML="Use only Alphabets"
    }
    else{
        document.getElementById("lastname").innerHTML=""
    }
}
function Cemail(){

    var f=document.frm.email.value
    var reg=/^[A-Za-z0-9-_.]+@[A-Za-z]+\.[A-Za-z]{2,4}$/;
    if(f=="")
			{
				document.getElementById("email").innerHTML="Please Enter Email";
			}
	else if(!reg.test(f))
			{
				document.getElementById("email").innerHTML="Please Enter Valid Email";
			}
	else
			{
				document.getElementById("email").innerHTML="";	
			}

}

function CPpassword()
		{
			var f=document.frm.password.value;
			var reg=/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/;
			if(f=="")
			{
				document.getElementById("password").innerHTML="Please Enter Password";
			}
			else if(!reg.test(f))
			{
				document.getElementById("password").innerHTML="Min 1 Digit, Upper,Lower & Special(8,15)";
			}
			else
			{
				document.getElementById("password").innerHTML="";	
			}

		}
function chpassword()
		{
			var f=document.frm.password.value;
			var g=document.frm.cpassword.value;
			if(g=="")
			{
				document.getElementById("cpassword").innerHTML="Please Enter Confirm Password";	
			}
			else if(f!=g)
			{
				document.getElementById("cpassword").innerHTML="Password and confirm Password Does Not Match";
			}
			else
			{
				document.getElementById("cpassword").innerHTML="";	
			}
			
		}