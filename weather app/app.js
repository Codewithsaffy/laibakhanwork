let Base_Url = `https://api.weatherapi.com/v1/current.json?key=84a9c6a0dc6848d590b174213241002&q=`;
let search = document.querySelector(".search-bar");
let cityname = document.querySelector(".city");
let temp = document.querySelector(".temp");
let humidity = document.querySelector(".humidity");
let wind = document.querySelector(".wind");
let searchbtn = document.querySelector(".search button");

async function weather() {
  let response = await fetch(Base_Url + `${"" + search.value + ""}&aqi=no`);
  let data = await response.json();
  temp.innerText = data.current.temp_c + "°C";
  cityname.innerText = data.location.name;
  humidity.innerText = data.current.humidity + "%";
  wind.innerText = data.current.wind_kph + "km/h";
}
searchbtn.addEventListener("click", () => {
  weather(search.value);
});

search.addEventListener("keyup", (event) => {
  if (event.key === "Enter") {
    weather(search.value);
  }
});
