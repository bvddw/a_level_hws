function pyramid(medianNumber) {
    for (let i = 0; i < medianNumber; i++) {
        let current_row = ''
        let number_of_sharps = i * 2 + 1
        let number_of_dash = medianNumber - i - 1
        for (let j = 0; j < number_of_dash; j++) {
            current_row += '-'
        }
        for (let j = 0; j < number_of_sharps; j++) {
            current_row += '#'
        }
        for (let j = 0; j < number_of_dash; j++) {
            current_row += '-'
        }
        current_row += ` //${i + 1}`
        console.log(current_row)
    }
}

/*
pyramid(12)
-----------#----------- //1
----------###---------- //2
---------#####--------- //3
--------#######-------- //4
-------#########------- //5
------###########------ //6
-----#############----- //7
----###############---- //8
---#################--- //9
--###################-- //10
-#####################- //11
####################### //12
 */