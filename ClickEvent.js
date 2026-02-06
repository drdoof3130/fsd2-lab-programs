let count = 0;
document.getElementById("countBtn").
addEventListener("click" ,() =>
    {
        count++;
        document.getElementById("count").innerText = count;
    }
);