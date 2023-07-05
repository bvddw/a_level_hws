// первый способ
// рекурсивная функция
let i = 1;

function fizBuz() {
  if (!(i % 3)) {
        console.log('FizBuz')
    } else if (!(i % 2)) {
        console.log('Fiz')
    } else {
        console.log('Buz')
    }

  i++;

  if (i <= 10) {
    fizBuz();
  }
}

fizBuz();

// второй способ
// map к массиву
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

const result = numbers.map((i) => {
  if (!(i % 3)) {
      console.log('FizBuz')
  } else if (!(i % 2)) {
      console.log('Fiz')
  } else {
      console.log('Buz')
  }
});