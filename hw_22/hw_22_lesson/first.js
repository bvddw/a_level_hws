const citiesAndCountries = {
	'Киев': 'Украина',
	'Вашингтон': 'США',
	'Амстердам': 'Нидерланды',
	'Берлин': 'Германия',
	'Париж': 'Франция',
	'Лиссабон': 'Португалия',
	'Вена': 'Австрия',
};

let result = []
for (let key in citiesAndCountries) {
  result.push(`${key} - это ${citiesAndCountries[key]}`)
}
console.log(result)
// (7) ['Киев - это Украина', 'Вашингтон - это США', 'Амстердам - это Нидерланды', 'Берлин - это Германия', 'Париж - это Франция', 'Лиссабон - это Португалия', 'Вена - это Австрия']