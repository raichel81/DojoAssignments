
function printFullName(students){
    for (var student in students){
        console.log(students[student].first_name + " " + students[student].last_name);
    }
}

printFullName([ 
     {first_name: 'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
]);