const emplyeeArr = [
    {
        id: 1,
        name: 'Денис',
        surname: 'Хрущ',
        salary: 1010,
        workExperience: 10, /// стаж работы (1 = один месяц)
        isPrivileges: false, /// льготы
        gender: 'male'
    },
    {
        id: 2,
        name: 'Сергей',
        surname: 'Войлов',
        salary: 1200,
        workExperience: 12, /// стаж работы (1 = один месяц)
        isPrivileges: false, /// льготы
        gender: 'male'
    },
    {
        id: 3,
        name: 'Татьяна',
        surname: 'Коваленко',
        salary: 480,
        workExperience: 3, /// стаж работы (1 = один месяц)
        isPrivileges: true, /// льготы
        gender: 'female'
    },
    {
        id: 4,
        name: 'Анна',
        surname: 'Кугир',
        salary: 2430,
        workExperience: 20, /// стаж работы (1 = один месяц)
        isPrivileges: false, /// льготы
        gender: 'female'
    },
    {
        id: 5,
        name: 'Татьяна',
        surname: 'Капустник',
        salary: 3150,
        workExperience: 30, /// стаж работы (1 = один месяц)
        isPrivileges: true, /// льготы
        gender: 'female'
    },
    {
        id: 6,
        name: 'Станислав',
        surname: 'Щелоков',
        salary: 1730,
        workExperience: 15, /// стаж работы (1 = один месяц)
        isPrivileges: false, /// льготы
        gender: 'male'
    },
    {
        id: 7,
        name: 'Денис',
        surname: 'Марченко',
        salary: 5730,
        workExperience: 45, /// стаж работы (1 = один месяц)
        isPrivileges: true, /// льготы
        gender: 'male'
    },
    {
        id: 8,
        name: 'Максим',
        surname: 'Меженский',
        salary: 4190,
        workExperience: 39, /// стаж работы (1 = один месяц)
        isPrivileges: false, /// льготы
        gender: 'male'
    },
    {
        id: 9,
        name: 'Антон',
        surname: 'Завадский',
        salary: 790,
        workExperience: 7, /// стаж работы (1 = один месяц)
        isPrivileges: false, /// льготы
        gender: 'male'
    },
    {
        id: 10,
        name: 'Инна',
        surname: 'Скакунова',
        salary: 5260,
        workExperience: 49, /// стаж работы (1 = один месяц)
        isPrivileges: true, /// льготы
        gender: 'female'
    },
    {
        id: 11,
        name: 'Игорь',
        surname: 'Куштым',
        salary: 300,
        workExperience: 1, /// стаж работы (1 = один месяц)
        isPrivileges: false, /// льготы
        gender: 'male'
    },
];



class Employee {
    // 1
    constructor ({id, name, surname, salary, workExperience, isPrivileges, gender}) {
        this.id = id
        this.name = name
        this.surname = surname
        this.salary = salary
        this.workExperience = workExperience
        this.isPrivileges = isPrivileges
        this.gender = gender
    }

    // 2
    getFullName() {
        return this.name + ' ' + this.surname
    }

    // 7
    get fullInfo () {
        return {
            id: this.id,
            name: this.name,
            surname: this.surname,
            salary: this.salary,
            workExperience: this.workExperience,
            isPrivileges: this.isPrivileges,
            gender: this.gender
        }
    }

    // 7
    set fullInfo (values) {
        for (let item in values) {
            this[item] = values[item]
        }
    }
}

// 3
let createEmployeesFromArr = (arr) => {
    return arr.map(item => new Employee(item))
}
const employeeConstructArr = createEmployeesFromArr(emplyeeArr)

// 4
const getFullNamesFromArr = (arr) => {
    return arr.map(item => {
        const person = new Employee(item)
        return person.getFullName()
    } )
}
getFullNamesFromArr(employeeConstructArr)

// 5
const getMiddleSalary = (arr) => {
    return arr.reduce((acc, item) => acc + item.salary, 0) / arr.length
}
getMiddleSalary(employeeConstructArr)

// 6
const getRandomEmployee = (arr) => {
    return arr[Math.ceil(Math.random() * arr.length) - 1]
}
getRandomEmployee(employeeConstructArr)

// 7
let objEmployee = new Employee({id: 12, name: 'Arsenii', surname: 'Galaida', salary: 1000, workExperience: 12, isPrivileges: false, gender: 'male'})
objEmployee.fullInfo
objEmployee.fullInfo = {salary: 900, workExperience: 13}