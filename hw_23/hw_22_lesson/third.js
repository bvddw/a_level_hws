const namesOfDays = {
    ru: ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота' , 'Воскресенье'],
    en: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' , 'Sunday'],
}

function weekdayToConsole (namesOfDays) {
  for (let key in namesOfDays) { // цикл для итерации по ключам, сам массив "номер дня недели - день недели" создаем без цикла
    const DaysOfWeek = namesOfDays[key].map((item, index) => `${index + 1} - ${item}`)
    console.log(DaysOfWeek.join(', '))
  }

}

weekdayToConsole(namesOfDays)
// 1 - Понедельник, 2 - Вторник, 3 - Среда, 4 - Четверг, 5 - Пятница, 6 - Суббота, 7 - Воскресенье
// 1 - Monday, 2 - Tuesday, 3 - Wednesday, 4 - Thursday, 5 - Friday, 6 - Saturday, 7 - Sunday