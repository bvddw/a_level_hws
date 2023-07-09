class CustomString{
    constructor (value) {
        this.mystr = value
    }

    // method to reverse string
    customReverse () {
        let result = ''
        for (let index in this.mystr) {
            result += this.mystr[this.mystr.length - index - 1]
        }
        return result
    }

    // capitalize first character of the first word
    customUcFirst () {
        return this.mystr.charAt(0).toUpperCase() + this.mystr.slice(1)
    }

    // capitalize first character of each word
    customUcWords () {
        return this.mystr.split(' ').map(item => {
            return (new CustomString(item)).customUcFirst()
        }).join(' ')
    }
}

const str = new CustomString('hello world')
str.customReverse()
str.customUcFirst()
str.customUcWords()