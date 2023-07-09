const studentArr = [{
        name: 'Сергей',
        surname: 'Войлов',
        ratingPoint: 1000,
        schoolPoint: 1000,
        course: 2,
    },
    {
        name: 'Татьяна',
        surname: 'Коваленко',
        ratingPoint: 880,
        schoolPoint: 700,
        course: 1,
    },
    {
        name: 'Анна',
        surname: 'Кугир',
        ratingPoint: 1430,
        schoolPoint: 1200,
        course: 3,
    },
    {
        name: 'Станислав',
        surname: 'Щелоков',
        ratingPoint: 1130,
        schoolPoint: 1060,
        course: 2,
    },
    {
        name: 'Денис',
        surname: 'Хрущ',
        ratingPoint: 1000,
        schoolPoint: 990,
        course: 4,
    },
    {
        name: 'Татьяна',
        surname: 'Капустник',
        ratingPoint: 650,
        schoolPoint: 500,
        course: 3,
    },
    {
        name: 'Максим',
        surname: 'Меженский',
        ratingPoint: 990,
        schoolPoint: 1100,
        course: 1,
    },
    {
        name: 'Денис',
        surname: 'Марченко',
        ratingPoint: 570,
        schoolPoint: 1300,
        course: 4,
    },
    {
        name: 'Антон',
        surname: 'Завадский',
        ratingPoint: 1090,
        schoolPoint: 1010,
        course: 3
    },
    {
        name: 'Игорь',
        surname: 'Куштым',
        ratingPoint: 870,
        schoolPoint: 790,
        course: 1,
    },
    {
        name: 'Инна',
        surname: 'Скакунова',
        ratingPoint: 1560,
        schoolPoint: 200,
        course: 2,
    },
];





class Student {
    static students = []; // array of students
    constructor({ name, surname, ratingPoint, schoolPoint, course}) {
        this.id = Student.students.length + 1; // adding id for each student
        this.name = name;
        this.surname = surname;
        this.ratingPoint = ratingPoint;
        this.schoolPoint = schoolPoint;
        this.course = course
        this.isSelfPayment = undefined
        Student.students.push(this); // push each student into array of students
    }

    static listOfStudents() { // return array of students
        return Student.students;
    }

    set selfPayment (value) {
        this.isSelfPayment = value
    }
}

// function that will create array of students, where each student is obj of Student from array of default objects
const createStudentsArr = (arr) => arr.map(item => new Student(item))
createStudentsArr(studentArr)

// take list of student from class Student
const students = Student.listOfStudents();

// sort by Points for realize the easiest way to determine self payment for each student
const sortByPoints = (arr) => {
    return arr.sort((student1, student2) => {
        if (student1.ratingPoint > student2.ratingPoint) {
            return -1
        }
        if (student1.ratingPoint < student2.ratingPoint) {
            return 1
        }
        if (student1.schoolPoint > student2.schoolPoint) {
            return -1
        }
        if (student1.schoolPoint < student2.schoolPoint) {
            return 1
        }
        return 0
    })
}

// sort by id for make default view of students list
const sortById = (arr) => {
    return arr.sort((student1, student2) => {
        if (student1.id > student2.id) {
            return 1
        }
        if (student1.id < student2.id) {
            return -1
        }
        return 0
    })
}

// function that will determine Self Payment for each student by given rules
function setSelfPayment (arr) {
    sortByPoints(arr)
    for (let index in arr) {
        arr[index].isSelfPayment = !(index < 5 && arr[index].ratingPoint >= 800);
    }
    sortById(arr)
}
setSelfPayment(students)
Student.listOfStudents()