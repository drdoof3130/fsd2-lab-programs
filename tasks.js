let result = 0;
let n1 = Number(prompt("Enter number 1"));
let n2 = Number(prompt("Enter number 2"));
document.getElementById("addbtn").
addEventListener("click" , function add()
    {
        result=n1+n2;
        document.getElementById("result").innerText = result;
    }
);

document.getElementById("subbtn").
addEventListener("click" , function sub()
    {
        result=n1-n2;
        document.getElementById("result").innerText = result;
    }
);

document.getElementById("mulbtn").
addEventListener("click" , function mul()
    {
        result=n1*n2;
        document.getElementById("result").innerText = result;
    }
);

document.getElementById(" divbtn").
addEventListener("click" , function div()
    {
        result=n1/n2;
        document.getElementById("result").innerText = result;
    }
);