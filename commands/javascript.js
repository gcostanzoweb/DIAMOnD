//Get node names and GDA score

table = document.querySelector("tbody")
rows = table.querySelectorAll("tr.odd, tr.even")
string=""
for(let i = 0; i < 111; i++){
row = rows[i].querySelectorAll("td:not(.text-right):not(.no-drag)")

string+=(row[0].querySelector("a span").textContent+" "+row[8].textContent+"\n")
}