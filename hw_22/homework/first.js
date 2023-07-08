function fizBuz(number) {
    for (let i = 1; i < number + 1; i++) {
        if (!(i % 3)) {
            console.log('FizBuz')
        } else if (!(i % 2)) {
            console.log('Fiz')
        } else {
            console.log('Buz')
        }
    }
}

/*
fizBuz(12)
Buz
Fiz
FizBuz
Fiz
Buz
FizBuz
Buz
Fiz
FizBuz
Fiz
Buz
FizBuz
 */