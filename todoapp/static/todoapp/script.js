console.log('hello')

//let inputEle = document.querySelector(".input");
//let submitEle = document.querySelector(".add");
//let tasksDiv = document.querySelector(".tasks")
//let containerDiv = document.querySelector(".container")
//let deleteAll = document.querySelector(".delete-all");
//let arrayOfTasks =[];
// console.log(inputEle)
//console.log(inForm)
//console.log(inTitle)
//console.log(inDescription)
//console.log(inDeadline)
//console.log(inSubmit)

let inForm = document.getElementById('inform')
let inTitle = document.getElementById('intitle')
let inDescription = document.getElementById('indescription')
let inDeadline = document.getElementById('indeadline')
let inSubmit = document.getElementById('insubmit')
let DellAll =  document.getElementById('deleteall')

inSubmit.addEventListener('click', function(event) {
   if (inTitle.value === '' || inDescription.value === '' || inDeadline.value === '' ) {
   event.preventDefault()
   alert('Please fill out all the lines')
   }
   console.log('Check Event')
})

DellAll.addEventListener('click', function(event) {
   if (confirm('Are you sure?') === false) {
       event.preventDefault()
   }
})

