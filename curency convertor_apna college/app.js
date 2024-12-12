let base_URL =
  "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies";
let dropdowns = document.querySelectorAll(".dropdown select");
let amount = document.querySelector("input");
let but = document.querySelector(" form button");
let fromCurr = document.querySelector(".from select");
let toCurr = document.querySelector(".to select");
let msg= document.querySelector(".msg");

const updateFlag = (Element) => {
  let curr_code = Element.value;
  // console.log(curr_code);
  let countrycode = countryList[curr_code];
  console.log(countrycode);
  let newsrc = `https://flagsapi.com/${countrycode}/flat/64.png`;
  let img = Element.parentElement.querySelector("img");
  img.src = newsrc;
};
for (let select of dropdowns) {
  for (let curr_code in countryList) {
    let newoption = document.createElement("option");
    newoption.innerText = curr_code;
    newoption.value = curr_code;
    if (select.name === "from" && curr_code === "USD") {
      newoption.selected = "selected";
    } else if (select.name === "to" && curr_code === "PKR") {
      newoption.selected = "selected";
    }
    select.append(newoption);
  }

  select.addEventListener("change", (evt) => {
    updateFlag(evt.target);
  });
}
but.addEventListener("click", async (evt) => {
  evt.preventDefault();
  let amount = document.querySelector(".amount input");
  let amountValue = amount.value;
  if (amountValue === "" || amountValue <= 0) {
    amountValue = 1;
    amount.value = "1";
  }
  console.log(fromCurr);
  const URL = `${base_URL}/${fromCurr.value.toLowerCase()}.json`;
  console.log(URL);
  const fromValue = fromCurr.value.toLowerCase()
  let response = await fetch(URL);

  const data = await response.json();
  console.log(data)
  console.log(data[fromValue]); 
  console.log(data[fromValue][toCurr.value.toLowerCase()]);
// console.log(amount.value)
console.log(fromCurr.value)
let rup=Math.round((amount.value*data[fromValue][toCurr.value.toLowerCase()]))
console.log(rup)
const updatemsg=()=>{
  msg . innerHTML=`${amount.value} ${fromCurr.value} = ${rup}  ${toCurr.value}`
}
updatemsg();

});
// data()