class Validator{
    constructor (value) {
        this.toValidate = value
    }

    checkIsEmail () {
        if (this.toValidate.split('@').length !== 2) {
            return false
        }
        let userName = this.toValidate.split('@')[0]
        let domainPart = this.toValidate.split('@')[1]
        if (userName.length === 0) {
            return false
        }
        if (domainPart.split('.').length !== 2) {
            return false
        }
        let domainExtension = domainPart.split('.')[1]
        let domain = domainPart.split('.')[0]
        if (domain.length === 0 || domainExtension.length === 0) {
            return false
        }
        return true
    }

    checkIsDomain () {
        if (this.toValidate.split('.').length !== 2) {
            return false
        }
        let domain = this.toValidate.split('.')[0]
        let domainExtension = this.toValidate.split('.')[1]
        if (domain.length * domainExtension.length === 0) {
            return false
        }
        return true
    }

    checkIsDate () {
        if (this.toValidate.split('.').length !== 3) {
            return false
        }
        let dayNumber = this.toValidate.split('.')[0]
        let monthNumber = this.toValidate.split('.')[1]
        let yearNumber = this.toValidate.split('.')[2]
        if (dayNumber.length !== 2 || isNaN(Number(dayNumber))) {
            return false
        }
        if (monthNumber.length !== 2 || isNaN(Number(monthNumber))) {
            return false
        }
        if (yearNumber.length !== 4 || isNaN(Number(yearNumber))) {
            return false
        }
        dayNumber = Number(dayNumber)
        monthNumber = Number(monthNumber)
        yearNumber = Number(yearNumber)
        if (monthNumber === 1 || monthNumber === 3 || monthNumber === 5 || monthNumber === 7 || monthNumber === 8 || monthNumber === 10 || monthNumber === 12) {
            if (dayNumber < 1 || dayNumber > 31) {
                return false
            }
        }
        if (monthNumber === 4 || monthNumber === 6 || monthNumber === 9 || monthNumber === 11) {
            if (dayNumber < 1 || dayNumber > 30) {
                return false
            }
        }
        if (monthNumber === 2) {
            if (yearNumber % 4) {
                if (dayNumber < 1 || dayNumber > 28) {
                    return false
                }
            } else {
                if (dayNumber < 1 || dayNumber > 29) {
                    return false
                }
            }
        }
        return true
    }
    
    checkIsPhone () {
        if (this.toValidate.split(' ').length !== 3) {
            return false
        }
        let uaCode = this.toValidate.split(' ')[0]
        let companyCode = this.toValidate.split(' ')[1]
        let randomNumbers = this.toValidate.split(' ')[2]
        if (uaCode !== '+38') {
            return false
        }
        if (companyCode.length !== 5 || companyCode[0] !== '(' || companyCode[4] !== ')' || isNaN(Number(companyCode.slice(1, 4)))) {
            return false
        }
        if (randomNumbers.length !== 9 || randomNumbers.split('-').length !== 3) {
            return false
        }
        let firstPart = randomNumbers.split('-')[0]
        let secondPart = randomNumbers.split('-')[1]
        let thirdPart = randomNumbers.split('-')[2]
        if (firstPart.length !== 3 || isNaN(Number(firstPart))) {
            return false
        }
        if (secondPart.length !== 2 || isNaN(Number(secondPart))) {
            return false
        }
        if (thirdPart.length !== 2 || isNaN(Number(thirdPart))) {
            return false
        }
        return true
    }
}

let newEmailToCheck = new Validator('galaida.arsenii@gmail.com')
newEmailToCheck.checkIsEmail()

let newDomainToCheck = new Validator('google.com')
newDomainToCheck.checkIsDomain()

let newDateToCheck = new Validator('30.11.2019')
newDateToCheck.checkIsDate()

let newPhoneToCheck = new Validator('+38 (066) 937-99-92')
newPhoneToCheck.checkIsPhone()